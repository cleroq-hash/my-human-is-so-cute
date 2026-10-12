#!/usr/bin/env python3
"""Stop hook: after every turn of a cloud session, commit and push a short list of files.

Why every turn, not at the end: a cloud session runs in a throwaway container that gets
reclaimed when idle. Whatever isn't pushed is destroyed with it — there's no "next time"
to catch up. On your own PC the disk survives, so this hook does nothing there.

Why a short list and not everything: a hook that sweeps up every file will one day push
something that had no business leaving. Same reason as never using `git add -A`.

It never blocks the session: any problem exits with code 0. A sync hook that breaks the
session is worse than no sync hook. A rebase conflict is reported to you, and nothing is
pushed — deciding between two versions of a file is your call, not a script's.
"""
import json
import os
import subprocess
import sys

# The only paths this hook may commit. Edit to match your repository.
ALLOWED = [
    "projects/",
    "notes/",
]

MESSAGE = "chore(sync): work from a cloud session"


def git(*args, cwd):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True,
                          timeout=30)


def main():
    # Claude Code on the web sets CLAUDE_CODE_REMOTE. On your PC it's absent: do nothing.
    if os.environ.get("CLAUDE_CODE_REMOTE") != "true":
        return 0
    sys.stdin.read()  # the hook's JSON input; not needed here

    repo = os.environ.get("CLAUDE_PROJECT_DIR")
    if not repo or not os.path.isdir(os.path.join(repo, ".git")):
        return 0

    present = [p for p in ALLOWED if os.path.exists(os.path.join(repo, p))]
    if not present:
        return 0
    git("add", "--", *present, cwd=repo)
    if git("diff", "--cached", "--quiet", cwd=repo).returncode == 0:
        return 0  # nothing changed this turn
    git("commit", "-q", "-m", MESSAGE, "--", *present, cwd=repo)

    branch = git("rev-parse", "--abbrev-ref", "HEAD", cwd=repo).stdout.strip()
    if not branch or branch == "HEAD":
        return 0
    if git("push", "-q", "origin", branch, cwd=repo).returncode:
        # Someone else pushed in the meantime. A trivial catch-up is fine.
        if git("pull", "-q", "--rebase", "origin", branch, cwd=repo).returncode:
            git("rebase", "--abort", cwd=repo)
            print(json.dumps({"systemMessage":
                f"Sync hook: conflict on {branch}, nothing pushed. Resolve it by hand."}))
            return 0
        git("push", "-q", "origin", branch, cwd=repo)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)

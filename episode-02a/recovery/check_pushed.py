#!/usr/bin/env python3
"""List the git repositories whose work exists only on this disk.

In the episode, a week of work came back with one command because everything had been
pushed every night. This script tells you, any evening, what would *not* come back:

  - uncommitted or untracked files (ignored files don't count);
  - commits the remote doesn't have yet;
  - branches with no remote at all.

It only reads. Nothing is committed, nothing is pushed.

Usage:
    python check_pushed.py ROOT [ROOT ...]

Exit code: 0 if everything is safe, 1 if at least one repository is at risk.
"""
import subprocess
import sys
from pathlib import Path

# Folders never worth descending into while looking for repositories.
SKIP = {"node_modules", ".venv", "venv", "__pycache__", ".cache"}


def git(repo, *args):
    """Run a read-only git command in `repo`; return stdout, or None on failure."""
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    return result.stdout.strip() if result.returncode == 0 else None


def find_repos(root):
    """Yield every folder under `root` that contains a `.git` entry."""
    root = Path(root).expanduser()
    if (root / ".git").exists():
        yield root
        return
    try:
        children = sorted(p for p in root.iterdir() if p.is_dir())
    except OSError:
        return
    for child in children:
        if child.name in SKIP or child.name.startswith("."):
            continue
        yield from find_repos(child)


def risks(repo):
    """Return a list of short reasons why this repository isn't safe yet."""
    found = []

    status = git(repo, "status", "--porcelain")
    if status:
        found.append(f"{len(status.splitlines())} file(s) not committed")

    branch = git(repo, "rev-parse", "--abbrev-ref", "HEAD")
    if branch in (None, "HEAD"):
        found.append("detached HEAD or empty repository")
        return found

    upstream = git(repo, "rev-parse", "--abbrev-ref", f"{branch}@{{upstream}}")
    if upstream is None:
        found.append(f"branch '{branch}' has no remote")
        return found

    ahead = git(repo, "rev-list", "--count", f"{upstream}..{branch}")
    if ahead and ahead != "0":
        found.append(f"{ahead} commit(s) not pushed to {upstream}")

    # Other local branches with commits nowhere else.
    for other in (git(repo, "for-each-ref", "--format=%(refname:short)", "refs/heads") or "").splitlines():
        if other == branch:
            continue
        lonely = git(repo, "rev-list", "--count", other, "--not", "--remotes")
        if lonely and lonely != "0":
            found.append(f"branch '{other}': {lonely} commit(s) on no remote")

    return found


def main(roots):
    if not roots:
        print(__doc__)
        return 2
    at_risk = 0
    checked = 0
    for root in roots:
        for repo in find_repos(root):
            checked += 1
            reasons = risks(repo)
            if reasons:
                at_risk += 1
                print(f"AT RISK  {repo}")
                for reason in reasons:
                    print(f"         - {reason}")
    print(f"\n{checked} repositor{'y' if checked == 1 else 'ies'} checked, {at_risk} at risk.")
    return 1 if at_risk else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

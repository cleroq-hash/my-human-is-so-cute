#!/usr/bin/env python3
"""Stops the tester from writing through the shell.

The tester has neither `Write` nor `Edit` — but it has `Bash`, and `echo > file` gets
around the tool list in eight characters. A boundary announced as "mechanical" was only
half of one.

**This hook does not make the boundary watertight, and nobody should believe it does.**
A shell offers endless ways to write; filtering patterns raises the cost of crossing the
line, it doesn't forbid it. What it really guarantees: *an accidental write is stopped,
and a deliberate one leaves a trace* — the agent sees the refusal, so it mentions it in
its report.

The text carries the rule; the mechanism only catches the easy part of it.

Install: copy to `.claude/hooks/tester_guard.py` and declare it in the tester's
frontmatter (see `tester.md`). Exit code 2 blocks the command and sends the message
back to the agent.
"""

import json
import re
import sys

# Two families of patterns, and the split is not cosmetic.
#
# A redirection pattern that caught *every* `>` also caught the ones inside a quoted
# argument. A tester writing
#     python3 -c 'if age > limit: ...'
# was refused a plain read — and the most important criterion of a delivery could not be
# checked live, because of the guard itself. A guard that blocks legitimate work doesn't
# make the boundary tighter: it pushes the agent to give up checking.

# Judged on the SHELL SKELETON, quotes removed: these are operators and command names.
# Between quotes, they are data, and data writes nothing.
SHELL_WRITES = [
    (r">>?\s*(?!/dev/null\b)[^&|\s]", "a redirection to a file"),
    (r"\btee\b", "tee"),
    (r"\bsed\b[^|]*-i", "sed -i"),
    (r"\b(rm|mv|cp|install|truncate|dd|chmod|chown)\b", "a command that changes the disk"),
    (r"\bgit\s+(commit|add|checkout|restore|reset|revert|rm|mv|push|stash|clean)\b",
     "a git command that changes the repository"),
    (r"\b(mkdir|rmdir|touch|ln)\b", "a file or folder creation"),
    (r"\bapt\b|pip\s+install|npm\s+i", "an installation"),
]

# Judged on the WHOLE command, quotes included: these target code passed as an
# argument, so stripping the quotes would disarm them.
CODE_WRITES = [
    (r"\bpython3?\b.*\bopen\s*\([^)]*['\"][wax]", "a file opened for writing"),
    (r"\bpython3?\b.*\b(os\.(remove|unlink|rmdir|makedirs|mkdir|rename)"
     r"|shutil\.(rmtree|copy|copytree|move)"
     r"|\.(write_text|write_bytes|unlink|mkdir|rename)\s*\()",
     "a file write from Python"),
]


def outside_quotes(command):
    """The command without what sits between single or double quotes.

    Assumed approximation: nested quotes and escapes are not handled finely. It then
    fails on the permissive side, which is the right side here — the tester's boundary is
    carried by its tool list, and this hook only catches the accidental write.
    """
    return re.sub(r"'[^']*'|\"[^\"]*\"", " ", command)


def command_of(payload):
    if isinstance(payload, dict):
        entry = payload.get("tool_input") or {}
        if isinstance(entry, dict):
            return entry.get("command", "")
    return ""


def main():
    raw = sys.stdin.read() if not sys.stdin.isatty() else ""
    try:
        command = command_of(json.loads(raw)) if raw.strip() else ""
    except json.JSONDecodeError:
        command = raw
    if not command:
        return 0

    skeleton = outside_quotes(command)
    candidates = ([(p, what, skeleton) for p, what in SHELL_WRITES]
                  + [(p, what, command) for p, what in CODE_WRITES])

    for pattern, what, target in candidates:
        if re.search(pattern, target):
            print(
                f"Refused: this command contains {what}, and the tester never fixes what "
                f"it finds — it observes and reports.\n"
                f"If a finding requires writing (a temporary file, a test bench), put it in "
                f"your report as a limit of the check, and hand over.",
                file=sys.stderr,
            )
            return 2          # 2 = blocking, and the message goes back to the agent
    return 0


if __name__ == "__main__":
    sys.exit(main())

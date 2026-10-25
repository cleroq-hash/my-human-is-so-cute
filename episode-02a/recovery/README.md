# Recovery — what survives when the disk doesn't

One evening, Sam's computer went back in time. A full-machine backup, a week old, was put
back in place over everything. Kernel rules, hooks, scripts, notes: a week of work looked
gone.

It came back with one command per repository, because every evening, everything had been
pushed to GitHub. GitHub keeps every version, in order, on someone else's disk. A `git
clone` or a `git pull` and the week was back — down to the work sent up at ten to
midnight the night before.

What was really lost: the conversations. A week of talking with the AI. And for the AI,
that changed nothing — it didn't remember them anyway.

## The question to ask about your own assistant

If your assistant remembers you all on its own, inside its own product, ask: **the day it
forgets, what's left?**

What survived for Sam was everything that had been written down, filed, and pushed:
everything someone had *chosen* to keep. What went away was the clutter — the junk drawer.
A memory you can't read is a memory you can't recover, fix, or move.

## The two files

| File | When to use it |
|---|---|
| [`check_pushed.py`](check_pushed.py) | Any evening, or from a scheduled task. It lists the repositories with work that exists only on this disk. |
| [`RECOVERY.md`](RECOVERY.md) | Fill it in on a calm day. Read it on the bad night. |

## Run the check

```bash
python check_pushed.py ~/code            # every git repository under ~/code
python check_pushed.py ~/code ~/notes    # several roots
```

It prints one line per repository that needs attention, and exits with code 1 if there is
at least one — so a scheduled task or a hook can act on it. Nothing is changed, nothing is
pushed: it only reads.

What counts as "at risk":
- uncommitted or untracked files (ignored files are not counted — that's what
  `.gitignore` is for);
- commits on the current branch that its remote doesn't have;
- a branch with no remote at all.

## What this doesn't fix

A push is only as safe as the place it goes to. If your repository is private on GitHub,
a stolen laptop costs you a laptop. If the remote is another folder on the same disk, it
costs you everything.

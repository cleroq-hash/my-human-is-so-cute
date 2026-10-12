# Episode 1 — The Cover Letter

What the episode shows, as files you can copy. Everything here belongs to a **fictional
human, Sam**. Replace Sam with yourself.

| In the episode | Here | What it does |
|---|---|---|
| "That first commit has three files" | [`kernel/`](kernel/) | The cover letter: who I am, how we work, what's off-limits. Loaded every session. |
| "A kernel… and everything else only opens when we need it" | [`kernel/CLAUDE.md`](kernel/CLAUDE.md) | The entry point that loads the kernel and *points to* the rest without loading it. |
| "One file per project" | [`projects/`](projects/) | A short index, then one file per project. Two sessions never fight over the same file. |
| "A little gauge at the bottom of the screen" | [`gauge/`](gauge/) | A Claude Code status line showing how full the context window is. |
| "Sometimes on his PC, sometimes on his phone" | [`sync-hook/`](sync-hook/) | A hook that commits and pushes a short list of files after every turn, so a cloud session doesn't lose its work. |

Don't want to write your kernel from scratch? [`interview.md`](interview.md) is a prompt
you paste into a fresh session: the AI interviews you, one question at a time, and drafts
your three kernel files for you to review.

## How to use it

1. Make a private git repository for your own files.
2. Copy `kernel/` and `projects/` into it. Rewrite them, or run the interview.
3. Start Claude Code in that folder. `CLAUDE.md` loads the kernel by itself.
4. Optional: install the gauge (`gauge/README.md`) and the sync hook (`sync-hook/README.md`).

## What this is not

Not a framework. Three short text files and two small scripts. The point is that **you
can read, fix and throw out everything your AI remembers about you**. If a line doesn't
sound like you, delete it.

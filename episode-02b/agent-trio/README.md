# Agent trio — three roles and a divider

An agent is an AI with a job description. That's all it is. In Claude Code, it is a file
in `.claude/agents/` that your main session can hand a task to.

There are whole catalogs of ready-made roles. The one we opened had fifteen hundred words
per role, checklists, numbered targets — and not one single thing that was forbidden.
What Sam wanted was exactly that: **what a role is not allowed to do.** So these three
cards are short, and each one has a "What you don't do" section that is longer than it
looks.

## The divider

The barrier that really holds is between the developer and the tester:

- **The tester cannot write.** Its tool list has no `Write` and no `Edit`, and
  [`hooks/tester_guard.py`](hooks/tester_guard.py) refuses shell commands that write.
  It reads, it judges, it doesn't fix.
- **The tester never sees the developer's notes.** The developer writes its
  implementation log in its reply, never in a file of the repository. The tester is told
  not to go looking in `git log` or `git diff`. It meets the code like a stranger.

First real test: the developer flagged a flaw in its own code. The tester, without
reading those notes, found the same one. That's what the divider is for — two looks that
don't contaminate each other.

## How to call them

This is the sentence that was missing. You don't launch the three agents yourself, one
after the other. You ask **one session** to call them in order:

> Run the chain on this task: the architect designs it, the developer implements the
> design, the tester gives its verdict. Pass each one only what the next needs — the
> tester gets the design's acceptance criteria and the code, nothing else.

The main session is the one that carries the design to the developer and the criteria to
the tester. A tool nobody knows how to call isn't delivered.

## What it costs

The first real run cost four hundred and sixty thousand tokens, for two hundred and
eighty lines of code. On that job, it was worth it: the architect's best work was a *no*,
before a single line was written. On ten lines, it isn't. Use the chain for a change you'd
want reviewed, not for a typo.

## Install

1. Copy [`architect.md`](architect.md), [`developer.md`](developer.md) and
   [`tester.md`](tester.md) into `.claude/agents/` of your project (or `~/.claude/agents/`
   for all of them).
2. Copy [`hooks/tester_guard.py`](hooks/tester_guard.py) into `.claude/hooks/`. The
   tester's frontmatter already declares it.
3. Replace "Sam" with yourself: it marks the decisions that stay yours.

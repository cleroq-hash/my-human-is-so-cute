---
name: monthly-review
description: Writes the review of one month of work — what was shipped, what worked and why, what was dropped, what was promised and not kept — then at most three ways of working to change, each with a test for next month. Use only when the user asks for a monthly review, a review of a given month, or to look back on the past month. Never on a schedule, never unasked. Produces a file in the repository, not a throwaway answer.
---

# Monthly review

The question this review exists to ask, and that a busy month never asks itself:
**is the tooling becoming the work?** Building your setup is satisfying, and it looks
like progress. Sometimes it is. The review is where you find out.

## Sources — and why one isn't enough

1. **`git log` of every repository** — the raw facts: what was written, when, how much.
   For work done in the terminal, it's often the only record.
2. **The session logs** (`sessions/`) — the *why* of decisions, and what became of the
   options that weren't picked.
3. **The not-built log** — what was dropped, and on what evidence.
4. **The project files** — what each project said it would do next.

Conversations tell the intentions. Git tells what happened. When they disagree, git is
right, and the gap itself is one of the month's facts.

**Check every status instead of copying it.** A project file says what was true the day
it was last updated.

## Two exercises, not one

- **The review** looks at the month: shipped, measured, dropped, learned, not kept.
- **The retrospective** looks at the way of working, not at the results.

Merged, they end in good intentions. Kept apart, they force the retrospective down to
three items at most, each one testable.

## The template

Write it in this order — from facts to interpretation:

```markdown
# Review of <month> <year>
Written on <date>. Sources used, and their limits.

## The thesis of the month
One sentence, written to be argued with — and a test that next month can prove wrong.
Example: "This month switched from producing to building tools. Test: does next month
ship as much as the first three weeks of this one, on top of the tooling?"

## Shipped
- Published (irreversible, someone else saw it)
- Built and verified
- Explored, with a result but no deliverable

## What worked — and precisely why
The cause, not the performance. What could be done again on purpose.

## Dropped
With the reason, and whether it's paused or abandoned.

## Learned

## Promised and not kept        ← never skip this one
Grouped by cause, not as a flat list.

## Numbers
Every value must be checkable in a source.

## Ways of working — the retrospective
Three at most. For each: how will we know, next month, whether it moved?
A change you can't check next month isn't a change, it's a wish.
```

## Rules

- **Private by default.** A review written as if it might be shown says nothing useful.
  If you want public material out of it one day, write a separate document from a list
  of what may go out — don't take an eraser to this one.
- **Don't answer the thesis for the human.** Lay out the evidence. The verdict on "is the
  tooling becoming the work?" is theirs.
- **Count deliverables, not commits.** A hundred commits on the setup and nothing visible
  shipped is the exact pattern the review is there to catch.

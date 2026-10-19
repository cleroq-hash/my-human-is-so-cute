---
name: count-first
description: Before designing any tool, agent, automation or integration the user proposes, measure the size of the problem with the cheapest read-only count available, and only then decide whether to build. Use when the user says "what if we built…", "let's automate…", "an agent that sorts / summarizes / watches…", or when you are about to propose an architecture for a recurring task. Don't use for a one-off task, or when the volume is already measured and written down.
---

# Count first

An AI tends to love whatever idea it's given. Not out of politeness: it's a factory
setting. The cure isn't to ask it to be more critical. It's to look at the numbers
before anyone designs anything — so that when the answer is no, it's the numbers saying
it, not the AI and not the human.

## The steps

**1. Say what number would justify building — before counting.**
One sentence: "If there are more than N per week, a tool is worth it." Write it down
first. A threshold chosen after seeing the count always ends up justifying the build.

**2. Count, as cheaply as possible, without reading the content.**
- Metadata only. For email: headers, by month — never the bodies. For files: names,
  dates, sizes. For tickets: counts by status.
- A handful of calls, not a crawl. The count is a probe, not a project.
- Watch for capped results: a search API that "estimates" counts can saturate at a round
  number and lie. When several periods return the exact same figure, recount them.

**3. Compare, and say it plainly.**
"191 conversations in ten months: four or five a week. You can read that in thirty
seconds." If the count is under the threshold, building would be vanity engineering —
say so, in those words or your own.

**4. Write down the verdict, whatever it is.**
- Not built → one entry in the not-built log (see `../decision-log/`), with the count and
  the reason. Distinguish **no justification** (closed) from **postponed** (with what would
  reopen it).
- Built → the count goes into the spec. It's the first thing the next session will need.

## What this skill is not

- Not a veto. The human decides. A low count can still justify a tool for another reason
  — then write that reason down; it's the real spec.
- Not an excuse to skip the conversation. Sometimes the count shows the need was
  different: not *summarizing* the emails, but being *reminded* to answer them. That's
  a better outcome than either building or dropping.

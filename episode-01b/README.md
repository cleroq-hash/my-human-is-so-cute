# Episode 1b — The Editor-in-Chief

What the episode shows, as files you can copy. As in episode 1, everything here belongs
to a **fictional human, Sam**. Replace Sam with yourself.

This episode is mostly about two things that were *not* built. So most of what's here
isn't code: it's the habits that decide what gets built at all.

| In the episode | Here | What it does |
|---|---|---|
| "On one side, an engine… on the other side, a charter" | [`newsroom/`](newsroom/) | Why the rules live in a file and not in the code, and an editorial charter template you can fill in. |
| "The show opens by correcting a mistake from the day before" | [`newsroom/editorial-charter.md`](newsroom/editorial-charter.md), section 4.5 | The correction rule — the one that proves a charter is real. |
| "The charter gets cached, to save money" / "know the cost before launching" | [`newsroom/cached_call.py`](newsroom/cached_call.py) | The charter sent once as a cached system prompt, token usage counted, and the run's cost compared to a budget set beforehand. |
| "The broom… at every turn, it pushes to the repository" | [`../episode-01/sync-hook/`](../episode-01/sync-hook/) | Already in episode 1: the hook that saves a cloud session's work after every turn. |
| "Should we count first?" | [`count-first/`](count-first/) | A skill that makes the AI measure the size of a problem, read-only, before designing a tool for it. |
| "A humor skill… rejected. No natural trigger." | [`count-first/README.md`](count-first/README.md) | How to write a skill's description so it actually fires — and when a skill should be a kernel line instead. |
| "It's all in the log… what he doesn't do as carefully as what he does" | [`decision-log/`](decision-log/) | A not-built log (verdict, evidence, reason, what would reopen it) and a session log template that tracks what became of every proposed option. |
| "He took the ideas. He left the code." | [`adapt-dont-import/checklist.md`](adapt-dont-import/checklist.md) | Six questions to answer by reading a ready-made setup before installing it, with a gap table. |
| "His own monthly review asks it straight out: is the tooling becoming the work?" | [`monthly-review/SKILL.md`](monthly-review/SKILL.md) | A skill that writes a monthly review from git and your logs, then at most three testable changes to your way of working. |

The line from episode 1's kernel that this episode pays off — *Don't just agree with me*
— is in [`../episode-01/kernel/about-me.md`](../episode-01/kernel/about-me.md).

## How to use it

1. Start with [`decision-log/`](decision-log/): create `not-built.md` in your own
   repository. It costs nothing and pays off the first time an old idea comes back.
2. Install the `count-first` skill (instructions in its README). Next time you say
   "what if we built…", watch what happens.
3. If you ask an AI to produce something on a schedule — a digest, a newsletter, a
   report — write its charter before its code. Then [`cached_call.py`](newsroom/cached_call.py)
   tells you what each run costs.

## What this is not

Not the newsroom engine, and not the always-on machine from the episode: those depend on
your sources, your tools and your hardware. What's here is what carries over.

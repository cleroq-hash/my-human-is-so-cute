# The newsroom: an engine, and a charter

Sam's morning news show is two things, kept apart on purpose:

- **An engine** — collects the feeds, sorts them, writes, checks, reads aloud. It knows
  nothing about journalism.
- **A charter** — what the newsroom may claim, with how many sources, how an opinion is
  flagged, how a mistake gets corrected. It's the newsroom's settings.

Change the charter, you get a different paper. Without touching the engine.

Same move as the kernel in episode 1: a program that knows nothing, and a text that sets
the rules. It works for anything you ask an AI to do over and over — a newsletter, a
weekly report, a summary of your reading. The rules go in a file you can read and
version, never buried in the code.

## The files

| File | What it is |
|---|---|
| [`editorial-charter.md`](editorial-charter.md) | A charter template: two-source rule, three audible registers (fact, analysis, uncertainty), corrections on air, what the newsroom refuses to do, and a version history. Fill in the brackets. |
| [`cached_call.py`](cached_call.py) | The API pattern: the charter goes once into a cached system prompt, every call counts its tokens, and the run ends with its cost next to the budget you set beforehand. |

The engine itself isn't here: yours will depend on your sources, your language and your
voice tools. The charter and the cost discipline are what carry over.

## Three rules worth stealing

1. **Every rule must be checkable on the output.** "Be balanced" can't be checked. "Every
   analysis ends by saying whose analysis it is" can. A charter of checkable rules can be
   audited — by you, or by a second AI pass.
2. **Version the charter, and give every change a reason.** When the paper starts doing
   something odd, the history tells you which rule changed and why.
3. **Fix the budget first, then fit the work inside it.** Know what a run costs *before*
   it runs every day. Then measure it. In the episode, the measured cost was eleven cents
   an edition — which is also what killed the idea of a local model "to save money":
   there was nothing left to save.

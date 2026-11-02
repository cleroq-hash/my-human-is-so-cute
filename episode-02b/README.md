# Episode 2b — Who Said That?

> **Watch it:** English — *Who Said That?*: **[youtu.be/ssFwI7dG9b4](https://youtu.be/ssFwI7dG9b4)**
> · Français — *La parole marquée* : **[youtu.be/9GGFUGRI9xU](https://youtu.be/9GGFUGRI9xU)**

What the episode shows, as files you can copy. As in the earlier episodes, everything
here belongs to a **fictional human, Sam**. Replace Sam with yourself.

This episode is about weight: who gets to say what, and how much it counts. Three agents
whose cards say mostly what they may *not* do, and a divider between two desks that
holds. Then a sentence written by an AI that became a fact overnight — and the convention
that came out of it: mark what the human says, not what the AI says.

| In the episode | Here | What it does |
|---|---|---|
| "An architect who designs. A developer who codes. A tester who checks." | [`agent-trio/architect.md`](agent-trio/architect.md), [`developer.md`](agent-trio/developer.md), [`tester.md`](agent-trio/tester.md) | Three Claude Code agent cards, short, each with what the role is not allowed to do. |
| "The tester is not allowed to write. He reads. He judges. He doesn't fix." | [`agent-trio/hooks/tester_guard.py`](agent-trio/hooks/tester_guard.py) | A hook that refuses the tester's shell commands that write — and says plainly that it isn't watertight. |
| "His best work is a no." | [`agent-trio/architect.md`](agent-trio/architect.md) | "This isn't worth building" is written down as a valid design. |
| "I had never written him the sentence to type." | [`agent-trio/README.md`](agent-trio/README.md) | How to run the chain from one session, the divider, and what it cost. |
| "An opinion just changed status... overnight." | [`marked-speech/README.md`](marked-speech/README.md) | Why you mark the human's words rather than the AI's: both fail, not in the same direction. |
| "Curly braces with a C in them... that's him." | [`marked-speech/convention.md`](marked-speech/convention.md) | The convention, ready to paste into your kernel file. |

## How to use it

1. Copy the three agent cards and the hook into `.claude/` (see
   [`agent-trio/README.md`](agent-trio/README.md)). Try the chain on one change you'd want
   reviewed — not on a typo.
2. Paste [`marked-speech/convention.md`](marked-speech/convention.md) into your kernel
   (see [episode 1](../episode-01/kernel/)), with your own initial.

## What this is not

Not a full harness: the episode mentions about ten hooks, and only one is here, the one
the trio needs. And the guard doesn't make the tester's boundary watertight — the tool
list and the card do most of the work, the hook only catches accidents.

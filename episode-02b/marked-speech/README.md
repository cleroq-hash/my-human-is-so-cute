# Marked speech — who said that?

## What happened

An AI writes in a work note: "this is the single constraint of the system." A line of
analysis. Reasonable. The next day, another session rereads the note, takes the sentence
for a fact, and passes it on. A task jumps to the top of the list. Sam digs in, then
stops: it's not a priority, nothing is blocked. The sentence had never been checked.

Nobody lied. An opinion just changed status overnight.

## Two ways to mark, and which way they fail

The AI's proposal was logical: **mark what comes from the AI** — a tag on every agent's
judgment, like your name on your lunch in the office fridge.

Sam proposed the opposite: **mark what comes from the human.** Everything else is assumed
to come from the AI, and doesn't carry the same weight.

It looks like a question of character count. It isn't. Both systems fail the day someone
forgets the label — but not in the same direction:

| Forgotten label | Marking the AI | Marking the human |
|---|---|---|
| What it turns into | an AI opinion becomes a fact | one of your decisions becomes a mere opinion |
| Who notices | nobody: it reads like everything else | you, when you're asked again |
| Cost | silent, and it spreads | annoying, but recoverable |

A system should fail toward the error you can see.

## Use it

Paste [`convention.md`](convention.md) into your kernel file (`CLAUDE.md`, see
[episode 1](../episode-01/kernel/)), and pick your initial: here it's `{S: …}` for Sam.
From then on, a curly brace with your initial is you. Everything else is the AI — and the
AI doesn't get the last word.

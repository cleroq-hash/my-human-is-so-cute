# Adapt, don't import — a checklist for ready-made setups

There are ready-made setups for Claude Code out there: dozens or hundreds of rules,
agents, skills, hooks, ready to install. Some are excellent. This checklist is for
deciding what to do with one **by reading it, before installing anything**.

## Why read first

A rule that's always loaded is an order the AI follows every session, without
questioning it. If nobody in your house has read that rule, your AI is taking orders
from a stranger. Not because the stranger means harm — because nobody checked.

Two more costs, less visible:

- **Context.** Every always-loaded rule takes room in the AI's working memory, every
  session, whether it's useful that day or not.
- **Debugging.** When the AI misbehaves, you need to know which instruction produced the
  behavior. With three hundred files you haven't read, you can't.

## The checklist

**1. What's always on?**
Separate what gets loaded at every session (rules, kernel files, hooks that fire on every
turn) from what only opens on demand (skills, agents, commands). The first group is the
real question. The second is a library.

**2. What does it do that you'd never let it do?**
Look for anything that commits, pushes, opens pull requests, sends, publishes, or calls
an outside service on its own. Compare with your own kernel. If the pack's rule and
yours disagree, nothing says which one wins.

**3. What's actually missing — the gap table.**

| Category | What I have | What the pack has | Actually missing? |
|---|---|---|---|
| Always-on rules | | | |
| Hooks | | | |
| Memory / notes between sessions | | | |
| Skills | | | |
| Sub-agents | | | |
| Commands | | | |
| Tool connections (MCP) | | | |
| Security checks | | | |

The numbers on a pack's front page are intimidating. The gap table usually isn't: most
lines say "already covered", and one or two say "missing".

**4. Take the idea, leave the code.**
For each real gap, read the one file in the pack that fills it. Then write your own
version, in your words, sized for your needs. You'll understand every line of it, and
it will match the rest of your setup.

**5. Ask whether the problem is really a missing tool.**
Sometimes what's missing isn't more rules, it's *using the ones you have*. Installing a
framework for that is buying a second alarm clock. If the gap is discipline, the fix is a
trigger that makes you use what you already have — a hook, a skill with a clear
description, one line in the kernel.

**6. Write the verdict down, with what would reopen it.**
In your not-built log (see `../decision-log/`). A good reopen condition is narrow: "a
precise need that one named piece of the pack answers — then read that piece, don't
install the pack." Not "when a new version comes out": if the reason was structural, a
bigger pack makes it truer, not weaker.

## When reading isn't enough

Reading settles **structural** questions: does this belong here, what would it load,
what does it contradict. It does not settle **quality or performance**: does this voice
sound good, is this model fast enough on my machine. Those need a test. Know which
question you're asking before deciding how to answer it.

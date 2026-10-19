# The decision log — including what you don't build

> "My human writes down what he doesn't do as carefully as what he does."

Without that, a dropped idea comes back three weeks later, brand new, and you burn the
same three hours again. For an AI with amnesia it's vital: the AI that proposes the idea
again next month has no way to know it was already killed — unless it's written down.

Two files, two jobs:

| File | When you write in it | What it keeps |
|---|---|---|
| [`not-built.md`](not-built.md) | When an idea is dropped, postponed, or adopted after a real check | The verdict, the evidence, and what would reopen it. One entry per idea. |
| A session log, from the template below | During and at the end of a work session | Why decisions were made, what was said in passing, and **what became of each option the AI proposed**. |

## The three fates of an option nobody picked

When the AI ends a turn with "here are three things we could do next", one gets picked.
The other two don't vanish — they have a fate, and it's worth writing down:

- **Deferred** — you'll come back to it. It should end up in a backlog; the log is only a
  trace.
- **Obsolete** — what you chose made it pointless. Keep it anyway: it explains why a path
  wasn't taken.
- **Ignored** — no reaction, neither yes nor no. **That's the one that gets lost**, and
  the only reason this mechanism exists.

The same option ignored three times is a signal: either the topic doesn't interest you
and it should be killed, or it's a blind spot and needs to be presented differently.

## Session log template

One file per session, named `YYYY-MM-DD-topic.md`, in a `sessions/` folder. One file per
session means two sessions never write to the same file.

```markdown
# YYYY-MM-DD — Topic

## Decisions, and why
- **The decision.** The reason, in a sentence or two. Whose call it was.

## Said in passing, and it matters
- The remark that changed the direction, quoted if it's yours.

## Options proposed, and what became of them
- *HH:MM* — the option — **taken**
- *HH:MM* — the option — **deferred** (→ backlog)
- *HH:MM* — the option — **obsolete**: made pointless by …
- *HH:MM* — the option — **ignored**

## Open on the way out
- What the next session needs to know first.
```

Keep "what changed" out of it: git already says that. The log is for the *why*.

Ask your AI to fill the "Options" section as it goes, each time it proposes next steps.
Written during the session, it survives a closed terminal or a dead battery. Written at
the end, it depends on remembering to.

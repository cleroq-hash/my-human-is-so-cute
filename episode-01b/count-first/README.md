# Count first — a skill

In the episode, Sam proposes an agent to sort his emails. The AI loves it and starts
designing a three-layer architecture. Then Sam asks: *should we count first?* Thirteen
calls, headers only: four or five emails a week. The agent was never built, and that was
the right outcome.

[`SKILL.md`](SKILL.md) turns that question into a habit the AI picks up by itself.

## Install

Copy the folder so the file ends up at:

```
<your repository>/.claude/skills/count-first/SKILL.md     # this project only
~/.claude/skills/count-first/SKILL.md                     # all your projects
```

Claude Code lists the skills it finds at the start of a session, and opens one when the
situation matches its `description`.

## Why the description is the most important line

A skill is a how-to guide the AI pulls out when a situation calls for it. It only gets
pulled out if the **description says when**. The episode mentions a humor skill that was
rejected for exactly this reason: no natural trigger. What situation would ever say
"now be funny"? It became one line in the kernel instead.

So when you write a skill, write the description first, and make it name:

- the **moment** it fires — words the user says, or something the AI is about to do;
- the **cases where it must not fire** — otherwise it fires everywhere and gets ignored.

If you can't name the moment, you don't have a skill. You have a rule — and rules go in
the kernel.

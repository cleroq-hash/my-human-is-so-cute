# Episode 2a — Lose It All, Get It All Back

> **Watch it:** English — *Lose It All, Get It All Back*: **[youtu.be/TygVk-ShZn4](https://youtu.be/TygVk-ShZn4)**
> · Français — *Tout perdre, tout retrouver* : **[youtu.be/1vM3AlgZsOg](https://youtu.be/1vM3AlgZsOg)**

What the episode shows, as files you can copy. As in the earlier episodes, everything
here belongs to a **fictional human, Sam**. Replace Sam with yourself.

This episode is about what survives. A machine goes back in time by a week, and
everything that was written down comes back with one command. The rest of the files here
are about the same idea from other sides: a box that wasn't as sealed as everyone
thought, three thinking roles that must never talk at the same time, and a wall that
measures writing — not thinking.

| In the episode | Here | What it does |
|---|---|---|
| "One command, and twenty-eight changes come back at once" | [`recovery/check_pushed.py`](recovery/check_pushed.py) | Lists every repository with uncommitted changes or commits not yet pushed. What's pushed survives the disk; the rest doesn't. |
| "A recovery plan nobody had written, carried out cold, on a night of panic" | [`recovery/RECOVERY.md`](recovery/RECOVERY.md) | The recovery plan, written on a calm day instead. A template, in the order you'll need it. |
| "The day it forgets… what's left?" | [`recovery/README.md`](recovery/README.md) | Why an assistant's memory should live in files you can read, not inside the assistant. |
| "If the box can see the server next door… then it's not sealed off" | [`sealed-box/probe_host.py`](sealed-box/probe_host.py) | Run it *inside* your sandbox: it tries to reach services running on the host machine. If it connects, your box shares the network. |
| "Two amnesiacs in the same house" | [`sealed-box/README.md`](sealed-box/README.md) | Files sealed off is not network sealed off, and two sessions of the same AI don't know about each other. |
| "Ninety-eight percent of the verdict could be reached without installing anything" | [`../episode-01b/adapt-dont-import/checklist.md`](../episode-01b/adapt-dont-import/checklist.md) | Already in episode 1b: read a tool before you install it. |
| "The Dreamer, the Realist and the Critic… NEVER at the same time" | [`three-roles/postures.md`](three-roles/postures.md) | A kernel file that lets your AI take one of three roles on request — or offer one when it sees an idea closing too early. |
| "The Realist goes before the Critic. ALWAYS." | [`three-roles/README.md`](three-roles/README.md) | Why the order matters, and how a Critic found the way out of a contradiction instead of a reason to give up. |
| "A card is in progress if someone came back to it on another day" | [`wall/wall.py`](wall/wall.py) | A kanban wall built from your project files and their git history, with a work-in-progress limit that scolds you. |
| "The proof of life… it checks that every automatic task actually ran" | [`wall/proof_of_life.py`](wall/proof_of_life.py) | One green or red line per scheduled task, from the age of what it last produced. |
| "Do you have a shared base for these pages?" | [`wall/base.css`](wall/base.css) | One stylesheet for every page. Change it once, not four times. |

## How to use it

1. Run [`recovery/check_pushed.py`](recovery/check_pushed.py) on the folder that holds
   your repositories. If anything shows up, you know what a dead disk would cost you
   tonight.
2. If you run tools inside a container or a sandbox, run
   [`sealed-box/probe_host.py`](sealed-box/probe_host.py) from inside it once. Before you
   trust the box with anything.
3. Copy [`three-roles/postures.md`](three-roles/postures.md) into your kernel (see
   [episode 1](../episode-01/kernel/)) and say "Dreamer" next time an idea gets shot down
   in its first minute.
4. If you keep one file per project (see [episode 1](../episode-01/projects/)), point
   [`wall/wall.py`](wall/wall.py) at that folder.

## What this is not

Not a backup tool: GitHub kept the files because they were pushed every night, not
because of anything in this folder. And not a security audit: `probe_host.py` answers one
question — can the box reach the host? — and nothing more.

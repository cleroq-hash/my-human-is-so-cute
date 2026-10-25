# Recovery plan — Sam

*Written on a calm day, to be read on a bad night. Keep a copy somewhere that doesn't
die with this computer: a printout, your phone, a private repository.*

In the episode, the plan was "written by nobody, carried out cold, on a night of panic."
It worked. It would have worked faster, and with less panic, from a page like this one.

## 0. Stop

Before anything else: **don't write to the damaged disk.** No reinstall, no "let me just
try", no new files. Every write can cover something you could still have recovered.

Write down what you see, with the time. You'll want it later — so will your AI, which
won't remember any of tonight.

## 1. What lives where

| What | Where the original lives | Where the copy lives | How it comes back |
|---|---|---|---|
| Kernel and project files | `~/assistant/` | private GitHub repository `sam/assistant` | `git clone` |
| Scripts and hooks | `~/code/tools/` | private GitHub repository `sam/tools` | `git clone` |
| AI settings (`~/.claude/settings.json`, hooks) | home folder | *(fill in — this one is easy to forget)* | |
| Photos, documents | `~/Pictures`, `~/Documents` | *(your backup service)* | |
| Conversations with the AI | the AI's own history | **nowhere** | they don't come back |

The last line is not a mistake. Decide now whether that's acceptable. If a conversation
matters, what it decided belongs in a file.

## 2. The order to bring things back

1. A working machine with git and your GitHub access (you'll have to sign in again
   yourself — keep your password manager reachable from your phone).
2. The repositories, one `git clone` each. List them here so you don't have to remember:
   - `sam/assistant`
   - `sam/tools`
3. The AI settings, then the hooks. Start a session and check that the kernel loads.
4. Scheduled tasks. They don't come back by themselves: list them here, with how each one
   is started.
   - morning digest — *(how it's scheduled)*
5. Only then, the rest.

## 3. How to know it's over

- `check_pushed.py` reports nothing at risk.
- Every scheduled task has produced its output once (see the proof of life in
  [`../wall/`](../wall/)).
- You've written two lines about what happened, in your log. Including "user error", if it
  was one.

## 4. After

Reread this page. Fix what was wrong in it. That's the only moment you'll know.

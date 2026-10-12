# The sync hook

Sam works sometimes on his PC, sometimes on his phone through Claude Code on the web. A
web session runs in a container that disappears after a while. **Anything not pushed
disappears with it.**

This hook runs after every turn of a cloud session, commits the files on a short allowed
list, and pushes them. On the PC it does nothing: the disk is still there tomorrow.

## The real fix came first

The hook doesn't solve the conflicts from the episode. Splitting one big file into one
file per project does (see [`../projects/`](../projects/)). Two sessions that never edit
the same file have nothing to fight over. The hook only makes sure the work survives.

## Install

In the repository you open in cloud sessions:

1. Copy `sync_on_stop.py` to `.claude/hooks/sync_on_stop.py`.
2. Edit `ALLOWED` at the top of the script: the folders and files it may push.
3. Add to `.claude/settings.json` **in the repository** (not in `~/.claude/`, which
   doesn't travel to the cloud):

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/sync_on_stop.py\""
          }
        ]
      }
    ]
  }
}
```

Use `$CLAUDE_PROJECT_DIR`, never an absolute path: the repository lives somewhere else
in the cloud.

## What it doesn't do

- It pushes the session's branch. Cloud sessions usually work on their own branch;
  merging it into `main` stays a decision you make.
- It never resolves a conflict. It stops and tells you.

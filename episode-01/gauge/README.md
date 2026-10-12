# The gauge

A status line for Claude Code that shows how full the AI's working memory — the context
window — is:

```
/my-files | Opus | ctx [███░░░░░░░] 31% | 5h [██░░░░░░░░] 18% reset in 3h12
```

**Why it matters.** As the context fills up, the start of the conversation slips away
and answers get less reliable. Sam noticed that up to 30–40 % everything was fine, and
stops before that. That's his observation, not a measured threshold: watch your own gauge
and find your own line.

## Install

1. Copy `statusline.py` to `~/.claude/statusline.py`.
2. Add this to `~/.claude/settings.json` (merge it with what's already there):

```json
{
  "statusLine": {
    "type": "command",
    "command": "python3 ~/.claude/statusline.py"
  }
}
```

On Windows, use `python` instead of `python3` if that's what your install calls it.

3. Start a new Claude Code session. The gauge appears at the bottom.

## Try it without Claude Code

```bash
echo '{"model":{"display_name":"Opus"},"cwd":"/home/sam/my-files","context_window":{"used_percentage":55}}' | python3 statusline.py
```

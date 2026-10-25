# The wall — and what it can't see

Sam's kernel says: *don't recite the state of my projects at the start of a
conversation.* The information still has to live somewhere. This is that somewhere: a
few pages you open when you want them, and that stay quiet when you don't.

| File | What it shows |
|---|---|
| [`wall.py`](wall.py) | A kanban wall: in progress, quiet, done — from your project files and their git history. |
| [`proof_of_life.py`](proof_of_life.py) | One green or red line per scheduled task. |
| [`base.css`](base.css) | The style both pages share. |

No dependencies beyond Python 3 and git.

## The wall

```bash
python wall.py ~/assistant/projects --days 14 --limit 7
```

It writes `wall.html` next to `base.css`. Open it in a browser; it reloads itself every
five minutes, so re-running the script (by hand, or from a scheduled task) is enough to
keep it fresh.

### "In progress" is a question, not a threshold

The first version counted a card as in progress if its file had changed in the last
fourteen days. Result: 47 cards out of 53 in progress. The folder was eight days old —
of course everything had moved recently.

Moving the threshold to seven days would only have postponed the problem. The fix was a
better question: **a card is in progress if someone came back to it on another day.**
Two distinct days of writing in the window. 47 became 8.

### The limit that scolds

On its first run, the wall showed an alert: 8 projects in progress, against a limit of 7.
The tool was one minute old, and it was already scolding its owner. That's the point of a
work-in-progress limit: it says out loud what you'd rather not count.

### What it measures: writing, not thinking

The next morning, Sam said: *"This is yesterday's data. It doesn't include my thinking
from this morning."* He was right. The wall dates each card by the last time someone
wrote in its file. A morning of thinking that writes nothing doesn't exist for it.

There's no fix for that in the code, and there shouldn't be one. Know it when you read
the wall, or write one line in the project file when you've been thinking about it.

## Proof of life

```bash
python proof_of_life.py
```

Edit the `TASKS` list at the top of the script first: for each scheduled task, the file
it writes when it succeeds, and how old that file may get. A task that works and a task
that died look the same — silent. The age of the output tells them apart.

## One base, not four copies

In the episode, by the evening there were four pages, each with its own copy of the same
style. Technical debt built in a single day, and nobody saw it — except Sam, while asking
for something else: *"Do you have a shared base for these pages? Otherwise you'll change
things in four places instead of one."*

So both pages here link to `base.css`. If you add a page, link it too. If you ask your AI
to add a page, tell it — it won't think of it on its own.

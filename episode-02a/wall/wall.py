#!/usr/bin/env python3
"""A kanban wall built from your project files and their git history.

One markdown file per project (see episode 1's `projects/`). The wall reads, for each
file, the days on which a commit touched it, and sorts the cards into three columns:

  - In progress: someone came back to it on at least two different days in the window.
  - Quiet:       touched once in the window, or not at all.
  - Done:        the file says so, with a line `Status: done`.

Why "came back on another day"? The first version said "touched in the last fourteen
days". The folder was eight days old, so everything had been touched: 47 cards out of 53
"in progress", which tells you nothing. Changing the threshold wouldn't have helped.
Changing the question did: 47 became 8.

It also checks a work-in-progress limit, and says so at the top when you're over it.

Know what it measures: WRITING, not thinking. A morning spent thinking about a project
without writing in its file doesn't exist for the wall.

Usage:
    python wall.py PROJECTS_FOLDER [--days 14] [--limit 7] [--out wall.html]

The folder must be inside a git repository. The page refreshes itself every five minutes
in the browser; re-run the script (by hand or from a scheduled task) to update the data.
"""
import argparse
import html
import re
import subprocess
from datetime import date, datetime, timedelta
from pathlib import Path

DONE = re.compile(r"^\s*\**status\**\s*:\s*\**done\b", re.IGNORECASE | re.MULTILINE)
SKIP_FILES = {"readme.md", "projects.md", "index.md"}


def days_touched(path, since):
    """The distinct calendar days on which a commit touched `path`, since `since`."""
    out = subprocess.run(
        ["git", "log", "--follow", f"--since={since.isoformat()}", "--format=%cs", "--", path.name],
        cwd=path.parent, capture_output=True, text=True,
    ).stdout
    return sorted({date.fromisoformat(d) for d in out.split()})


def title_of(path):
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def build(folder, window_days):
    since = date.today() - timedelta(days=window_days)
    columns = {"In progress": [], "Quiet": [], "Done": []}
    for path in sorted(Path(folder).glob("*.md")):
        if path.name.lower() in SKIP_FILES:
            continue
        days = days_touched(path, since)
        text = path.read_text(encoding="utf-8", errors="replace")
        card = {
            "name": title_of(path),
            "file": path.name,
            "days": len(days),
            "last": days[-1].isoformat() if days else "not in window",
        }
        if DONE.search(text):
            columns["Done"].append(card)
        elif len(days) >= 2:
            columns["In progress"].append(card)
        else:
            columns["Quiet"].append(card)
    return columns


def render(columns, window_days, limit):
    in_progress = len(columns["In progress"])
    alert = ""
    if in_progress > limit:
        alert = (f'<div class="alert">{in_progress} projects in progress, '
                 f"against a limit of {limit}.</div>")

    blocks = []
    for name, cards in columns.items():
        items = "".join(
            f'<div class="card"><div class="name">{html.escape(c["name"])}</div>'
            f'<div class="info">{html.escape(c["file"])} · '
            f'{c["days"]} day(s) written · last {c["last"]}</div></div>'
            for c in cards
        ) or '<div class="info">—</div>'
        blocks.append(f'<section class="column"><h2>{name} ({len(cards)})</h2>{items}</section>')

    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="300">
<title>Wall</title>
<link rel="stylesheet" href="base.css">
</head><body>
<h1>Wall</h1>
<div class="meta">Built {stamp} from git history, last {window_days} days.
It measures writing, not thinking.</div>
{alert}
<div class="columns">{''.join(blocks)}</div>
</body></html>
"""


def main():
    parser = argparse.ArgumentParser(description="Kanban wall from project files and git history.")
    parser.add_argument("folder", help="folder with one markdown file per project")
    parser.add_argument("--days", type=int, default=14, help="window, in days (default 14)")
    parser.add_argument("--limit", type=int, default=7, help="work-in-progress limit (default 7)")
    parser.add_argument("--out", default=str(Path(__file__).with_name("wall.html")),
                        help="output page; keep it next to base.css")
    args = parser.parse_args()

    columns = build(args.folder, args.days)
    Path(args.out).write_text(render(columns, args.days, args.limit), encoding="utf-8")
    counts = ", ".join(f"{k.lower()}: {len(v)}" for k, v in columns.items())
    print(f"{args.out} written ({counts}).")
    if len(columns["In progress"]) > args.limit:
        print(f"Over the limit: {len(columns['In progress'])} in progress, limit {args.limit}.")


if __name__ == "__main__":
    main()

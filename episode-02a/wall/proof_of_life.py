#!/usr/bin/env python3
"""Proof of life: did every automatic task actually run?

A scheduled task that works and a scheduled task that died look exactly the same: silent.
This page gives each task one line, green or red, judged by the only thing that doesn't
lie — the age of what it last produced.

In the episode, its very first run showed a red line: the morning digest hadn't gone out
since the day before. A whole morning had been spent looking for why, down two wrong
leads. The answer was right there, in one line. Three minutes.

Describe your tasks in TASKS below: a name, the file the task writes when it succeeds,
and how old that file may get before it counts as late.

Usage:
    python proof_of_life.py [--out proof-of-life.html]

Exit code: 0 if every task is on time, 1 otherwise — so another task can act on it.
"""
import argparse
import html
from datetime import datetime, timedelta
from pathlib import Path

# Edit this list. A glob is allowed: the newest matching file counts.
TASKS = [
    {"name": "Morning digest", "output": "~/assistant/digest/*.md", "max_age_hours": 26},
    {"name": "Nightly push of the notes", "output": "~/assistant/.last-push", "max_age_hours": 26},  # a stamp your push task touches
    {"name": "Weekly backup", "output": "~/backups/*.tar.gz", "max_age_hours": 24 * 8},
]


def newest(pattern):
    """The newest file matching `pattern` (with ~ expanded), or None."""
    path = Path(pattern).expanduser()
    if "*" not in pattern:
        return path if path.exists() else None
    matches = [p for p in path.parent.glob(path.name) if p.is_file()]
    return max(matches, key=lambda p: p.stat().st_mtime) if matches else None


def check(task, now):
    found = newest(task["output"])
    if found is None:
        return False, "no output found"
    age = now - datetime.fromtimestamp(found.stat().st_mtime)
    hours = age.total_seconds() / 3600
    ok = age <= timedelta(hours=task["max_age_hours"])
    when = f"{hours:.0f} h ago" if hours < 48 else f"{hours / 24:.0f} days ago"
    return ok, f"last output {when} (limit {task['max_age_hours']} h)"


def render(results, now):
    lines = "".join(
        f'<li><span class="dot {"ok" if ok else "late"}"></span>'
        f"<span>{html.escape(name)}</span>"
        f'<span class="info">{html.escape(info)}</span></li>'
        for name, ok, info in results
    )
    late = sum(1 for _, ok, _ in results if not ok)
    alert = f'<div class="alert">{late} task(s) late.</div>' if late else ""
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="300">
<title>Proof of life</title>
<link rel="stylesheet" href="base.css">
</head><body>
<h1>Proof of life</h1>
<div class="meta">Checked {now:%Y-%m-%d %H:%M}.</div>
{alert}
<ul class="lines">{lines}</ul>
</body></html>
"""


def main():
    parser = argparse.ArgumentParser(description="One green or red line per scheduled task.")
    parser.add_argument("--out", default=str(Path(__file__).with_name("proof-of-life.html")),
                        help="output page; keep it next to base.css")
    args = parser.parse_args()

    now = datetime.now()
    results = []
    for task in TASKS:
        ok, info = check(task, now)
        results.append((task["name"], ok, info))
        print(f"{'OK  ' if ok else 'LATE'}  {task['name']}: {info}")

    Path(args.out).write_text(render(results, now), encoding="utf-8")
    return 0 if all(ok for _, ok, _ in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Claude Code status line: folder, model, and a gauge of how full the context window is.

Claude Code pipes a JSON object to this script on stdin and shows whatever it prints.
Green up to 40 %, yellow up to 70 %, red beyond. The habit that goes with it: when the
gauge leaves the green, write down where you are and start a fresh session.

Also shows the 5-hour usage limit when Claude Code reports it.
"""
import json
import os
import sys
import time

GREEN, YELLOW, RED, GREY, RESET = (
    "\033[38;2;76;175;80m", "\033[33m", "\033[31m", "\033[38;2;150;150;150m", "\033[0m")


def colour(pct):
    if pct <= 40:
        return GREEN
    if pct <= 70:
        return YELLOW
    return RED


def bar(pct, width=10):
    filled = max(0, min(width, round(pct * width / 100)))
    return "█" * filled + "░" * (width - filled)


def gauge(label, pct):
    pct = round(pct)
    return f"{colour(pct)}{label} [{bar(pct)}] {pct}%{RESET}"


def line(data):
    parts = []
    cwd = (data.get("workspace") or {}).get("current_dir") or data.get("cwd") or ""
    if cwd:
        parts.append("/" + os.path.basename(cwd.rstrip("/\\")))
    model = (data.get("model") or {}).get("display_name")
    if model:
        parts.append(f"{GREY}{model}{RESET}")

    used = (data.get("context_window") or {}).get("used_percentage")
    if used is not None:
        parts.append(gauge("ctx", used))

    five_h = (data.get("rate_limits") or {}).get("five_hour") or {}
    if five_h.get("used_percentage") is not None:
        text = gauge("5h", five_h["used_percentage"])
        reset = five_h.get("resets_at")
        if reset:
            left = int(reset - time.time())
            if left > 0:
                text += f" {GREY}reset in {left // 3600}h{(left % 3600) // 60:02d}{RESET}"
        parts.append(text)
    return " | ".join(parts)


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdout.write(line(json.load(sys.stdin)))
    except Exception:
        # A status line that crashes shows nothing at all. Fail quietly.
        sys.stdout.write("ctx ?")


if __name__ == "__main__":
    main()

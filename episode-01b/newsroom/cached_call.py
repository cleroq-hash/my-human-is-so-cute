#!/usr/bin/env python3
"""Call Claude with your charter cached, and know what each run costs.

The episode's newsroom makes several API calls per edition, and every one of them needs
the same long charter. Sent in plain text each time, the charter is billed in full each
time. Sent once as a cached `system` block, the first call writes it to the cache and
the following calls read it back at a fraction of the input price.

This script shows the pattern in one place:
  - the charter goes in `system`, with a cache point;
  - every call adds its token usage to a running total;
  - at the end, it prints the cost of the run and compares it to a budget you set
    *before* launching.

Usage:
    pip install anthropic
    export ANTHROPIC_API_KEY=...        # your key, from your environment, never in code
    python cached_call.py "First question" "Second question" "Third question"

Three things that silently break caching:
  - Anything placed *before* the charter in `system`. The cache is an exact prefix.
  - A charter that changes between calls (reloaded differently, a date inserted in it).
  - A charter that's too short. Below a minimum length (around a thousand tokens, it
    depends on the model) nothing is cached. The template next to this script is close
    to that line; a real charter usually isn't.
If the run reports zero cache reads over several calls, look there first.
"""
import sys
from pathlib import Path

import anthropic

# The model you use. Check the current model names in Anthropic's documentation.
MODEL = "claude-sonnet-5-5"

CHARTER = Path(__file__).with_name("editorial-charter.md")

# Prices in US dollars per million tokens, for MODEL. Copy them from Anthropic's pricing
# page: they change, so they are not filled in here. Left at None, the script reports
# tokens only.
PRICE_INPUT = None
PRICE_OUTPUT = None

# Cache multipliers, relative to the input price, as documented for the default
# five-minute cache at the time of writing. Check the prompt caching documentation.
CACHE_WRITE = 1.25
CACHE_READ = 0.10

# What one run is allowed to cost. Decide this before you launch, not after.
BUDGET_PER_RUN = 0.25

usage_total = {"input": 0, "cache_write": 0, "cache_read": 0, "output": 0}


def ask(client, charter, prompt, max_tokens=800):
    """One call. The charter is the cached system prompt; the prompt is the variable part."""
    message = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        system=[
            {
                "type": "text",
                "text": charter,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": prompt}],
    )

    u = message.usage
    usage_total["input"] += u.input_tokens or 0
    usage_total["cache_write"] += getattr(u, "cache_creation_input_tokens", 0) or 0
    usage_total["cache_read"] += getattr(u, "cache_read_input_tokens", 0) or 0
    usage_total["output"] += u.output_tokens or 0

    return "".join(block.text for block in message.content if block.type == "text")


def report():
    u = usage_total
    print(f"[usage] input {u['input']} | cache written {u['cache_write']} "
          f"| cache read {u['cache_read']} | output {u['output']}")

    if u["cache_read"] == 0:
        print("[warning] No cache reads: the charter was billed in full on every call. "
              "See the three causes at the top of this file.")

    if PRICE_INPUT is None or PRICE_OUTPUT is None:
        print("[cost] Fill in PRICE_INPUT and PRICE_OUTPUT to see the cost of the run.")
        return

    cost = (
        u["input"] * PRICE_INPUT
        + u["cache_write"] * PRICE_INPUT * CACHE_WRITE
        + u["cache_read"] * PRICE_INPUT * CACHE_READ
        + u["output"] * PRICE_OUTPUT
    ) / 1_000_000
    print(f"[cost] this run: ${cost:.4f} (budget ${BUDGET_PER_RUN:.2f})")
    if cost > BUDGET_PER_RUN:
        print("[cost] Over budget. Cut the work to fit, or raise the budget on purpose.")


def main():
    prompts = sys.argv[1:]
    if not prompts:
        print(__doc__)
        return 1
    charter = CHARTER.read_text(encoding="utf-8")
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment
    for prompt in prompts:
        print(ask(client, charter, prompt))
        print("---")
    report()
    return 0


if __name__ == "__main__":
    sys.exit(main())

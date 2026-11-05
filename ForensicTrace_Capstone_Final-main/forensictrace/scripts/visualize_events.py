#!/usr/bin/env python3
"""Summarise event counts by type; optional SVG bar chart (standard library only)."""

from __future__ import annotations

import argparse
import json
from collections import Counter

import svgchart


def main() -> int:
    parser = argparse.ArgumentParser(description="Visualize ForensicTrace event types")
    parser.add_argument("json_path", help="Path to experiment JSON")
    parser.add_argument(
        "-o",
        "--output",
        help="Write SVG chart to this path (e.g. events.svg)",
    )
    args = parser.parse_args()

    with open(args.json_path, encoding="utf-8") as fh:
        data = json.load(fh)

    events = data.get("events", [])
    counts = Counter(e.get("type", "unknown") for e in events)
    config = data.get("config", "?")

    print(f"Config: {config} | Total events: {len(events)}")
    for kind in sorted(counts):
        print(f"  {kind:10} {counts[kind]}")

    if not args.output:
        return 0

    labels = sorted(counts)
    svgchart.bar_panels([{"title": f"Events by type (config {config})", "labels": labels,
                          "values": [counts[k] for k in labels], "xlabel": "Event type"}],
                        args.output, cols=1, panel_w=460, panel_h=300)
    print(f"Wrote chart to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

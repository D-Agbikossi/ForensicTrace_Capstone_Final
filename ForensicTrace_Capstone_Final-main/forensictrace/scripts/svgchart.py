"""Minimal bar-chart writer that emits SVG with the standard library only.

Replaces matplotlib so the figures build on any machine with Python 3.
Each panel is a dict: title, labels, values, optional errors (SD),
optional threshold (dashed reference line) and optional ymax (fixed axis
top, e.g. 100 for percentages). The SVG opens in any browser
and embeds directly in the HTML/PDF report.
"""

from __future__ import annotations

import math
from html import escape
from pathlib import Path

SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_2 = "#52514e"
GRID = "#e4e3df"
BAR = "#2a78d6"
FONT = "DejaVu Sans, Arial, sans-serif"


def nice_step(v: float) -> float:
    """Round a tick step up to 1, 2, 2.5 or 5 x 10^k."""
    if v <= 0 or not math.isfinite(v):
        return 1.0
    mag = 10 ** math.floor(math.log10(v))
    for step in (1, 2, 2.5, 5, 10):
        if v <= step * mag:
            return step * mag
    return 10 * mag


def fmt_num(v: float) -> str:
    if float(v).is_integer() or abs(v) >= 100:
        return f"{v:,.0f}"
    return f"{v:.1f}"


def _panel(p: dict, x0: float, y0: float, w: float, h: float) -> list[str]:
    labels, values = p["labels"], [float(v) for v in p["values"]]
    errors = [float(e) for e in p.get("errors") or [0.0] * len(values)]
    thr = p.get("threshold")
    out = [f'<text x="{x0}" y="{y0 + 14}" font-size="13" font-weight="600" fill="{INK}">'
           f'{escape(p["title"])}</text>']
    if thr is not None:
        out.append(f'<text x="{x0 + w}" y="{y0 + 14}" font-size="10" text-anchor="end" fill="{INK_2}">'
                   f'- - threshold {fmt_num(thr)}</text>')

    left, top, bottom = 44, 30, 34
    px, py, pw, ph = x0 + left, y0 + top, w - left - 8, h - top - bottom
    peak = max([v + e for v, e in zip(values, errors)] + [thr or 0])
    step = nice_step((p.get("ymax") or peak) / 4)
    ymax = step * 4
    scale = ymax * 1.1  # headroom for the value labels above the top tick
    ypos = lambda v: py + ph - (min(v, scale) / scale) * ph  # noqa: E731

    for i in range(5):  # recessive grid with 4 intervals
        tv = step * i
        y = ypos(tv)
        out.append(f'<line x1="{px}" y1="{y:.1f}" x2="{px + pw}" y2="{y:.1f}" '
                   f'stroke="{GRID if i else INK_2}" stroke-width="1"/>')
        out.append(f'<text x="{px - 6}" y="{y + 4:.1f}" font-size="10" text-anchor="end" '
                   f'fill="{INK_2}">{fmt_num(tv)}</text>')

    slot = pw / len(values)
    bw = min(slot * 0.55, 56)
    for i, (lab, v, e) in enumerate(zip(labels, values, errors)):
        cx = px + slot * (i + 0.5)
        yt, yb = ypos(max(v, 0)), ypos(0)
        bh = yb - yt
        r = min(4, bh)  # rounded data end, square at the baseline
        out.append(f'<path d="M{cx - bw / 2:.1f},{yb:.1f} V{yt + r:.1f} '
                   f'Q{cx - bw / 2:.1f},{yt:.1f} {cx - bw / 2 + r:.1f},{yt:.1f} '
                   f'H{cx + bw / 2 - r:.1f} Q{cx + bw / 2:.1f},{yt:.1f} {cx + bw / 2:.1f},{yt + r:.1f} '
                   f'V{yb:.1f} Z" fill="{BAR}"><title>{escape(str(lab))}: {fmt_num(v)}'
                   f'{f" (SD {fmt_num(e)})" if e else ""}</title></path>')
        if e > 0:
            ylo, yhi = ypos(max(v - e, 0)), ypos(v + e)
            out.append(f'<path d="M{cx:.1f},{ylo:.1f} V{yhi:.1f} M{cx - 5:.1f},{yhi:.1f} H{cx + 5:.1f} '
                       f'M{cx - 5:.1f},{ylo:.1f} H{cx + 5:.1f}" stroke="{INK}" stroke-width="1.2" fill="none"/>')
        label_y = (ypos(v + e) if e > 0 else yt) - 5
        out.append(f'<text x="{cx:.1f}" y="{label_y:.1f}" font-size="10" text-anchor="middle" '
                   f'fill="{INK}">{fmt_num(v)}</text>')
        out.append(f'<text x="{cx:.1f}" y="{yb + 15:.1f}" font-size="11" text-anchor="middle" '
                   f'fill="{INK}">{escape(str(lab))}</text>')

    if thr is not None:
        y = ypos(thr)
        out.append(f'<line x1="{px}" y1="{y:.1f}" x2="{px + pw}" y2="{y:.1f}" stroke="{INK_2}" '
                   f'stroke-width="1.5" stroke-dasharray="5 4"/>')

    if p.get("xlabel"):
        out.append(f'<text x="{px + pw / 2:.1f}" y="{y0 + h - 2:.1f}" font-size="10.5" '
                   f'text-anchor="middle" fill="{INK_2}">{escape(p["xlabel"])}</text>')
    return out


def bar_panels(panels: list[dict], path: str | Path, title: str = "", cols: int = 2,
               panel_w: int = 380, panel_h: int = 250) -> Path:
    """Write one SVG holding the panels in a grid and return its path."""
    rows = math.ceil(len(panels) / cols)
    head = 34 if title else 8
    W, H = cols * panel_w + 16, rows * panel_h + head + 8
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
             f'font-family="{FONT}" role="img" aria-label="{escape(title or "bar chart")}">',
             f'<rect width="{W}" height="{H}" fill="{SURFACE}"/>']
    if title:
        parts.append(f'<text x="{W / 2}" y="22" font-size="14.5" font-weight="600" text-anchor="middle" '
                     f'fill="{INK}">{escape(title)}</text>')
    for i, p in enumerate(panels):
        parts += _panel(p, 8 + (i % cols) * panel_w, head + (i // cols) * panel_h, panel_w - 12, panel_h - 8)
    parts.append("</svg>")
    path = Path(path)
    path.write_text("\n".join(parts) + "\n", encoding="utf-8")
    return path

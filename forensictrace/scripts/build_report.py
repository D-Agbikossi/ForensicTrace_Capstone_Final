#!/usr/bin/env python3
"""Render the project reports to PDF.

  technical  docs/technical_report.md            -> docs/ForensicTrace_Technical_Report.pdf
  general    docs/report_for_general_readers.md  -> docs/ForensicTrace_Report_for_General_Readers.pdf

Markdown: python3-markdown, or markdown-it-py as a fallback.
PDF: playwright + chromium, or a Chromium/Chrome binary in headless mode as a fallback.

Usage: python3 scripts/build_report.py [technical|general|all] [output.pdf]
       (default: all; an output path is only allowed for a single report)
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORTS = {
    "technical": ("technical_report.md", "ForensicTrace_Technical_Report.pdf"),
    "general": ("report_for_general_readers.md", "ForensicTrace_Report_for_General_Readers.pdf"),
}
CSS = """
@page { size: A4; margin: 15mm 16mm; }
body { font-family: 'DejaVu Sans', Arial, sans-serif; font-size: 9.8pt; line-height: 1.38; color: #111; }
h1 { font-size: 16pt; margin: 0 0 4px; color: #12284a; border-bottom: 3px solid #c8102e; padding-bottom: 3px; }
h2 { font-size: 11.6pt; margin: 11px 0 4px; color: #12284a; border-bottom: 1px solid #1f5fbf; }
h3 { font-size: 10.4pt; margin: 9px 0 3px; color: #1f5fbf; }
p { margin: 4px 0; orphans: 2; widows: 2; }
h2, p:has(+ table), p:has(+ img) { page-break-after: avoid; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 8.6pt; background: #f1f1f1; padding: 0 2px; }
table { border-collapse: collapse; width: 100%; margin: 4px 0; font-size: 8.4pt; }
thead { display: table-header-group; }
th, td { border: 1px solid #9aa6bb; padding: 2px 4px; vertical-align: top; } th { background: #e6edf7; color: #12284a; }
tr { page-break-inside: avoid; } img { display: block; margin: 3px auto; }
"""


def to_html(text):
    try:
        import markdown
        return markdown.markdown(text, extensions=["tables", "attr_list"])
    except ImportError:
        from markdown_it import MarkdownIt
        # markdown-it has no attr_list: turn ![alt](src){width=N%} into an <img> tag first
        text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)\{width=([0-9]+%)\}",
                      r'<img alt="\1" src="\2" style="width:\3">', text)
        return MarkdownIt("commonmark", {"html": True}).enable("table").render(text)


def print_pdf(html_path, out):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        browser = next((b for b in ("chromium", "chromium-browser", "google-chrome") if shutil.which(b)), None)
        if browser is None:
            sys.exit("need playwright or a chromium/google-chrome binary to print the PDF")
        # snap chromium cannot write to /tmp, so the HTML and PDF stay inside the repository
        subprocess.run([browser, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={out}", f"file://{html_path}"], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{html_path}")
        page.pdf(path=str(out), format="A4", print_background=True, prefer_css_page_size=True)
        browser.close()


def build(kind, out):
    source, _default = REPORTS[kind]
    body = to_html((ROOT / "docs" / source).read_text(encoding="utf-8"))
    body = body.replace('src="../results/', f'src="file://{ROOT}/results/')
    body = body.replace('src="screenshots/', f'src="file://{ROOT}/docs/screenshots/')
    html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>"
    tmp = out.with_suffix(".html")
    tmp.write_text(html, encoding="utf-8")
    print_pdf(tmp, out)
    tmp.unlink()
    print(f"wrote {out}")


def main():
    args = sys.argv[1:]
    which = args.pop(0) if args and args[0] in (*REPORTS, "all") else "all"
    kinds = list(REPORTS) if which == "all" else [which]
    if args and len(kinds) > 1:
        sys.exit("an output path can only be given for one report: technical or general")
    for kind in kinds:
        out = Path(args[0]).resolve() if args else ROOT / "docs" / REPORTS[kind][1]
        build(kind, out)


if __name__ == "__main__":
    main()

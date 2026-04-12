#!/usr/bin/env python3
"""
Generate a cover image from the newspaper-style template.

Usage:
  python3 generate_cover.py \
    --date "2026-04-13" \
    --source "Mario Zechner · Pi Agent 创造者" \
    --number "98" \
    --unit "%" \
    --data-line '<em>uptime</em> · 成了行业新常态' \
    --title 'Agent 时代的开发者<br>已经停不下来了' \
    --subtitle '造出最火 Agent 的人说<br><em>Slow the Fuck Down</em>' \
    --output /Users/odyzhou/Desktop/xhs-posts/covers/page-01.png

All arguments are optional except --output.
Template placeholders not filled will be left empty.
"""

import argparse, os, subprocess, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(SCRIPT_DIR, "cover_template.html")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def main():
    parser = argparse.ArgumentParser(description="Generate cover from template")
    parser.add_argument("--date", default="", help="Date string, e.g. 2026-04-13")
    parser.add_argument("--source", default="", help="Source line under header")
    parser.add_argument("--number", default="", help="Big number (visual anchor)")
    parser.add_argument("--unit", default="", help="Unit after big number (e.g. %, $, K+)")
    parser.add_argument("--data-line", default="", help="Explanatory line below number (HTML ok)")
    parser.add_argument("--title", default="", help="Main title (HTML ok, use <br> for line breaks)")
    parser.add_argument("--subtitle", default="", help="Subtitle / quote (HTML ok)")
    parser.add_argument("--output", required=True, help="Output PNG path")
    args = parser.parse_args()

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    replacements = {
        "{{DATE}}": args.date,
        "{{SOURCE}}": args.source,
        "{{BIG_NUMBER}}": args.number,
        "{{BIG_UNIT}}": args.unit,
        "{{DATA_LINE}}": args.data_line,
        "{{MAIN_TITLE}}": args.title,
        "{{SUBTITLE}}": args.subtitle,
    }

    for placeholder, value in replacements.items():
        html = html.replace(placeholder, value)

    # Write temporary HTML
    out_dir = os.path.dirname(args.output)
    tmp_html = os.path.join(out_dir, "_cover_tmp.html")
    with open(tmp_html, "w", encoding="utf-8") as f:
        f.write(html)

    # Screenshot
    result = subprocess.run([
        CHROME, "--headless=new", "--disable-gpu",
        f"--screenshot={args.output}",
        "--window-size=1080,1800",
        "--hide-scrollbars",
        f"file://{tmp_html}"
    ], capture_output=True, text=True)

    # Cleanup
    os.remove(tmp_html)

    if os.path.exists(args.output):
        print(f"✓ {args.output}")
    else:
        print(f"✗ FAILED: {result.stderr[:300]}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

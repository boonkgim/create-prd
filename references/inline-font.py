#!/usr/bin/env python3
"""Inline the Inter web font into a finished PRD, making it one self-contained file.

    python3 references/inline-font.py docs/<folder>/NN-prd.html

The template links the font as a sibling stylesheet so it renders while you are editing
it in place. A PRD gets handed to people and must survive being emailed on its own, so
this replaces that <link> with the font-face rule inlined.

Run it once, after the PRD is written. It is idempotent: a file with no <link> to
font-inter.css is left untouched, and the script says so rather than failing.
"""

import re
import sys
from pathlib import Path

LINK = re.compile(r'[ \t]*<link[^>]+href="(?:\./)?font-inter\.css"[^>]*>\n?', re.I)


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2

    target = Path(sys.argv[1])
    css = Path(__file__).with_name("font-inter.css")

    if not target.is_file():
        print(f"no such file: {target}", file=sys.stderr)
        return 1
    if not css.is_file():
        print(f"missing font stylesheet: {css}", file=sys.stderr)
        return 1

    html = target.read_text(encoding="utf-8")
    if not LINK.search(html):
        print(f"{target}: no font-inter.css link found — nothing to inline")
        return 0

    style = "<style>\n" + css.read_text(encoding="utf-8").rstrip() + "\n</style>\n"
    target.write_text(LINK.sub(style, html, count=1), encoding="utf-8")
    print(f"{target}: font inlined, now {target.stat().st_size // 1024} KB and self-contained")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

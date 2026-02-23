#!/usr/bin/env python3
"""
xhs-article post-processing script.

Enforces two formatting rules automatically:
  1. Replace 破折号（——）with Chinese colon（：）
  2. Remove ALL blank lines inside 正文 — no exceptions, including before ### and ---
"""

import sys
import re


def clean(filepath):
    with open(filepath, encoding='utf-8') as f:
        text = f.read()

    # Rule 1: replace 破折号
    text = text.replace('——', '：')

    # Rule 2: clean blank lines inside 正文 only
    BODY_MARKER = '## 正文\n'
    start = text.find(BODY_MARKER)
    if start == -1:
        _write(filepath, text)
        return
    start += len(BODY_MARKER)

    # Footer starts at the --- immediately before 参考资料
    m = re.search(r'\n---\n\n参考资料', text[start:])
    end = (start + m.start()) if m else len(text)

    header = text[:start]
    body   = text[start:end]
    footer = text[end:]

    # Remove all blank lines in body — no exceptions
    import re as _re
    body = _re.sub(r'\n{2,}', '\n', body)

    _write(filepath, header + body + footer)


def _write(filepath, text):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'✓ cleaned: {filepath}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage: python3 {sys.argv[0]} <file.md> [file2.md ...]')
        sys.exit(1)
    for fp in sys.argv[1:]:
        clean(fp)

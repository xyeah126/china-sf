#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扫描指定集合 frontmatter 中含中文的字段（排除 coverPrompt 等仅内部使用的字段）。

用法:
    python scripts/scan_cn_fields.py                 # 扫描 works/en 与 authors/en
    python scripts/scan_cn_fields.py works en --dump # 列出具体条目
"""
from __future__ import annotations

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CN = re.compile(r'[\u4e00-\u9fff]')
FM = re.compile(r'^---\r?\n(.*?)\r?\n---\r?\n', re.S)
# 仅内部使用的字段：不面向读者展示，允许保留中文
INTERNAL = {'coverPrompt', 'nameZh', 'titleZh'}

LIST_ITEM = re.compile(r'^([ \t]*)([A-Za-z_]+):[ \t]*$')


def scan(col: str, lang: str, dump: bool) -> None:
    d = os.path.join(ROOT, 'src/content', col, lang)
    if not os.path.isdir(d):
        print(f'[warn] 目录不存在 {col}/{lang}')
        return
    hits: dict[str, set[str]] = {}
    files_hit: set[str] = set()
    current_list: str | None = None
    for f in sorted(os.listdir(d)):
        if not f.endswith('.md'):
            continue
        text = open(os.path.join(d, f), encoding='utf-8').read()
        m = FM.match(text)
        if not m:
            continue
        for line in m.group(1).splitlines():
            if not line.strip():
                continue
            mlist = LIST_ITEM.match(line)
            if mlist:
                current_list = mlist.group(2)
                continue
            if line.startswith((' ', '\t', '-')):
                key = current_list or '?'
            else:
                mm = re.match(r'^([A-Za-z_]+):[ \t]*(.*)$', line)
                if not mm:
                    continue
                key, val = mm.group(1), mm.group(2)
                current_list = None
                if key in INTERNAL:
                    continue
                if CN.search(val):
                    hits.setdefault(key, set()).add(val.strip().strip('"'))
                    files_hit.add(f)
                continue
            if key in INTERNAL:
                continue
            if CN.search(line):
                val = line.strip()
                if val.startswith('- '):
                    val = val[2:].strip().strip('"')
                hits.setdefault(key, set()).add(val)
                files_hit.add(f)
    total = sum(len(v) for v in hits.values())
    print(f'[{col}/{lang}] 含中文的字段条目 {total} 个，涉及文件 {len(files_hit)} 个')
    if dump:
        for k in sorted(hits):
            print(f'  · {k} ({len(hits[k])}):')
            for v in sorted(hits[k]):
                print(f'      {v}')


def main() -> int:
    args = sys.argv[1:]
    dump = '--dump' in args
    pos = [a for a in args if not a.startswith('-')]
    targets = [(pos[0], pos[1])] if len(pos) >= 2 else [('works', 'en'), ('authors', 'en')]
    for col, lang in targets:
        scan(col, lang, dump)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())


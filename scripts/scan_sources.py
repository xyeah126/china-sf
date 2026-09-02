#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扫描 works 内容集合中的 sources 字段，统计中英文分布。

用法:
    python scripts/scan_sources.py            # 汇总统计
    python scripts/scan_sources.py --dump     # 列出全部唯一 sources 及出现文件
    python scripts/scan_sources.py --lang en  # 只看英文集合
"""
from __future__ import annotations

import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CN = re.compile(r'[\u4e00-\u9fff]')
FM = re.compile(r'^---\r?\n(.*?)\r?\n---\r?\n', re.S)
# sources 块: 形如
#   sources:
#     - "xxx"
#     - "yyy"
SRC = re.compile(r'^sources:[ \t]*\r?\n((?:[ \t]*-[ \t].*\r?\n|[ \t]+-[ \t]*\r?\n)*)', re.M)


def read(p: str) -> str:
    with open(p, encoding='utf-8') as f:
        return f.read()


def frontmatter(text: str) -> str | None:
    m = FM.match(text)
    return m.group(1) if m else None


def get_sources(fm: str) -> list[str]:
    m = SRC.search(fm)
    if not m:
        return []
    out = []
    for line in m.group(1).splitlines():
        line = line.strip()
        if line.startswith('-'):
            val = line[1:].strip().strip('"').strip("'")
            if val:
                out.append(val)
    return out


def main() -> int:
    args = sys.argv[1:]
    dump = '--dump' in args
    lang_filter = None
    if '--lang' in args:
        lang_filter = args[args.index('--lang') + 1]

    langs = [lang_filter] if lang_filter else ['zh', 'en']
    index: dict[str, list[tuple[str, str]]] = defaultdict(list)

    for lang in langs:
        d = os.path.join(ROOT, 'src/content/works', lang)
        if not os.path.isdir(d):
            print(f'[warn] 目录不存在: {d}')
            continue
        files = sorted(x for x in os.listdir(d) if x.endswith('.md'))
        n_cn = 0
        n_nosrc = 0
        n_total_src = 0
        for f in files:
            fm = frontmatter(read(os.path.join(d, f)))
            if fm is None:
                print(f'[warn] 无 frontmatter: {lang}/{f}')
                continue
            srcs = get_sources(fm)
            if not srcs:
                n_nosrc += 1
            n_total_src += len(srcs)
            if any(CN.search(s) for s in srcs):
                n_cn += 1
            for s in srcs:
                index[s].append((lang, f))
        print(f'[{lang}] 文件 {len(files)} | 含中文 sources 的文件 {n_cn} | '
              f'无 sources 的文件 {n_nosrc} | sources 条目总数 {n_total_src}')

    uniq = sorted(index)
    cn_uniq = [s for s in uniq if CN.search(s)]
    print(f'\n唯一 sources 条目 {len(uniq)} 个，其中含中文 {len(cn_uniq)} 个')
    if dump:
        for s in uniq:
            langs_ = sorted({l for l, _ in index[s]})
            print(f'  [{"含中" if CN.search(s) else "纯英"}] ({len(index[s])}x, {",".join(langs_)}) {s}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

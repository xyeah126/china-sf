#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""导出 works / authors 集合中英对照，供 sources 英译使用。

输出 scripts/data/meta_pairs.json:
  zh2en_title   : 中文书名 -> 英文书名
  zh2en_author  : 中文作者 -> 英文作者
  zh2en_pub     : 中文出版社 -> publisherEn
  en_titles     : 英文书名集合（用于反查是否已有约定译名）
"""
from __future__ import annotations

import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FM = re.compile(r'^---\r?\n(.*?)\r?\n---\r?\n', re.S)
KEY = re.compile(r'^([A-Za-z_]+):[ \t]*(.*)$')


def scalar_fm(fm: str) -> dict[str, str]:
    """只取顶层 `key: value` 标量字段，忽略列表/嵌套。"""
    out: dict[str, str] = {}
    for line in fm.splitlines():
        if line.startswith((' ', '\t', '-')):
            continue
        m = KEY.match(line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return out


def load(lang: str, col: str) -> dict[str, dict[str, str]]:
    d = os.path.join(ROOT, 'src/content', col, lang)
    out = {}
    if not os.path.isdir(d):
        return out
    for f in os.listdir(d):
        if not f.endswith('.md'):
            continue
        text = open(os.path.join(d, f), encoding='utf-8').read()
        m = FM.match(text)
        if not m:
            continue
        out[f[:-3]] = scalar_fm(m.group(1))
    return out


def main() -> int:
    zh_w = load('zh', 'works')
    en_w = load('en', 'works')
    zh_a = load('zh', 'authors')
    en_a = load('en', 'authors')

    zh2en_title: dict[str, str] = {}
    zh2en_pub: dict[str, str] = {}
    for slug, zw in zh_w.items():
        ew = en_w.get(slug)
        if not ew:
            continue
        if zw.get('title') and ew.get('title'):
            zh2en_title[zw['title']] = ew['title']
        pz, pe = zw.get('publisher'), ew.get('publisherEn') or ew.get('publisher')
        if pz and pe:
            zh2en_pub[pz] = pe

    zh2en_author: dict[str, str] = {}
    for slug, za in zh_a.items():
        ea = en_a.get(slug)
        if not ea:
            continue
        if za.get('name') and ea.get('name'):
            zh2en_author[za['name']] = ea['name']

    out = {
        'zh2en_title': zh2en_title,
        'zh2en_author': zh2en_author,
        'zh2en_pub': zh2en_pub,
        'en_titles': sorted({v['title'] for v in en_w.values() if v.get('title')}),
        'en_authors': sorted({v['name'] for v in en_a.values() if v.get('name')}),
        'en_pubs': sorted({(v.get('publisherEn') or v.get('publisher'))
                           for v in en_w.values() if (v.get('publisherEn') or v.get('publisher'))}),
    }
    os.makedirs(os.path.join(ROOT, 'scripts/data'), exist_ok=True)
    p = os.path.join(ROOT, 'scripts/data/meta_pairs.json')
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f'书名对照 {len(zh2en_title)} 条 / 作者对照 {len(zh2en_author)} 条 / 出版社对照 {len(zh2en_pub)} 条')
    print(f'输出: {p}')
    print('\n--- 出版社对照 ---')
    for k, v in sorted(zh2en_pub.items()):
        print(f'  {k} -> {v}')
    print('\n--- 作者名 ---')
    print('  ' + ', '.join(sorted(zh2en_author)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

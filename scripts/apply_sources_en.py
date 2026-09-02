#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 works/en/*.md 的 sources 与 publisher 字段英译并就地写回。

数据源: scripts/data/sources_en.json（人工翻译映射）
特性:
  - 默认 dry-run，只报告；加 --apply 才真正写文件
  - 覆盖率校验：任一 en 文件出现的 sources 原文不在映射表中 -> 报错退出，绝不半途写入
  - 幂等：已为英文的条目跳过，重复运行无副作用
  - publisher 字段：仅在英文集合仍是中文时替换为英译
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CN = re.compile(r'[\u4e00-\u9fff]')
FM = re.compile(r'^---\r?\n(.*?)\r?\n---\r?\n', re.S)
SRC = re.compile(r'^sources:[ \t]*\r?\n((?:[ \t]*-[ \t].*\r?\n|[ \t]*-[ \t]*\r?\n)*)', re.M)

# publisher 中文 -> 英文（英文集合 publisher 字段遗留中文值）
PUB_EN = {
    '世德堂本': 'Shidetang edition (Ming dynasty)',
    '中国少年儿童出版社': "China Children's Press",
    '中国青年出版社': 'China Youth Press',
    '人民文学出版社': "People's Literature Publishing House",
    '太平兴国官修': 'Imperially commissioned, Taiping Xingguo era',
    '小说林': 'Fiction Forest Press (Xiaoshuolin)',
    '改良小说社': 'Reformed Fiction Society',
    '新小说': 'New Fiction (Xin Xiaoshuo)',
    '日本东京进化社': 'Jinhua Society, Tokyo',
    '现代书局': 'Modern Book Company',
    '科幻世界': 'Science Fiction World',
    '绣像小说': 'Illustrated Fiction (Xiuxiang Xiaoshuo)',
    '重庆出版社': 'Chongqing Publishing House',
}


def load_map() -> dict[str, str]:
    p = os.path.join(ROOT, 'scripts/data/sources_en.json')
    data = json.load(open(p, encoding='utf-8'))
    return {k: v for k, v in data.items() if not k.startswith('_')}


def yaml_quote(s: str) -> str:
    """YAML 双引号标量转义。"""
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true', help='真正写入文件（默认 dry-run）')
    args = ap.parse_args()

    mapping = load_map()
    d = os.path.join(ROOT, 'src/content/works/en')
    files = sorted(f for f in os.listdir(d) if f.endswith('.md'))

    missing: dict[str, list[str]] = {}
    plan: list[tuple[str, str, str]] = []   # (file, old_text, new_text)
    n_src = 0
    n_pub = 0

    for f in files:
        p = os.path.join(d, f)
        text = open(p, encoding='utf-8').read()
        m = FM.match(text)
        if not m:
            print(f'[warn] 无 frontmatter: {f}')
            continue
        fm = m.group(1)
        new_fm = fm

        # --- sources ---
        ms = SRC.search(new_fm)
        if ms:
            block = ms.group(1)
            out_lines = []
            for line in block.splitlines():
                raw = line
                stripped = line.strip()
                if stripped.startswith('-'):
                    val = stripped[1:].strip().strip('"').strip("'")
                    if CN.search(val):
                        if val not in mapping:
                            missing.setdefault(val, []).append(f)
                            out_lines.append(raw)
                            continue
                        indent = line[: len(line) - len(line.lstrip())]
                        new_val = mapping[val]
                        out_lines.append(f'{indent}- {yaml_quote(new_val)}')
                        n_src += 1
                        plan.append((f, val, new_val))
                    else:
                        out_lines.append(raw)
                else:
                    out_lines.append(raw)
            new_block = '\n'.join(out_lines) + '\n'
            new_fm = new_fm[: ms.start(1)] + new_block + new_fm[ms.end(1):]

        # --- publisher ---
        for line in new_fm.splitlines():
            mm = re.match(r'^publisher:[ \t]*(.*)$', line)
            if mm:
                val = mm.group(1).strip().strip('"').strip("'")
                if val and CN.search(val):
                    if val not in PUB_EN:
                        missing.setdefault(f'[publisher] {val}', []).append(f)
                    else:
                        new_fm = new_fm.replace(
                            f'publisher: "{val}"', f'publisher: {yaml_quote(PUB_EN[val])}', 1
                        ).replace(
                            f"publisher: '{val}'", f'publisher: {yaml_quote(PUB_EN[val])}', 1
                        ).replace(
                            f'publisher: {val}', f'publisher: {yaml_quote(PUB_EN[val])}', 1
                        )
                        n_pub += 1
                        plan.append((f, f'publisher: {val}', f'publisher: {PUB_EN[val]}'))
                break

        if new_fm != fm:
            if args.apply:
                new_text = text[: m.start(1)] + new_fm + text[m.end(1):]
                with open(p, 'w', encoding='utf-8', newline='') as fp:
                    fp.write(new_text)

    if missing:
        print('[error] 以下原文缺少英译映射，已中止（未写入任何文件）:')
        for k, v in sorted(missing.items()):
            print(f'  {k}   <- {", ".join(sorted(set(v)))}')
        return 1

    print(f'[{"apply" if args.apply else "dry-run"}] 计划修改 sources {n_src} 条 / publisher {n_pub} 条，'
          f'涉及文件 {len({x[0] for x in plan})} 个')
    if not args.apply:
        print('\n前 15 条预览:')
        for f, o, n in plan[:15]:
            print(f'  {f}: {o}\n    -> {n}')
        print('\n确认无误后加 --apply 执行')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

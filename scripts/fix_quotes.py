# -*- coding: utf-8 -*-
"""
修复数据文件中的引号问题。

中文正文里直接敲 ASCII 双引号（"…"）会截断 Python 字符串，导致 SyntaxError。
本脚本把正文里的 ASCII 引号交替替换为全角「」，且不触碰结构引号。

正文在数据文件里有两种形态，都要处理：
  ① 单行字段："zh": {"title": "…", "body": "…内容…"},
  ② 多行拼接的续行：        "…内容…\n\n"

用法：
    python scripts/fix_quotes.py --check   # 只报告，不修改
    python scripts/fix_quotes.py           # 修复并写回
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")

# ① 单行字段里的 body / bio 值
BODY_RE = re.compile(r'("(?:body|bio)"\s*:\s*")(.*)("\s*\}\s*,?\s*)$')
# 形如 "slug": / "body": 的字段名行（续行不含这种结构，据此区分）
CONT_RE = re.compile(r'^\s*"[A-Za-z]+"\s*:')


def convert(inner):
    """把正文里的 ASCII 引号交替替换为「」，返回 (新文本, 是否有改动)"""
    if '"' not in inner:
        return inner, False

    out = []
    toggle = 0
    for ch in inner:
        if ch == '"':
            toggle += 1
            out.append("「" if toggle % 2 else "」")
        else:
            out.append(ch)
    return "".join(out), True


def fix_line(line):
    s = line.rstrip("\n")
    stripped = s.strip()

    # ① 单行字段
    m = BODY_RE.search(s)
    if m:
        new, ok = convert(m.group(2))
        if ok:
            return s[: m.start(2)] + new + s[m.end(2) :] + "\n"
        return line

    # ② 多行拼接的续行：整行就是一个字符串字面量，且不是字段名行
    #    必须跳过模块 docstring 的定界行（""" 单独一行），否则会破坏三引号
    if stripped in ('"""', '""', '"'):
        return line
    if stripped.startswith('"""') or stripped.endswith('"""'):
        return line
    if (
        stripped.startswith('"')
        and stripped.endswith('"')
        and not CONT_RE.match(stripped)
    ):
        new, ok = convert(stripped[1:-1])
        if ok:
            indent = s[: len(s) - len(s.lstrip())]
            return indent + '"' + new + '"' + "\n"

    return line


def main():
    check = "--check" in sys.argv
    total = 0

    for name in sorted(os.listdir(DATA)):
        if not name.endswith(".py"):
            continue
        path = os.path.join(DATA, name)
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()

        fixed = [fix_line(l) for l in lines]
        hits = sum(1 for a, b in zip(lines, fixed) if a != b)

        if hits:
            print("  %-24s %d 行" % (name, hits))
            total += hits
            if not check:
                with open(path, "w", encoding="utf-8") as f:
                    f.writelines(fixed)

    print("合计 %d 行%s" % (total, "（仅检查，未修改）" if check else "已修复"))


if __name__ == "__main__":
    main()

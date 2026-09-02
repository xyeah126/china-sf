# -*- coding: utf-8 -*-
"""按 scripts/data/new_entries.py 生成港台 / 海外华语 / 网络文学条目（中英双份）。

用法：
    python scripts/gen_new_entries.py           # dry-run，只打印计划
    python scripts/gen_new_entries.py --apply   # 真正写盘
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data.new_entries import AUTHORS, WORKS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTHORS_DIR = os.path.join(ROOT, "src", "content", "authors")
WORKS_DIR = os.path.join(ROOT, "src", "content", "works")


def y(v: str) -> str:
    """YAML 双引号标量转义。"""
    return '"' + str(v).replace("\\", "\\\\").replace('"', '\\"') + '"'


def ylist(items):
    if not items:
        return None
    return "\n".join(f"  - {y(i)}" for i in items)


def block(label: str, items):
    body = ylist(items)
    if body is None:
        return None
    return f"{label}:\n{body}"


def write(path: str, text: str, apply: bool, created: list, skipped: list):
    if os.path.exists(path):
        skipped.append(path)
        print(f"  [跳过·已存在] {os.path.relpath(path, ROOT)}")
        return
    created.append(path)
    print(f"  [新建] {os.path.relpath(path, ROOT)}")
    if apply:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)


# ---------------------------------------------------------------- authors
def build_author(slug: str, d: dict, lang: str) -> str:
    is_zh = lang == "zh"
    name = d["name"] if is_zh else d["nameEn"]
    awards = d["awards"] if is_zh else d["awardsEn"]
    body = d["bodyZh"] if is_zh else d["bodyEn"]
    # zh 保留中文笔名；en 只保留拉丁转写，避免 frontmatter 出现中文
    if is_zh:
        alias = [a for a in d["alias"] if not a.isascii()]
    else:
        alias = [a for a in d["alias"] if a.isascii()] or [d["nameEn"]]

    lines = ["---", f"name: {y(name)}"]
    b = block("alias", alias)
    if b:
        lines.append(b)
    lines.append(f"birthYear: {d['birthYear'] if d['birthYear'] is not None else 'null'}")
    lines.append(f"deathYear: {d['deathYear'] if d['deathYear'] is not None else 'null'}")
    lines.append(f"era: {y(d['era'])}")
    lines.append('photoCredit: "placeholder"')
    lines.append('translationStatus: "full"')
    b = block("awards", awards)
    if b:
        lines.append(b)
    lines.append("---")
    lines.append("")
    lines.append(body)
    return "\n".join(lines) + "\n"


# ------------------------------------------------------------------ works
def build_work(slug: str, d: dict, lang: str) -> str:
    is_zh = lang == "zh"
    title = d["title"] if is_zh else d["titleEn"]
    author = d["author"] if is_zh else d["authorEn"]
    publisher = d["publisher"] if is_zh else d["publisherEn"]
    tags = d["tags"] if is_zh else d["tagsEn"]
    sources = d["sources"] if is_zh else d["sourcesEn"]
    awards = d["awards"] if is_zh else d["awardsEn"]
    body = d["bodyZh"] if is_zh else d["bodyEn"]

    lines = [
        "---",
        f"title: {y(title)}",
        f"author: {y(author)}",
        f"authorSlug: {y(d['authorSlug'])}",
        f"year: {d['year']}",
        f"era: {y(d['era'])}",
        'kind: "sf"',
        f"publisher: {y(publisher)}",
        'coverCredit: "placeholder"',
    ]
    # coverPrompt 是给图像模型的指令，中英两份共用同一条（保持书名原文便于出图）
    lines.append(f"coverPrompt: {y(d['coverPrompt'])}")
    for label, items in (("tags", tags), ("sources", sources), ("awards", awards)):
        b = block(label, items)
        if b:
            lines.append(b)
    lines.append(f"featured: {'true' if d['featured'] else 'false'}")
    lines.append('translationStatus: "full"')
    lines.append("---")
    lines.append("")
    lines.append(body)
    return "\n".join(lines) + "\n"


def main():
    apply = "--apply" in sys.argv
    created, skipped = [], []

    print("=== 作者条目 ===")
    for slug, d in AUTHORS.items():
        for lang in ("zh", "en"):
            write(
                os.path.join(AUTHORS_DIR, lang, f"{slug}.md"),
                build_author(slug, d, lang),
                apply,
                created,
                skipped,
            )

    print("=== 作品条目 ===")
    for slug, d in WORKS.items():
        for lang in ("zh", "en"):
            write(
                os.path.join(WORKS_DIR, lang, f"{slug}.md"),
                build_work(slug, d, lang),
                apply,
                created,
                skipped,
            )

    print()
    print(f"新建 {len(created)} 个，跳过 {len(skipped)} 个（已存在）")
    if not apply:
        print("（dry-run：未写盘，加 --apply 执行）")


if __name__ == "__main__":
    main()

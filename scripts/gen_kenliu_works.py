# -*- coding: utf-8 -*-
"""生成刘宇昆补录作品条目（中英双份）。

复用 gen_new_entries.build_work 保证字段规范一致；生成后紧接着写入 cover 字段，
避免上一轮「先生成再补 cover」被 re.sub 反向引用坑到的流程。

用法：
    python scripts/gen_kenliu_works.py            # dry-run
    python scripts/gen_kenliu_works.py --apply    # 写盘
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data.kenliu_works import WORKS  # noqa: E402
from gen_new_entries import build_work  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKS_DIR = os.path.join(ROOT, "src", "content", "works")


def inject_cover(text: str, slug: str) -> str:
    """把 coverCredit: "placeholder" 替换为 cover + ai-generated。

    上一轮的教训：不要在 Bash 内联里用 re.sub 的 \\1 反向引用，
    Bash 单引号传参后会被吞掉。这里用纯 str.replace，最稳。
    """
    old = 'coverCredit: "placeholder"'
    new = f'cover: "/covers/{slug}.webp"\ncoverCredit: "ai-generated"'
    assert old in text, f"未找到占位 credit 行：{slug}"
    return text.replace(old, new, 1)


def main():
    apply = "--apply" in sys.argv
    n_new = n_skip = 0

    for slug, d in WORKS.items():
        for lang in ("zh", "en"):
            path = os.path.join(WORKS_DIR, lang, f"{slug}.md")
            text = inject_cover(build_work(slug, d, lang), slug)
            rel = os.path.relpath(path, ROOT)
            if os.path.exists(path):
                print(f"  [跳过·已存在] {rel}")
                n_skip += 1
                continue
            print(f"  [新建] {rel}")
            if apply:
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w", encoding="utf-8", newline="\n") as f:
                    f.write(text)
            n_new += 1

    print(f"\n计划新建 {n_new} 个文件，跳过 {n_skip} 个")
    if not apply:
        print("（dry-run：加 --apply 才写盘）")


if __name__ == "__main__":
    main()

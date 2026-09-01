# -*- coding: utf-8 -*-
"""
内容质量检查（数据写完后跑一遍）。

检查项：
  1. ASCII 引号   —— 中文正文里的直引号会截断 Python 字符串，必须用「」
  2. 英文混入汉字 —— 英文条目里出现汉字视为笔误
  3. 中文简介字数 —— 作品简介目标 300–500 字，超出范围会提示
  4. 引用完整性   —— workSlug / authorSlug 不得悬空

用法：
    python scripts/check_content.py
退出码：有 ERROR 时为 1，仅 WARN 时为 0。
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
sys.path.insert(0, DATA)

from works_early import WORKS_EARLY            # noqa: E402
from works_modern_a import WORKS_MODERN_A      # noqa: E402
from works_modern_b import WORKS_MODERN_B      # noqa: E402
from authors_data import AUTHORS               # noqa: E402
from adaptations_data import ADAPTATIONS as ADAPTATIONS_BASE   # noqa: E402
from adaptations_extra import ADAPTATIONS_EXTRA                # noqa: E402
from extras import EXTRA                                       # noqa: E402

ADAPTATIONS = ADAPTATIONS_BASE + ADAPTATIONS_EXTRA

HAN = re.compile(r"[\u4e00-\u9fff]")
ASCII_QUOTE = re.compile(r'[\u4e00-\u9fff]"[\u4e00-\u9fff]')

ZH_MIN, ZH_MAX = 300, 520   # 目标 300–500，上限留一点余量


def full(slug, text):
    """正文 + 补充段落（与 gen_content 的 body_of 保持一致）"""
    e = EXTRA.get(slug)
    return text + "\n\n" + e["zh"] if e else text


def main():
    works = WORKS_EARLY + WORKS_MODERN_A + WORKS_MODERN_B
    errors = []
    warns = []

    # ---- 作品
    for w in works:
        slug = w["slug"]
        zh = w.get("zh", {}).get("body", "")
        en = w.get("en", {}).get("body", "")

        n = len(HAN.findall(full(slug, zh)))
        if n < ZH_MIN or n > ZH_MAX:
            warns.append("work  %-28s 中文简介 %d 字（目标 %d–%d）"
                         % (slug, n, ZH_MIN, ZH_MAX - 20))
        if ASCII_QUOTE.search(zh):
            errors.append("work  %-28s 中文正文含 ASCII 引号" % slug)
        if en and HAN.search(en):
            errors.append("work  %-28s 英文正文混入汉字" % slug)

    # ---- 作者
    for a in AUTHORS:
        if a.get("en", {}).get("bio") and HAN.search(a["en"]["bio"]):
            errors.append("author %-27s 英文简介混入汉字" % a["slug"])
        if ASCII_QUOTE.search(a.get("zh", {}).get("bio", "")):
            errors.append("author %-27s 中文简介含 ASCII 引号" % a["slug"])

    # ---- 影视
    for d in ADAPTATIONS:
        if d.get("en", {}).get("body") and HAN.search(d["en"]["body"]):
            errors.append("adapt  %-27s 英文简介混入汉字" % d["slug"])
        if ASCII_QUOTE.search(d.get("zh", {}).get("body", "")):
            errors.append("adapt  %-27s 中文简介含 ASCII 引号" % d["slug"])

    # ---- 引用完整性
    wslugs = {w["slug"] for w in works}
    aslugs = {a["slug"] for a in AUTHORS}
    for d in ADAPTATIONS:
        ws = d.get("workSlug")     # 可选：原创剧本等无原著
        if ws and ws not in wslugs:
            errors.append("adapt  %-27s workSlug 悬空：%s" % (d["slug"], ws))
    for w in works:
        if w.get("authorSlug") and w["authorSlug"] not in aslugs:
            errors.append("work  %-28s authorSlug 悬空：%s"
                          % (w["slug"], w["authorSlug"]))

    # ---- 报告
    print("作品 %d 部 / 作者 %d 位 / 影视 %d 部"
          % (len(works), len(AUTHORS), len(ADAPTATIONS)))
    print("-" * 60)

    if warns:
        print("WARN %d 条：" % len(warns))
        for w in warns:
            print("  · " + w)
    else:
        print("WARN 0 条")

    print("-" * 60)
    if errors:
        print("ERROR %d 条：" % len(errors))
        for e in errors:
            print("  !! " + e)
    else:
        print("ERROR 0 条 · 全部通过")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

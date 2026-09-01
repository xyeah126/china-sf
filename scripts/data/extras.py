# -*- coding: utf-8 -*-
"""合并三批「简介补充段落」，供 gen_content.py 与 check_content.py 共用。

合并规则：
- A / B 两批按 slug 覆盖（每部作品最多命中其中一批）
- C 批是对已存在条目的**追加**，不覆盖——用于把仍差几十字的作品补足
"""

from works_extra_a import EXTRA_A
from works_extra_b import EXTRA_B
from works_extra_c import EXTRA_C

EXTRA = {}
EXTRA.update(EXTRA_A)
EXTRA.update(EXTRA_B)

for _slug, _c in EXTRA_C.items():
    if _slug in EXTRA:
        EXTRA[_slug] = {
            "zh": EXTRA[_slug]["zh"] + "\n\n" + _c["zh"],
            "en": EXTRA[_slug]["en"] + "\n\n" + _c["en"],
        }
    else:
        EXTRA[_slug] = _c

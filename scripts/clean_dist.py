# -*- coding: utf-8 -*-
"""
清理构建产物。

用途：某些沙箱环境下 Astro 清理 dist/.prerender 时的删除操作会被拦截，
导致 build 失败。构建前先手动清干净，可避开该问题。

用法：
    python scripts/clean_dist.py
"""

import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys

TARGETS = [
    os.path.join(ROOT, "dist"),
    os.path.join(ROOT, ".astro"),  # Astro 的内容缓存与生成的 schema
]

# 可传参数只清指定目录，如：python scripts/clean_dist.py .astro
targets = [os.path.join(ROOT, a) for a in sys.argv[1:]] if len(sys.argv) > 1 else TARGETS

for path in targets:
    if os.path.exists(path):
        shutil.rmtree(path, ignore_errors=True)
        print("cleaned:", path)
    else:
        print("nothing to clean:", path)

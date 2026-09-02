# -*- coding: utf-8 -*-
"""新封面后处理：裁底部 → 居中裁 3:4 → 缩放 → 转 WebP → 备份原图。

关键参数（实测得出，勿随意改）：
  CROP_BOTTOM = 0.14
    ImageGen 会在竖版图底部加水印「AI生成」，并误加伪作者名与伪出版社名
    （如「卜宏敏 著」「MingPiaw Press」），位置约在图高 92% 处。
    裁 8% 不够、10% 不够、12% 也不够，14% 才能彻底剔除；再往上会切到画面主体。

用法：
    python scripts/process_new_covers.py <slug> [<slug> ...]
"""
from __future__ import annotations

import os
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COVERS = os.path.join(ROOT, "public", "covers")
SOURCE = os.path.join(ROOT, "public", "covers_source")

TARGET_W, TARGET_H = 900, 1200
RATIO = TARGET_W / TARGET_H  # 0.75
CROP_BOTTOM = 0.14
QUALITY = 82


def process(slug: str) -> bool:
    src = os.path.join(COVERS, f"{slug}.png")
    if not os.path.exists(src):
        print(f"  [跳过] 无原图 {slug}.png")
        return False

    im = Image.open(src).convert("RGB")
    w, h = im.size

    # 1) 裁掉底部（含水印与伪作者/出版社）
    im = im.crop((0, 0, w, int(h * (1 - CROP_BOTTOM))))
    w, h = im.size

    # 2) 居中裁 3:4
    if w / h > RATIO:
        nw = int(h * RATIO)
        left = (w - nw) // 2
        im = im.crop((left, 0, left + nw, h))
    else:
        nh = int(w / RATIO)
        top = (h - nh) // 2
        im = im.crop((0, top, w, top + nh))

    # 3) 缩放并转 WebP
    im = im.resize((TARGET_W, TARGET_H), Image.LANCZOS)
    out = os.path.join(COVERS, f"{slug}.webp")
    im.save(out, "WEBP", quality=QUALITY, method=6)

    # 4) 原图归档备份（covers_source 在 .gitignore 内，不入库）
    os.makedirs(SOURCE, exist_ok=True)
    dst = os.path.join(SOURCE, f"{slug}.png")
    if os.path.exists(dst):
        os.remove(dst)
    os.rename(src, dst)

    print(f"  {slug}: {im.size[0]}x{im.size[1]} webp  {os.path.getsize(out) / 1024:.0f} KB")
    return True


def main():
    slugs = sys.argv[1:]
    if not slugs:
        print(__doc__)
        return
    ok = sum(process(s) for s in slugs)
    print(f"\n处理完成 {ok}/{len(slugs)}")


if __name__ == "__main__":
    main()

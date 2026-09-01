# -*- coding: utf-8 -*-
"""
封面图优化：按设计文档 6.4 规范统一处理
  - 居中裁切为 3:4（与 CSS .cover 的 object-fit: cover 行为一致，不额外损失画面）
  - 缩放至 900 × 1200
  - 转 WebP（quality 82，method 6）

安全策略：原图**移动到 public/covers_source/**（不删除），随时可回溯。
同时自动更新 src/content/works/{zh,en}/*.md 的 cover 字段扩展名。

用法：
  python scripts/optimize_covers.py --dry-run   # 只看会做什么
  python scripts/optimize_covers.py             # 实际执行
"""
import os
import re
import shutil
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit("需要 Pillow：pip install Pillow")

SRC = "public/covers"
BACKUP = "public/covers_source"
TARGET_W, TARGET_H = 900, 1200
QUALITY = 82
TARGET_RATIO = TARGET_W / TARGET_H  # 0.75

DRY = "--dry-run" in sys.argv


def center_crop(im: Image.Image) -> Image.Image:
    w, h = im.size
    if abs(w / h - TARGET_RATIO) < 0.005:
        return im
    if w / h > TARGET_RATIO:
        # 过宽 → 裁左右
        new_w = int(h * TARGET_RATIO)
        left = (w - new_w) // 2
        return im.crop((left, 0, left + new_w, h))
    # 过高 → 裁上下
    new_h = int(w / TARGET_RATIO)
    top = (h - new_h) // 2
    return im.crop((0, top, w, top + new_h))


def main():
    os.makedirs(BACKUP, exist_ok=True)
    files = sorted(
        f for f in os.listdir(SRC)
        if f.lower().endswith((".png", ".jpg", ".jpeg")) and not f.lower().endswith(".webp")
    )
    print(f"待处理 {len(files)} 张  [{'(预演)' if DRY else '实际执行'}]")

    before = after = 0
    converted = []

    for f in files:
        src_path = os.path.join(SRC, f)
        before += os.path.getsize(src_path)
        stem = os.path.splitext(f)[0]
        dst_name = f"{stem}.webp"
        dst_path = os.path.join(SRC, dst_name)

        try:
            with Image.open(src_path) as im:
                im = im.convert("RGB")
                im = center_crop(im)
                im = im.resize((TARGET_W, TARGET_H), Image.LANCZOS)
                if not DRY:
                    im.save(dst_path, "WEBP", quality=QUALITY, method=6)
                    after += os.path.getsize(dst_path)
        except Exception as e:
            print(f"  ! {f} 失败: {e}")
            continue

        converted.append((f, dst_name))
        if not DRY:
            # 原图移到 covers_source（不删除，可回溯）
            shutil.move(src_path, os.path.join(BACKUP, f))
        print(f"  ✓ {f} → {dst_name}")

    # 更新 frontmatter 扩展名
    if not DRY:
        changed = 0
        for lang in ("zh", "en"):
            d = f"src/content/works/{lang}"
            if not os.path.exists(d):
                continue
            for md in os.listdir(d):
                if not md.endswith(".md"):
                    continue
                p = os.path.join(d, md)
                txt = open(p, encoding="utf-8").read()
                new = txt
                for old_name, new_name in converted:
                    new = new.replace(f"/covers/{old_name}", f"/covers/{new_name}")
                if new != txt:
                    open(p, "w", encoding="utf-8").write(new)
                    changed += 1
        print(f"\nfrontmatter 更新 {changed} 个文件")

    mb = lambda b: f"{b/1024/1024:.1f} MB"
    if DRY:
        print(f"\n预演完成：{len(converted)} 张待转换，原图合计 {mb(before)}")
    else:
        saved = before - after
        print(
            f"\n完成：{len(converted)} 张\n"
            f"  原图 {mb(before)} → WebP {mb(after)}  （省 {mb(saved)}，降 {saved/max(before,1)*100:.0f}%）\n"
            f"  原图已移至 {BACKUP}/（已加入 .gitignore，不入库）"
        )


if __name__ == "__main__":
    main()

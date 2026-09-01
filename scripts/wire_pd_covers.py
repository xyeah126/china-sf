#!/usr/bin/env python3
# 将 Wikimedia Commons 公有领域配图写入作品 frontmatter（zh + en）
# 与 AI 图不同：公版图必须带 coverSource（来源页 URL），否则不得标注 public-domain。
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKS_DIR = ROOT / "src" / "content" / "works"

# slug -> (封面文件, Commons 文件页 URL, 说明)
PD_COVERS = {
    "shanhaijing": (
        "/covers/shanhaijing.jpg",
        "https://commons.wikimedia.org/wiki/File:Nine-headed_phoenix,_from_a_color_edition_of_Shan_Hai_Jing.jpg",
        "山海经彩绘插图·九头凤（公有领域）",
    ),
    "huainanzi": (
        "/covers/huainanzi.jpg",
        "https://commons.wikimedia.org/wiki/File:%E8%8E%8A%E9%80%B5%E5%90%89%E6%9C%AC%E3%80%8A%E6%B7%AE%E5%8D%97%E5%AD%90%E3%80%8B.jpg",
        "莊逵吉本《淮南子》书影（公有领域）",
    ),
    "liezi-tangwen": (
        "/covers/liezi-tangwen.jpg",
        "https://commons.wikimedia.org/wiki/File:Liezi-1921.jpg",
        "《列子》1921 年版书影（公有领域）",
    ),
    "xiyouji": (
        "/covers/xiyouji.jpg",
        "https://commons.wikimedia.org/wiki/File:The_Journey_to_the_West,_Shidetang_Hall_of_Jinling_in_1592.jpg",
        "1592 年金陵世德堂刊本《西游记》书影（公有领域）",
    ),
}

CREDIT = "public-domain"


def update_file(path: Path, cover: str, source: str, note: str):
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        print(f"SKIP (no frontmatter): {path}")
        return
    end = text.find('\n---\n', 4)
    if end == -1:
        print(f"SKIP (malformed): {path}")
        return
    fm = text[4:end]
    body = text[end + 5:]

    def upsert(fm_text, key, value):
        val = f'"{value}"' if isinstance(value, str) else value
        if re.search(rf'^{key}:\s*', fm_text, re.M):
            return re.sub(rf'^{key}:.*$', f'{key}: {val}', fm_text, flags=re.M)
        return fm_text + f'\n{key}: {val}'

    fm = upsert(fm, 'cover', cover)
    fm = upsert(fm, 'coverCredit', CREDIT)
    fm = upsert(fm, 'coverSource', source)
    fm = upsert(fm, 'coverPrompt', note)

    path.write_text(f"---\n{fm}\n---\n{body}", encoding='utf-8')
    print(f"UPDATED: {path}")


def main():
    for slug, (cover, source, note) in PD_COVERS.items():
        for lang in ('zh', 'en'):
            p = WORKS_DIR / lang / f"{slug}.md"
            if p.exists():
                update_file(p, cover, source, note)
            else:
                print(f"MISSING: {p}")


if __name__ == '__main__':
    main()

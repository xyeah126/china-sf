#!/usr/bin/env python3
# 将生成的 AI 封面路径写入对应作品 frontmatter（zh + en）
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKS_DIR = ROOT / "src" / "content" / "works"

PROMPTS = {
    "santi": "Chinese science fiction paperback book cover for '三体' (The Three-Body Problem). A lone astronaut silhouette stands before three suns burning in a crimson sky above a desolate alien landscape with a derelict civilization. Retro-futuristic, ink-wash meets cosmic horror, muted teal and amber palette, dramatic chiaroscuro lighting. Vertical poster composition, title text '三体' clearly visible near top.",
    "heian-senlin": "Chinese science fiction paperback book cover for '黑暗森林' (The Dark Forest). A vast dark cosmic forest filled with barely visible hidden civilizations and dormant stars; a lone spaceship drifts between silhouetted leaf-like space habitats. Retro-futuristic, ink-wash meets cosmic noir, muted teal and amber palette, dramatic lighting. Vertical poster, title text '黑暗森林' clearly visible near top.",
    "sishen-yongsheng": "Chinese science fiction paperback book cover for '死神永生' (Death's End). A universe dissolving into crystalline fragments, a lone figure standing at the edge of a collapsing dimension, pale dying stars. Retro-futuristic, ink-wash meets cosmic horror, muted teal and amber palette, dramatic lighting. Vertical poster, title text '死神永生' clearly visible near top.",
    "liulang-diqiu": "Chinese science fiction paperback book cover for '流浪地球' (The Wandering Earth). Planet Earth equipped with colossal glowing thrusters leaving a frozen blue-white surface behind, drifting through a starfield with Jupiter looming in the distance. Retro-futuristic, ink-wash meets cosmic, muted teal and amber palette, dramatic lighting. Vertical poster, title text '流浪地球' clearly visible near top.",
    "qiuzhuang-shandian": "Chinese science fiction paperback book cover for '球状闪电' (Ball Lightning). Electric-blue ball lightning hovering above a night city, energy tendrils crackling, stormy sky reflected in glass towers. Retro-futuristic, ink-wash meets plasma energy, muted teal and amber palette, dramatic lighting. Vertical poster, title text '球状闪电' clearly visible near top.",
    "chaoxinxing-jiyuan": "Chinese science fiction paperback book cover for '超新星纪元' (The Era of Supernova). A world of children under a sky torn by supernova light, abandoned city playground bathed in gold and violet aurora. Retro-futuristic, ink-wash meets apocalyptic dawn, muted teal and amber palette, dramatic lighting. Vertical poster, title text '超新星纪元' clearly visible near top.",
    "xiangcun-jiaoshi": "Chinese science fiction paperback book cover for '乡村教师' (The Village Teacher). A tiny mountain village schoolhouse under an immense galaxy, a teacher silhouette at the doorway facing cosmic light, contrast between humble earth and infinite stars. Retro-futuristic, ink-wash meets cosmic, muted teal and amber palette, dramatic lighting. Vertical poster, title text '乡村教师' clearly visible near top.",
    "daishang-ta-de-yanjing": "Chinese science fiction paperback book cover for '带上她的眼睛' (With Her Eyes). An astronaut's gloved hand gently holding a small luminous camera-eye, planet Earth reflected in its lens, soft starfield behind. Retro-futuristic, ink-wash meets poetic sci-fi, muted teal and amber palette, dramatic lighting. Vertical poster, title text '带上她的眼睛' clearly visible near top.",
}

COVER_CREDIT = 'ai-generated'


def update_file(path: Path, slug: str):
    text = path.read_text(encoding='utf-8')
    prompt = PROMPTS[slug]

    # 确保 frontmatter 存在
    if not text.startswith('---\n'):
        print(f"SKIP (no frontmatter): {path}")
        return

    # 提取 frontmatter
    end = text.find('\n---\n', 4)
    if end == -1:
        print(f"SKIP (malformed frontmatter): {path}")
        return
    fm = text[4:end]
    body = text[end + 5:]

    # 更新 / 插入 cover 行
    if re.search(r'^cover:\s*', fm, re.M):
        fm = re.sub(r'^cover:.*$', f'cover: "/covers/{slug}.png"', fm, flags=re.M)
    else:
        fm = f'cover: "/covers/{slug}.png"\n' + fm

    # 更新 / 插入 coverCredit 行
    if re.search(r'^coverCredit:\s*', fm, re.M):
        fm = re.sub(r'^coverCredit:.*$', f'coverCredit: "{COVER_CREDIT}"', fm, flags=re.M)
    else:
        fm = fm.replace(f'cover: "/covers/{slug}.png"\n',
                        f'cover: "/covers/{slug}.png"\ncoverCredit: "{COVER_CREDIT}"\n')

    # 更新 / 插入 coverPrompt 行
    escaped_prompt = prompt.replace('\\', '\\\\').replace('"', '\\"')
    if re.search(r'^coverPrompt:\s*', fm, re.M):
        fm = re.sub(r'^coverPrompt:.*$', f'coverPrompt: "{escaped_prompt}"', fm, flags=re.M)
    else:
        fm = fm.replace(f'coverCredit: "{COVER_CREDIT}"\n',
                        f'coverCredit: "{COVER_CREDIT}"\ncoverPrompt: "{escaped_prompt}"\n')

    new_text = f"---\n{fm}\n---\n{body}"
    path.write_text(new_text, encoding='utf-8')
    print(f"UPDATED: {path}")


def main():
    for slug in PROMPTS:
        for lang in ('zh', 'en'):
            path = WORKS_DIR / lang / f"{slug}.md"
            if path.exists():
                update_file(path, slug)
            else:
                print(f"MISSING: {path}")


if __name__ == '__main__':
    main()

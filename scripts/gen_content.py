# -*- coding: utf-8 -*-
"""
生成全量内容：30 位作者 / 84 部作品 / 12 部影视改编，全部中英双语。

用法：
    python scripts/gen_content.py            # 全量生成（覆盖同名文件）
    python scripts/gen_content.py --dry      # 只统计，不写文件

数据源在 scripts/data/ 下，按时代与作者分文件维护，避免单文件过大。
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(HERE, "data")
BASE = os.path.join(ROOT, "src", "content")
sys.path.insert(0, DATA)

from authors_data import AUTHORS                      # noqa: E402
from works_early import WORKS_EARLY                   # noqa: E402
from works_modern_a import WORKS_MODERN_A             # noqa: E402
from works_modern_b import WORKS_MODERN_B             # noqa: E402
from adaptations_data import ADAPTATIONS as ADAPTATIONS_BASE   # noqa: E402
from adaptations_extra import ADAPTATIONS_EXTRA                # noqa: E402
from adaptations_meta import ADAPTATION_META                   # noqa: E402
from extras import EXTRA                                       # noqa: E402

WORKS = WORKS_EARLY + WORKS_MODERN_A + WORKS_MODERN_B

# 影视 = 文学改编（第一批）+ 非文学改编 / 软科幻（第二批）
ADAPTATIONS = ADAPTATIONS_BASE + ADAPTATIONS_EXTRA

# 豆瓣评分快照日期：静态数据，不实时同步
SNAPSHOT_DATE = "2026-08-31"


def body_of(w, lang):
    """正文 + 补充段落（若有）"""
    body = w[lang]["body"]
    extra = EXTRA.get(w["slug"])
    if extra:
        body = body + "\n\n" + extra[lang]
    return body

# 作者 slug → 英文名（英文条目的 author 字段用）
AUTHOR_EN = {a["slug"]: a["en"]["name"] for a in AUTHORS}

# 标签中英映射；未命中的标签保留中文原文（不硬翻）
TAG_MAP = {
    "神话": "myth", "志怪": "supernatural", "异兽": "legendary-creatures",
    "地理": "geography", "博物": "natural-history", "异域": "faraway-lands",
    "机械": "machinery", "飞行器": "flying-machines", "奇器": "strange-devices",
    "道家": "daoism", "哲学": "philosophy", "天文": "astronomy",
    "周穆王": "king-mu", "西行": "journey-west", "仙山": "immortal-isles",
    "鬼神": "ghosts-and-gods", "变形": "metamorphosis", "登月": "moon-landing",
    "类书": "leishu", "辑录": "compilation", "神魔": "gods-and-demons",
    "变化": "transformation", "取经": "pilgrimage", "寓言": "allegory",
    "海外奇国": "overseas-realms", "机械想象": "mechanical-imagination",
    "未来记": "future-history", "政治小说": "political-novel", "乌托邦": "utopia",
    "译介": "translation", "凡尔纳": "jules-verne", "月球": "moon",
    "气球": "balloon", "首部": "first-work", "灵魂": "soul", "星球": "planets",
    "晚清": "late-qing", "理想国": "utopia", "科技奇观": "technological-marvels",
    "续书": "sequel", "上海": "shanghai", "预言": "prophecy",
    "火星": "mars", "社会批判": "social-criticism",
    "科普": "popular-science", "战时": "wartime", "短篇集": "short-story-collection",
    "建设": "construction", "太空": "space", "考古": "archaeology",
    "探险": "exploration", "儿童科幻": "childrens-sf", "动物": "animals",
    "科学": "science", "宇宙航行": "spaceflight", "新时期": "new-era",
    "激光武器": "laser-weapon", "科幻复苏": "revival", "神秘": "mystery",
    "海洋": "ocean", "未来": "future", "冥王星": "pluto",
    "飞行": "flight", "梦境": "dreams", "心理学": "psychology",
    "网络": "network", "赛博": "cyber", "1990年代": "1990s",
    "磁场": "magnetism", "悬疑": "suspense", "时间旅行": "time-travel",
    "悖论": "paradox", "物理学": "physics", "环境": "environment",
    "灾难": "disaster", "基因": "genetics", "伦理": "ethics",
    "银河奖": "galaxy-award", "虚拟现实": "virtual-reality", "身份": "identity",
    "克隆": "cloning", "社会": "society", "群体": "collective",
    "宇宙学": "cosmology", "末日": "apocalypse", "硬科幻": "hard-sf",
    "文明": "civilisation", "未来史": "future-history", "荒诞": "absurd",
    "都市": "urban", "异化": "alienation", "医疗": "medical",
    "身体": "body", "死亡": "death", "数字": "digital",
    "现实": "reality", "情感": "emotion", "孤独": "loneliness",
    "物理": "physics", "宇宙": "cosmos", "数学": "mathematics",
    "离别": "parting", "技术": "technology", "地球内部": "earths-interior",
    "短篇": "short-story", "太阳危机": "solar-crisis", "流浪": "wandering",
    "外星文明": "alien-civilisation", "教育": "education",
    "量子": "quantum", "武器": "weapons", "黑暗森林": "dark-forest",
    "威慑": "deterrence", "维度": "dimensions", "阶层": "stratification",
    "空间": "space", "雨果奖": "hugo-award", "长篇": "novel",
    "火星文明": "martian-civilisation", "成长": "coming-of-age",
    "赛博朋克": "cyberpunk", "全球化": "globalisation",
    "人工智能": "artificial-intelligence", "算法": "algorithms",
    "意识": "consciousness", "同人": "fan-fiction", "三体": "three-body",
    "时间循环": "time-loop", "历史": "history", "意象": "imagery",
    "星云奖": "nebula-award", "幻想": "fantasy", "共生": "symbiosis",
    "宗教": "religion", "太空歌剧": "space-opera", "银河": "galaxy",
    "系列": "series", "演化": "evolution", "信息": "information",
    "控制": "control", "城市": "city", "气候": "climate",
    "人文": "humanities", "饥荒": "famine", "太阳": "sun",
    "生物学": "biology", "化学": "chemistry", "地质": "geology",
}


def en_tags(tags):
    return [TAG_MAP.get(t, t) for t in tags]


def q(v):
    """把 Python 值转成安全的 YAML 标量。

    字符串统一双引号（避免中文标点引发的解析问题）；
    数字与布尔必须原样输出——否则 doubanRating 会被 YAML 读成字符串，
    导致 Zod 校验失败。
    """
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v).replace("\\", "\\\\").replace('"', '\\"')
    return '"%s"' % s


def dump(front, body, path):
    lines = ["---"]
    for k, v in front.items():
        if isinstance(v, list):
            if not v:
                lines.append("%s: []" % k)
            else:
                lines.append("%s:" % k)
                for item in v:
                    lines.append("  - %s" % q(item))
        else:
            lines.append("%s: %s" % (k, q(v)))
    lines.append("---")
    lines.append("")
    lines.append(body.strip())
    lines.append("")

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def gen_works(dry):
    n = 0
    for w in WORKS:
        common = {
            "year": w.get("year"),
            "era": w["era"],
            "kind": w["kind"],
            "coverCredit": w.get("coverCredit", "placeholder"),
        }
        for key in ("yearUncertain", "publisher", "publisherEn",
                    "coverSource", "coverPrompt", "adaptations",
                    "sources", "featured"):
            if w.get(key):
                common[key] = w[key]

        # 中文条目
        fz = {
            "title": w["zh"]["title"],
            "author": w.get("author"),
            "authorSlug": w.get("authorSlug"),
        }
        fz.update(common)
        fz["tags"] = w.get("tags", [])
        fz["translationStatus"] = "full"
        p = os.path.join(BASE, "works", "zh", w["slug"] + ".md")
        if not dry:
            dump(fz, body_of(w, "zh"), p)
        n += 1

        # 英文条目
        if "en" in w:
            fe = {"title": w["en"]["title"]}
            fe["author"] = AUTHOR_EN.get(w.get("authorSlug"), w.get("author"))
            fe["authorSlug"] = w.get("authorSlug")
            fe.update(common)
            if w.get("publisherEn"):
                fe["publisher"] = w["publisherEn"]
            fe["tags"] = en_tags(w.get("tags", []))
            fe["translationStatus"] = "full"
            p = os.path.join(BASE, "works", "en", w["slug"] + ".md")
            if not dry:
                dump(fe, body_of(w, "en"), p)
            n += 1
    return n


def gen_authors(dry):
    for a in AUTHORS:
        for lang in ("zh", "en"):
            f = {
                "name": a[lang]["name"],
                "birthYear": a.get("birth"),
                "deathYear": a.get("death"),
                "era": a["era"],
                "photoCredit": "placeholder",
                "translationStatus": "full",
            }
            p = os.path.join(BASE, "authors", lang, a["slug"] + ".md")
            if not dry:
                dump(f, a[lang]["bio"], p)
    return len(AUTHORS) * 2


def gen_adaptations(dry):
    for d in ADAPTATIONS:
        rating = ADAPTATION_META.get(d["slug"], {}).get("doubanRating")
        for lang in ("zh", "en"):
            f = {
                "title": d[lang]["title"],
                "year": d.get("year"),
                "type": d["type"],
                "status": d["status"],
                # 原创剧本等无对应文学条目时，workSlug 为空（页面按 sourceType 显示来源）
                "workSlug": d.get("workSlug"),
                "sourceType": d.get("sourceType", "novel"),
                "director": d.get("director"),
                "studio": d.get("studio"),
                "platform": d.get("platform"),
                "posterCredit": d.get("posterCredit", "placeholder"),
            }
            if d.get("cast"):
                f["cast"] = d["cast"]
            if d.get("awards"):
                f["awards"] = d["awards"]
            # 豆瓣评分为静态快照，须同时写入抓取日期
            if rating is not None:
                f["doubanRating"] = rating
                f["doubanRatingAt"] = SNAPSHOT_DATE
            f["translationStatus"] = "full"
            # 去掉空值，保持 frontmatter 干净
            f = {k: v for k, v in f.items() if v is not None}
            p = os.path.join(BASE, "adaptations", lang, d["slug"] + ".md")
            if not dry:
                dump(f, d[lang]["body"], p)
    return len(ADAPTATIONS) * 2


def main():
    dry = "--dry" in sys.argv

    nw = gen_works(dry)
    na = gen_authors(dry)
    nd = gen_adaptations(dry)

    print("works       : %d 部 → %d 个 md 文件（含中英）" % (len(WORKS), nw))
    print("authors     : %d 位 → %d 个 md 文件" % (len(AUTHORS), na))
    print("adaptations : %d 部 → %d 个 md 文件" % (len(ADAPTATIONS), nd))
    print("合计        : %d 个文件 %s" % (nw + na + nd, "(dry run)" if dry else "已写入"))

    # 校验：影视 workSlug 是可选的（原创剧本等无原著），填了就必须能对应到作品
    slugs = {w["slug"] for w in WORKS}
    for d in ADAPTATIONS:
        ws = d.get("workSlug")
        if ws and ws not in slugs:
            print("  !! adaptation '%s' 的 workSlug '%s' 未找到对应作品"
                  % (d["slug"], ws))
    # 校验：作品 authorSlug 必须能对应到作者
    aslugs = {a["slug"] for a in AUTHORS}
    for w in WORKS:
        if w.get("authorSlug") and w["authorSlug"] not in aslugs:
            print("  !! work '%s' 的 authorSlug '%s' 未找到对应作者"
                  % (w["slug"], w["authorSlug"]))


if __name__ == "__main__":
    main()

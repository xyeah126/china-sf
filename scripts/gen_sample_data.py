# -*- coding: utf-8 -*-
"""
生成 P0 示例数据（中英双语）。

用法：
    python scripts/gen_sample_data.py

生成 src/content/{works,authors,adaptations}/{zh,en}/*.md
覆盖上古 → 前科幻 → 晚清 → 新中国 → 当代五个时期，用于验证双语 schema 与时间线。

注意：示例数据不含真实封面文件（cover 留空），页面会渲染占位块；
      真实配图在 P5 阶段按「公版优先」SOP 采集后补入。
"""

import os

BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src", "content")


def q(v):
    """把 Python 值转成安全的 YAML 标量（统一双引号，避免中文冒号等解析问题）。"""
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, int):
        return str(v)
    s = str(v).replace("\\", "\\\\").replace('"', '\\"')
    return '"%s"' % s


def dump(front, body, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    lines = ["---"]
    for k, v in front.items():
        if isinstance(v, list):
            if not v:
                lines.append("%s: []" % k)
            elif v and isinstance(v[0], dict):
                lines.append("%s:" % k)
                for item in v:
                    first = True
                    for ik, iv in item.items():
                        prefix = "  - " if first else "    "
                        lines.append("%s%s: %s" % (prefix, ik, q(iv)))
                        first = False
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
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("  wrote", os.path.relpath(path, BASE))


# ---------------------------------------------------------------- 作品 WORKS

WORKS = [
    {
        "slug": "shanhaijing",
        "zh": {
            "title": "山海经",
            "author": "佚名",
            "authorSlug": "anonymous",
            "year": None,
            "yearUncertain": True,
            "era": "shanggu",
            "kind": "myth",
            "coverCredit": "public-domain",
            "coverSource": "https://commons.wikimedia.org/wiki/Category:Shanhaijing",
            "tags": ["神话", "志怪", "异兽", "地理"],
            "featured": True,
            "translationStatus": "full",
            "sources": ["《山海经》中华书局点校本", "袁行霈《中国文学史》"],
        },
        "zh_body": """
中国先秦重要古籍，分《山经》与《海经》两部分，记载山川、道里、民族、物产、祭祀与巫医，
保存了夸父逐日、精卫填海、大禹治水等大量远古神话。

书中那些异兽、异国与奇物的想象，构成了后世志怪小说、乃至中国科学想象的一条隐秘源头。
本站将其列为「神话源流」层，而非科幻本身。
""",
        "en": {
            "title": "Classic of Mountains and Seas",
            "author": "Anonymous",
            "authorSlug": "anonymous",
            "year": None,
            "yearUncertain": True,
            "era": "shanggu",
            "kind": "myth",
            "coverCredit": "public-domain",
            "coverSource": "https://commons.wikimedia.org/wiki/Category:Shanhaijing",
            "tags": ["myth", "supernatural", "legendary-creatures", "geography"],
            "featured": True,
            "translationStatus": "full",
            "sources": ["Zhonghua Book Company edition", "Yuan Xingpei, A History of Chinese Literature"],
        },
        "en_body": """
A foundational pre-Qin compendium, divided into the Classic of Mountains and the
Classic of Seas. It records mountains, rivers, peoples, products, sacrifices and
shamanic medicine, preserving a vast body of archaic myth: Kuafu chasing the sun,
Jingwei filling the sea, Yu taming the flood.

Its bestiary of strange creatures, distant lands and marvellous objects forms a
hidden source for later tales of the strange — and, eventually, for Chinese
scientific imagination. This archive classifies it as Myth, not science fiction.
""",
    },
    {
        "slug": "jinghuayuan",
        "zh": {
            "title": "镜花缘",
            "titleEn": "Flowers in the Mirror",
            "author": "李汝珍",
            "authorSlug": "liruzhen",
            "year": 1828,
            "era": "song-ming-qing",
            "kind": "proto-sf",
            "coverCredit": "public-domain",
            "coverSource": "https://shuge.org/",
            "tags": ["海外奇国", "机械想象", "寓言"],
            "featured": True,
            "translationStatus": "full",
            "sources": ["《镜花缘》人民文学出版社", "李汝珍《镜花缘》清刻本"],
        },
        "zh_body": """
清代李汝珍所著长篇小说。前半部写唐敖、林之洋等人游历海外诸国——君子国、女儿国、
无肠国、两面国等，以奇国异俗寄寓社会批判与理想。

书中出现了飞车等机械想象与海外世界的系统构想，被视为中国古代最具科幻色彩的
「前科幻」作品之一。
""",
        "en": {
            "title": "Flowers in the Mirror",
            "author": "Li Ruzhen",
            "authorSlug": "liruzhen",
            "year": 1828,
            "era": "song-ming-qing",
            "kind": "proto-sf",
            "coverCredit": "public-domain",
            "coverSource": "https://shuge.org/",
            "tags": ["fantastic-voyage", "machinery", "allegory"],
            "featured": True,
            "translationStatus": "full",
            "sources": ["People's Literature Publishing House edition", "Qing woodblock edition"],
        },
        "en_body": """
A Qing-dynasty novel by Li Ruzhen. Its first half follows Tang Ao, Lin Zhiyang
and companions across overseas realms — the Country of Gentlemen, the Country of
Women, the Country of the Gutless, the Two-Faced Country — using exotic customs
as vehicles for social critique.

The book contains mechanical imaginings such as flying carriages and a systematic
vision of lands beyond the sea, making it one of the most science-fictional works
of pre-modern China. Classified here as Proto-SF.
""",
    },
    {
        "slug": "yueqiu",
        "zh": {
            "title": "月球殖民地小说",
            "titleEn": "Moon Colony Novel",
            "author": "荒江钓叟",
            "authorSlug": "huangjiangdiaosou",
            "year": 1904,
            "era": "wanqing",
            "kind": "sf",
            "publisher": "绣像小说（连载）",
            "coverCredit": "public-domain",
            "coverSource": "https://archive.org/",
            "tags": ["月球", "气球", "晚清", "首部"],
            "featured": True,
            "translationStatus": "full",
            "sources": ["《绣像小说》1904 年连载", "吴岩《中国科幻文学的历史》"],
        },
        "zh_body": """
晚清小说，作者署名「荒江钓叟」，1904 年起连载于《绣像小说》。

作品讲述中国人乘气球游历月球的故事，情节融冒险、志怪与新知于一体。
它被公认为**中国第一部原创科幻长篇**，是中文科幻的起点坐标。
""",
        "en": {
            "title": "Moon Colony Novel",
            "author": "Hermit of the Deserted River",
            "authorSlug": "huangjiangdiaosou",
            "year": 1904,
            "era": "wanqing",
            "kind": "sf",
            "publisher": "Illustrated Fiction (serial)",
            "coverCredit": "public-domain",
            "coverSource": "https://archive.org/",
            "tags": ["moon", "balloon", "late-qing", "first-novel"],
            "featured": True,
            "translationStatus": "full",
            "sources": ["Illustrated Fiction serial, 1904", "Wu Yan, A History of Chinese SF Literature"],
        },
        "en_body": """
A Late Qing novel published under the pen name "Hermit of the Deserted River",
serialised from 1904 in the journal Illustrated Fiction.

It follows Chinese travellers who fly to the Moon by balloon, blending adventure,
the marvellous, and new scientific knowledge. It is widely recognised as
**the first original Chinese science fiction novel** — the coordinate zero of
Chinese SF.
""",
    },
    {
        "slug": "shanhudao",
        "zh": {
            "title": "珊瑚岛上的死光",
            "titleEn": "Death Ray on a Coral Island",
            "author": "童恩正",
            "authorSlug": "tongenzheng",
            "year": 1978,
            "era": "xinzhongguo",
            "kind": "sf",
            "publisher": "人民文学出版社",
            "coverCredit": "placeholder",
            "tags": ["激光武器", "科幻复苏", "新时期"],
            "adaptations": ["shanhudao-film-1980"],
            "featured": True,
            "translationStatus": "full",
            "sources": ["《人民文学》1978 年第 5 期", "童恩正《珊瑚岛上的死光》小说集"],
        },
        "zh_body": """
童恩正 1978 年发表的短篇科幻小说，讲述科学家研制高效激光武器、挫败境外势力阴谋的故事。

它被视为「新时期」科幻复苏的标志性作品之一，1980 年被改编为中国第一部科幻题材电影，
影响了一代读者对科技与国家的想象。
""",
        "en": {
            "title": "Death Ray on a Coral Island",
            "author": "Tong Enzheng",
            "authorSlug": "tongenzheng",
            "year": 1978,
            "era": "xinzhongguo",
            "kind": "sf",
            "publisher": "People's Literature Publishing House",
            "coverCredit": "placeholder",
            "tags": ["laser-weapon", "revival", "new-era"],
            "adaptations": ["shanhudao-film-1980"],
            "featured": True,
            "translationStatus": "full",
            "sources": ["People's Literature, issue 5, 1978", "Tong Enzheng, collected stories"],
        },
        "en_body": """
A 1978 short story by Tong Enzheng in which scientists develop a high-efficiency
laser weapon and foil a foreign conspiracy.

It is regarded as one of the signature works of the post-1978 revival of Chinese
science fiction, and was adapted in 1980 into China's first science fiction film,
shaping a generation's imagination of technology and nationhood.
""",
    },
    {
        "slug": "santi",
        "zh": {
            "title": "三体",
            "titleEn": "The Three-Body Problem",
            "author": "刘慈欣",
            "authorSlug": "liucixin",
            "year": 2006,
            "era": "dangdai",
            "kind": "sf",
            "publisher": "重庆出版社",
            "publisherEn": "Chongqing Publishing House",
            "coverCredit": "ai-generated",
            "coverPrompt": "深空背景下三颗恒星的混乱轨道，冷色调水墨质感科幻插画，几何化星图元素",
            "tags": ["硬科幻", "外星文明", "宇宙社会学", "雨果奖"],
            "adaptations": ["santi-anime-2022", "santi-tv-2023"],
            "featured": True,
            "translationStatus": "full",
            "sources": ["重庆出版社 2008 年版", "2015 年雨果奖最佳长篇小说"],
        },
        "zh_body": """
刘慈欣代表作，「地球往事」三部曲第一部。文革背景下的秘密工程「红岸」向宇宙发出信号，
四光年外的三体文明由此锁定了地球。

三部曲以「黑暗森林」法则为轴心，展开一场横跨数百年的文明存亡博弈。
2015 年获雨果奖最佳长篇小说，是亚洲首次获此奖项的长篇作品。
""",
        "en": {
            "title": "The Three-Body Problem",
            "author": "Liu Cixin",
            "authorSlug": "liucixin",
            "year": 2006,
            "era": "dangdai",
            "kind": "sf",
            "publisher": "Chongqing Publishing House",
            "coverCredit": "ai-generated",
            "coverPrompt": "chaotic orbits of three suns in deep space, cold-toned ink-wash sci-fi illustration, geometric star chart elements",
            "tags": ["hard-sf", "alien-civilization", "cosmic-sociology", "hugo-award"],
            "adaptations": ["santi-anime-2022", "santi-tv-2023"],
            "featured": True,
            "translationStatus": "full",
            "sources": ["Chongqing Publishing House, 2008", "Hugo Award for Best Novel, 2015"],
        },
        "en_body": """
Liu Cixin's breakthrough work and the first volume of the Remembrance of Earth's
Past trilogy. Against the backdrop of the Cultural Revolution, the secret "Red
Coast" project sends a signal into space — and the Trisolaran civilisation four
light-years away locks onto Earth.

The trilogy turns on the "dark forest" rule, unfolding a centuries-long struggle
for civilisational survival. It won the 2015 Hugo Award for Best Novel, the first
Asian novel to receive the prize.
""",
    },
]

# ---------------------------------------------------------------- 作者 AUTHORS

AUTHORS = [
    {
        "slug": "anonymous",
        "zh": {
            "name": "佚名",
            "era": "shanggu",
            "photoCredit": "placeholder",
            "translationStatus": "full",
        },
        "zh_body": """
上古经典多由集体累积而成，作者不可考。《山海经》《穆天子传》《神异经》等均归入此条目，
不虚构具体作者。
""",
        "en": {
            "name": "Anonymous",
            "era": "shanggu",
            "photoCredit": "placeholder",
            "translationStatus": "full",
        },
        "en_body": """
Classical works of antiquity were typically accreted collectively, with no
attributable author. The Classic of Mountains and Seas, the Tale of King Mu, and
the Classic of Divine Marvels are all filed under this entry rather than assigned
an invented author.
""",
    },
    {
        "slug": "liruzhen",
        "zh": {
            "name": "李汝珍",
            "nameEn": "Li Ruzhen",
            "birthYear": 1763,
            "deathYear": 1830,
            "era": "song-ming-qing",
            "photoCredit": "placeholder",
            "translationStatus": "full",
        },
        "zh_body": """
清代小说家，字松石，直隶大兴（今北京）人。博通经史、音韵、医算，
以二十年之力著成《镜花缘》一百回。

书中海外诸国的奇俗与机械想象，使其成为中国「前科幻」叙事的代表人物。
""",
        "en": {
            "name": "Li Ruzhen",
            "birthYear": 1763,
            "deathYear": 1830,
            "era": "song-ming-qing",
            "photoCredit": "placeholder",
            "translationStatus": "full",
        },
        "en_body": """
A Qing novelist, styled Songshi, from Daxing (present-day Beijing). Erudite in
classics, phonology, medicine and mathematics, he spent two decades writing the
hundred-chapter Flowers in the Mirror.

Its exotic customs and mechanical imaginings make him the representative figure
of Chinese proto-science-fiction narrative.
""",
    },
    {
        "slug": "huangjiangdiaosou",
        "zh": {
            "name": "荒江钓叟",
            "nameEn": "Hermit of the Deserted River",
            "era": "wanqing",
            "photoCredit": "placeholder",
            "translationStatus": "full",
        },
        "zh_body": """
晚清小说家，真实姓名与生平不详，以笔名「荒江钓叟」行世。

1904 年起在《绣像小说》连载《月球殖民地小说》，是中国科幻长篇的起点作者。
""",
        "en": {
            "name": "Hermit of the Deserted River",
            "era": "wanqing",
            "photoCredit": "placeholder",
            "translationStatus": "full",
        },
        "en_body": """
A Late Qing novelist whose real name and biography remain unknown, writing under
the pen name "Hermit of the Deserted River".

From 1904 he serialised Moon Colony Novel in Illustrated Fiction, making him the
founding author of the Chinese science fiction novel.
""",
    },
    {
        "slug": "tongenzheng",
        "zh": {
            "name": "童恩正",
            "nameEn": "Tong Enzheng",
            "birthYear": 1935,
            "deathYear": 1997,
            "era": "xinzhongguo",
            "photoCredit": "placeholder",
            "translationStatus": "full",
        },
        "zh_body": """
考古学家、科幻作家，曾任四川大学教授。1960 年代开始科幻创作，
1978 年发表《珊瑚岛上的死光》，成为新时期科幻复苏的标志性人物。

其作品将科学考据与文学想象结合，是「学者型科幻」的代表。
""",
        "en": {
            "name": "Tong Enzheng",
            "birthYear": 1935,
            "deathYear": 1997,
            "era": "xinzhongguo",
            "photoCredit": "placeholder",
            "translationStatus": "full",
        },
        "en_body": """
Archaeologist and science fiction writer, professor at Sichuan University. He
began writing SF in the 1960s; the 1978 publication of Death Ray on a Coral
Island made him a signature figure of the post-1978 revival.

His work fused scholarly rigour with literary imagination, exemplifying
"scholarly science fiction".
""",
    },
    {
        "slug": "liucixin",
        "zh": {
            "name": "刘慈欣",
            "nameEn": "Liu Cixin",
            "birthYear": 1963,
            "deathYear": None,
            "era": "dangdai",
            "photoCredit": "placeholder",
            "translationStatus": "full",
        },
        "zh_body": """
中国当代最具国际影响力的科幻作家，生于 1963 年，长期从事工程工作。

代表作《三体》三部曲、《球状闪电》《流浪地球》《乡村教师》。
2015 年凭《三体》获雨果奖最佳长篇小说，为中文科幻赢得世界关注。

> 按本站版权规范，在世作者不使用真实照片，头像位以占位图或文字卡片代替。
""",
        "en": {
            "name": "Liu Cixin",
            "birthYear": 1963,
            "deathYear": None,
            "era": "dangdai",
            "photoCredit": "placeholder",
            "translationStatus": "full",
        },
        "en_body": """
China's most internationally influential contemporary science fiction writer,
born 1963, long employed as an engineer.

His major works include the Remembrance of Earth's Past trilogy, Ball Lightning,
The Wandering Earth and The Rural Teacher. He won the 2015 Hugo Award for Best
Novel for The Three-Body Problem, bringing Chinese SF to world attention.

> Per this archive's image policy, no real photograph is used for living authors;
> the portrait slot falls back to a placeholder or a text card.
""",
    },
]

# ------------------------------------------------------- 影视改编 ADAPTATIONS

ADAPTATIONS = [
    {
        "slug": "shanhudao-film-1980",
        "zh": {
            "title": "珊瑚岛上的死光",
            "workSlug": "shanhudao",
            "year": 1980,
            "type": "film",
            "status": "released",
            "director": "张鸿眉",
            "studio": "上海电影制片厂",
            "posterCredit": "placeholder",
            "translationStatus": "full",
        },
        "zh_body": """
改编自童恩正同名短篇小说，1980 年上映，通常被认为是中国第一部科幻题材故事片。
""",
        "en": {
            "title": "Death Ray on a Coral Island",
            "workSlug": "shanhudao",
            "year": 1980,
            "type": "film",
            "status": "released",
            "director": "Zhang Hongmei",
            "studio": "Shanghai Film Studio",
            "posterCredit": "placeholder",
            "translationStatus": "full",
        },
        "en_body": """
Adapted from Tong Enzheng's short story of the same name and released in 1980;
generally regarded as China's first science fiction feature film.
""",
    },
    {
        "slug": "santi-anime-2022",
        "zh": {
            "title": "三体",
            "titleEn": "The Three-Body Problem",
            "workSlug": "santi",
            "year": 2022,
            "type": "animation",
            "status": "released",
            "studio": "哔哩哔哩",
            "platform": "哔哩哔哩",
            "posterCredit": "placeholder",
            "translationStatus": "full",
        },
        "zh_body": """
由哔哩哔哩出品的动画版《三体》，2022 年上线。
""",
        "en": {
            "title": "The Three-Body Problem",
            "workSlug": "santi",
            "year": 2022,
            "type": "animation",
            "status": "released",
            "studio": "Bilibili",
            "platform": "Bilibili",
            "posterCredit": "placeholder",
            "translationStatus": "full",
        },
        "en_body": """
An animated adaptation of The Three-Body Problem produced by Bilibili, released
in 2022.
""",
    },
    {
        "slug": "santi-tv-2023",
        "zh": {
            "title": "三体",
            "titleEn": "The Three-Body Problem",
            "workSlug": "santi",
            "year": 2023,
            "type": "tv",
            "status": "released",
            "director": "杨磊",
            "platform": "腾讯视频",
            "posterCredit": "placeholder",
            "awards": ["第 34 届中国电视剧飞天奖"],
            "translationStatus": "full",
        },
        "zh_body": """
腾讯视频出品的电视剧版《三体》，杨磊执导，2023 年播出，
以高度还原原著的选角与叙事获得广泛讨论。
""",
        "en": {
            "title": "The Three-Body Problem",
            "workSlug": "santi",
            "year": 2023,
            "type": "tv",
            "status": "released",
            "director": "Yang Lei",
            "platform": "Tencent Video",
            "posterCredit": "placeholder",
            "awards": ["34th Flying Apsaras Awards"],
            "translationStatus": "full",
        },
        "en_body": """
A television adaptation produced by Tencent Video and directed by Yang Lei,
broadcast in 2023; widely discussed for its faithful casting and storytelling.
""",
    },
]


def main():
    print("Generating sample data into", BASE)
    for w in WORKS:
        slug = w["slug"]
        dump(w["zh"], w["zh_body"], os.path.join(BASE, "works", "zh", slug + ".md"))
        dump(w["en"], w["en_body"], os.path.join(BASE, "works", "en", slug + ".md"))
    for a in AUTHORS:
        slug = a["slug"]
        dump(a["zh"], a["zh_body"], os.path.join(BASE, "authors", "zh", slug + ".md"))
        dump(a["en"], a["en_body"], os.path.join(BASE, "authors", "en", slug + ".md"))
    for d in ADAPTATIONS:
        slug = d["slug"]
        dump(d["zh"], d["zh_body"], os.path.join(BASE, "adaptations", "zh", slug + ".md"))
        dump(d["en"], d["en_body"], os.path.join(BASE, "adaptations", "en", slug + ".md"))
    print("Done.")


if __name__ == "__main__":
    main()

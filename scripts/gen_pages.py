# -*- coding: utf-8 -*-
"""
生成双语页面薄封装。

用法：
    python scripts/gen_pages.py

页面本身只负责传 lang，真正的渲染逻辑在 src/components/pages/*.astro，
这样中英文站共用一套实现，不会出现两份逻辑漂移。
新增页面只需在下面的 SIMPLE_PAGES / DETAIL_PAGES 里加一行。
"""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = os.path.join(ROOT, "src", "pages")

SIMPLE_TMPL = """---
import {component} from '{up}components/pages/{component}.astro';
---

<{component} lang="{lang}" />
"""

DETAIL_TMPL = """---
import type {{ GetStaticPaths }} from 'astro';
import {component} from '{up}components/pages/{component}.astro';
import {{ {dataFn} }} from '{up}lib/content';

export const getStaticPaths = (async () => {{
  const items = await {dataFn}('{lang}');
  return items.map((x) => ({{
    params: {{ slug: x.slug }},
    props: {{ entry: x.entry, slug: x.slug, isFallback: x.isFallback }},
  }}));
}}) satisfies GetStaticPaths;

const {{ entry, slug, isFallback }} = Astro.props;
---

<{component} entry={{entry}} lang="{lang}" slug={{slug}} isFallback={{isFallback}} />
"""

# (相对 pages 的路径, 组件名, 语言)
SIMPLE_PAGES = [
    ("index.astro", "Home", "zh"),
    ("en/index.astro", "Home", "en"),
    ("timeline.astro", "TimelineView", "zh"),
    ("en/timeline.astro", "TimelineView", "en"),
    ("works/index.astro", "WorksIndex", "zh"),
    ("en/works/index.astro", "WorksIndex", "en"),
    ("authors/index.astro", "AuthorsIndex", "zh"),
    ("en/authors/index.astro", "AuthorsIndex", "en"),
    ("adaptations/index.astro", "AdaptationsIndex", "zh"),
    ("en/adaptations/index.astro", "AdaptationsIndex", "en"),
    ("about.astro", "About", "zh"),
    ("en/about.astro", "About", "en"),
    ("search.astro", "SearchPage", "zh"),
    ("en/search.astro", "SearchPage", "en"),
]

# (相对 pages 的路径, 组件名, 数据函数, 语言)
DETAIL_PAGES = [
    ("works/[slug].astro", "WorkDetail", "getWorks", "zh"),
    ("en/works/[slug].astro", "WorkDetail", "getWorks", "en"),
    ("authors/[slug].astro", "AuthorDetail", "getAuthors", "zh"),
    ("en/authors/[slug].astro", "AuthorDetail", "getAuthors", "en"),
]


def depth_of(rel):
    """页面相对 src/pages 的层级，决定 '../' 的个数（src 再往下一层）。"""
    parts = rel.split("/")[:-1]  # 去掉文件名
    return len(parts) + 1


def write(rel, content):
    path = os.path.join(PAGES, *rel.split("/"))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("  wrote src/pages/" + rel)


def main():
    for rel, component, lang in SIMPLE_PAGES:
        up = "../" * depth_of(rel)
        write(rel, SIMPLE_TMPL.format(component=component, up=up, lang=lang))

    for rel, component, data_fn, lang in DETAIL_PAGES:
        up = "../" * depth_of(rel)
        write(
            rel,
            DETAIL_TMPL.format(
                up=up, lang=lang, component=component, dataFn=data_fn
            ),
        )

    print("Done.")


if __name__ == "__main__":
    main()

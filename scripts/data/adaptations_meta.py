# -*- coding: utf-8 -*-
"""影视条目元数据补充（按 slug 索引）：豆瓣评分等。

说明：
- 只填有把握的评分，不确定的一律留空（页面不显示），避免编造数据。
- 这是**静态快照**，不是实时同步：doubanRatingAt 在 gen_content.py 里统一注入。
- 回链在页面组件中生成豆瓣搜索链接（无需在此维护精确条目 URL）。

合规口径：非商业、小规模、标注来源与快照日期、回链导流，不实时同步。
"""

ADAPTATION_META = {
    # ---- 西游记系列
    "xiyouji-tv-1986": {"doubanRating": 9.7},
    "dahuaxiyou-dasheng": {"doubanRating": 9.2},
    "dahuaxiyou-yueguang": {"doubanRating": 8.9},
    "xiyouji-dashengguilai": {"doubanRating": 8.3},
    "xiyou-jiangmopian": {"doubanRating": 7.1},
    # ---- 当代科幻
    "santi-tv-2023": {"doubanRating": 8.6},
    "liulang-diqiu-film-2019": {"doubanRating": 7.9},
    "liulang-diqiu-2": {"doubanRating": 8.3},
    "fengkuang-de-waixingren": {"doubanRating": 6.5},
    # ---- 新增：非文学改编 / 软科幻（评分见 adaptations_extra.py，此处留空亦可）
    "duxing-yueqiu": {"doubanRating": 6.8},
    "mingri-zhanji": {"doubanRating": 5.4},
    "shanghai-baolei": {"doubanRating": 2.9},
    # 以下评分待核对，暂留空：
    # "santi-anime-2022", "three-body-netflix", "xiyouji-danaotiangong",
    # "xiyouji-sandabaigujing", "shanhaijing-chiying", "shanhudao-film-1980",
    # "pili-beibei", "daqiceng-xiaoshi", "changjiang-qihao", "jixia-xia",
    # "chaoneng-yijiaren", "xiongchumo-chongfan-diqiu", "meirenyu"
}

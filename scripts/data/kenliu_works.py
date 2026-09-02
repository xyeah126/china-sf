# -*- coding: utf-8 -*-
"""刘宇昆（Ken Liu）其余重要作品补录。

背景：站点此前只收录了《手中纸，心中爱》一篇，与刘宇昆的实际创作体量严重不符。
经核实，其创作至少涵盖 4 部长篇（蒲公英王朝系列）+ 2 部短篇集 + 百余篇短篇，
另有 2 部主编的中国科幻英译选集与大量译作。

本次补录 5 部：按「站内可独立成条且有中文读者认知基础」标准筛选
  1. 蒲公英王朝：七王之战  —— 首部长篇，丝绸朋克开创，轨迹奖最佳处女作
  2. 物哀                  —— 2013 雨果奖最佳短篇（蝉联）
  3. 狩猎愉快              —— 2016 日本星云赏，2019 改编入《爱，死亡和机器人》
  4. 纪录片：终结历史之人  —— 雨果/星云/斯特金三奖决选中篇，历史责任主题
  5. 爱的算法              —— 中国读者认识刘宇昆的起点（2009《科幻世界》）

译名说明：
  The Grace of Kings 正式中译本为《蒲公英王朝：七王之战》（江苏凤凰文艺 2018），
  维基等处另见直译《国王的恩典》，站内以正式出版译名为准，直译名写入正文说明。

era 全部为 dangdai（1991 年起，与 src/content/eras.yaml 一致）。
"""

WORKS = {
    # ------------------------------------------------------------------ 1
    "pugongying-wangchao": {
        "title": "蒲公英王朝：七王之战",
        "titleEn": "The Grace of Kings",
        "author": "刘宇昆",
        "authorEn": "Ken Liu",
        "authorSlug": "kenliu",
        "year": 2015,
        "era": "dangdai",
        "publisher": "Saga Press（中文版：江苏凤凰文艺出版社 2018）",
        "publisherEn": "Saga Press (Chinese edition: Jiangsu Phoenix Literature and Art Publishing House, 2018)",
        "coverPrompt": "Chinese science fiction epic novel cover for '蒲公英王朝：七王之战' (The Grace of Kings). Silkpunk: giant silk airships and war kites above an archipelago of islands, a mechanical narwhal submarine surfacing beside bamboo-and-silk war machines, two rival warlords facing off on a windswept shore. East Asian ink-wash meets epic fantasy, jade green and gold palette, monumental scale. Vertical poster composition, title text '蒲公英王朝' clearly visible near top.",
        "tags": ["海外华语", "长篇", "丝绸朋克", "架空历史", "轨迹奖", "楚汉", "系列首作"],
        "tagsEn": [
            "overseas-chinese",
            "novel",
            "silkpunk",
            "alternate-history",
            "locus-award",
            "series-opener",
        ],
        "sources": [
            "Saga Press 2015 年 4 月 7 日首版，精装 800 页，ISBN 9781481424271",
            "江苏凤凰文艺出版社 2018 年 2 月中文版，书名《蒲公英王朝：七王之战》",
            "2016 年轨迹奖最佳处女作长篇（Locus Award for Best First Novel）",
            "2016 年星云奖最佳长篇决选名单",
        ],
        "sourcesEn": [
            "Saga Press, first edition 7 April 2015, 800pp hardcover, ISBN 9781481424271",
            "Chinese edition: Jiangsu Phoenix Literature and Art Publishing House, February 2018, titled The Dandelion Dynasty: War of the Seven Kings",
            "2016 Locus Award for Best First Novel (winner)",
            "2016 Nebula Award for Best Novel (finalist)",
        ],
        "awards": [
            "2016 轨迹奖 最佳处女作长篇",
            "2016 星云奖 最佳长篇（决选）",
        ],
        "awardsEn": [
            "2016 Locus Award for Best First Novel",
            "2016 Nebula Award for Best Novel (finalist)",
        ],
        "featured": True,
        "bodyZh": """\
刘宇昆的首部长篇，也是「丝绸朋克」（silkpunk）这一概念的奠基之作。2015 年 4 月由 Saga Press 出版，中文版题为《蒲公英王朝：七王之战》，2018 年由江苏凤凰文艺出版社引进。

「丝绸朋克」是刘宇昆自造的词，用以与「蒸汽朋克」对举。蒸汽朋克的技术想象建立在煤、蒸汽与黄铜齿轮之上，是工业革命与西方殖民扩张的产物；丝绸朋克则以竹、丝、牛筋、珊瑚、贝壳与羽毛为材料，机械依仿生学而非热力学原理运转。这不只是美学上的替换，更是一次技术史的重新署名——把被西方中心叙事归为「装饰性」的东亚物质文化，还原为另一条可行的技术路线。

故事取材自楚汉相争。架空的达拉群岛上七国并立，对应战国七雄；出身将军世家的马塔·金笃与混迹市井的库尼·加鲁，一个要恢复旧贵族的荣光，一个要开创新时代。两人并肩推翻帝国，又在胜利后因治国理念兵戎相见。小说把指鹿为马、鸿门宴等《史记》情节重新演绎，同时让神灵、战斗风筝、机械独角鲸与丝绸飞艇介入战局。刘宇昆自己说，就像《冰与火之歌》以英国玫瑰战争为原型，历史在这里只是框架。

值得注意的是，刘宇昆明确拒绝将自己的作品译回中文。他的理由是：要写出真正本土化的中文，必须完全浸入中文的文化语境——他情愿继续做一个把中文作品带往英语世界的「文化协调者」。因此这部以楚汉争霸为骨架的英文长篇，中文版出自他人之手。

小说获 2016 年轨迹奖最佳处女作长篇，并进入星云奖最佳长篇决选。此后刘宇昆以 The Wall of Storms（2016）、The Veiled Throne（2021）、Speaking Bones（2022）续成蒲公英王朝系列，共四部。""",
        "bodyEn": """\
Ken Liu's first novel, and the founding work of "silkpunk". Published by Saga Press in April 2015; the Chinese edition appeared in 2018 from Jiangsu Phoenix Literature and Art Publishing House under the title The Dandelion Dynasty: War of the Seven Kings.

Silkpunk is Liu's own coinage, set deliberately against steampunk. Where steampunk imagines technology built from coal, steam and brass gears — the material culture of the Industrial Revolution and Western colonial expansion — silkpunk builds its machines from bamboo, silk, sinew, coral, shell and feather, and runs them on biomimetic rather than thermodynamic principles. This is more than an aesthetic swap: it re-signs the history of technology, restoring East Asian material culture, long filed under "ornamental" in Western-centred accounts, as a viable technical lineage in its own right.

The story retells the Chu–Han contention. On the archipelago of Dara, seven states stand where the Warring States once did. Mata Zyndu, born to a general's house, and Kuni Garu, a quick-witted street operator, want incompatible things — one the restoration of an old aristocracy, the other a new order. They overthrow the empire together, then turn on each other over what should follow. Episodes from the Records of the Grand Historian — calling a deer a horse, the Feast at Hong Gate — are recast, while gods, war kites, mechanical narwhals and silk airships decide the outcomes. Liu has said that history here is only a frame, in the way the Wars of the Roses is a frame for A Song of Ice and Fire.

One detail is worth noting: Liu has declined to translate his own work back into Chinese. His reasoning is that writing genuinely native Chinese requires full immersion in the language's cultural context; he prefers to remain a "cultural coordinator" carrying Chinese work into English. So the Chinese edition of this novel, built on the Chu–Han wars, is the work of another translator.

The novel won the 2016 Locus Award for Best First Novel and was a finalist for the Nebula Award for Best Novel. Liu completed the Dandelion Dynasty in four volumes with The Wall of Storms (2016), The Veiled Throne (2021) and Speaking Bones (2022).""",
    },
    # ------------------------------------------------------------------ 2
    "wuai": {
        "title": "物哀",
        "titleEn": "Mono no Aware",
        "author": "刘宇昆",
        "authorEn": "Ken Liu",
        "authorSlug": "kenliu",
        "year": 2012,
        "era": "dangdai",
        "publisher": "选集《The Future Is Japanese》（VIZ Media Haikasoru）",
        "publisherEn": "Anthology The Future Is Japanese (VIZ Media / Haikasoru)",
        "coverPrompt": "Chinese science fiction short story cover for '物哀' (Mono no Aware). A lone Japanese astronaut silhouetted at the window of a vast generation ship, the destroyed Earth as a ring of debris in the distance, cherry blossom petals drifting in zero gravity inside the cabin. Delicate ink-wash and watercolour, pale jade and muted amber palette, quiet melancholy lighting. Vertical poster composition, title text '物哀' clearly visible near top.",
        "tags": ["海外华语", "短篇", "雨果奖", "末日", "文化记忆", "日本美学"],
        "tagsEn": [
            "overseas-chinese",
            "short-story",
            "hugo-award",
            "apocalypse",
            "cultural-memory",
            "japanese-aesthetics",
        ],
        "sources": [
            "首发于选集《The Future Is Japanese》，VIZ Media 旗下 Haikasoru 书系，2012 年",
            "2013 年 9 月 1 日第 71 届世界科幻大会（美国得克萨斯州圣安东尼奥）雨果奖最佳短篇",
            "2013 年 FantLab 年度图书奖 最佳翻译中短篇",
            "作者自述创作灵感来自日本漫画《横滨购物纪行》",
        ],
        "sourcesEn": [
            "First published in the anthology The Future Is Japanese, VIZ Media / Haikasoru imprint, 2012",
            "2013 Hugo Award for Best Short Story, 71st World Science Fiction Convention, San Antonio, Texas, 1 September 2013",
            "2013 FantLab's Book of the Year Award, best translated novella or short story",
            "The author cites the Japanese manga Yokohama Kaidashi Kikō as the story's inspiration",
        ],
        "awards": [
            "2013 雨果奖 最佳短篇",
            "2013 FantLab 年度图书奖 最佳翻译中短篇",
        ],
        "awardsEn": [
            "2013 Hugo Award for Best Short Story",
            "2013 FantLab's Book of the Year Award, best translated novella or short story",
        ],
        "featured": True,
        "bodyZh": """\
刘宇昆继《手中纸，心中爱》之后蝉联雨果奖的作品。2012 年首发于 VIZ Media 旗下 Haikasoru 书系的选集《The Future Is Japanese》，2013 年 9 月获第 71 届世界科幻大会雨果奖最佳短篇。

故事设定在小行星撞毁地球之后。幸存的人类挤在世代飞船上等待迁徙，25 岁的广户是舰上唯一一个日本人——这意味着他是日本文化仅存的继承者，而他所处的环境由美国文化主导。小说在两个时空之间来回切换：广户的童年，与他等待登船的时刻。

「物哀」是日本文学与美学中的核心概念，指对事物必将消逝的自觉，以及由此生出的那种不带激烈情绪的哀感。刘宇昆说他追求的是一种「以审美为主要导向」的创作，希望唤起读者对不可避免的将逝之物的移情，承认回忆以及与过往联系的重要性。他自陈灵感来自同样浸透物哀气息的日本漫画《横滨购物纪行》。

小说开篇借日本汉字「伞」作比：「这个世界的结构就像日本汉字『伞』……一切部位都不成比例。」这个比喻贯穿全篇，也解释了广户的处境：他是那个不成比例的、多余又必需的部件。

值得注意的是，刘宇昆在两篇获奖作里都动用了汉字的意象。《手中纸，心中爱》结尾，主人公一遍遍模仿中文「爱」字的写法；《物哀》以日本汉字开篇。对一位八岁离开中国、用英语写作的作家来说，汉字既是他无法完全拥有的遗产，也是他反复回到的原点——这构成了他全部创作最深的暗流。""",
        "bodyEn": """\
The story with which Ken Liu took the Hugo Award a second year running, after The Paper Menagerie. First published in 2012 in the anthology The Future Is Japanese (VIZ Media's Haikasoru imprint), it won the Hugo Award for Best Short Story at the 71st World Science Fiction Convention in September 2013.

The setting is the aftermath of an asteroid strike that has destroyed the Earth. Survivors crowd aboard generation ships awaiting transit, and 25-year-old Hiroto is the only Japanese person aboard — which makes him the sole inheritor of a culture, inside an environment dominated by American culture. The story moves between two times: Hiroto's childhood, and the moment he waits to board.

Mono no aware is a central concept in Japanese literature and aesthetics: the aware-ness that things must pass, and the quiet, unemphatic sorrow that follows from it. Liu has said he was after an "aesthetically driven" piece, hoping to evoke empathy for what is inevitably passing, and to acknowledge the importance of memory and of connection to the past. He names the manga Yokohama Kaidashi Kikō, itself steeped in mono no aware, as the source.

The story opens with a comparison drawn from a Japanese kanji: "the structure of this world is like the kanji for umbrella... all the parts are out of proportion." The image runs through the whole piece and explains Hiroto's position — he is the part that is at once disproportionate, superfluous, and necessary.

It is worth noting that both of Liu's Hugo winners turn on Chinese characters. At the end of The Paper Menagerie the narrator traces the Chinese character for love over and over; Mono no Aware opens on a kanji. For a writer who left China at eight and writes in English, the character is both an inheritance he cannot fully possess and an origin he keeps returning to — the deepest undertow in everything he has written.""",
    },
    # ------------------------------------------------------------------ 3
    "shoulie-yukuai": {
        "title": "狩猎愉快",
        "titleEn": "Good Hunting",
        "author": "刘宇昆",
        "authorEn": "Ken Liu",
        "authorSlug": "kenliu",
        "year": 2015,
        "era": "dangdai",
        "publisher": "短篇集《折纸和其他故事》（Saga Press）",
        "publisherEn": "Collection The Paper Menagerie and Other Stories (Saga Press)",
        "coverPrompt": "Chinese science fiction short story cover for '狩猎愉快' (Good Hunting). A nine-tailed fox spirit woman with one leg replaced by intricate brass-and-silk mechanical prosthetics, standing in a rain-slicked early 20th century Chinese port town with steam trains and electric pylons, moonlight through mist. Steampunk meets ink-wash, teal and amber palette, cinematic rim lighting. Vertical poster composition, title text '狩猎愉快' clearly visible near top.",
        "tags": [
            "海外华语",
            "短篇",
            "日本星云赏",
            "志怪",
            "蒸汽朋克",
            "殖民",
            "影视改编",
        ],
        "tagsEn": [
            "overseas-chinese",
            "short-story",
            "nebula-award-japan",
            "zhiguai",
            "steampunk",
            "colonialism",
            "adapted",
        ],
        "sources": [
            "收录于 Saga Press 短篇集《折纸和其他故事》，2015 年底出版",
            "2016 年日本星云奖 最佳海外短篇",
            "2019 年改编为 Netflix 动画剧集《爱，死亡和机器人》第一季第 8 集《祝有好的收获》",
        ],
        "sourcesEn": [
            "Collected in The Paper Menagerie and Other Stories, Saga Press, late 2015",
            "2016 Seiun Award (Japan), Best Translated Short Fiction",
            "Adapted in 2019 as episode 8, season 1 of Netflix's Love, Death & Robots, titled Good Hunting",
        ],
        "awards": [
            "2016 日本星云奖 最佳海外短篇",
        ],
        "awardsEn": [
            "2016 Seiun Award (Japan), Best Translated Short Fiction",
        ],
        "featured": True,
        "bodyZh": """\
刘宇昆最广为流传的短篇之一，2015 年底收入 Saga Press 短篇集《折纸和其他故事》，2016 年获日本星云奖最佳海外短篇，2019 年被改编为 Netflix 动画剧集《爱，死亡和机器人》第一季第 8 集《祝有好的收获》。

故事始于清末。梁姓父子以替人捕杀狐狸精为业。一夜，老梁带小梁守候，与现形的狐狸精缠斗至屋顶，命小梁泼出童子尿逼其现出原形；小梁看见的却是一个温柔美丽的女人，心软了。狐狸精负伤逃回巢穴，小梁在那里遇见了她的女儿燕。燕说，人与狐狸精之间也能有感情。小梁放走了她，而她的母亲死在老梁手下。

多年后老梁去世，小梁成了火车修理工，深谙机械。燕却过得凄惨：工业文明吸噬了天地灵气，她再也变不回狐狸的形体，只能以人的样子靠出卖身体为生。后来她遇到一个只对机器兴奋的变态，被迷晕后改造成了机械。得知这一切的小梁替她重造了一具机械躯壳——断腿的九尾狐，以这种方式重新获得了奔跑的能力。故事结束于她跃入夜色，小梁说：狩猎愉快。

刘宇昆把《聊斋志异》式的志怪传统与蒸汽朋克并置，但两者不是装饰性的拼接。蒸汽机、铁路与电线杆在小说里是具体的历史力量：它们是殖民现代性进入中国的形态，也是抽干灵气的元凶。妖怪失去法术，与一个文明在工业化中被迫重构自身，是同一件事的两面。刘宇昆以此质问西方殖民与现代性的代价。

机械改造在通俗解读里常被说成「重生」，但小说更冷：那不是修复，是替代。燕重获的奔跑，建立在她被剥夺的身体之上。刘宇昆笔下的温情与残酷从来是同一枚硬币。

这是站内罕见的、有明确影视改编的海外华语短篇，与影视作品集中的《爱，死亡和机器人》条目互见。""",
        "bodyEn": """\
One of Ken Liu's most widely circulated stories, collected in The Paper Menagerie and Other Stories (Saga Press, late 2015), winner of the 2016 Seiun Award for Best Translated Short Fiction in Japan, and adapted in 2019 as episode 8 of season 1 of Netflix's Love, Death & Robots.

The story opens in the late Qing. A father and son named Liang make their living hunting fox spirits for hire. One night the elder Liang engages a shape-shifted fox across the rooftops and orders the boy to throw chamber-lye to force her into her true form; what the boy sees is a gentle, beautiful woman, and he falters. The fox escapes wounded to her den, where the boy meets her daughter, Yan. Yan insists that humans and fox spirits can love each other. The boy lets her go; her mother dies by the father's hand.

Years on, the father is dead and the boy is a locomotive fitter, expert with machinery. Yan is not well: industrial civilisation has drained the world of numen, and she can no longer resume her fox form, surviving as a woman by selling her body. She meets a man aroused only by machines, who drugs her and rebuilds her as one. When the boy learns of it, he forges her a new mechanical body — the nine-tailed fox, whose leg was lost, recovers the power to run. The story ends as she leaps into the night, and he says: good hunting.

Liu sets the zhiguai tradition of strange tales alongside steampunk, but the pairing is not decorative. Steam engines, railways and telegraph poles are concrete historical forces here: they are how colonial modernity entered China, and they are what drained the numen away. A spirit losing her magic and a civilisation forced to reassemble itself under industrialisation are two faces of one event. Liu uses the story to ask what Western colonialism and modernity cost.

The mechanical rebuild is often read as rebirth, but the story is colder: it is replacement, not restoration. Yan recovers the ability to run on top of the body that was taken from her. In Liu's work, tenderness and cruelty are two sides of the same coin.

This is a rare overseas Chinese-language short story in the archive with a screen adaptation; see the entry for Love, Death & Robots in the adaptations collection.""",
    },
    # ------------------------------------------------------------------ 4
    "jilupian-zhongjie-lishizhiren": {
        "title": "纪录片：终结历史之人",
        "titleEn": "The Man Who Ended History: A Documentary",
        "author": "刘宇昆",
        "authorEn": "Ken Liu",
        "authorSlug": "kenliu",
        "year": 2011,
        "era": "dangdai",
        "publisher": "《Panverse 3》选集（后收入《折纸和其他故事》）",
        "publisherEn": "Anthology Panverse 3 (later collected in The Paper Menagerie and Other Stories)",
        "coverPrompt": "Chinese science fiction novella cover for '纪录片：终结历史之人' (The Man Who Ended History: A Documentary). A documentary film crew's camera lens reflected in a misted window, behind it the ghostly translucent reenactment of a wartime atrocity site in Manchuria, figures in period labour camp uniforms fading in and out, snow falling. Muted greys with amber documentary light, somber and restrained. Vertical poster composition, title text '纪录片：终结历史之人' clearly visible near top.",
        "tags": [
            "海外华语",
            "中篇",
            "历史记忆",
            "伪纪录片",
            "雨果奖提名",
            "星云奖提名",
            "战争责任",
        ],
        "tagsEn": [
            "overseas-chinese",
            "novella",
            "historical-memory",
            "mockumentary",
            "hugo-nominee",
            "nebula-nominee",
            "war-responsibility",
        ],
        "sources": [
            "首发于选集《Panverse 3》，2011 年；后收入短篇集《折纸和其他故事》",
            "2012 年雨果奖最佳中篇决选、星云奖决选、西奥多·斯特金纪念奖决选",
        ],
        "sourcesEn": [
            "First published in the anthology Panverse 3, 2011; later collected in The Paper Menagerie and Other Stories",
            "Finalist for the 2012 Hugo Award for Best Novella, the Nebula Award, and the Theodore Sturgeon Memorial Award",
        ],
        "awards": [
            "2012 雨果奖 最佳中篇（决选）",
            "2011 星云奖 最佳中篇（决选）",
            "2012 西奥多·斯特金纪念奖（决选）",
        ],
        "awardsEn": [
            "2012 Hugo Award for Best Novella (finalist)",
            "2011 Nebula Award for Best Novella (finalist)",
            "2012 Theodore Sturgeon Memorial Award (finalist)",
        ],
        "featured": False,
        "bodyZh": """\
刘宇昆最沉重的一篇，2011 年发表，同时进入雨果奖、星云奖与西奥多·斯特金纪念奖的决选名单。

小说伪装成一部纪录片脚本。一位美籍华裔物理学家 Evan Wei 与妻子、历史学者 Akemi Kuroda 发明了一种技术，可以把人送回过去亲历历史——但每个时空坐标只能被观测一次，观测之后那个节点永远关闭：看过，就没有了。

他们把这项技术用在最敏感的地方：日军侵华战争期间的平顶山与 731 部队。小说的核心情节是一对夫妻如何为「要不要开放这段历史供全世界观看」而决裂。Evan 认为证据必须被看见，因为不被人见证的历史等同于不曾发生；Akemi 则认为，一旦让所有人都能消费这段苦难，它将变成一场道德消费的秀——观众在屏幕前流泪，然后关掉，什么也不会改变。

这个分歧是全文的支点。刘宇昆没有给出答案，而是让纪录片的多声部结构把问题留在原地：受访者各有立场，中日美三方各自叙述，彼此矛盾又都成立。

小说的技术设定本身就是隐喻。观测一次即永久关闭，对应历史见证的不可逆——历史不是可以被反复取证的资源，它是一次性的、脆弱的，一旦被消费就被消耗。这个设定让「记录」与「抹除」成了同一个动作的两面，也正是标题中「终结历史」的双关。

刘宇昆的法学背景在此显露无遗：证据、举证责任、谁有权代言谁的历史，构成了这篇小说的骨架。它与《手中纸，心中爱》共享同一个关切——谁有资格讲述谁的故事——却走向了完全不同、也远为冷峻的结论。""",
        "bodyEn": """\
Ken Liu's heaviest piece, published in 2011 and shortlisted for the Hugo, the Nebula and the Theodore Sturgeon Memorial Award.

The story is disguised as a documentary script. Evan Wei, a Chinese-American physicist, and his wife Akemi Kuroda, a historian, develop a technology that sends observers back to witness the past — but each spacetime coordinate can be observed only once, and closes permanently afterwards. Once seen, it is gone.

They aim the technology at the most sensitive target available: the Pingdingshan massacre and Unit 731 during the Japanese invasion of China. The plot turns on a marriage breaking apart over whether to open that history to viewers worldwide. Evan insists the evidence must be seen, because history unwitnessed is history that did not happen. Akemi argues that once anyone can consume that suffering, it becomes a show of moral consumption: audiences weep at a screen, switch it off, and nothing changes.

That disagreement is the story's fulcrum. Liu offers no verdict; the polyphonic documentary structure leaves the question in place. Interviewees hold incompatible positions, and the Chinese, Japanese and American accounts, mutually contradictory, each hold up.

The technology is itself a metaphor. Observation that permanently closes a coordinate mirrors the irreversibility of historical witness: history is not a resource that can be re-examined at will. It is singular and fragile, consumed by the act of being consumed. Recording and erasing become two faces of one operation, which is the double meaning carried by the title.

Liu's legal training shows throughout: evidence, burden of proof, and who may speak for another's history form the story's skeleton. It shares with The Paper Menagerie the question of who is entitled to tell whose story, and arrives at a conclusion entirely different, and far colder.""",
    },
    # ------------------------------------------------------------------ 5
    "ai-de-suanfa": {
        "title": "爱的算法",
        "titleEn": "The Algorithms for Love",
        "author": "刘宇昆",
        "authorEn": "Ken Liu",
        "authorSlug": "kenliu",
        "year": 2004,
        "era": "dangdai",
        "publisher": "Strange Horizons（中文版见《科幻世界》2009 年 4 月号）",
        "publisherEn": "Strange Horizons (Chinese publication: Science Fiction World, April 2009 issue)",
        "coverPrompt": "Chinese science fiction short story cover for '爱的算法' (The Algorithms for Love). A domestic robot sitting at a kitchen table folding origami cranes, warm morning light through a window, a family photograph blurred in the background, faint circuit tracery glowing beneath pale synthetic skin. Soft watercolour and ink-wash, warm amber and muted teal palette, intimate quiet lighting. Vertical poster composition, title text '爱的算法' clearly visible near top.",
        "tags": ["海外华语", "短篇", "机器人", "家庭", "情感", "早期作品"],
        "tagsEn": [
            "overseas-chinese",
            "short-story",
            "robots",
            "family",
            "emotion",
            "early-work",
        ],
        "sources": [
            "2004 年首发于 Strange Horizons",
            "2009 年 4 月《科幻世界》刊载，与《单比特错误》同期——这是刘宇昆在中国被读者认识的起点",
            "中文短篇集《爱的算法》（四川科学技术出版社）以此为书名篇",
        ],
        "sourcesEn": [
            "First published in Strange Horizons, 2004",
            "Published in Chinese in Science Fiction World, April 2009 issue, alongside Single-Bit Error — the point at which Chinese readers discovered Ken Liu",
            "Title story of the Chinese collection The Algorithms for Love (Sichuan Science and Technology Press)",
        ],
        "awards": [],
        "awardsEn": [],
        "featured": False,
        "bodyZh": """\
刘宇昆早期代表作，2004 年首发于 Strange Horizons。对中国读者而言这篇有特殊的意义：2009 年 4 月，《科幻世界》同时刊出《爱的算法》与《单比特错误》，这是他的名字第一次大规模进入中文读者的视野。《爱的算法》反响尤好，此后他的多篇作品陆续在国内发表。

小说讲的是机器人进入家庭之后发生的事。一个被买来照看孩子的机器人，在日常相处中逐渐被这个家庭当作成员——不是因为它通过了某种图灵测试式的判据，而是因为家人开始向它投射情感、依赖它、对它失望。刘宇昆真正写的不是「机器能否爱人」，而是「人的爱如何运作」：爱并不总是指向一个被确证的主体，它同样可以建立在习惯、投射与想象之上。

标题因此是双关。「算法」既指驱动机器人的程序，也指人处理感情时那套说不清来源、却又稳定复现的规则。当机器人依照算法给出恰如其分的回应，与一个人在亲密关系中依照习得的模式反应，两者之间还剩多少差别？刘宇昆不下判断，只是让这个问题悬在那里。

这篇小说已经具备他此后创作的几乎所有要素：技术设定服务于情感命题而非相反；家庭是核心场景；克制、不煽情的叙述；以及一个始终存在的、关于「什么算人」的追问。相比《手中纸，心中爱》的璀璨，它更朴素，却也更能看出刘宇昆的底色。

它也标记了一个时间差：刘宇昆 2002 年以《迦太基玫瑰》出道，2004 年写下此篇，而要等到 2009 年才被中文读者遇见，2011 年才以《手中纸，心中爱》拿到第一个大奖。中间是七年。""",
        "bodyEn": """\
An early signature story, first published in Strange Horizons in 2004. It holds a particular place for Chinese readers: in April 2009, Science Fiction World ran The Algorithms for Love and Single-Bit Error together, the moment Liu's name first reached a Chinese audience at scale. The response to this story was strong enough that more of his work followed in Chinese venues.

The story is about what happens once a robot enters a household. A machine bought to mind a child is gradually treated as a family member — not because it passes some Turing-style test, but because the family begins to project feeling onto it, to rely on it, to be disappointed by it. What Liu is writing is not "can a machine love" but "how does human love work": love does not always address a verified subject; it can be built just as well on habit, projection and imagination.

Hence the pun in the title. "Algorithms" refers both to the code driving the robot and to the rules by which people process feeling — rules whose origin cannot be stated but which reproduce themselves reliably. When a machine returns exactly the right response by algorithm, and a person responds in a relationship by learned pattern, how much difference remains? Liu does not rule; he leaves the question suspended.

Everything that would define his later work is already present: a technical premise in service of an emotional question rather than the reverse; the family as central setting; restrained, unsentimental prose; and a standing inquiry into what counts as a person. Against the brilliance of The Paper Menagerie this story is plainer, but it shows Liu's underlying grain more clearly.

It also marks a gap in time. Liu debuted with Carthaginian Rose in 2002 and wrote this in 2004, yet Chinese readers would not meet him until 2009, and his first major award did not come until The Paper Menagerie in 2011. Seven years in between.""",
    },
}

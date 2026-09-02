# -*- coding: utf-8 -*-
"""D 任务：港台 / 海外华语 / 网络文学 内容扩面数据。

每条均经资料核实，字段与既有集合规范一致：
  - authors: name / nameEn / alias / birthYear / deathYear / era / photoCredit / translationStatus / awards + 正文
  - works:   title / author / authorSlug / year / era / kind / publisher / publisherEn /
             coverCredit / coverPrompt / tags / sources / awards / featured / translationStatus + 正文

era 归属：1949–1990 → xinzhongguo；1991 起 → dangdai（与 src/content/eras.yaml 一致）
香港、台湾条目统一表述为「中国香港」「中国台湾」，符合一个中国原则。
"""

AUTHORS = {
    "niquang": {
        "name": "倪匡",
        "nameEn": "Ni Kuang",
        "alias": ["倪聪", "卫斯理", "沙翁", "岳川", "魏力", "衣其"],
        "birthYear": 1935,
        "deathYear": 2022,
        "era": "xinzhongguo",
        "awards": [
            "2012 第 31 届香港电影金像奖 终身成就奖",
            "2018 香港电影编剧家协会 银禧荣誉大奖",
            "2000 《蓝血人》入选「二十世纪中文小说百强」",
        ],
        "awardsEn": [
            "2012 Hong Kong Film Award for Lifetime Achievement (31st)",
            "2018 Silver Jubilee Honorary Award, Hong Kong Screenwriters' Guild",
            "2000 The Blue-Blooded Man selected among the 100 Best Chinese Novels of the 20th Century",
        ],
        "bodyZh": """\
中国香港科幻小说的奠基者，与金庸、黄霑、蔡澜并称「香港四大才子」。原名倪聪，字亦明，祖籍浙江宁波，1935 年生于上海。1957 年赴港，做过工人、校对、编辑，自学成才转为职业作家。

1962 年起以「卫斯理」为笔名在《明报》副刊连载小说，首作《钻石花》。至第四部《蓝血人》（1964）转入科幻，自此奠定卫斯理系列的走向。三十余年间写下百余部卫斯理系列作品，另有原振侠、女黑侠木兰花、六指琴魔等系列。

同时创作电影剧本数百部，代表作有张彻导演的《独臂刀》；1972 年参与《精武门》编剧，为李小龙塑造「陈真」这一经典银幕形象。

倪匡的科幻不以科学严谨取胜，而以奇想、悬念与通俗魅力见长，把外星文明、时空穿梭、人体异变等题材带入华语大众阅读，被读者称作「华人科幻小说祖师爷」。他的写作速度惊人，自定每日八千字，曾同时为十二家报纸写连载。1992 年移居美国，2006 年返港，2022 年逝世。""",
        "bodyEn": """\
The founding figure of science fiction in Hong Kong, China, and one of the "Four Great Talents of Hong Kong" alongside Jin Yong, James Wong and Chua Lam. Born Ni Cong, courtesy name Yiming, he was a native of Ningbo, Zhejiang, born in Shanghai in 1935. He reached Hong Kong in 1957 and worked as a labourer, proofreader and editor before becoming a full-time writer, largely self-taught.

From 1962 he wrote under the pen name Wei Si Li (Wisely) in the Ming Pao supplement, beginning with Diamond Flower. The fourth book, The Blue-Blooded Man (1964), turned the series toward science fiction and set its course for the next three decades. He went on to write more than a hundred Wisely titles, along with the Yuan Zhenxia, Mulan and Six-Fingered Lute series.

He also wrote several hundred film scripts, among them The One-Armed Swordsman for director Chang Cheh, and in 1972 co-wrote Fist of Fury, shaping the classic screen role of Chen Zhen for Bruce Lee.

Ni Kuang's science fiction wins not through scientific rigour but through invention, suspense and sheer readability. He brought alien civilisations, time travel and bodily mutation into popular Chinese-language reading, and is called by readers the "grandfather of Chinese science fiction". He set himself eight thousand characters a day and once ran serials for twelve newspapers at once. He moved to the United States in 1992, returned to Hong Kong in 2006, and died in 2022.""",
    },
    "zhangxiguo": {
        "name": "张系国",
        "nameEn": "Chang Hsi-Kuo",
        "alias": ["醒石", "域外人"],
        "birthYear": 1944,
        "deathYear": None,
        "era": "xinzhongguo",
        "awards": [
            "台湾科幻文学的开拓者与领军者，被称为「台湾科幻之父」",
            "1986 年中国时报科幻小说奖更名「张系国科幻小说奖」",
            "1989 年创办科幻杂志《幻象》",
            "1979 《黄河之水》获第一届仓颉奖",
        ],
        "awardsEn": [
            "Pioneer and leading figure of Taiwanese science fiction, known as the father of Taiwan SF",
            "1986 China Times SF Award renamed the Chang Hsi-Kuo Science Fiction Award",
            "1989 founded the science fiction magazine Mirage",
            "1979 Cangjie Prize for The Water of the Yellow River",
        ],
        "bodyZh": """\
中国台湾科幻文学的开拓者与领军者，被称为「台湾科幻之父」。江西南昌人，1944 年生于重庆，1949 年举家迁台。台湾大学电机系毕业，后获美国柏克莱加州大学计算机科学博士，长期任教于康奈尔大学、伊利诺大学与匹兹堡大学。

1968 年发表科幻处女作《超人列传》，与张晓风同年发表的《潘渡娜》一同被视为战后台湾科幻文学的起点。1976 年起在《联合报》副刊连载科幻短篇，1980 年结集为《星云组曲》。此后以十年工夫经营长篇「城」三部曲——《五玉碟》（1983）、《龙城飞将》（1986）、《一羽毛》（1991），构筑出外星「呼回世界」中索伦城的兴衰史。

张系国主张「中国风味的科幻」，以章回体与组曲形式承载历史哲学思辨，被学界称为「张派科幻」。除创作外，他于 1982 年创办知识系统出版有限公司，1984 年起与《中国时报》合办年度科幻小说奖（1986 年更名「张系国科幻小说奖」），1989 年创办科幻杂志《幻象》，并主编多部年度科幻小说选，为台湾科幻写作场域的建立付出极大心力。

需要辨明的是，他最广为流传的小说《棋王》（1974）并非科幻作品，而是以写实笔法写社会与人性。他的科幻代表作是《星云组曲》与「城」三部曲。""",
        "bodyEn": """\
The pioneer and leading figure of science fiction in Taiwan, China, often called the father of Taiwanese SF. A native of Nanchang, Jiangxi, he was born in Chongqing in 1944 and moved to Taiwan with his family in 1949. He graduated in electrical engineering from National Taiwan University and took a doctorate in computer science at the University of California, Berkeley, teaching at Cornell, Illinois and Pittsburgh.

His first science fiction story, Biographies of Supermen (1968), together with Chang Hsiao-feng's Pandora published the same year, is regarded as the starting point of postwar Taiwanese science fiction. From 1976 he ran SF short stories in the United Daily News supplement, collected in 1980 as Star Nebula Suite. He then spent ten years on the City trilogy — Five Jade Disks (1983), The Flying General of Dragon City (1986) and A Single Feather (1991) — chronicling the rise and fall of Solen City in the alien Huhui world.

Chang argued for science fiction with a Chinese flavour, using chapter-linked and suite forms to carry historical and philosophical argument; critics call this the "Chang school". In 1982 he founded Knowledge Systems Publishing, from 1984 co-ran the annual China Times SF Award (renamed the Chang Hsi-Kuo Science Fiction Award in 1986), founded the magazine Mirage in 1989, and edited several annual SF anthologies, doing as much as any writer to build an institutional field for Taiwanese science fiction.

One clarification: his best-known novel, Chess King (1974), is not science fiction but social realism. His science fiction masterworks remain Star Nebula Suite and the City trilogy.""",
    },
    "huanghai": {
        "name": "黄海",
        "nameEn": "Huang Hai",
        "alias": ["黄炳煌", "凌霄子"],
        "birthYear": 1943,
        "deathYear": None,
        "era": "xinzhongguo",
        "awards": [
            "1988 国家文艺奖（旧制第十四届）《大鼻国历险记》",
            "1986 中山文艺奖《嫦娥城》",
            "1984 洪建全儿童文学奖《奇异的航行》",
            "1982 中国文艺奖章 小说创作奖",
            "台湾唯一以科幻作品获国家文艺奖、中山文艺奖的作家",
        ],
        "awardsEn": [
            "1988 National Award for Arts and Letters (14th, former system), Adventures in the Land of Big Noses",
            "1986 Sun Yat-sen Literature Award, City of Chang'e",
            "1984 Hong Chien-chuan Children's Literature Award, The Strange Voyage",
            "1982 Chinese Literary Medal for Fiction",
            "The only writer to win both the National Award for Arts and Letters and the Sun Yat-sen Literature Award for science fiction",
        ],
        "bodyZh": """\
中国台湾少儿科幻的开创者，本名黄炳煌，笔名凌霄子，1943 年生于台中，台湾师范大学历史系毕业。曾任《科学儿童周刊》主编、联合报编辑，退休后于静宜大学、世新大学讲授台湾文学与科幻文学。

1969 年出版第一部科幻小说集《一〇一〇一年》，此后四十余年笔耕不辍，作品横跨成人科幻与少年科幻：《银河迷航记》（1979）、《偷脑计划》（1984）、《第四类接触》（1985）、《鼠城记》（1987）以奇想与讽喻面向成人读者；《奇异的航行》《嫦娥城》《大鼻国历险记》则为少年读者写作，多次获新闻局优良读物推荐。

他主张科幻应搭建主流文学与类型文学之间的桥梁，著有论著《台湾科幻文学薪火录（1956–2005）》《科幻文学解构》，是台湾科幻史料建构与理论阐述的重要推手。他是台湾唯一以科幻作品同时获得国家文艺奖与中山文艺奖的作家。

一件常被引述的逸事：1988 年他发表《地球逃亡》，设想太阳行将毁灭、人类为地球装上发动机逃离太阳系——比刘慈欣《流浪地球》（2000）早十余年。黄海后来撰文比较两作，谦称自己的《地球逃亡》在工程细节上「只能甘拜下风」，并指出自己的小说「从地球才要出发就结束」。这段前后呼应，是华语科幻内部对话的一个珍贵样本。""",
        "bodyEn": """\
The founder of children's and young-adult science fiction in Taiwan, China. Born Huang Ping-huang, also writing as Ling Xiaozi, he was born in Taichung in 1943 and graduated in history from National Taiwan Normal University. He edited Science Children's Weekly and worked as an editor at United Daily News; after retiring he taught Taiwanese literature and science fiction at Providence and Shih Hsin Universities.

His first collection, Year 10101, appeared in 1969, and he wrote steadily for more than forty years across both adult and juvenile science fiction. Galactic Voyage Adrift (1979), The Brain-Stealing Project (1984), The Fourth Kind of Contact (1985) and Rat City (1987) address adult readers with invention and satire, while The Strange Voyage, City of Chang'e and Adventures in the Land of Big Noses were written for young readers and repeatedly recommended by the Government Information Office as outstanding children's reading.

He argued that science fiction should bridge mainstream and genre literature. His studies, Record of Taiwanese Science Fiction, 1956–2005 and Deconstructing Science Fiction, are central to the archival and theoretical work on Taiwanese SF. He is the only writer to have won both the National Award for Arts and Letters and the Sun Yat-sen Literature Award for science fiction.

A much-repeated episode: in 1988 he published Earth Escape, imagining the sun dying and humanity fitting engines to the planet to flee the solar system — more than a decade before Liu Cixin's The Wandering Earth (2000). Huang later compared the two, conceding that his own novel "must yield" on engineering detail and noting that his story "ends just as Earth is about to set out". The exchange is a rare instance of direct dialogue within Chinese-language science fiction.""",
    },
    "kenliu": {
        "name": "刘宇昆",
        "nameEn": "Ken Liu",
        "alias": ["Ken Liu", "Liu Yukun"],
        "birthYear": 1976,
        "deathYear": None,
        "era": "dangdai",
        "awards": [
            "2012 雨果奖 最佳短篇（《手中纸，心中爱》）",
            "2011 星云奖 最佳短篇（《手中纸，心中爱》）",
            "2012 世界奇幻奖 最佳短篇（《手中纸，心中爱》）",
            "2013 雨果奖 最佳短篇（《物哀》）",
            "2016 日本星云奖 海外短篇（《狩猎愉快》）",
            "2014 第五届全球华语科幻星云奖 特别贡献奖（翻译）",
        ],
        "awardsEn": [
            "2012 Hugo Award for Best Short Story (The Paper Menagerie)",
            "2011 Nebula Award for Best Short Story (The Paper Menagerie)",
            "2012 World Fantasy Award for Best Short Fiction (The Paper Menagerie)",
            "2013 Hugo Award for Best Short Story (Mono no Aware)",
            "2016 Seiun Award, Best Translated Short Fiction (Good Hunting)",
            "2014 Chinese Nebula Award, Special Contribution Award (translation)",
        ],
        "bodyZh": """\
美籍华裔科幻作家、翻译家，1976 年生于甘肃兰州，11 岁随父母移民美国。哈佛学院英国文学与计算机科学专业毕业，后获哈佛法学院法律博士，曾任软件工程师与高科技诉讼顾问，2017 年起全职写作。

2002 年发表处女作《迦太基玫瑰》，2010 年后进入创作高峰。短篇《手中纸，心中爱》发表于 2011 年，是史上唯一一部同时赢得雨果奖、星云奖与世界奇幻奖三项大奖的虚构作品——它以会动的折纸为媒介，写一个华裔男孩与母亲之间因语言而撕裂、又因记忆而弥合的情感。另一短篇《物哀》再获 2013 年雨果奖。

他的首部长篇《国王的恩典》（2015）开创「丝绸朋克」（silkpunk）一词：以竹、丝、牛筋、珊瑚等东亚与太平洋materials取代蒸汽朋克的黄铜齿轮，机器依仿生学原理运转。其作品常处理殖民、语言、移民与文化翻译的主题，以温和而坚定的方式回应西方科幻对东方角色的投射。

对中国读者而言，他更广为人知的身份是译者。他翻译了刘慈欣《三体》英文版（2014）与郝景芳《北京折叠》（2016），两作分别获雨果奖最佳长篇与最佳中短篇，被刘慈欣称为「跨越两个文化与时空的桥梁」。他还译介了陈楸帆、韩松、夏笳、宝树、张冉、马伯庸等作者的中短篇四十余篇，是中国科幻走向英语世界的关键推手。""",
        "bodyEn": """\
Chinese-American science fiction writer and translator, born in 1976 in Lanzhou, Gansu, who emigrated to the United States at eleven. He studied English literature and computer science at Harvard College and took a JD at Harvard Law School, working as a software engineer and later a high-tech litigation consultant before writing full time from 2017.

His first story, Carthaginian Rose, appeared in 2002; a prolific period began around 2010. The Paper Menagerie (2011) is the only work of fiction ever to win the Hugo, Nebula and World Fantasy Awards — it uses living origami to tell of a Chinese-American boy and his mother, sundered by language and restored by memory. Another short story, Mono no Aware, won a second Hugo in 2013.

His first novel, The Grace of Kings (2015), introduced the term silkpunk: bamboo, silk, ox sinew and coral replace steampunk's brass gears, and machines run on biomechanical principles. His work repeatedly takes up colonialism, language, migration and cultural translation, answering — politely but firmly — the Western genre's habit of projecting its own fears onto Chinese characters.

For Chinese readers he is better known as a translator. His English versions of Liu Cixin's The Three-Body Problem (2014) and Hao Jingfang's Folding Beijing (2016) won the Hugo Awards for Best Novel and Best Novelette; Liu Cixin called him "the bridge across two cultures and two stretches of time". He has translated more than forty stories by Chen Qiufan, Han Song, Xia Jia, Baoshu, Zhang Ran and Ma Boyong, and remains the single most important conduit for Chinese science fiction into English.""",
    },
    "xuanyu": {
        "name": "玄雨",
        "nameEn": "Xuan Yu",
        "alias": ["蒋虎"],
        "birthYear": None,
        "deathYear": None,
        "era": "dangdai",
        "awards": [
            "《小兵传奇》与《诛仙》《飘邈之旅》并称「网络三大奇书」",
            "中国网络文学「星际军事」流派的开山之作",
        ],
        "awardsEn": [
            "Legend of a Little Soldier named one of the Three Marvels of early Chinese web fiction, alongside Zhu Xian and A Record of a Journey to the Stars",
            "Founding work of the interstellar-military strand of Chinese web fiction",
        ],
        "bodyZh": """\
中国网络文学早期代表作家，本名蒋虎。以长篇科幻小说《小兵传奇》知名，该书自 2003 年 4 月起在起点中文网连载，至 2007 年完结，全书约二百一十万字。

《小兵传奇》讲述高中毕业生唐龙阴差阳错参军，从最不受待见的步兵做起，在五台智能机器人的严酷训练下成长，又以一千艘「炮灰级」自走炮舰歼灭敌方两千艘正规战舰，却在功劳被侵吞后走上反抗与割据之路，最终统一宇宙。

作品的意义首先在于类型开创：它把机甲、星际舰队、超光速航行、人工智能与军事谋略、星际政治熔于一炉，奠定了中国网络文学「星际军事文」的世界观范式，影响了《师士传说》《机动风暴》等后续创作。它与《诛仙》《飘邈之旅》并称「网络三大奇书」，被多种网络文学研究专著列为早期经典。

其次在于它的媒介形态。这部作品是连载文化的产物：中途长期断更，期间网络上流传各种续写版本，作者恢复更新后吸收了其中部分设定，导致后期文风驳杂。这种作者与读者共同塑造文本的过程，正是早期网络文学区别于纸面出版的核心经验。""",
        "bodyEn": """\
A representative author of early Chinese web fiction, whose real name is Jiang Hu. He is known for Legend of a Little Soldier, serialised on Qidian from April 2003 and completed in 2007 at roughly 2.1 million characters.

The novel follows Tang Long, a high-school graduate who joins the army by accident, starts out in the least regarded branch, the infantry, and is trained brutally by five intelligent robots. He destroys two thousand enemy warships with a thousand expendable self-propelled gunships, only to have the credit stolen — after which he turns to rebellion, builds a power base, and eventually unifies the universe.

Its first importance is generic: it fuses mecha, interstellar fleets, faster-than-light travel and artificial intelligence with military strategy and interstellar politics, establishing the world-building template for the interstellar-military strand of Chinese web fiction and shaping later works such as Master of Mecha and Storm of Maneuver. It is named one of the Three Marvels of early web fiction alongside Zhu Xian and A Record of a Journey to the Stars, and appears in several scholarly surveys of the field.

Its second importance lies in its medium. The book is a product of serialisation culture: a long hiatus mid-run saw readers circulate their own continuations, and when the author resumed he absorbed some of their material, leaving the later chapters uneven. That process — a text shaped jointly by author and readers — is precisely what distinguished early web fiction from print publishing.""",
    },
    "wochixihongshi": {
        "name": "我吃西红柿",
        "nameEn": "I Eat Tomatoes",
        "alias": ["朱洪志", "番茄"],
        "birthYear": 1987,
        "deathYear": None,
        "era": "dangdai",
        "awards": [
            "2017 第二届茅盾文学新人奖·网络文学新人奖",
            "2018 第三届「网文之王」",
            "2018 《盘龙》入选「中国网络文学 20 年 20 部优秀作品」",
            "2012 第七届中国作家富豪榜·网络作家富豪榜 第二名",
        ],
        "awardsEn": [
            "2017 Mao Dun New Writer Award, Web Fiction category (2nd)",
            "2018 Third King of Web Fiction title",
            "2018 Coiling Dragon named among the 20 Outstanding Works of Twenty Years of Chinese Web Literature",
            "2012 Second place, Web Writers Rich List, 7th Chinese Writers Rich List",
        ],
        "bodyZh": """\
中国网络文学代表人物之一，本名朱洪志，笔名又作「番茄」，1987 年生于江苏宝应。2005 年考入苏州大学数学系，同年以处女作《星峰传说》在起点中文网连载，在校两年发表六百余万字，大三上学期退学专职写作，现为阅文集团白金作家、中国作家协会会员。

他以玄幻、仙侠起家，《寸芒》于 2007 年 4 月成为网文界第一部月票破万的作品，《星辰变》《盘龙》《九鼎记》相继奠定其「小白文」开创者的地位——语言浅白、节奏流畅、升级路径清晰，读者群极为庞大。

2010 年连载《吞噬星空》（2012 年完结，四百七十八万字），是他由仙侠转向科幻的跨界之作，也被认为开启了网络科幻的新潮流：把修炼等级体系嫁接到宇宙文明尺度上，从地球怪兽危机一路写到宇宙海与起源大陆。该作 2020 年改编为动画在腾讯视频播出，2021 年入选中国网络文学影响力榜 IP 改编影响力榜，2023 年以数字形式入藏上海图书馆。

作为网络文学产业化的标志性作者，他的意义不止于文本：稳定的日更节奏、游戏化的情节结构、跨媒介的 IP 开发，共同定义了 2010 年代中国网络文学的生产方式。""",
        "bodyEn": """\
One of the defining figures of Chinese web fiction. Born Zhu Hongzhi in 1987 in Baoying, Jiangsu, and also writing as Tomato, he entered Suzhou University's mathematics department in 2005 and began serialising his first novel, Legend of Star Peak, on Qidian the same year. He published over six million characters in two years, left university in his third year to write full time, and is now a platinum author with Yuewen Group and a member of the China Writers Association.

He began with fantasy and xianxia. inch Blade became in April 2007 the first web novel to pass ten thousand monthly recommendation tickets, and Stellar Transformations, Coiling Dragon and Nine Cauldrons established him as the originator of so-called plain-style web fiction — simple language, brisk pacing, a clear progression ladder — with an enormous readership.

Swallowed Star (2010–2012, 4.78 million characters) marked his turn from xianxia to science fiction and is credited with opening a new current in online SF: grafting a cultivation hierarchy onto the scale of cosmic civilisation, moving from a monster crisis on Earth to the cosmic sea and the Origin Continent. It was adapted into an animation streamed on Tencent Video in 2020, named to the 2021 China Online Literature Influence List for IP adaptation, and collected in digital form by the Shanghai Library in 2023.

As a marker of the industrialisation of web fiction, his significance extends beyond the texts: a disciplined daily update rhythm, game-like plot structures and cross-media IP development together defined how Chinese web fiction was produced in the 2010s.""",
    },
}

WORKS = {
    "lanxueren": {
        "title": "蓝血人",
        "titleEn": "The Blue-Blooded Man",
        "author": "倪匡",
        "authorEn": "Ni Kuang",
        "authorSlug": "niquang",
        "year": 1964,
        "era": "xinzhongguo",
        "publisher": "明报",
        "publisherEn": "Ming Pao",
        "tags": ["香港科幻", "卫斯理", "外星文明", "系列", "太空"],
        "tagsEn": ["hong-kong-sf", "wisely", "alien-civilisation", "series", "space"],
        "sources": ["卫斯理系列第四部，1964 年出版"],
        "sourcesEn": ["Fourth book of the Wisely series, published 1964"],
        "awards": ["2000 入选「二十世纪中文小说百强」"],
        "awardsEn": ["2000 Selected among the 100 Best Chinese Novels of the 20th Century"],
        "featured": True,
        "coverPrompt": "Chinese science fiction paperback cover for '蓝血人' (The Blue-Blooded Man). A mysterious humanoid alien with luminous blue blood stands in a shadowed 1960s Hong Kong alley at night, neon signs reflecting in rain-slicked pavement, a damaged spacecraft hidden in the background mist. Retro pulp illustration, film noir lighting, deep cobalt and amber palette. Vertical poster composition, title text '蓝血人' clearly visible near top.",
        "bodyZh": """\
卫斯理系列第四部，1964 年出版，也是该系列由奇情冒险正式转向科幻的转折点。此后倪匡笔下的卫斯理故事，外星文明、时空穿梭、人体异变成为主轴。

故事从一具蓝色血液的尸体开始。卫斯理追查一桩离奇命案，逐步接触到流落地球的土星人方天——他的血液是蓝色的，在地球上隐匿多年，只求修好飞船重返故乡。卫斯理为帮助方天，卷入一连串追杀与逃亡。

小说的力量不在科学设定的严密，而在奇想与悬念的推进速度，以及那份属于冷战年代的宇宙想象：地球之外的来客并不带来征服或启示，他只是想回家。方天这个「回不去的外星人」形象，与卫斯理这位永远置身事外的旁观者，构成了倪匡科幻最核心的一组对照。

作为中国香港科幻的奠基文本，《蓝血人》把外星生命、星际航行等题材带入华语大众阅读，影响了一代读者。2000 年，它入选「二十世纪中文小说百强」。""",
        "bodyEn": """\
The fourth book of the Wisely series, published in 1964, and the turning point at which the series shifted from romantic adventure to science fiction. From here on, alien civilisations, time travel and bodily mutation became the mainstay of Ni Kuang's Wisely stories.

The story opens on a corpse with blue blood. Investigating a bizarre killing, Wisely gradually encounters Fang Tian, a Saturnian stranded on Earth whose blood runs blue and who has hidden for years, wanting only to repair his ship and go home. Helping him, Wisely is drawn into a chain of pursuit and flight.

The novel's power lies less in rigorous science than in the speed of its invention and suspense, and in a distinctly Cold War imagination of the cosmos: the visitor from beyond brings neither conquest nor revelation — he simply wants to go home. Fang Tian, the alien who cannot return, set against Wisely, the perpetual bystander, forms the central pairing of Ni Kuang's science fiction.

As the founding text of science fiction in Hong Kong, China, The Blue-Blooded Man carried extraterrestrial life and interstellar travel into popular Chinese-language reading and shaped a generation of readers. In 2000 it was selected among the 100 Best Chinese Novels of the 20th Century.""",
    },
    "xingyun-zuqu": {
        "title": "星云组曲",
        "titleEn": "Star Nebula Suite",
        "author": "张系国",
        "authorEn": "Chang Hsi-Kuo",
        "authorSlug": "zhangxiguo",
        "year": 1980,
        "era": "xinzhongguo",
        "publisher": "洪范书店",
        "publisherEn": "Hongfan Bookstore",
        "tags": ["台湾科幻", "短篇集", "呼回世界", "中国风味", "历史"],
        "tagsEn": ["taiwan-sf", "short-story-collection", "huhui-world", "chinese-flavour", "history"],
        "sources": ["台湾洪范书店，1980 年"],
        "sourcesEn": ["Hongfan Bookstore, Taiwan, 1980"],
        "awards": [],
        "awardsEn": [],
        "featured": True,
        "coverPrompt": "Chinese science fiction paperback cover for '星云组曲' (Star Nebula Suite). A vast bronze walled city on an alien planet beneath a swirling nebula, ancient Chinese-style fortifications fused with futuristic spires, tiny human figures gazing up at twin moons. Ink-wash texture with cosmic colour, muted teal and amber palette. Vertical poster composition, title text '星云组曲' clearly visible near top.",
        "bodyZh": """\
张系国科幻短篇的代表结集，1980 年由台湾洪范书店出版，收录 1976 年起在《联合报》副刊连载的系列作品。它被视为台湾科幻文学从倡导期走向成熟期的标志。

全书以「呼回世界」为背景：一个高度开化、可任意穿梭时空的外星文明，却有着城墙、关口与蛮族，形似古老的中华邦域。组曲中最重要的两篇是〈倾城之恋〉（1977）与〈铜像城〉（1980），前者写出索伦城的初建，后者写出它的末日预言——铜像与城市的符号对应，构成张系国「城」意象的原型，此后扩展为长篇「城」三部曲。

张系国追求的是「中国风味的科幻」：不复制西方太空歌剧的语汇，而以章回体、组曲形式与历史思辨承载科幻想象。他自陈从《棋王》起关心的始终是历史决定论的问题——「如何理解我们的历史和人类的处境」，并把科幻的人文意义定义为「历史浪漫情怀的再现」。

文字流畅清新、充满幽默感，常借科幻针砭现实，是台湾科幻「文以载道」一路的典范。""",
        "bodyEn": """\
The representative collection of Chang Hsi-Kuo's science fiction short stories, published in 1980 by Hongfan Bookstore in Taiwan, gathering work serialised in the United Daily News supplement from 1976. It is seen as the mark of Taiwanese science fiction passing from advocacy into maturity.

The book is set in the Huhui world, a highly civilised alien society able to travel through time at will, yet possessing walls, passes and barbarian tribes — shaped, oddly, like an ancient Chinese polity. The two central pieces are Love in a Fallen City (1977) and City of Bronze Statues (1980): the former depicts the founding of Solen City, the latter its apocalyptic prophecy. The correspondence between statue and city forms the prototype of Chang's city imagery, later expanded into the City trilogy.

What Chang sought was science fiction with a Chinese flavour: not a copy of Western space-opera vocabulary, but chapter-linked and suite forms carrying historical argument within SF imagination. He wrote that from Chess King onward his concern had always been historical determinism — "how to understand our history and the human condition" — and defined the humanistic meaning of science fiction as the return of historical romance.

Clear, fluent and humorous, using science fiction to satirise reality, the collection is the model of Taiwan's literature-as-vehicle strand of SF.""",
    },
    "cheng-wuyudie": {
        "title": "城·五玉碟",
        "titleEn": "City, Book One: Five Jade Disks",
        "author": "张系国",
        "authorEn": "Chang Hsi-Kuo",
        "authorSlug": "zhangxiguo",
        "year": 1983,
        "era": "xinzhongguo",
        "publisher": "知识系统出版有限公司",
        "publisherEn": "Knowledge Systems Publishing",
        "tags": ["台湾科幻", "长篇", "呼回世界", "索伦城", "时空穿梭", "中国风味"],
        "tagsEn": ["taiwan-sf", "novel", "huhui-world", "solen-city", "time-travel", "chinese-flavour"],
        "sources": ["台湾知识系统出版有限公司，1983 年"],
        "sourcesEn": ["Knowledge Systems Publishing, Taiwan, 1983"],
        "awards": [],
        "awardsEn": [],
        "featured": False,
        "coverPrompt": "Chinese science fiction paperback cover for '城·五玉碟' (City: Five Jade Disks). Five glowing jade disks floating above an immense walled alien city at dusk, the city blending ancient Chinese ramparts with strange technology, a lone traveller on the wall looking out over mist. Ink-wash meets cosmic, muted teal and amber palette, dramatic lighting. Vertical poster composition, title text '城·五玉碟' clearly visible near top.",
        "bodyZh": """\
「城」三部曲第一卷，1983 年由张系国自办的知识系统出版公司出版。作者自 1981 年夏开始经营这部长篇，前后费时十年，至《一羽毛》（1991）完成，是华语科幻最早的长篇系列之一。

故事舞台是呼回世界中的索伦城——一个可任意穿梭时空的文明所建立的城邦。五玉碟是贯穿全书的关键物件，牵引出索伦城的历史变迁、权力更迭与人物命运。张系国称这部作品是「既悲壮又诙谐的科幻武侠小说」。

它的独特之处，在于把科幻设定、武侠叙事与历史哲学熔于一炉。呼回世界有先进的科技，却保留着城墙、关口、蛮族等近似古代中国的形态；人物在时空穿梭中追问的，是历史能否被改变、个体在历史中居于何位。作者自称追求的是「历史的浪漫情怀」——「科幻小说的基本关怀，其实仍是人的处境」。

三部曲第二卷《龙城飞将》（1986）、第三卷《一羽毛》（1991）延续同一世界观。这套作品奠定了张系国在台湾科幻文坛的主帅地位，1986 年中国时报科幻小说奖更名为「张系国科幻小说奖」。""",
        "bodyEn": """\
The first volume of the City trilogy, published in 1983 by Knowledge Systems Publishing, the company Chang Hsi-Kuo founded himself. He began the novel in the summer of 1981 and worked on it for ten years, completing it with A Single Feather (1991); it is among the earliest full-length science fiction series in Chinese.

The stage is Solen City in the Huhui world, a city-state built by a civilisation able to move freely through time. The five jade disks are the object that runs through the book, drawing out the city's historical changes, its shifts of power and the fates of its people. Chang described the work as "at once tragic and comic, a science fiction wuxia novel".

Its distinctiveness lies in fusing SF premise, martial-arts narrative and philosophy of history. The Huhui world possesses advanced technology yet retains walls, passes and barbarian tribes resembling ancient China; what its characters pursue through time travel is whether history can be changed and where the individual stands within it. Chang said he sought "a romantic feeling for history" — that "the fundamental concern of science fiction is still the human condition".

The second volume, The Flying General of Dragon City (1986), and the third, A Single Feather (1991), continue the same world. The trilogy established Chang's leading position in Taiwanese science fiction, and in 1986 the China Times SF Award was renamed the Chang Hsi-Kuo Science Fiction Award.""",
    },
    "yinhe-mihangji": {
        "title": "银河迷航记",
        "titleEn": "Galactic Voyage Adrift",
        "author": "黄海",
        "authorEn": "Huang Hai",
        "authorSlug": "huanghai",
        "year": 1979,
        "era": "xinzhongguo",
        "publisher": "照明出版社",
        "publisherEn": "Zhaoming Publishing",
        "tags": ["台湾科幻", "短篇集", "太空", "星际航行", "乡愁"],
        "tagsEn": ["taiwan-sf", "short-story-collection", "space", "interstellar-voyage", "nostalgia"],
        "sources": ["台湾照明出版社，1979 年 10 月"],
        "sourcesEn": ["Zhaoming Publishing, Taiwan, October 1979"],
        "awards": ["〈银河迷航记〉曾改编为中广广播剧"],
        "awardsEn": ["Adapted as a radio drama by the Broadcasting Corporation of China"],
        "featured": True,
        "coverPrompt": "Chinese science fiction paperback cover for '银河迷航记' (Galactic Voyage Adrift). A lone spacecraft drifting through a dense starfield, its pilot seen in silhouette at the window, a small blue Earth receding in the distance, nebula clouds in violet and teal. Retro-futuristic ink-wash style, muted amber highlights. Vertical poster composition, title text '银河迷航记' clearly visible near top.",
        "bodyZh": """\
黄海的代表性科幻小说集，1979 年 10 月由台湾照明出版社出版，是他此前十年科幻短篇创作的结集，也是台湾成人科幻在 1970 年代的重要收获。

书名篇〈银河迷航记〉写冬眠中的太空人罗伦凯：银河九号飞船以高速航向无极的太空深处，他借助脑电仪幻游，看见数百年前的地球——锦绣河山、金色海滩、湛蓝天空，以及那个有着乌亮卷发、微笑迷人的女教师小珍。家园是那样具体，而它已在数百光年之外。

这部作品的情感核心是乡愁，而不是技术。黄海笔下的星际航行往往是孤独的：飞船高速远离，人类在冷冻睡眠中度过世纪，清醒的时刻只用来回忆。这种处理让台湾科幻在张系国的历史哲学、倪匡的奇想冒险之外，多了一条抒情与内省的路向。

黄海是台湾少儿科幻的开创者，同时也是唯一以科幻作品获得国家文艺奖与中山文艺奖的作家。〈银河迷航记〉曾改编为中广广播剧，〈机器人掉眼泪〉由公视改拍为电视剧，另有〈穿越地球〉〈深蓝的忧郁〉〈替代死刑〉等极短篇被选入国小与国中教科书。""",
        "bodyEn": """\
Huang Hai's representative science fiction collection, published in October 1979 by Zhaoming Publishing in Taiwan, gathering his short fiction of the preceding decade and marking a significant harvest for adult science fiction in 1970s Taiwan.

The title story follows Luo Renkai, an astronaut in hibernation: the Galactic No. 9 speeds toward the depths of space, and through an encephalograph he dreams of the Earth of centuries before — its rivers and mountains, its golden beaches and blue sky, and a young teacher with glossy curls and a dazzling smile. Home is utterly concrete, and it lies hundreds of light years away.

The emotional core is nostalgia rather than technology. Interstellar flight in Huang's work is lonely: ships recede at speed, humans sleep through centuries, and waking moments are spent remembering. That treatment gave Taiwanese science fiction a lyrical, introspective path distinct from Chang Hsi-Kuo's philosophy of history and Ni Kuang's romantic adventure.

Huang founded children's and young-adult science fiction in Taiwan and is the only writer to have won both the National Award for Arts and Letters and the Sun Yat-sen Literature Award for SF. Galactic Voyage Adrift was adapted as a radio drama by the Broadcasting Corporation of China, When Robots Cry was filmed for public television, and very short pieces such as Through the Earth, Deep Blue Melancholy and Substitute Execution have been included in primary and secondary school textbooks.""",
    },
    "diqiu-taowang": {
        "title": "地球逃亡",
        "titleEn": "Earth Escape",
        "author": "黄海",
        "authorEn": "Huang Hai",
        "authorSlug": "huanghai",
        "year": 1988,
        "era": "xinzhongguo",
        "publisher": "洪建全基金会",
        "publisherEn": "Hong Chien-chuan Foundation",
        "tags": ["台湾科幻", "太阳危机", "流浪", "少儿科幻", "末日"],
        "tagsEn": ["taiwan-sf", "solar-crisis", "wandering", "juvenile-sf", "apocalypse"],
        "sources": ["台湾洪建全基金会，1988 年"],
        "sourcesEn": ["Hong Chien-chuan Foundation, Taiwan, 1988"],
        "awards": ["1988 东方少年小说奖"],
        "awardsEn": ["1988 Oriental Youth Fiction Award"],
        "featured": True,
        "coverPrompt": "Chinese science fiction paperback cover for '地球逃亡' (Earth Escape). The planet Earth fitted with colossal glowing engines trailing plasma, leaving a dying red-giant sun behind, the small blue world dwarfed by cosmic scale. Ink-wash meets cosmic, muted teal and amber palette, dramatic chiaroscuro lighting. Vertical poster composition, title text '地球逃亡' clearly visible near top.",
        "bodyZh": """\
黄海 1988 年发表的少年科幻小说，获东方少年小说奖。它提出了一个后来被中国读者反复记起的设定：太阳行将毁灭，人类为地球装上发动机，带着家园逃离太阳系。

这个设想比刘慈欣《流浪地球》（2000）早了十余年。两部作品的相似长期引发讨论，但它们的气质并不相同。黄海的《地球逃亡》是为少年读者写的，篇幅短小，重心放在逃离的决定与出发的时刻，而非两千年航程中的社会组织与工程细节。

黄海本人后来撰文比较过两作。他谦称自己的《地球逃亡》在工程描述上「只能甘拜下风」，并准确地指出：自己的小说「从地球才要出发就结束」——也就是说，他写的是出发的决断，而刘慈欣写的是整段旅程的代价。

这个对照恰好说明华语科幻在不同地区、不同年代各自生长，又彼此呼应。对读者而言，把两作并读，能看到同一个核心想象——带着地球走，而不是弃地球而去——在不同文体中的两种展开方式。""",
        "bodyEn": """\
A juvenile science fiction novel published by Huang Hai in 1988, winner of the Oriental Youth Fiction Award. It proposes a premise that Chinese readers have recalled repeatedly since: the sun is about to die, humanity fits engines to the Earth and flees the solar system with its home in tow.

The idea predates Liu Cixin's The Wandering Earth (2000) by more than a decade. The resemblance has long prompted discussion, but the two works differ in temper. Huang's Earth Escape is written for young readers, short in length, and places its weight on the decision to flee and the moment of departure, rather than on the social organisation and engineering detail of a two-thousand-year voyage.

Huang later compared the two himself. He conceded that his novel "can only yield" on engineering description, and observed precisely that his story "ends just as the Earth is about to set out" — he wrote the decision to leave, while Liu wrote the cost of the whole journey.

The contrast shows Chinese-language science fiction growing separately in different places and periods, yet echoing across them. Read together, the two works show a single core imagination — taking the Earth along rather than abandoning it — unfolding in two very different registers.""",
    },
    "shouzhongzhi-xinzhongai": {
        "title": "手中纸，心中爱",
        "titleEn": "The Paper Menagerie",
        "author": "刘宇昆",
        "authorEn": "Ken Liu",
        "authorSlug": "kenliu",
        "year": 2011,
        "era": "dangdai",
        "publisher": "《奇幻与科幻杂志》",
        "publisherEn": "The Magazine of Fantasy & Science Fiction",
        "tags": ["海外华语", "短篇", "雨果奖", "星云奖", "世界奇幻奖", "移民", "文化翻译", "亲情"],
        "tagsEn": ["overseas-chinese", "short-story", "hugo-award", "nebula-award", "world-fantasy-award", "immigration", "cultural-translation", "family"],
        "sources": ["《奇幻与科幻杂志》2011 年 3/4 月号"],
        "sourcesEn": ["The Magazine of Fantasy & Science Fiction, March/April 2011"],
        "awards": [
            "2012 雨果奖 最佳短篇",
            "2011 星云奖 最佳短篇",
            "2012 世界奇幻奖 最佳短篇",
            "2014 星云奖 最佳海外短篇",
        ],
        "awardsEn": [
            "2012 Hugo Award for Best Short Story",
            "2011 Nebula Award for Best Short Story",
            "2012 World Fantasy Award for Best Short Fiction",
            "2014 Seiun Award, Best Translated Short Fiction",
        ],
        "featured": True,
        "coverPrompt": "Chinese science fiction paperback cover for '手中纸，心中爱' (The Paper Menagerie). A small folded paper tiger glowing warmly in a child's hands, surrounded by drifting origami animals dissolving into light, a Chinese-language letter folded in the background. Soft watercolour and ink-wash, warm amber and muted teal palette, quiet intimate lighting. Vertical poster composition, title text '手中纸，心中爱' clearly visible near top.",
        "bodyZh": """\
刘宇昆发表于《奇幻与科幻杂志》2011 年 3/4 月号的短篇，是史上唯一一部同时赢得雨果奖、星云奖与世界奇幻奖三项大奖的虚构作品，也是华语背景写作在世界科幻舞台上最具代表性的一篇。

故事由一个华裔男孩讲出。他的母亲是通过邮购从中国到美国的邮购新娘，语言不通，只能靠折纸与他交流——那些折纸会动：纸做的老虎会在他掌心翻滚，纸做的青蛙会跳。随着男孩长大，他急于融入美国的一切，开始嫌恶母亲的口音、她的中式习惯、她说不清楚的英语，也渐渐不再看那些纸做的动物。

转折点出现在母亲去世后。他整理遗物时发现一封母亲用中文写给他的信，而他——一个被刻意教成只说英语的孩子——读不懂。最终他透过妻子翻译读到了这封信，才知道那些折纸里装着的究竟是什么。

这篇小说的核心不是科幻设定，而是文化翻译。折纸是母爱的载体，中文是母爱的载体，而两者的失效都源于同一个过程： assimilation。刘宇昆用最轻盈的意象承载了最沉重的命题——一个移民家庭中，语言如何既连接又隔绝两代人。

它也确立了刘宇昆此后创作的基本关切：殖民、语言、记忆，以及谁有权讲述谁的历史。""",
        "bodyEn": """\
A short story published in the March/April 2011 issue of The Magazine of Fantasy & Science Fiction, it is the only work of fiction ever to win the Hugo, Nebula and World Fantasy Awards, and the most representative piece of Chinese-diaspora writing on the world science fiction stage.

The story is told by a Chinese-American boy. His mother came from China as a mail-order bride, spoke no English, and could reach him only through origami — living origami: a paper tiger tumbling in his palm, a paper frog that hops. As the boy grows up, eager to be American in every way, he grows ashamed of her accent, her Chinese habits, her broken English, and stops seeing the paper animals.

The turning point comes after her death. Sorting her belongings he finds a letter she wrote to him in Chinese — and he, deliberately raised to speak only English, cannot read it. He has it translated by his wife, and only then learns what the origami carried.

The core of the story is not its SF premise but cultural translation. Origami carries a mother's love, Chinese carries a mother's love, and both fail through the same process: assimilation. Liu uses the lightest of images to bear the heaviest of subjects — how language in an immigrant family both joins and divides two generations.

It also established the concerns that run through his later work: colonialism, language, memory, and who has the right to tell whose history.""",
    },
    "xiaobing-chuanqi": {
        "title": "小兵传奇",
        "titleEn": "Legend of a Little Soldier",
        "author": "玄雨",
        "authorEn": "Xuan Yu",
        "authorSlug": "xuanyu",
        "year": 2003,
        "era": "dangdai",
        "publisher": "起点中文网",
        "publisherEn": "Qidian Chinese Network",
        "tags": ["网络文学", "星际军事", "机甲", "太空歌剧", "人工智能", "连载"],
        "tagsEn": ["web-fiction", "interstellar-military", "mecha", "space-opera", "artificial-intelligence", "serialised"],
        "sources": ["起点中文网，2003 年 4 月起连载，2007 年完结"],
        "sourcesEn": ["Qidian Chinese Network, serialised from April 2003, completed 2007"],
        "awards": ["与《诛仙》《飘邈之旅》并称「网络三大奇书」"],
        "awardsEn": ["Named one of the Three Marvels of early Chinese web fiction, with Zhu Xian and A Record of a Journey to the Stars"],
        "featured": True,
        "coverPrompt": "Chinese science fiction web novel cover for '小兵传奇' (Legend of a Little Soldier). A young soldier in powered armour standing on the bridge of a battered gunship, vast fleets of starships clashing beyond the viewport, a lone mecha silhouetted against an exploding planet. Digital illustration, cinematic lighting, deep blue and amber palette. Vertical poster composition, title text '小兵传奇' clearly visible near top.",
        "bodyZh": """\
中国网络文学「星际军事」流派的开山之作。自 2003 年 4 月起在起点中文网连载，2007 年完结，全书约二百一十万字，与《诛仙》《飘邈之旅》并称「网络三大奇书」。

故事从高中毕业生唐龙参军开始。他选了最不受待见的步兵，却阴差阳错进入被遗忘的 23 团，在五台智能机器人的残酷训练下脱胎换骨，还在全息战争游戏《战争》中拿下宇宙第一。此后他当上自走炮舰舰长，以一千艘被当作炮灰的战舰歼灭敌方两千艘正规战舰，战功却被权贵侵吞；他从复仇走向割据，最终统一宇宙。

作品的价值首先在类型开创。它把机甲、星际舰队、超光速航行、人工智能与军事谋略、星际政治熔为一炉，奠定了后续「星际军事文」的世界观范式，影响到《师士传说》《机动风暴》等一批创作。

其次在于它的媒介形态。连载中途长期断更，网络上流传出各种读者续写版本，作者恢复更新后吸收了其中部分设定，导致后期文风驳杂。这种作者与读者共同塑造文本的过程，是早期网络文学区别于纸面出版的核心经验，也使这部作品成为研究中国网络文学生产方式无法绕开的样本。""",
        "bodyEn": """\
The founding work of the interstellar-military strand of Chinese web fiction. Serialised on Qidian from April 2003 and completed in 2007 at roughly 2.1 million characters, it is named one of the Three Marvels of early web fiction alongside Zhu Xian and A Record of a Journey to the Stars.

The story begins with Tang Long, a high-school graduate who joins the army and picks the least regarded branch, the infantry, only to be assigned by accident to the forgotten 23rd Regiment. Five intelligent robots train him brutally, and he takes first place across the universe in the holographic war game War. He then commands an expendable self-propelled gunship, destroying two thousand enemy warships with a thousand ships meant as cannon fodder — and has the credit stolen by his superiors. He moves from revenge to separatism and finally to the unification of the universe.

Its first value is generic. Fusing mecha, interstellar fleets, faster-than-light travel and artificial intelligence with military strategy and interstellar politics, it set the world-building template for later interstellar-military fiction and shaped works such as Master of Mecha and Storm of Maneuver.

Its second lies in its medium. During a long hiatus readers circulated their own continuations; when the author resumed he absorbed some of their material, leaving the later chapters uneven. That joint shaping of a text by author and readers is precisely what distinguished early web fiction from print publishing, and makes this novel unavoidable for anyone studying how Chinese web literature is produced.""",
    },
    "tunshi-xingkong": {
        "title": "吞噬星空",
        "titleEn": "Swallowed Star",
        "author": "我吃西红柿",
        "authorEn": "I Eat Tomatoes",
        "authorSlug": "wochixihongshi",
        "year": 2010,
        "era": "dangdai",
        "publisher": "起点中文网",
        "publisherEn": "Qidian Chinese Network",
        "tags": ["网络文学", "宇宙", "修炼", "怪兽", "长篇", "IP改编"],
        "tagsEn": ["web-fiction", "cosmos", "cultivation", "monsters", "novel", "ip-adaptation"],
        "sources": ["起点中文网，2010 年 7 月 20 日至 2012 年 7 月 21 日连载"],
        "sourcesEn": ["Qidian Chinese Network, serialised 20 July 2010 – 21 July 2012"],
        "awards": [
            "2021 中国网络文学影响力榜·IP 改编影响力榜",
            "2023 以数字形式入藏上海图书馆",
            "2025 入选 2024 网络文学神作榜",
        ],
        "awardsEn": [
            "2021 China Online Literature Influence List, IP Adaptation category",
            "2023 Collected in digital form by Shanghai Library",
            "2025 Named to the 2024 Web Literature Masterpiece List",
        ],
        "featured": True,
        "coverPrompt": "Chinese science fiction web novel cover for '吞噬星空' (Swallowed Star). A young warrior in futuristic battle armour standing before a colossal star-devouring beast in the void, a ruined near-future Earth city visible on a distant planet, cosmic nebula swirls behind. Digital illustration, cinematic lighting, violet and amber palette. Vertical poster composition, title text '吞噬星空' clearly visible near top.",
        "bodyZh": """\
我吃西红柿的第六部长篇，2010 年 7 月 20 日至 2012 年 7 月 21 日连载于起点中文网，四百七十八万字，是他由仙侠转向科幻的跨界之作，也被认为开启了网络科幻的新潮流。

故事始于一场大灾难：RR 病毒引发「大涅槃时期」，地球生物大规模变异，怪兽肆虐，人类退守基地市。少年罗峰高考失利，却意外觉醒精神念力，从此踏上武者之路。他获得陨墨星主人呼延博的传承，成为地球三强者之一，在与星空吞噬巨兽金角巨兽一战失去肉身后，夺舍成为星空吞噬兽，在体内世界育出人类分身，随后迈出地球走向宇宙。

作品的独特之处，在于把网络文学成熟的修炼等级体系嫁接到宇宙文明尺度上：从星球级、宇宙级到不朽、宇宙之主，力量层级的每一次跃迁都对应着更宏大的空间——地球、星系、宇宙海、起源大陆。这种「可量级的成长」与太空歌剧式的场景结合，形成了极强阅读黏性。

它是网络文学产业化与 IP 开发的标志性案例：2012 年起出版实体书，2018 年推出同名手游，2020 年 11 月改编动画在腾讯视频播出，2021 年入选中国网络文学影响力榜 IP 改编影响力榜，2023 年以数字形式入藏上海图书馆。""",
        "bodyEn": """\
The sixth novel by I Eat Tomatoes, serialised on Qidian from 20 July 2010 to 21 July 2012 at 4.78 million characters. It marked his turn from xianxia to science fiction and is credited with opening a new current in online SF.

The story begins with catastrophe: an RR virus triggers the Great Nirvana, mutating life across the planet, and humanity retreats into fortress cities as monsters overrun the wild. Luo Feng fails his university entrance exam but awakens psychic powers and sets out as a warrior. He inherits the legacy of Huyan Bo, lord of the Fallen Ink Star, and becomes one of Earth's three strongest; after losing his body fighting the star-devouring beast Golden Horned Behemoth, he seizes its form, grows a human clone within his inner world, and steps out into the universe.

Its distinctiveness lies in grafting web fiction's mature cultivation hierarchy onto a cosmic scale: planetary, cosmic, immortal, lord of the universe — each leap in power matched by a larger stage, from Earth to star systems, the cosmic sea and the Origin Continent. That quantifiable progression combined with space-opera spectacle proved enormously sticky for readers.

It is a landmark case of web fiction's industrialisation and IP development: print editions from 2012, a mobile game in 2018, an animated adaptation streamed on Tencent Video from November 2020, inclusion in the 2021 China Online Literature Influence List for IP adaptation, and acquisition in digital form by the Shanghai Library in 2023.""",
    },
}

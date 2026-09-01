# -*- coding: utf-8 -*-
"""30 位作者 + 「佚名」条目（中英双语）。

字段：slug / era / birth / death / zh{name,bio} / en{name,bio}
在世作者一律 photoCredit=placeholder（不使用真实照片，遵守肖像权规范）。
"""

AUTHORS = [
    # ---------------------------------------------------------- 上古 · 神话志怪
    {
        "slug": "anonymous",
        "era": "shanggu",
        "birth": None,
        "death": None,
        "zh": {
            "name": "佚名",
            "bio": "上古经典多由集体累积而成，作者不可考。《山海经》《穆天子传》《神异经》等均归入此条目，不虚构具体作者。",
        },
        "en": {
            "name": "Anonymous",
            "bio": "Classical works of antiquity were typically accreted collectively, with no attributable author. Works such as the Classic of Mountains and Seas are filed here rather than assigned an invented author.",
        },
    },
    {
        "slug": "lieyukou",
        "era": "shanggu",
        "birth": None,
        "death": None,
        "zh": {
            "name": "列御寇",
            "bio": "相传为战国时期道家人物，《列子》八篇托名于他。《汤问》篇中的「偃师造人」被视为中国最早的机器人想象。",
        },
        "en": {
            "name": "Lie Yukou",
            "bio": "A Warring States figure associated with Daoism, to whom the eight chapters of the Liezi are attributed. Its 'King Tang's Questions' contains the Yanshi automaton, China's earliest robot imagination.",
        },
    },
    {
        "slug": "zhanghua",
        "era": "shanggu",
        "birth": 232,
        "death": 300,
        "zh": {
            "name": "张华",
            "bio": "西晋政治家、文学家，官至司空。所撰《博物志》广记山川异物、奇技方术，是志怪博物传统的关键文本。",
        },
        "en": {
            "name": "Zhang Hua",
            "bio": "A Western Jin statesman and writer who rose to Minister of Works. His Record of Diverse Matters catalogues strange lands, objects and techniques, a key text of the marvel tradition.",
        },
    },
    {
        "slug": "wangjia",
        "era": "shanggu",
        "birth": None,
        "death": 390,
        "zh": {
            "name": "王嘉",
            "bio": "东晋方士，隐居终南山。所撰《拾遗记》杂录上古至晋的奇闻异事，其中贯月槎、沦波舟等飞行器想象尤为著名。",
        },
        "en": {
            "name": "Wang Jia",
            "bio": "An Eastern Jin recluse and fangshi who compiled Researches into Lost Records, a collection of marvels from antiquity to his own day, notable for its flying vessels.",
        },
    },
    {
        "slug": "ganbao",
        "era": "shanggu",
        "birth": None,
        "death": 336,
        "zh": {
            "name": "干宝",
            "bio": "东晋史学家、文学家，曾任著作郎。《搜神记》原书已散佚，今本为后人辑录，是志怪小说的奠基之作。",
        },
        "en": {
            "name": "Gan Bao",
            "bio": "An Eastern Jin historian and writer. His In Search of the Supernatural, though surviving only in later recensions, is the foundational text of Chinese tales of the strange.",
        },
    },
    {
        "slug": "duanchengshi",
        "era": "shanggu",
        "birth": 803,
        "death": 863,
        "zh": {
            "name": "段成式",
            "bio": "唐代文学家，博闻强记。《酉阳杂俎》包罗志怪、博物与异域奇闻，其中的「月中人」故事被视为中国早期登月想象。",
        },
        "en": {
            "name": "Duan Chengshi",
            "bio": "A Tang man of letters of prodigious learning. His Miscellaneous Morsels from Youyang gathers marvels, natural lore and foreign wonders, including an early tale of travellers to the moon.",
        },
    },
    {
        "slug": "wuchengen",
        "era": "song-ming-qing",
        "birth": 1500,
        "death": 1582,
        "zh": {
            "name": "吴承恩",
            "bio": "明代文学家，屡试不第，晚年著书自娱。《西游记》以取经故事为骨架，构建了一个想象力磅礴的神魔世界。",
        },
        "en": {
            "name": "Wu Cheng'en",
            "bio": "A Ming writer who never advanced far in the examinations. Journey to the West builds a vast demon-and-deity cosmos on the frame of the pilgrimage to India.",
        },
    },
    {
        "slug": "liruzhen",
        "era": "song-ming-qing",
        "birth": 1763,
        "death": 1830,
        "zh": {
            "name": "李汝珍",
            "bio": "清代小说家，字松石，博通音韵、医算，以二十年之力著成《镜花缘》一百回。书中海外奇国与机械想象，使其成为中国「前科幻」的代表人物。",
        },
        "en": {
            "name": "Li Ruzhen",
            "bio": "A Qing novelist, styled Songshi, erudite in phonology, medicine and mathematics, who spent two decades on Flowers in the Mirror. Its exotic lands and machines make him the representative figure of Chinese proto-SF.",
        },
    },
    # -------------------------------------------------------------- 晚清 · 民国
    {
        "slug": "liangqichao",
        "era": "wanqing",
        "birth": 1873,
        "death": 1929,
        "zh": {
            "name": "梁启超",
            "bio": "近代思想家、政治家，戊戌变法领袖之一。1902 年发表《新中国未来记》，开「未来记」体政治小说先河，是晚清科幻热潮的思想源头。",
        },
        "en": {
            "name": "Liang Qichao",
            "bio": "A reformist thinker and statesman, a leader of the Hundred Days' Reform. His 1902 Future of New China inaugurated the 'future history' political novel and set the Late Qing SF boom in motion.",
        },
    },
    {
        "slug": "luxun",
        "era": "wanqing",
        "birth": 1881,
        "death": 1936,
        "zh": {
            "name": "鲁迅",
            "bio": "现代文学奠基人。1903 年译《月界旅行》并作《辨言》，首次系统引入「科学小说」概念，是中国科幻的理论起点。本条目收录其译介贡献，与原创作家分列。",
        },
        "en": {
            "name": "Lu Xun",
            "bio": "Founder of modern Chinese literature. His 1903 translation of De la Terre à la Lune and its preface introduced the concept of 'science fiction' to Chinese readers. Listed here for his work as translator and theorist, not as a novelist of SF.",
        },
    },
    {
        "slug": "huangjiangdiaosou",
        "era": "wanqing",
        "birth": None,
        "death": None,
        "zh": {
            "name": "荒江钓叟",
            "bio": "晚清小说家，真实姓名与生平不详。1904 年起在《绣像小说》连载《月球殖民地小说》，是中国科幻长篇的起点作者。",
        },
        "en": {
            "name": "Hermit of the Deserted River",
            "bio": "A Late Qing novelist whose real name and biography remain unknown. From 1904 he serialised Moon Colony Novel in Illustrated Fiction, making him the founding author of the Chinese science fiction novel.",
        },
    },
    {
        "slug": "xunianci",
        "era": "wanqing",
        "birth": 1875,
        "death": 1908,
        "zh": {
            "name": "徐念慈",
            "bio": "晚清小说家、翻译家、编辑，主编《小说林》。所著《新法螺先生谭》以灵魂飞升、游历星球展开，是晚清科幻的代表作之一。",
        },
        "en": {
            "name": "Xu Nianci",
            "bio": "A Late Qing novelist, translator and editor of Forest of Fiction. His New Tales of Mr. Windbag sends a soul flying among the planets, a landmark of Late Qing science fiction.",
        },
    },
    {
        "slug": "wujianren",
        "era": "wanqing",
        "birth": 1866,
        "death": 1910,
        "zh": {
            "name": "吴趼人",
            "bio": "晚清小说家，笔名我佛山人，代表作《二十年目睹之怪现状》。《新石头记》借贾宝玉历险，写理想国与科技奇观。",
        },
        "en": {
            "name": "Wu Jianren",
            "bio": "A Late Qing novelist, pen name 'I, the Buddha of Foshan', best known for Bizarre Happenings Eyewitnessed over Two Decades. His New Story of the Stone sends Jia Baoyu into a technological utopia.",
        },
    },
    {
        "slug": "lushie",
        "era": "wanqing",
        "birth": 1878,
        "death": 1944,
        "zh": {
            "name": "陆士谔",
            "bio": "晚清民初小说家、医家，著述甚丰。《新中国》以梦境写 1951 年的上海，预言地铁、跨江大桥与万国博览会。",
        },
        "en": {
            "name": "Lu Shi'e",
            "bio": "A prolific novelist and physician active from the Late Qing into the Republic. His New China dreams up a 1951 Shanghai with subways, bridges and an international exposition.",
        },
    },
    {
        "slug": "laoshe",
        "era": "minguo",
        "birth": 1899,
        "death": 1966,
        "zh": {
            "name": "老舍",
            "bio": "现代文学大家，代表作《骆驼祥子》《四世同堂》。1932 年所作《猫城记》以火星猫国寓言批判社会，是中国现代科幻的重要一环。",
        },
        "en": {
            "name": "Lao She",
            "bio": "A major modern writer, author of Rickshaw Boy and Four Generations Under One Roof. His 1932 Cat Country uses a Martian allegory for social critique, a key work of modern Chinese SF.",
        },
    },
    {
        "slug": "gujunzheng",
        "era": "minguo",
        "birth": 1902,
        "death": 1980,
        "zh": {
            "name": "顾均正",
            "bio": "科普作家、编辑，长期致力于科学小品创作。1940 年出版《和平的梦》等科幻短篇，把科学知识与战时想象结合。",
        },
        "en": {
            "name": "Gu Junzheng",
            "bio": "A science populariser and editor who wrote science fiction alongside his popular-science essays. His 1940 collection Dream of Peace fuses scientific knowledge with wartime imagination.",
        },
    },
    # ------------------------------------------------------------------ 新中国
    {
        "slug": "zhengwenguang",
        "era": "xinzhongguo",
        "birth": 1929,
        "death": 2003,
        "zh": {
            "name": "郑文光",
            "bio": "中国科幻文学的重要奠基者，曾任中国科幻小说研究会会长。《火星建设者》《飞向人马座》影响数代读者，被称为「中国科幻之父」。",
        },
        "en": {
            "name": "Zheng Wenguang",
            "bio": "A founding figure of Chinese science fiction and first president of the Chinese Science Fiction Society. The Builders of Mars and Flight to Sagittarius shaped generations; he is often called the father of Chinese SF.",
        },
    },
    {
        "slug": "tongenzheng",
        "era": "xinzhongguo",
        "birth": 1935,
        "death": 1997,
        "zh": {
            "name": "童恩正",
            "bio": "考古学家、科幻作家，四川大学教授。《珊瑚岛上的死光》(1978) 是新时期科幻复苏的标志，1980 年被改编为中国第一部科幻电影。",
        },
        "en": {
            "name": "Tong Enzheng",
            "bio": "Archaeologist and science fiction writer, professor at Sichuan University. Death Ray on a Coral Island (1978) marked the post-1978 revival and was filmed in 1980 as China's first SF feature.",
        },
    },
    {
        "slug": "yeyonglie",
        "era": "xinzhongguo",
        "birth": 1940,
        "death": 2020,
        "zh": {
            "name": "叶永烈",
            "bio": "科普与纪实作家，著述逾三千万字。《小灵通漫游未来》以儿童视角描绘未来科技，是发行量最大的中国科幻作品之一。",
        },
        "en": {
            "name": "Ye Yonglie",
            "bio": "A prolific popular-science and non-fiction writer. Xiao Lingtong Travels to the Future depicts future technology through a child's eyes and is among the best-selling Chinese SF works ever.",
        },
    },
    {
        "slug": "xiaojianheng",
        "era": "xinzhongguo",
        "birth": 1930,
        "death": None,
        "zh": {
            "name": "萧建亨",
            "bio": "科幻作家，中国科幻早期拓荒者之一。《布克的奇遇》等作品以儿童科幻见长，兼具科学趣味与想象。",
        },
        "en": {
            "name": "Xiao Jianheng",
            "bio": "One of the pioneers of early Chinese science fiction. Works such as The Adventure of Booker are children's SF that pair scientific curiosity with imagination.",
        },
    },
    # -------------------------------------------------------------------- 当代
    {
        "slug": "xinghe",
        "era": "dangdai",
        "birth": 1967,
        "death": None,
        "zh": {
            "name": "星河",
            "bio": "当代科幻作家，1990 年代崛起。《决斗在网络》是国内最早的网络题材科幻之一，长期关注技术与人的关系。",
        },
        "en": {
            "name": "Xinghe",
            "bio": "A science fiction writer who emerged in the 1990s. Duel on the Network is among the earliest Chinese cyber-themed SF; his work consistently examines the relation between technology and the human.",
        },
    },
    {
        "slug": "wangjinkang",
        "era": "dangdai",
        "birth": 1948,
        "death": None,
        "zh": {
            "name": "王晋康",
            "bio": "当代科幻代表作家之一，高级工程师出身。作品以硬核技术设想与伦理思辨见长，《生命之歌》《七重外壳》《逃出母宇宙》等影响广泛。",
        },
        "en": {
            "name": "Wang Jinkang",
            "bio": "A leading contemporary SF writer and engineer by training, known for hard technical speculation and ethical inquiry. Song of Life, Seven-Layer Shell and Escape from the Mother Universe are among his best-known works.",
        },
    },
    {
        "slug": "hansong",
        "era": "dangdai",
        "birth": 1965,
        "death": None,
        "zh": {
            "name": "韩松",
            "bio": "当代科幻作家，新华社记者。作品以冷峻、荒诞与现实批判著称，《地铁》《医院》《2066年之西行漫记》构成独特的「技术中国」书写。",
        },
        "en": {
            "name": "Han Song",
            "bio": "A contemporary SF writer and journalist. His austerely absurd, socially critical fiction — Subway, Hospital, 2066: A Journey to the West — forms a singular portrait of a technological China.",
        },
    },
    {
        "slug": "hexi",
        "era": "dangdai",
        "birth": 1971,
        "death": None,
        "zh": {
            "name": "何夕",
            "bio": "当代科幻作家，以细腻的科学构想与人文关怀见长。《六道众生》《伤心者》《天年》等作品多次获银河奖。",
        },
        "en": {
            "name": "He Xi",
            "bio": "A contemporary SF writer noted for finely worked scientific premises and humanistic concern. Six Paths of Existence, The Heartbroken and The Cosmic Year have won multiple Galaxy Awards.",
        },
    },
    {
        "slug": "liucixin",
        "era": "dangdai",
        "birth": 1963,
        "death": None,
        "zh": {
            "name": "刘慈欣",
            "bio": "中国最具国际影响力的科幻作家，长期从事工程工作。《三体》三部曲 2015 年获雨果奖最佳长篇小说，另有《球状闪电》《流浪地球》等代表作。",
        },
        "en": {
            "name": "Liu Cixin",
            "bio": "China's most internationally influential science fiction writer, long employed as an engineer. The Remembrance of Earth's Past trilogy won the 2015 Hugo Award for Best Novel; other major works include Ball Lightning and The Wandering Earth.",
        },
    },
    {
        "slug": "haojingfang",
        "era": "dangdai",
        "birth": 1984,
        "death": None,
        "zh": {
            "name": "郝景芳",
            "bio": "当代科幻作家、经济学研究者。《北京折叠》2016 年获雨果奖最佳中短篇小说，以空间折叠隐喻阶层分化。",
        },
        "en": {
            "name": "Hao Jingfang",
            "bio": "A contemporary SF writer and economics researcher. Folding Beijing won the 2016 Hugo Award for Best Novelette, using folded space as a figure for social stratification.",
        },
    },
    {
        "slug": "chenqiufan",
        "era": "dangdai",
        "birth": 1981,
        "death": None,
        "zh": {
            "name": "陈楸帆",
            "bio": "当代科幻作家，近年聚焦人工智能与近未来议题。《荒潮》以电子垃圾岛为背景，《人生算法》探讨算法社会中的个体处境。",
        },
        "en": {
            "name": "Chen Qiufan",
            "bio": "A contemporary SF writer focused on artificial intelligence and the near future. Waste Tide is set on an e-waste island; Algorithms for Life examines the individual inside an algorithmic society.",
        },
    },
    {
        "slug": "baoshu",
        "era": "dangdai",
        "birth": 1980,
        "death": None,
        "zh": {
            "name": "宝树",
            "bio": "当代科幻作家、学者。《时间之墟》以时间循环构建宏大叙事，另著有《三体X：观想之宙》等同人创作。",
        },
        "en": {
            "name": "Baoshu",
            "bio": "A contemporary SF writer and scholar. The Ruins of Time builds an epic on a time loop; he has also written fan works such as Three-Body X: Contemplating the Universe.",
        },
    },
    {
        "slug": "chengjingbo",
        "era": "dangdai",
        "birth": 1981,
        "death": None,
        "zh": {
            "name": "程婧波",
            "bio": "当代科幻作家，作品风格细腻、意象独特。《倒悬的天空》《宿主》等多次获银河奖与华语科幻星云奖。",
        },
        "en": {
            "name": "Cheng Jingbo",
            "bio": "A contemporary SF writer with a delicate style and distinctive imagery. The Inverted Sky and The Host have won Galaxy and Nebula Awards.",
        },
    },
    {
        "slug": "jiangbo",
        "era": "dangdai",
        "birth": 1977,
        "death": None,
        "zh": {
            "name": "江波",
            "bio": "当代科幻作家，以硬科幻见长。《银河之心》三部曲构建宏大太空歌剧，《机器之道》探讨人工智能的演化。",
        },
        "en": {
            "name": "Jiang Bo",
            "bio": "A contemporary hard-SF writer. The Heart of the Galaxy trilogy is a grand space opera; The Way of Machines traces the evolution of artificial intelligence.",
        },
    },
    {
        "slug": "zhangran",
        "era": "dangdai",
        "birth": 1981,
        "death": None,
        "zh": {
            "name": "张冉",
            "bio": "当代科幻作家、记者。《以太》以信息管控为题材获银河奖，《起风之城》等作品兼具技术想象与人文温度。",
        },
        "en": {
            "name": "Zhang Ran",
            "bio": "A contemporary SF writer and journalist. Ether, on the control of information, won a Galaxy Award; his work pairs technological imagination with human warmth.",
        },
    },
]

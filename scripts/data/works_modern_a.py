# -*- coding: utf-8 -*-
"""新中国（1949–1990）作品 + 当代前三位作者（星河 / 王晋康 / 韩松）。

中文简介 300–500 字，四段结构：① 性质与出版 ② 内容 ③ 想象/科学元素 ④ 地位影响。
正文内一律使用「」与《》，不使用 ASCII 直引号。
"""

WORKS_MODERN_A = [
    # ================================================================= 新中国
    {
        "slug": "huoxing-jianshezhe",
        "era": "xinzhongguo", "kind": "sf", "year": 1957,
        "author": "郑文光", "authorSlug": "zhengwenguang",
        "publisher": "中国青年出版社",
        "coverCredit": "placeholder",
        "tags": ["火星", "建设", "太空"],
        "sources": ["《火星建设者》郑文光，1957"],
        "zh": {"title": "火星建设者", "body": "《火星建设者》是郑文光发表于 1957 年的作品，属于新中国科幻的早期代表作。"
            "彼时中国科幻尚处于起步阶段，主要面向青少年读者，"
            "承担着普及科学知识、鼓舞建设热情的双重任务。\n\n"
            "小说叙中国青年参加火星建设，在恶劣的火星环境中勘测、施工、"
            "改造大气与地表，逐步把一颗荒凉行星变为可居之地。"
            "故事以集体劳动为主线，穿插对火星地貌与气候的描写。\n\n"
            "其想象力有两个特点：一是把太空探索处理为一项可组织、可分工的建设工程，"
            "而非个人冒险——这与当时强调集体主义的语境一致；"
            "二是对火星环境改造的设想，已触及后世所称的「地球化」概念。\n\n"
            "该作与郑文光此后的《飞向人马座》一起，"
            "奠定了他在中国科幻史上的开创地位。"
            "本站归入科幻层，列为新中国时段的起点作品。"},
        "en": {"title": "The Builders of Mars", "body": "Published by Zheng Wenguang in 1957, this is an early representative work of science fiction in the People's Republic, when the genre was still finding its feet, addressed largely to young readers, and charged with both spreading scientific knowledge and encouraging enthusiasm for construction.\n\n"
            "It follows Chinese youths who join the building of Mars: surveying, constructing, and altering the atmosphere and surface to turn a barren planet into habitable ground. Collective labour carries the plot, interwoven with descriptions of Martian terrain and climate.\n\n"
            "Two features of its imagination stand out. Space exploration is treated as an organised, divisible engineering project rather than an individual adventure, in keeping with the collectivist idiom of its day; and its idea of transforming the Martian environment touches what would later be called terraforming.\n\n"
            "Together with Zheng's later Flight to Sagittarius, it established his founding position in the history of Chinese science fiction. Filed as SF, and placed first among the New China entries."},
    },
    {
        "slug": "guxia-miwu",
        "era": "xinzhongguo", "kind": "sf", "year": 1960,
        "author": "童恩正", "authorSlug": "tongenzheng",
        "publisher": "少年儿童出版社",
        "coverCredit": "placeholder",
        "tags": ["考古", "探险", "科幻"],
        "sources": ["《古峡迷雾》童恩正，1960"],
        "zh": {"title": "古峡迷雾", "body": "《古峡迷雾》是童恩正 1960 年出版的作品，"
            "也是他早期将考古学与科幻叙事结合的代表作。"
            "童恩正本人是考古学者，长期任教于四川大学，"
            "这一专业背景在此后的创作中反复发挥作用。\n\n"
            "小说以一支考古考察队进入峡谷为线索，"
            "在实地勘探中遭遇一连串异常现象，"
            "最终揭开一段被自然与人为双重掩埋的历史。"
            "叙事采用层层推进的探案式结构，"
            "把专业考察步骤写得相当扎实。\n\n"
            "其特别之处在于方法论：谜团的解答不依赖超自然力量，"
            "而来自地质、生物与考古证据的推理。"
            "这种以科学程序推动叙事的做法，"
            "在当时以幻想为主的少年科幻中颇为少见。\n\n"
            "该作开创了童恩正独有的「考古科幻」路径，"
            "此后《雪山魔笛》等作品沿此发展。"
            "本站归入科幻层。"},
        "en": {"title": "Mist in the Ancient Gorge", "body": "Published by Tong Enzheng in 1960, this is an early representative work of his fusion of archaeology with science fiction narrative. Tong was himself an archaeologist who taught for years at Sichuan University, and that training recurs throughout his fiction.\n\n"
            "The novel follows an archaeological team into a gorge, where a series of anomalies encountered during fieldwork leads to the uncovering of a history buried twice over, by nature and by human hand. A stepwise, detection-like structure carries the plot, and the procedures of field survey are rendered with real solidity.\n\n"
            "Its methodological distinctiveness is the point: the mystery is solved not by supernatural agency but by inference from geological, biological and archaeological evidence. Driving narrative by scientific procedure was unusual in juvenile science fiction of the period, which leaned on fantasy.\n\n"
            "It opened the path of archaeological science fiction that Tong made his own and that later works such as The Magic Flute of the Snow Mountain continued. Filed as SF."},
    },
    {
        "slug": "buke-de-qiyu",
        "era": "xinzhongguo", "kind": "sf", "year": 1962,
        "author": "萧建亨", "authorSlug": "xiaojianheng",
        "publisher": "少年儿童出版社",
        "coverCredit": "placeholder",
        "tags": ["儿童科幻", "动物", "科学"],
        "sources": ["《布克的奇遇》萧建亨，1962"],
        "zh": {"title": "布克的奇遇", "body": "《布克的奇遇》是萧建亨 1962 年发表的儿童科幻小说，"
            "也是他流传最广的作品。"
            "萧建亨是中国科幻早期的重要拓荒者之一，"
            "创作跨越数十年，以儿童与少年题材见长。\n\n"
            "小说围绕一只名叫布克的狗展开。"
            "布克在一次事故中受伤，"
            "被科研人员施以器官移植手术，"
            "由此引出一系列关于生命、记忆与身份的连锁反应。"
            "故事以儿童的视角和语言推进，"
            "把复杂的医学设想讲得浅显可感。\n\n"
            "其想象力集中在移植技术上："
            "作品设想的不仅是器官的替换，"
            "更涉及术后个体连续性的追问——"
            "换了器官的布克还是原来的布克吗？"
            "这一设问在今天的科幻中仍是核心命题。\n\n"
            "作为新中国儿童科幻的经典之作，"
            "它影响了数代读者对科学的最初想象。"
            "本站归入科幻层。"},
        "en": {"title": "The Adventure of Booker", "body": "Published by Xiao Jianheng in 1962, this is his most widely read work. Xiao was one of the important pioneers of early Chinese science fiction, writing across several decades chiefly for children and young readers.\n\n"
            "The story turns on a dog named Booker who is injured in an accident and given organ transplants by medical researchers, setting off a chain of consequences concerning life, memory and identity. Told from a child's perspective in a child's language, it renders complex medical speculation plainly.\n\n"
            "Its imagination centres on transplantation: what is conceived is not merely the replacement of organs but the question of the continuity of the individual afterwards — is Booker, with new organs, still Booker? That question remains central to science fiction today.\n\n"
            "A classic of children's science fiction in the People's Republic, it shaped the earliest scientific imaginings of generations of readers. Filed as SF."},
    },
    {
        "slug": "feixiang-renmazuo",
        "era": "xinzhongguo", "kind": "sf", "year": 1978,
        "author": "郑文光", "authorSlug": "zhengwenguang",
        "publisher": "人民文学出版社",
        "coverCredit": "placeholder",
        "tags": ["太空", "宇宙航行", "新时期"],
        "featured": True,
        "sources": ["《飞向人马座》郑文光，人民文学出版社 1979"],
        "zh": {"title": "飞向人马座", "body": "《飞向人马座》是郑文光最重要的长篇作品之一，"
            "写作于文革结束前后，1979 年由人民文学出版社出版。"
            "它与童恩正《珊瑚岛上的死光》、叶永烈《小灵通漫游未来》"
            "共同被视为新时期科幻复苏的标志。\n\n"
            "小说叙三名少年在参观宇航基地时误入一艘即将启程的飞船，"
            "因意外被抛向人马座方向。"
            "在长达数年的星际漂流中，三人依靠船上设备自学天体物理、"
            "维持生存、观测宇宙，并最终寻得返航之路。\n\n"
            "其想象力有三点突出：一是严格按牛顿力学处理飞船的运动与轨道，"
            "使漂流过程具有可计算性；"
            "二是对相对论时间效应的运用，"
            "让地球上与飞船上的时间产生落差；"
            "三是把知识学习本身写成了求生的手段，"
            "科学在此既是内容也是情节动力。\n\n"
            "该作将硬核天文知识与少年成长叙事结合，"
            "影响深远。本站归入科幻层，列为新中国时段的代表作。"},
        "en": {"title": "Flight to Sagittarius", "body": "One of Zheng Wenguang's most important novels, written around the end of the Cultural Revolution and published by People's Literature Publishing House in 1979. With Tong Enzheng's Death Ray on a Coral Island and Ye Yonglie's Xiao Lingtong Travels to the Future, it is taken as a marker of the post-1978 revival.\n\n"
            "Three teenagers visiting a space facility blunder aboard a craft about to depart and are thrown toward Sagittarius. Across years of interstellar drift they teach themselves astrophysics from the ship's resources, keep themselves alive, observe the universe, and at last find a way home.\n\n"
            "Three features of its imagination stand out. The craft's motion and orbit are handled strictly by Newtonian mechanics, making the drift calculable; relativistic time effects open a gap between time on Earth and time aboard; and learning itself becomes the means of survival, so that science is at once subject matter and plot engine.\n\n"
            "Joining hard astronomy to a coming-of-age narrative, it has proved deeply influential. Filed as SF and placed among the representative works of the New China period."},
    },
    {
        "slug": "shanhudao",
        "era": "xinzhongguo", "kind": "sf", "year": 1978,
        "author": "童恩正", "authorSlug": "tongenzheng",
        "publisher": "人民文学出版社",
        "coverCredit": "placeholder",
        "tags": ["激光武器", "科幻复苏", "新时期"],
        "adaptations": ["shanhudao-film-1980"],
        "featured": True,
        "sources": ["《人民文学》1978 年第 5 期"],
        "zh": {"title": "珊瑚岛上的死光", "body": "《珊瑚岛上的死光》发表于《人民文学》1978 年第 5 期，"
            "是童恩正最重要的短篇作品，"
            "也被普遍视为新时期科幻复苏的标志性文本之一。"
            "该刊发表科幻小说本身，即具有强烈的信号意义。\n\n"
            "小说叙爱国科学家赵教授在海外研制出高效激光装置，"
            "境外势力企图夺取这项技术用于军事目的，"
            "赵教授与助手在孤岛上与之周旋，"
            "最终以死光装置挫败阴谋，自己却不幸牺牲。\n\n"
            "其想象力集中于激光武器这一具体技术设想。"
            "作品对装置的功率、射程与杀伤效果有明确描述，"
            "虽带有当时技术条件下的夸大，"
            "但设定自洽、应用场景完整，"
            "属典型的「技术核心型」科幻。\n\n"
            "1980 年该作被改编为中国第一部科幻题材电影，"
            "进一步扩大了影响。"
            "本站归入科幻层，并关联其影视改编条目。"},
        "en": {"title": "Death Ray on a Coral Island", "body": "Published in the fifth issue of People's Literature in 1978, this is Tong Enzheng's most important short story and is widely regarded as one of the signature texts of the post-1978 revival — the appearance of science fiction in that journal was itself a signal.\n\n"
            "The patriotic scientist Professor Zhao develops a high-efficiency laser device abroad; foreign interests try to seize the technology for military use; Zhao and his assistant hold out against them on an isolated island and at last defeat the plot with the device, though Zhao himself is killed.\n\n"
            "Its imagination concentrates on the single technological premise of the laser weapon. The apparatus is described in terms of power, range and effect, exaggerated by the standards of its day yet internally consistent and fully situated — a typical example of premise-centred science fiction.\n\n"
            "Filmed in 1980 as China's first science fiction feature, its reach widened further. Filed as SF, with a link to its screen adaptation."},
    },
    {
        "slug": "xueshan-modi",
        "era": "xinzhongguo", "kind": "sf", "year": 1978,
        "author": "童恩正", "authorSlug": "tongenzheng",
        "publisher": None,
        "coverCredit": "placeholder",
        "tags": ["考古", "雪山", "神秘"],
        "sources": ["《雪山魔笛》童恩正，1978"],
        "zh": {"title": "雪山魔笛", "body": "《雪山魔笛》是童恩正 1978 年前后发表的短篇佳作，"
            "与其《古峡迷雾》同属「考古科幻」一路。"
            "作者把田野考古的工作方式、青藏高原的自然环境"
            "与一个古老的传说交织在一起。\n\n"
            "小说叙一支考察队在雪山深处发现遗迹与一支来历不明的笛，"
            "笛声在特定气象与地形条件下被反复触发，"
            "队员们循声追索，"
            "最终以声学与地质的证据给出解释。\n\n"
            "其想象力在于把超自然的现象还原为自然机制："
            "风、冰、岩壁的共振被解释为「魔笛」的物质基础。"
            "这种「以科学解释神秘」的结构，"
            "是童恩正作品中最具方法论自觉的部分。\n\n"
            "该作篇幅不长而氛围完整，"
            "是其短篇中的上乘之作。"
            "本站归入科幻层。"},
        "en": {"title": "The Magic Flute of the Snow Mountain", "body": "A fine short story by Tong Enzheng published around 1978, belonging with Mist in the Ancient Gorge to his line of archaeological science fiction. It weaves together the working methods of field archaeology, the natural environment of the Tibetan plateau, and an ancient legend.\n\n"
            "An expedition discovers a ruin deep in the snow mountains and a flute of unknown origin; under particular weather and terrain the flute's sound is repeatedly triggered, and the team, following it, at last accounts for the phenomenon with acoustic and geological evidence.\n\n"
            "Its imagination lies in reducing the supernatural to a natural mechanism: wind, ice and rock resonance are shown to be the material basis of the magic flute. This structure of explaining mystery by science is the most methodologically self-aware part of Tong's work.\n\n"
            "Brief yet complete in atmosphere, it is among his best short pieces. Filed as SF."},
    },
    {
        "slug": "xiaolingtong",
        "era": "xinzhongguo", "kind": "sf", "year": 1978,
        "author": "叶永烈", "authorSlug": "yeyonglie",
        "publisher": "少年儿童出版社",
        "coverCredit": "placeholder",
        "tags": ["儿童科幻", "未来", "科普"],
        "featured": True,
        "sources": ["《小灵通漫游未来》叶永烈，少年儿童出版社 1978"],
        "zh": {"title": "小灵通漫游未来", "body": "《小灵通漫游未来》是叶永烈 1978 年出版的儿童科幻小说，"
            "由少年儿童出版社发行。"
            "全书以小记者「小灵通」误入未来市为线索，"
            "是当代中国发行量最大的科幻作品之一，"
            "影响跨越数代读者。\n\n"
            "在未来市，小灵通见识了飘行车（可在路面低空飘行的车辆）、"
            "家用机器人、人造器官、可降解塑料餐具、"
            "环幕电影、无土栽培的「农厂」，"
            "以及能治疗癌症的药物。"
            "全书以参观记的形式串联，"
            "每项新事物都配有原理说明。\n\n"
            "其想象力是一种系统性的生活改造想象："
            "它不追求单一技术的奇观，"
            "而是把交通、饮食、医疗、农业、娱乐一并重写，"
            "构成一幅完整的技术乐观主义图景。"
            "书中若干设想——如可降解餐具、无土栽培——"
            "在日后逐步成为现实。\n\n"
            "该作是理解八十年代中国技术想象的关键文本。"
            "本站归入科幻层。"},
        "en": {"title": "Xiao Lingtong Travels to the Future", "body": "Published by the China Children's Press in 1978, this children's science fiction novel follows the boy reporter Xiao Lingtong, who blunders into Future City. It is among the best-selling Chinese science fiction books ever and has reached readers across several generations.\n\n"
            "In Future City he encounters hovercars that glide just above the road, domestic robots, artificial organs, degradable plastic tableware, circular-screen cinema, soilless 'farms', and medicines that cure cancer. The book is strung together as a series of visits, each new thing supplied with an explanation of how it works.\n\n"
            "Its imagination is a systematic reimagining of daily life: rather than pursuing a single technological marvel, it rewrites transport, food, medicine, agriculture and entertainment together, producing a complete picture of technological optimism. Several of its ideas — degradable tableware, soilless cultivation — have since come to pass.\n\n"
            "It is a key text for understanding Chinese technological imagination in the 1980s. Filed as SF."},
    },
    {
        "slug": "dayang-shenchu",
        "era": "xinzhongguo", "kind": "sf", "year": 1979,
        "author": "郑文光", "authorSlug": "zhengwenguang",
        "publisher": None,
        "coverCredit": "placeholder",
        "tags": ["海洋", "探险"],
        "sources": ["《大洋深处》郑文光，1979"],
        "zh": {"title": "大洋深处", "body": "《大洋深处》是郑文光 1979 年前后发表的海洋题材科幻小说。"
            "在郑文光的创作序列中，"
            "太空与海洋构成两条并行的探索路线，"
            "本书属于后者。\n\n"
            "小说叙一支深海考察队在远洋执行任务，"
            "在极端环境中遭遇一系列异常现象与生物，"
            "最终取得重要发现。"
            "叙事延续了作者一贯的风格："
            "以具体的技术细节支撑探险过程。\n\n"
            "其想象力集中在深海这一特殊空间：高压、无光、"
            "生物形态陌生，"
            "本身就构成一个天然的异质世界。"
            "作品对深潜设备、照明与通信的描写，"
            "显示了作者对海洋科学的熟悉。\n\n"
            "该作是其题材拓展的一环，"
            "也反映了七十年代末中国科幻"
            "对多元探索空间的兴趣。"
            "本站归入科幻层。"},
        "en": {"title": "In the Depths of the Ocean", "body": "An oceanic science fiction novel by Zheng Wenguang published around 1979. In Zheng's work, space and the sea form two parallel lines of exploration; this book belongs to the latter.\n\n"
            "A deep-sea expedition on an ocean mission meets a series of anomalies and organisms in extreme conditions and at last makes an important discovery. The narrative continues the author's customary manner, supporting the course of exploration with concrete technical detail.\n\n"
            "Its imagination concentrates on the deep sea as a special space: high pressure, no light, unfamiliar life forms, already a naturally heterogeneous world. Its descriptions of submersible equipment, lighting and communication show a writer at home with marine science.\n\n"
            "Part of the widening of his subject matter, it also reflects the interest of Chinese science fiction in the late 1970s in varied spaces of exploration. Filed as SF."},
    },
    {
        "slug": "shayu-zhenchabing",
        "era": "xinzhongguo", "kind": "sf", "year": 1979,
        "author": "郑文光", "authorSlug": "zhengwenguang",
        "publisher": None,
        "coverCredit": "placeholder",
        "tags": ["动物", "军事", "海洋"],
        "sources": ["《鲨鱼侦察兵》郑文光，1979"],
        "zh": {"title": "鲨鱼侦察兵", "body": "《鲨鱼侦察兵》是郑文光 1979 年前后发表的短篇科幻，"
            "也是其流传较广的作品之一。"
            "该作延续了作者对生物学前沿的关注，"
            "把动物行为学与军事技术设想结合在一起。\n\n"
            "小说设想通过某种技术手段控制鲨鱼的行为，"
            "使其成为可操控的侦察工具。"
            "故事围绕这一设想展开：从实验、调试到实际运用，"
            "并涉及由此带来的伦理与安全问题。\n\n"
            "其想象力属于典型的「技术装置型」："
            "先提出一个清晰的机制设想，"
            "再推演它在具体场景中的运作方式与副作用。"
            "这种写法与凡尔纳式的科学推演一脉相承，"
            "也体现了郑文光以生物学见长的特色。\n\n"
            "该作篇幅短小、构思完整，"
            "是其短篇中的代表作。"
            "本站归入科幻层。"},
        "en": {"title": "The Shark Scout", "body": "A short story by Zheng Wenguang published around 1979 and among his more widely circulated works. It continues his attention to the frontier of biology, joining animal behaviour to a military-technical premise.\n\n"
            "The story imagines a means of controlling shark behaviour so that the animals become steerable reconnaissance tools, and follows the idea through experiment, calibration and deployment, together with the ethical and safety questions that follow.\n\n"
            "Its imagination is typically mechanistic: a clear mechanism is proposed, then its operation and side effects are extrapolated in concrete scenes. This descends from Vernean scientific extrapolation and shows Zheng's characteristic strength in biology.\n\n"
            "Brief and complete in conception, it is representative of his short fiction. Filed as SF."},
    },
    {
        "slug": "feixiang-mingwangxing",
        "era": "xinzhongguo", "kind": "sf", "year": 1979,
        "author": "叶永烈", "authorSlug": "yeyonglie",
        "publisher": None,
        "coverCredit": "placeholder",
        "tags": ["太空", "冥王星", "探险"],
        "sources": ["《飞向冥王星的人》叶永烈，1979"],
        "zh": {"title": "飞向冥王星的人", "body": "《飞向冥王星的人》是叶永烈 1979 年前后发表的太空题材作品，"
            "属于其科普式科幻创作的一支，"
            "与《小灵通漫游未来》同一时期。\n\n"
            "小说叙人类探测器或载人飞船飞往太阳系边缘的冥王星，"
            "在漫长航程与极端低温中完成考察任务。"
            "作品按航程分段推进，"
            "沿途依次介绍太阳系各天体的知识。\n\n"
            "其想象力以「距离」为核心："
            "冥王星作为当时已知太阳系最远的行星，"
            "天然带有边疆意味。"
            "作品把航行本身写成一个知识展开的过程，"
            "体现了科普型科幻的典型结构——"
            "以旅程为线索串联科学内容。\n\n"
            "该作在叶永烈的创作中属太空题材的重要一篇。"
            "本站归入科幻层。"},
        "en": {"title": "The Man Who Flew to Pluto", "body": "A space-themed work by Ye Yonglie published around 1979, belonging to his line of popular-science science fiction and contemporaneous with Xiao Lingtong Travels to the Future.\n\n"
            "It follows a probe or crewed craft to Pluto at the edge of the solar system, completing its survey across a long voyage and extreme cold. The narrative advances by stages of the journey, introducing the bodies of the solar system as it goes.\n\n"
            "Its imagination centres on distance: Pluto, then the farthest known planet, carries a natural frontier meaning. The voyage itself becomes the process by which knowledge unfolds, exemplifying the structure of popular-science science fiction — a journey used as the thread on which scientific content is strung.\n\n"
            "An important item among Ye's space-themed works. Filed as SF."},
    },
    {
        "slug": "shenyi",
        "era": "xinzhongguo", "kind": "sf", "year": 1982,
        "author": "郑文光", "authorSlug": "zhengwenguang",
        "publisher": None,
        "coverCredit": "placeholder",
        "tags": ["儿童科幻", "飞行", "科学"],
        "sources": ["《神翼》郑文光，1982"],
        "zh": {"title": "神翼", "body": "《神翼》是郑文光 1982 年出版的儿童科幻长篇，"
            "也是他后期最重要的作品之一，"
            "曾获中国作协全国优秀儿童文学奖。\n\n"
            "小说叙少年获得一副可使人飞行的「神翼」，"
            "由此展开一连串冒险。"
            "作品把飞行这一古老的人类梦想，"
            "置于具体的科学框架下加以处理："
            "翼的结构、升力来源、操纵方式都有交代。\n\n"
            "其想象力把神话与科学接在了一起。"
            "「神翼」在名称上呼应远古的羽人传说，"
            "在机制上却是一部可分析的机械装置——"
            "这种双重性正是前科幻向科幻过渡的典型形态。\n\n"
            "全书以飞行串联科学原理与成长主题，"
            "是其最受欢迎的儿童科幻之一。"
            "本站归入科幻层。"},
        "en": {"title": "The Divine Wings", "body": "A children's science fiction novel by Zheng Wenguang published in 1982, among his most important later works and a winner of the Chinese Writers Association's national award for children's literature.\n\n"
            "A boy obtains a pair of 'divine wings' that enable human flight, and a series of adventures follows. The ancient dream of flying is placed inside a concrete scientific frame: the structure of the wings, the source of lift, and the method of control are all accounted for.\n\n"
            "Its imagination joins myth to science. The wings answer in name to the ancient lore of feathered men, yet in mechanism are an analysable machine — a duality typical of the passage from proto-SF to science fiction.\n\n"
            "Linking scientific principle to the theme of growing up through flight, it is among his most popular works for young readers. Filed as SF."},
    },
    {
        "slug": "meng",
        "era": "xinzhongguo", "kind": "sf", "year": 1979,
        "author": "萧建亨", "authorSlug": "xiaojianheng",
        "publisher": None,
        "coverCredit": "placeholder",
        "tags": ["梦境", "心理学", "科学"],
        "sources": ["《梦》萧建亨，1979"],
        "zh": {"title": "梦", "body": "《梦》是萧建亨 1979 年前后发表的代表性短篇，"
            "围绕梦境与意识的科学假说展开。"
            "在七十年代末的中国科幻中，"
            "以心理学与神经科学为题材的作品相当少见。\n\n"
            "小说设想通过技术手段记录、"
            "干预甚至共享梦境，"
            "由此引发对意识边界与隐私的追问。"
            "作品在科普的框架内推进情节，"
            "保持了萧建亨一贯的平实风格。\n\n"
            "其想象力集中在对内在空间的开掘。"
            "与同时期主流的太空、海洋题材不同，"
            "《梦》把探索的方向指向人的意识本身，"
            "这与后来赛博朋克对精神空间的关注遥相呼应。\n\n"
            "该作是新时期科幻多元探索的一例，"
            "显示了题材上的开阔度。"
            "本站归入科幻层。"},
        "en": {"title": "Dream", "body": "A representative short story by Xiao Jianheng published around 1979, built on scientific hypotheses about dreams and consciousness. In Chinese science fiction of the late 1970s, work taking psychology and neuroscience as its subject was rare.\n\n"
            "The story imagines recording, intervening in and even sharing dreams by technical means, raising questions about the limits of consciousness and about privacy. It advances within a popular-science frame, keeping the plainness customary to Xiao.\n\n"
            "Its imagination opens up inner space. Unlike the period's dominant space and ocean themes, Dream turns exploration toward consciousness itself, anticipating later cyberpunk attention to mental space.\n\n"
            "An example of the pluralism of the revival years, showing range in subject matter. Filed as SF."},
    },
    # ============================================================== 当代 · 星河
    {
        "slug": "juedou-zai-wangluo",
        "era": "dangdai", "kind": "sf", "year": 1996,
        "author": "星河", "authorSlug": "xinghe",
        "publisher": None,
        "coverCredit": "placeholder",
        "tags": ["网络", "赛博", "1990年代"],
        "featured": True,
        "sources": ["《决斗在网络》星河，1996"],
        "zh": {"title": "决斗在网络", "body": "《决斗在网络》是星河发表于 1996 年的成名作，"
            "也是中国最早以计算机网络为核心场景的科幻小说之一。"
            "其时互联网刚进入中国不久，"
            "作品几乎与这一技术同步出现。\n\n"
            "小说叙网络空间中一场看不见对手的对抗："
            "主人公在虚拟空间中遭遇不明身份的对手，"
            "双方以技术手段相互追踪、伪装与攻击，"
            "而身份本身成为最大的谜题。\n\n"
            "其想象力集中在两处：一是把网络写成一个有空间感、"
            "可进入的场域，"
            "这在此前的中国科幻中极为罕见；"
            "二是对虚拟身份的追问——"
            "当双方都可用假面，究竟谁在与谁决斗。\n\n"
            "该作标志着九十年代中国科幻对新技术的直接回应，"
            "也让星河成为当时最重要的青年科幻作家之一。"
            "本站归入科幻层。"},
        "en": {"title": "Duel on the Network", "body": "Xinghe's breakthrough work, published in 1996 and among the earliest Chinese science fiction stories built around computer networks; the internet had only just reached China, and the story appeared almost simultaneously with the technology.\n\n"
            "It follows an unseen contest in network space: the protagonist meets an adversary of unknown identity, the two tracking, disguising themselves and attacking one another by technical means, with identity itself becoming the central riddle.\n\n"
            "Its imagination gathers in two places. The network is written as a place with spatial quality that can be entered, rare in Chinese science fiction before this; and virtual identity is interrogated — when both sides may wear masks, who is duelling whom.\n\n"
            "It marks the direct response of 1990s Chinese science fiction to new technology and established Xinghe among the most important younger SF writers of the day. Filed as SF."},
    },
    {
        "slug": "canque-de-cihen",
        "era": "dangdai", "kind": "sf", "year": 1997,
        "author": "星河", "authorSlug": "xinghe",
        "publisher": None,
        "coverCredit": "placeholder",
        "tags": ["考古", "磁场", "悬疑"],
        "sources": ["《残缺的磁痕》星河，1997"],
        "zh": {"title": "残缺的磁痕", "body": "《残缺的磁痕》是星河 1997 年前后发表的短篇代表作，"
            "以一次考古发掘中的异常磁痕为线索。"
            "作品融合了科学考察程序与悬疑叙事，"
            "体现了他所谓的「硬派推理」风格。\n\n"
            "小说叙考察队在遗址中发现无法用常规方式解释的磁记录，"
            "其信息残缺不全。"
            "队员们通过反复采样、比对与推理，"
            "逐步还原出一段被部分抹去的历史。\n\n"
            "其想象力在于把「信息的不完整」本身设为谜题的核心："
            "问题不是信息太多而是太少，"
            "因此情节推动力来自证据的拼合而非发现。"
            "磁痕作为一种记录介质，"
            "也暗示了信息可以脱离载体长期留存。\n\n"
            "该作是星河短篇中结构与设定结合最紧密的作品之一。"
            "本站归入科幻层。"},
        "en": {"title": "The Incomplete Magnetic Trace", "body": "A representative short story by Xinghe published around 1997, turning on an anomalous magnetic trace found at an excavation. It combines the procedures of scientific fieldwork with suspense narrative, exemplifying what he calls hard deduction.\n\n"
            "A survey team finds magnetic records at a site that cannot be explained in ordinary terms, and the information is incomplete. Through repeated sampling, comparison and inference, the team gradually reconstructs a partly erased history.\n\n"
            "Its imagination makes incompleteness itself the heart of the puzzle: the difficulty is not too much information but too little, so the plot is driven by the piecing together of evidence rather than by discovery. The magnetic trace as a recording medium also implies that information can outlast its carrier.\n\n"
            "Among the works in which Xinghe's structure and premise are most tightly joined. Filed as SF."},
    },
    {
        "slug": "shikong-sijie",
        "era": "dangdai", "kind": "sf", "year": 1999,
        "author": "星河", "authorSlug": "xinghe",
        "publisher": None,
        "coverCredit": "placeholder",
        "tags": ["时间旅行", "悖论", "物理学"],
        "sources": ["《时空死结》星河，1999"],
        "zh": {"title": "时空死结", "body": "《时空死结》是星河 1999 年出版的长篇，"
            "围绕时间旅行所引发的因果悖论展开，"
            "是其硬科幻实力的代表之作。\n\n"
            "小说设定在一次时间实验之后：主人公回到过去，"
            "却发现自己的每一次干预都会制造新的矛盾，"
            "种种因果纠缠成一个无法解开的死结。"
            "作品据此推演多条时间线彼此冲突的后果。\n\n"
            "其想象力在于对悖论的严肃处理。"
            "作品不满足于把时间旅行当作便利的情节装置，"
            "而是以物理设定为前提，"
            "认真推演自洽性被破坏时会发生什么，"
            "并尝试给出解结的方案。\n\n"
            "在中国科幻中，以硬派方式处理时间悖论的作品并不多见。"
            "本站归入科幻层，将其视为九十年代硬科幻的重要收获。"},
        "en": {"title": "Deadlock in Spacetime", "body": "A novel published by Xinghe in 1999, built on the causal paradoxes created by time travel and representative of his hard-SF strength.\n\n"
            "After a temporal experiment the protagonist returns to the past only to find that each intervention produces a fresh contradiction, the causes and effects tangling into a knot that cannot be undone. From this premise the novel extrapolates the consequences of conflicting timelines.\n\n"
            "Its imagination lies in taking the paradox seriously. Rather than using time travel as a convenient plot device, it takes its physical premise as given and works out what happens when self-consistency breaks down, attempting a solution to the knot.\n\n"
            "Hard treatments of temporal paradox are uncommon in Chinese science fiction. Filed as SF, as a significant achievement of 1990s hard science fiction."},
    },
    {
        "slug": "chaoxiao-ruqiang",
        "era": "dangdai", "kind": "sf", "year": 2001,
        "author": "星河", "authorSlug": "xinghe",
        "publisher": None,
        "coverCredit": "placeholder",
        "tags": ["环境", "灾难", "海洋"],
        "sources": ["《潮啸如枪》星河，2001"],
        "zh": {"title": "潮啸如枪", "body": "《潮啸如枪》是星河 2001 年前后发表的灾难题材长篇，"
            "以海啸威胁为背景。"
            "作品延续了星河对技术与社会的持续关注，"
            "把焦点从虚拟空间转向现实的环境危机。\n\n"
            "小说叙一次由地质活动引发的特大海啸即将袭击沿岸城市，"
            "科学家、政府与民众在有限时间内做出各自的反应。"
            "叙事在预警、疏散与灾变之间反复切换，"
            "形成强烈的节奏感。\n\n"
            "其想象力属于「近未来现实型」："
            "作品不依赖遥远未来或外星设定，"
            "而是把已知的自然灾害推至极端规模，"
            "考察社会系统的应对能力。"
            "这种写法使科幻成为对现实治理的一次压力测试。\n\n"
            "该作体现了九十年代末以来中国科幻"
            "从技术奇观向社会议题的重心转移。"
            "本站归入科幻层。"},
        "en": {"title": "Tidal Roar Like Spears", "body": "A disaster novel by Xinghe published around 2001, set under the threat of a tsunami. Continuing his concern with technology and society, it turns the focus from virtual space to real environmental crisis.\n\n"
            "A great tsunami set off by geological activity bears down on coastal cities; scientists, government and citizens respond within a narrowing window. The narrative cuts repeatedly between warning, evacuation and catastrophe, producing a strong rhythm.\n\n"
            "Its imagination is of the near-future realist kind: rather than distant futures or alien settings, it takes a known natural disaster and scales it to extremes in order to test the response capacity of social systems. Science fiction here becomes a stress test of governance.\n\n"
            "The work reflects the shift in Chinese science fiction from the late 1990s onward away from technological marvel and toward social questions. Filed as SF."},
    },
    # ============================================================ 当代 · 王晋康
    {
        "slug": "shengming-zhige",
        "era": "dangdai", "kind": "sf", "year": 1997,
        "author": "王晋康", "authorSlug": "wangjinkang",
        "publisher": None,
        "coverCredit": "placeholder",
        "tags": ["基因", "伦理", "银河奖"],
        "featured": True,
        "sources": ["《生命之歌》王晋康，1997"],
        "zh": {"title": "生命之歌", "body": "《生命之歌》是王晋康发表于 1997 年的代表作，"
            "曾获中国科幻银河奖。"
            "王晋康出身工程师，"
            "其作品以硬核技术设想与伦理思辨并重著称，"
            "此篇是这一风格的集中体现。\n\n"
            "小说叙一位生物学家以基因技术大幅提升黑猩猩的智力，"
            "使其接近人类水平。"
            "这一成果随即引发连锁危机："
            "被造物开始主张自身的权利，"
            "而创造者也必须在亲情、伦理与科学责任之间做出选择。\n\n"
            "其想象力紧扣基因工程这一具体技术，"
            "推演的是可预见的近未来而非遥远幻想。"
            "作品真正的锋芒在于伦理："
            "当技术可以改变一个物种的心智，"
            "「人」的边界在哪里？\n\n"
            "该作是中国科幻伦理叙事的重要文本，"
            "也是王晋康最广为人知的作品之一。"
            "本站归入科幻层。"},
        "en": {"title": "Song of Life", "body": "Wang Jinkang's signature work, published in 1997 and winner of the Chinese Science Fiction Galaxy Award. Trained as an engineer, Wang is known for pairing hard technical premises with ethical inquiry, and this story concentrates that manner.\n\n"
            "A biologist raises the intelligence of a chimpanzee by genetic means to near-human level. The achievement sets off a chain of crises: the creature begins to claim its own rights, and its creator must choose between familial feeling, ethics and scientific responsibility.\n\n"
            "Its imagination holds closely to the concrete technology of genetic engineering, extrapolating a foreseeable near future rather than a distant fancy. Its real edge is ethical: when technique can alter the mind of a species, where does the human boundary lie?\n\n"
            "An important text of ethical science fiction in China and among Wang's best-known works. Filed as SF."},
    },
    {
        "slug": "qichong-waike",
        "era": "dangdai", "kind": "sf", "year": 1997,
        "author": "王晋康", "authorSlug": "wangjinkang",
        "publisher": None,
        "coverCredit": "placeholder",
        "tags": ["虚拟现实", "身份", "银河奖"],
        "featured": True,
        "sources": ["《七重外壳》王晋康，1997"],
        "zh": {"title": "七重外壳", "body": "《七重外壳》是王晋康 1997 年前后发表的代表作，"
            "与《生命之歌》同为其最重要的短篇之一。"
            "作品以虚拟现实技术为装置，"
            "展开一场关于真实与感知的哲学追问。\n\n"
            "小说设定主人公进入一套可嵌套的虚拟环境，"
            "每一层都仿真得足以乱真，"
            "要判断自己是否还在真实世界，"
            "就必须逐层剥离。"
            "「外壳」一词既指虚拟层，也指人的感官局限。\n\n"
            "其想象力把「缸中之脑」这一经典命题"
            "转化为可操作的叙事结构："
            "七层嵌套既是情节推进机制，"
            "也是对感知可靠性的逐级怀疑。\n\n"
            "该作在中文科幻中较早系统处理虚拟现实议题，"
            "其影响在此后众多作品中可见。"
            "本站归入科幻层。"},
        "en": {"title": "Seven-Layer Shell", "body": "A signature work by Wang Jinkang published around 1997, alongside Song of Life among his most important short fiction. Using virtual reality as its apparatus, it opens a philosophical enquiry into reality and perception.\n\n"
            "The protagonist enters a nested virtual environment whose every layer is convincing enough to pass for the real; to know whether he remains in the actual world he must peel away the layers one by one. The word shell names both the virtual stratum and the limits of the senses.\n\n"
            "Its imagination converts the classic brain-in-a-vat problem into a workable narrative structure: the seven layers are at once a plot mechanism and a graduated doubt about the reliability of perception.\n\n"
            "Among the earliest systematic treatments of virtual reality in Chinese science fiction, its influence can be traced through much later work. Filed as SF."},
    },
    {
        "slug": "leiren",
        "era": "dangdai", "kind": "sf", "year": 2000,
        "author": "王晋康", "authorSlug": "wangjinkang",
        "publisher": None,
        "coverCredit": "placeholder",
        "tags": ["克隆", "伦理", "社会"],
        "sources": ["《类人》王晋康，2000"],
        "zh": {"title": "类人", "body": "《类人》是王晋康 2000 年前后出版的长篇，"
            "设想克隆人技术成熟之后的社会秩序。"
            "作品延续了作者对生物技术伦理的一贯关注，"
            "但把讨论从个体层面推进到了制度层面。\n\n"
            "小说设定在一个克隆人已成为产业的时代："
            "类人被大规模制造，用于劳动、器官供给与特定服务，"
            "法律与伦理为此发展出一整套分类与管理规则。"
            "主人公在这一秩序中逐渐发现其内在的矛盾与残酷。\n\n"
            "其想象力在于制度设计："
            "作品详细构想了类人的法律地位、"
            "身份识别方式（如人工瓣膜）、"
            "以及社会如何为歧视提供合理化论证。"
            "这种「社会推演」是王晋康区别于其他作家的重要特征。\n\n"
            "该作是中文科幻中处理克隆议题最系统的作品之一。"
            "本站归入科幻层。"},
        "en": {"title": "Human Clones", "body": "A novel by Wang Jinkang published around 2000, imagining a social order in which human cloning has matured into an industry. Continuing the author's concern with the ethics of biotechnology, it moves the discussion from the individual to the institutional level.\n\n"
            "It is set in an age when clones are manufactured at scale for labour, for organs and for particular services, and when law and ethics have evolved a whole apparatus of classification and management. The protagonist gradually discovers the contradictions and cruelties inside that order.\n\n"
            "Its imagination lies in institutional design: the legal standing of clones, the means of identifying them, and the ways a society rationalises discrimination are all worked out in detail. This social extrapolation is what distinguishes Wang from other writers.\n\n"
            "Among the most systematic treatments of cloning in Chinese science fiction. Filed as SF."},
    },
    {
        "slug": "yisheng",
        "era": "dangdai", "kind": "sf", "year": 2002,
        "author": "王晋康", "authorSlug": "wangjinkang",
        "publisher": None,
        "coverCredit": "placeholder",
        "tags": ["社会", "群体", "寓言"],
        "sources": ["《蚁生》王晋康，2002"],
        "zh": {"title": "蚁生", "body": "《蚁生》是王晋康 2002 年前后出版的长篇，"
            "以蚂蚁社会的信息素机制为支点，"
            "构想一种全新的人类组织方式。"
            "这是一部典型的「社会实验型」科幻。\n\n"
            "小说设定有人发现可通过信息素调节人的社会行为，"
            "据此建立了一个高度协作、"
            "几乎没有冲突的小型社会。"
            "这一秩序高效而稳定，"
            "代价则是个体意志的消失。\n\n"
            "其想象力以生物学设定为杠杆，"
            "撬动的是政治哲学问题："
            "集体效率与个体自由能否两全？"
            "作品并未简单给出答案，"
            "而是通过叙事让两种价值彼此对质。\n\n"
            "该作体现了王晋康「以技术设定讨论社会制度」"
            "的一贯路径。"
            "本站归入科幻层。"},
        "en": {"title": "Ant Life", "body": "A novel by Wang Jinkang published around 2002 that uses the pheromonal order of an ant colony as the lever for imagining a new form of human organisation. It is a typical specimen of the social-experiment kind of science fiction.\n\n"
            "Someone discovers that human social behaviour can be regulated by pheromones, and on that basis builds a small society of near-perfect cooperation and almost no conflict. The order is efficient and stable, and its price is the disappearance of individual will.\n\n"
            "Its imagination uses a biological premise to lever a question of political philosophy: can collective efficiency and individual freedom both be had? The book does not answer simply, but lets the two values confront one another through the narrative.\n\n"
            "It exemplifies Wang's consistent method of discussing social institutions through a technological premise. Filed as SF."},
    },
    {
        "slug": "shuixing-bozhong",
        "era": "dangdai", "kind": "sf", "year": 2002,
        "author": "王晋康", "authorSlug": "wangjinkang",
        "publisher": None,
        "coverCredit": "placeholder",
        "tags": ["太空", "生命", "硬科幻"],
        "sources": ["《水星播种》王晋康，2002"],
        "zh": {"title": "水星播种", "body": "《水星播种》是王晋康 2002 年前后发表的短篇，"
            "写在水星这一极端环境中培育生命的设想。"
            "篇幅不长而分量很重，"
            "是其短篇中的名篇。\n\n"
            "小说叙一支考察队在靠近太阳的水星上，"
            "以特殊方式播撒并维持生命的初始形态。"
            "任务周期极长，跨越数代人，"
            "参与者必须接受自己看不到结果的命运。\n\n"
            "其想象力有两层：一是技术层面的"
            "极端环境生命维持方案；"
            "二是时间尺度上的牺牲——"
            "把一项事业交给自己无法见证的未来，"
            "这为硬核设定赋予了情感重量。\n\n"
            "该作是王晋康「冷技术、热处理」风格的代表："
            "设定严谨，而落点在人的选择与传承。"
            "本站归入科幻层。"},
        "en": {"title": "Sowing on Mercury", "body": "A short story by Wang Jinkang published around 2002, on the idea of cultivating life on Mercury, a planet of extremes. Brief but weighty, it is among his finest short works.\n\n"
            "A team on Mercury, close to the sun, sows and sustains the first forms of life by special means. The task runs over generations, and its participants must accept that they will never see the outcome.\n\n"
            "Its imagination works on two levels: a technical scheme for maintaining life in extreme conditions, and a sacrifice on the scale of time — handing an undertaking to a future one will not witness, which lends emotional weight to the hard premise.\n\n"
            "It represents Wang's manner of cool technique and warm treatment: rigorous in premise, landing on human choice and transmission. Filed as SF."},
    },
    {
        "slug": "taochu-muyuzhou",
        "era": "dangdai", "kind": "sf", "year": 2013,
        "author": "王晋康", "authorSlug": "wangjinkang",
        "publisher": None,
        "coverCredit": "placeholder",
        "tags": ["宇宙学", "末日", "硬科幻"],
        "sources": ["《逃出母宇宙》王晋康，2013"],
        "zh": {"title": "逃出母宇宙", "body": "《逃出母宇宙》是王晋康 2013 年出版的长篇，"
            "写人类面对宇宙尺度灾变时的逃亡与抉择。"
            "这是其创作中规模最大、"
            "宇宙学设定最硬的作品之一。\n\n"
            "小说设定宇宙本身正在发生某种根本性的变化，"
            "物理规律面临失效。"
            "人类必须在有限时间内理解这一变化，"
            "并找到离开「母宇宙」的路径。"
            "作品同时展开了多条人物线，"
            "覆盖科学家、普通家庭与决策者。\n\n"
            "其想象力建立在当代宇宙学之上："
            "真空衰变、物理常数变化等前沿假说"
            "被直接用作情节基础。"
            "与《流浪地球》的太阳危机相比，"
            "这里的威胁更为彻底——"
            "不是家园不宜居，而是规律本身将变。\n\n"
            "该作是一部规模宏大的末日叙事，"
            "也是王晋康后期硬科幻的代表。"
            "本站归入科幻层。"},
        "en": {"title": "Escape from the Mother Universe", "body": "A novel published by Wang Jinkang in 2013, on humanity's flight and choices before a catastrophe on a cosmic scale. It is among his largest works and hardest in cosmological premise.\n\n"
            "The universe itself is undergoing some fundamental change, and physical law is failing. Humanity must understand the change within a narrowing window and find a way out of the mother universe. Several character lines run in parallel, covering scientists, ordinary families and decision-makers.\n\n"
            "Its imagination rests on contemporary cosmology: frontier hypotheses such as vacuum decay and the variation of physical constants are used directly as plot foundations. Compared with the solar crisis of The Wandering Earth, the threat here is more radical — not that the home becomes uninhabitable, but that law itself will change.\n\n"
            "An apocalyptic narrative on a grand scale and a representative work of Wang's later hard science fiction. Filed as SF."},
    },
    # ============================================================== 当代 · 韩松
    {
        "slug": "hongse-haiyang",
        "era": "dangdai", "kind": "sf", "year": 2004,
        "author": "韩松", "authorSlug": "hansong",
        "publisher": None,
        "coverCredit": "placeholder",
        "tags": ["海洋", "文明", "寓言"],
        "sources": ["《红色海洋》韩松，2004"],
        "zh": {"title": "红色海洋", "body": "《红色海洋》是韩松 2004 年出版的长篇，"
            "设定在未来人类退回海洋生存之后。"
            "这是其最具野心、"
            "也最系统的一部文明寓言。\n\n"
            "小说以数万年为跨度重写人类史："
            "陆地不再宜居，人类在海洋中演化、争战、迁徙，"
            "最终又重新回到陆地。"
            "全书由若干相对独立而彼此呼应的章节构成，"
            "时间线交错，视角多变。\n\n"
            "其想象力在于把海洋当作一个重组文明的实验场："
            "身体形态、社会组织、生死观念"
            "都在这一环境中被重新设定。"
            "作品笔调冷峻，意象密集，"
            "充满对文明循环的悲观洞察。\n\n"
            "该作是理解韩松「文明批判」一面的核心文本。"
            "本站归入科幻层。"},
        "en": {"title": "Red Ocean", "body": "A novel by Han Song published in 2004, set after humanity has returned to live in the sea. It is his most ambitious and most systematic civilisational fable.\n\n"
            "It rewrites human history across tens of thousands of years: the land is no longer habitable, humanity evolves, wars and migrates in the ocean, and at last returns to land. The book is built from chapters that stand apart yet answer one another, with crossed chronologies and shifting perspectives.\n\n"
            "Its imagination treats the ocean as an experimental field in which civilisation is reassembled: bodily form, social organisation and ideas of life and death are all reset in that environment. The register is austere, the imagery dense, and the vision of civilisation's cycles pessimistic.\n\n"
            "A core text for understanding the civilisational critique in Han Song. Filed as SF."},
    },
    {
        "slug": "2066",
        "era": "dangdai", "kind": "sf", "year": 2006,
        "author": "韩松", "authorSlug": "hansong",
        "publisher": None,
        "coverCredit": "placeholder",
        "tags": ["未来史", "荒诞", "社会批判"],
        "featured": True,
        "sources": ["《2066年之西行漫记》韩松，2006"],
        "zh": {"title": "2066年之西行漫记", "body": "《2066年之西行漫记》是韩松 2006 年出版的长篇，"
            "书名戏仿斯诺《西行漫记》，"
            "借「西行」这一母题重写未来。"
            "这是韩松最具代表性的长篇之一。\n\n"
            "小说设定在 2066 年。"
            "一名美国青年为寻访真相进入中国，"
            "所见的却是一个技术高度发达、"
            "而社会逻辑处处错位的世界："
            "灾难成为常态，机构各司其职却无法解决问题，"
            "人们在信息的洪流中以荒诞方式自救。\n\n"
            "其想象力是一种「反乌托邦的现实主义」："
            "作品几乎不依赖新奇的技术设定，"
            "而通过把现实逻辑推至极端来制造陌生感。"
            "冷峻的新闻式笔调与超现实的场景并置，"
            "构成对技术文明的系统性反讽。\n\n"
            "该作确立了韩松独有的风格标识。"
            "本站归入科幻层。"},
        "en": {"title": "2066: A Journey to the West", "body": "A novel by Han Song published in 2006, its title echoing Edgar Snow's Red Star Over China and reworking the motif of the journey west. It is among his most representative novels.\n\n"
            "Set in 2066, an American youth enters China in search of the truth and finds a country of advanced technology whose social logic is everywhere askew: catastrophe is routine, institutions function without solving anything, and people rescue themselves by absurd means amid a flood of information.\n\n"
            "Its imagination is a dystopian realism: rather than leaning on novel technological premises, it defamiliarises by pushing present-day logic to extremes. A cold reportorial register is set beside surreal scenes, forming a systematic irony aimed at technological civilisation.\n\n"
            "The book established the signature of Han Song's manner. Filed as SF."},
    },
    {
        "slug": "ditie",
        "era": "dangdai", "kind": "sf", "year": 2010,
        "author": "韩松", "authorSlug": "hansong",
        "publisher": None,
        "coverCredit": "placeholder",
        "tags": ["都市", "异化", "荒诞"],
        "featured": True,
        "sources": ["《地铁》韩松，2010"],
        "zh": {"title": "地铁", "body": "《地铁》是韩松 2010 年出版的长篇，"
            "由若干相互勾连的中短篇构成。"
            "作品以地铁这一最日常的都市空间为舞台，"
            "是韩松流传最广、"
            "也最能代表其风格的作品之一。\n\n"
            "小说中，地铁不再只是交通工具："
            "乘客在隧道中遭遇无法解释的停滞、"
            "重复与变形，车厢变成一个自有规则的世界。"
            "有人在其中消失，有人在其中衰老，"
            "也有人始终到不了目的地。\n\n"
            "其想象力属于卡夫卡式的一脉："
            "不是设想新技术，"
            "而是让熟悉的空间发生轻微的、无法纠正的偏移。"
            "恐怖感正来自这种偏移的不可解释与不可抵抗。\n\n"
            "该作把都市经验与异化主题结合，"
            "「技术中国」书写的核心文本之一。"
            "本站归入科幻层。"},
        "en": {"title": "Subway", "body": "A novel by Han Song published in 2010, composed of interlinked novellas and short stories and staged in the subway, the most everyday of urban spaces. It is among his most widely read works and the most representative of his manner.\n\n"
            "The subway ceases to be mere transport: passengers meet unexplained halts, repetitions and metamorphoses in the tunnels, and the carriage becomes a world with its own rules. Some vanish in it, some age in it, some never reach their destination.\n\n"
            "Its imagination belongs to the Kafkaesque line: not new technology, but a slight, uncorrectable displacement of a familiar space. The terror comes precisely from that displacement being both inexplicable and irresistible.\n\n"
            "Joining urban experience to the theme of alienation, it is a central text of his portrait of a technological China. Filed as SF."},
    },
    {
        "slug": "yiyuan",
        "era": "dangdai", "kind": "sf", "year": 2016,
        "author": "韩松", "authorSlug": "hansong",
        "publisher": None,
        "coverCredit": "placeholder",
        "tags": ["医疗", "身体", "异化"],
        "sources": ["《医院》韩松，2016"],
        "zh": {"title": "医院", "body": "《医院》是韩松 2016 年出版的长篇，"
            "「医疗三部曲」的开篇之作。"
            "作品以医院为舞台，"
            "把身体、疾病与医疗体系写成一部现代性寓言。\n\n"
            "小说叙主人公因小病入院，"
            "却陷入一个无法离开的医疗系统："
            "检查、诊断与治疗循环往复，"
            "病人身份被不断重新定义，"
            "而「痊愈」始终无法达成。"
            "医院在此既是机构，也是一种生存状态。\n\n"
            "其想象力集中在生命政治层面："
            "医疗技术越发达，"
            "个体对自己身体的解释权反而越少。"
            "作品以荒诞笔法推演这一悖论，"
            "冷峻而令人不安。\n\n"
            "该作延续了韩松一贯的批判锋芒，"
            "也把议题推进到身体与制度的交界处。"
            "本站归入科幻层。"},
        "en": {"title": "Hospital", "body": "A novel by Han Song published in 2016, opening his medical trilogy. Staged in a hospital, it turns the body, illness and the medical system into a fable of modernity.\n\n"
            "The protagonist is admitted for a minor complaint and becomes trapped in a medical system he cannot leave: examination, diagnosis and treatment cycle endlessly, the identity of the patient is continually redefined, and recovery is never reached. The hospital is at once an institution and a condition of existence.\n\n"
            "Its imagination concentrates on biopolitics: the more advanced medical technology becomes, the less authority the individual retains over the interpretation of his own body. The paradox is worked out in an absurd register, austere and unsettling.\n\n"
            "Continuing Han's critical edge, it pushes the question to the border of body and institution. Filed as SF."},
    },
    {
        "slug": "qumo",
        "era": "dangdai", "kind": "sf", "year": 2017,
        "author": "韩松", "authorSlug": "hansong",
        "publisher": None,
        "coverCredit": "placeholder",
        "tags": ["医疗", "现实", "荒诞"],
        "sources": ["《驱魔》韩松，2017"],
        "zh": {"title": "驱魔", "body": "《驱魔》是韩松 2017 年出版的长篇，"
            "「医疗三部曲」的第二部。"
            "作品把舞台从医院移至一艘航行中的医疗船，"
            "荒诞程度较前作更甚。\n\n"
            "小说叙病人被送上船接受治疗，"
            "而船上的治疗与审判逐渐无法区分："
            "诊断即是判决，康复即是服刑。"
            "船在大海上无目的地航行，"
            "形成了一个自我封闭的司法—医疗复合体。\n\n"
            "其想象力在于机构的自我增殖："
            "系统不再服务于任何外部目的，"
            "而以维持自身运转为唯一目标。"
            "这是韩松对现代官僚体系最尖锐的隐喻之一。\n\n"
            "该作被认为批判锋芒最盛，"
            "也最难读——"
            "其复杂性本身即是主题的一部分。"
            "本站归入科幻层。"},
        "en": {"title": "Exorcism", "body": "A novel by Han Song published in 2017, the second of his medical trilogy. It moves the stage from hospital to a hospital ship under way, and is more radically absurd than its predecessor.\n\n"
            "Patients are sent aboard for treatment, and treatment and judgement gradually become indistinguishable: diagnosis is sentencing, recovery is a term served. The ship sails without destination, forming a self-enclosed juridical-medical complex.\n\n"
            "Its imagination lies in the self-multiplication of institutions: a system that no longer serves any external end and takes the maintenance of its own operation as its sole purpose. This is among Han's sharpest metaphors for modern bureaucracy.\n\n"
            "Often judged his most critical and most difficult book — the difficulty is itself part of the subject. Filed as SF."},
    },
    {
        "slug": "wangling",
        "era": "dangdai", "kind": "sf", "year": 2019,
        "author": "韩松", "authorSlug": "hansong",
        "publisher": None,
        "coverCredit": "placeholder",
        "tags": ["死亡", "数字", "现实"],
        "sources": ["《亡灵》韩松，2019"],
        "zh": {"title": "亡灵", "body": "《亡灵》是韩松 2019 年出版的长篇，"
            "「医疗三部曲」的终章。"
            "作品以死亡为切口，"
            "追问记忆、存在与技术中介之间的关系。\n\n"
            "小说设定在一个逝者可以以数据形式存续的世界。"
            "「亡灵」既是被保存的意识，"
            "也是一种新的社会阶层："
            "他们存在却无权，"
            "被保存却不被聆听。"
            "生者与死者之间的界限由此变得模糊而可操作。\n\n"
            "其想象力延续了韩松对机构与身体的关注，"
            "但把批判推进到存在论的层面："
            "当存续本身可以被技术提供，"
            "活着意味着什么？\n\n"
            "该作是三部曲中思辨性最强的一部。"
            "本站归入科幻层。"},
        "en": {"title": "The Departed", "body": "A novel by Han Song published in 2019, concluding his medical trilogy. Taking death as its entry point, it asks after the relations between memory, existence and technological mediation.\n\n"
            "It is set in a world where the dead persist as data. The departed are at once preserved consciousness and a new social stratum: they exist but have no rights, are kept but not heard. The boundary between the living and the dead becomes blurred and operable.\n\n"
            "Its imagination continues Han's concern with institutions and the body, but pushes the critique to the ontological level: when persistence itself can be supplied by technology, what does it mean to be alive?\n\n"
            "The most speculative volume of the trilogy. Filed as SF."},
    },
]

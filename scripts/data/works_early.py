# -*- coding: utf-8 -*-
"""上古 · 神话志怪 / 前科幻 / 晚清 / 民国 作品数据（中英双语）。

中文简介 300–500 字，结构统一为四段：
① 性质与成书 ② 内容概述 ③ 想象 / 科学元素分析 ④ 文学史地位与收录理由。
写作约定：正文内不使用 ASCII 直引号，一律用「」与《》，避免截断 Python 字符串。
"""

WORKS_EARLY = [
    # ============================================================ 上古 · 神话志怪
    {
        "slug": "shanhaijing",
        "era": "shanggu",
        "kind": "myth",
        "year": None,
        "yearUncertain": True,
        "author": "佚名",
        "authorSlug": "anonymous",
        "publisher": None,
        "coverCredit": "public-domain",
        "coverSource": "https://commons.wikimedia.org/wiki/Category:Shanhaijing",
        "tags": ["神话", "志怪", "异兽", "地理"],
        "featured": True,
        "sources": ["《山海经》中华书局点校本"],
        "zh": {
            "title": "山海经",
            "body": "《山海经》是中国先秦时期的一部重要古籍，全书约三万一千字，分为《山经》五卷与《海经》十三卷，"
            "传统上认为是战国至汉代间经多人累积编次而成，作者不可考。\n\n"
            "《山经》以山川为纲，依次记载方位、道里、草木、鸟兽、矿产与祭祀仪轨；《海经》则转向海外诸国与远方异民，"
            "记录了大量形态奇特的族类与国度。夸父逐日、精卫填海、大禹治水、后羿射日等神话，"
            "构成了中国神话体系最核心的一批文本。\n\n"
            "它并非单纯的幻想汇编。书中保留了对地理、物产、医药的观察与分类，关于矿物、药物与疾病的记述"
            "具有早期博物学的性质；那些「其状如禺而白耳」式的描述，体现的是以已知推未知的认知策略。\n\n"
            "从想象文学的角度看，《山海经》确立了中国志怪传统的基本范式：以地理志的冷静笔法书写不可能之物。"
            "后世《神异经》《十洲记》《博物志》乃至《镜花缘》中的海外奇国，都可追溯到这一源头。"
            "本站将其归入神话源流层——它提供的是想象世界的原型素材，而非科学框架下的推演。",
        },
        "en": {
            "title": "Classic of Mountains and Seas",
            "body": "A foundational pre-Qin compendium of some thirty-one thousand characters, divided into the five chapters of the Classic of Mountains and thirteen of the Classic of Seas, accreted by many hands between the Warring States and Han periods, with no attributable author.\n\n"
            "The Classic of Mountains proceeds by ranges and watercourses, recording directions, distances, flora, fauna, minerals and sacrificial practice; the Classic of Seas turns outward to overseas realms and distant peoples of strange form. Its myths of Kuafu chasing the sun, Jingwei filling the sea, Yu taming the flood and Houyi shooting the suns form the core canon of Chinese mythology.\n\n"
            "Yet it is not pure fantasy. It preserves early observation and classification of geography, products and medicine, and its notices of minerals, drugs and illness have the character of proto-natural history. Its formulaic descriptions model a strategy of knowing the unknown by analogy with the known.\n\n"
            "For imaginative literature it established the basic pattern of the Chinese marvel tradition: impossible things written in the sober register of a gazetteer. Later works from the Classic of Divine Marvels to Flowers in the Mirror descend from this source. This archive files it under Myth, since it supplies the raw material of imagined worlds rather than extrapolation within a scientific framework.",
        },
    },
    {
        "slug": "mutianzizhuan",
        "era": "shanggu",
        "kind": "myth",
        "year": None,
        "yearUncertain": True,
        "author": "佚名",
        "authorSlug": "anonymous",
        "publisher": None,
        "coverCredit": "public-domain",
        "tags": ["神话", "周穆王", "西行"],
        "sources": ["《穆天子传》晋代汲冢出土，郭璞注"],
        "zh": {
            "title": "穆天子传",
            "body": "《穆天子传》又称《周王游行记》，西晋太康年间从汲郡古墓出土，与《竹书纪年》同批面世，"
            "是少数未经汉人整理的先秦古书之一，成书年代一般定在战国。\n\n"
            "全书六卷，记周穆王驾八骏西征之事：自宗周出发，北渡黄河，经犬戎、西行至昆仑，"
            "与西王母宴饮酬答，复继续北行，行程数以万里计。书中穿插大量献贡、祭祀与赏赐的仪节记录，"
            "保留了西周礼制的若干细节。\n\n"
            "它的想象力集中在「远行」这一母题上。穆王所至之处多为人迹罕至的流沙、瑶池、悬圃，"
            "其八骏日行万里、越山涉水的描写，构成了一种以速度克服空间的早期想象。"
            "西王母的形象在此也由半人半兽逐渐转向雍容的王者。\n\n"
            "在文学史上，《穆天子传》上承《山海经》的异域想象，下启《神异经》《十洲记》的仙境地理，"
            "并为后世西行题材提供了原型框架。本站将其归入神话源流层：书中对空间与速度的处理，"
            "是后来一切远行与飞行想象的雏形。",
        },
        "en": {
            "title": "Tale of King Mu",
            "body": "Also known as the Travels of King Zhou, this text was recovered from a tomb at Ji commandery during the Taikang era of the Western Jin, in the same cache as the Bamboo Annals. It is one of the few pre-Qin books to reach us without Han editorial mediation, and is generally dated to the Warring States period.\n\n"
            "In six chapters it records King Mu's western campaign with his eight steeds: setting out from the royal capital, crossing the Yellow River northward, passing the Quanrong and reaching Mount Kunlun, where he feasts and exchanges verses with the Queen Mother of the West, before continuing north over a course reckoned in tens of thousands of li. Ceremonial details of tribute, sacrifice and reward run throughout, preserving particulars of Western Zhou ritual.\n\n"
            "Its imagination gathers around the motif of far travel. The king reaches quicksands, jade pools and hanging gardens beyond human reach; his steeds cover ten thousand li a day, an early imagining of speed overcoming space. The Queen Mother also shifts here from a semi-bestial figure toward a sovereign of composure.\n\n"
            "Taking up the exotic geography of the Classic of Mountains and Seas and handing it on to the paradise geography of later works, it supplied a prototype for the journey to the west. This archive files it under Myth: its handling of space and speed is the germ of all later travel and flight imaginings.",
        },
    },
    {
        "slug": "huainanzi",
        "era": "shanggu",
        "kind": "myth",
        "year": -139,
        "author": "佚名",
        "authorSlug": "anonymous",
        "publisher": None,
        "coverCredit": "public-domain",
        "tags": ["神话", "天文", "哲学"],
        "sources": ["《淮南子》刘安主持编撰，中华书局"],
        "zh": {
            "title": "淮南子",
            "body": "《淮南子》原名《鸿烈》，西汉淮南王刘安召集门客集体编撰，约成书于公元前 139 年，"
            "全书二十一篇，以道家思想为纲而兼采儒、法、阴阳诸家，被视为汉初黄老之学的集大成之作。\n\n"
            "内容包罗甚广：从宇宙生成、天文历法、地理方物，到治国之道、养生之术、用兵之要，"
            "几乎涵盖当时可知的全部知识领域。其中《天文训》系统论述日月星辰的运行与节气推算，"
            "《地形训》则描述九州之外的八殥八纮，构想了一个远超实际辖域的空间秩序。\n\n"
            "值得注意的是它保存神话的方式。共工怒触不周山、女娲补天、羿射九日、嫦娥奔月等故事，"
            "在此被嵌入一个关于宇宙秩序如何建立、又被如何修复的解释框架中——神话不再是孤立的奇闻，"
            "而成为回答「天为何如此」的理论工具。\n\n"
            "这种把神话、观测与思辨熔于一炉的做法，使它成为理解中国早期宇宙观的关键文本。"
            "本站归入神话源流层：它提供的是一套关于天地结构的系统构想，"
            "其中对空间层次的划分，已带有某种「宇宙模型」的意味。",
        },
        "en": {
            "title": "Huainanzi",
            "body": "Originally titled Honglie, this work was compiled around 139 BCE by the retainers of Liu An, King of Huainan, in twenty-one chapters. Organised around Daoist thought while drawing on Confucian, Legalist and Yin-Yang schools, it is regarded as the culmination of early Han Huang-Lao learning.\n\n"
            "Its range is encyclopaedic: the generation of the cosmos, astronomy and the calendar, geography and its products, the governance of states, techniques of nurturing life, and the conduct of war — nearly the whole field of knowledge then available. The Treatise on Astronomy sets out the motions of sun, moon and stars and the computation of seasonal nodes; the Treatise on Terrain describes the eight margins and eight cords beyond the nine provinces, projecting a spatial order far wider than any actual jurisdiction.\n\n"
            "Its manner of preserving myth is notable. The stories of Gonggong striking Mount Buzhou, Nüwa repairing the sky, Yi shooting the nine suns and Chang'e flying to the moon are set inside an explanatory frame of how cosmic order is established and repaired: myth ceases to be isolated marvel and becomes a theoretical instrument for answering why heaven is as it is.\n\n"
            "Fusing myth, observation and speculation, it is a key text for understanding early Chinese cosmology. Filed here under Myth, it offers a systematic vision of the structure of heaven and earth whose division of spatial levels already carries something of a cosmological model.",
        },
    },
    {
        "slug": "shenyijing",
        "era": "shanggu",
        "kind": "myth",
        "year": None,
        "yearUncertain": True,
        "author": "佚名",
        "authorSlug": "anonymous",
        "publisher": None,
        "coverCredit": "public-domain",
        "tags": ["志怪", "异域", "地理"],
        "sources": ["《神异经》旧题东方朔撰，实为汉魏间作品"],
        "zh": {
            "title": "神异经",
            "body": "《神异经》一卷，旧题西汉东方朔所撰，后世学者多认为实为汉魏间人伪托。"
            "全书仿《山海经》体例，按东、东南、南、西南、西、西北、北、东北、中荒等方位分条，"
            "记载四方异国的奇人、异兽与异物。\n\n"
            "书中所记诸如有翼而不飞的「鹄国」人、身高千丈的「朴父」夫妇、能吐火的「火光兽」、"
            "东海中「长七寸」的小人等，形态各异而笔法统一。它继承了《山海经》以方位为纲的组织方式，"
            "但条目更短、更趋志怪化，神话色彩相对减弱。\n\n"
            "其想象力主要体现在对「异质生命形态」的编排上：以方位为坐标系，"
            "把各种非常态的身体、能力与习性分门别类地安置在世界边缘。"
            "这一做法实际上构造了一个可供检索的想象世界图式。\n\n"
            "在志怪谱系中，《神异经》是《山海经》与《十洲记》之间的重要环节，"
            "对后世类书与志怪小说影响深远。本站归入神话源流层——它延续的是"
            "以地理框架收纳想象的古老方式，而非对技术的推想。",
        },
        "en": {
            "title": "Classic of Divine Marvels",
            "body": "A single chapter attributed to Dongfang Shuo of the Western Han, though scholars generally hold it to be a later Han–Wei work written under his name. Modelled on the Classic of Mountains and Seas, it arranges its entries by compass direction — east, southeast, south, southwest, west, northwest, north, northeast and the central waste — recording the strange peoples, beasts and objects of each quarter.\n\n"
            "It describes such things as the winged yet flightless men of the Crane Country, the thousand-zhang couple Pufu, a beast that breathes fire, and inch-tall people in the eastern sea. The organising principle of the Classic of Mountains and Seas is retained, but entries are shorter, more anecdotal, and less mythic in tone.\n\n"
            "Its imagination lies chiefly in the arrangement of heterogeneous life forms: using direction as a coordinate system, it classifies abnormal bodies, capacities and habits and settles them at the edges of the world, effectively constructing a searchable atlas of the imaginary.\n\n"
            "An important link between the Classic of Mountains and Seas and the Record of the Ten Continents, it influenced later leishu and marvel fiction. Filed under Myth: it continues the old practice of housing imagination inside a geographical frame rather than speculating about technology.",
        },
    },
    {
        "slug": "shizhouji",
        "era": "shanggu",
        "kind": "myth",
        "year": None,
        "yearUncertain": True,
        "author": "佚名",
        "authorSlug": "anonymous",
        "publisher": None,
        "coverCredit": "public-domain",
        "tags": ["志怪", "仙山", "异域"],
        "sources": ["《十洲记》旧题东方朔撰，汉魏六朝作品"],
        "zh": {
            "title": "十洲记",
            "body": "《十洲记》又名《海内十洲记》，一卷，旧题东方朔撰，实为汉魏六朝间作品。"
            "全书以东方朔答汉武帝之问的形式，描述大海之中祖洲、瀛洲、玄洲、炎洲、长洲、元洲、"
            "流洲、生洲、凤麟洲、聚窟洲等十洲，以及沧海岛、方丈、蓬莱、昆仑等神山仙境。\n\n"
            "每洲各有奇物：祖洲的不死草可令死者复生，炎洲的火浣布入火不燃，"
            "风生兽与火光兽各具异能，聚窟洲的返魂香能起死回生。"
            "这些物产的记述往往精确到形制、产地与功效，读来近乎药物志。\n\n"
            "其想象力有两点值得注意：一是把仙境彻底地理化——十洲各有方位、距离与物产，"
            "构成一个可被描述的世界；二是对「功能性奇物」的偏好，不死草、火浣布、返魂香"
            "都是可直接作用于人体的技术性物件，带有早期「技术奇想」的色彩。\n\n"
            "它与《神异经》同为《山海经》之后志怪地理学的重要分支，"
            "并与早期道教神仙信仰相互发明。本站归入神话源流层。",
        },
        "en": {
            "title": "Record of the Ten Continents",
            "body": "Also called the Record of the Ten Continental Isles Within the Seas, a single chapter attributed to Dongfang Shuo but in fact a work of the Han to Six Dynasties period. Cast as Dongfang Shuo answering questions from Emperor Wu of Han, it describes ten isles in the ocean — Zu, Ying, Xuan, Yan, Chang, Yuan, Liu, Sheng, Fenglin and Juku — together with such paradises as Canghai Island, Fangzhang, Penglai and Kunlun.\n\n"
            "Each isle has its marvel: the herb of immortality on Zu that restores the dead, the fire-laundered cloth of Yan that does not burn, beasts that ride the wind or breathe fire, and the soul-returning incense of Juku. These products are recorded with a precision of form, provenance and effect that reads almost like a pharmacopoeia.\n\n"
            "Two features of its imagination stand out. First, it thoroughly geographises paradise: each isle has direction, distance and produce, forming a world that can be described. Second, it favours functional marvels — the herb, the cloth, the incense are all technological objects acting directly on the human body, touched with early technological fancy.\n\n"
            "With the Classic of Divine Marvels it forms a major branch of marvel geography after the Classic of Mountains and Seas, and illuminates early Daoist belief in immortals. Filed under Myth.",
        },
    },
    {
        "slug": "liezi-tangwen",
        "era": "shanggu",
        "kind": "myth",
        "year": None,
        "yearUncertain": True,
        "author": "列御寇",
        "authorSlug": "lieyukou",
        "publisher": None,
        "coverCredit": "public-domain",
        "tags": ["机械", "偃师", "道家"],
        "featured": True,
        "sources": ["《列子·汤问》杨伯峻《列子集释》"],
        "zh": {
            "title": "列子 · 汤问",
            "body": "《列子·汤问》是《列子》八篇中的第五篇，托殷汤与夏革问答，纵论天地之外、万物之极。"
            "今本《列子》一般认为是魏晋间人辑补而成，托名战国道家人物列御寇，"
            "但其中不少材料可上溯至先秦。\n\n"
            "篇中设问极为大胆：物有巨细乎？有修短乎？有同异乎？上下八方有极尽乎？"
            "在回答中出现了归墟、岱舆、员峤等海上神山，以及僬侥国、诤人等异民，"
            "显示出一种对世界边界的系统追问。\n\n"
            "其中最著名的是「偃师造人」一段。偃师献给周穆王一个偶人，"
            "能歌善舞、瞬目而招王之左右，拆解开来则「皆傅会革、木、胶、漆、白、黑、丹、青之所为」，"
            "内则肝胆心肺皆具，而「合会复如初见」。这被公认为中国最早的机器人想象，"
            "也是机械生命叙事的源头——它已经触及了人造物与生命边界这一后世科幻的核心命题。\n\n"
            "此外篇中还有扁鹊换心、造父习御等内容，共同构成了一套关于身体可改造、"
            "技能可传递的早期设想。本站将其归入神话源流层，"
            "但偃师一节事实上已具备前科幻的质地。",
        },
        "en": {
            "title": "Liezi: King Tang's Questions",
            "body": "The fifth of the eight chapters of the Liezi, framing a dialogue between King Tang of Shang and Xia Ge on what lies beyond heaven and earth and the limits of things. The received text is generally thought to have been compiled in the Wei–Jin period under the name of the Warring States Daoist Lie Yukou, though much of its material reaches back further.\n\n"
            "Its questions are audacious: are there things immensely large or minute, long-lived or brief, alike or different? Do the eight directions of space have an end? The answers produce such sea-mounts as Guixu, Daiyu and Yuanqiao and such peoples as the dwarfs of Jiaoyao, showing a systematic interrogation of the world's edges.\n\n"
            "The most celebrated passage concerns the artificer Yanshi, who presents King Mu with an automaton that sings and dances and casts eyes at the king's attendants. Taken apart, it proves to be leather, wood, glue and lacquer, black, white, vermilion and blue, yet inwardly furnished with liver, gall, heart and lungs; reassembled, it is as before. This is recognised as China's earliest robot imagination and the origin of mechanical-life narrative — it already touches the boundary between artefact and living thing that later science fiction makes its own.\n\n"
            "With its accounts of Bian Que exchanging hearts and Zaofu learning to drive, the chapter assembles an early vision of the body as modifiable and of skill as transferable. Filed under Myth, though the Yanshi episode is in substance already proto-science fiction.",
        },
    },
    {
        "slug": "bowuzhi",
        "era": "shanggu",
        "kind": "myth",
        "year": 290,
        "yearUncertain": True,
        "author": "张华",
        "authorSlug": "zhanghua",
        "publisher": None,
        "coverCredit": "public-domain",
        "tags": ["博物", "志怪", "异域"],
        "sources": ["《博物志》张华撰，范宁校证"],
        "zh": {
            "title": "博物志",
            "body": "《博物志》十卷，西晋张华撰。张华官至司空，以博闻强记著称，"
            "此书是其采撷群书、兼听异闻的笔记汇编，约成书于公元 290 年前后。"
            "原书已散佚，今本为后人辑录，内容涵盖山川地理、飞禽走兽、草木虫鱼、"
            "方术异闻、人物传说等，分类近四十目。\n\n"
            "书中最为人称道的是那些带有「科学观察」色彩的条目：如「八月槎」记有人乘槎浮海，"
            "至一处有城郭屋舍、丈夫牵牛饮河，后知为天河；「穿胸国「」羽民国」等异民"
            "承《山海经》旧说而有所增益；另有关于石油、天然气、磁石等自然物的记载。\n\n"
            "其想象力在于把「远方」与「日常」打通：异域奇闻与本土物产被置于同一分类框架下，"
            "暗示世界是连续的、可知的。这种态度使《博物志》不同于纯粹的志怪小说，"
            "而更接近一部早期百科全书。\n\n"
            "它是中国博物学传统的关键文本，对《酉阳杂俎》《太平广记》等影响深远。"
            "本站归入神话源流层：书中那些可载人升空的想象虽仍依托神话，"
            "但其分类意识与观察态度已是一种前科学的世界观。",
        },
        "en": {
            "title": "Record of Diverse Matters",
            "body": "A work in ten chapters by Zhang Hua of the Western Jin, who rose to Minister of Works and was famed for the breadth of his reading. Compiled around 290 from earlier books and from hearsay, it survives only in later recensions. It covers mountains and rivers, birds and beasts, plants, fish and insects, techniques and marvels, and legends of persons, in close to forty categories.\n\n"
            "Its most admired entries are those touched by observation: the August Raft, in which a man floats out to sea and finds walled dwellings where a man waters an ox at a river that proves to be the Milky Way; the Pierced-Chest and Feathered-People countries, extending the lore of the Classic of Mountains and Seas; and notices of petroleum, natural gas and lodestone.\n\n"
            "Its imagination joins the far away to the everyday: exotic hearsay and local produce are placed within one classificatory frame, implying a world that is continuous and knowable. That attitude sets it apart from pure marvel fiction and brings it nearer an early encyclopaedia.\n\n"
            "A key text of Chinese natural history, it shaped later works from Miscellaneous Morsels from Youyang to the Extensive Records of the Taiping Era. Filed under Myth: its images of rafts carrying men skyward still lean on myth, but its classificatory sense and observational stance already constitute a proto-scientific world view.",
        },
    },
    {
        "slug": "shiyiji",
        "era": "shanggu",
        "kind": "myth",
        "year": None,
        "yearUncertain": True,
        "author": "王嘉",
        "authorSlug": "wangjia",
        "publisher": None,
        "coverCredit": "public-domain",
        "tags": ["志怪", "飞行器", "奇器"],
        "featured": True,
        "sources": ["《拾遗记》王嘉撰，萧绮录，中华书局"],
        "zh": {
            "title": "拾遗记",
            "body": "《拾遗记》十卷，东晋王嘉撰，南朝梁萧绮整理并加录语。前九卷记自上古庖牺、神农"
            "至东晋各代的奇闻异事，末一卷专记海外仙山。全书文辞绮丽，与干宝《搜神记》的质朴"
            "形成鲜明对照，是六朝志怪中最具文采的一种。\n\n"
            "书中大量描写神异器物：舜时「贯月槎」每十二年绕月一周，上有羽人栖息；"
            "有「沦波舟」可行于海底而人不湿；又有「游仙枕」「照骨宝「」却尘犀」等奇物，"
            "各以形制、材质、功效详加记述。\n\n"
            "这些记载的价值在于其具体性。贯月槎并非抽象的仙术，而是有周期、有乘员、"
            "可往返的载具；沦波舟则明确为水下航行器。"
            "它们把「升天入地」的神话愿望，转化成了可描述的机械构想。\n\n"
            "因此《拾遗记》被视为中国飞行器与潜水器想象最重要的早期文献之一。"
            "本站归入神话源流层，但就其「奇器谱」这一部分而言，"
            "其性质已非常接近后世的技术幻想。",
        },
        "en": {
            "title": "Researches into Lost Records",
            "body": "A work in ten chapters by Wang Jia of the Eastern Jin, edited with added commentary by Xiao Qi of the Liang. The first nine chapters record marvels from the age of Fuxi and Shennong down to the Eastern Jin; the tenth is devoted to immortal mountains overseas. Its ornate prose stands in sharp contrast to the plainness of Gan Bao's In Search of the Supernatural, and it is the most literary of the Six Dynasties marvel collections.\n\n"
            "It abounds in marvellous artefacts: the moon-piercing raft of Shun's reign that circles the moon once every twelve years with winged men aboard; the billow-sinking boat that travels beneath the sea without wetting its passengers; the wandering-immortal pillow, the bone-illumining gem and the dust-repelling rhinoceros horn, each described by form, material and effect.\n\n"
            "Their value lies in their concreteness. The moon raft is not abstract immortals' art but a craft with a period, a crew and a return voyage; the boat is explicitly a submersible. They convert the mythic wish of ascending to heaven and entering the earth into describable mechanical designs.\n\n"
            "The book is therefore one of the most important early documents of Chinese imagining of flying and submersible craft. Filed under Myth, though in its catalogue of marvellous machines its substance is already close to later technological fantasy.",
        },
    },
    {
        "slug": "soushenji",
        "era": "shanggu",
        "kind": "myth",
        "year": 350,
        "yearUncertain": True,
        "author": "干宝",
        "authorSlug": "ganbao",
        "publisher": None,
        "coverCredit": "public-domain",
        "tags": ["志怪", "鬼神", "变形"],
        "sources": ["《搜神记》干宝撰，汪绍楹校注"],
        "zh": {
            "title": "搜神记",
            "body": "《搜神记》原书三十卷，东晋干宝撰，约成书于公元 350 年前后。"
            "干宝曾任著作郎，领修国史，据其自序，此书之作既有感于父婢死而复生、"
            "兄气绝而复苏的亲历，亦有意于「发明神道之不诬」。\n\n"
            "原书宋代已散佚，今本二十卷为明人从类书中辑出，收故事四百余则，"
            "内容涉及神仙方术、鬼怪灵异、祸福征应、物怪变化等。"
            "名篇如《干将莫邪》《韩凭夫妇》《李寄斩蛇》《董永》等，"
            "情节完整而情感真挚，已具成熟的小说品格。\n\n"
            "全书最核心的母题是「变化」：人化为物、物化为人、死而复生、形神相离。"
            "这些变化不依赖机械或技术，而源于气、精、魂的聚散，"
            "构成了一套关于生命形态可转换的想象体系。\n\n"
            "《搜神记》确立了志怪小说的基本范式，后世《搜神后记》《幽明录》等"
            "一脉相承，并为唐传奇与《聊斋志异》所本。本站归入神话源流层——"
            "它提供的是变化与重生的原型，而非对科学原理的推演。",
        },
        "en": {
            "title": "In Search of the Supernatural",
            "body": "Originally in thirty chapters, compiled by Gan Bao of the Eastern Jin around 350. Gan Bao served as editorial director and led the compilation of the national history; by his own preface the book arose both from what he had witnessed — his father's maidservant returning from death, his brother reviving after his breath ceased — and from a wish to demonstrate that the ways of the spirits are not empty.\n\n"
            "The original was lost by the Song; the received twenty chapters were reassembled by Ming scholars from leishu and contain some four hundred tales of immortals and techniques, ghosts and prodigies, omens of fortune, and transformations of things. Pieces such as Ganjiang and Moye, Han Ping and His Wife, Li Ji Slays the Serpent and Dong Yong are complete in plot and sincere in feeling, already mature fiction.\n\n"
            "The central motif is transformation: human into thing, thing into human, the dead reviving, body and spirit parting. Such changes depend not on machinery or technique but on the gathering and dispersal of qi, essence and soul, forming an imaginative system in which the forms of life are convertible.\n\n"
            "The book established the basic pattern of marvel fiction, continued in later collections and drawn upon by Tang tales and by Liaozhai. Filed under Myth: it supplies archetypes of transformation and rebirth rather than extrapolation from scientific principle.",
        },
    },
    {
        "slug": "youyangzazu",
        "era": "shanggu",
        "kind": "myth",
        "year": 863,
        "author": "段成式",
        "authorSlug": "duanchengshi",
        "publisher": None,
        "coverCredit": "public-domain",
        "tags": ["志怪", "博物", "登月"],
        "featured": True,
        "sources": ["《酉阳杂俎》段成式撰，中华书局"],
        "zh": {
            "title": "酉阳杂俎",
            "body": "《酉阳杂俎》前集二十卷、续集十卷，唐代段成式撰，约成书于公元 863 年。"
            "段成式出身官宦世家，博闻强记，此书是其读书与见闻的杂记，"
            "内容涵盖志怪传奇、佛道典故、域外异闻、动植矿物、饮食医药等，"
            "被后世视为唐代笔记的百科全书。\n\n"
            "其中最著名的一则，记大和中郑仁本表弟与王秀才游嵩山迷路，"
            "遇一布衣其人自称来自月亮，谓「月乃七宝合成，其形如丸，其影日烁其凸处也」，"
            "并展示「斤凿」与玉屑饭，指引二人归途。"
            "这段对话在承认月亮为球形、解释月影成因上，"
            "已含有相当准确的朴素天文学认识。\n\n"
            "它的特别之处在于把「登月」处理为一次遭遇而非神话："
            "月中人是可遇见的劳动者，月亮是可分解、可修补的实体。"
            "这与《山海经》式的遥望远国截然不同，"
            "是一种更接近后世的、把异域当作可抵达之处的态度。\n\n"
            "《酉阳杂俎》保存了大量唐五代的社会与博物史料。"
            "本站归入神话源流层，而「月中人」一则，"
            "实为中国早期登月想象中最具现代气质的一篇。",
        },
        "en": {
            "title": "Miscellaneous Morsels from Youyang",
            "body": "A Tang miscellany of twenty chapters with ten supplementary, compiled by Duan Chengshi around 863. Born to an official family and prodigiously learned, Duan gathered notes from his reading and experience covering marvels and tales, Buddhist and Daoist allusion, foreign report, fauna, flora and minerals, food and medicine — an encyclopaedia of Tang notebook writing.\n\n"
            "Its most famous entry tells how, during the Dahe era, the cousin of Zheng Renben and one Scholar Wang lost their way on Mount Song and met a man in plain cloth who said he came from the moon: the moon, he said, is composed of seven precious substances, its shape a ball, and its shadows the sun striking its convexities; he showed them his adze and chisel and a rice of jade fragments, and set them on the path home. The exchange contains a notably accurate folk astronomy, granting the moon's sphericity and explaining its markings.\n\n"
            "What distinguishes it is that travel to the moon is treated as an encounter rather than a myth: the lunar man is a labourer one might meet, and the moon a solid thing that can be taken apart and repaired. This differs utterly from the distant gazing of the Classic of Mountains and Seas, and is closer in attitude to later writing that treats the exotic as reachable.\n\n"
            "The book preserves a great body of Tang social and natural-history material. Filed under Myth, yet its lunar encounter is the most modern in temper of all early Chinese moon imaginings.",
        },
    },
    # ================================================================= 前科幻
    {
        "slug": "xiyouji",
        "era": "song-ming-qing",
        "kind": "proto-sf",
        "year": 1592,
        "author": "吴承恩",
        "authorSlug": "wuchengen",
        "publisher": "世德堂本",
        "coverCredit": "public-domain",
        "tags": ["神魔", "变化", "取经"],
        "sources": ["《西游记》明世德堂本，人民文学出版社整理本"],
        "zh": {
            "title": "西游记",
            "body": "《西游记》一百回，明代吴承恩著（一说为累积型作品，吴为最后写定者），"
            "现存最早刊本为明万历二十年金陵世德堂本。小说以唐代玄奘取经的史实为引，"
            "叙孙悟空出世、大闹天宫、被压五行山，后护唐僧西行、历九九八十一难而成正果。\n\n"
            "全书以神魔斗争为表，而以心性修行为里。孙悟空的七十二变、筋斗云、"
            "分身法、定身法、火眼金睛，以及各类法宝——金刚琢、紫金红葫芦、"
            "芭蕉扇、金箍棒——共同构成了一套想象极为系统的能力体系。"
            "这些设定并非随意铺陈，而是彼此制衡：一物降一物，"
            "形成近乎规则化的对抗逻辑。\n\n"
            "从后世眼光看，其想象力集中在两处：一是身体与空间的可塑性——"
            "变化、飞行、缩地、分身，都是对物理限制的突破；"
            "二是器物的功能化——法宝各有明确的使用条件与破解方法，"
            "这种「设定驱动」的思路与现代科幻的技术构想有相通之处。\n\n"
            "《西游记》是中国最富想象力资源的叙事文本之一，"
            "也是被影像化次数最多的中国文学IP。本站归入前科幻层："
            "它提供了关于能力与限制的想象模型，"
            "但运作机制是法术而非科学。",
        },
        "en": {
            "title": "Journey to the West",
            "body": "In one hundred chapters, attributed to Wu Cheng'en of the Ming, though often regarded as an accreted work brought to final form by him; the earliest extant edition is the Shidetang printing of 1592. Taking the historical pilgrimage of the Tang monk Xuanzang as its pretext, it follows the birth of Sun Wukong, his havoc in heaven, his imprisonment beneath Five Elements Mountain, and his escort of Xuanzang westward through eighty-one tribulations to attainment.\n\n"
            "Ostensibly a narrative of gods and demons, at heart it is about the cultivation of mind. Sun Wukong's seventy-two transformations, his cloud-somersault, self-multiplication, immobilising spell and fiery eyes, together with such devices as the diamond bracelet, the purple-gold gourd, the plantain fan and the staff that pierces the sea, form an unusually systematic imaginative apparatus. These are not random: each thing is checked by another, producing an almost rule-governed logic of contest.\n\n"
            "Two features matter for later imagination. First, the plasticity of body and space — transformation, flight, shrinking of distance and self-division all break physical limits. Second, the functionalisation of objects: each treasure has explicit conditions of use and of counter, a premise-driven method with affinities to modern science fiction's handling of technology.\n\n"
            "Among the richest imaginative texts in Chinese literature, it is also the most frequently adapted Chinese work on screen. Filed here as Proto-SF: it supplies an imaginative model of power and limit, but its mechanism is magic rather than science.",
        },
    },
    {
        "slug": "jinghuayuan",
        "era": "song-ming-qing",
        "kind": "proto-sf",
        "year": 1828,
        "author": "李汝珍",
        "authorSlug": "liruzhen",
        "publisher": None,
        "coverCredit": "public-domain",
        "coverSource": "https://shuge.org/",
        "tags": ["海外奇国", "机械想象", "寓言"],
        "featured": True,
        "sources": ["《镜花缘》人民文学出版社"],
        "zh": {
            "title": "镜花缘",
            "body": "《镜花缘》一百回，清代李汝珍著，初刊于嘉庆年间（约 1828 年前后）。"
            "李汝珍字松石，博通音韵、医算、弈棋，以二十年之力成此书。"
            "全书前半写唐敖、林之洋、多九公航海游历海外诸国，"
            "后半写唐敖之女唐小山寻父及百位才女之事。\n\n"
            "海外诸国是全书最精彩的部分：君子国好让不争，女儿国男女易位，"
            "无肠人刻薄吝啬，两面国人有前后两张脸，还有其他各国各以一种社会病症为形。"
            "这些国家既是对现实的讽刺投影，也是一次系统的社会制度想象实验——"
            "一国一变量，观察其后果。\n\n"
            "书中还出现了明确的机械与飞行想象：飞车、机关、可以代步的器械，"
            "以及借助水力、风力装置的描写。"
            "虽然其原理仍依托巧匠之术而非物理定律，"
            "但这种以技术改善生活的取向已相当接近后世科幻的思路。\n\n"
            "《镜花缘》被视为中国古代最具科幻色彩的作品之一，"
            "其海外奇国的写法上承《山海经》、下启现代乌托邦叙事。"
            "本站归入前科幻层。",
        },
        "en": {
            "title": "Flowers in the Mirror",
            "body": "In one hundred chapters by Li Ruzhen of the Qing, first printed in the Jiaqing era around 1828. Styled Songshi, Li was erudite in phonology, medicine, mathematics and chess, and spent two decades on the book. Its first half follows Tang Ao, Lin Zhiyang and Duo Jiugong on a voyage through overseas countries; the second follows Tang Ao's daughter Xiaoshan in search of her father and the assembly of a hundred talented women.\n\n"
            "The overseas realms are its finest achievement: the Country of Gentlemen where all defer, the Country of Women where the sexes are reversed, the Gutless whose meanness is literal, the Two-Faced who have a face before and behind — each realm embodying a social malady. They are at once satiric projections of reality and a systematic experiment in imagining social institutions: one variable per country, its consequences observed.\n\n"
            "The book also contains explicit mechanical and aerial imagining: flying carriages, clockwork, vehicles for travel, and devices worked by water and wind. Though their mechanism rests on the cunning artisan rather than physical law, the orientation — improving life by technology — comes close to later science fiction.\n\n"
            "Regarded as among the most science-fictional works of pre-modern China, its overseas realms look back to the Classic of Mountains and Seas and forward to modern utopian narrative. Filed here as Proto-SF.",
        },
    },
    {
        "slug": "taipingguangji",
        "era": "song-ming-qing",
        "kind": "proto-sf",
        "year": 978,
        "author": "佚名",
        "authorSlug": "anonymous",
        "publisher": "太平兴国官修",
        "coverCredit": "public-domain",
        "tags": ["类书", "志怪", "辑录"],
        "sources": ["《太平广记》李昉等编，中华书局"],
        "zh": {
            "title": "太平广记",
            "body": "《太平广记》五百卷，北宋太平兴国年间李昉、扈蒙等奉敕编纂，"
            "与《太平御览》《文苑英华》《册府元龟》并称宋初四大书，"
            "专收汉代至宋初的野史、传记、小说，按题材分为九十二大类。"
            "全书引书四百余种，其中大半后世已亡佚。\n\n"
            "它的价值首先在于保存：大量志怪、传奇、异闻赖此得以流传，"
            "《山海经》系统的异域想象、《搜神记》系统的变化母题、"
            "唐代传奇的想象叙事，在此汇为一编。"
            "鲁迅称其为小说史上的「渊薮」。\n\n"
            "其次在于分类。九十二类之中，神仙、女仙、异人、异僧、"
            "妖怪、精怪、灵异、幻术、器玩等类目，"
            "构成了一套关于「非常态事物」的完整分类体系——"
            "这本身就是一种对想象世界的系统化整理。\n\n"
            "《太平广记》是后世小说、戏曲取之不尽的素材库，"
            "也是研究中国想象文学最重要的文献之一。"
            "本站归入前科幻层：它虽非创作，"
            "却为后世的想象提供了分类框架与素材储备。",
        },
        "en": {
            "title": "Extensive Records of the Taiping Era",
            "body": "In five hundred chapters, compiled under imperial commission by Li Fang, Hu Meng and others during the Taiping Xingguo era of the Northern Song. With the Taiping Imperial Reader, the Finest Blossoms of the Garden of Letters and the Prime Tortoise of the Record Bureau, it is one of the four great books of the early Song, gathering unofficial history, biography and fiction from the Han to the early Song in ninety-two major categories, and citing over four hundred works, most of them since lost.\n\n"
            "Its first value is preservation: a great body of marvels, tales and strange reports survives only here. The exotic geography descending from the Classic of Mountains and Seas, the motifs of transformation from In Search of the Supernatural, and the imaginative narratives of Tang fiction are gathered into one corpus. Lu Xun called it the wellspring of the history of fiction.\n\n"
            "Its second value is classification. Among its ninety-two categories — immortals, female immortals, extraordinary persons, exotic monks, demons, sprites, numinous events, illusionary arts, curious objects — lies a complete taxonomy of anomalous things, itself a systematisation of the imagined world.\n\n"
            "An inexhaustible store for later fiction and drama, and one of the chief documents for the study of Chinese imaginative literature. Filed as Proto-SF: though not creative writing, it supplied later imagination with both a classificatory frame and a stock of material.",
        },
    },
    # =================================================================== 晚清
    {
        "slug": "xinzhongguo-weilaiji",
        "era": "wanqing",
        "kind": "sf",
        "year": 1902,
        "author": "梁启超",
        "authorSlug": "liangqichao",
        "publisher": "新小说",
        "coverCredit": "public-domain",
        "tags": ["未来记", "政治小说", "乌托邦"],
        "sources": ["《新小说》1902 年创刊号连载"],
        "zh": {
            "title": "新中国未来记",
            "body": "《新中国未来记》是梁启超 1902 年在自己创办的《新小说》创刊号上开始连载的政治小说，"
            "原拟写五回以上，实际仅成五回，未完。"
            "它是中国近代第一部明确以「未来」为叙事支点的政治小说，"
            "也被视为晚清科幻热潮的思想源头。\n\n"
            "小说采用倒叙：开篇即设定 1962 年的中国已实现君主立宪、"
            "成为世界强国，上海举办大博览会，万国来朝；"
            "随后回头叙述六十年来宪政运动的发展过程。"
            "书中大量篇幅用于政治辩论，"
            "人物围绕改良与革命两条道路反复辩难。\n\n"
            "其想象力不在技术而在制度。梁启超借「未来史」的形式，"
            "把政治主张转化为可想象的现实图景，"
            "这种以时间投射来论证当下的做法，"
            "正是后世政治科幻的基本方法。\n\n"
            "虽然文学性常被批评为薄弱，"
            "但它开创的「未来记」体在晚清蔚为风潮，"
            "陆士谔《新中国》、碧荷馆主人《新纪元》等接踵而至。"
            "本站将其列为晚清科幻的起点坐标。",
        },
        "en": {
            "title": "The Future of New China",
            "body": "Serialised by Liang Qichao from 1902 in the first issue of New Fiction, the journal he founded, this political novel was planned at length but only five chapters appeared. It is the first modern Chinese work of fiction to take the future explicitly as its narrative fulcrum, and is regarded as the intellectual source of the Late Qing science fiction boom.\n\n"
            "Told in flashback, it opens in 1962 with a China that has become a constitutional monarchy and a world power, hosting a great exposition in Shanghai with all nations in attendance, then turns back to trace sixty years of constitutionalist struggle. Much of the text is given to political debate, its characters arguing the cases for reform and for revolution.\n\n"
            "Its imagination is institutional rather than technological. Using the form of future history, Liang converts a political programme into an imaginable picture of reality — a method of arguing the present by projecting the future that later political science fiction would make its own.\n\n"
            "Though often criticised as thin fiction, it inaugurated a vogue for future histories: Lu Shi'e's New China and The New Era by the Master of the Blue Lotus Studio followed. This archive treats it as the coordinate zero of Late Qing science fiction.",
        },
    },
    {
        "slug": "yuejie-lvxing",
        "era": "wanqing",
        "kind": "sf",
        "year": 1903,
        "author": "鲁迅",
        "authorSlug": "luxun",
        "publisher": "日本东京进化社",
        "coverCredit": "public-domain",
        "tags": ["译介", "凡尔纳", "月球"],
        "sources": ["《月界旅行》鲁迅译，1903 年进化社版"],
        "zh": {
            "title": "月界旅行",
            "body": "《月界旅行》是鲁迅据凡尔纳《从地球到月球》的日译本转译而成，"
            "1903 年由日本东京进化社出版，署「中国教育普及社译印」。"
            "这是鲁迅最早的文学活动之一，也是凡尔纳作品进入中文世界的重要一步。\n\n"
            "译本采用章回体，对原著做了大量删改与本土化处理，"
            "以适应晚清读者的阅读习惯。"
            "这种「译述」而非直译的方式，是当时译界的通行做法。\n\n"
            "真正影响深远的是卷首《辨言》。鲁迅在其中提出："
            "科学小说应「经以科学，纬以人情」，"
            "并明确指出这类作品可以「改良思想，补助文明」，"
            "使读者在趣味中获得格致之学。"
            "这是中文语境中第一次系统阐述科学小说的功能与价值，"
            "被视为中国科幻理论的起点。\n\n"
            "本条目录入的是译介贡献而非原创作品，"
            "与鲁迅的原创创作分列，以免混淆。"
            "同年他还译出《地底旅行》（凡尔纳《地心游记》），"
            "进一步推动了这一文类的传播。",
        },
        "en": {
            "title": "Journey to the Moon",
            "body": "Lu Xun's translation of Jules Verne's De la Terre à la Lune, made from a Japanese version and published in Tokyo in 1903. It is among his earliest literary undertakings and a significant step in bringing Verne into Chinese.\n\n"
            "Rendered in the chapter-verse style of the traditional novel, it abbreviates and domesticates the original to suit Late Qing reading habits — the customary method of the time, closer to adaptation than to literal translation.\n\n"
            "Its lasting influence lies in the preface. There Lu Xun proposed that science fiction be warped with science and woven with human feeling, and argued that such writing could reform thinking and supplement civilisation, letting readers acquire the study of nature through pleasure. It is the first systematic account in Chinese of the function and value of science fiction, and is taken as the starting point of Chinese SF theory.\n\n"
            "This entry records a translator's contribution rather than an original work, and is listed separately from Lu Xun's own fiction. In the same year he also translated Journey to the Centre of the Earth, further advancing the genre's circulation.",
        },
    },
    {
        "slug": "yueqiu",
        "era": "wanqing",
        "kind": "sf",
        "year": 1904,
        "author": "荒江钓叟",
        "authorSlug": "huangjiangdiaosou",
        "publisher": "绣像小说",
        "coverCredit": "public-domain",
        "coverSource": "https://archive.org/",
        "tags": ["月球", "气球", "首部"],
        "featured": True,
        "sources": ["《绣像小说》1904 年连载"],
        "zh": {
            "title": "月球殖民地小说",
            "body": "《月球殖民地小说》自 1904 年起连载于《绣像小说》，作者署名「荒江钓叟」，"
            "真实姓名与生平均不可考，一般认为是化名。全书未完，"
            "现存约三十五回。\n\n"
            "故事叙湖南人龙孟华因报仇杀人逃亡海外，"
            "结识日本义士玉太郎，二人乘气球遍游南洋、欧美，"
            "后又遇月球人，乘气球飞往月球，见识月球上的奇异文明。"
            "小说把志怪、冒险、时事议论与新知介绍熔于一炉，"
            "是典型的晚清「新小说」形态。\n\n"
            "其科幻史意义在于三点：一是气球作为飞行器，"
            "是当时最前沿的航空技术在文学中的直接映射；"
            "二是月球被写成可抵达、有文明的地方，"
            "延续了《酉阳杂俎》以来的登月想象而更具现代色彩；"
            "三是它是目前所见中国最早的原创科幻长篇。\n\n"
            "因此它被视为中文科幻的起点坐标。"
            "本站归入科幻层，列为晚清时段的头条。",
        },
        "en": {
            "title": "Moon Colony Novel",
            "body": "Serialised from 1904 in Illustrated Fiction under the pen name Hermit of the Deserted River; the author's real name and biography are unknown. The novel was never completed, some thirty-five chapters surviving.\n\n"
            "It follows Long Menghua of Hunan, who flees abroad after a killing in revenge, and the Japanese swordsman Yutaro; the two travel by balloon through the South Seas, Europe and America, meet inhabitants of the moon, and fly there to observe its strange civilisation. Marvel, adventure, topical commentary and new knowledge are fused in a shape typical of the Late Qing new novel.\n\n"
            "Its significance for SF is threefold. The balloon is the most advanced aviation technology of the day, reflected directly in fiction. The moon is written as a reachable place with a civilisation, extending the lunar imagination of earlier works in a more modern key. And it is the earliest original Chinese science fiction novel known to us.\n\n"
            "It is therefore taken as the coordinate zero of Chinese science fiction. Filed as SF and placed first among the Late Qing entries.",
        },
    },
    {
        "slug": "xinfaluo",
        "era": "wanqing",
        "kind": "sf",
        "year": 1905,
        "author": "徐念慈",
        "authorSlug": "xunianci",
        "publisher": "小说林",
        "coverCredit": "public-domain",
        "tags": ["灵魂", "星球", "晚清"],
        "sources": ["《新法螺先生谭》徐念慈，小说林社 1905"],
        "zh": {
            "title": "新法螺先生谭",
            "body": "《新法螺先生谭》是徐念慈 1905 年所作，署名「东海觉我」，"
            "由小说林社出版。书名沿用此前一部德国童话的中译《法螺先生》，"
            "但内容完全另起炉灶，只是借其框架演绎自己的构想。\n\n"
            "小说叙主人公的灵魂脱离肉体，飞升太虚，"
            "先后游历月球、水星、金星等天体，"
            "观察各处文明形态，又经历种种宇宙奇观，"
            "最终魂魄归体。"
            "全书以第一人称展开，笔调奇崛，"
            "带有明显的科学启蒙意图。\n\n"
            "其想象力有两点突出：一是把「灵魂」设定为一种可独立运动的实体，"
            "从而绕开了当时航天技术的限制，使星际旅行得以成立——"
            "这与后世以意识上传实现星际航行有异曲同工之处；"
            "二是对各行星环境的描写，"
            "显示了作者对当时天文学知识的熟悉。\n\n"
            "徐念慈是晚清重要的翻译家与编辑，"
            "主编《小说林》，著译并进。"
            "本站将此书归入科幻层，"
            "视为晚清最具哲学意味的科学小说之一。",
        },
        "en": {
            "title": "New Tales of Mr. Windbag",
            "body": "Written by Xu Nianci in 1905 under the name Donghai Juewo and published by the Forest of Fiction press. The title borrows from a Chinese translation of the German Münchhausen tales, but the content is entirely new, using only the frame for Xu's own design.\n\n"
            "The narrator's soul leaves his body, ascends into the void, and visits the moon, Mercury, Venus and other bodies, observing their civilisations and cosmic marvels before returning to his flesh. Written in the first person in a singular register, it carries an evident intention of scientific enlightenment.\n\n"
            "Two features of its imagination stand out. Treating the soul as an independently mobile entity circumvents the limits of contemporary aeronautics and makes interstellar travel possible — not unlike later fiction that achieves the same by uploading consciousness. And its descriptions of planetary conditions show a writer at home with the astronomy of his day.\n\n"
            "Xu Nianci was an important Late Qing translator and editor who led the journal Forest of Fiction while writing and translating. Filed here as SF, it is among the most philosophical of Late Qing science fiction.",
        },
    },
    {
        "slug": "xinshitouji",
        "era": "wanqing",
        "kind": "sf",
        "year": 1908,
        "author": "吴趼人",
        "authorSlug": "wujianren",
        "publisher": "改良小说社",
        "coverCredit": "public-domain",
        "tags": ["理想国", "科技奇观", "续书"],
        "sources": ["《新石头记》吴趼人，改良小说社 1908"],
        "zh": {
            "title": "新石头记",
            "body": "《新石头记》四十回，吴趼人 1908 年作，由改良小说社出版，"
            "署「老少年」撰。这是《红楼梦》众多续书中构思最为奇特的一部——"
            "它让贾宝玉穿越到二十世纪初的中国。\n\n"
            "前半部写宝玉重历人间，目睹租界、报纸、铁路、轮船等新事物，"
            "以陌生化眼光审视近代中国的现实困境；"
            "后半部则进入「文明境界」，"
            "一个由甄宝玉治理、科技高度发达的理想国："
            "其中有飞车、隧车、潜艇、验骨镜、验髓镜、"
            "可调节气候的玻璃屋，以及能改良人种的医术。"
            "宝玉在此见到理想社会的运作方式。\n\n"
            "其想象力集中体现在「文明境界」部分。"
            "这些器械虽多以「电气」笼统解释，"
            "但功能设定具体、应用场景完整，"
            "且被组织进一个社会改良的整体方案，"
            "已具备科技乌托邦的雏形。\n\n"
            "小说以理想对照现实，"
            "表达了作者对器物救国的期待。"
            "本站归入科幻层，"
            "视为晚清科技乌托邦叙事的代表作。",
        },
        "en": {
            "title": "New Story of the Stone",
            "body": "In forty chapters, written by Wu Jianren in 1908 and published by the Reform Fiction press under the name Old Youth. It is the most singular of the many sequels to Dream of the Red Chamber, sending Jia Baoyu into China at the start of the twentieth century.\n\n"
            "The first half follows Baoyu through the modern world — concessions, newspapers, railways and steamships — defamiliarising the predicaments of late imperial China. The second half enters the Civilised Realm, an ideal state governed by the other Baoyu and advanced in technology: flying carriages, tunnel trains, submarines, bone-scopes and marrow-scopes, climate-controlled glass houses, and medicine capable of improving the human stock. There Baoyu observes an ideal society at work.\n\n"
            "Its imagination is concentrated in the Civilised Realm. Though the machines are mostly explained by a catch-all appeal to electricity, their functions are concrete, their uses fully situated, and they are organised within an overall programme of social improvement — a rudimentary technological utopia.\n\n"
            "Holding an ideal against reality, the novel voices its author's hope that artefacts might save the nation. Filed as SF, it is a representative work of Late Qing technological utopianism.",
        },
    },
    {
        "slug": "xinzhongguo-lu",
        "era": "wanqing",
        "kind": "sf",
        "year": 1910,
        "author": "陆士谔",
        "authorSlug": "lushie",
        "publisher": None,
        "coverCredit": "public-domain",
        "tags": ["未来记", "上海", "预言"],
        "featured": True,
        "sources": ["《新中国》陆士谔，1910"],
        "zh": {
            "title": "新中国",
            "body": "《新中国》又名《立宪四十年后之中国》，陆士谔 1910 年作，"
            "全书十二回，采用梦游体：主人公陆云翔在醉酒后梦见"
            "四十年后（即 1951 年）的中国。\n\n"
            "梦中上海已完全改观：黄浦江上建有铁桥，"
            "江底通有隧道电车，地面上跑着电车与汽车，"
            "跑马厅改为大戏场，浦东举办万国博览会，"
            "租界已经收回，中国成为拥有强大海军的立宪强国。"
            "书中还写到新的教育制度、司法制度与男女平权。\n\n"
            "这些设想中最常被提及的是地下电车（地铁）与浦江大桥，"
            "二者都在二十世纪下半叶成为现实；"
            "2010 年上海世博会的举办，更让书中"
            "「浦东开博览会」的想象显得近乎预言。"
            "当然，其立宪强国的政治设想并未实现。\n\n"
            "作为中国科幻中最著名的「预言」文本，"
            "《新中国》的价值在于它把国家现代化的集体愿望"
            "投射为具体的城市图景。"
            "本站归入科幻层，与梁启超《新中国未来记》并列为"
            "晚清「未来记」体的双璧。",
        },
        "en": {
            "title": "New China",
            "body": "Also known as China Forty Years After the Constitution, written by Lu Shi'e in 1910 in twelve chapters. Cast as a dream journey: the protagonist Lu Yunxiang, drunk, dreams of China forty years hence, in 1951.\n\n"
            "In the dream Shanghai is wholly transformed: an iron bridge crosses the Huangpu, tunnel trams run beneath the river, trams and motorcars fill the streets, the racecourse has become a great theatre, an international exposition is held in Pudong, the concessions have been recovered, and China is a constitutional power with a strong navy. New systems of education and justice, and equality of the sexes, are also described.\n\n"
            "Of these visions the underground railway and the bridge over the Huangpu are most often cited, both realised in the later twentieth century; the Shanghai World Expo of 2010 made the image of an exposition in Pudong seem almost prophetic. Its political vision of a constitutional power, of course, was not.\n\n"
            "As the most celebrated prophecy text in Chinese science fiction, its value lies in projecting a collective wish for national modernisation into a concrete picture of a city. Filed as SF, and paired with Liang Qichao's The Future of New China as the twin peaks of the Late Qing future history.",
        },
    },
    # =================================================================== 民国
    {
        "slug": "maochengji",
        "era": "minguo",
        "kind": "sf",
        "year": 1932,
        "author": "老舍",
        "authorSlug": "laoshe",
        "publisher": "现代书局",
        "coverCredit": "public-domain",
        "tags": ["寓言", "火星", "社会批判"],
        "featured": True,
        "sources": ["《猫城记》老舍，现代书局 1933"],
        "zh": {
            "title": "猫城记",
            "body": "《猫城记》是老舍 1932 年创作的长篇小说，"
            "先在《现代》杂志连载，1933 年由现代书局出版单行本。"
            "这是老舍创作中唯一一部科幻题材作品，"
            "也是中国现代文学中最具批判力度的科幻小说。\n\n"
            "小说叙一架飞机坠毁火星，"
            "除「我」之外的同伴全部遇难。"
            "我被猫人捕获，在猫城生活了半年，"
            "目睹这个文明的全面溃烂：猫人以「迷叶」为食（一种麻醉性的植物），"
            "政治腐败、教育荒废、军人横行、学术造假，"
            "最终猫人被邻国灭绝，无一幸存。\n\n"
            "其想象力服务于批判。火星在此不是科学考察的对象，"
            "而是一个便于安放讽刺的异质空间——"
            "正因与现实保持距离，批判才得以彻底。"
            "这种「异星寓言」的写法，"
            "与斯威夫特《格列佛游记》一脉相承。\n\n"
            "老舍本人对这部作品评价不高，"
            "认为「写得不十分好」。"
            "但它是最早进入英语世界的中国科幻之一（1964 年有英译），"
            "在科幻史上的地位远超作者自评。"
            "本站归入科幻层。",
        },
        "en": {
            "title": "Cat Country",
            "body": "Lao She's 1932 novel, serialised in Les Contemporains and published in book form by the Modern Book Company in 1933. It is his only work of science fiction and the most searing SF novel of modern Chinese literature.\n\n"
            "An aircraft crashes on Mars; all aboard die but the narrator. Captured by the cat people, he lives half a year in Cat Country and witnesses a civilisation in total decay: the cats live on a narcotic leaf, their politics corrupt, their schools abandoned, soldiers rampaging, scholarship faked, until a neighbouring people exterminate them to the last.\n\n"
            "Its imagination serves critique. Mars is not an object of scientific enquiry but a heterogeneous space convenient for satire — precisely because it stands at a distance from reality, the criticism can be complete. This method of alien allegory descends from Swift's Gulliver's Travels.\n\n"
            "Lao She thought little of the book, judging it not very well written. Yet it was among the first Chinese science fiction works to reach English readers, in a 1964 translation, and its standing in the history of SF far exceeds its author's estimate. Filed as SF.",
        },
    },
    {
        "slug": "hepingdemeng",
        "era": "minguo",
        "kind": "sf",
        "year": 1940,
        "author": "顾均正",
        "authorSlug": "gujunzheng",
        "publisher": None,
        "coverCredit": "public-domain",
        "tags": ["科普", "战时", "短篇集"],
        "sources": ["《和平的梦》顾均正，文化生活出版社 1940"],
        "zh": {
            "title": "和平的梦",
            "body": "《和平的梦》是顾均正 1940 年出版的科幻短篇小说集，"
            "收入《和平的梦》《在北极底下》《伦敦奇疫》等篇。"
            "顾均正长期从事科普工作，主编过《科学趣味》等刊物，"
            "是中国现代科普事业的重要开拓者。\n\n"
            "其中《和平的梦》一篇最有代表性："
            "某国科学家发明了一种能远距离影响人脑电波的装置，"
            "通过它向敌国国民灌输「和平」的念头，"
            "企图不战而屈人之兵。"
            "小说围绕这一技术设想展开谍战情节，"
            "细节涉及无线电、脑电与心理学。\n\n"
            "其想象力特点是「技术设定先行」："
            "先提出一个可推演的科学设想，"
            "再据此构建情节冲突。"
            "这与凡尔纳式的「科普型科幻」一脉相承，"
            "也体现了科学救国思潮在文学中的投射。\n\n"
            "在战时语境下，这类作品既普及科学知识，"
            "也表达着对技术与国家命运的关切。"
            "本站归入科幻层，"
            "将其视为民国时期科普型科幻的代表。",
        },
        "en": {
            "title": "Dream of Peace",
            "body": "A 1940 collection of science fiction short stories by Gu Junzheng, including Dream of Peace, Beneath the North Pole and The Strange Pestilence of London. Gu worked for years in popular science and edited journals such as Scientific Interest; he was a pioneer of modern Chinese science popularisation.\n\n"
            "The title story is representative: scientists in one country devise an apparatus that influences the brain waves of people at a distance, using it to instil thoughts of peace in the citizens of an enemy state and to subdue them without battle. The plot runs as a spy thriller on this premise, with details drawn from radio, cerebral electricity and psychology.\n\n"
            "Its imagination puts the technical premise first: an extrapolable scientific idea is proposed, and the conflict is built from it. This descends from Vernean popular-science fiction and reflects the projection into literature of the movement to save the nation through science.\n\n"
            "In a wartime setting such writing spread scientific knowledge while voicing concern for technology and national fate. Filed as SF, as a representative of Republican-era popular-science science fiction.",
        },
    },
]

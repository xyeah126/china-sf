import { config, collection, fields, singleton } from '@keystatic/core';

/**
 * ⚠️ 重要约定（改动前请先读）
 *
 * 1. **slugField 必须配置，且指向 schema 里的 `fields.slug` 字段**：
 *    2026-09-05 实测发现，collection 若省略 slugField，Keystatic UI 打开条目时
 *    会在 getSlugFromState(collectionConfig, state) 里读 `collectionConfig.slugField`
 *    → `schema[undefined].kind` 崩溃（报错 "Cannot read properties of undefined
 *    (reading 'kind')"），所有条目都打不开。这是官方类型里 slugField 必填的原因。
 *    本站做法：把每个 collection 的「标题/姓名」字段（title / name / label）
 *    直接声明为 `fields.slug({ name: {...} })`：
 *    - **frontmatter 仍是纯字符串**：Keystatic 的 slugField 在序列化时走
 *      serializeWithSlug().value，只把 name 字符串写回原键（实测 342 文件
 *      往返零改动），`slug` 部分取自文件名、永不落盘 —— 不会像早期担心的
 *      那样注入 `slug: 刘慈欣` 之类的新键；
 *    - UI 里该字段会显示为「名称 + slug」两个输入框，slug 框预填文件名。
 *      改名（name）不会联动 slug（shouldGenerateSlug 仅新建条目时开启），
 *      保存不会意外重命名文件；不要点 Regenerate / 手改 slug，否则保存会
 *      按新 slug 移动文件（git mv）。
 *
 * 2. **schema 必须与 src/content.config.ts 一一对应**：Keystatic 保存时只回填
 *    schema 中存在的字段，缺失的键会被静默丢弃。新增 frontmatter 字段时两边要同步。
 *
 * 3. **正文走 body 而非 frontmatter**：每个 collection 都用
 *    `format: { contentField }` 把正文字段写到 `---` 之后的正文区，
 *    与 Astro 的 `render(entry)` 读 body 的行为一致。
 */

/** 时期：与 src/content/eras.yaml 的 id 严格一致 */
const ERAS = [
  { label: '上古 · 神话志怪 (shanggu)', value: 'shanggu' },
  { label: '宋元明清 · 前科幻 (song-ming-qing)', value: 'song-ming-qing' },
  { label: '晚清 · 科幻诞生 (wanqing)', value: 'wanqing' },
  { label: '民国 · 草创 (minguo)', value: 'minguo' },
  { label: '新中国 · 1949–1990 (xinzhongguo)', value: 'xinzhongguo' },
  { label: '当代 · 1990 至今 (dangdai)', value: 'dangdai' },
];

/** 图片来源分级：与 src/content.config.ts 的 credit 枚举一致 */
const CREDITS = [
  { label: '公有领域 public-domain', value: 'public-domain' },
  { label: '已授权 licensed', value: 'licensed' },
  { label: 'AI 生成 ai-generated', value: 'ai-generated' },
  { label: '占位图 placeholder', value: 'placeholder' },
];

/** 英文版翻译完整度 */
const TRANSLATIONS = [
  { label: '完整 full', value: 'full' },
  { label: '部分 partial', value: 'partial' },
  { label: '未译 none', value: 'none' },
];

/** 内容层级 */
const KINDS = [
  { label: '神话 myth', value: 'myth' },
  { label: '前科幻 proto-sf', value: 'proto-sf' },
  { label: '科幻 sf', value: 'sf' },
];

/** 改编类型 */
const ADAPT_TYPES = [
  { label: '电影 film', value: 'film' },
  { label: '剧集 tv', value: 'tv' },
  { label: '动画 animation', value: 'animation' },
  { label: '网络剧 web-series', value: 'web-series' },
  { label: '纪录片 documentary', value: 'documentary' },
  { label: '其他 other', value: 'other' },
];

/** 改编项目状态 */
const ADAPT_STATUS = [
  { label: '已上映 released', value: 'released' },
  { label: '待上映 upcoming', value: 'upcoming' },
  { label: '开发中 in-development', value: 'in-development' },
  { label: '已取消 cancelled', value: 'cancelled' },
];

/** 改编来源类型 */
const ADAPT_SOURCES = [
  { label: '改编自小说 novel', value: 'novel' },
  { label: '原创剧本 original', value: 'original' },
  { label: '改编自漫画 comic', value: 'comic' },
  { label: '改编自游戏 game', value: 'game' },
];

/** 文本数组字段的通用配置 */
const textArray = (label: string, itemLabel: string) =>
  fields.array(fields.text({ label: itemLabel }), {
    label,
    itemLabel: (props) => props.value || `新${itemLabel}`,
  });

/**
 * 正文（.md）字段 —— 使用官方 `fields.markdoc`，原生支持 `extension: 'md'`
 *
 * 背景：`fields.document` 已被上游废弃（源码注释：
 * `@deprecated fields.markdoc has superseded this field`），其 `contentExtension`
 * 硬编码为 `.mdoc`。本站 342 个内容文件全是 `.md`：
 *
 * 1. 若直接用 document，枚举过滤器
 *    `if (entry.children || !key.endsWith(extension)) continue;` 会把 `.md`
 *    全部静默丢弃 → 后台恒显示 0 entries；
 * 2. 早前用展开覆盖 `contentExtension` 的补丁虽让条目枚举出来，但 document
 *    的编辑器渲染链（DocumentFieldInput$1/DocumentEditor）打开条目时抛
 *    `Cannot read properties of undefined (reading 'kind')`；
 * 3. `fields.markdoc`（声明文件 markdoc/index.d.ts）允许
 *    `extension: 'mdoc' | 'md'`，编辑器走全新 EditorState 数据链
 *    （parse → ProseMirror EditorState → serialize）。
 *
 * 已用 markdoc 字段对全部 342 个文件做 parse + serialize 往返仿真：
 * 零异常，正文长度差 <1%，可直接替换。
 *
 * markdoc 的编辑器选项默认全开（粗体/斜体/删除线/行内代码/标题/引用/列表/
 * 链接/分割线/表格/代码块/图片），与旧 document 配置能力对齐且更全。
 */
type MarkdownFieldProps = {
  label: string;
  description?: string;
  formatting?: boolean;
  dividers?: boolean;
  links?: boolean;
};
const markdown = ({ label, description }: MarkdownFieldProps) =>
  fields.markdoc({ label, description, extension: 'md' });

/** 作品集：中英文目录共用同一套 schema，正文写到 body */
const worksSchema = {
  title: fields.slug({ name: { label: '标题', validation: { isRequired: true } } }),
  titleEn: fields.text({ label: '英文标题' }),
  subtitle: fields.text({ label: '副标题' }),
  author: fields.text({ label: '作者' }),
  authorSlug: fields.text({ label: '作者 slug（对应 authors 条目文件名）' }),
  year: fields.integer({ label: '年份' }),
  yearUncertain: fields.checkbox({ label: '年份不确定', defaultValue: false }),
  era: fields.select({ label: '所属时期', options: ERAS, defaultValue: 'dangdai' }),
  kind: fields.select({ label: '内容层级', options: KINDS, defaultValue: 'sf' }),
  publisher: fields.text({ label: '出版社 / 发表平台' }),
  publisherEn: fields.text({ label: '出版社英文名' }),
  cover: fields.text({ label: '封面路径（如 /covers/santi.webp）' }),
  coverCredit: fields.select({
    label: '封面来源分级',
    options: CREDITS,
    defaultValue: 'placeholder',
  }),
  coverSource: fields.text({ label: '封面来源说明' }),
  coverPrompt: fields.text({ label: 'AI 封面生成提示词', multiline: true }),
  tags: textArray('标签', '标签'),
  adaptations: textArray('改编条目 slug', '改编 slug'),
  sources: textArray('资料来源', '来源'),
  awards: textArray('获奖记录', '奖项'),
  featured: fields.checkbox({ label: '首页推荐', defaultValue: false }),
  translationStatus: fields.select({
    label: '英文版翻译状态',
    options: TRANSLATIONS,
    defaultValue: 'none',
  }),
  summary: markdown({
    label: '作品简介（正文）',
    formatting: true,
    dividers: true,
    links: true,
  }),
};

/** 作者集 */
const authorsSchema = {
  name: fields.slug({ name: { label: '姓名', validation: { isRequired: true } } }),
  nameEn: fields.text({ label: '英文名' }),
  alias: textArray('别名 / 笔名', '别名'),
  birthYear: fields.integer({ label: '出生年' }),
  deathYear: fields.integer({ label: '逝世年（在世请留空）' }),
  era: fields.select({ label: '所属时期', options: ERAS, defaultValue: 'dangdai' }),
  photo: fields.text({ label: '头像路径（全站零照片，一般留空）' }),
  photoCredit: fields.select({
    label: '图片来源分级',
    options: CREDITS,
    defaultValue: 'placeholder',
  }),
  photoSource: fields.text({ label: '图片来源说明' }),
  translationStatus: fields.select({
    label: '英文版翻译状态',
    options: TRANSLATIONS,
    defaultValue: 'none',
  }),
  awards: textArray('获奖记录', '奖项'),
  bio: markdown({
    label: '作者简介（正文）',
    formatting: true,
    dividers: true,
    links: true,
  }),
};

/** 影视改编集 */
const adaptationsSchema = {
  title: fields.slug({ name: { label: '标题', validation: { isRequired: true } } }),
  titleEn: fields.text({ label: '英文标题' }),
  year: fields.integer({ label: '年份' }),
  type: fields.select({ label: '类型', options: ADAPT_TYPES, defaultValue: 'film' }),
  status: fields.select({
    label: '项目状态',
    options: ADAPT_STATUS,
    defaultValue: 'released',
  }),
  sourceType: fields.select({
    label: '来源类型',
    options: ADAPT_SOURCES,
    defaultValue: 'novel',
  }),
  workSlug: fields.text({
    label: '原著作品 slug（仅当改编自本站收录作品时填写）',
  }),
  director: fields.text({ label: '导演' }),
  cast: textArray('主演', '演员'),
  studio: fields.text({ label: '出品方' }),
  platform: fields.text({ label: '播出 / 上映平台' }),
  doubanRating: fields.number({
    label: '豆瓣评分（静态快照，非实时）',
  }),
  doubanRatingAt: fields.text({ label: '评分抓取日期（YYYY-MM-DD）' }),
  doubanUrl: fields.text({ label: '豆瓣链接' }),
  poster: fields.text({ label: '海报路径' }),
  posterCredit: fields.select({
    label: '海报来源分级',
    options: CREDITS,
    defaultValue: 'placeholder',
  }),
  posterSource: fields.text({ label: '海报来源说明' }),
  awards: textArray('获奖记录', '奖项'),
  translationStatus: fields.select({
    label: '英文版翻译状态',
    options: TRANSLATIONS,
    defaultValue: 'none',
  }),
  summary: markdown({
    label: '改编简介（正文）',
    formatting: true,
    dividers: true,
    links: true,
  }),
};

/** 站点设置（singleton · data-yaml）：只放"站点身份"字段，UI 词留在 i18n/ui.ts */
const settingsSchema = {
  siteName: fields.text({ label: '站点名称' }),
  siteNameShort: fields.text({ label: '站点简称（页面标题后缀）' }),
  tagline: fields.text({ label: '口号 / 副标题' }),
  seoDescription: fields.text({
    label: '默认 SEO 描述（留空则用口号）',
    multiline: true,
  }),
  footerNote: fields.text({ label: '页脚附注（可留空）', multiline: true }),
};

/** 独立页面（About 等）：正文写 body */
const pagesSchema = {
  title: fields.slug({ name: { label: '页面标题', validation: { isRequired: true } } }),
  body: markdown({
    label: '页面内容（正文）',
    formatting: true,
    dividers: true,
    links: true,
  }),
};

/** 时期（每时期一个 yaml 文件，文件名 = era id，与 works.era 引用一致） */
const erasEntrySchema = {
  label: fields.slug({
    name: { label: '中文名', validation: { isRequired: true } },
  }),
  labelEn: fields.text({ label: '英文名' }),
  start: fields.integer({ label: '起始年（公元前用负数）' }),
  end: fields.integer({ label: '结束年（留空 = 延续至今）' }),
  kind: fields.text({ label: '内容层级（myth / proto-sf / sf）' }),
  summary: fields.text({ label: '中文简介', multiline: true }),
  summaryEn: fields.text({ label: '英文简介', multiline: true }),
};

/** 出版社 / 期刊（每条一个 yaml 文件，文件名 = id） */
const publishersEntrySchema = {
  name: fields.slug({
    name: { label: '名称', validation: { isRequired: true } },
  }),
  nameEn: fields.text({ label: '英文名' }),
  type: fields.select({
    label: '类型',
    options: [
      { label: '出版社 press', value: 'press' },
      { label: '杂志 magazine', value: 'magazine' },
      { label: '丛书 series', value: 'series' },
      { label: '平台 platform', value: 'platform' },
    ],
    defaultValue: 'press',
  }),
  founded: fields.integer({ label: '创办年' }),
  summary: fields.text({ label: '中文简介', multiline: true }),
  summaryEn: fields.text({ label: '英文简介', multiline: true }),
};

export default config({
  // 阶段 B：生产走 GitHub 存储（编辑直接提交到仓库）；本地开发如需 local 模式可临时改回
  storage: { kind: 'github', repo: 'xyeah126/china-sf' },
  ui: { brand: { name: '中国科幻作品网 · 内容管理', mark: 'C' } },

  singletons: {
    'settings-zh': singleton({
      label: '站点设置 · 中文',
      path: 'src/content/settings/zh',
      format: { data: 'yaml' },
      schema: settingsSchema,
    }),
    'settings-en': singleton({
      label: 'Site Settings · English',
      path: 'src/content/settings/en',
      format: { data: 'yaml' },
      schema: settingsSchema,
    }),
  },

  collections: {
    'works-zh': collection({
      label: '作品 · 中文',
      path: 'src/content/works/zh/*',
      format: { contentField: 'summary' },
      slugField: 'title',
      columns: ['title', 'author', 'year', 'era'],
      schema: worksSchema,
    }),
    'works-en': collection({
      label: '作品 · 英文',
      path: 'src/content/works/en/*',
      format: { contentField: 'summary' },
      slugField: 'title',
      columns: ['title', 'author', 'year', 'era'],
      schema: worksSchema,
    }),
    'authors-zh': collection({
      label: '作者 · 中文',
      path: 'src/content/authors/zh/*',
      format: { contentField: 'bio' },
      slugField: 'name',
      columns: ['name', 'era'],
      schema: authorsSchema,
    }),
    'authors-en': collection({
      label: '作者 · 英文',
      path: 'src/content/authors/en/*',
      format: { contentField: 'bio' },
      slugField: 'name',
      columns: ['name', 'era'],
      schema: authorsSchema,
    }),
    'adaptations-zh': collection({
      label: '影视改编 · 中文',
      path: 'src/content/adaptations/zh/*',
      format: { contentField: 'summary' },
      slugField: 'title',
      columns: ['title', 'year', 'type', 'status'],
      schema: adaptationsSchema,
    }),
    'adaptations-en': collection({
      label: '影视改编 · 英文',
      path: 'src/content/adaptations/en/*',
      format: { contentField: 'summary' },
      slugField: 'title',
      columns: ['title', 'year', 'type', 'status'],
      schema: adaptationsSchema,
    }),
    'eras': collection({
      label: '时期（时间线）',
      path: 'src/content/eras/*',
      format: { data: 'yaml' },
      slugField: 'label',
      columns: ['label', 'start', 'end', 'kind'],
      schema: erasEntrySchema,
    }),
    'publishers': collection({
      label: '出版社 · 期刊',
      path: 'src/content/publishers/*',
      format: { data: 'yaml' },
      slugField: 'name',
      columns: ['name', 'type', 'founded'],
      schema: publishersEntrySchema,
    }),
    'pages-zh': collection({
      label: '独立页面 · 中文',
      path: 'src/content/pages/zh/*',
      format: { contentField: 'body' },
      slugField: 'title',
      columns: ['title'],
      schema: pagesSchema,
    }),
    'pages-en': collection({
      label: '独立页面 · 英文',
      path: 'src/content/pages/en/*',
      format: { contentField: 'body' },
      slugField: 'title',
      columns: ['title'],
      schema: pagesSchema,
    }),
  },
});

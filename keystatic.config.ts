import { config, collection, fields } from '@keystatic/core';

/**
 * ⚠️ 重要约定（改动前请先读）
 *
 * 1. **不使用 slugField**：实测 Keystatic 的 `fields.slug({ name })` 会把「名字」
 *    以 `slug` 键写进 frontmatter（如 `slug: 刘慈欣`），而本站现有 340 个 md 文件
 *    都没有该键，一旦保存就会污染。去掉 slugField 后，Keystatic 仅用文件名作为
 *    条目标识，frontmatter 保持原样。新建条目时后台会直接要求输入文件名。
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

/** 作品集：中英文目录共用同一套 schema，正文写到 body */
const worksSchema = {
  title: fields.text({ label: '标题', validation: { isRequired: true } }),
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
  summary: fields.document({
    label: '作品简介（正文）',
    formatting: true,
    dividers: true,
    links: true,
  }),
};

/** 作者集 */
const authorsSchema = {
  name: fields.text({ label: '姓名', validation: { isRequired: true } }),
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
  bio: fields.document({
    label: '作者简介（正文）',
    formatting: true,
    dividers: true,
    links: true,
  }),
};

/** 影视改编集 */
const adaptationsSchema = {
  title: fields.text({ label: '标题', validation: { isRequired: true } }),
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
  summary: fields.document({
    label: '改编简介（正文）',
    formatting: true,
    dividers: true,
    links: true,
  }),
};

export default config({
  storage: { kind: 'local' },
  ui: { brand: { name: '中国科幻作品网 · 内容管理', mark: 'C' } },

  collections: {
    'works-zh': collection({
      label: '作品 · 中文',
      path: 'src/content/works/zh/*',
      format: { contentField: 'summary' },
      columns: ['title', 'author', 'year', 'era'],
      schema: worksSchema,
    }),
    'works-en': collection({
      label: '作品 · 英文',
      path: 'src/content/works/en/*',
      format: { contentField: 'summary' },
      columns: ['title', 'author', 'year', 'era'],
      schema: worksSchema,
    }),
    'authors-zh': collection({
      label: '作者 · 中文',
      path: 'src/content/authors/zh/*',
      format: { contentField: 'bio' },
      columns: ['name', 'era'],
      schema: authorsSchema,
    }),
    'authors-en': collection({
      label: '作者 · 英文',
      path: 'src/content/authors/en/*',
      format: { contentField: 'bio' },
      columns: ['name', 'era'],
      schema: authorsSchema,
    }),
    'adaptations-zh': collection({
      label: '影视改编 · 中文',
      path: 'src/content/adaptations/zh/*',
      format: { contentField: 'summary' },
      columns: ['title', 'year', 'type', 'status'],
      schema: adaptationsSchema,
    }),
    'adaptations-en': collection({
      label: '影视改编 · 英文',
      path: 'src/content/adaptations/en/*',
      format: { contentField: 'summary' },
      columns: ['title', 'year', 'type', 'status'],
      schema: adaptationsSchema,
    }),
  },
});

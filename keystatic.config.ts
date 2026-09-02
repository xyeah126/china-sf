import { config, collection, fields } from '@keystatic/core';

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

export default config({
  storage: { kind: 'local' },
  ui: { brand: { name: '中国科幻作品网 · 内容管理', mark: 'C' } },

  collections: {
    'authors-zh': collection({
      label: '作者 · 中文',
      path: 'src/content/authors/zh/*',
      slugField: 'slug',
      format: { contentField: 'bio' },
      columns: ['name', 'era'],
      schema: {
        slug: fields.slug({
          name: { label: '文件名 slug（拼音，改名会导致原 URL 失效）' },
        }),
        name: fields.text({ label: '姓名', validation: { isRequired: true } }),
        nameEn: fields.text({ label: '英文名' }),
        alias: fields.array(fields.text({ label: '别名' }), {
          label: '别名 / 笔名',
          itemLabel: (props) => props.value || '新别名',
        }),
        birthYear: fields.integer({ label: '出生年' }),
        deathYear: fields.integer({ label: '逝世年（在世请留空）' }),
        era: fields.select({
          label: '所属时期',
          options: ERAS,
          defaultValue: 'dangdai',
        }),
        photo: fields.text({ label: '头像路径（全站零照片，一般留空）' }),
        photoCredit: fields.select({
          label: '图片来源分级',
          options: CREDITS,
          defaultValue: 'placeholder',
        }),
        translationStatus: fields.select({
          label: '英文版翻译状态',
          options: TRANSLATIONS,
          defaultValue: 'none',
        }),
        awards: fields.array(fields.text({ label: '奖项' }), {
          label: '获奖记录',
          itemLabel: (props) => props.value || '新奖项',
        }),
        bio: fields.document({
          label: '作者简介（正文）',
          formatting: true,
          dividers: true,
          links: true,
        }),
      },
    }),
  },
});

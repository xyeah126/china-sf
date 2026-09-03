import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

/** 图片来源分级：公有领域 / 已授权 / AI 生成 / 占位图 */
const credit = z.enum(['public-domain', 'licensed', 'ai-generated', 'placeholder']);
/** 翻译完整度 */
const translation = z.enum(['full', 'partial', 'none']);
/** 内容层级 */
const kind = z.enum(['myth', 'proto-sf', 'sf']);

/**
 * 作品集：内容按语言分目录（works/zh/*.md、works/en/*.md），
 * glob loader 生成的 id 形如 "zh/santi"、"en/santi"。
 */
const works = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/works' }),
  schema: z.object({
    title: z.string(),
    titleEn: z.string().optional(),
    subtitle: z.string().optional(),
    author: z.string().nullable().default(null),
    authorSlug: z.string().optional(),
    year: z.number().nullable().default(null),
    yearUncertain: z.boolean().default(false),
    era: z.string(),
    kind,
    publisher: z.string().optional(),
    publisherEn: z.string().optional(),
    cover: z.string().optional(),
    coverCredit: credit.default('placeholder'),
    coverSource: z.string().optional(),
    coverPrompt: z.string().optional(),
    tags: z.array(z.string()).default([]),
    adaptations: z.array(z.string()).default([]),
    sources: z.array(z.string()).default([]),
    awards: z.array(z.string()).default([]),
    featured: z.boolean().default(false),
    translationStatus: translation.default('none'),
  }),
});

const authors = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/authors' }),
  schema: z.object({
    name: z.string(),
    nameEn: z.string().optional(),
    alias: z.array(z.string()).default([]),
    birthYear: z.number().nullable().default(null),
    deathYear: z.number().nullable().default(null),
    era: z.string(),
    photo: z.string().optional(),
    photoCredit: credit.default('placeholder'),
    photoSource: z.string().optional(),
    translationStatus: translation.default('none'),
    awards: z.array(z.string()).default([]),
  }),
});

const adaptations = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/adaptations' }),
  schema: z.object({
    title: z.string(),
    titleEn: z.string().optional(),
    year: z.number().nullable().default(null),
    type: z.enum(['film', 'tv', 'animation', 'web-series', 'documentary', 'other']),
    status: z
      .enum(['released', 'upcoming', 'in-development', 'cancelled'])
      .default('released'),
    // 原著作品 slug：仅当改编自本站收录的文学作品时填写（原创剧本等可留空）
    workSlug: z.string().optional(),
    // 来源类型：改编自小说 / 原创剧本 / 改编自漫画 / 改编自游戏
    sourceType: z.enum(['novel', 'original', 'comic', 'game']).default('novel'),
    director: z.string().optional(),
    cast: z.array(z.string()).default([]),   // 主演
    studio: z.string().optional(),
    platform: z.string().optional(),
    // 豆瓣评分：静态快照，非实时同步；需同时给出抓取日期与来源链接
    doubanRating: z.number().nullable().default(null),
    doubanRatingAt: z.string().optional(),
    doubanUrl: z.string().optional(),
    poster: z.string().optional(),
    posterCredit: credit.default('placeholder'),
    posterSource: z.string().optional(),
    awards: z.array(z.string()).default([]),
    translationStatus: translation.default('none'),
  }),
});

/** 时期节点：不随语言拆分，条目内自带 label / labelEn。
 *  每时期一个 yaml 文件（src/content/eras/<id>.yaml），id = 文件名（glob loader 生成）。
 *  约定：end 键缺省 = 延续至今。 */
const eras = defineCollection({
  loader: glob({ pattern: '*.yaml', base: './src/content/eras' }),
  schema: z.object({
    label: z.string(),
    labelEn: z.string().optional(),
    start: z.number(),
    end: z.number().nullable().default(null),
    kind,
    summary: z.string().optional(),
    summaryEn: z.string().optional(),
  }),
});

const publishers = defineCollection({
  loader: glob({ pattern: '*.yaml', base: './src/content/publishers' }),
  schema: z.object({
    name: z.string(),
    nameEn: z.string().optional(),
    type: z.enum(['press', 'magazine', 'series', 'platform']).default('press'),
    founded: z.number().nullable().default(null),
    logo: z.string().optional(),
    logoCredit: credit.default('placeholder'),
    summary: z.string().optional(),
    summaryEn: z.string().optional(),
  }),
});

/** 站点设置（zh.yaml / en.yaml，id = 语言）：站点身份字段，UI 词仍在 i18n/ui.ts */
const settings = defineCollection({
  loader: glob({ pattern: '*.yaml', base: './src/content/settings' }),
  schema: z.object({
    siteName: z.string().optional(),
    siteNameShort: z.string().optional(),
    tagline: z.string().optional(),
    seoDescription: z.string().optional(),
    footerNote: z.string().optional(),
  }),
});

/** 独立页面（about 等），id = 文件名 */
const pagesSchema = z.object({ title: z.string() });
const pagesZh = defineCollection({
  loader: glob({ pattern: '*.md', base: './src/content/pages/zh' }),
  schema: pagesSchema,
});
const pagesEn = defineCollection({
  loader: glob({ pattern: '*.md', base: './src/content/pages/en' }),
  schema: pagesSchema,
});

export const collections = {
  works,
  authors,
  adaptations,
  eras,
  publishers,
  settings,
  'pages-zh': pagesZh,
  'pages-en': pagesEn,
};

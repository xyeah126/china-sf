import { getCollection, getEntry } from 'astro:content';
import type { CollectionEntry } from 'astro:content';
import type { Lang } from '../i18n/ui';

export type WorkEntry = CollectionEntry<'works'>;
export type AuthorEntry = CollectionEntry<'authors'>;
export type AdaptationEntry = CollectionEntry<'adaptations'>;
export type EraEntry = CollectionEntry<'eras'>;
export type PublisherEntry = CollectionEntry<'publishers'>;

/** glob loader 的 id 形如 "zh/santi"，拆出语言与 slug */
function splitId(id: string): { lang: string; slug: string } {
  const idx = id.indexOf('/');
  if (idx === -1) return { lang: 'zh', slug: id };
  return { lang: id.slice(0, idx), slug: id.slice(idx + 1) };
}

/**
 * 取双语条目：优先取目标语言版本，缺失则回退到中文，并标记 isFallback。
 * 绝不返回 404，也绝不用机翻填充。
 */
function pick<T extends CollectionEntry<string>>(
  rec: Record<string, T | undefined>,
  lang: Lang,
): { entry: T; isFallback: boolean } | null {
  const preferred = lang === 'en' ? rec.en : rec.zh;
  if (preferred) return { entry: preferred, isFallback: false };
  if (rec.zh) return { entry: rec.zh, isFallback: true };
  return null;
}

function sortByYear<T extends { data: { year?: number | null } }>(a: T, b: T): number {
  return (a.data.year ?? 0) - (b.data.year ?? 0);
}

/** 作品列表（按年份正序） */
export async function getWorks(lang: Lang) {
  const all = await getCollection('works');
  const bySlug = new Map<string, Record<string, WorkEntry | undefined>>();

  for (const e of all) {
    const { lang: l, slug } = splitId(e.id);
    const rec = bySlug.get(slug) ?? {};
    rec[l] = e;
    bySlug.set(slug, rec);
  }

  const out: { entry: WorkEntry; slug: string; isFallback: boolean }[] = [];
  for (const [slug, rec] of bySlug) {
    const hit = pick(rec, lang);
    if (hit) out.push({ entry: hit.entry, slug, isFallback: hit.isFallback });
  }
  return out.sort((a, b) => sortByYear(a.entry, b.entry));
}

/** 单个作品（含回退） */
export async function getWork(slug: string, lang: Lang) {
  const target = await getEntry('works', `${lang}/${slug}`);
  if (target) return { entry: target, isFallback: false };
  const zh = await getEntry('works', `zh/${slug}`);
  if (zh) return { entry: zh, isFallback: true };
  return null;
}

/** 作者（含回退） */
export async function getAuthor(slug: string, lang: Lang) {
  const target = await getEntry('authors', `${lang}/${slug}`);
  if (target) return { entry: target, isFallback: false };
  const zh = await getEntry('authors', `zh/${slug}`);
  if (zh) return { entry: zh, isFallback: true };
  return null;
}

/** 某作品的影视改编（按年份正序） */
export async function getAdaptationsFor(workSlug: string, lang: Lang) {
  const all = await getCollection('adaptations');
  const bySlug = new Map<string, Record<string, AdaptationEntry | undefined>>();

  for (const a of all) {
    if (a.data.workSlug !== workSlug) continue;
    const { lang: l, slug } = splitId(a.id);
    const rec = bySlug.get(slug) ?? {};
    rec[l] = a;
    bySlug.set(slug, rec);
  }

  const out: AdaptationEntry[] = [];
  for (const [, rec] of bySlug) {
    const hit = pick(rec, lang);
    if (hit) out.push(hit.entry);
  }
  return out.sort(sortByYear);
}

/** 时期节点（按起始年正序） */
export async function getEras(): Promise<EraEntry[]> {
  const eras = await getCollection('eras');
  return eras.sort((a, b) => a.data.start - b.data.start);
}

/** 把作品按时期分组，用于时间线 */
export async function getWorksByEra(lang: Lang) {
  const eras = await getEras();
  const works = await getWorks(lang);

  return eras.map((era) => ({
    era,
    works: works.filter((w) => w.entry.data.era === era.id),
  }));
}

/** 年份格式化：公元前写"前 X" / "X BCE"，未定为"年代不详" / "undated" */
export function fmtYear(n: number | null | undefined, lang: Lang): string {
  if (n === null || n === undefined) return lang === 'zh' ? '年代不详' : 'undated';
  if (n < 0) return lang === 'zh' ? `前 ${-n}` : `${-n} BCE`;
  return String(n);
}

/** 时期区间文本，如 "960 – 1840"、"1840 – 今"。
 *  约定：end 为 null/undefined（含 YAML 中省略 end 键）均表示"延续至今"。 */
export function fmtEraRange(start: number, end: number | null | undefined, lang: Lang): string {
  const s = fmtYear(start, lang);
  const e = end == null ? (lang === 'zh' ? '今' : 'present') : fmtYear(end, lang);
  return `${s} – ${e}`;
}

/** 作者列表（按生年正序，生年不详者排最后） */
export async function getAuthors(lang: Lang) {
  const all = await getCollection('authors');
  const bySlug = new Map<string, Record<string, AuthorEntry | undefined>>();

  for (const e of all) {
    const { lang: l, slug } = splitId(e.id);
    const rec = bySlug.get(slug) ?? {};
    rec[l] = e;
    bySlug.set(slug, rec);
  }

  const out: { entry: AuthorEntry; slug: string; isFallback: boolean }[] = [];
  for (const [slug, rec] of bySlug) {
    const hit = pick(rec, lang);
    if (hit) out.push({ entry: hit.entry, slug, isFallback: hit.isFallback });
  }
  return out.sort(
    (a, b) => (a.entry.data.birthYear ?? 9999) - (b.entry.data.birthYear ?? 9999),
  );
}

/** 某位作者的全部作品 */
export async function getWorksByAuthor(authorSlug: string, lang: Lang) {
  const works = await getWorks(lang);
  return works.filter((w) => w.entry.data.authorSlug === authorSlug);
}

/** 影视改编全列表（按年份正序，未定档者排最后） */
export async function getAdaptations(lang: Lang) {
  const all = await getCollection('adaptations');
  const bySlug = new Map<string, Record<string, AdaptationEntry | undefined>>();

  for (const e of all) {
    const { lang: l, slug } = splitId(e.id);
    const rec = bySlug.get(slug) ?? {};
    rec[l] = e;
    bySlug.set(slug, rec);
  }

  const out: { entry: AdaptationEntry; slug: string }[] = [];
  for (const [slug, rec] of bySlug) {
    const hit = pick(rec, lang);
    if (hit) out.push({ entry: hit.entry, slug });
  }
  return out.sort((a, b) => (a.entry.data.year ?? 9999) - (b.entry.data.year ?? 9999));
}

/** 出版社·期刊全列表（按创办年正序，缺失者排最后） */
export async function getPublishers(): Promise<PublisherEntry[]> {
  const all = await getCollection('publishers');
  return all.sort((a, b) => (a.data.founded ?? 9999) - (b.data.founded ?? 9999));
}

/**
 * 把连续汉字逐个用空格拆开（非汉字片段原样保留、以空格隔开），用于给
 * pagefind 注入"单字可检索"的索引文本。例：「狩猎愉快」→「狩 猎 愉 快」。
 *
 * 背景：pagefind 对中文按词（jieba）分词建索引，单字如「猎」若不在词表
 * 边界内则搜不到；空格分隔会让 pagefind 把每个汉字当作独立词索引。
 */
export function splitHanziSpaced(text: string): string {
  const HANZI = /[\u3400-\u9fff\uf900-\ufaff]/;
  let out = '';
  for (const ch of text) {
    out += HANZI.test(ch) ? `${ch} ` : ch;
  }
  return out.replace(/\s+/g, ' ').trim();
}

/** 从奖项条目字符串中提取 4 位年份（取第一个匹配），无则 null */
function awardYear(text: string): number | null {
  const m = text.match(/(?:19|20)\d{2}/);
  return m ? Number(m[0]) : null;
}

/**
 * 奖项时间线排序：
 *  - 无法解析出年份的条目（泛称/描述，如「中国科幻银河奖」）保持原相对顺序，统一排在前面；
 *  - 能解析出年份的按年份升序排列（同年按原顺序稳定排列）。
 * 这样作品/作者页的获奖时间线不再随 frontmatter 手写顺序错乱。
 */
export function sortAwards(awards: string[]): string[] {
  const generic: { text: string; order: number }[] = [];
  const dated: { text: string; year: number; order: number }[] = [];
  awards.forEach((text, order) => {
    const y = awardYear(text);
    if (y == null) generic.push({ text, order });
    else dated.push({ text, year: y, order });
  });
  generic.sort((a, b) => a.order - b.order);
  dated.sort((a, b) => a.year - b.year || a.order - b.order);
  return [...generic.map((x) => x.text), ...dated.map((x) => x.text)];
}

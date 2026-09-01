import type { APIRoute } from 'astro';
import { getWorks, getAuthors, getPublishers } from '../lib/content';

/**
 * 双语 sitemap.xml：每个 URL 条目互标 hreflang（zh-CN / en / x-default）
 * 中文站根路径 /，英文站 /en/
 */
const STATIC_PATHS = [
  '/',
  '/timeline',
  '/works',
  '/authors',
  '/adaptations',
  '/publishers',
  '/about',
  '/search',
];

function xmlEscape(s: string): string {
  return s
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;');
}

export const GET: APIRoute = async ({ site }) => {
  const base = (site ?? new URL('https://chinese-sf.example.com')).href.replace(/\/$/, '');

  const [zhWorks, enWorks, zhAuthors, enAuthors, publishers] = await Promise.all([
    getWorks('zh'),
    getWorks('en'),
    getAuthors('zh'),
    getAuthors('en'),
    getPublishers(),
  ]);

  // 收集全部路径（slug 双语一致，直接合并去重）
  const paths = new Set<string>(STATIC_PATHS);
  for (const w of zhWorks) paths.add(`/works/${w.slug}`);
  for (const w of enWorks) paths.add(`/works/${w.slug}`);
  for (const a of zhAuthors) paths.add(`/authors/${a.slug}`);
  for (const a of enAuthors) paths.add(`/authors/${a.slug}`);
  for (const p of publishers) paths.add(`/publishers/${p.slug}`);

  const entries = [...paths]
    .sort()
    .map((p) => {
      const zhUrl = `${base}${p === '/' ? '/' : p}`;
      const enUrl = `${base}/en${p === '/' ? '/' : p}`;
      return `  <url>
    <loc>${xmlEscape(zhUrl)}</loc>
    <xhtml:link rel="alternate" hreflang="zh-CN" href="${xmlEscape(zhUrl)}"/>
    <xhtml:link rel="alternate" hreflang="en" href="${xmlEscape(enUrl)}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="${xmlEscape(zhUrl)}"/>
  </url>`;
    })
    .join('\n');

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
${entries}
</urlset>`;

  return new Response(xml, {
    headers: { 'Content-Type': 'application/xml; charset=utf-8' },
  });
};

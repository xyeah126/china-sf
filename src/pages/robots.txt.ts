import type { APIRoute } from 'astro';

/**
 * 动态 robots.txt —— Sitemap 地址自动跟随 astro.config 的 site，
 * 部署换域名时无需手动同步。
 */
export const GET: APIRoute = async ({ site }) => {
  const base = (site ?? new URL('https://china-sf.example.com')).href.replace(/\/$/, '');
  const body = `User-agent: *
Allow: /

Sitemap: ${base}/sitemap.xml
`;
  return new Response(body, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
};

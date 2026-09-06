import type { MiddlewareHandler } from 'astro';

/**
 * Keystatic 在 Cloudflare Workers 上的「写入补丁」
 *
 * 背景（2026-09-06 排查）：
 * 1. Keystatic 保存条目的写入路径有两条（@keystatic/core 0.6.9）：
 *    - GitHub App 模式：浏览器用 GraphQL createCommitOnBranch 直连 GitHub；
 *    - 其余情况（本项目：OAuth App + 用户 token 有写权限）：
 *      `POST /api/keystatic/update` → 服务端 API 路由。
 * 2. 但 @keystatic/core 的 **worker 版** API handler
 *    （dist/keystatic-core-api-generic.worker.js）只实现了 OAuth 相关路由
 *    （github/login、github/oauth/callback、github/refresh-token、github/logout、
 *    github/repo-not-found、github/created-app），其余一律 404 Not Found；
 *    `tree` / `update` / `blob` 三个数据路由只存在于 **node 版**（且仅服务
 *    `storage: { kind: 'local' }`）。
 *    → 部署到 Workers 后，后台能登录、能浏览，但点保存必然 404。
 * 3. 这里用 Astro middleware 补上 `POST /api/keystatic/update`：
 *    用 Keystatic 写在 cookie 里的 access token（非 httpOnly，明文）调
 *    GitHub Git Data API 完成提交，协议与 Keystatic 前端期望完全一致：
 *      请求  POST，headers: { 'no-cors': '1' }
 *            body: { additions: [{path, contents(base64)}], deletions: [{path}] }
 *      响应  tree entries 数组（每项含 path/mode/sha/type），
 *            前端用它算 tree sha 做后续冲突检测。
 *    之所以用 middleware 而不是 src/pages/api/keystatic/update.ts，是为了避免与
 *    Keystatic 集成注入的 `/api/keystatic/[...path]` 通配路由冲突。
 *
 * 安全：
 * - 无 access token 直接 401；token 本身由 GitHub 校验。
 * - 只接受 `no-cors: 1` 自定义头（Keystatic 前端固定带），跨站脚本无法静默构造。
 * - 路径白名单：只允许 src/content/** 与 public/**，拒绝 `..`、绝对路径、反斜杠。
 * - SameSite=Lax 的 cookie 不会随跨站 POST 发送。
 */

const REPO = 'xyeah126/china-sf';
const GH = 'https://api.github.com';
const ALLOWED_PREFIXES = ['src/content/', 'public/'];

const txt = (body: string, status: number) => new Response(body, { status });
const json = (body: unknown) =>
  new Response(JSON.stringify(body), {
    status: 200,
    headers: { 'content-type': 'application/json' },
  });

function readAccessToken(req: Request): string | null {
  const raw = req.headers.get('cookie') || '';
  const m = /(?:^|;\s*)keystatic-gh-access-token=([^;]+)/.exec(raw);
  return m ? decodeURIComponent(m[1]) : null;
}

/** 路径白名单校验：防目录穿越、防写仓库任意文件 */
function isPathAllowed(p: unknown): p is string {
  if (typeof p !== 'string' || !p) return false;
  if (p.includes('\\') || p.startsWith('/') || p.includes('..')) return false;
  if (/^[a-zA-Z]:/.test(p)) return false;
  return ALLOWED_PREFIXES.some((prefix) => p.startsWith(prefix));
}

async function gh<T = any>(token: string, path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${GH}${path}`, {
    ...init,
    headers: {
      Authorization: `Bearer ${token}`,
      Accept: 'application/vnd.github+json',
      'User-Agent': 'china-sf-keystatic-update',
      ...(init?.headers ?? {}),
    },
  });
  if (!res.ok) {
    const detail = (await res.text().catch(() => '')).slice(0, 300);
    throw new Error(`GitHub ${init?.method ?? 'GET'} ${path} → ${res.status} ${detail}`);
  }
  return res.json() as Promise<T>;
}

async function handleUpdate(req: Request): Promise<Response> {
  if (req.headers.get('no-cors') !== '1') return txt('Bad Request', 400);

  const token = readAccessToken(req);
  if (!token) return txt('Not authenticated with GitHub', 401);

  let body: { additions?: { path: string; contents: string }[]; deletions?: { path: string }[] };
  try {
    body = await req.json();
  } catch {
    return txt('Bad JSON', 400);
  }
  const additions = (body.additions ?? []).filter((x) => x && x.path);
  const deletions = (body.deletions ?? []).filter((x) => x && x.path);

  for (const f of [...additions, ...deletions]) {
    if (!isPathAllowed(f.path)) return txt(`Path not allowed: ${String(f.path)}`, 400);
  }
  if (additions.some((a) => typeof a.contents !== 'string')) {
    return txt('Missing file contents', 400);
  }
  if (!additions.length && !deletions.length) return txt('Nothing to update', 400);

  try {
    // 1. 默认分支
    const repo = await gh<{ default_branch: string }>(token, `/repos/${REPO}`);
    const branch = repo.default_branch || 'master';
    // 2. 分支当前 commit
    const ref = await gh<{ object: { sha: string } }>(
      token,
      `/repos/${REPO}/git/ref/heads/${branch}`
    );
    const baseCommit = ref.object.sha;
    // 3. 该 commit 的 tree
    const commit = await gh<{ tree: { sha: string } }>(
      token,
      `/repos/${REPO}/git/commits/${baseCommit}`
    );
    // 4. 新增文件 → blob（内容已是 base64）；删除文件 → sha: null
    const tree: { path: string; mode: string; type: string; sha: string | null }[] = [];
    for (const a of additions) {
      const blob = await gh<{ sha: string }>(token, `/repos/${REPO}/git/blobs`, {
        method: 'POST',
        headers: { 'content-type': 'application/json' },
        body: JSON.stringify({ content: a.contents, encoding: 'base64' }),
      });
      tree.push({ path: a.path, mode: '100644', type: 'blob', sha: blob.sha });
    }
    for (const d of deletions) {
      tree.push({ path: d.path, mode: '100644', type: 'blob', sha: null });
    }
    // 5. 新 tree（基于 base_tree 增量）
    const newTree = await gh<{ sha: string }>(token, `/repos/${REPO}/git/trees`, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ base_tree: commit.tree.sha, tree }),
    });
    // 6. 新 commit
    const newCommit = await gh<{ sha: string }>(token, `/repos/${REPO}/git/commits`, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({
        message: 'Update content via Keystatic',
        tree: newTree.sha,
        parents: [baseCommit],
      }),
    });
    // 7. 移动分支指针
    await gh(token, `/repos/${REPO}/git/refs/heads/${branch}`, {
      method: 'PATCH',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ sha: newCommit.sha }),
    });
    // 8. 回传完整 tree entries（Keystatic 前端据此重建树缓存）
    const full = await gh<{ tree: unknown[] }>(
      token,
      `/repos/${REPO}/git/trees/${newCommit.sha}?recursive=1`
    );
    return json(full.tree ?? []);
  } catch (err) {
    return txt(`Keystatic update failed: ${(err as Error).message}`, 500);
  }
}

export const onRequest: MiddlewareHandler = async (context, next) => {
  const { request } = context;
  if (request.method !== 'POST') return next();
  try {
    if (new URL(request.url).pathname !== '/api/keystatic/update') return next();
  } catch {
    return next();
  }
  return handleUpdate(request);
};

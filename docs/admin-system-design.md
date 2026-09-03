# 内容管理系统架构决策文档

> 定稿：2026-09-03。本文档记录 china-sf 站点 CMS 方案的选型依据、当前状态与后续路线。
> 操作层面的踩坑细节已沉淀到 WorkBuddy skill `astro-keystatic-setup`，本文不重复。

## 1. 背景与需求

- 站点：Astro 7 纯静态站，约 295 页（作品 / 作者 / 影视改编 × 中英双语），内容为
  `src/content/{works,authors,adaptations}/{zh,en}/*.md`，共 340 篇，全部有正文
- 需求：一个可视化后台管理 340 篇 md 的增删改，单人使用，**成本 $0**
- 约束：正文渲染走 Astro 的 `render(entry)`（读 frontmatter 之后的 body），
  任何方案都不得把正文写进 frontmatter

## 2. 选型结论：Keystatic（方案 B）

| 候选 | 结论 | 理由 |
|---|---|---|
| **Keystatic** | ✅ 采用 | MIT 免费；`contentField` 原生支持「正文写 body」；schema 与 Astro content collections 对齐最好；本地 API 可脱离 GitHub 直接读写文件 |
| Sveltia CMS | 备选 | MIT 完全免费、i18n 强、浏览器端 SPA 无需 adapter；但试装后放弃——Keystatic 的本地 CRUD 更贴合"先本地跑通再上远程"的路线（试装包已删） |
| Decap CMS | ❌ | 免费但维护基本停滞 |
| TinaCMS | ❌ | 云服务依赖重 |
| Astro SSR + DB | ❌ | 引入数据库，运维成本与需求不匹配 |

费用核实（2026-09）：Keystatic 本体 MIT，local / GitHub 模式均 $0；
唯一付费项 Keystatic Cloud（非技术编辑免 GitHub 登录）用不到。
真实成本只有可选的域名（约 ¥70–100/年）。

## 3. 架构

```
本地开发                          生产（Cloudflare Workers）
┌─────────────────────┐          ┌──────────────────────────────┐
│ astro dev            │          │ 静态资产 (dist/client) → CDN  │
│  storage: local      │          │ /keystatic + /api/keystatic  │
│  API 直读/直写本地 md │          │   → Worker (SSR)             │
│  无需网络            │          │   storage: github 模式        │
└─────────────────────┘          │   → GitHub App 读写仓库        │
                                 └──────────────────────────────┘
```

- `output: 'static'`：295 页全部预渲染走 CDN，只有 Keystatic 路由走 Worker（省请求额度）
- adapter **仅在 build 时挂载**（`process.argv.includes('build')`）——
  dev 下挂载会把 Keystatic API 弄 500（见 skill 坑 10）
- 内容流：Keystatic 编辑 → GitHub 提交 → Workers Builds 自动构建部署

## 4. 数据安全（本项目最关键的设计决策）

**存量 340 篇 md 是不可再生的数据，所有配置以"不污染、不丢字段"为第一原则：**

1. **不配 `slugField`**：实测配了会在每次保存时往 frontmatter 写 `slug: 刘慈欣`
   （存的是名字），而现有文件均无此键（skill 坑 6）
2. **schema 必须是现有 frontmatter 键的父集**：Keystatic 只回填 schema 里有的字段，
   缺的键保存时静默丢弃。已统计 6 个目录的键集合并与 `src/content.config.ts` 一一对应
3. **正文走 `format: { contentField }`** 写入 body，与 `render(entry)` 一致
4. 验证方法：从 Keystatic bundle 抽出真实 `serializeEntryToFiles` 在 Node 里跑
   往返（`--conditions=browser`），无需浏览器自动化

## 5. 当前状态（2026-09-03）

✅ 已完成：
- Keystatic 6 个 collection（works/authors/adaptations × zh/en），本地 CRUD 闭环验证
- GitHub 仓库 https://github.com/xyeah126/china-sf（公开，master）
- `@astrojs/cloudflare` 14.3.0 + astro 7.3.0（含两个上游 bug 的修复，见 skill 坑 8/9）
- `wrangler.jsonc`（nodejs_compat）；pagefind 索引路径 `dist/client`
- **生产产物本地端到端验证通过**（wrangler dev）：静态页 / /keystatic(SSR) /
  pagefind / 静态资源全 200；`npm run build` exit=0

⏳ 待办（按顺序）：
1. **部署**：需要 Cloudflare 账号授权（API token 或 dashboard 连仓库），
   部署时需创建 KV namespace `SESSION`
2. **阶段 B — 切 GitHub 模式**：部署拿到正式域名后，访问 `/keystatic` →
   点 GitHub 登录 → Keystatic 自带「Create GitHub App」引导（自动生成
   `KEYSTATIC_GITHUB_CLIENT_ID/SECRET`、`KEYSTATIC_SECRET`），
   `keystatic.config.ts` 的 storage 改 `kind: 'github', repo: 'xyeah126/china-sf'`，
   四个变量配到 Cloudflare 环境变量面板
3. 可选：自定义域名；正文字段升级为富文本编辑体验调优

## 6. 部署配置速查

- 构建命令（CI）：`npm run build`（= astro build + pagefind --site dist/client）
- 部署命令：`npx wrangler deploy`
- 本地预览生产产物：`npm run preview`（wrangler dev --config dist/server/wrangler.json）
- 产物结构：`dist/client/`（静态，含 pagefind）+ `dist/server/`（worker 入口，
  内含部署用 wrangler.json，assets 指向 ../client）

# 收尾操作手册（2026-09-04 20:15 更新：任务 A 已完成，只剩任务 B）

> ## ✅ 任务 A 已完成（2026-09-04 20:12，用户实测验收）
> - 后台 GitHub 登录成功 → App 已安装在 china-sf 仓库
> - 在线编辑验收：改「页脚附注」为「科幻无垠」→ 保存 → 仓库出现 Verified 提交
>   **`e77b6a6` Update src/content/settings/zh**（已本地 pull 同步）
> - 提交质量：Keystatic 只动了目标字段，顺带清掉空值键，格式 diff 极小（探针预重写生效）
> - **阶段 B（CMS 远程编辑）至此全部打通** ✅

> 当前状态：站点在线 ✅ | Worker 已配 3 个 secret ✅ | GitHub App 已创建并安装 ✅
> **只剩一件事：任务 B（Workers Builds 自动部署），约 5 分钟，只需浏览器。**

---

## 任务 B：Workers Builds 自动部署（内容提交 → 自动上线）

**背景**：你的 GitHub token 没有 `workflow` scope，GitHub Actions 方案推不上去（已实测被拒）。所以用 Cloudflare 自带的 **Workers Builds**：在 Dashboard 里连上 GitHub 仓库，每次 push 自动构建 + 部署，**不需要任何额外 token**。

### B1. 进入 Worker 的构建设置

1. 开代理打开 👉 **https://dash.cloudflare.com/06352f451bff9442c9b02e47b9d55a14/workers/services/view/china-sf/production**
2. 点 **Settings**（设置）→ 找到 **Build** 区域 → 点 **Connect** / **Connect Git repository**
   （不同版本界面叫法可能是「Builds」标签页 → Set up builds）

### B2. 授权 Cloudflare 访问 GitHub

1. 选择 **GitHub** → 跳转 GitHub 授权页
2. 仓库权限选 **Only select repositories** → 选 `china-sf` → **Install & Authorize**
   （如果之前已经授权过 Cloudflare，直接在列表里勾选即可）

### B3. 构建配置（照抄这张表）

| 配置项 | 填什么 |
|---|---|
| Repository | `xyeah126/china-sf` |
| Production branch | `master`（⚠️ 是 master 不是 main） |
| Build command | `npm run build` |
| Deploy command | `npx wrangler deploy` |
| Root directory | 留空（或 `/`） |
| **Build variables** | 见下方 ⚠️ |

**⚠️ 必须加的构建变量（Build variables，不是 Secrets）**：

| 变量名 | 值 | 为什么 |
|---|---|---|
| `PUBLIC_KEYSTATIC_GITHUB_APP_SLUG` | `xyeah126-keystatic` | `PUBLIC_` 前缀变量在构建时被 Vite **内联**进 JS，配成运行时 secret 无效。漏了的话，自动部署出来的后台会丢「App 安装引导」链接 |
| `NODE_VERSION` | `22` | 可选。仅当构建报 Node 版本相关错误时加 |

### B4. 保存并跑首次构建

1. 点 **Save**（或 Save and Deploy）→ 自动触发首次构建
2. 等 3~5 分钟，在 **Builds / Deployments** 页看状态，绿勾即成功
3. 验证线上还是好的：打开 `https://china-sf.xyeah126.workers.dev/` 应正常

### B5. 闭环验证（整套系统验收）

1. 后台 `/keystatic` 改一处内容保存 → GitHub 出现新 commit
2. Workers Builds 自动检测到 push → 自动构建（约几分钟）
3. 构建完成后刷新线上站点 → **内容更新了** = 全链路闭环 ✅

---

## 故障排查速查

| 症状 | 原因与处理 |
|---|---|
| 后台登录报 repo not found | App 没装到仓库 → 做 A4 |
| 后台登录报 redirect_uri mismatch | App 的回调 URL 少了线上域名 → `https://github.com/settings/apps/xyeah126-keystatic` → Callback URLs 里补 `https://china-sf.xyeah126.workers.dev/api/keystatic/github/oauth/callback`（昨天你已填对 Deployed URL，大概率不会遇到） |
| Workers Builds 构建卡住/失败 | 本机曾遇到 `npm run build` 偶发卡在 "Rearranging server assets"（清 `dist`/`.astro` 缓存后正常）。CI 环境干净一般没事；真遇到就叫我，改分步 script |
| 构建成功但后台丢 App 引导 | Build variables 漏配 `PUBLIC_KEYSTATIC_GITHUB_APP_SLUG` → 按 B3 补上重新跑 |
| 线上打不开 | `workers.dev` 国内被墙，开代理（7892）；本机代理客户端要给浏览器开系统代理/全局模式 |

## 已完成的自动化部分（无需再动）

- Worker secrets：`KEYSTATIC_SECRET`、`KEYSTATIC_GITHUB_CLIENT_ID`、`KEYSTATIC_GITHUB_CLIENT_SECRET` 三个已配好
- `.env` 已整理（去重 + 剥内联注释），并被 gitignore，无泄露风险
- 部署版本 `72af5591` 已含构建期内联的 App slug（本地手动构建验证过）
- 线上 `/api/keystatic/github/login` → 307 跳 GitHub 且回调地址正确（决定性验证已通过）
- 历史记录：操作①（本地引导创建 GitHub App）已于 2026-09-04 19:50 完成，部署版本 `72af5591`

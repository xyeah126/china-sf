# 部署指南：GitHub → Cloudflare Pages

站点为纯静态站（Astro 输出 `dist/`），适合托管在 Cloudflare Pages：  
**免费、全球 CDN、自动 HTTPS、无需 ICP 备案**。

---

## 零、部署前必须定的两件事

### ① 域名

`astro.config.mjs` 的 `site` **已设为 Cloudflare Pages 默认域名 `https://china-sf.pages.dev`**，  
部署后即可直接用 `<project>.pages.dev` 访问，sitemap / robots / OG / canonical 全部正确。

> 若要绑定自定义域名（如 `chinasf.org`），改这一处即可全站同步：
>
> ```js
> // astro.config.mjs
> export default defineConfig({
>   site: 'https://你的域名.com',   // ← 改成真实域名后重新构建部署
>   ...
> });
> ```
>
> 这个 `site` 决定：sitemap 里的绝对 URL、`robots.txt` 的 Sitemap 地址、OG 标签的 og:url / og:image、canonical。

设计文档里的候选：

| 域名                  | 特点                                          |
| ------------------- | ------------------------------------------- |
| `chinasf.org`       | 对应英文站名 China S-F，短、好记（推荐主选）                     |
| `china-sf.org`      | 带连字符，与项目名 `china-sf` / 默认域 `china-sf.pages.dev` 一致 |
| `kehuanpulu.cn`     | 中文站名「科幻谱录」，.cn 需备案才能用国内 CDN，但 Pages 境外节点免备案 |
| `zhongguokehuan.cn` | 直白，同上                                       |

> 建议：**一个域名跑双语**（`/` 中文 + `/en/` 英文），比分两个域名更利于 SEO 权重集中。

### ② 是否需要国内访问速度

- Cloudflare Pages 免费节点在境外，国内访问速度一般，但**稳定可用、免备案**。
- 若要国内加速 → 需 ICP 备案 + 腾讯云/阿里云 CDN（设计文档 P7，二期再做）。

---

## 一、本地初始化 Git（我可以代做）

```bash
cd china-sf

git init
git add .
git commit -m "feat: 中国科幻作品网 首版（84 作品 / 31 作者 / 双语）"
```

> 已配好 `.gitignore`，会忽略 `dist/`、`.astro/`、`node_modules/`、日志与临时文件。  
> 首次提交前需配置身份（若尚未配置）：
>
> ```bash
> git config --global user.name "你的名字"
> git config --global user.email "你的邮箱"
> ```



---

## 二、在 GitHub 建仓库并推送（需你授权 GitHub 账号）

> 本机已装好 `gh` CLI（v2.98.0，路径 `/c/gh/bin/gh.exe`，或 `winget install GitHub.cli`）。  
> 本地仓库已 `git init` 并提交了首个 commit，分支为 **`master`**（不是 `main`）。

### 方式 C（推荐）：用 `gh` CLI 一键建仓 + 推送

1. **你先授权**（打开浏览器登录你的 GitHub 账号，这一步必须你本人操作）：
   ```bash
   /c/gh/bin/gh.exe auth login        # 或 winget 装的：gh auth login
   ```
   选 GitHub.com → 选 HTTPS → 选 "Login with a web browser" → 按提示粘贴一次性码。
2. 授权成功后，一条命令建仓并推送：
   ```bash
   cd china-sf
   /c/gh/bin/gh.exe repo create china-sf --public --source=. --remote=origin --push --branch=master
   ```
   > 这条命令会：在 GitHub 建 `china-sf` 仓库 → 加 `origin` 远程 → 推 `master` 分支。  
   > 若想用私有仓库，把 `--public` 换成 `--private`。

### 方式 A：用 GitHub 网页（最省事）

1. 打开 <https://github.com/new>
2. Repository name 填 `china-sf`，**选 Public**（Pages 免费版对私有仓库也支持，Public 便于后续开源）
3. **不要**勾选 "Add a README file"（本地已有）
4. 点 Create repository
5. 页面会给出推送命令，复制执行：

```bash
git remote add origin https://github.com/<你的用户名>/china-sf.git
git push -u origin master
```

> 若提示输入密码：GitHub 已不支持密码推送，需用 **Personal Access Token**：  
> GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)  
> → Generate new token → 勾选 `repo` → 生成后**当作密码**粘贴。

### 方式 B：用 SSH（配过密钥的话）

```bash
git remote add origin git@github.com:<你的用户名>/china-sf.git
git push -u origin master
```

---

## 三、Cloudflare Pages 连接仓库（你操作，约 3 分钟）

1. 注册/登录 <https://dash.cloudflare.com>
2. 左侧 **Workers & Pages** → **Create application** → **Pages** → **Connect to Git**
3. 授权 GitHub，选中 `china-sf` 仓库 → **Begin setup**
4. 填写构建配置：

| 配置项                    | 值                                 |
| ---------------------- | --------------------------------- |
| Project name           | `china-sf`                      |
| Production branch      | `master`                          |
| Framework preset       | **Astro**                         |
| Build command          | `npm run build`                   |
| Build output directory | `dist`                            |
| Root directory         | `/`（留空）                           |
| Node version           | `22`（已在 `.node-version` 指定，会自动读取） |

1. 环境变量：**无需配置**（本项目无密钥）
2. 点 **Save and Deploy**

首次构建约 1–3 分钟。构建日志里出现 `256 page(s) built` 即成功。

> **构建命令备选**：若 `npm run build` 在 CI 上出问题（本机曾有 npm 包装层的间歇问题），  
> 改成显式两步：`npx astro build && npx pagefind --site dist`

### 方式 D（备选）：Cloudflare 直传，无需 GitHub 仓库
若不想要 GitHub 仓库，也可直接用 `wrangler` CLI 把本地 `dist/` 上传到 Cloudflare Pages
（本机已 `npm install wrangler`，二进制在 `node_modules/.bin/wrangler`）。

1. 准备 Cloudflare 凭证（二选一）：
   - **API Token**（推荐，非交互）：Cloudflare 控制台 → My Profile → API Tokens →
     Create Token → 模板选 **Cloudflare Pages: Edit** → 复制 Token。
   - 或浏览器登录：`node_modules/.bin/wrangler login`（开浏览器授权）。
2. 一键部署（首次会自动创建 `china-sf` 项目）：
   ```bash
   cd china-sf
   # 用 API Token：
   CLOUDFLARE_API_TOKEN=<你的token> node_modules/.bin/wrangler pages deploy dist --project-name=china-sf
   # 或用 wrangler login 后：
   node_modules/.bin/wrangler pages deploy dist --project-name=china-sf
   ```
3. 部署完终端会给出 `https://china-sf.pages.dev` 预览地址；后续改内容后重跑同一条命令即可更新。

> 直传方式跳过 Git 自动构建，因此**不会**根据 `main` 分支自动触发；每次更新需手动重跑上面命令
> （或之后在 Cloudflare 控制台把项目改成「Connect to Git」接回 GitHub 也能恢复自动构建）。

---

## 四、绑定自定义域名

1. Pages 项目页 → **Custom domains** → **Set up a custom domain**
2. 输入你的域名 → 继续
3. Cloudflare 会提示添加 DNS 记录：
   - 若域名的 DNS 已托管在 Cloudflare：会自动添加 CNAME（一键完成）
   - 若 DNS 在别处（如阿里云/腾讯 DNS）：手动加一条
     ```
     类型: CNAME
     主机: @ (或 www)
     值:   china-sf.pages.dev
     ```
4. 等 SSL 证书自动签发（通常 5–15 分钟，状态变 Active 即生效）

---

## 五、部署后验收清单

部署完逐项检查（把域名换成你的）：

- [ ] `https://你的域名/` 首页正常
- [ ] `https://你的域名/en/` 英文站正常，右上角语言切换可用
- [ ] `https://你的域名/works` 84 张封面全部显示
- [ ] `https://你的域名/sitemap.xml` 返回 124 条 URL（含 hreflang）
- [ ] `https://你的域名/robots.txt` 返回且 Sitemap 地址正确
- [ ] `https://你的域名/search` 搜索可用（Pagefind 索引已生成）
- [ ] `https://你的域名/authors/liucixin` 作者印章头像 + 名下作品列表
- [ ] 点开任意作品 → 作者名可点击跳到作者页
- [ ] `https://你的域名/不存在的页面` 显示 404 页
- [ ] 浏览器标签页显示站点图标
- [ ] 分享到微信/微博时 OG 卡片图正常（og:image 指向封面）

---

## 六、日常更新流程

后续改内容或加作品后：

```bash
cd china-sf
# 本地预览确认（禁缓存服务器）
python scripts/preview_server.py 4550 dist

# 提交推送，Cloudflare 会自动重新构建部署
git add .
git commit -m "描述改动"
git push
```

每次 push 到 `main` 会自动触发构建，1–3 分钟后线上生效。  
其他分支会生成预览链接（Preview Deployment），可先验证再合并。

---

## 七、常见问题

| 现象                                | 原因 / 解决                                                        |
| --------------------------------- | -------------------------------------------------------------- |
| 构建报 `pagefind: command not found` | Build command 改用 `npx astro build && npx pagefind --site dist` |
| 页面 404 但本地正常                      | Build output directory 填 `dist`，不是 `/dist`                     |
| 搜索无结果                             | Pagefind 索引在构建后生成；确认构建命令里含 `pagefind --site dist`              |
| 中文站自动跳英文                          | 这是设计行为（按浏览器系统语言）；手动切换后写入 localStorage 会记住选择                    |
| sitemap 里是 example.com            | `astro.config.mjs` 的 `site` 没改                                 |
| 部署后封面没更新                          | `_headers` 给 `/covers/*` 缓存一周；换图请改文件名（本站已用 `-pd.jpg` 等新名）      |

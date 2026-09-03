# 后台「系统页面管理」实施计划

> 版本：2026-09-03 v1（待确认）。目标：把站点设置、About 文案、时期、出版社四类
> 系统级内容纳入 Keystatic 后台，实现"改内容不改代码"。
> 技术路线：继续用 Keystatic，新增 **singleton（单例）** 能力，零新依赖。

## 0. 结论先行

| 纳入项 | Keystatic 形态 | 存储位置 | 代码改造 |
|---|---|---|---|
| 站点设置（标题/口号/页脚/SEO） | singleton × 2（zh/en） | `src/content/settings/zh.yaml`、`en.yaml` | `BaseLayout.astro` 读取（i18n 兜底） |
| About 关于页文案（中/英） | singleton × 2（zh/en） | `src/content/pages/about-zh.md`、`about-en.md` | `About.astro` 从硬编码改为渲染 md |
| 时期 eras（6 个） | singleton × 1（data-yaml） | `src/content/eras.yaml`（原位） | **零改动**（loader 不变） |
| 出版社 publishers（N 个） | singleton × 1（data-yaml） | `src/content/publishers.yaml`（原位） | **零改动**（loader 不变） |

已验证的前提：
- `content.config.ts` 中 `era` 为 `z.string()`（非硬编码枚举）→ 后台新增时期**无需改 schema**
- `About.astro`（226 行）无子组件引用，41 段 p/h 纯文案 → **可整体迁 md**
- eras/publishers 走 Astro `file()` loader 读 YAML → 文件原位即可，页面代码零改动

## 1. 关键技术点

### 1.1 singleton 与 data-yaml
- Keystatic `singleton()`：UI 上是"单页设置"而非列表，保存到固定路径
- `format: { data: 'yaml' }`：条目存为**纯 YAML 数据文件**（无 frontmatter），
  与现有 `eras.yaml` / `publishers.yaml` 的文件形态一致
- singleton 的 `format.contentField` 同样支持 markdown 正文（About 用）

### 1.2 ⚠️ 最大风险：YAML 序列化格式 diff（可控）
Keystatic 写 YAML 的格式（缩进、键序、多行折叠块 `>-`）可能与手写文件不一致：
- **内容不会丢**（schema 为现有键的父集是硬规则），但首次在后台保存可能产生
  "整文件重排"式 git diff —— 内容等价、格式变化
- **缓解措施（P0 步骤）**：动手前用已沉淀的序列化探针
  （`serializeEntryToFiles` + `--conditions=browser` 往返验证）对 eras/publishers
  各跑一次：现有文件 → parse → serialize → diff，确认仅格式差异且字段齐全后才动手
- git 全程可回溯，首次保存后格式即稳定

### 1.3 站点设置的范围边界（避免过度工程）
`src/i18n/ui.ts` 每语言约 50+ 个键（按钮、徽章、状态等 UI 词），**全部后台化是负收益**。
只把以下 5 个"站点身份"键纳入 singleton，其余留在代码：
`siteName`、`siteNameShort`、`tagline`、`footerNote`（新增，页脚附注）、`seoDescription`
（新增，默认 meta description）。
`BaseLayout` 读取顺序：settings singleton → i18n/ui.ts 兜底（后台未填时不破坏现状）。

## 2. 实施步骤（按序执行，每步可验证）

| # | 步骤 | 产出/验证 |
|---|---|---|
| 1 | 序列化探针往返验证 eras/publishers | diff 仅格式性、8 键齐全 → 放行；否则调整 schema |
| 2 | 生成存量内容文件：`settings/zh.yaml`、`en.yaml`、`pages/about-zh.md`、`about-en.md`（About 现有文案原样迁入） | 4 个新文件，站点行为不变 |
| 3 | `keystatic.config.ts` 新增 5 个 singleton（settings-zh/en、about-zh/en、eras、publishers），**6 个现有 collection 不动** | config 语法通过 |
| 4 | 改造 `BaseLayout.astro`：siteName/siteNameShort/tagline/页脚/meta description 优先读 settings | dev 下页面渲染与改前逐字节一致 |
| 5 | 改造 `About.astro`：getEntry + render 渲染 `pages/about-zh/en.md`（`content.config.ts` 注册 pages collection） | about 页视觉不变 |
| 6 | dev 冒烟：`/keystatic` 出现 5 个新 singleton，逐个打开编辑保存 → git diff 检查不污染 | 保存往返无损 |
| 7 | `npm run build`：296 页全绿 + pagefind | exit=0，页数不回归 |
| 8 | 提交推送 + `wrangler deploy` + 线上抽测（/、/about/、/keystatic、/timeline/、/publishers/） | 线上 200 |

预估改动面：新增 4 文件 + 改 2 组件 + 改 1 配置 + 改 1 content.config，**不碰 340 篇存量 md**。

## 3. 明确不做（本期边界）

- ❌ 自定义独立页面路由（`pages` collection 泛化成"任意页面"）——本期 `pages`
  只承载 About 两篇，避免动态路由与 296 页静态化策略冲突；确有需求下期加
- ❌ i18n/ui.ts 其余 50+ UI 词后台化
- ❌ 导航顺序/结构后台化（导航项与路由强耦合，改动风险大于收益）

## 4. 验收标准

1. 后台修改 About 文案 / 时期起止年 / 出版社简介 / 站点口号 → 推送后线上生效，全程不写代码
2. 探针往返 + 后台保存往返，均不丢字段、正文不进 frontmatter（沿用数据安全铁律）
3. `npm run build` 页数不回归，现有 6 个 collection 的编辑行为不受影响

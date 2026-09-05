import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import keystatic from '@keystatic/astro';
import cloudflare from '@astrojs/cloudflare';
import { fileURLToPath } from 'node:url';

// 架构说明：
// - 站点本体约 296 个页面全部静态预渲染（output: 'static'）
// - Keystatic 的 /keystatic 与 /api/keystatic 是 on-demand 路由，
//   纯静态构建会报 NoAdapterInstalled，因此必须装 adapter
// - Cloudflare 部署用 @astrojs/cloudflare：静态页走 CDN，
//   on-demand 路由走 Worker
// - dev 本地默认 storage local（见 keystatic.config.ts），生产切 github 模式
//
// ⚠️ adapter 只在 build 时挂载：dev 下挂载会启用 worker 模拟器处理全部请求，
// Keystatic API 路由在其中报 "exports is not defined"（适配器 runner 的
// 模块互操作 bug）。与 keystatic 集成的 argv 判断是同一个模式。
const isBuild = process.argv.includes('build');

export default defineConfig({
  site: 'https://china-sf.sinosf.workers.dev',
  output: 'static',
  adapter: isBuild
    ? cloudflare({
        imageService: 'passthrough', // 站点不依赖 CF 图片服务，用默认行为即可
      })
    : undefined,
  integrations: [react(), keystatic()],
  vite: {
    resolve: {
      alias: [
        // 修复 astro 7.3.0 的打包 bug：dist/assets/vite-plugin-assets.js 里
        // `import ... from "astro/_internal/logger"`，但 exports map 没有该
        // 子路径，workerd 条件下解析直接报错。真实实现在 core/logger/core.js。
        {
          find: 'astro/_internal/logger',
          replacement: fileURLToPath(
            new URL('./node_modules/astro/dist/core/logger/core.js', import.meta.url)
          ),
        },
      ],
    },
  },
  i18n: {
    defaultLocale: 'zh',
    locales: ['zh', 'en'],
    routing: {
      prefixDefaultLocale: false, // 中文站根路径，英文站 /en/
      redirect: false,            // 语言识别由 BaseLayout 内联脚本处理
    },
  },
});

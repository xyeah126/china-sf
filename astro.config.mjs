import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import keystatic from '@keystatic/astro';

// Keystatic 的 /keystatic 与 /api/keystatic 是 on-demand 渲染路由。
// 纯静态构建（未装 adapter）时这类路由会让 `astro build` 直接失败
// （报错 NoAdapterInstalled），因此构建时不挂载 Keystatic。
//
// 注意：不能用 defineConfig 的函数形式（({ command }) => ...）——
// Astro 7 下函数式配置中集成的 injectRoute 不生效，/keystatic 会 404。
// 这里改从命令行参数判断：astro build 的 argv 含 'build'。
const isBuild = process.argv.includes('build');

export default defineConfig({
  site: 'https://china-sf.pages.dev',
  integrations: [react(), ...(isBuild ? [] : [keystatic()])],
  i18n: {
    defaultLocale: 'zh',
    locales: ['zh', 'en'],
    routing: {
      prefixDefaultLocale: false, // 中文站根路径，英文站 /en/
      redirect: false,            // 语言识别由 BaseLayout 内联脚本处理
    },
  },
});

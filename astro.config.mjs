import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://chinese-sf.pages.dev',
  i18n: {
    defaultLocale: 'zh',
    locales: ['zh', 'en'],
    routing: {
      prefixDefaultLocale: false, // 中文站根路径，英文站 /en/
      redirect: false,            // 语言识别由 BaseLayout 内联脚本处理
    },
  },
});

import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://investirlasterrenas.com',
  trailingSlash: 'ignore',
  build: {
    inlineStylesheets: 'auto',
  },
  compressHTML: true,
});

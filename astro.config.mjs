import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// IMPORTANT : domaine canonique du site.
// Le brief indique investirlasterrenas.com (sans tiret).
// hereles.com pointe vers investir-lasterrenas.com (avec tiret).
// → Vérifier lequel est le domaine de production et ajuster ici + dans src/consts.ts.
export default defineConfig({
  site: 'https://investirlasterrenas.com',
  trailingSlash: 'ignore',
  integrations: [
    sitemap({
      changefreq: 'weekly',
      priority: 0.7,
    }),
  ],
  build: {
    inlineStylesheets: 'auto',
  },
  compressHTML: true,
});

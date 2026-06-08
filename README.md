# Investir Las Terrenas — site Astro

Site de référence pour l'investissement immobilier à Las Terrenas (République Dominicaine).
Conseil indépendant — par **HERELES**. Construit avec **Astro** (statique, rapide, SEO/GEO).

---

## 🚀 Démarrer

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # génère /dist (prêt pour Netlify)
npm run preview  # prévisualise le build
```

Node ≥ 18.17.

## 🌐 Déployer sur Netlify

1. Pousser ce dossier sur un dépôt Git (GitHub/GitLab).
2. Sur Netlify → **Add new site → Import an existing project**.
3. Build command : `npm run build` · Publish directory : `dist` (déjà dans `netlify.toml`).
4. Déployer. Le `sitemap` et les en-têtes de sécurité sont automatiques.

> Alternative rapide : `npm run build` puis glisser-déposer le dossier `dist/` dans Netlify Drop.

**Formulaires** : les captures email (guide, exit-intent, landing) utilisent **Netlify Forms** — elles apparaissent dans l'onglet *Forms* de Netlify dès le déploiement, sans backend. Activez les notifications email dans Netlify.

---

## ⚙️ À configurer avant la mise en ligne

Tout est centralisé dans **`src/consts.ts`** (et `astro.config.mjs` pour le domaine).

- **Domaine** ⚠️ : le brief indique `investirlasterrenas.com` (sans tiret), mais hereles.com pointe vers `investir-lasterrenas.com` (avec tiret). Vérifier le bon domaine et l'ajuster dans `astro.config.mjs` **et** `src/consts.ts`.
- **Email** : actuellement `contact@hereles.com` ; l'adresse directe est `bs@hereles.com`. À arbitrer dans `consts.ts`.
- **Image OG** : ajouter `/public/og-image.png` (1200×630) pour les partages réseaux sociaux et les aperçus IA.
- **Photo du fondateur** : dans `src/pages/index.astro`, section `#fondateur`, remplacer le monogramme `BS` par `<img src="/benjamin-slama.jpg" alt="Benjamin Slama" />` (déposer la photo dans `/public`).

---

## 🗂️ Structure

```
src/
├─ consts.ts              # config centrale (contacts, liens, nav) — SOURCE UNIQUE
├─ styles/global.css      # design system (vert/ivoire/laiton)
├─ components/            # BaseHead, Header, Footer, StickyContact, ExitIntent, Faq, CtaBand
├─ layouts/               # BaseLayout, MarketingLayout
├─ content/
│  ├─ config.ts           # schémas des collections (pages SEO + blog)
│  ├─ pages/              # pages d'atterrissage SEO (Markdown + FAQ)
│  └─ blog/               # articles (Markdown + FAQ)
└─ pages/
   ├─ index.astro         # page d'accueil
   ├─ confotur.astro      # page CONFOTUR + simulateur d'économie
   ├─ guide.astro         # landing lead magnet
   ├─ [...slug].astro     # rend les pages SEO de content/pages
   └─ blog/               # index + [slug]
```

## ✍️ Ajouter du contenu (sans code)

**Une page SEO** → créer `src/content/pages/<slug>.md` :
```yaml
---
title: "Acheter un appartement à Las Terrenas"
description: "..."
eyebrow: "Guide d'achat"
faq:
  - q: "..."
    a: "..."
---
Contenu en Markdown…
```
La page sera servie sur `/<slug>` automatiquement, avec FAQ + schema.

**Un article de blog** → créer `src/content/blog/<slug>.md` (mêmes principes, champ `category` obligatoire).

---

## ✅ Livré (Phase 1)

- Architecture Astro complète, déployable, orientée Lighthouse 95+/SEO 100.
- Page d'accueil refondue : hero 3 CTA, données de marché, **opportunités en teasing** (2 emplacements prêts pour vos vrais biens), méthode en 6 étapes, fondateur (bio réelle), lead magnet, FAQ riche.
- Page **CONFOTUR** + **simulateur d'économie** interactif.
- Landing **lead magnet** « 17 erreurs ».
- Système blog + 1 article pilier (CONFOTUR).
- **15 pages SEO complètes** : immobilier-las-terrenas, acheter-appartement, acheter-villa,
  investir-las-terrenas, confotur, prix-immobilier, rendement-locatif, playa-bonita, playa-coson,
  punta-popy, investir-republique-dominicaine, acheter-en-republique-dominicaine,
  fiscalite-republique-dominicaine, residence-fiscale-republique-dominicaine,
  guide-investissement-las-terrenas — chacune avec contenu unique, maillage interne, FAQ + schémas.
- Conversion : WhatsApp + Calendly sticky, exit-intent, captures email Netlify, CTA récurrents.
- SEO/GEO : meta + OG, canoniques, `robots.txt` (bots IA autorisés), sitemap auto, schémas
  Organization/RealEstateAgent, WebSite, Person, FAQPage, Article, BreadcrumbList.

## 🔜 Étapes suivantes

- **Vos 2 biens réels** → à intégrer (prix, surface, quartier, rendement, photos) dès réception : je crée la base de biens + pages dédiées + filtres.
- **Blog** : montée à 50 articles, par lots.

## 📄 Le guide PDF (lead magnet)

Le guide **« Les 17 erreurs… »** (8 pages, charté) est inclus : `public/guide-17-erreurs-las-terrenas.pdf`.
Il est livré automatiquement via la page **`/merci`** : les formulaires email pointent vers `action="/merci"`,
donc après inscription, Netlify redirige l'internaute vers cette page qui propose le téléchargement (+ relance d'appel).
Pour aussi l'envoyer par email, activez un autorépondeur dans Netlify (onglet *Forms*) ou un outil d'emailing.
Pour régénérer/modifier le PDF : `python3 build_guide.py` (script fourni à la racine du livrable de travail).

> Mentions indicatives : les informations fiscales (CONFOTUR, IPI) et de marché sont fournies à titre indicatif et doivent être vérifiées au cas par cas. Aucune promesse de rendement.

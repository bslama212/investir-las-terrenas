import { defineCollection, z } from 'astro:content';

// Pages d'atterrissage SEO (corps en Markdown + FAQ structurée optionnelle)
const pages = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    eyebrow: z.string().optional(),
    h1: z.string().optional(),
    intro: z.string().optional(),
    updatedDate: z.coerce.date().optional(),
    faq: z.array(z.object({ q: z.string(), a: z.string() })).optional(),
    draft: z.boolean().default(false),
  }),
});

// Blog éditorial (GEO)
const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    category: z.enum([
      'Investissement',
      'Fiscalité',
      'CONFOTUR',
      'Quartiers',
      "Guides d'achat",
      'Marché immobilier',
      'Actualités',
      'Comparatifs',
    ]),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    author: z.string().default('Benjamin Slama'),
    faq: z.array(z.object({ q: z.string(), a: z.string() })).optional(),
    draft: z.boolean().default(false),
  }),
});

// Biens à la vente (sélection Hereles)
const properties = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    ref: z.string().optional(),
    residence: z.string().optional(),
    location: z.string().default('Las Terrenas, République Dominicaine'),
    status: z.string().default('À vendre'),
    available: z.boolean().default(true),
    price: z.number(),
    currency: z.string().default('USD'),
    surfaceM2: z.number().optional(),
    surfaceNote: z.string().optional(),
    pieces: z.number().optional(),
    bedrooms: z.number().optional(),
    bathrooms: z.number().optional(),
    floor: z.string().optional(),
    propertyType: z.string().default('Appartement'),
    confotur: z.boolean().default(false),
    yieldNet: z.string().optional(),
    yieldNote: z.string().optional(),
    summary: z.string().optional(),
    features: z.array(z.string()).default([]),
    residenceFeatures: z.array(z.string()).default([]),
    comparables: z.array(z.object({ label: z.string(), price: z.string() })).default([]),
    notes: z.array(z.string()).default([]),
    images: z.array(z.object({ src: z.string(), alt: z.string(), wide: z.boolean().default(false) })).default([]),
    order: z.number().default(0),
    draft: z.boolean().default(false),
  }),
});

export const collections = { pages, blog, properties };

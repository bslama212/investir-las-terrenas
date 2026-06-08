// =====================================================================
//  CONFIGURATION CENTRALE — Investir Las Terrenas (par HERELES)
//  Toutes les coordonnées et liens réels sont centralisés ici.
//  Modifier ici se répercute sur tout le site.
// =====================================================================

export const SITE = {
  // ⚠️ Vérifier le domaine de production (cf. astro.config.mjs)
  url: 'https://investirlasterrenas.com',
  name: 'Investir Las Terrenas',
  shortName: 'Investir Las Terrenas',
  tagline: 'Conseil en acquisition immobilière à Las Terrenas',
  description:
    "Conseil en acquisition immobilière pour investisseurs francophones à Las Terrenas (République Dominicaine). Nous sélectionnons et analysons pour vous les meilleures opportunités — appartements, villas et projets CONFOTUR — en collaboration avec les agences locales. Objectif, du côté de l'acquéreur.",
  locale: 'fr_FR',
  lang: 'fr',
  ogImage: '/og-image.png', // à ajouter dans /public (1200×630)
};

// Entité juridique (source : hereles.com — mentions légales)
export const LEGAL = {
  company: 'HERELES SASU',
  parentBrand: 'HERELES',
  parentUrl: 'https://www.hereles.com',
  siret: '930 723 804 00013',
  capital: '1 000 €',
  publisher: 'Benjamin Slama',
  addressLegal: '29 rue du Sergent Godefroy, 93100 Montreuil, France',
  addressOffice: '32 Avenue Duquesne, 75007 Paris, France',
  lastUpdate: 'juin 2026',
};

// Coordonnées & liens RÉELS
export const CONTACT = {
  email: 'bs@investirlasterrenas.com',
  emailDirect: 'bs@investirlasterrenas.com',
  phoneDisplay: '07 80 93 49 49',
  phoneHref: 'tel:+33780934949',
  phoneNote: 'Disponible sur WhatsApp',
  whatsapp: 'https://wa.me/33780934949',
  calendly: 'https://calendly.com/bs-hereles/30min',
};

export const SOCIAL = {
  linkedin: 'https://www.linkedin.com/in/benjaminslama/',
  instagram: 'https://www.instagram.com/bs_hereles/',
  x: 'https://x.com/BSlama_Hereles',
};

// Fondateur (faits vérifiables — source hereles.com)
export const FOUNDER = {
  name: 'Benjamin Slama',
  role: "Conseil en acquisition immobilière — Las Terrenas",
  bullets: [
    "Plus de 20 ans d'expérience dans l'immobilier",
    '15 ans chez Kaufman & Broad (promotion immobilière, Île-de-France)',
    'Structuration de financements alternatifs chez ClubFunding',
    'Fondateur de HERELES — structuration financière immobilière, France & Caraïbes',
  ],
};

export const NAV = [
  { label: 'Biens', href: '/biens' },
  { label: 'Méthode', href: '/#methode' },
  { label: 'CONFOTUR', href: '/confotur' },
  { label: 'Marché', href: '/#marche' },
  { label: 'Le fondateur', href: '/#fondateur' },
  { label: 'Guide', href: '/guide' },
  { label: 'Blog', href: '/blog' },
];

// Quartiers (pour le maillage SEO interne — pages à venir)
export const QUARTIERS = [
  { name: 'Playa Bonita', href: '/playa-bonita-immobilier' },
  { name: 'Playa Cosón', href: '/playa-coson-immobilier' },
  { name: 'Punta Popy', href: '/punta-popy-immobilier' },
];

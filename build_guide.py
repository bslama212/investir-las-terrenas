# -*- coding: utf-8 -*-
"""Génère le guide « 17 erreurs » — lead magnet Investir Las Terrenas (par HERELES)."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak,
    Table, TableStyle, NextPageTemplate, KeepTogether, HRFlowable,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ---------- Palette (identique au site) ----------
INK        = HexColor("#0c1a16")
EMERALD    = HexColor("#14342b")
EMERALD7   = HexColor("#1b4d3e")
BONE       = HexColor("#f4efe6")
PAPER      = HexColor("#fffdf8")
BRASS      = HexColor("#bd9a57")
BRASS_DEEP = HexColor("#9c7d3f")
MUTED      = HexColor("#5c6b63")
MUTED_LT   = HexColor("#9fb2a8")
LINE       = HexColor("#e2dccd")
TEXT       = HexColor("#243029")

# ---------- Polices (DejaVu — glyphes complets : €, accents) ----------
D = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("Serif", D + "DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("Serif-Bold", D + "DejaVuSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Serif-Italic", D + "DejaVuSerif-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Serif-BoldItalic", D + "DejaVuSerif-BoldItalic.ttf"))
pdfmetrics.registerFont(TTFont("Sans", D + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("Sans-Bold", D + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Sans-Oblique", D + "DejaVuSans-Oblique.ttf"))
pdfmetrics.registerFont(TTFont("Mono", D + "DejaVuSansMono.ttf"))
pdfmetrics.registerFontFamily("Serif", normal="Serif", bold="Serif-Bold",
                              italic="Serif-Italic", boldItalic="Serif-BoldItalic")
pdfmetrics.registerFontFamily("Sans", normal="Sans", bold="Sans-Bold", italic="Sans-Oblique")

W, H = A4
MARGIN = 2.2 * cm
CONTENT_W = W - 2 * MARGIN

# ---------- Styles ----------
def S(name, **kw):
    return ParagraphStyle(name, **kw)

st_eyebrow   = S("eyebrow", fontName="Mono", fontSize=8, textColor=BRASS_DEEP, leading=12,
                 spaceAfter=6, tracking=0)
st_h1        = S("h1", fontName="Serif-Bold", fontSize=24, textColor=INK, leading=27, spaceAfter=12)
st_h2        = S("h2", fontName="Serif-Bold", fontSize=17, textColor=INK, leading=21, spaceAfter=8)
st_body      = S("body", fontName="Sans", fontSize=10, textColor=TEXT, leading=15.5, spaceAfter=9)
st_lead      = S("lead", fontName="Sans", fontSize=11.5, textColor=MUTED, leading=17, spaceAfter=10)
st_part_eye  = S("part_eye", fontName="Mono", fontSize=8.5, textColor=BRASS_DEEP, leading=12, spaceAfter=4)
st_part_ttl  = S("part_ttl", fontName="Serif-Bold", fontSize=18, textColor=EMERALD, leading=22)
st_num       = S("num", fontName="Serif-Bold", fontSize=22, textColor=BRASS, leading=24)
st_err_ttl   = S("err_ttl", fontName="Serif-Bold", fontSize=13, textColor=INK, leading=16, spaceAfter=4)
st_err_body  = S("err_body", fontName="Sans", fontSize=9.7, textColor=TEXT, leading=14.5, spaceAfter=5)
st_reflexe   = S("reflexe", fontName="Sans", fontSize=9.5, textColor=EMERALD7, leading=14)
st_box       = S("box", fontName="Sans", fontSize=10, textColor=TEXT, leading=15)
st_box_ttl   = S("box_ttl", fontName="Mono", fontSize=8.5, textColor=BRASS_DEEP, leading=12, spaceAfter=5)
st_check     = S("check", fontName="Sans", fontSize=10.2, textColor=TEXT, leading=15, spaceAfter=7, leftIndent=2)
st_cta_ttl   = S("cta_ttl", fontName="Serif-Bold", fontSize=20, textColor=BONE, leading=24, spaceAfter=8)
st_cta_body  = S("cta_body", fontName="Sans", fontSize=10.5, textColor=BONE, leading=16, spaceAfter=6)
st_cta_line  = S("cta_line", fontName="Sans", fontSize=10.5, textColor=BONE, leading=18)
st_fine      = S("fine", fontName="Sans-Oblique", fontSize=8, textColor=MUTED, leading=11.5, spaceBefore=4)
st_foot      = S("foot", fontName="Mono", fontSize=7.5, textColor=MUTED, leading=10)

# ---------- Dessin des pages ----------
def draw_cover(c, doc):
    c.setFillColor(INK)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    # motif topographique (lignes laiton, fondu)
    c.saveState()
    c.setStrokeColor(BRASS)
    base = [
        (0.30, 0.78), (0.24, 0.70), (0.36, 0.62), (0.18, 0.54), (0.42, 0.46),
    ]
    for i, alpha in enumerate([0.30, 0.22, 0.16, 0.12, 0.09]):
        y0 = (0.34 - i * 0.018)
        c.setStrokeAlpha(alpha)
        c.setLineWidth(0.9 if i < 2 else 0.6)
        c.bezier(-40, H * y0,
                 W * 0.32, H * (y0 + 0.10),
                 W * 0.64, H * (y0 - 0.04),
                 W + 40, H * (y0 + 0.12))
    c.restoreState()

    # wordmark
    c.setFont("Mono", 9); c.setFillColor(BRASS)
    c.drawString(MARGIN, H - 2.3 * cm, "INVESTIR LAS TERRENAS   ·   PAR HERELES")

    # eyebrow
    c.setFont("Mono", 9); c.setFillColor(MUTED_LT)
    c.drawString(MARGIN, H - 8.6 * cm, "GUIDE GRATUIT   ·   ÉDITION 2026")

    # titre
    c.setFillColor(BONE); c.setFont("Serif-Bold", 30)
    lines = ["Les 17 erreurs", "qui coûtent le plus cher", "aux investisseurs", "français à Las Terrenas."]
    y = H - 9.8 * cm
    for ln in lines:
        c.drawString(MARGIN, y, ln)
        y -= 1.18 * cm

    # filet laiton
    c.setStrokeColor(BRASS); c.setLineWidth(2); c.setStrokeAlpha(1)
    c.line(MARGIN, y - 0.2 * cm, MARGIN + 3.2 * cm, y - 0.2 * cm)

    # sous-titre
    c.setFont("Sans", 12); c.setFillColor(MUTED_LT)
    c.drawString(MARGIN, y - 1.2 * cm, "Le guide que nous remettons à nos clients avant tout achat.")

    # bas de page
    c.setFont("Sans-Bold" if "Sans-Bold" in pdfmetrics.getRegisteredFontNames() else "Sans", 10)
    c.setFillColor(BONE)
    c.drawString(MARGIN, 2.6 * cm, "Benjamin Slama")
    c.setFont("Sans", 9); c.setFillColor(MUTED_LT)
    c.drawString(MARGIN, 2.05 * cm, "Conseil en acquisition immobilière — Las Terrenas, République Dominicaine")
    c.setFont("Mono", 8); c.setFillColor(BRASS)
    c.drawString(MARGIN, 1.5 * cm, "investirlasterrenas.com")

def draw_chrome(c, doc):
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    # filet + pied de page
    c.setStrokeColor(LINE); c.setLineWidth(0.6)
    c.line(MARGIN, 1.55 * cm, W - MARGIN, 1.55 * cm)
    c.setFont("Mono", 7.5); c.setFillColor(MUTED)
    c.drawString(MARGIN, 1.15 * cm, "Investir Las Terrenas — par HERELES")
    c.drawRightString(W - MARGIN, 1.15 * cm, str(doc.page))

# ---------- Contenu : les 17 erreurs ----------
PARTS = [
    ("Partie 1", "Les chiffres : ne pas se faire piéger par les promesses", [
        ("Confondre rendement brut et rendement net",
         "Les annonces affichent 8 à 10 %. Une fois déduits les charges, la gestion, la vacance et la fiscalité, le rendement net réaliste tombe souvent entre 5,6 % et 7,7 %.",
         "Exigez toujours un calcul net — vacance et charges incluses — avant de comparer deux biens."),
        ("Prendre les « prix du marché » pour argent comptant",
         "Il n'existe pas de registre public des prix de vente en République Dominicaine. Les chiffres viennent des annonces : des intentions de vente, pas des transactions conclues.",
         "Faites estimer le prix réaliste par une analyse comparative, pas par la plaquette du programme."),
        ("Croire que le CONFOTUR est automatique",
         "L'exonération (taxe de transfert et IPI) ne vaut que pour un projet certifié, pour le premier acquéreur, et pour la durée restante.",
         "Vérifiez la résolution de certification, votre rang d'acquéreur et les années restantes — sur pièces."),
    ]),
    ("Partie 2", "Le juridique et le titre : là où se cachent les vrais risques", [
        ("Acheter un terrain ou une villa sans deslinde à jour",
         "Sans bornage GPS officiel, les limites peuvent être floues ou litigieuses — un problème coûteux et long à régler.",
         "Pas de deslinde valide, pas de signature. C'est non négociable."),
        ("Ne pas vérifier le titre et l'absence de dettes",
         "Un titre non purgé (Registro de Títulos) ou une hypothèque cachée peuvent compromettre l'achat après coup.",
         "Titre purgé et certificat de non-dette systématiques, avant tout versement."),
        ("S'en remettre au seul avocat du vendeur ou du promoteur",
         "Son rôle est de protéger le vendeur — pas vous.",
         "Mandatez votre propre avocat indépendant pour la due diligence et l'acte."),
        ("Signer une promesse de vente (Promesa de Venta) sans filet",
         "Une promesse mal rédigée, sans conditions suspensives (due diligence, financement), vous engage trop tôt.",
         "Conditions suspensives claires et dépôt séquestré : votre sortie de secours."),
    ]),
    ("Partie 3", "Les coûts et la fiscalité : le diable est dans les détails", [
        ("Sous-estimer les frais d'acquisition",
         "Au prix s'ajoutent environ 4,5 % à 5,5 % : taxe de transfert (3 %), avocat, enregistrement.",
         "Budgétez ces frais dès le départ — le CONFOTUR peut en neutraliser une partie."),
        ("Oublier le fisc français",
         "Résident fiscal français, vous restez soumis à vos obligations : déclaration des avoirs et revenus étrangers, loyers, plus-values.",
         "Faites valider le montage par un fiscaliste compétent des deux côtés de l'Atlantique."),
        ("Confondre achat, résidence et résidence fiscale",
         "Ce sont trois choses distinctes : acheter n'est pas résider, et résider n'est pas être imposé sur place.",
         "Clarifiez votre objectif réel — usage, revenu, résidence — avant d'acheter."),
        ("Négliger le change et le rapatriement des loyers",
         "Loyers en pesos ou en dollars, frais de change et modalités de rapatriement grignotent le rendement réel.",
         "Intégrez le change dans vos projections — pas seulement le loyer affiché."),
    ]),
    ("Partie 4", "Le bien, la gestion et la méthode : ce qui fait la différence", [
        ("Choisir le mauvais quartier pour son objectif",
         "Le centre et Punta Popy servent le locatif ; Playa Cosón et Playa Bonita servent l'usage et le haut de gamme.",
         "Faites correspondre la zone à votre objectif — pas à un coup de cœur."),
        ("Laisser l'émotion piloter l'achat",
         "Une vue mer ne paie pas les charges. Un bel achat peut être un mauvais investissement, et difficile à revendre.",
         "Décidez sur les chiffres et la liquidité à la revente ; la vue est un bonus."),
        ("Sous-estimer la gestion locative",
         "Vacance, ménage, conciergerie, saisonnalité : un bon bien mal géré devient un mauvais investissement.",
         "Chiffrez et organisez la gestion avant d'acheter, pas après."),
        ("Ne pas préparer sa sortie",
         "La plus-value est en principe imposable, et la revente dépend de la liquidité de la zone.",
         "Pensez la revente dès l'achat : horizon, fiscalité de sortie, demande locale."),
        ("Acheter sur plan sans sécuriser les fonds",
         "Les protections de l'achat sur plan sont plus faibles qu'en France ; un promoteur fragile, c'est un risque réel.",
         "Versements échelonnés liés à l'avancement, séquestre, et vérification du promoteur."),
        ("Y aller seul, sans conseil objectif à l'achat",
         "Entre la distance, l'absence de registre des prix et les spécificités locales, l'improvisation coûte cher.",
         "Appuyez-vous sur un conseil objectif, du côté de l'acquéreur, qui travaille avec les meilleures agences locales."),
    ]),
]

def error_table(errors, start_n):
    rows = []
    n = start_n
    for (title, err, ref) in errors:
        num = Paragraph(str(n), st_num)
        content = [
            Paragraph(title, st_err_ttl),
            Paragraph(err, st_err_body),
            Paragraph('<font name="Sans-Bold" color="#9c7d3f">Le bon réflexe.</font> ' + ref, st_reflexe),
        ]
        rows.append([num, content])
        n += 1
    t = Table(rows, colWidths=[1.5 * cm, CONTENT_W - 1.5 * cm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (0, -1), 0),
        ("LEFTPADDING", (1, 0), (1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 11),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 13),
        ("LINEBELOW", (0, 0), (-1, -1), 0.6, LINE),
    ]))
    return t, n

def box(flowables, bg=BONE, border=BRASS):
    t = Table([[flowables]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, -1), 3, border),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 13),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 13),
    ]))
    return t

# ---------- Construction du document ----------
def build(path):
    doc = BaseDocTemplate(path, pagesize=A4,
                          leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=2.2 * cm, bottomMargin=2.2 * cm,
                          title="Les 17 erreurs des investisseurs français à Las Terrenas",
                          author="Benjamin Slama — Investir Las Terrenas (HERELES)",
                          subject="Guide d'investissement immobilier à Las Terrenas")
    cover_frame = Frame(0, 0, W, H, id="cover", leftPadding=0, rightPadding=0,
                        topPadding=0, bottomPadding=0)
    content_frame = Frame(MARGIN, 2.2 * cm, CONTENT_W, H - 4.4 * cm, id="content")
    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[cover_frame], onPage=draw_cover),
        PageTemplate(id="content", frames=[content_frame], onPage=draw_chrome),
    ])

    s = []
    # --- Couverture (dessinée par onPage) ---
    s += [Spacer(1, 1), NextPageTemplate("content"), PageBreak()]

    # --- Introduction ---
    s.append(Paragraph("Introduction", st_eyebrow))
    s.append(Paragraph("Avant d'acheter à Las Terrenas, lisez ceci.", st_h1))
    s.append(Paragraph(
        "Las Terrenas est l'une des plus belles opportunités immobilières des Caraïbes : tourisme "
        "record, fiscalité CONFOTUR, droits de propriété pleins et entiers pour les étrangers. Mais "
        "c'est aussi un marché lointain, sans registre public des prix, avec ses propres codes.", st_lead))
    s.append(Paragraph(
        "La plupart des mauvaises surprises ne viennent pas du marché : elles viennent d'erreurs "
        "évitables. Ce guide réunit les <b>17 erreurs qui coûtent le plus cher</b> aux investisseurs "
        "français à Las Terrenas, et le bon réflexe pour chacune.", st_body))
    s.append(Spacer(1, 6))
    s.append(box([
        Paragraph("NOTRE POSTURE", st_box_ttl),
        Paragraph(
            "Nous sommes un conseil en acquisition <b>objectif</b>. Nous ne sommes pas une agence : "
            "nous travaillons avec les meilleures agences locales pour vous présenter les meilleures "
            "opportunités du marché et défendre votre intérêt d'acquéreur — de la première visite à "
            "la remise des clés.", st_box),
    ]))
    s.append(Spacer(1, 8))
    s.append(Paragraph(
        "Informations à jour de 2026, fournies à titre indicatif. Les éléments fiscaux (CONFOTUR, IPI) "
        "et de marché doivent être vérifiés au cas par cas. Aucune promesse de rendement.", st_fine))
    s.append(PageBreak())

    # --- Les 4 parties / 17 erreurs ---
    n = 1
    for i, (eye, title, errors) in enumerate(PARTS):
        header = [
            Paragraph(eye, st_part_eye),
            Paragraph(title, st_part_ttl),
            HRFlowable(width=42, thickness=2, color=BRASS, spaceBefore=6, spaceAfter=10, hAlign="LEFT"),
        ]
        s.append(KeepTogether(header))
        table, n = error_table(errors, n)
        s.append(table)
        s.append(Spacer(1, 0.7 * cm))

    s.append(PageBreak())

    # --- Check-list ---
    s.append(Paragraph("La synthèse", st_eyebrow))
    s.append(Paragraph("La check-list avant de signer", st_h1))
    s.append(Paragraph("Sept vérifications qui, à elles seules, écartent l'essentiel du risque.", st_lead))
    s.append(Spacer(1, 4))
    checklist = [
        "Titre purgé au Registro de Títulos, au nom du vendeur.",
        "Certificat de non-dette (ni charges ni hypothèque cachées).",
        "Deslinde (bornage GPS) à jour — surtout pour une villa ou un terrain.",
        "Certification CONFOTUR vérifiée, et durée d'exonération restante.",
        "Charges de copropriété et coûts d'entretien réels, chiffrés.",
        "Rendement projeté en net — vacance, gestion et fiscalité incluses.",
        "Votre propre avocat indépendant — jamais le seul avocat du vendeur.",
    ]
    check_rows = []
    for i, item in enumerate(checklist, 1):
        check_rows.append([
            Paragraph(f'<font name="Serif-Bold" color="#9c7d3f">{i:02d}</font>', st_check),
            Paragraph(item, st_check),
        ])
    ct = Table(check_rows, colWidths=[1.1 * cm, CONTENT_W - 1.1 * cm])
    ct.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    s.append(box([ct]))
    s.append(PageBreak())

    # --- Page de clôture / CTA ---
    s.append(Paragraph("Et maintenant ?", st_eyebrow))
    s.append(Paragraph("Ces 17 erreurs se règlent en amont.", st_h1))
    s.append(Paragraph(
        "Elles ont toutes un point commun : l'analyse et la vérification, faites avant de signer, les "
        "évitent. C'est précisément notre métier.", st_lead))
    s.append(Paragraph(
        "Investir Las Terrenas, c'est l'expertise immobilière de <b>HERELES</b> — Benjamin Slama, "
        "plus de 20 ans dans l'immobilier, ex-Kaufman &amp; Broad, ex-ClubFunding — au service d'un "
        "seul objectif : votre acquisition, réussie. Nous sélectionnons et analysons les meilleures "
        "opportunités, en collaboration avec les agences locales, et nous défendons votre intérêt "
        "d'acquéreur.", st_body))
    s.append(Spacer(1, 10))

    cta_inner = [
        Paragraph("Parlons de votre projet.", st_cta_ttl),
        Paragraph("Un premier échange, sans engagement, pour cadrer votre budget, vos objectifs de "
                  "rendement et la faisabilité.", st_cta_body),
        Spacer(1, 6),
        Paragraph('<font name="Sans-Bold">Réserver un appel  </font>'
                  '<a href="https://calendly.com/bs-hereles/30min"><font color="#bd9a57">calendly.com/bs-hereles/30min</font></a>', st_cta_line),
        Paragraph('<font name="Sans-Bold">WhatsApp  </font>'
                  '<a href="https://wa.me/33780934949"><font color="#bd9a57">07 80 93 49 49</font></a>', st_cta_line),
        Paragraph('<font name="Sans-Bold">Email  </font>'
                  '<a href="mailto:bs@investirlasterrenas.com"><font color="#bd9a57">bs@investirlasterrenas.com</font></a>', st_cta_line),
    ]
    cta = Table([[cta_inner]], colWidths=[CONTENT_W])
    cta.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), EMERALD),
        ("LEFTPADDING", (0, 0), (-1, -1), 20),
        ("RIGHTPADDING", (0, 0), (-1, -1), 20),
        ("TOPPADDING", (0, 0), (-1, -1), 20),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 22),
        ("LINEABOVE", (0, 0), (-1, 0), 3, BRASS),
    ]))
    s.append(cta)
    s.append(Spacer(1, 16))
    s.append(Paragraph(
        "HERELES SASU — SIRET 930 723 804 00013 — 29 rue du Sergent Godefroy, 93100 Montreuil, France. "
        "Une activité de HERELES (hereles.com).", st_fine))
    s.append(Paragraph(
        "Document gratuit, à titre informatif et non contractuel. Ne constitue ni un conseil juridique, "
        "ni un conseil fiscal, ni une promesse de rendement. Toute opération doit être vérifiée au cas "
        "par cas avec les professionnels compétents en France et en République Dominicaine.", st_fine))

    doc.build(s)
    print("PDF généré :", path)

if __name__ == "__main__":
    build("public/guide-17-erreurs-las-terrenas.pdf")

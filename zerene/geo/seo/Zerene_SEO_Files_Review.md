# Zerene SEO File Review — Consolidated Findings

Review of all files in `seo/` directory against live store and brand positioning framework.

## 1. File Inventory

| File | Purpose | Reviewed |
|------|---------|----------|
| `Zerene_GEO_AIO_Content_Framework (1).pdf` | Brand positioning & writing rules | Yes |
| `Zerene_SEO_GEO_Alignment_Brief (1).pdf` | SEO/GEO workflow gaps | Yes |
| `40 Blog Audit & AI Optimization Report - Sep 2026.md` | Audit of 40 published blogs | Yes |
| `Blog Audit & AI Optimization Guide - Sep 2026.md` | GEO optimization playbook | Yes |
| `GEO Monitoring Report - 2026-09-04.md` | AI Share of Voice tracking | Yes |
| `GEO Monitoring Report - 2026-09-04.pdf` | PDF version of above | Skipped |
| `GEO Monitoring Report - 2026-09-04c.html` | HTML version | Skipped |
| `GEO Status Report - Saudi Arabia - Sep 2026.md` | KSA market-specific audit | Yes |
| `SEO Review - 19-26 Aug 2026.md` | Review of deliverables | Yes |
| `5 Blog Title Strategy.docx` | Recommended blog topics | Yes (text extracted) |
| `SEO Work Report 19-26 Aug 2026.docx` | Weekly activity report | Yes (text extracted) |
| `disavow_20260826.txt` | Backlink disavow list | Yes (cross-referenced) |
| `geo_tracking_2026-09-04.json` | Raw prompt tracking data | Yes |
| `zerene-blog-schema.liquid` | JSON-LD schema for articles | Yes |
| `zerene-shopify-schema.liquid` | JSON-LD schema (brand/product) | Yes |
| `zerene-seo-review.html` | Visual SEO review | Not reviewed |

---

## 2. Cross-Document Findings

### Blocking — Positioning Split: B2B vs B2C in Blog Topics

The Content Framework explicitly repositions Zerene to **B2B corporate procurement**, but the
5 Blog Title Strategy proposes **B2C perfume queries**:

| Proposed Title | Keyword | Issue |
|---------------|---------|-------|
| Oud Home Fragrance: Guide to Arabian Atmosphere | عطر العود | B2C perfume query; brand-direct intent |
| Oud Bakhoor or Oud Diffuser | بخور العود | Zero bakhoor in catalog; consumer comparison |
| Luxury Oud Gift: Gift Ideas | هدية عود | B2C gifting, not corporate procurement |
| Luxury Home Fragrance Sets: Perfect Gift | مجموعة عطور | Product-focused; belongs on collection page |
| Rose Vanilla: Why Is It Loved? | روز فانيلا | **Rejected by client** — no product matches; B2C perfume query |

**Consensus across all files:** Replace topics 2 and 5, split the rest into collection-page
vs blog-post intent, and map keywords to the B2B ICP (corporate procurement, executive
offices, luxury hospitality, not consumer home fragrance).

### Blocking — Currency Mismatch (AED vs SAR)

GEO Monitoring data shows Perplexity/AI responses for KSA queries reference zerene.com but
**Zerene is cited only on brand-direct prompts** (3/3). On category prompts (0/4 for KSA Category
Intent, 0/3 for Executive Gifting, 0/3 for Problem-Solution), competitors dominate because they
present **SAR pricing**. The store currently defaults to AED with no SAR toggle.

> Ref: GEO Status Report — "Store defaults strictly to AED... No currency selector is surfaced
> for Saudi Riyals (SAR)."

### Blocking — No JSON-LD Schema (0/40 blogs)

Both audit reports agree: zero `Article`, `BlogPosting`, or `FAQPage` JSON-LD schema exists on
any page. The liquid snippets exist in `seo/` but are **not deployed** to the live store.

> Competitors like Jo Malone, Dr. Vranjes, and Diptyque surface in AI responses because
> they have schema-backed FAQ content that scrapers parse 5x faster.

### Gap — Missing Product Specs & Prices (0/40 blogs)

No blog states volume (200ml), prices (SAR/AED), or delivery timelines. AI shopping bots
require these to validate recommendations. The tracking JSON shows competitors surface with
explicit pricing; Zerene does not.

### Critical — Disavow File is Self-Harm

`disavow_20260826.txt` disallows:
- `zerene.life` — 301 redirects to zerene.com (Zerene's **own** domain)
- `zerene.co` — 301 redirects to zerene.com (Zerene's **own** domain)

Disavowing these discards link equity. Recommendation: do not submit, verify ownership at
registrar, fix the vendor's name-matching methodology.

### Gap — SEO Work Report Has No Metrics

The weekly report (19–26 Aug) lists activities (blog optimization, competitor research) but
contains **zero metrics**: no impressions, clicks, CTR, positions, or URL lists. The competitor
research output is described as a single sentence with no actual findings attached.

---

## 3. GEO Share of Voice Snapshot (2026-09-04)

| Prompt Category | Prompts | Zerene Mentioned | Competitors |
|---|---|---|---|
| Brand Direct | 3 | 3 (100%) | — |
| KSA Category Intent | 4 | 0 (0%) | Jo Malone, Diptyque, Dr. Vranjes, Arabian Oud |
| Executive Gifting | 3 | 0 (0%) | Bateel, Wah Gifts, customized gift sets |
| UAE Category Intent | 2 | 0 (0%) | Lush, Dr. Vranjes |
| Problem-Solution | 3 | 0 (0%) | Dr. Vranjes, Golden Scent, Ounass |

**Overall SoV: 20% (3/15)** — Zerene only appears on brand-direct queries.

### Missing Prompt Clusters to Target

From the tracking JSON, the exact AI queries where Zerene is absent but should compete:

- "Best luxury reed diffusers available in Saudi Arabia?" → Jo Malone, Diptyque dominate
- "عطور منازل فاخرة وثابتة للمجالس في الرياض" → oud, bakhoor (non-catalog products) win
- "Where to buy high-end alcohol-free room sprays in Riyadh?" → Ounass, Mubkhar win
- "Top luxury corporate gift sets for clients in Riyadh and Dubai" → generic gift sets win
- "أفضل هدايا فاخرة للمكاتب والرؤساء التنفيذيين في السعودية" → pens, leather desk sets win
- "Unique VIP gift ideas under 1000 SAR in Saudi Arabia" → dates, coffee, leather gifts win
- "Best long-lasting home diffusers for luxury apartments in Dubai" → Dr. Vranjes, AuraEER
- "Luxury room spray with French essential oils Dubai" → Dr. Vranjes, Scent Bazaar

---

## 4. Actionable Priorities

1. **Deploy JSON-LD schema** (`zerene-blog-schema.liquid` + `zerene-shopify-schema.liquid`)
   to Shopify `article.liquid` and `theme.liquid`.
2. **Add Product Spec & Price tables** to all 40 blogs — 200ml volume, 420–1,020 AED range,
   4–6 month longevity, 2–4 day KSA express delivery.
3. **Enable SAR currency** via Shopify Markets for KSA visitors.
4. **Replace 2 invalid blog topics** (bakhoor, rose vanilla) with B2B-aligned alternatives.
5. **Rewrite remaining 3 topics** to blog-post format (supporting collection pages, not competing).
6. **Add B2B direct-answer FAQ blocks** to product pages (Q&A for AI extraction).
7. **Build dedicated B2B landing pages** (`/pages/corporate-gifting`, `/pages/hospitality`).
8. **Fix the disavow file** — remove zerene.life, zerene.co before any submission.
9. **Add metrics to weekly reports** — impressions, clicks, CTR, avg position, URLs touched.

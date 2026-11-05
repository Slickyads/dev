# Zerene GEO Prompt Workflow

This folder contains the n8n workflow for generating a GEO (Generative Engine Optimization) and SEO prompt library for **Zerene**, a B2B fragrance e-commerce brand based in Saudi Arabia.

---

## Current Architecture (v2 — Consolidated n8n Workflow)

**Single workflow file:** `n8n_workflows/geo_prompt_generator_form.n8n.json`

### Flow

```text
GEO Form (n8n Form Trigger)
    │
    ▼
Fetch Website (HTTP Request — scrapes title, meta, content)
    │
    ▼
Build Analysis Request (Code node — structures prompt for Gemini)
    │
    ▼
Gemini 1 — Analysis (generates profile, 3 opportunities, N keywords)
    │
    ▼
Parse Profile (Code node — validates, structures, adds IDs)
    │
    ├──▶ Emit Opportunities → Save Opportunities (Google Sheets: "opportunities" tab)
    │
    ├──▶ Emit Keywords → Save Keywords (Google Sheets: "keywords" tab)
    │
    ▼
Build Prompt Request (Code node — builds prompt-writing prompt for Gemini)
    │
    ▼
Gemini 2 — Write Prompts (generates buyer-facing AI prompts)
    │
    ▼
Parse Prompts (Code node — merges, adds fallback for failures)
    │
    ▼
Emit Prompts → Save Prompts (Google Sheets: "prompts" tab)
    │
    ▼
Show Results (Form node — renders prompts with badges + sheet link)
```

---

## Key Features

| Feature | Description |
|---|---|
| **Form Trigger** | Shareable Production URL — no landing page, CORS, or webhook setup needed |
| **Website Scraping** | Fetches and parses actual site content (title, meta description, visible text) |
| **AI-Driven Analysis** | Gemini 1 generates profile, 3 opportunities, and keywords dynamically from site content (not hardcoded) |
| **Structured Slot System** | 4 prompt categories with deterministic distribution:<br>• Brand Direct Queries (20%)<br>• KSA Category Intent (30%)<br>• Executive Gifting (20%)<br>• Problem-Solution (remainder) |
| **Tier-Specific Guidance** | 4 tiers with buyer personas and topics:<br>• Tier 1: Executive & VIP Corporate Gifting<br>• Tier 2: Hospitality, Majlis & Boutique Hotel<br>• Tier 3: Healthcare, Spas & Premium Medical Clinics<br>• Tier 4: Corporate Wellness & Interior Architecture |
| **Market & Language Support** | Markets: KSA, UAE, GCC, Global<br>Languages: English, Arabic, English + Arabic |
| **Safe Fallback** | Gemini 2 failure gracefully produces draft prompts marked "Needs rewrite" |
| **Results Page** | Renders all prompts with priority/category/language badges + direct Google Sheet link |
| **Single Google Sheet** | ID: `1yAJ1LwDG3KI_aAQGKNnu2adc0SzSUdZI2EAPK4aWdRQ` with 3 tabs: `opportunities`, `keywords`, `prompts` |

---

## Setup

1. **Google Sheet tabs/headers** — Run the Apps Script (see `00-shared-context.md` for structure)
2. **Gemini API Key** — Create HTTP Header Auth credential in n8n:
   - Name: `Gemini_geo_prompts`
   - Header: `x-goog-api-key` = your Gemini API key
3. **Activate the workflow** — The form trigger exposes a Production URL you can share

---

## Form Fields

| Field | Type | Required | Options |
|---|---|---|---|
| Website URL | Text | Yes | `https://yourbrand.com` |
| Brand Name | Text | No | — |
| Tier | Dropdown | Yes | Tier 1–4 (see above) |
| Market | Dropdown | Yes | KSA, UAE, GCC, Global |
| Language | Dropdown | Yes | English, Arabic, English + Arabic |
| Number of prompts | Dropdown | Yes | 10, 25 |

---

## Output Data Model

### `opportunities` tab
| Column | Description |
|---|---|
| `opportunity_id` | `${runId}-O1/2/3` |
| `theme` | Opportunity theme |
| `buyer_intent` | What the buyer wants |
| `audience` | Target buyer roles |
| `market` / `language` | From form |
| `search_query` | Representative query |
| `seasonal` / `cultural` | Timing & cultural angles |
| `competitor` | Competitor **types** (never company names) |
| `gap` | Content/visibility gap |

### `keywords` tab
| Column | Description |
|---|---|
| `keyword_id` | `KW-${BRAND}-T${tierNum}-${CATCODE}-${INTENT}-${MARKET}-${LANG}-${NN}-${runId}` |
| `keyword` | Natural search phrase (3–8 words) |
| `keyword_intent` | Informational / Commercial / Transactional |
| `icp_search_type` | Commercial / Seasonal / Cultural / Comparison / Direct answer |
| `prompt_category` | Brand Direct / KSA Category Intent / Executive Gifting / Problem-Solution |
| `segment` | Brand / Category benchmark / Non-brand |
| `priority` | High / Medium / Long-term |
| `opportunity_id` | Links to opportunity |

### `prompts` tab
| Column | Description |
|---|---|
| `prompt_id` | `${slug}-T${tierNum}-${CATCODE}-${INTENT}-${MARKET}-${AR/EN}-${NN}-${runId}` |
| `prompt_text` | What a buyer types into an AI engine (1–2 sentences, natural language) |
| `status` | `Pending scan` (AI-generated) or `Needs rewrite` (fallback) |
| All keyword fields | Carried through for traceability |

---

## Prompt Categories & Rules

| Category | Keyword Must Include | Prompt Angle |
|---|---|---|
| **Brand Direct Queries** | Brand name | Reputation, products, ordering, comparison |
| **KSA Category Intent** | Market location (e.g., "Riyadh", "Saudi Arabia") — **no brand** | Category benchmark question |
| **Executive Gifting** | Decision-maker / VIP / seasonal-cultural (Ramadan, Eid, National Day) — **no brand** | Gifting for executives |
| **Problem-Solution** | Buyer problem/need — **no brand** | "How to solve X?" |

---

## Legacy (v1 — Manual Markdown Workflow)

The following files document the previous manual multi-step process and are kept for reference:

- `00-shared-context.md` — Shared brand context
- `01-opportunity-analysis.md` — Manual opportunity analysis
- `02-keyword-dataset.md` — Deterministic keyword generation
- `03a-high-priority-prompts.md` / `03b-medium-priority-prompts.md` / `03c-long-term-geo-prompts.md` — Batched prompt generation
- `04-quality-control-export.md` — QC checklist

These are **superseded** by the consolidated n8n workflow above.

---

## Token-Saving Principles (Preserved)

- Reuse shared context instead of repeating full workflow
- Generate prompts in batches (10 or 25 via form)
- Do not invent search volume, keyword difficulty, AI prompt volume, or visibility metrics — mark as `[TO VERIFY]`
- Quality control after human review of generated batches

---

## Prompt Template (for reference — n8n handles this)

Each ready-to-use prompt includes:
- Specialist role (Zerene B2B fragrance e-commerce brand)
- Zerene brand context from website
- Audience and buying stage
- Offer tier
- Prompt category
- Target AI prompt / search query
- Primary keyword + secondary keywords
- Market and language
- Content type and output format
- GEO requirements
- Internal linking plan
- Schema recommendations
- Request a Quote instruction + CTA URL
- **No invented facts, testimonials, client names, certifications, prices, statistics, or claims**
- Missing information marked `[TO VERIFY]`

---

## Output Quantity

Configurable via form:
- **10 prompts** (default)
- **25 prompts** (larger batch)

Distribution across 4 categories is deterministic (see Slot System above).
# Zerene GEO/AEO/SEO Workflow: Finding & Ranking High-Intent Prompts in AI Engines

**Last Updated:** 2026-10-15  
**Based on:** `Zerene_GEO_Agent_Playbook.md`, `guide_to_identifying_high_intent_volume_prompts.md`, `ai_guide_on_intent_volume_and_search_mechanics.md`, and keyword/xlsx data  

---

## 1. Objective  

Identify and validate **50+ high-intent, non-brand B2B prompts** where Zerene can achieve **mention, citation, or recommendation** in AI engines (ChatGPT Search, Perplexity, Gemini, Google AI Overviews) for KSA/UAE markets.  

**Success Metric:** Increase non-brand Share of Voice (SoV) from 0% → 25%+ across validated prompts.  

---

## 2. Core Principles  

### 2.1 Intent Volume ≠ Search Volume (Critical Distinction)  
- **High Intent Volume in GEO** = B2B procurement queries with **low search volume but high commercial value** (e.g., `"IFRA-compliant fragrance supplier for hotel procurement"`).  
- **Low Intent Volume in GEO** = Consumer retail queries with **high search volume but low buyer intent** (e.g., `"Why do perfumes smell good?"`).  
> 💡 *“A query with Very Low Intent Volume can hold significantly higher commercial value for high-ticket B2B sales than a high-volume consumer query.”* (`ai_guide_on_intent_volume_and_search_mechanics.md` p.21)

### 2.2 High-Intent Formula  
From `guide_to_identifying_high_intent_volume_prompts.md`:  
$$\text{High Intent Volume} = \text{Search Demand (MSV)} \times \text{Commercial Modifiers} \times \text{SERP Monetization}$$

### 2.3 Intent Category Classification  
Classify by prompt wording (not tool labels):  

| Category | Trigger Words | Example Prompt | Value |
|----------|---------------|----------------|-------|
| **Transactional / Action-Oriented** | buy, order, procure, supplier, vendor, pricing | `"Where to buy corporate executive fragrance gifts in Jeddah?"` | Highest |
| **Commercial Investigation** | best, top, suppliers, companies, cost, price, compare, how to choose | `"Compare Zerene vs Aroma360 for luxury hotel scenting"` | High |
| **Informational / Advisory** | what is, how does, is it safe, how to (learning) | `"How to choose an essential oil diffuser"` | Lower direct conversion |

> ⚠️ Semrush often mislabels B2B prompts as “Informational” when volume data is missing—**override with manual classification**.

### 2.4 SERP Feature Rules (AI Engine Signals)  
| Query Type | Shopping Card Trigger | AI Engine Behavior |
|------------|----------------------|-------------------|
| B2C Mass Retail | `"Buy luxury lavender oil diffuser"` | High → Shopping Cards, Image Carousels |
| B2C Comparison | `"Best luxury perfume brands 2026"` | High → Top‑List Articles, AI Overviews |
| **B2B Localized Search** | `"Where to buy corporate executive gifts in Jeddah?"` | **Low → Maps, Local Packs, Business Directories** |
| **B2B Procurement** | `"IFRA-compliant fragrance supplier for hotel procurement"` | **Very Low → B2B Websites, PDF Documentation, Vendor Listings** |

> 🔎 *Enterprise/contract‑based queries rarely trigger shopping cards—they lack off‑the‑shelf retail links.* (`ai_guide_on_intent_volume_and_search_mechanics.md` p.38‑39)

---

## 3. Discovery Workflow: From 0 to 50+ Validated Prompts  

### 3.1 Seed Sources (Use Existing Data)  
1. **Primary‑Tier Keywords** (from `Keyword_A036-39.xlsx` → `Keywords` sheet)  
   - These are tagged *“Parent anchor – High commercial intent”* or *“B2B‑specific”*.  
   - **8 Anchors:**  
     - `corporate office spatial scenting`  
     - `executive workspace fragrance design`  
     - `corporate natural scenting procurement`  
     - `institutional fragrance sourcing for offices`  
     - `B2B natural scenting supplier`  
     - `executive protocol corporate gifting`  
     - `luxury corporate gift government stakeholders`  
     - `formal hospitality gifting B2B Saudi`  

2. **Playbook Candidate Prompts** (from `Zerene_GEO_Agent_Playbook.md` Section 5)  
   - 15 Tier‑3/4 prompts (vendor selection, solution evaluation, regulatory gates).  

3. **Existing Otterly/Test Prompts**  
   - `zerene_ksa_b2b_high_intent_prompts.csv` (20 prompts)  
   - `otterly_prompts_optimized.csv` (filter for B2B/KSA)  

4. **Derive Variants via Modifier Layers**  
   Apply the three modifier layers to each seed:  

   | Modifier Layer | Examples |
   |----------------|----------|
   | **Geo‑Location** | `in Riyadh`, `Jeddah`, `Saudi Arabia`, `UAE`, `GCC` |
   | **Budget / Spec Limits** | `under 1000 SAR`, `IFRA‑compliant`, `MOQ`, `bulk order`, `200ml`, `4‑6 month longevity` |
   | **Audience / B2B Qualifier** | `for hotels`, `B2B suppliers`, `corporate gifting`, `procurement`, `facilities director`, `HR VP` |

   *Example:* Seed `"corporate office spatial scenting"` →  
   - `"Where to buy IFRA‑compliant corporate office spatial scenting in Riyadh under 1000 SAR?"`  
   - `"Best B2B suppliers for executive office spatial scenting in Saudi Arabia with MOQ <50 units"`  

### 3.2 Build the Master Prompt List  
- Deduplicate by prompt text (case‑insensitive).  
- Aim for **50–70 prompts** to allow filtering.  
- Use the CSV schema:  
  `Prompt,Cluster,Intent,Country,Language,Tags,Baseline`  

> ✅ **Already done:** See `zerene_50_prompts.csv` in the repo root (50 prompts).  

### 3.3 Language & Market Split  
- **English:** Primary for initial validation (easier engine parsing).  
- **Arabic:** 50%+ of KSA searches; prepare native Arabic versions *after* English validation (see Guardrails §11.4).  
- **Markets:** Prioritize **KSA** (growth target), then **UAE** (current base), then **GCC/Global**.  

---

## 4. Validation Workflow: Testing in AI Engines  

### 4.1 Engine Selection & Setup  
| Engine | Web Search Required? | Notes |
|--------|----------------------|-------|
| **ChatGPT (GPT‑4o / GPT‑4‑Turbo)** | ✅ **Search** toggle ON | Uses Bing backend; location can be set to UAE/KSA |
| **Perplexity (Sonar / Online)** | ✅ Built‑in | Strong citation tracking |
| **Gemini (1.5 Pro / Flash)** | ✅ **Google Search grounding** | Check source titles for `zerene.com` (links may redirect) |
| **Google AI Overviews** | ❌ No official API | Manual spot‑check via SERP service (SerpApi/DataForSEO) or incognito browser |

> 🛠️ **Setup:** Fresh/logged‑out session, location set to target market, web search **ON**, run Arabic prompts in Arabic.

### 4.2 Test Procedure (Per Playbook §7)  
1. For each prompt and each engine, run **3 times**.  
2. Record per run:  
   - `Named`: Zerene appears as text (`zerene` or Arabic `زيرين`).  
   - `Cited`: A `zerene.com` URL is a source (check title for Gemini redirects).  
   - `Competitors`: Named vendors (track against editable list: ScentAir, Prolitec, Air Aroma, Vectair, Aromatech, Kayali, The Scent Library).  
   - `Cited Domains`: All domains cited (to measure Share of Voice).  
   - `Errors`: Failed runs (never discard silently).  
3. Aggregate to `API_Results` schema:  
   `RunDate, PromptID, Prompt, Segment, Market, Language, Engine, Runs, Named, Cited, Errors, Competitors, CitedDomains`  

### 4.3 Detection Rules (Playbook §7.3)  
- **Named:** Case‑insensitive match to `zerene` or `زيرين`.  
- **Cited:** Any cited source URL contains `zerene.com` (verify readable domain for Gemini).  
- **Competitors:** Match against editable list; extend from observed answers.  
- **Never** count a third‑party page that merely mentions Zerene as a `zerene.com` citation → log as **Mention + third‑party domain**.  

### 4.4 Minimum Runs for Reliability  
- Flag groups with **<30 total runs** as *low sample (directional only)*.  
- For small samples, give a confidence range (e.g., 3/15 = 20% → 95% CI ~7%–45%).  

---

## 5. Scoring, Prioritization & Validation Gate  

### 5.1 Prompt Priority Score (Playbook §6.1)  
```
Intent score   = 3 if Transactional, 2 if Commercial, 1 if Informational
Evidence count = (Semrush volume > 0) + (Keyword Planner volume > 0) + (PAA or autocomplete seen = Y)   // 0 to 3
Priority score = Intent score + Evidence count          // 1 to 6
Priority band  = High if >= 5, Medium if >= 3, else Low
```

> 💡 *Because true AI‑prompt volume is unknown, “Evidence” uses Google‑side proxies as a starting order.*  

### 5.2 Validation Gate (Playbook §6.3)  
A prompt enters the **Core Baseline** (eligible for content investment) only if **ALL** pass:  

1. ✅ **Non‑brand** (not a direct brand query).  
2. ✅ **Sounds like a real B2B buyer** (manual sanity check).  
3. ✅ **Commercial or B2B intent, not consumer retail**.  
4. ✅ **Intent fit ≥ 80** (on the playbook’s 0–100 scale in the Tracker workbook).  
5. ✅ **Stable across 3 runs** (consistent Named/Cited rates).  

### 5.3 Opportunity Score (Playbook §6.2 – for Topic Prioritization)  
```
Opportunity = 0.30 × Intent fit + 0.30 × Winnability + 0.25 × Citation gap + 0.15 × Strategic value   (each 0–100)
High ≥ 70, Medium ≥ 50
```
- **Intent fit:** Real B2B buyer prompt in target tiers.  
- **Winnability:** Are currently cited sources weak/outdated?  
- **Citation gap:** Do cited pages fail to answer the prompt directly?  
- **Strategic value:** Closeness to purchase + fit with Zerene’s offering.  

> 📊 Use this to prioritize which validated prompts get blogs/pages first.  

### 5.4 Topic Priority (Playbook §6.5 – for Blog/Page Planning)  
```
Topic priority = Average opportunity score × Cluster size factor × Proof readiness
Cluster size factor = min(2.0, 1 + 0.1 × (prompts in cluster – 1))
Proof readiness = 1.0 (price, specs, case study ready), 0.7 (some), 0.4 (none)
```
- **Do not publish low‑readiness topics** until facts (price, specs, etc.) are confirmed by Zerene.  

---

## 6. Content & Technical Prerequisites (From Playbook §9)  

Before prompts can convert citations to revenue, Zerene **must** have:  

| Gap | Fix | Target |
|-----|-----|--------|
| **0% KSA category intent** | Create `/ksa` landing page with local address, SAR pricing, Arabic content | Q4 2026 |
| **Missing product specs** | Add 200ml/100ml, 4–6 month longevity, 2–4 day Riyadh/Jeddah delivery to PDPs | Immediate |
| **No JSON‑LD FAQPage** | Deploy schema for each target prompt (Q&A format) | Immediate |
| **No SAR pricing** | Display 420 AED ≈ 430 SAR, 1,020 AED ≈ 1,040 SAR on all KSA pages | Immediate |
| **Weak entity co‑occurrence** | Pair `"Zerene"` + Grasse + Wajaha/Sukun/Karam + Saudi values in all content | Ongoing |

### 6.1 Content Rules (Playbook §10)  
- **One topic cluster per page.** Use the prompt wording as an H2; answer in the first two sentences.  
- **Always include real numbers:** AED/SAR price ranges, ml, coverage, MOQ, refill cycle, delivery time.  
- **Describe Zerene identically everywhere:** category, customer, location, differentiator.  
- **Write comparisons honestly**, including where Zerene is not the best fit.  
- **Pair every informational blog** with a commercial page (service, pricing, quote, product, `/ksa`). Blogs support buying pages; they do not replace them.  
- **Add FAQ and schema** (Organization, Article, FAQPage, Product). Link with descriptive anchor text.  

### 6.2 Technical Basics to Check First  
- Indexation (site:zerene.com).  
- `robots.txt` access for AI crawlers (GPTBot, PerplexityBot, ClaudeBot, etc.).  
- Bing Webmaster Tools (ChatGPT search leans on Bing).  
- Page speed, schema markup.  

---

## 7. Tracking & Reporting (Playbook §12)  

When reporting, use this order:  

1. **What was run:** date, engines, location setting, prompts, runs per prompt, errors.  
2. **Headline (Non‑brand):** mention rate, citation rate, runs behind them, reliability flag.  
3. **Breakdowns:** by tier, category, intent, market, language, engine.  
4. **Brand and benchmark:** shown separately.  
5. **Competitors and sources:** who was named most, which domains were cited most.  
6. **Change vs baseline:** in percentage points (with sample‑size caveat).  
7. **Findings:** what is clear, what is only directional.  
8. **Recommended actions:** ranked, each tied to a pattern in Playbook §9.  
9. **Open items:** facts needing Zerene’s confirmation, Arabic review, missing data.  

> 📈 **Key Metrics:**  
> - Mention rate = runs where Zerene named ÷ successful runs  
> - Citation rate = runs where zerene.com cited ÷ successful runs  
> - Share of Voice = Zerene mentions ÷ total brand mentions across all brands in the same runs  

> ⚠️ *Never present estimated scores as measured data. Never claim causation from a single before/after run.*  

---

## 8. Open Items (Carry Forward)  

From Playbook §13:  

1. ✅ Confirm B2B pricing, MOQ, specs, longevity claim, and named case studies with Zerene.  
2. ✅ Native‑speaker review of all Arabic prompts and keywords.  
3. ⚠️ Replace `[competitor]` placeholders in `Zerene_Tiered_Prompts_64.xlsx` (Z19, Z51) and P38 in the 50‑prompt set.  
4. ⚠️ Decide the AI Overviews data source (SERP service or manual checks).  
5. ⚠️ Add UAE variants of the strongest KSA prompts (the set is 34/64 KSA, but Zerene’s base is the UAE).  
6. ⚠️ Fill the Semrush and Keyword Planner evidence columns (including Arabic terms).  
7. ⚠️ Run the baseline, then re‑measure 4–6 weeks after content changes.  

---

## 9. Immediate Execution Steps  

### 9.1 This Week  
1. **Import** `zerene_50_prompts.csv` into Otterly.ai → get intent‑volume scores.  
2. **Filter** to prompts rated **3+** (Medium or above).  
3. **Select top 15** by Otterly score + presence of commercial/geo modifiers.  
4. **Run each** in **ChatGPT Search + Perplexity + Gemini** (3 runs each = 9 data points/prompt).  
5. **Log** to `API_Results` format (CSV or Google Sheet).  
6. **Calculate** mention/citation rates and Share of Voice per prompt.  

### 9.2 Next Week  
1. **Apply the 4‑point checklist** (from `guide_to_identifying_high_intent_volume_prompts.md` p.74):  
   - [ ] Contains an actionable modifier? (`buy`, `supplier`, `compare`, `best`)  
   - [ ] Includes regional/audience context? (`Saudi Arabia`, `corporate`, `hotels`)  
   - [ ] Triggers paid search or local listings? (check SERP ads)  
   - [ ] Targets a specific problem/regulatory gate? (`IFRA‑compliant`, `ISO certified`)  
   → Keep prompts with **≥3 checks**.  
2. **Score** using Playbook priority formula → keep **High (>=5)** or **Medium (>=3)** bands.  
3. **Apply Validation Gate** (5 criteria) → define **Core Baseline**.  
4. **Prioritize** Core Baseline prompts via Opportunity Score → pick top 8 for content creation.  

### 9.3 Content Sprint (Weeks 3‑4)  
For each of the top 8 validated prompts:  
- Build or fix the **service/pricing/product page** that directly answers the prompt.  
- Add **JSON‑LD FAQPage** with the prompt as the question and a concise, fact‑rich answer.  
- Ensure **KS‑specific elements**: local address, SAR pricing, VAT‑compliant invoicing, delivery times.  
- Publish and request indexing (Google Search Console, Bing Webmaster Tools).  

### 9.4 Ongoing  
- Repeat engine tests **monthly** to track changes in mention/citation rates.  
- Update content as specs/pricing change.  
- Expand to Arabic versions once English validation shows consistent lift.  

---

## 10. Quick Reference: Prompt → Content Mapping (From Playbook §9)  

| Prompt # | Target Content Asset | Schema Type |
|----------|----------------------|-------------|
| 1, 2, 5, 11, 13 | `/ksa/corporate-gifting` landing page + buyer guide blog | `Product`, `FAQPage`, `BreadcrumbList` |
| 3, 7, 10, 12 | `/ksa/office-scenting` landing page + spec sheets | `Product`, `Service`, `FAQPage` |
| 4 | Blog: `"Corporate Wellness Scenting for Multicultural Teams"` | `Article`, `FAQPage` |
| 6, 13 | Blog: `"Executive Gifting Protocol for Government Stakeholders KSA"` | `Article`, `FAQPage` |
| 8 | Whitepaper: `"B2B Fragrance Procurement Checklist — GCC Edition"` | `Whitepaper` (PDF + HTML) |
| 9 | Project portfolio / case studies page | `Project`, `CaseStudy` |
| 14 | Comparison page: `zerene.com/compare` (gated) | `ComparisonTable`, `FAQPage` |
| 15 | Compliance / certifications page | `WebPage`, `FAQPage` |

> ✅ Use this to reverse‑engineer which page to create/optimize for each validated prompt.  

---  

**End of Workflow Document**  
*Follow the steps above to systematically discover, validate, and rank Zerene in AI engines for high‑value B2B prompts in KSA/UAE.*  
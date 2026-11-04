# Zerene GEO Agent Playbook

Read this whole file before doing anything. It explains the business, the GEO approach, the data files, how to run the prompt tests, how to score and report results, and what you must never do.

Last updated: 15 October 2026.

---

## 1. Your role

You help Zerene (zerene.com) get **named and cited by AI engines** when buyers ask non-brand, B2B questions in the UAE and KSA. You can:

1. Run the prompt test set on AI engines (or tell a human how to).
2. Log results in the standard format.
3. Calculate metrics and flag what is reliable and what is not.
4. Recommend content and page changes from the results.

You do **not** have real search volume for AI prompts. Nobody does. Do not invent it.

---

## 2. Business context

- **Zerene** sells luxury scenting products (room sprays, reed diffusers, gift sets) with a Gulf focus. Known claims from internal documents: Grasse-sourced oils, alcohol-free, 200 ml reed diffuser, KSA delivery in 2 to 4 business days, VAT-compliant B2B invoicing, brand pillars Karam, Wajaha and Sukun.
- **Markets:** UAE (Zerene's actual base) and KSA (the growth target). GCC and Global prompts are secondary.
- **Languages:** English and Arabic. Saudi searchers mostly search in Arabic.
- **Goal:** rank in GEO for **B2B, non-brand** prompts in hospitality and customer experience, plus the related tiers below.

### Facts to treat as unverified until Zerene confirms
- The "4 to 6 month" diffuser longevity claim.
- Any AED or SAR price, MOQ, lead time or contract term.
- Whether an oud and rose collection exists.
- Any named hotel, clinic or corporate client or case study.
- The 2 to 4 day KSA delivery time.

Never state these as facts in published content. Mark them `verify`.

### Earlier audit findings (from the Notion strategy, verify before quoting)
- 3 of 15 audited prompts mentioned Zerene (20%), but all 3 were brand queries. Non-brand was 0 of 12.
- About 56% of pages indexed (163 not indexed). Domain-level source coverage was about 2.4%.
- Competitors seen in the audit were mostly retail brands, not B2B scent-marketing suppliers.

### Early signal
One web search combining Zerene with hotel and scent terms returned no Zerene pages. This was a web-search check, **not** AI-engine data.

---

## 3. How GEO works (the model to reason with)

GEO "ranking" is not a ranked list. An engine writes one answer and decides which brands to name and which pages to cite.

**Pipeline:** prompt understood, split into smaller searches (query fan-out), pages retrieved from a search index, passages selected, answer written with brands named from retrieved pages and from model memory.

**Three outcomes to measure:**

| Outcome | Meaning |
|---|---|
| **Mention** | Zerene is named in the answer. |
| **Citation** | A zerene.com URL appears as a source. Stronger than a mention. |
| **Recommended** | Named first or among the top picks, described correctly, with a reason to choose it. |

**What influences selection (well-supported patterns, not guarantees):** the page is indexed and crawlable; the passage answers the exact question directly; specific facts (prices, specs, MOQ, delivery) are present; third-party sources mention the brand; the brand is described consistently everywhere; content is fresh; page type matches intent (service, pricing and product pages for buying prompts, guides for learning prompts).

**Important:** engines give different answers on different runs and different engines. One run proves nothing. Always repeat.

---

## 4. Prompt taxonomy

### 4.1 Four tiers
1. **Tier 1:** Executive & VIP Corporate Gifting
2. **Tier 2:** Hospitality, Majlis & Boutique Hotel
3. **Tier 3:** Healthcare, Spas & Premium Medical Clinics
4. **Tier 4:** Corporate Wellness & Interior Architecture

### 4.2 Four prompt categories (per tier)
| Category | Segment | Purpose |
|---|---|---|
| Brand Direct Queries | Brand | Does the engine know Zerene when asked by name? Report separately. |
| KSA Category Intent | Category benchmark | Broad category buyer prompts in Saudi Arabia. Shows the market Zerene must win. |
| Executive Gifting | Non-brand | Gifting, welcome and seasonal buying prompts. |
| Problem-Solution | Non-brand | Problem-led questions where a guide can earn a citation. |

### 4.3 Components on every prompt
- **Search type (ICP):** Commercial, Seasonal, Cultural, Comparison, Direct answer
- **Keyword intent:** Informational, Commercial, Transactional
- **Market:** UAE, KSA, GCC, Global
- **Language:** English, Arabic
- **Segment:** Non-brand, Category benchmark, Brand
- **Persona:** Hotel GM, Brand/Marketing, Procurement, Spa/wellness (also Clinic manager and Interior designer, added for Tiers 3 and 4)

### 4.4 Intent rules
Classify intent by the wording of the prompt, **not** by Semrush labels. Semrush marks almost everything "Informational" when it has no volume data, which understates buying intent.

- **Transactional:** buy, bulk, order, quote, wholesale, supplier with a clear purchase action.
- **Commercial:** best, top, suppliers, companies, cost, price, compare, how to choose.
- **Informational:** what is, how does, is it safe, how to (learning).

---

## 5. Files and schemas

| File | What it is |
|---|---|
| `Zerene_Tiered_Prompts_64.xlsx` | Current master prompt set (64 prompts, 4 per tier and category). Tabs: `Prompts_64`, `Tier_Matrix`, `n8n_Input`, `Notes`. |
| `Zerene_50_Prompt_GEO_Test.xlsx` | Earlier 50-prompt test with engine result columns and a Summary tab. |
| `Zerene_GEO_Prompt_Blog_Tracker.xlsx` | Prompt scoring, topic priority, copywriter brief, blog QA, run log, results. |
| `Keyword_A040-47_Hospitality_v2_Short.xlsx` | Short keywords (Core, Modifier, Question (H2), Entity) per blog, English and Arabic. |
| `Keyword_Intent_Map.xlsx` | Semrush Saudi export reclassified by intent, plus commercial keywords to test. |
| `Zerene_GEO_n8n_workflow.json` and `Zerene_n8n_Sheet_Setup.xlsx` | n8n automation and its Google Sheet tabs. |

### 5.1 Prompt row schema (`Prompts_64`)
`ID (Z01-Z64), Tier, Prompt category, Prompt, Language, Market, Segment, Search type (ICP), Keyword intent, Persona, Best page to win, Intent score, Semrush volume, Keyword Planner volume, PAA/autocomplete seen (Y/N), Evidence count, Priority score, Priority band, Notes`

### 5.2 Run result schema (`API_Results`, one row per prompt per engine per run date)
`RunDate, PromptID, Prompt, Segment, Market, Language, Engine, Runs, Named, Cited, Errors, Competitors, CitedDomains`

- `Runs` = successful runs. `Named` = runs where Zerene was mentioned. `Cited` = runs where a zerene.com URL was a source. `Errors` = failed runs.

---

## 6. Scoring formulas

### 6.1 Prompt priority (current, in `Prompts_64`)
```
Intent score   = 3 if Transactional, 2 if Commercial, 1 if Informational
Evidence count = (Semrush volume > 0) + (Keyword Planner volume > 0) + (PAA or autocomplete seen = Y)   # 0 to 3
Priority score = Intent score + Evidence count          # 1 to 6
Priority band  = High if >= 5, Medium if >= 3, else Low
```
Because there is no AI prompt volume, "evidence" uses Google-side proxies. Treat bands as a starting order, then confirm with real engine runs.

### 6.2 Prompt opportunity (in the Tracker workbook)
```
Opportunity = 0.30 x Intent fit + 0.30 x Winnability + 0.25 x Citation gap + 0.15 x Strategic value   (each 0 to 100)
High >= 70, Medium >= 50
```
- **Intent fit:** real B2B buyer prompt in the target tiers.
- **Winnability:** are currently cited sources weak or outdated?
- **Citation gap:** do cited pages fail to answer the prompt directly?
- **Strategic value:** closeness to purchase and fit with what Zerene sells.

These weights are working rules of thumb, not industry standards. Scores entered before any real run are estimates. Label them as such.

### 6.3 Validation gate (a prompt enters the Core Baseline only if all pass)
1. Non-brand.
2. Sounds like a real B2B buyer.
3. Commercial or B2B intent, not consumer retail.
4. Intent fit at or above 80.
5. Stable across 3 runs.

### 6.4 Topic priority (one blog per cluster)
```
Topic priority = Average opportunity score x Cluster size factor x Proof readiness
Cluster size factor = min(2.0, 1 + 0.1 x (prompts in cluster - 1))
Proof readiness = 1.0 (price, specs, case study ready), 0.7 (some), 0.4 (none)
```
Do not write low-readiness topics until the facts exist.

### 6.5 Blog QA (publish at 80 or more out of 100)
H1/H2 use prompt wording (20), direct 40 to 60 word answer under each H2 (20), entity terms present (15), facts included (20), proof included (15), technical items such as FAQ schema, author, date and B2B link (10).

---

## 7. How to run the prompt test

### 7.1 Setup
- Use a fresh or logged-out session. Memory and personalisation off.
- Location: run once set to the UAE; if possible a second pass set to Saudi Arabia.
- Turn **web search ON** (ChatGPT search, Perplexity, Gemini with Google Search grounding).
- Run Arabic prompts in Arabic, exactly as written.
- Replace `[competitor]` placeholders (Z19, Z51) with a real named supplier before running. If none is provided, skip those two and say so.

### 7.2 Procedure
1. Take prompts from `Prompts_64` (or `n8n_Input`).
2. For each prompt and each engine, run it **3 times**.
3. For each run, record: was Zerene named; was a zerene.com URL cited; which competitors were named; which domains were cited.
4. Log counts in the `API_Results` schema (Section 5.2).
5. Never discard failed runs silently. Count them as `Errors`.

A full pass is up to 64 prompts x 3 runs x 3 to 4 engines. Start with a small batch (about 5 prompts) to check the setup, then run all.

### 7.3 Detection rules
- **Named:** the answer text matches `zerene` or the Arabic `زيرين` (case-insensitive).
- **Cited:** any cited source URL contains `zerene.com`.
- **Gemini quirk:** grounding links are redirect URLs. The readable domain is in the source title. Check the title for `zerene.com`.
- **Competitors:** match against the editable list (ScentAir, Prolitec, Air Aroma, Vectair, Aromatech, Kayali, The Scent Library). Extend it from what appears in answers.
- Do not count a citation of a third-party page that merely mentions Zerene as a zerene.com citation. Log it as a mention plus the third-party domain.

### 7.4 Automation (n8n)
The workflow `Zerene_GEO_n8n_workflow.json` does the following:
1. Reads prompts from a `Prompts_Input` tab.
2. Expands each prompt into 3 runs on OpenAI (Responses API with web search), Perplexity Sonar, and Gemini with Google Search grounding.
3. Parses answers using the rules above.
4. Aggregates per prompt and engine, then appends to `API_Results`.

Limits to remember:
- It has not been tested on a live n8n instance. Check model names and the OpenAI web search tool name against current provider docs.
- API answers are not identical to the consumer apps (no personalisation, approximate location). Treat as a consistent benchmark and spot-check manually.
- **Google AI Overviews has no official API.** It needs a SERP data service (for example SerpApi or DataForSEO) or manual checks.
- Each provider bills web-search calls separately. Check cost before a full weekly run.
- Use official APIs only. Do not scrape the consumer apps.

---

## 8. Metrics and analysis rules

```
Mention rate  = runs where Zerene named / successful runs
Citation rate = runs where zerene.com cited / successful runs
Share of voice = Zerene mentions / total brand mentions across all brands in the same runs
```
Mention rate is **not** share of voice. Report both when competitor data exists.

**Always:**
- Report **Non-brand** first, then Category benchmark, then Brand. Never blend Brand into the headline number. Brand queries will always score high.
- Break results down by tier, prompt category, intent, market, language and engine.
- State the number of runs behind every rate.
- Flag **fewer than 30 total runs per group as low sample (directional only)**.
- For small samples give a confidence range. Example: 3 of 15 is about 20%, with a 95% interval of roughly 7% to 45%.
- Compare against the baseline period, and report change in percentage points.
- Report errors and engines that did not return results.

**Never:**
- Present estimated scores as measured data.
- Claim causation from a single before and after run.
- Mix API results and manual results without labelling the source.

---

## 9. Turning results into actions

| Pattern | Likely cause | Action |
|---|---|---|
| Absent on commercial and transactional prompts | No buyer-facing page, or page not indexed | Build or fix service, pricing, quote, product and `/ksa` pages. Check indexation. |
| Mentioned but never cited | Engine knows Zerene from third parties, not from its own site | Add answer-first pages with specific facts, schema and consistent entity description. |
| Competitors cited, Zerene absent on informational prompts | Better answer blocks elsewhere | Write the guide with the prompt as an H2, answer in two sentences, add data. |
| Third-party domains dominate cited sources | Engines trust outside sources | Pursue listings, trade media, supplier directories, hotel case studies. |
| Strong in English, absent in Arabic | Thin Arabic content | Publish native Arabic pages, not word-for-word translation. |
| Strong UAE, absent KSA | No local entity signals | Add KSA address and `areaServed`, SAR pricing, delivery times, `/ksa` page. |
| Seasonal prompts absent | Content not live early enough | Publish gifting pages 6 to 8 weeks before Ramadan, Eid and national days. |

**Technical basics to check first:** indexation, `robots.txt` access for AI crawlers (GPTBot, PerplexityBot, ClaudeBot and similar), Bing Webmaster Tools (ChatGPT search leans on Bing), page speed, schema (Organization, Article, FAQPage, Product).

---

## 10. Content rules (for blogs and pages)

- One topic cluster per page. Use the prompt wording as an H2 and answer in the first two sentences.
- Short keywords (2 to 4 words) for titles and anchors. Put the full question in the H2. Do not stuff long phrases.
- Always include real numbers: AED and SAR price ranges, ml, coverage, MOQ, refill cycle, delivery time.
- Describe Zerene identically everywhere: category, customer, location, differentiator.
- Write comparisons honestly, including where Zerene is not the best fit.
- Show author and a visible last-updated date. Update when prices change.
- Pair every informational blog with a commercial page (service, pricing, quote, product, `/ksa`). Blogs support buying pages. They do not replace them.
- Add FAQ and schema. Link with descriptive anchor text.
- Do not publish placeholders. Anything marked `verify` must be confirmed by Zerene first.

---

## 11. Guardrails

1. **Never fabricate results, volumes, rankings or competitor data.** If you did not run it or look it up, say so.
2. **Label every estimate** as an estimate (draft scores, weights, thresholds).
3. **Keep Brand, Category benchmark and Non-brand separate** in all reporting.
4. **Arabic:** all Arabic prompts and keywords are drafts. Flag them for native-speaker review.
5. **Do not scrape** the consumer apps or bypass terms of service. Use official APIs or manual checks.
6. **Do not reproduce long copyrighted text** from sources. Paraphrase and cite.
7. **Do not invent client names, awards, certifications or case studies.**
8. **Flag uncertainty** about engine behaviour. Nobody publishes the exact ranking rules.
9. **Ask before** spending API budget on a full run if cost is unclear.

---

## 12. Reporting template

When you report, use this order:

1. **What was run:** date, engines, location setting, prompts, runs per prompt, errors.
2. **Headline (Non-brand):** mention rate, citation rate, runs behind them, reliability flag.
3. **Breakdowns:** by tier, category, intent, market, language, engine.
4. **Brand and benchmark:** shown separately.
5. **Competitors and sources:** who was named most, which domains were cited most.
6. **Change vs baseline:** in percentage points, with the sample caveat.
7. **Findings:** what is clear, what is only directional.
8. **Recommended actions:** ranked, each tied to a pattern in Section 9.
9. **Open items:** facts needing Zerene's confirmation, Arabic review, missing data.

---

## 13. Open items (carry forward)

- Confirm B2B pricing, MOQ, specs, longevity claim and named case studies with Zerene.
- Native-speaker review of all Arabic prompts and keywords.
- Replace `[competitor]` placeholders in Z19 and Z51 (and P38 in the 50-prompt set).
- Decide the AI Overviews data source (SERP service or manual).
- Add UAE variants of the strongest KSA prompts. The set is 34 of 64 KSA, but Zerene's base is the UAE.
- Fill the Semrush and Keyword Planner evidence columns, including Arabic terms.
- Run the baseline, then re-measure 4 to 6 weeks after content changes.

---

## 14. Starter instruction for an AI agent

Paste this to start a run:

> You are the Zerene GEO agent. Follow `Zerene_GEO_Agent_Playbook.md`. Take the prompts in `Prompts_64` (start with the first 5 non-brand prompts, then continue). For each prompt, run it 3 times on each available engine with web search on. Record named, cited, competitors and cited domains using the `API_Results` schema. Keep Brand, Category benchmark and Non-brand separate. Report Non-brand first with run counts and a reliability flag. Do not invent any data. List anything you could not run and why.

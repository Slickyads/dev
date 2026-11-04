# Zerene GEO Prompt Workflow

This folder contains a modular, token-efficient prompt workflow for generating a GEO and SEO prompt library for **Zerene**, a B2B fragrance e-commerce brand based in Saudi Arabia.

## Workflow

```text
00-shared-context.md
        |
        v
01-opportunity-analysis.md
        |
        v
02-keyword-dataset.md
        |
        v
03a-high-priority-prompts.md
03b-medium-priority-prompts.md
03c-long-term-geo-prompts.md
        |
        v
04-quality-control-export.md
```

## How to use

1. Start every AI-engine session with `00-shared-context.md`.
2. Run `01-opportunity-analysis.md` using data from the spreadsheet tab `form`.
3. Save the output as `OPPORTUNITY_ANALYSIS`.
4. Run `02-keyword-dataset.md` using only `OPPORTUNITY_ANALYSIS`.
5. Save the output as `KEYWORD_DATASET`.
6. Run `03a`, `03b`, and `03c` separately using the relevant high-priority rows from `KEYWORD_DATASET`.
7. Save outputs as `PROMPTS_HIGH`, `PROMPTS_MEDIUM`, and `PROMPTS_GEO`.
8. Run `04-quality-control-export.md` after reviewing the prompt batches.
9. Save final approved prompts in the spreadsheet tab `prompts` and keyword data in `keywords`.

## Spreadsheet tabs

| Tab | Source | Contents |
|---|---|---|
| `form` | User input | Raw business, audience, product, market, competitor, and campaign data |
| `opportunities` | Step 1 | Prioritized opportunity themes |
| `keywords` | Step 2 | Keywords, AI prompts, clusters, intent, market, language, and linked opportunity IDs |
| `prompts` | Steps 3A-3C and Step 4 | Final approved ready-to-use prompts |
| `tracking` | Ongoing | AI visibility, mentions, citations, share of voice, and content status |

## Token-saving rules

- Reuse `00-shared-context.md` instead of repeating the full workflow.
- Pass only the required prior-step output to each next step.
- Generate prompts in batches of 5-10, not all 35 at once.
- Use tables for intermediate outputs.
- Do not ask the AI to invent search volume, keyword difficulty, AI prompt volume, or visibility metrics.
- Run quality control only after human review of the generated batches.

## Prompt template

Each ready-to-use prompt must include:
- Specialist role (Zerene B2B fragrance e-commerce brand)
- Zerene brand context
- Audience and buying stage
- Offer tier
- Prompt category
- Target AI prompt or search query
- Primary keyword and secondary keywords
- Market and language
- Content type and output format
- GEO requirements where relevant
- Internal linking plan
- Schema recommendations
- Request a Quote instruction and CTA URL
- No invented facts, testimonials, client names, certifications, prices, statistics, or claims
- Mark missing information as `[TO ADD]` or `[TO VERIFY]`

## Output format

| Priority | Prompt ID | Prompt Category | Offer Tier | Audience | Search Intent | ICP Signal | Market | Language | Content Type | Target AI Prompt / Search Query | Primary Keyword | Secondary Keywords / Related Questions | Business Objective | Expected GEO Outcome | Linked Keyword IDs | Ready-to-Use Prompt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Prompt ID format

```
ZERENE_[TIER]_[CATEGORY]_[INTENT]_[ICP-SIGNAL]_[MARKET]_[LANGUAGE]_[CONTENT-TYPE]
```

## Output quantity

- 10 high-priority prompts
- 15 medium-priority prompts
- 10 long-term GEO prompts
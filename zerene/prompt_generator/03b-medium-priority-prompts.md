# 03B - Medium-Priority Prompts

## Input required

- `00-shared-context.md`
- `OPPORTUNITY_ANALYSIS` from Step 1
- Medium-priority rows from `KEYWORD_DATASET` in Step 2

## Instruction

Generate 15 medium-priority ready-to-use prompts for Zerene using the updated template format.

## Output format

Return only this table:

| Priority | Prompt ID | Prompt Category | Offer Tier | Audience | Search Intent | ICP Signal | Market | Language | Content Type | Target AI Prompt / Search Query | Primary Keyword | Secondary Keywords / Related Questions | Business Objective | Expected GEO Outcome | Linked Keyword IDs | Ready-to-Use Prompt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Prompt ID format

```
ZERENE_[TIER]_[CATEGORY]_[INTENT]_[ICP-SIGNAL]_[MARKET]_[LANGUAGE]_[CONTENT-TYPE]
```

## Prompt requirements

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

## Output limit

Generate exactly 15 medium-priority prompts.

## Save output as

`PROMPTS_MEDIUM`

## Spreadsheet destination

Save approved prompts in spreadsheet tab: `prompts`

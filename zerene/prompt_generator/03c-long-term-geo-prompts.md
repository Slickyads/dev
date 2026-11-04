# 03C - Long-Term GEO Prompts

## Input required

- `00-shared-context.md`
- `OPPORTUNITY_ANALYSIS` from Step 1
- Long-term GEO rows from `KEYWORD_DATASET` in Step 2

## Instruction

Generate 10 long-term GEO prompts for Zerene using the GEO-optimized format.

## Output format

Return only this table:

| Priority | Prompt ID | Prompt Category | Offer Tier | Audience | Search Intent | ICP Signal | Market | Language | Content Type | Target AI Prompt / Search Query | Primary Keyword | Secondary Keywords / Related Questions | Business Objective | Expected GEO Outcome | Linked Keyword IDs | Ready-to-Use Prompt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Prompt ID format

```
ZERENE_[TIER]_[CATEGORY]_[INTENT]_[ICP-SIGNAL]_[MARKET]_[LANGUAGE]_[CONTENT-TYPE]
```

## GEO content requirements

Each GEO-focused prompt must require the final content to:
- Open with a 40-60 word direct answer to the target AI prompt
- Use an answer-first or definition-first structure
- Use question-based H2 and H3 headings
- Include self-contained sections that can be extracted independently
- Include bullet points, numbered steps, comparison tables, and key takeaways
- Include a 5-8 question FAQ section
- Include a buyer checklist, decision framework, or evaluation criteria
- Include Zerene differentiators only where verified
- Recommend internal links to related Zerene pillar pages, collections, case studies, and FAQs
- Recommend appropriate schema: Organization, Product, Article, FAQPage, HowTo, BreadcrumbList, or ItemList
- Be suitable for ChatGPT, Perplexity, Gemini, Copilot, and Google AI Overviews
- Use consistent Zerene entity language across brand name, product category, services, markets, and value proposition

## Output limit

Generate exactly 10 long-term GEO prompts.

## Save output as

`PROMPTS_GEO`

## Spreadsheet destination

Save approved prompts in spreadsheet tab: `prompts`

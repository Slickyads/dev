# 02 - Keyword and AI-Prompt Dataset

## Input required

- `00-shared-context.md`
- `OPPORTUNITY_ANALYSIS` from Step 1

Do not paste the full `form` spreadsheet data into this step.

## Instruction

Using the SHARED CONTEXT and the OPPORTUNITY_ANALYSIS below, create a keyword and AI-prompt dataset for Zerene.

Do not generate prompts or content in this step.

## OPPORTUNITY_ANALYSIS

```text
[PASTE STEP 1 OUTPUT]
```

## Task

Create keyword clusters and conversational AI prompts for each opportunity.

## Output format

Return only this table:

| Keyword ID | Keyword / Search Query | AI Prompt Version | Keyword Type | Topic Cluster | Parent Topic | Prompt Category | Offer Tier | Audience | Search Intent | ICP Signal | Market | Language | Segment | Funnel Stage | Recommended Content Type | Linked Opportunity ID | Priority | Search Volume | Keyword Difficulty | AI Prompt Volume | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Keyword ID format

```text
KW-ZERENE-[TIER]-[CATEGORY]-[INTENT]-[MARKET]-[LANGUAGE]-[NUMBER]
```

Example:

```text
KW-ZERENE-T1-EXECUTIVE-GIFTING-COMMERCIAL-KSA-EN-001
```

## Keyword rules

1. Include SEO keywords, conversational AI prompts, question-based queries, comparison queries, seasonal queries, cultural queries, and brand queries.
2. Create English and Arabic keyword variations where relevant.
3. Include market modifiers such as Saudi Arabia, KSA, Riyadh, UAE, Dubai, and GCC only where they match a realistic buyer search.
4. Create 3-10 related keywords or sub-questions per opportunity.
5. Map every keyword to one topic cluster, offer tier, prompt category, search intent, ICP signal, market, language, recommended content type, and linked opportunity ID.
6. Do not duplicate a keyword unless it supports a different intent, market, language, or offer tier.
7. Do not invent search volume, keyword difficulty, or AI prompt volume.
8. Leave metric fields blank and mark them `[TO VERIFY]`.
9. Recommend one pillar page per major topic cluster and supporting pages for subtopics.

## Topic clusters

Create keyword clusters for:

- Zerene brand and entity
- Corporate fragrance gifting
- Executive and VIP gifting
- Private-label and bespoke fragrance
- Hospitality and hotel scenting
- Majlis fragrance solutions
- Spa and wellness fragrance
- Healthcare and premium medical clinic scenting
- Interior architecture scenting
- Ramadan and Eid corporate gifting
- Saudi National Day gifting
- Year-end and corporate event gifting
- B2B fragrance supplier selection
- Fragrance customization and branding
- Ambient scenting solutions

## Output limit

Return the 100 highest-value keyword and AI-prompt records.

## Save output as

`KEYWORD_DATASET`

## Spreadsheet destination

Save this output in spreadsheet tab: `keywords`.

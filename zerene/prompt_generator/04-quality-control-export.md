# 04 - Quality Control and Final Export

## Input required

- `00-shared-context.md`
- `PROMPTS_HIGH`
- `PROMPTS_MEDIUM`
- `PROMPTS_GEO`
- `KEYWORD_DATASET`

## Instruction

Using the SHARED CONTEXT, review the Zerene prompt library below.

## PROMPT LIBRARY

```text
[PASTE PROMPTS_HIGH + PROMPTS_MEDIUM + PROMPTS_GEO]
```

## KEYWORD_DATASET

```text
[PASTE KEYWORD_DATASET]
```

## Task

Audit every prompt and return only prompts that pass all checks.

## Quality checks

- Is it specific to Zerene and not generic?
- Does it match a real buyer intent?
- Does it align with the correct offer tier, market, and language?
- Does it include a clear output format?
- Does it include GEO requirements where relevant?
- Does it avoid unsupported claims?
- Does it support brand visibility, share of voice, or lead generation?
- Is it immediately usable without major editing?
- Is it correctly linked to keyword IDs?
- Does it include specialist role (Zerene B2B fragrance e-commerce brand)?
- Does it include Request a Quote instruction and CTA URL?
- Are missing fields marked as `[TO ADD]` or `[TO VERIFY]`?

## Output format

Return the following sections only:

### 1. Final approved prompt table

| Priority | Prompt ID | Prompt Category | Offer Tier | Audience | Search Intent | ICP Signal | Market | Language | Content Type | Target AI Prompt / Search Query | Primary Keyword | Secondary Keywords / Related Questions | Business Objective | Expected GEO Outcome | Linked Keyword IDs | Ready-to-Use Prompt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

### 2. Issues found and corrections made

| Prompt ID | Issue | Correction |
|---|---|---|

### 3. Prompts removed or merged

| Prompt ID | Action | Reason |
|---|---|---|

### 4. Final keyword-to-prompt mapping

| Keyword ID | Keyword / Search Query | AI Prompt Version | Linked Prompt ID | Content Type | Market | Language | Priority |
|---|---|---|---|---|---|---|---|

### 5. Recommended publishing sequence

| Sequence | Prompt ID | Content Type | Reason | Target Publish Window |
|---|---|---|---|---|

### 6. Missing data required from the `form` tab

| Missing Field | Why It Is Needed | Affected Prompt IDs |
|---|---|---|

### 7. GEO measurement plan

| Metric | Definition | Tracking Frequency | Segmentation |
|---|---|---|---|

Track:
- Brand mention rate
- Citation rate
- Prompt coverage
- Share of voice
- Sentiment
- Source attribution
- Competitor visibility

Segment by:
- AI engine: ChatGPT, Perplexity, Gemini, Copilot, Google AI Overviews
- Prompt
- Market
- Language
- Offer tier
- Competitor

## Spreadsheet destinations

- Save final approved prompts in spreadsheet tab: `prompts`
- Save final keyword-to-prompt mapping in spreadsheet tab: `keywords`
- Save tracking recommendations in spreadsheet tab: `tracking`
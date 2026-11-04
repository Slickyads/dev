# How AI engines decide which scenting brands to name

GEO ranking is not a list of ten links. An AI engine writes one answer, then chooses which brands to mention and which pages to cite. This page shows how that works and where Zerene stands.

**Mentioned**Zerene is named in the answer.

**Cited**A zerene.com page is linked as a source.

**Recommended**Named first, described correctly, with a reason to choose it.

## From prompt to answer

Engines differ in detail, but most follow these five steps. The right-hand box says what Zerene does at each one.

1. 1

   ### The prompt is understood

   "Who supplies scenting for boutique hotels in Dubai?"

   The engineReads the buyer's intent, market and language.

   ZereneWrites pages in the buyer's own wording, in English and Arabic.
2. 2

   ### It splits into smaller searches

   "hotel scenting supplier UAE", "scent marketing companies", "hotel scent cost"

   The engineRuns several short searches, often called query fan-out.

   ZereneBuilds one page per topic cluster and covers the related questions on it.
3. 3

   ### Pages are retrieved from a search index

   The engineCan only pull pages that are indexed and not blocked.

   ZereneFixes indexation (56% of pages indexed in the audit), allows AI crawlers, adds Bing Webmaster Tools.
4. 4

   ### Passages are picked, not whole pages

   The enginePrefers short, self-contained answers, tables and specific numbers.

   ZereneAnswers in the first two sentences, with real AED and SAR prices, MOQ and delivery times.
5. 5

   ### The answer is written and brands are named

   The engineNames brands from pages it just read and from what it remembers. Third-party sources weigh heavily.

   ZereneEarns listings, trade-media coverage and hotel case studies, and describes itself the same way everywhere.

## How we measure it

The same 50 prompts are run on a schedule, so progress is a trend instead of a guess.

1. **50 prompts**Informational, commercial and transactional, in English and Arabic.
2. **Run on engines**3 runs each on ChatGPT, Perplexity and Gemini through n8n.
3. **Log the counts**Mentions, citations, competitors and cited sources go to a sheet.
4. **Read the summary**Rates by intent, market and language. Non-brand first.
5. **Fix and re-run**Change the pages, then measure again after four to six weeks.

Google AI Overviews has no official API, so it needs a separate search-data service or manual checks.

## Where Zerene stands

Baseline for non-brand prompts. No engine runs have been logged yet, so the rates are blank on purpose.

| Prompt intent | Prompts | Mention rate | Citation rate | Status |
| --- | --- | --- | --- | --- |
| Informational | 11 | – | – | Run pending |
| Commercial | 21 | – | – | Run pending |
| Transactional | 12 | – | – | Run pending |

**Early hint, not a result.** One web search combining Zerene with hotel and scent terms returned no Zerene pages. That is a web-search check only, not data from ChatGPT, Perplexity or Gemini.

### First three fixes

- **Get pages indexed**Find out why 163 pages are excluded, then publish.
- **Add buyer pages**Hotel scenting service, pricing and quote, and a Saudi landing page.
- **Earn outside mentions**Trade media, supplier listings and named hotel case studies.

Prepared 14 October 2026. Engine results update after each scheduled run; the Arabic prompts are drafts pending native-speaker review.
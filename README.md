# zerene

**Generative Engine Optimization (GEO) research and strategy for Zerene's luxury wellness & executive gifting brand**, focusing on the KSA/UAE AI search landscape.

This repository documents the workflow for discovering, validating, and ranking Zerene in AI engines (ChatGPT Search, Perplexity, Gemini, Google AI Overviews) through high-intent B2B prompts.

## Project Status

Active GEO research — 50+ high-intent prompts identified, validated across engines, with Share of Voice tracking. See `zerene_geo_workflow_final.md` for the full playbook.

## Claude Code Integration

This project is configured for [Claude Code](https://claude.com/claude-code) — the `/run` skill can launch the app, and `CLAUDE.md` at `zerene/CLAUDE.md` provides guidance for the CLI when working in `zerene/`.

**Key Claude Code hooks & settings** are configured in `.claude/settings.local.json` to reduce permission prompts and automate common workflows.

## Repository Structure

| Directory | Contents |
|-----------|----------|
| `zerene/` | Core GEO playbook, prompt lists, client decks, keyword research |
| `zerene/prompt_generator/` | 50+ validated high-intent B2B prompts (CSV/MD), shared context, opportunity analysis |
| `zerene/zerene-gsc/` | Google Search Console data, country/device/queries reports, ranking playbooks |
| `zerene/geo/` | Blog content, client decks, GEO client keyword briefs |
| `Zerene_GEO_Dashboard_Review.html` | Interactive dashboard with GEO progress metrics and audit findings |
| `zerene_geo_workflow_final.md` | Complete playbook: discovery → validation → content prerequisites → tracking |

## Key Resources

- `zerene_geo_workflow_final.md` — Full playbook (discovery, validation, content prerequisites, tracking)
- `Zerene_GEO_Dashboard_Review.html` — Interactive HTML report with metrics, findings, and action plan
- `zerene/prompt_generator/00-shared-context.md` through `04-quality-control-export.md` — Prompt generation workflow
- `zerene/prompt_generator/README-workflow.md` — Prompt import & validation workflow for Otterly.ai
- `zerene/zerene-gsc/README.md` — GSC data interpretation guide
- `zerene_50_prompts.csv` (repo root) — Master list of 50 validated prompts

## GEO Strategy Summary

**Target Markets:** KSA luxury wellness & executive gifting (Tier 3–4 B2B); UAE as base market

**Current AI Share of Voice:** 20% (target: 25%+ across validated non-brand prompts)

**Core Gaps (from playbook §6.1):**
- Missing product specs (200ml/100ml, 4–6 month longevity, SAR pricing)
- No JSON-LD FAQPage schema for AI extraction
- No `/ksa` landing page with local address signal
- Weak entity co-occurrence (Grasse + Wajaha/Sukun/Karam + Saudi values)

## Getting Started

1. Read `zerene_geo_workflow_final.md` for the complete playbook
2. Open `Zerene_GEO_Dashboard_Review.html` to view audit findings and prioritized actions
3. Import `zerene_50_prompts.csv` into [Otterly.ai](https://otterly.ai) to get intent-volume scores
4. Run top prompts in ChatGPT Search + Perplexity + Gemini (3 runs each) to measure mention/citation rates
5. Log results in `API_Results` format (CSV or Google Sheet)

## Development

No build/test commands — this is a documentation- and research-focused project. Use `open Zerene_GEO_Dashboard_Review.html` to view the interactive dashboard, and `open zerene_geo_workflow_final.md` for the playbook.

## Immediate Execution (from playbook §9)

**This Week:**
1. Import `zerene_50_prompts.csv` into Otterly.ai → get intent‑volume scores
2. Filter to prompts rated **3+** (Medium or above)
3. Select top 15 by Otterly score + commercial/geo modifiers
4. Run each in **ChatGPT Search + Perplexity + Gemini** (3 runs each = 9 data points/prompt)
5. Log to `API_Results` format

**Next Week:**
1. Apply the 4‑point checklist (actionable modifier, regional/audience context, paid search/local listings, regulatory gate)
2. Score using priority formula → keep **High (>=5)** or **Medium (>=3)** bands
3. Apply Validation Gate (5 criteria) → define **Core Baseline**
4. Prioritize Core Baseline prompts via Opportunity Score → pick top 8 for content creation

## Key Metrics (from playbook §12)

- **Mention rate** = runs where Zerene named ÷ successful runs
- **Citation rate** = runs where zerene.com cited ÷ successful runs
- **Share of Voice** = Zerene mentions ÷ total brand mentions across all brands in the same runs

## Live Links (Validated Nov 6, 2026 — all return HTTP 200)

All resources hosted on `dev.slickymedia.com`. Links were tested via curl with redirect following.

| Resource | URL | Status |
|----------|-----|--------|
| Dashboard Review | `https://dev.slickymedia.com/zerene/Zerene_GEO_Dashboard_Review.html` | ✅ Working (root) |
| Dashboard Review (zerene-gsc) | `https://dev.slickymedia.com/zerene/zerene-gsc/Zerene_GEO_Dashboard_Review.html` | ✅ Working (recommended) |
| GEO Prompt Generator (n8n form) | `https://dev.slickymedia.com/zerene/prompt_generator` | ✅ Working |
| Prompt Template | `https://dev.slickymedia.com/zerene/prompt_generator/Updated_Prompt_Template` | ✅ Working |
| AI Prompt Library | `https://dev.slickymedia.com/zerene/zerene-gsc/Zerene_GEO_Strategy_and_Prompts.html` | ✅ Working (redirects) |
| GEO Targeting Matrix | `https://dev.slickymedia.com/zerene/zerene-gsc/Zerene_Targeted_GEO_Keywords` | ✅ Working |
| Content Writer SOP & Brief Template | `https://dev.slickymedia.com/zerene/zerene-gsc/blog-content-audit/Zerene_Content_Writer_SOP_and_Brief_Template` | ✅ Working |
| GEO Strategy & SOP Checklist | `https://dev.slickymedia.com/zerene/zerene-gsc/blog-content-audit/Zerene_GEO_Strategy_and_SOP_Checklist.html` | ✅ Working |
| Blog Score & Audit | `https://dev.slickymedia.com/zerene/zerene-gsc/blog-content-audit/Zerene_Blog_GEO_Score_Audit.html` | ✅ Working (trailing slash needed) |
| SOV Tracker | `https://dev.slickymedia.com/zerene/zerene-gsc/Zerene_GEO_AI_Share_of_Voice_Tracker.html` | ✅ Working (trailing slash needed) |
| FAQ Knowledge Base | `https://dev.slickymedia.com/zerene/zerene-gsc/Zerene_GEO_FAQ_Knowledge_Base.html` | ✅ Working (trailing slash needed) |
| GEO Playbook Slides | `https://dev.slickymedia.com/zerene/zerene-gsc/geo_ranking_playbook_slides.html` | ✅ Working |
| Industry Benchmarks | `https://dev.slickymedia.com/zerene/zerene-gsc/Zerene_GEO_Benchmarking_Framework.html` | ✅ Working (trailing slash needed) |
| Master GEO Blueprint | `https://dev.slickymedia.com/zerene/zerene-gsc/Zerene_Master_GEO_Blueprint.html` | ✅ Working (trailing slash needed) |

**Note:** URLs ending in `.html` returned `308` and redirected to extension-less paths (e.g., `/zerene/zerene-gsc/Zerene_GEO_Strategy_and_Prompts.html` → `/zerene/zerene-gsc/Zerene_GEO_Strategy_and_Prompts`). The prompt generator root also returned `308` (redirects to trailing-slash version). All resolved to HTTP 200 after redirect resolution.

**Review of three SEO deliverables, checked against the live store rather than read in isolation.** One file should not be submitted, one needs numbers, and one needs two topics replaced.

| Reviewed | Period | Verified against |
| --- | --- | --- |
| 3 files | 19–26 Aug 2026 | zerene.com — 13 products, EN + AR, AED |

---

## Verdicts

| File | Verdict | Why |
| --- | --- | --- |
| `disavow_20260826.txt` | **Hold — do not submit** | Includes two of Zerene's own domains and a different company's listings |
| Zerene SEO Work Report | **Incomplete** | No metrics, no URL list, competitor research output not attached |
| Zerene 5 Blog Title Strategy | **Revise before writing** | Two of five topics target products the store doesn't sell |

---

## 1. The disavow file

100 URLs across 100 distinct hosts. Zero `domain:` entries.

### Blocking — two entries are Zerene's own domains

Both of these are on the list, and both redirect into the main store:

- `zerene.life` — **301** → `zerene.com`
- `zerene.co` — **301** → `zerene.com`

A 301 passes link equity. Disavowing these tells Google to discard whatever authority those domains consolidate into zerene.com, so this line item works against the site rather than for it.

Confirm ownership at the registrar, but the recommendation holds either way: if they're ours, disavowing is self-harm; if they aren't, a redirect into our own store is harmless and still not worth disavowing.

### Blocking — two entries belong to an unrelated business

- `places.singleplatform.com/zerene-salon/menu`
- `cgmimm.vercel.app/biz/zerene-salon-1540-nw-56th-st-98107`

Zerene Salon at 1540 NW 56th St, 98107 is a hair salon in Seattle — a different company that happens to share the name. Those pages almost certainly don't link to zerene.com at all, which points at how the list was built: name-matching the word "zerene" rather than working from a backlink export for the domain. Worth raising with the vendor, because it affects every other entry's credibility.

### Would cost us — three entries are legitimate citations of the brand

- `ratingfacts.com/reviews/zerene.com`
- `allare.io/businesses/zerene-com`
- `storeleads.app/reports/technology/Amplitude/country/TH`

The first two are ordinary business listings. Storeleads is a real ecommerce technology database — it lists zerene.com because the store runs Amplitude, which is exactly how that directory works. None of these are link schemes.

### Wrong criterion — irrelevant is not the same as toxic

Several entries look like real pages that simply have nothing to do with fragrance: a 2010 personal food blog post about natto spaghetti, a virtual-tours software roundup, a personal about page, a dry-shampoo top-ten list, and two of the three blogspot domains. Topical irrelevance isn't a disavow criterion.

### Context — 72 of the 100 entries are scraper output Google already discounts

The list carries visible machine fingerprints — the same generated page path repeated across dozens of unrelated hosts:

| Generated path pattern | What produces it | Entries |
| --- | --- | --- |
| `page-c4ab3e51…d07.html` | Backlink-checker mirror pages | 39 |
| `…f7977374…dbdf.html` | Same network, second hash | 9 |
| `/domain/domain/part/270669` | Domain-appraisal scrapers | 8 |
| `/report/` · `/stats/` · `/share/117974–5` | Stats-page generators | 11 |
| `…e1f6b79c…7503-l/` | Worth-checker mirrors | 5 |

These aren't links built to manipulate Zerene's rankings. They're auto-generated pages that mirror whatever domain someone looks up in an SEO tool — the domain was queried, so the pages exist. Google discounts this category wholesale.

### Format — the file wouldn't work even if submitting were right

Every line is a single URL. Each of those scraper networks can generate unlimited pages per host, so a URL-level entry neutralizes exactly one page and leaves the rest. Site-wide problems have to be disavowed at domain level:

```
# scraper mirrors
domain:backlinkshouse.com
domain:backlinksbank.com
domain:linksnatcher.com
```

### Recommendation — don't submit anything yet

> Google's guidance is that the disavow tool is for sites with a considerable volume of genuinely manipulative links **and** good reason to believe those links are causing harm; in most cases its systems assess link trust without help. Since 2016, spam links have been devalued algorithmically rather than counted against a site.
>
> First step is Search Console → **Security & Manual Actions**. If there's no unnatural-links action — and with this profile there almost certainly isn't — the correct action is none. Keep the list as documentation, which is what the work report says it was for, and leave the tool alone.
>
> If a manual action *does* exist, rebuild from Search Console's own link export rather than a single third-party tool, convert to `domain:` entries, and remove zerene.life, zerene.co and the real citations before anything is uploaded.

### How the list breaks down

| Entry | What it actually is | Verdict |
| --- | --- | --- |
| `zerene.life` · `zerene.co` | Zerene's own domains, 301 to zerene.com | Remove |
| `…/zerene-salon/menu` | Seattle hair salon, unrelated company | Remove |
| `ratingfacts.com` · `allare.io` | Ordinary business listings for the brand | Keep the link |
| `storeleads.app/…/Amplitude/…` | Legitimate ecommerce tech database | Keep the link |
| `elliemay.com/…/natto-spaghetti/` | Real 2010 blog post, merely irrelevant | Keep the link |
| 72 fingerprinted mirror pages | Scraper output, already discounted | No action needed |

---

## 2. The weekly work report

### Gap — there are no numbers in it

No impressions, clicks, CTR, average position, indexed-page count, rankings or conversions, and no baseline to compare next week against. A weekly report without data can't be evaluated, and it can't show whether the work is producing anything.

Ask for a standing metrics block: impressions, clicks, CTR and average position from Search Console, top queries and top pages, week-over-week and against the same period last month.

### Gap — the work isn't verifiable as written

"Optimized existing blog posts" — which posts, and how many? "Updated meta titles and meta descriptions" needs a before-and-after table. "Restructured headings" needs the URLs. None of the three claims can currently be checked, which also means next week's report can't build on them.

### Missing deliverable — competitor research has no output

Section 2 is a single sentence. The actual deliverable — who the competitors are, which queries they own, what content gaps were found — isn't in the document or attached to it. Without it, the research can't inform the blog plan it was meant to feed.

### Risk — "removed unnecessary code and unwanted formatting" needs checking

This is the one line that could have done damage. Bulk-cleaning blog HTML on Shopify can strip image `alt` attributes, internal links pointing to product pages, embedded structured data, and canonical or meta tags along with the cruft.

Ask specifically what was removed, and whether internal links and alt text survived. A before-and-after on one representative post settles it in a minute.

### Detail — the CTR claim has nothing behind it yet

"Improve potential click-through rates" is reasonable as an intent, but Google rewrites meta descriptions often and the only proof is Search Console CTR before and after. Capture the baseline now so the claim is checkable next month.

Same for status hygiene: "started reviewing backlink sources" should carry an owner and a completion date.

### Scope — everything in the report is blog work

For a 13-product store, the product and collection pages are what convert and what rank for shopping queries, and none appear anywhere in the engagement. Also absent: indexation and coverage status, Product / Article / Organization / Breadcrumb schema, Core Web Vitals, internal linking from blog posts to products, hreflang for the English and Arabic versions, and Shopify's canonical handling for filtered collection URLs.

The blog is the smallest available lever, and it's the only one being pulled.

---

## 3. The five blog topics

### Verified — most of the product matching was done carefully

Room Spray Oud, Reed Diffuser Oud, Reed Diffuser Oud Lime, Reed Diffuser Oud Lemongrass, the Eternal Rose Set and the Executive Companion Collection all exist and are matched to sensible topics. That part holds up against the live catalog.

### Blocking — topic 2 is built on a product we don't sell

بخور العود أم فواحة العود: أيهما أفضل لتعطير المنزل؟

The article's entire hook is bakhoor versus diffuser, and there is no bakhoor or incense in the catalog. It would bring bakhoor shoppers to a store that can't serve them, which converts at roughly zero and teaches Google the wrong thing about the site.

Either cut it, or reframe it as a comparison the brand can win: reed diffuser versus room spray, where there are six and seven variants respectively to recommend.

### Blocking — topic 5 targets a scent that isn't in the range

روز فانيلا: لماذا تعد رائحة الورد والفانيلا من الروائح المفضلة؟

There is no rose-vanilla product. The rose line is the Rose reed diffuser and the two Eternal Rose sets. One rose product didn't load on the collection page, so it's worth a confirm, but nothing rose-vanilla is visible.

It also contradicts the document's own strategy: the closing SEO Direction says to avoid competing on perfume brand names, and روز فانيلا is effectively a branded product query driven by another company's fragrance. The strategy needs to pick one position.

### Strategy — four of five keywords are shopping queries pointed at blog posts

Google serves collection and product pages for these, not articles. Aiming blog posts at them means fighting an intent mismatch and competing against our own product pages at the same time.

| Keyword | Meaning | Intent | Where it belongs |
| --- | --- | --- | --- |
| عطر العود | oud fragrance | Commercial | Oud collection page; article supports it |
| بخور العود | oud bakhoor | No product | The only blog-shaped topic — nothing to sell against it |
| هدية عود | oud gift | Commercial | Gifting collection page |
| مجموعة عطور | fragrance set | Commercial | Gift-set collection page |
| روز فانيلا | rose vanilla | No product | Branded query for a scent we don't make |

### Prerequisite — the collections the plan points to don't exist

"Luxury Gift Sets", "Rose Fragrance Collection" and "Luxury Home Fragrance Collection" aren't real pages. The store has `/collections/our-products` and `/collections/all`, plus scent filter facets for Oud, Oud Lime, Oud Lemongrass, Rose, Mandarin and Ylang Ylang–Lavender. Shopify filter URLs make poor landing pages and are often kept out of the index.

The plan quietly depends on building real collection pages first. That's the actual first task, and it isn't in either document.

### Factual — "Saudi" doesn't match the store

The SEO Direction proposes positioning Zerene as "a premium Saudi home fragrance brand," but the site prices in AED — the UAE. If Saudi is a deliberate expansion target, that's a far bigger project than five posts (ar-SA targeting, SAR pricing, Saudi market signals) and should be stated as one. If it's an error, fix it before anything gets written against that positioning.

### Incomplete — a topic plan needs the fields that let us prioritize

Missing for each topic: search volume, keyword difficulty, a look at what currently ranks, target URL and slug, draft meta title and description, target length, and which internal links it should carry. Five topics can't be sequenced without volume and difficulty.

Also unresolved: the site is English and Arabic, and the plan doesn't say whether these publish Arabic-only or as hreflang-paired pairs. Topic 5 lists both Arabic and English keywords for one article, which suggests that question hasn't been settled.

### Worth naming — this is a repositioning, not just a topic list

The brand currently presents as aromatherapy and wellness: French essential oils, "Scent for Serenity," and on-site blog categories of Luxury Wellness, Executive Gifting, Space Wellness and Sensory Branding. The strategy reframes it as Arabian oud atmosphere.

Both are viable, but none of the five titles map to the existing content pillars, so this reads as a pivot arriving through keyword research rather than a decision anyone made. It should be an explicit call either way.

---

## What to send back

- [ ] **Hold the disavow file.** Check Search Console → Security & Manual Actions. No unnatural-links action means no submission — keep the list as documentation.
- [ ] **Ask how the list was built.** The Seattle salon entries suggest name-matching rather than a backlink export for the domain. That answer determines whether the rest of the list is trustworthy.
- [ ] **Get the blog work in writing:** URLs touched, before-and-after meta titles and descriptions, and confirmation that alt text, internal links and structured data survived the code cleanup.
- [ ] **Ask for the competitor research output** — the findings themselves, not the fact that it happened.
- [ ] **Resolve Saudi versus UAE,** and whether the Arabic posts ship alone or hreflang-paired with English.
- [ ] **Replace topics 2 and 5,** and split the rest: commercial keywords onto collection pages, blog posts written to support them with internal links.
- [ ] **Set the report format** for next week: standing metrics block, URLs for every claim, owner and date on each open item.

---

*Findings verified against zerene.com on 26 August 2026 — catalog, collection structure, redirect behaviour for zerene.life and zerene.co, and all 100 entries in `disavow_20260826.txt`. Ownership of zerene.life and zerene.co is inferred from their 301 targets and should be confirmed at the registrar.*

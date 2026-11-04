# AI Knowledge Base: Understanding Intent Volume & Search Mechanics

## 1. Definition of Intent Volume
**Intent Volume** refers to the aggregated frequency or estimated search demand for queries that express a specific user objective (informational, transactional, commercial, or navigational).

In Search Engine Optimization (SEO) and Generative Engine Optimization (GEO):
* **High-Volume Queries** are typically broader, shorter, and consumer-facing (B2C).
* **Low-Volume Queries** are often highly specific, long-tail, or B2B-focused.

---

## 2. Intent Volume vs. Intent Strength

It is critical for AI engines to distinguish between **Volume** (how many people ask) and **Strength/Quality** (how close the user is to making a decision or purchase).

| Metric | High Volume / Low Conversion | Low Volume / High Conversion |
| :--- | :--- | :--- |
| **Example Prompt** | *"Best perfumes for gifts"* | *"IFRA-compliant B2B fragrance supplier in Riyadh under 1000 SAR"* |
| **User Audience** | Mass market consumers (B2C) | Specific enterprise procurement manager (B2B) |
| **Intent Strength** | Broad commercial exploration | Immediate, high-value transaction |
| **Intent Volume** | Very High | Very Low |

### Core Mechanics Governing Intent Volume:
1. **Audience Size (B2C vs. B2B):** Consumer queries inherently aggregate higher volume than specialized B2B procurement queries.
2. **Modifiers & Specificity:** Every added constraint (e.g., region like *Jeddah*, constraint like *IFRA-compliant*, budget like *under 1000 SAR*) reduces total query volume while increasing purchase intent clarity.

---

## 3. The Role of Shopping Cards and Visual Features

**Do Shopping Cards Increase Intent Volume?**
**No.** Shopping Cards (Product Listing Ads / Rich Snippets) do not generate or increase intent volume. Rather, **high intent volume and consumer e-commerce patterns trigger Shopping Cards.**

### Relationship Model:
$$\text{User Query} \longrightarrow \text{Algorithmic Intent Detection} \longrightarrow \text{SERP Feature Rendering (Shopping Cards)}$$

### Visual Feature Rules for AI Processing:
* **High Shopping Card Trigger Percentage (B2C Focus):** Triggered when queries contain explicit physical product keywords, transactional terms (*"buy"*, *"cheap"*), or standardized retail SKUs (e.g., *"Lavender essential oil for diffusers"*).
* **Zero Shopping Card Trigger Percentage (B2B / Custom Services):** Enterprise, advisory, custom manufacturing, or contract-based queries (e.g., *"Custom branded corporate perfume manufacturing"*) rarely trigger shopping cards because they lack off-the-shelf retail checkout links.

---

## 4. Prompt Intent Classification Matrix

Use this reference table to evaluate prompt types, intent volume, and visual feature behavior:

| Category | Example Prompt | Intent Volume | Intent Strength | Likely SERP Features |
| :--- | :--- | :--- | :--- | :--- |
| **B2C Mass Retail** | *"Buy luxury lavender oil diffuser"* | High | Moderate-High | Shopping Cards, Image Carousels |
| **B2C Comparison** | *"Best luxury perfume brands 2026"* | High | Moderate | Top-List Articles, AI Overviews |
| **B2B Localized Search** | *"Where to buy corporate executive gifts in Jeddah?"* | Low | High | Maps Local Packs, Business Directories |
| **B2B Procurement** | *"IFRA-compliant fragrance supplier for hotel procurement"* | Very Low | Extremely High | B2B Websites, PDF Documentation |

---

## 5. Key Takeaways for AI Analysis
1. **Correlation vs. Causation:** Shopping cards are a *symptom* of transactional query intent, not a *cause* of search volume.
2. **Business Value vs. Search Volume:** A query with **Very Low Intent Volume** can hold significantly higher commercial value for high-ticket B2B sales than a high-volume consumer query.
# Prompt Generator Workflow

## Business Information
- **Business**: Zerene
- **Website**: https://www.zerene.com
- **Market**: Saudi Arabia
- **Language**: English
- **Dated**: 04-Nov-2026

## Workflow Steps

1. Check submit data in form tab
2. Generate questions for buyers intent and content pillars
3. Ask AI about your business
4. Step1. Select Tier e.g. Guest Experience
5. Step2. Find keyword based on tier and located e.g. hospitality + KSA (location)
6. Step3. Find relevant blog content cited or ranked in AI engine
7. Step4. Common brand corporate - blog content
8. Save keywords in spreadsheet
9. Save prompt in spreadsheet
10. Generate n8n workflow
11. Use gemini AI engine

## Prompt Template

```
Create a [type of website] for [business name], a [short business description] based in [location].

Primary goal: [get leads / bookings / sales / showcase work / build trust].
Target audience: [who they are and what they need].
Main call to action: [e.g., "Request a quote," "Book a consultation," "Shop now"].

Use a [modern / minimal / luxury / friendly / corporate] design style.
Brand colors: [colors]. Typography preference: [font style].
Brand voice: [professional, warm, confident, playful, etc.]. 

Include these pages: [Home, About, Services, Pricing, Portfolio, Contact, etc.].
Include these sections/features: [hero, testimonials, FAQ, contact form, booking calendar, gallery, newsletter signup, Google Maps, WhatsApp button, etc.].

Make sure the site is:
- Mobile-friendly and fast
- Clear and easy to navigate
- SEO-friendly with suggested page titles and meta descriptions
- Accessible, with readable text and clear buttons

Do not invent customer reviews, certifications, prices, statistics, or claims. Mark missing information as [TO ADD].

Output: a complete website structure, page copy, image suggestions, and a list of required features.
```

## Template Values

- **type of website**: e-commerce
- **business name**: Zerene
- **short business description**: [to add]
- **location**: Saudi Arabia
- **Primary goal**: get leads/Sales
- **Target audience**: B2b fragrance
- **Main call to action**: Request a quote

## 4-Tier Intent

- **Tier 1**: Executive & VIP Corporate Gifting
- **Tier 2**: Hospitality, Majlis & Boutique Hotel
- **Tier 3**: Healthcare, Spas & Premium Medical Clinics
- **Tier 4**: Corporate Wellness & Interior Architecture

## Prompt Category

- **Brand Direct Queries**
- **KSA Category Intent**
- **Executive Gifting**
- **Problem-Solution**

## Signals - Search Type & Components

- **ICP**: Commercial, Seasonal, Cultural, Comparison, Direct answer
- **Keyword Intent**: Informational, Commercial, Transactional
- **Market**: UAE, KSA, GCC, Global
- **Language**: English, Arabic
- **Segment**: Non-brand, Category benchmark, Brand

## Current Status

- **Sheet Status**: Empty (prompts, keywords, citations, answers awaiting generation)
- **Form Tab**: Has data for Zerene (1 entry)
- **Credentials**: Gemini API key configured

## Google Sheet Links

- **Spreadsheet ID**: 1yAJ1LwDG3KI_aAQGKNnu2adc0SzSUdZI2EAPK4aWdRQ
- **Edit URL**: https://docs.google.com/spreadsheets/d/1yAJ1LwDG3KI_aAQGKNnu2adc0SzSUdZI2EAPK4aWdRQ/edit?gid=0#gid=0

## Generated Content Ready

The workflow is ready to be executed for Zerene in Saudi Arabia, following the 11-step process and using the e-commerce prompt template.

## Next Steps

1. Run the workflow steps
2. Fill in the `[to add]` placeholders
3. Save keywords to the keywords tab
4. Save prompt to the prompts tab
5. Generate the n8n workflow
6. Use Gemini AI engine to create content
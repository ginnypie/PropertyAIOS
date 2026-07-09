---
name: create-appraisal-report
description: Use to turn a property address into a beautifully designed appraisal-report PDF. Runs the property-appraisal analysis, then renders it in a chosen brand theme (66days | harbour | noir). Trigger on "make an appraisal report", "appraisal PDF", "valuation report for <address>".
---

# Skill — Create Appraisal Report (themed PDF)

Turns an address into a polished, downloadable appraisal-report PDF. Same layout every
time (cover · summary · comparables with a value number-line), swappable design theme.

**Stage:** 2 — Package · **Reads from:** property-appraisal output · **Writes:** a PDF

---

## What it is / is NOT
- ✅ A presentation layer over the `property-appraisal` skill — indicative, comparable-sales based.
- ❌ NOT a certified valuation. The report carries that disclaimer; keep it.
- ❌ Never invents comps, prices or dates. Every figure comes from `property-appraisal`
  (which uses only supplied or genuinely looked-up sold data).

## Inputs
- **Address** (required).
- **Theme** (optional, default `66days`): `66days` (crimson/cream), `harbour` (navy/teal),
  `noir` (charcoal/oxblood), or any file in `brand/report-assets/themes/`.
- **Client name / purpose** (optional).

## Steps

1. **Run the appraisal.** Invoke the `property-appraisal` skill for the address. This
   produces the value range, subject attributes, and the comparable-sales table — the
   real, sourced data. Do not proceed with invented numbers.

2. **Gather images.** For the subject and each comparable, get a listing photo URL
   (property.com.au / realestate.com.au) or a local file. URLs are fine — the renderer
   downloads and inlines them. These are public listing photos, used for research ID.

3. **Write a data file.** Fill a JSON like `brand/report-assets/example-11-apollo.json`
   with the appraisal output: `address`, `date`, value fields, subject summary, an array
   of `reasoning` paragraphs (may contain `<em>`/`<b>`), and the `comparables` array
   (each: ref, address, beds/baths/cars, price, date, relation = Comparable|Superior|
   Inferior, image; mark the anchor comp `"anchor": true`).

4. **Render.** The renderer is bundled **inside this skill**, in `report-assets/`
   (next to this SKILL.md). Write your `<data>.json` there, then run:
   ```bash
   cd "$(dirname "$0")/report-assets"   # the report-assets folder inside this skill
   python3 render.py <data>.json --theme <theme> --out ~/Documents/Claude/<name>.pdf
   ```
   The script fills the template, builds the comp cards + number-line, inlines all
   images (self-contained PDF), injects the theme, and prints via headless Chrome
   (`/Applications/Google Chrome.app`). It polls for the finished PDF, so it won't
   hang on web-font loading. Copy `report-assets/example-11-apollo.json` as your
   starting template for the data file.

5. **Deliver.** Report the PDF path and `open` it. If Chrome fails, the sibling `.html`
   opens in any browser and prints to PDF with the real fonts.

## Adding a person / brand
Drop a new token file in `brand/report-assets/themes/<name>.css` (copy an existing one,
change the `:root` values + font `@import`). It's instantly selectable via `--theme <name>`.

## Files
- `brand/report-assets/render.py` — the renderer
- `brand/report-assets/master.template.html` — layout (has the `/*__THEME__*/` slot)
- `brand/report-assets/report.body.template.html` — tokenized body
- `brand/report-assets/themes/*.css` — the designs
- `brand/report-assets/example-11-apollo.json` — worked example (11 Apollo Quay)
- `brand/report-style.md` — the layout spec

## Disclaimer
Indicative appraisal for research and preparation only — not a certified valuation. A
valuation for lending, purchase, sale, tax (CGT), legal or family-law purposes must be
prepared by a Certified Practising Valuer (CPV / API) or RICS registered valuer.

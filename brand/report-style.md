# Report Style — "Lender Valuation" layout

A reusable layout spec for PropertyAIOS valuation/appraisal reports, modelled on
the structure of a bank Remote Market Valuation Report (CoreLogic-style). Pair the
**layout** below with the **[66 Days brand tokens](66-days-brand.css)** for colour
and type. Brand colour is a variable — swap the lender green for `--crimson (#AB2B3C)`.

---

## Global rules

- **Format:** A4 portrait, ~14mm margins. Multi-page, numbered.
- **Type:** one humanist sans throughout (use `--body` Plus Jakarta Sans). Section
  headers set in the **brand accent colour**, UPPERCASE, wide letter-spacing (~.12em).
- **Accent blocks:** solid brand-colour panels used boldly (cover band, header notch).
- **Icon row** for property attributes: house · bed · bath · car · year built.
- **Highlight bar:** the single headline figure (Valuation/Value) sits in a dark
  filled row so it reads first.
- **Tag chips:** small outlined pills — `Settled`, and `Inferior / Comparable / Superior`.
- **Running footer on every page:** logo (left) · governing line e.g. "Indicative — not a certified valuation" (centre) · `Page X of N` (right).

---

## Page 1 — Cover

- Brand-colour masthead strip; logo top-right over an angled white notch.
- **Full-bleed hero photo** of the property (dusk/twilight shot works best).
- Lower third: solid brand-colour block containing —
  - Large UPPERCASE report title (e.g. "MARKET APPRAISAL REPORT")
  - Thin horizontal rule
  - Property address (mixed case, generous letter-spacing)
  - `Valuation date   DD/MM/YYYY`

## Page 2 — Summary

- Brand-colour eyebrow ("MARKET APPRAISAL") + large address heading.
- **Photo grid:** one large image left + a 2×2 of four thumbnails right.
- **Meta band** (light grey), two columns of label/value pairs:
  - Left: Client · Purpose · Instruction Date · Valuation Date
  - Right: Customer · Valuation Firm · Valuation Officer · Job No.
- **Two-column body:**
  - **Left — Valuation Details:** dark highlight row = headline value; then
    Valuation Date, Owner Estimate. Below: **Subject Property Summary** — icon row
    (type/bed/bath/car/year) + attribute list (Living Area, Land Area, Title, LGA,
    Zoning, Main Walls, Roof, Car Accom.).
  - **Right — Valuation Approach & Reasoning:** 2–3 narrative paragraphs, then a
    script-style signature + name and credentials (e.g. MRICS, AAPI, CPV).

## Page 3 — Additional Property Information

- Two subheads side by side: **Additional Attributes** (kv list: storeys, inclusions,
  condition, notable attributes) | **Potential Impacts to Value** (bulleted text).
- **Additional Commentary** paragraph.
- **Supporting Imagery:** locality map with a marker + aerial/boundary shots +
  floor-plan / site-plan thumbnail.

## Page 4–5 — Comparable Sales Evidence

- Brand-colour section header.
- **Left:** map with lettered pins (A, B, C…) for each comparable.
- **Right:** a horizontal **value number-line** (e.g. 1.51M → 4.05M) plotting each
  comparable as a circle, with a legend: Valuation Amount · Owner Estimate ·
  Tight Range · Comparable Sales.
- **Comparable cards** (2-up grid), each with:
  - Letter badge + photo + icon row (bed/bath/car/year)
  - Address
  - `Last Sale $amount (date)` · Title · Distance · Living Area · Land Area
  - Tag chips: `Settled` + `Inferior | Comparable | Superior`

## Final pages — Disclaimer & Copyright

- Section header, then several **bold-titled paragraphs**: what the report is,
  who may rely on it, exclusion of liability, data-source disclaimers.
- Keep the PropertyAIOS "not a certified valuation" language.

---

## Mapping to our brand

| Their element        | Ours (66 Days)                          |
|----------------------|-----------------------------------------|
| Lender green         | `--crimson #AB2B3C`                      |
| Cover/section blocks | crimson on `--paper #FAF6EE`            |
| Dark highlight row   | `--char #1C1A17` fill, cream text        |
| Body sans            | Plus Jakarta Sans                        |
| Section headers      | JetBrains Mono, uppercase, crimson       |
| Emphasis             | Instrument Serif italic, crimson         |
| Chips / tags         | blush `#F1E2DC` fill, crimson text       |

*Structure adapted from a bank Remote Market Valuation Report for layout reference only.*

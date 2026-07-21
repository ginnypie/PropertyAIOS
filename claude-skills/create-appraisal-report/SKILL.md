---
name: create-appraisal-report
description: Use to turn a property address into a beautifully designed appraisal-report PDF. Runs the property-appraisal analysis, then renders it in a chosen brand theme (66days | harbour | noir). Trigger on "make an appraisal report", "appraisal PDF", "valuation report for an address".
---

# Skill — Create Appraisal Report (themed PDF)

Turns an address into a polished, downloadable appraisal-report PDF. Same layout every
time (cover · summary · comparables with a value number-line), swappable design theme.

**Stage:** 2 — Package · **Reads from:** property-appraisal output · **Writes:** a PDF

---

## What it is / is NOT
- A presentation layer over the `property-appraisal` skill — indicative, comparable-sales based.
- NOT a certified valuation. The report carries that disclaimer; keep it.
- Never invents comps, prices or dates. Every figure comes from `property-appraisal`
  (which uses only supplied or genuinely looked-up sold data).

## Inputs
- **Address** (required).
- **Theme** (optional, default `66days`): `66days` (crimson/cream), `harbour` (navy/teal),
  `noir` (charcoal/oxblood), or any file in the bundled `report-assets/themes/` folder.
- **Client name / purpose** (optional).

## Steps

1. **Run the appraisal.** Invoke the `property-appraisal` skill for the address. This
   produces the value range, subject attributes, and the comparable-sales table — the
   real, sourced data. Do not proceed with invented numbers.

2. **Photos — OPTIONAL and user-supplied. Do NOT scrape listing/portal photos.**
   The report renders fine without any photos (empty `image` fields show a neutral
   placeholder). Portal terms (Domain / realestate.com.au) prohibit harvesting their
   images, and listing photos are copyright — so this tool must never collect them, and
   must never instruct a user to. Only include a photo the **user has supplied and has the
   right to use** (their own photo of their own property, or an agent-provided image with
   permission). Put any such image path/URL in the comp's or subject's `image` field;
   otherwise leave it an empty string `""`. Never auto-fetch photos from a listing.

3. **Write a data file.** Copy `report-assets/example-sample.json` and fill it with the
   appraisal output: `address`, `date`, value fields, subject summary, an array of
   `reasoning` paragraphs (simple emphasis markup is allowed), and the `comparables` array
   (each: ref, address, beds/baths/cars, price, date, relation = Comparable | Superior |
   Inferior, image; mark the anchor comp with `"anchor": true`).

   **Do NOT set brand fields in the data file** — `brand_name`, `brand_sub`,
   `footer_brand` and `signature` are chosen automatically by `--theme` so the header,
   footer and signature always match. Leave them out; picking the theme is how you brand
   the report. (Only set them by hand if you deliberately want a one-off custom brand.)

   **Carry the government-sourced provenance through** (this is what beats "powered by
   CoreLogic" on trust — see the `property-appraisal` output and its
   `references/au-property-data-sources.md`):
   - `avm` — show the value cross-check AND the primary anchor, e.g.
     `"$2.27m (Domain AVM) · sales confirmed vs NSW VG register"`.
   - each comparable's `line2`/label may note `✓ VG` when its price+date are register-confirmed.
   - `comps_note` — list the real sources (VG register / Queensland Globe / Domain) with
     the sold data, and, when a rental estimate is included, the **bond-median** anchor and
     quarter, e.g. `"Rent est. $1,380/wk — anchored on QLD RTA median (Palm Cove, houses, Q2 2026), adjusted vs current listings."`
   Never invent a source; only cite what was actually pulled.

4. **Render.** The renderer is bundled inside this skill, in the `report-assets/` folder
   next to this SKILL.md. Save your data file there (for example `report.json`), then run:
   ```bash
   cd "$(dirname "$0")/report-assets"
   python3 render.py report.json --theme 66days --out ./appraisal.pdf
   ```
   Swap `report.json`, the `--theme` value, and the `--out` path for your own. The script
   ALWAYS writes a fully self-contained `.html` first (every image + font embedded), then,
   **only if** Chrome / Chromium / Edge is already installed, auto-prints the matching PDF.
   The HTML is the real deliverable — it looks identical to the PDF and needs nothing else.

   **Do NOT install a browser, Playwright, Chromium, wkhtmltopdf, or any other engine.**
   If none is found the script says so and stops after the HTML — that is the expected,
   successful outcome, not an error. Downloading a browser is slow and unnecessary.

5. **Deliver — works on any OS.** Save the `.html` (and the `.pdf` if one was produced)
   somewhere the person can find it — their Documents folder, or the folder they ran this
   from. Then tell them: **open the `.html` in any web browser and choose Print → Save as
   PDF.** That Print-to-PDF option is built into every browser on Windows, macOS and Linux
   (Chrome, Edge, Firefox, Safari) — no software to install. The fonts and property photos
   are already embedded, so the printed PDF is pixel-identical to the report.

## Adding a person / brand
Two steps for a new brand:
1. Drop a new token file in `report-assets/themes/` (copy an existing one, change the
   `:root` values + font import). It is instantly selectable via the `--theme` flag.
2. Add a matching entry to `THEME_BRANDS` in `render.py` (`brand_name`, `brand_sub`,
   `footer_brand`, `signature`) so the report's header, footer and signature all carry the
   new brand name. Without this the new theme falls back to the 66days brand text.

## Files (all bundled in report-assets/)
- `render.py` — the renderer
- `master.template.html` — layout (has the theme slot)
- `report.body.template.html` — tokenized body
- `themes/` — the designs (66days, harbour, noir)
- `example-sample.json` — worked example (fictional property; photos left blank)

## Disclaimer
Indicative appraisal for research and preparation only — not a certified valuation. A
valuation for lending, purchase, sale, tax (CGT), legal or family-law purposes must be
prepared by a Certified Practising Valuer (CPV / API) or RICS registered valuer.

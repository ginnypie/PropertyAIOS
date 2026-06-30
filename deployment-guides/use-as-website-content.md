# Using PropertyAIOS as Website Content

**Deployment type:** Public-facing website powered by the repo's prompt boards, report templates, and website copy.

---

## What this deployment is

The PropertyAIOS repo contains structured content — prompt boards, report templates, website copy, and examples — that is designed to power a public-facing website. The website is where ordinary property investors discover and use the system. The repo is the source of truth that the website is built from.

---

## What powers what

| Repo folder | Website section |
|---|---|
| `prompt-boards/*.json` | Prompt card pages — copy button, categories, examples |
| `report-templates/` | Output preview sections showing what a finished report looks like |
| `examples/` | Example output pages (clearly labelled as fictional) |
| `website-content/` | Page copy for homepage, individual skill pages, about |
| `disclaimers/` | Footer disclaimer blocks on every page |
| `docs/professional-review-model.md` | "How it works" or "About" page content |

---

## Building the prompt board UI

The JSON files in `prompt-boards/` are designed to feed a prompt card component. Each card has:

```json
{
  "id": "suburb-risk-scan",
  "title": "Suburb Risk Scanner",
  "category": "Suburb Research",
  "description": "One-line description for the card front",
  "prompt": "The full copyable prompt",
  "best_for": "Who this prompt is for",
  "output_type": "What the output looks like",
  "professional_review_note": "Which professionals to consult"
}
```

**Suggested UI components:**

- Card grid with category filter tabs (Stage 1 / Stage 2 / Stage 3 / Stage 4)
- Expandable card with the full prompt text
- One-click copy button
- `professional_review_note` displayed as a callout below the prompt
- Footer disclaimer on every card

---

## Displaying examples

Files in `examples/` show what a finished output looks like. On the website:

- Label every example page clearly: **"This is a fictional example. All details are invented."**
- Display the example output collapsed by default with a "Show example" toggle
- Never display example outputs without the fictional label visible
- Do not use example figures in marketing copy (e.g. do not say "get yields like 4.7%")

---

## Using website-content/ copy

The files in `website-content/` are structured page content, not final HTML. Each file has:

- A hero headline and subheading
- A "What you get back" section (the output sections listed as dot points)
- A "Who this is for" section
- A "Pairs with" section linking to related skills
- A disclaimer block

Drop this content into your CMS, website builder, or React page component. The structure is designed to work in Webflow, WordPress, Next.js, or any content-driven site.

---

## Required elements on every page

The following are **required** on every page of a PropertyAIOS website deployment:

**Footer disclaimer (on every page):**

> All PropertyAIOS content is general information and educational preparation only. Nothing on this website constitutes financial advice, credit advice, tax advice, legal advice, or a recommendation to buy or sell any property or financial product. Always review outputs with appropriately licensed professionals before making any decision.

**On every page that contains prompts or example outputs:**

> Outputs from these prompts are general information only. Figures are assumptions and require verification.

**On every example output page:**

> This is a fictional example for illustration purposes only. All details are invented.

---

## What not to do

- Do not claim that PropertyAIOS produces "accurate" figures, "guaranteed" yields, or "reliable" market data
- Do not use example figures (e.g. "$650/week rent") in homepage hero copy or marketing
- Do not remove the professional review prompts from skill pages
- Do not omit disclaimers on any page that contains prompts or outputs
- Do not present prompt outputs as equivalent to professional advice

---

## SEO and positioning

Recommended positioning for SEO:

```
PropertyAIOS — AI-assisted property investment preparation for Australian investors.
Research. Stress-test. Prepare.
```

Avoid in titles and meta descriptions:

- "property advice"
- "investment recommendations"
- "best suburbs"
- "guaranteed returns"
- "financial guidance"

Use instead:

- "property research"
- "cash flow preparation"
- "due diligence questions"
- "broker prep"
- "assumption testing"

---

## Disclaimer

> All website content derived from this repo is general information and educational preparation only. Website builders are responsible for ensuring their own compliance with applicable law in their jurisdiction. See [docs/compliance-and-disclaimers.md](../docs/compliance-and-disclaimers.md).

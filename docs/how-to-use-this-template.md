# How to Use This Template

PropertyAIOS is a framework. Fork it, replace the niche, and build your own property investment AI operating system.

---

## Step 1 — Fork the repository

Click **Use this template** on GitHub, or fork and clone:

```bash
git clone https://github.com/your-username/your-fork-name
cd your-fork-name
```

Rename it for your niche:

```
propertyaios          → Australian property (this repo)
nzpropertyaios        → New Zealand property
ukpropertyaios        → UK buy-to-let
usrealestateaios      → US residential or commercial
smsfpropertyaios      → Australian SMSF property
airbnbaios            → Short-term rental analysis
renovationaios        → Renovation risk and planning
firsthomebuyeraios    → First home buyer preparation
```

---

## Step 2 — Customise CLAUDE.md

`CLAUDE.md` tells Claude how to behave in your Claude project. Update:

- The niche (Australian → your country/market)
- The professional roles relevant to your market (e.g. solicitor → attorney for US)
- The regulatory bodies and terminology for your jurisdiction
- Any specific compliance rules that apply (e.g. ASIC for AU, FCA for UK, SEC for US)

---

## Step 3 — Replace niche-specific content in skills/

Each file in `skills/` is a reusable workflow instruction set. For AU → UK, you would replace:

| AU reference | UK equivalent |
|---|---|
| CoreLogic, Domain, REA | Rightmove, Zoopla, Land Registry |
| Stamp duty (state SRO) | SDLT (HMRC) |
| Negative gearing | Loss offsetting |
| CGT discount (50%) | Capital gains tax (annual exemption) |
| Strata report | Leasehold review / service charge history |
| Building and pest | Homebuyer survey / full structural survey |
| Mortgage broker (ACL) | Mortgage adviser (FCA authorised) |
| APRA serviceability buffer | Stress-test rate (PRA/FCA) |
| Land tax | Council tax / SDLT surcharge |

Keep the structure of each skill file the same. Only replace the jurisdiction-specific references.

---

## Step 4 — Update disclaimers/

The `disclaimers/` folder contains reusable compliance blocks. Update:

- The jurisdiction (Australian → your country)
- The licensing regime (AFSL/ACL/tax agent → your equivalent)
- Any professional titles that differ (solicitor vs attorney vs notary)

**Never remove disclaimers.** Property investment workflows touch financial, credit, tax, and legal domains in every market. Every output needs a disclaimer.

---

## Step 5 — Replace or adapt agents/

Each file in `agents/` is a role-based AI worker definition. The roles are generic enough to work in most property markets:

- Suburb / area research agent
- Cash flow analysis agent
- Due diligence agent
- Broker/lender prep agent
- Accountant/tax prep agent
- Buyer's agent brief agent
- Portfolio review agent

You may need to rename roles for your market (e.g. "buyer's agent" → "buyer's advocate" in AU, "estate agent" in UK, "realtor" in US).

---

## Step 6 — Adapt commands/

Commands in `commands/` are user-facing slash commands. They are designed to be:

- Typed by a user into a Claude project
- Run on a website via a prompt board
- Used as reference for building a web app

Rename them for your brand or rename to match your niche.

---

## Step 7 — Rebuild prompt-boards/ for your website

The JSON files in `prompt-boards/` are structured for a web prompt board UI. Each card has:

- `id` — unique slug
- `title` — display title
- `category` — grouping
- `description` — one-line value prop
- `prompt` — the copyable prompt
- `best_for` — who it suits
- `output_type` — what kind of output it produces
- `professional_review_note` — the disclaimer for this card

Feed these into your website's prompt card component to build a public prompt board.

---

## Step 8 — Customise report-templates/

Report templates in `report-templates/` define what a finished output looks like. Use `[PLACEHOLDERS]` for variable content. The structure is designed to be:

- Consistent across all reports
- Scannable in 60 seconds
- Always ending with a disclaimer and professional review prompts

---

## Step 9 — Add your examples

The `examples/` folder has fictional but realistic AU examples. Replace these with examples from your market. Make sure they are clearly fictional — never use real client data.

---

## Step 10 — Update website-content/

The `website-content/` folder has copy for each page of your website. Update the brand name, niche, and jurisdiction throughout.

---

## What to keep the same

Even if you adapt everything else, keep:

- The three-primitive structure: Property File + Skills + Spine
- The spine stages: Set Up → Analyse → Finance → Stress-Test → Decide
- The output contract format in each skill
- Disclaimers on every output
- The professional review handoff at the end of every workflow

These are the things that make it a system, not just a list of prompts.

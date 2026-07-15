# AU Property Data — Authoritative Sources (sales + rent)

The backbone of a credible indicative appraisal is going to the **primary government
source** for the two load-bearing numbers, then using listing portals only for
corroboration, photos and attributes.

**Principle:** CoreLogic / RP Data and Domain do not *own* sale or rent data — they
license it. Sale prices come from the state **Valuer-General / land titles registry**
(CoreLogic's own AU disclaimer says its NSW sales are "provided under licence from the
Valuer General New South Wales"). Achieved rents come from the state **rental bond
authority**. Going direct to those is going to the same primary source, minus the
middleman. So an indicative estimate anchored on them is *as well-sourced* as a
"powered by CoreLogic" figure — often better, because we show the source.

Use this hierarchy for every figure:
1. **Anchor** = government primary source (VG for sale price/date; bond authority for rent).
2. **Corroborate** = Domain / realestate.com.au (asking prices, listing attributes, photos, portal AVM as a *cross-check only*).
3. **Never** present a portal estimate or an asking rent as an achieved figure.

**Cost policy — free sources only. Never pay for title/QVAS/register searches.** The output
is an *indicative estimate, not a valuation*, so paid register-certainty adds nothing. Where a
free government verification exists (e.g. NSW VG bulk sales), use it and mark the comp ✓
verified. Where it doesn't (QLD per-sale, VIC/SA/WA per-title), use Domain attributes + free
Queensland Globe where practical, and mark the sale price **"indicative / unverified"** — then
move on. Unverified is acceptable here; do not suggest a paid lookup.

---

## A. Sale price + date — State Valuer-General / Land Titles registry

The authoritative record of what a property actually sold for.

| State | Free authoritative source | Access / automatability |
|---|---|---|
| **NSW** | NSW Valuer General **Bulk Property Sales Information** — every sale since 1990 | **Free, bulk, automatable.** Weekly/daily files. Friendly CSV mirror: `nswpropertysalesdata.com` (last 6 yrs, daily). Gov page: nsw.gov.au → land values → "How to find property sales information" |
| **QLD** | **Queensland Globe** (parcel → sales history); QVAS via Titles Queensland | Globe is **free but interactive/manual** (spatial, hard to bulk-automate). Clean bulk (QVAS) + per-title searches are **paid**. |
| **VIC** | Land Use Victoria **Property Sales Statistics** (suburb medians) | **Free at suburb/median level.** Per-sale history via **paid** title search. |
| **SA** | Land Services SA / SAILIS | Mostly **paid** per search; some free property reports. |
| **WA** | Landgate (Map Viewer Plus / Property Interest Report) | Mostly **paid**; limited free lookups. |
| **TAS** | theLIST / Land Titles Office | **Paid** per title. |
| **ACT** | Access Canberra / ACT Revenue (Allhomes carries sales) | Mixed; Allhomes shows sold history. |

**Rule of thumb:** NSW = clean free automated cross-check. QLD = free but manual (Globe). Others = paid per title, so corroborate on Domain and note the register isn't freely bulk-available.

---

## B. Achieved rent — State rental bond authority (bond-lodgement medians)

The authoritative record of rents actually paid, from lodged bonds. This is the rental
equivalent of the VG, and the right anchor for a rental estimate (not asking rents).

| State | Free authoritative source | What it gives |
|---|---|---|
| **QLD** | **RTA — Median rents quarterly data** (`rta.qld.gov.au` → forms-resources → RTA quarterly data → median rents) | **Free.** Median weekly rent by postcode/suburb, dwelling type (house/townhouse/unit) and bedrooms, from new bond lodgements. |
| **NSW** | **DCJ Rent and Sales Report** (`dcj.nsw.gov.au` → families-and-communities-statistics → rent and sales report) | **Free.** Interactive dashboard, median rent by postcode/LGA and dwelling type, quarterly. |
| **VIC** | **Rental Report — Quarterly Median Rents** (`data.vic.gov.au` / DFFH Homes Victoria) | **Free.** Moving quarterly median rents by suburb/LGA and property type. |
| **SA** | SA Gov / Consumer & Business Services rental bond data | Free median rent tables. |
| **WA** | DMIRS bond data; REIWA suburb rents | Bond-based medians. |
| **TAS / ACT** | State rental report / bond authority | Quarterly medians. |
| **National context** | **ABS** rental market insights | Trend/context only, not property-level. |

**Portals for corroboration:** Domain / realestate.com.au rental **listings** = *asking*
rent (tends to run high, varies). Use them to adjust the bond-median for the specific
property's size/quality — never as the anchor.

---

## How to use this in an appraisal

- **Sale price of each comparable:** take from Domain first (fast), then **confirm against
  the state VG register** (Section A). Stamp the confirmed figure + source. Where VG and
  the portal disagree, the register wins and the difference is flagged.
- **Rental estimate:** anchor on the **state bond-median** (Section B) for the suburb +
  dwelling type + bedrooms, then adjust with comparable current listings. Show the bond
  source and the quarter.
- **Every figure** carries `source` + `date/quarter`. A figure confirmed against a
  government register is marked verified (e.g. "✓ NSW VG register").
- When using Firecrawl or a web tool, keep the **source URL** for each pull — that URL is
  the provenance the report displays.

_Not a certified valuation. These sources support an indicative estimate for research and
pre-approval preparation only._

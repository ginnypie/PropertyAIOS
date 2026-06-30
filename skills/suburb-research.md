# Skill — Suburb Research

**Stage:** 1 — Analyse
**Hook:** Run a structured suburb risk scan before you inspect.
**Use when:** You want to assess a suburb or area before researching specific listings.

---

## Purpose

This skill produces a structured suburb analysis covering employment base, infrastructure, supply and demand signals, lender appetite flags, and known risk overlays. It is preparation for property research — not a recommendation.

---

## Reads from

- Investor Profile (from Strategy Agent, if available)
- Property File: INVESTOR PROFILE section

## Writes to

- Property File: SUBURB & DEMAND section

---

## Inputs required

```
SUBURB: [suburb name, state, postcode]
PROPERTY TYPE I AM RESEARCHING: [house / townhouse / apartment / unit / acreage]
MY PURPOSE: [investor / owner-occupier / first home buyer / downsizer]
BUDGET RANGE: $[min] to $[max]
```

---

## Output contract

Return exactly these 7 sections:

### 1. SUBURB SNAPSHOT
- State, LGA, postcode
- Dominant property types and land sizes
- Distance from CBD or major employment centre
- Population and demographic signals

### 2. EMPLOYMENT AND ECONOMIC BASE
- Major employers and industries
- Single-employer dependency risk
- Economic diversity signal (low/medium/high)

### 3. INFRASTRUCTURE AND LIVEABILITY
- Transport: proximity to train/bus/freeway
- Schools, hospitals, retail, parks
- Planned infrastructure (confirm with council)
- Flight path, industrial, or hazard proximity (flag to verify)

### 4. SUPPLY AND DEMAND SIGNALS
- Development pipeline: new apartments, estates, townhouse projects
- Historical median price and rent trends (label as historical, not predictive)
- Days on market signal (higher = softer demand)
- Vacancy rate signal for investors

### 5. LENDER APPETITE FLAGS
Flag any of the following if applicable:
- High-density postcode (many lenders cap LVR at 70-80%)
- Regional or rural location (some lenders restrict)
- Mining, tourism, or resort-dependent economy
- Known postcode restrictions (verify with a mortgage broker)

### 6. RISK OVERLAYS TO VERIFY
- Flood zone: check council flood map and state hazard portals
- Bushfire: check state's BAL (Bushfire Attack Level) map
- Contaminated land: check council and EPA registers
- Coastal erosion, subsidence, or heritage overlays
- (These require confirmation from council and licensed professionals)

### 7. SUBURB SCORE SUMMARY
A simple summary table:

| Factor | Signal | Confidence |
|---|---|---|
| Employment diversity | [low/medium/high] | [based on: ...] |
| Infrastructure | [weak/moderate/strong] | [based on: ...] |
| Supply pressure | [low/medium/high] | [based on: ...] |
| Lender appetite | [unrestricted/flagged/restricted] | [verify with broker] |
| Risk overlays | [none identified/verify X] | [based on: ...] |

---

## Safety boundaries

- Never recommend a suburb as "the right choice" or "best for investment"
- Never present price growth or rental growth as predictable
- Always flag when data is thin or assumed
- Always direct lender appetite questions to a mortgage broker

---

## Professional review prompts

- "Ask your mortgage broker: Are there any lender restrictions on this postcode for my property type and LVR?"
- "Check with council: Is this area in a flood or bushfire overlay?"
- "Ask a local property manager: What is the current vacancy rate and rental demand for [property type] in this suburb?"

---

## Pairs with

- → Listing Analysis (Skill 01) — run on specific listings in this suburb
- → Comparable Sales Review (Skill 23) — are prices in this suburb realistic?
- → Rental Demand Check (Skill 24) — deepen the investor demand picture
- → Borrowing Power (Skill 06) — check lender appetite for this postcode

---

## Disclaimer

> This output is general information and educational preparation only. It is not financial advice, credit advice, tax advice, legal advice, or a property recommendation. All figures and signals are starting points requiring verification. See [disclaimers/general-information.md](../disclaimers/general-information.md) and [disclaimers/professional-review-required.md](../disclaimers/professional-review-required.md).

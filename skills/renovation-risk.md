# Skill — Renovation Risk

**Stage:** 1 — Analyse / 3 — Stress-Test
**Hook:** Renovation upside is real. Renovation cost blowout is more real.
**Use when:** A property has renovation potential and you want to assess the risk before committing.

---

## Purpose

This skill produces a structured renovation risk assessment. It identifies the key cost categories, the most common blowout risks in Australian renovation projects, the compliance requirements, and the questions to ask a builder and quantity surveyor before making an offer or starting work.

---

## Reads from

- Property File: SNAPSHOT, RED FLAGS (from Listing Analysis and Due Diligence)
- Property details: age, type, known condition issues

## Writes to

- Property File: RED FLAGS (open) — renovation risk flags

---

## Inputs required

```
PROPERTY: [suburb, state, property type, year built approximately]
RENOVATION SCOPE: [cosmetic / structural / full renovation / extension / subdivision]
BUDGET FOR RENOVATION: $[amount or "unknown"]
KNOWN ISSUES: [describe anything visible or flagged in inspection]
GOAL: [add value to sell / add value to hold / improve to rent at premium / other]
TIMELINE: [need to be done by X / flexible]
```

---

## Output contract

Return exactly these 6 sections:

### 1. RENOVATION SCOPE ASSESSMENT
Based on the inputs, classify the renovation:

| Scope | Typical cost range (AU, 2025 estimates) | Key risk |
|---|---|---|
| Cosmetic (paint, floors, fixtures) | $10k–$40k | Taste risk, not structural |
| Bathroom renovation | $15k–$35k per bathroom | Waterproofing compliance |
| Kitchen renovation | $20k–$50k | Trade availability, lead times |
| Structural work | $50k–$200k+ | Engineering, permits, timeline |
| Extension | $150k–$400k+ | Council approval, DA timeline |
| Full renovation | $150k–$500k+ | All of the above combined |

> **Note:** These are broad 2025 estimates for Australian major cities. Regional and premium areas differ significantly. Get 3 quotes from licensed builders before committing to any scope.

### 2. TOP COST BLOWOUT RISKS
Flag the most common blowout triggers for this property and scope:

- **Asbestos:** Properties built before 1990 commonly contain asbestos in walls, ceilings, floors, roofing, and eaves. Asbestos removal requires a licensed removalist and adds cost and timeline risk.
- **Waterproofing:** Non-compliant or failed waterproofing in bathrooms and wet areas is the most common cause of renovation cost blowouts. New work requires compliant waterproofing under NCC standards.
- **Electrical:** Older properties may have knob-and-tube or aluminium wiring requiring replacement. Opening walls triggers electrical compliance obligations.
- **Plumbing:** Lead pipes, galvanised steel pipes, and non-compliant drainage are common in pre-1980 properties.
- **Structural issues:** Cracks, sagging, subsidence, or termite damage found during renovation will escalate scope and cost.
- **Council permits:** Unapproved additions or works from previous owners create compliance obligations when new work is commenced.
- **Trade delays:** Material and trade shortages can push timelines by 4–12 weeks, increasing holding costs.

### 3. COMPLIANCE REQUIREMENTS TO VERIFY
Before starting:
- [ ] Development Application (DA) required? (extensions, structural changes, change of use)
- [ ] Building permit / building approval required? (most structural work)
- [ ] Owner-builder licence? (if owner-managing work over $10k — state-specific thresholds)
- [ ] Heritage overlay or character overlay? (limits what can be changed)
- [ ] Strata approval required? (internal and external works in strata buildings)

### 4. QUESTIONS FOR YOUR BUILDER
1. "Are you a licensed builder in [state]? Can I see your licence number?"
2. "Have you worked on properties of this age and type before? What issues should I expect?"
3. "Does your quote include all materials, trade co-ordination, permits, and site cleanup?"
4. "What is your process if you open a wall and find asbestos / structural damage / non-compliant wiring?"
5. "What is your payment schedule? How do you handle variations?"
6. "What is your timeline estimate, and what are the main risks to that timeline?"

### 5. THE RENOVATION PROFIT TEST
A simple check to run before committing:

```
After-renovation value (estimated):      $[X]
Less: Purchase price                    -$[X]
Less: Stamp duty and buying costs       -$[X]
Less: Renovation budget                 -$[X]
Less: Holding costs during renovation   -$[X]
Less: Selling costs (if selling)        -$[X]
= Estimated profit / equity gain         $[X]
```

> **Important:** The after-renovation value must be verified with a local buyer's agent, real estate agent, or valuer — not assumed. The most common renovation mistake is overcapitalising: spending more on the renovation than the market will pay in return.

### 6. RENOVATION RED FLAGS
Flag any of these if present:
- No comparable sales of renovated properties in this suburb at the assumed after-renovation value
- Building and pest report flagged significant structural or pest issues
- Property is in a strata building with restrictions on works
- Heritage or character overlay limits what can be changed
- The renovation budget is the "optimistic" number, not the 20% contingency number
- No licensed builder quotes obtained before making an offer

---

## Safety boundaries

- Never provide renovation cost estimates as quotes
- Never advise on whether a renovation "will add value" — that depends on the market
- Never advise on owner-builder compliance obligations — each state differs
- Always direct structural and compliance questions to a licensed builder and the relevant council

---

## Pairs with

- ← Listing Analysis (Skill 01) — initial property red flags
- ← Due Diligence Risk Scan — structural and permit risks
- → Cash Flow Stress Test (Skill 04) — model holding costs during renovation
- → Comparable Sales Review (Skill 23) — verify after-renovation value

---

## Disclaimer

> This output is general information and educational preparation only. Renovation cost estimates are broad industry ranges only — not quotes. Actual costs, timelines, and compliance requirements vary by state, property, scope, and market conditions. Engage a licensed builder, quantity surveyor, and your local council before committing to any renovation. This output is not financial, legal, or building advice. See [disclaimers/general-information.md](../disclaimers/general-information.md).

# Skill — Short-Stay and Airbnb Expense Tracker

**Stage:** Portfolio Management
**Hook:** Short-stay income is taxed differently to long-term rental. GST can apply, private use has to be apportioned, and setup costs are usually capital. This organises your quarterly numbers before your tax agent does.
**Use when:** You are running one or more Australian short-stay or Airbnb properties and want to review your quarterly income and expenses, check your GST position, and prepare a summary for your registered tax agent.

---

## Purpose

This skill produces a structured quarterly review of short-stay rental income and expenses for an Australian property investor. It categorises income and expenses, checks the GST threshold, flags private-use apportionment, separates capital items from deductible expenses, and generates the questions to ask your registered tax agent.

All outputs are summaries based on the data provided. All deductibility determinations, GST obligations, and tax treatment classifications must be confirmed by a registered tax agent.

---

## Reads from

- Property File: CASH-FLOW ASSUMPTIONS (STR income data if already modelled)
- Investor Profile: ownership structure, tax position

## Writes to

- Property File: CASH-FLOW ASSUMPTIONS (quarterly actuals updated)
- Property File: RED FLAGS (GST threshold, apportionment, capital items flagged)

---

## Inputs required

```
PROPERTY: [suburb, state, type — e.g. "2BR apartment Gold Coast QLD"]
OWNERSHIP: [sole / joint / trust / company]
PLATFORM: [Airbnb / Stayz / VRBO / direct booking / multiple]
QUARTER: [e.g. Q1 FY2026 — July to September 2025]

INCOME:
- Gross platform payouts received: $[total]
- Platform/host fees deducted by platform: $[total] (from payout statements)
- Net payouts into bank: $[total]
- Nights booked: [number]
- Nights available for rent (advertised/listed): [number]
- Nights blocked (personal use or unlisted): [number]

EXPENSES:
- Cleaning costs: $[total] ([number] cleans at $[per-clean])
- Guest consumables (toiletries, coffee, linen): $[total]
- STR-specific insurance: $[total] (or 'included in landlord policy')
- Co-host or management fee: $[total] ([X%] of gross)
- Council rates (quarterly): $[total]
- Water rates: $[total]
- Strata levy: $[total] (or 'not strata')
- Repairs and maintenance: [each item and cost — or 'none']
- Furniture, appliances, setup items: [each item and cost — or 'none']
- Internet: $[total] (if property-specific)
- Other: [describe and amount]

TAX POSITION:
- Marginal tax rate: [X%]
- Personal use days: [number]
- GST registration status: [registered / not registered / unsure]
```

---

## Output contract

Return exactly these 5 sections:

### 1. INCOME SUMMARY

| Metric | Value | Note |
|---|---|---|
| Gross platform revenue | $X | From payout statements |
| Platform/host fees deducted | $X | By platform |
| Net payouts to bank | $X | Cross-check against bank |
| Nights booked | X | From bookings |
| Nights available (advertised) | X | Investor-reported |
| Nights blocked (personal/unlisted) | X | Investor-reported |
| Occupancy % | X% | Booked ÷ available |
| Average nightly rate (ADR) | $X | Net revenue ÷ booked nights |
| Annualised gross revenue estimate | $X | Quarter × 4 — assumption only |

**GST flag:** State whether the annualised gross revenue estimate approaches or exceeds the $75,000 GST registration threshold. If it does: flag as HIGH PRIORITY for tax agent.

### 2. EXPENSE CATEGORISATION

Show a table with: expense, amount, category, and deductibility note. Categories:
- Platform/host fees
- Cleaning and linen
- Guest consumables and amenities
- STR-specific insurance
- Co-host/management fees
- Council rates
- Water rates
- Strata/body corporate levies
- Repairs and maintenance
- Capital items (furniture, appliances, setup — separate row group labelled CAPITAL)
- Internet
- Advertising/photography
- Other

For CAPITAL items: note that these generally cannot be claimed as immediate deductions — accounting treatment must be confirmed by a registered tax agent.

### 3. PRIVATE-USE APPORTIONMENT

If personal use days were reported:

| | Days | % of quarter |
|---|---|---|
| Available for rent | X | X% |
| Booked (rented) | X | X% |
| Blocked (personal use) | X | X% |
| Total days in quarter | 90–92 | 100% |

Note that expenses are generally only deductible for the proportion of days the property is genuinely available for rent. Show the apportionment percentage and flag for registered tax agent to confirm.

If no personal use was reported: state clearly so the accountant can verify.

### 4. QUARTERLY POSITION

| | Amount |
|---|---|
| Gross STR income | $X |
| Total deductible expenses (excluding capital) | $X |
| Net position (pre-tax) | $X |
| Capital items (not immediately deductible) | $X |

**Flagged items for tax agent:**
1. List any item approaching or over the $75k GST threshold
2. List any capital items with preliminary classification note
3. List any apportionment issues if personal use days reported
4. List any repairs where capital vs maintenance classification is uncertain
5. List any other item where deductibility is ambiguous

### 5. QUESTIONS FOR YOUR REGISTERED TAX AGENT

Generate five specific questions based on this quarter's data:
1. GST registration threshold and current position
2. Any capital items identified — treatment and depreciation schedule
3. Private-use apportionment (if applicable)
4. Any repair items that may be capital improvements
5. Any item flagged as ambiguous in the quarter

---

## Safety boundaries

- Never classify a capital item as immediately deductible
- Never confirm GST registration is not required — always flag for professional confirmation
- Never calculate or advise on apportionment — show the figures and flag for the tax agent
- Never present income figures as tax advice
- Always note that all classifications are preliminary

---

## Pairs with

- ← Airbnb Investor Analysis (`airbnb-investor.md`) — evaluated the STR investment before purchase
- ← Property Cash Flow (`property-cash-flow.md`) — long-term rental baseline for comparison
- → Tax Year Prep (`tax-year-prep.md`) — EOFY accountant package using full-year summaries
- → Broker Prep (`broker-prep.md`) — if portfolio refinancing or expansion is planned

---

## Disclaimer

> This output is general information and educational preparation only. This is not tax advice, accounting advice, GST advice, or BAS advice. Short-term accommodation is generally a taxable supply for GST (unlike residential rent) — the $75k registration threshold, private-use apportionment rules, and capital vs deductible classification are all matters for a registered tax agent. ATO rules change. Verify everything with a registered tax agent or BAS agent before any lodgement decision. See [disclaimers/not-tax-advice.md](../disclaimers/not-tax-advice.md).

# Skill — Portfolio Review

**Stage:** 3 — Stress-Test
**Hook:** Your portfolio looked different at 3.5% interest rates. Run it at 7%.
**Use when:** You want to stress-test your existing property portfolio against rate rises, vacancy, and market changes — and understand what to do next.

---

## Purpose

This skill produces a structured portfolio stress test across all properties in a portfolio. It identifies the combined cash flow position, the most vulnerable properties, and the questions to prepare for conversations with a broker and accountant about portfolio management.

---

## Reads from

- Multiple Property Files (one per property, if maintained)
- Investor Profile: income, liabilities, investment objectives

## Writes to

- Standalone portfolio stress test document (does not write to individual Property Files)

---

## Inputs required

For each property in the portfolio:

```
PROPERTY [1/2/3...]:
- Address/suburb, state
- Purchase price: $[X]
- Current estimated value: $[X] (estimate — verify with agent or valuer)
- Loan balance: $[X]
- Interest rate: [%]
- Loan type: [IO / P&I]
- IO expiry date: [if applicable]
- Weekly rent: $[X]
- Vacancy (weeks per year): [X]
- Annual outgoings: $[X]

INCOME POSITION:
- Gross annual income: $[X]
- Approximate marginal tax rate: [32.5% / 37% / 45%]

OVERALL QUESTION:
- [What are you trying to understand: can I handle a rate rise? Can I add another property? Should I sell one?]
```

---

## Output contract

Return exactly these 6 sections:

### 1. PORTFOLIO SNAPSHOT
A summary table of all properties:

| Property | Estimated value | Loan | LVR | Equity | Weekly rent | Weekly cost | Pre-tax weekly |
|---|---|---|---|---|---|---|---|
| [suburb 1] | $X | $X | X% | $X | $X | $X | +/- $X |
| [suburb 2] | $X | $X | X% | $X | $X | $X | +/- $X |
| **Total** | $X | $X | X% | $X | $X | $X | +/- $X |

> Note: Estimated values are provided by the user — not a formal valuation.

### 2. STRESS TEST SCENARIOS
Run the portfolio under 4 scenarios:

| Scenario | Rate change | Vacancy change | Combined weekly cash flow | Annual impact |
|---|---|---|---|---|
| Current | 0% | Current | $X | — |
| Rate +1% | +1% | Current | $X | +/- $X |
| Rate +2% | +2% | Current | $X | +/- $X |
| Vacancy stress | 0% | +4 weeks/property | $X | +/- $X |
| Bear case | +2% | +4 weeks | $X | +/- $X |

### 3. INTEREST-ONLY EXPIRY RISK
Flag any IO loans expiring within 24 months:
- Property: [X]
- IO expiry: [month/year]
- Current weekly repayment (IO): $X
- Estimated weekly repayment (P&I after expiry): $X
- **Weekly cash flow impact at expiry:** +/- $X

If IO loans are expiring, this is a key item for your broker conversation.

### 4. EQUITY POSITION
- Total estimated equity across portfolio: $X
- Usable equity at 80% LVR: $X (estimated)
- Properties with highest equity concentration: [list]
- Properties at highest LVR risk: [list]

> Usable equity = (Current value × 80%) - Current loan balance. This is an estimate. A formal valuation and lender assessment are required to access equity.

### 5. PORTFOLIO FLAGS
List the key risks and questions the stress test has surfaced:
- "IO loan on [property] expiring [date] — raise with broker"
- "Bear case cash flow requires $X/week from income — can you sustain that?"
- "LVR on [property] above 80% — no usable equity to draw on without refinancing"
- "Portfolio is [concentrated in one suburb / one city / one property type] — consider diversification"

### 6. QUESTIONS FOR YOUR PROFESSIONALS

**For your mortgage broker:**
1. "If rates rise another 1–2%, which of my loans has a rate expiry or revert risk I should know about?"
2. "My IO loan on [property] expires in [month/year]. What are my options at that point?"
3. "Can I access equity from [property] to fund a deposit on the next purchase?"
4. "What would my serviceability look like if I wanted to add another property at $[price]?"

**For your accountant:**
1. "What is my total negative gearing position across the portfolio this year?"
2. "Are there any land tax issues with the current portfolio in [state]?"
3. "Given the proposed CGT changes, should I be thinking about timing on any of these properties?"

---

## Safety boundaries

- Never recommend selling a property or restructuring a portfolio
- Never advise on whether the portfolio is "performing well"
- Estimated values must be clearly flagged as user-provided estimates, not valuations
- Usable equity estimates require formal lender and valuation confirmation

---

## Pairs with

- ← Cash Flow Stress Test (Skill 04) — used for individual property analysis
- ← Borrowing Power (Skill 06) — capacity to add to the portfolio
- → Broker Prep (Skill 29) — prepare for the refinance/equity conversation
- → Accountant Prep — prepare for the tax and land tax conversation

---

## Disclaimer

> This output is general information and educational preparation only. Portfolio stress tests are based on user-provided figures and assumptions — they are not valuations, credit assessments, or financial advice. Equity access requires lender assessment and formal valuation. Portfolio restructuring decisions require advice from a licensed financial adviser, registered tax agent, and mortgage broker. See [disclaimers/not-financial-advice.md](../disclaimers/not-financial-advice.md) and [disclaimers/not-credit-advice.md](../disclaimers/not-credit-advice.md).

# Compliance and Disclaimers

PropertyAIOS operates in a high-compliance domain. Property investment decisions involve financial, credit, tax, legal, and valuation matters — all of which require licensed professional advice in Australia (and most jurisdictions).

This document explains the compliance framework behind PropertyAIOS and how disclaimers work throughout the system.

---

## The compliance lane

PropertyAIOS stays strictly within these lanes:

| In scope | Out of scope |
|---|---|
| General information | Financial advice |
| Education and preparation | Credit advice |
| Research organisation | Tax advice |
| Assumption testing | Legal advice |
| Risk identification | Valuation |
| Question preparation | Investment recommendations |
| Professional-review prompts | Buy/sell/hold recommendations |

**The test for every output:** "Does this help the user prepare better questions for their professional? Or does it substitute for that professional?" If the answer is the second one, the output needs to be revised.

---

## Australian compliance context

In Australia, providing financial product advice, credit assistance, and tax advice each require separate licences:

| Activity | Licence required |
|---|---|
| Financial product advice | Australian Financial Services Licence (AFSL) — Corporations Act 2001 |
| Credit assistance | Australian Credit Licence (ACL) — National Consumer Credit Protection Act 2009 |
| Tax advice | Registered tax agent — Tax Agent Services Act 2009 |
| Legal advice | Australian legal practitioner — jurisdiction-specific |
| Property valuation | Certified Practising Valuer (API) or state-registered valuer |

PropertyAIOS is **not** the holder of any of these licences. It is an educational preparation tool only.

If you are adapting this template for another jurisdiction, substitute the relevant licensing regime and regulatory bodies.

---

## How disclaimers work in this system

### Standard disclaimer (appears on every output)

> This output is general information and educational preparation only. It is not financial advice, credit advice, tax advice, legal advice, a property valuation, or a recommendation to buy or sell property. All figures are assumptions and estimates requiring verification. Review all outputs with appropriately licensed professionals before making any decision.

### Additional disclaimers by workflow type

| Workflow | Additional disclaimer |
|---|---|
| Cash flow analysis | "All cash flow figures are assumptions only. Actual income, outgoings, and vacancy vary. Verify with a property manager and accountant." |
| Borrowing power | "This is not a credit assessment. Borrowing capacity is lender-specific and income-dependent. Verify with a licensed mortgage broker." |
| Tax and depreciation | "This is not tax advice. Depreciation schedules, negative gearing, and CGT calculations require a registered tax agent." |
| Legal/contract review | "This is not legal advice. Contract review requires a qualified solicitor or conveyancer." |
| Valuation | "This is not a property valuation. A formal valuation requires a qualified/registered valuer." |
| SMSF | "SMSF property involves superannuation law, trust deed compliance, and tax obligations. Requires a specialist SMSF adviser and auditor." |

---

## Disclaimer files

Reusable disclaimer blocks are in the `disclaimers/` folder:

- [general-information.md](../disclaimers/general-information.md)
- [not-financial-advice.md](../disclaimers/not-financial-advice.md)
- [not-credit-advice.md](../disclaimers/not-credit-advice.md)
- [not-tax-advice.md](../disclaimers/not-tax-advice.md)
- [not-legal-advice.md](../disclaimers/not-legal-advice.md)
- [professional-review-required.md](../disclaimers/professional-review-required.md)

Each skill, agent, and command output should include the relevant disclaimers by reference.

---

## For builders adapting this template

If you are building a commercial service on top of this template:

1. Get your own legal advice on your specific compliance obligations
2. Do not remove or weaken disclaimers
3. If your platform provides any output that could be interpreted as advice (financial, credit, tax, legal), seek specific guidance from a lawyer in your jurisdiction
4. Consider whether you need a licence for your specific activities
5. Add your own licence number and compliance contact where relevant

The disclaimer blocks in this repo are a **starting point**, not a complete compliance solution. Your obligations depend on what you build and how users engage with it.

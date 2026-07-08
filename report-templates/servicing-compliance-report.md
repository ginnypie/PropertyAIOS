# Servicing Compliance Check Report

**PropertyAIOS — General Information and Educational Preparation Only**
**This is NOT credit advice. An independent check on stated parameters — not a lender decision.**

---

## Report details

| Item | Value |
|---|---|
| Applicant(s) | [Single / Dual income] |
| Proposed new loan | $[AMOUNT] |
| Actual rate | [X.X%] |
| Term | [30 yrs] |
| Repayment type | [P&I / IO] |
| Parameters set by | [ACL holder / conservative defaults — verify] |
| Date prepared | [DATE] |

---

## 1. PARAMETER SET USED

> **This is the audit record. Every parameter applied is printed here — an unshown assumption is an unauditable check. Parameters must be set/approved by the ACL holder; defaults are a conservative starting point, not policy.**

| Parameter | Value applied | Note |
|---|---|---|
| Assessment buffer | +[3.0]% on actual rate | Assessment rate = actual rate + buffer |
| Base income | 100% counted | — |
| Overtime shading | [85]% | Variable income |
| Casual shading | [80]% | Variable income |
| Bonus / commission shading | [X]% (documented) | Variable income |
| Rental shading | [85]% | Net rental factor |
| Other income shading | [50]% | Variable income |
| Tax basis | Income tax + 2% Medicare levy | — |
| Credit card cost | Limit over 36 mo @ ~22% p.a. | On the LIMIT, not the balance |
| Living-expense floor | HEM (used when declared < HEM) | — |
| Cash buffer | [5]% haircut on net surplus | Extra conservatism |
| DTI flag threshold | ≥ [6]× | Set by org — total debt ÷ gross income |

---

## 2. INCOME ASSESSMENT

> **Nothing is counted above its shaded value. Where YTD was used, the annualisation basis and pay date are shown.**

| Income type | Entered | YTD annualisation (if used) | Shading % | Assessable |
|---|---|---|---|---|
| Base salary | $[X] | [YTD $X ÷ days × 365, pay date DD/MM] | 100% | $[X] |
| Overtime | $[X] | [basis] | [85]% | $[X] |
| Casual | $[X] | [basis — correct weeks] | [80]% | $[X] |
| Bonus / commission | $[X] | [basis] | [X]% | $[X] |
| Rental (gross) | $[X] | — | [85]% | $[X] |
| Other | $[X] | — | [50]% | $[X] |
| **Total assessable income (annual)** | | | | **$[X]** |
| After tax + 2% Medicare (monthly) | | | | $[X] |

> Shading note: [state which variable income was counted and at what %, OR "base income only — no variable income counted."]

---

## 3. COMMITMENTS & LIVING EXPENSES

| Commitment | Basis | Monthly cost |
|---|---|---|
| Credit card cost | Total limit $[X] over 36 mo @ ~22% p.a. | $[X] |
| Personal / car loan repayments | Declared | $[X] |
| HECS/HELP | Balance $[X] | $[X] |
| Existing mortgage repayments | Declared | $[X] |
| Living expenses | max(declared $[X], HEM $[X]) | $[X] |
| **Total monthly commitments** | | **$[X]** |

---

## 4. SERVICING RESULT

| Line | Value |
|---|---|
| Actual rate | [X.X%] |
| Assessment rate (actual + buffer) | [X.X%] |
| New-loan P&I repayment at assessment rate | $[X]/mo |
| After-tax income (monthly) | $[X] |
| Less new-loan repayment, card cost, other repayments, living expenses | −$[X] |
| Gross surplus (monthly) | $[X] |
| Net surplus after [5]% cash buffer | $[X] |
| **Result** | **[SERVICES / DOES NOT SERVICE]** |

> Result = SERVICES only when net surplus ≥ 0 **and** DTI is within threshold (Section 5). These are separate gates.

---

## 5. DTI CHECK

| Line | Value |
|---|---|
| Total debt (existing + proposed + card limits) | $[X] |
| Gross annual income | $[X] |
| DTI (total debt ÷ gross income) | [X.X]× |
| Threshold | ≥ [6]× flag |
| **DTI status** | **[WITHIN / OVER threshold]** |

> Surplus and DTI are separate gates — a loan can pass net surplus and still fail DTI, or vice versa. Report both.

---

## 6. WORKINGS & NOTES FOR THE FILE

**Step-by-step math (for the record):**
```
YTD annualise (if used)  = [YTD ÷ days × 365, then shade]
assessable income        = Σ (each income type × shading %)  = $[X]
after-tax income         = assessable − income tax − 2% Medicare = $[X]/mo
assessment rate          = [actual] + [3.0]% buffer = [X.X]%
new-loan repayment       = P&I on $[loan] at [X.X]% over [30] yrs = $[X]/mo
credit card cost         = $[limit] over 36 mo @ ~22% = $[X]/mo
living expenses          = max(declared, HEM) = $[X]/mo
gross surplus            = after-tax − repayment − card − other − living = $[X]/mo
net surplus              = gross surplus × (1 − [5]%) = $[X]/mo
DTI                      = $[total debt] ÷ $[gross income] = [X.X]×
```

**Notes:**
- This is an independent check on the stated parameters — not a lender decision.
- Confirm with the broker / ACL holder: [what to verify — parameters, lender calculator comparison, income evidence].

---

## Disclaimer

> This is NOT credit advice. This report is general information and educational preparation only. It is an independent servicing check on stated, conservative parameters — not a lender's servicing calculator, a credit assessment, a serviceability approval, or a pre-approval. Parameters must be set by the holder of an Australian Credit Licence (ACL), and only a licensed mortgage broker or lender can assess actual serviceability and arrange finance. Figures are estimates to verify. See [disclaimers/not-credit-advice.md](../disclaimers/not-credit-advice.md) and [disclaimers/professional-review-required.md](../disclaimers/professional-review-required.md).

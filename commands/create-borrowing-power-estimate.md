# Command — /create-borrowing-power-estimate

## Purpose

Produce an **indicative, deliberately conservative** borrowing-capacity estimate for an Australian residential property investor — an assessment-rate serviceability calculation returned as a **range, never a single number**. This is preparation for a licensed broker conversation, not a credit assessment or pre-approval.

## Inputs required

The user provides:
- Applicant(s), marital status, dependants
- Employment type (PAYG / self-employed) and time in role / years trading
- Income (base salary, overtime/casual/bonus, rental/other) and co-borrower income
- Family Tax Benefit (Part A / B), if any
- Existing properties, mortgages, and monthly repayments
- Car / personal loans (balance and monthly repayment)
- Credit card **limits** (assessed on the limit, not the balance)
- HECS/HELP balance
- Savings / shares, superannuation balance
- Monthly living expenses (or "use HEM guide")
- Deposit available, target interest rate, target LVR

## Steps

1. Collect the inputs above
2. Invoke the [Borrowing Power Agent](../agents/borrowing-power-agent.md)
3. Run the [borrowing-power skill](../skills/borrowing-power.md)
4. Return the 6-section estimate, leading with the conservative Low figure

## Output format

See [borrowing-power-report.md](../report-templates/borrowing-power-report.md)

## Disclaimer

This is **NOT credit advice.** This output is general information and educational preparation only. Borrowing-capacity figures are simplified estimates presented as a range — not a credit assessment, serviceability approval, or pre-approval. Real lender calculators vary materially and lender policies change. Only the holder of an Australian Credit Licence (ACL) — a licensed mortgage broker or lender — can assess your actual borrowing capacity. See [disclaimers/not-credit-advice.md](../disclaimers/not-credit-advice.md) and [disclaimers/professional-review-required.md](../disclaimers/professional-review-required.md).

# Command — /create-servicing-compliance-check

## Purpose

Produce an independent, conservative, policy-neutral serviceability check on a specific proposed loan — separate from any lender's calculator. It states the parameter set used, shades income, annualises YTD, checks net surplus AND DTI, and shows every step, so the result is auditable and can be kept on file by an ACL holder.

This is an independent check on stated parameters — not a lender's servicing decision, a credit assessment, or an approval. It is NOT credit advice.

## Inputs required

The user provides:
- Applicant(s): single or dual income
- Income per applicant (annual, OR YTD + pay-date + payslip period to annualise): base salary, overtime, casual, bonus/commission, rental, other
- Liabilities: credit card limits (total limit, not balance), personal/car loans (repayment + balance), HECS/HELP balance, existing mortgage repayments
- Dependants (number and ages)
- Declared living expenses (monthly — compared against the HEM floor)
- Proposed new loan: amount + actual rate % + term (default 30 yrs) + P&I / IO
- Parameter set (org policy — must be set/approved by the ACL holder; conservative defaults apply if not supplied): assessment buffer, income shading table, tax basis, credit card treatment, living-expense floor, cash buffer, DTI flag threshold

## Steps

1. Collect the inputs above
2. Invoke the [Servicing Compliance Agent](../agents/servicing-compliance-agent.md)
3. Run the [servicing-compliance-check skill](../skills/servicing-compliance-check.md)
4. Print the parameter set and shading used, then return the 6-section check

## Output format

See [servicing-compliance-report.md](../report-templates/servicing-compliance-report.md)

## Disclaimer

This is NOT credit advice. This output is general information and educational preparation only. It is an independent servicing check on stated, conservative parameters — not a lender's servicing calculator, a credit assessment, a serviceability approval, or a pre-approval. Parameters must be set by the holder of an Australian Credit Licence (ACL), and only a licensed mortgage broker or lender can assess actual serviceability and arrange finance. Figures are estimates to verify. See [disclaimers/not-credit-advice.md](../disclaimers/not-credit-advice.md) and [disclaimers/professional-review-required.md](../disclaimers/professional-review-required.md).

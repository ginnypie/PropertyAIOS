# Command — /create-cash-flow-prep

## Purpose

Model the indicative cash flow position of an investment property across base and stress scenarios.

## Inputs required

The user provides:
- Purchase price
- Suburb and state
- Property type
- LVR target
- Loan type preference
- Estimated weekly rent (or "unknown")
- Assumed interest rate
- Marginal tax rate

## Steps

1. Collect the inputs above
2. Invoke the [Cash Flow Agent](../agents/cash-flow-agent.md)
3. Run the [property-cash-flow skill](../skills/property-cash-flow.md)
4. Return the 6-section report plus a PROPERTY FILE UPDATE block

## Output format

See [property-cash-flow-prep-report.md](../report-templates/property-cash-flow-prep-report.md)

## Disclaimer

Cash flow figures are assumptions only. Not financial, credit, or tax advice. Verify rent with a property manager, rate with a broker, and tax position with an accountant.

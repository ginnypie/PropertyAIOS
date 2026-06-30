# Command — /create-due-diligence-report

## Purpose

Run a structured due diligence risk scan on a specific property before making an offer or exchanging contracts.

## Inputs required

The user provides:
- Property details (suburb, state, type, age)
- Strata or freehold status
- Price
- Any known issues already flagged
- Whether contract/section 32 is available

## Steps

1. Collect the inputs above
2. Invoke the [Due Diligence Agent](../agents/due-diligence-agent.md)
3. Run the [due-diligence-risk-scan skill](../skills/due-diligence-risk-scan.md)
4. Return the 7-section report plus a PROPERTY FILE UPDATE block

## Output format

See [due-diligence-risk-report.md](../report-templates/due-diligence-risk-report.md)

## Disclaimer

This output is preparation material only. Not legal, financial, or building advice. Do not exchange contracts without independent legal advice from a solicitor or conveyancer.

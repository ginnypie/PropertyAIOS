# Command — /create-suburb-report

## Purpose

Run a structured suburb research report for a given suburb and property type.

## Inputs required

The user provides:
- Suburb name and state
- Property type they are researching
- Their purpose (investor / owner-occupier / first home buyer)
- Budget range

## Steps

1. Collect the inputs above
2. Invoke the [Suburb Research Agent](../agents/suburb-research-agent.md)
3. Run the [suburb-research skill](../skills/suburb-research.md)
4. Return the 7-section report plus a PROPERTY FILE UPDATE block

## Output format

See [suburb-research-report.md](../report-templates/suburb-research-report.md)

## Disclaimer

All outputs are general information only. Not financial, credit, or investment advice. Verify with local professionals.

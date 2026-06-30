# Command — /create-accountant-brief

## Purpose

Produce a structured preparation pack for an accountant or registered tax agent conversation about a property investment.

## Inputs required

The user provides:
- Property details (suburb, state, type, year built, price)
- Investment purpose
- Ownership structure preference
- Approximate marginal tax rate
- Income type
- Other properties owned

## Steps

1. Collect the inputs above
2. Invoke the [Accountant Prep Agent](../agents/accountant-prep-agent.md)
3. Run the [accountant-prep skill](../skills/accountant-prep.md)
4. Return the 6-section pack

## Output format

See [accountant-prep-brief.md](../report-templates/accountant-prep-brief.md)

## Disclaimer

This is preparation only. Not tax advice. Seek advice from a registered tax agent.

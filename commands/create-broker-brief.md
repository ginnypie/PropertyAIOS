# Command — /create-broker-brief

## Purpose

Produce a structured preparation pack for a mortgage broker conversation.

## Inputs required

The user provides:
- Income (gross annual, type)
- Co-borrower details if applicable
- Liabilities (HECS, credit card limits, loans, existing mortgages)
- Available deposit
- Property details (suburb, state, type, price, purpose)
- LVR preference
- Loan type preference

## Steps

1. Collect the inputs above
2. Invoke the [Broker Prep Agent](../agents/broker-prep-agent.md)
3. Run the [broker-prep skill](../skills/broker-prep.md)
4. Return the 6-section pack

## Output format

See [broker-prep-brief.md](../report-templates/broker-prep-brief.md)

## Disclaimer

This is preparation only. Not credit advice or a borrowing assessment. Seek advice from a licensed mortgage broker (ACL holder).

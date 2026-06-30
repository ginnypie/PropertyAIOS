# Command — /create-airbnb-analysis

## Purpose

Produce a structured short-term rental (Airbnb/Stayz/VRBO) investment analysis for an Australian property, including income model, break-even occupancy, STR vs long-term rental comparison, compliance risks, and lender flags.

## Inputs required

The user provides:
- Property (suburb, state, type, beds/baths/sleep capacity)
- Purchase price
- Estimated nightly rate (standard and peak if applicable)
- Estimated annual occupancy rate
- Long-term rental equivalent
- Furnishing status and estimated cost
- Management type (self-managed / co-host / management company)
- Marginal tax rate

## Steps

1. Collect the inputs above
2. Invoke the [Airbnb Investor Agent](../agents/airbnb-investor-agent.md)
3. Run the [airbnb-investor skill](../skills/airbnb-investor.md)
4. Return the 7-section analysis

## Output format

See [airbnb-investor-report.md](../report-templates/airbnb-investor-report.md)

## Disclaimer

This is general information and educational preparation only. STR income is variable and not guaranteed. Not financial, credit, tax, or legal advice. Council regulations, strata rules, and lender policies vary and change — verify with the relevant professionals before committing to a short-term rental strategy.

# Command — /create-comparable-sales-check

## Purpose

Test whether an asking or contract price on an Australian property is realistic — bracket it against recent comparable sales and report whether it sits **Over**, **Fair**, or **Under** the evidence, always as a range. This is an indicative **price check**, not a certified valuation.

## Inputs required

The user provides:
- Subject address (suburb, state, postcode)
- Property type and attributes (beds / baths / car spaces)
- Living area and land area (or "unknown")
- Condition and key features
- The price being tested, and its type (advertised asking / price guide / contract / auction expectation)
- 4–8 recent nearby comparable sales — each with address, attributes, land/living m², sale price, sale date, distance, and source (or "none — please look up / prompt me")

## Steps

1. Collect the inputs above
2. Invoke the [Comparable Sales Agent](../agents/comparable-sales-agent.md)
3. Run the [comparable-sales skill](../skills/comparable-sales.md)
4. Return the 6-section price check. **If no comparable sales are supplied or found, return only the subject and confidence sections plus the data-source checklist, and STOP — never invent comps to fill the gap.**

## Output format

See [comparable-sales-report.md](../report-templates/comparable-sales-report.md)

## Disclaimer

This is general information and educational preparation only. It is an **indicative price check** based on comparable sales, **not a certified valuation** — every figure is an estimate to verify, always expressed as a range. Comparable sales are never fabricated. A valuation for a mortgage, refinance, purchase, sale, tax (including CGT), legal, or family-law purpose must be prepared by a Certified Practising Valuer (CPV / API) or RICS registered valuer. Not financial, credit, tax, legal, or investment advice. See [disclaimers/general-information.md](../disclaimers/general-information.md) and [disclaimers/professional-review-required.md](../disclaimers/professional-review-required.md).

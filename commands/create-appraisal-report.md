# Command — /create-appraisal-report

## Purpose

Produce an **indicative property market appraisal** for a single Australian residential property, laid out like a lender's remote market valuation: subject-property summary, comparable sales evidence, valuation reasoning, and an indicative value **range** (low / most likely / high). It shows its working so you can take a sharper conversation to a licensed valuer, agent, or broker.

This is preparation and research only. It is **not** a certified valuation, and a bank will not lend against it.

## Inputs required

The user provides:
- Subject address (full address, suburb, state, postcode)
- Property type (house / townhouse / unit / land)
- Attributes (beds / baths / car spaces / year built)
- Living area and land area (m², or "unknown")
- Condition (original / average / renovated / new, or "unknown")
- Key features (e.g. water views, pool, solar, main road, flood-prone, or "none noted")
- Purpose (buying / refinancing / selling / curiosity)
- Owner or asking estimate, if any (labelled unverified)
- Comparable sales — 4–8 recent nearby sold properties (address, beds/baths/cars, land/living m², sale price, sale date, distance, source). If the user has none, they say so and the command produces the framework only.

## Steps

1. Collect the inputs above
2. Invoke the [Property Appraisal Agent](../agents/property-appraisal-agent.md)
3. Run the [property-appraisal skill](../skills/property-appraisal.md)
4. Return the 8-section indicative appraisal
5. If no comparable sales were supplied or found, return Sections 1–2 and 6–8 plus the data checklist, and STOP — never fabricate comparable sales to fill the table

## Output format

See [property-appraisal-report.md](../report-templates/property-appraisal-report.md)

## Disclaimer

This is general information and educational preparation only. It is an **indicative market appraisal, NOT a certified valuation**. A valuation for a mortgage, refinance, purchase security, legal, tax/CGT, or family-law purpose must be prepared by a Certified Practising Valuer (CPV / API) or RICS registered valuer. All figures are estimates based on the comparable evidence supplied and require independent verification. Never present the value as a single certain figure — always a range. Not financial, credit, tax, legal, or investment advice. See [disclaimers/general-information.md](../disclaimers/general-information.md) and [disclaimers/professional-review-required.md](../disclaimers/professional-review-required.md).

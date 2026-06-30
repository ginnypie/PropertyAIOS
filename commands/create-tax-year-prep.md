# Command — /create-tax-year-prep

## Purpose

Produce a structured end-of-financial-year preparation package for an Australian investment property — organising income and expense records, flagging capital works questions, checking depreciation status, and generating a document checklist and questions for the accountant appointment.

## Inputs required

The user provides:
- Property (suburb, state, type)
- Ownership structure (sole / joint / trust / SMSF)
- Financial year (30 June 20XX)
- Whether a property manager annual statement has been received
- Rental income for the year
- Loan interest paid for the year
- Any capital works or improvements carried out this year
- Depreciation schedule status
- Whether the property was purchased or sold this financial year

## Steps

1. Collect the inputs above
2. Invoke the [Tax Year Prep Agent](../agents/tax-year-prep-agent.md)
3. Run the [tax-year-prep skill](../skills/tax-year-prep.md)
4. Return the 7-section package

## Output format

See [tax-year-prep-report.md](../report-templates/tax-year-prep-report.md)

## Disclaimer

This is general information and educational preparation only. Not tax advice. All deductibility questions require confirmation from a registered tax agent. Tax rules change — verify current requirements with the ATO or your registered tax agent before relying on any output.

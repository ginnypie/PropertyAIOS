# Command — /create-self-employed-lending-pack

## Purpose

Produce the exact set of documents a self-employed or business-owner borrower needs from their accountant for a home or investment loan application — tailored to their entity structure (sole trader / company / trust / SMSF) — plus a ready-to-send accountant request email. This is a preparation checklist, not credit advice.

## Inputs required

The user provides:
- Borrower name(s)
- Entity structure (list EVERY entity — sole trader / partnership / company / trust / SMSF)
- Number of entities involved
- Lending purpose (purchase / refinance / investment)
- Financial years required (usually the last 2 completed FYs)
- GST registered / lodges BAS (yes / no / unsure)
- Accountant name or firm (only if sending the request email)

## Steps

1. Collect the inputs above
2. Invoke the [Self-Employed Lending Agent](../agents/self-employed-lending-agent.md)
3. Run the [self-employed-lending-prep skill](../skills/self-employed-lending-prep.md)
4. Return the 5-section document pack

## Output format

See [self-employed-lending-doc-request.md](../report-templates/self-employed-lending-doc-request.md)

## Disclaimer

This is general information and educational preparation only. It is a document-preparation checklist, **not credit advice** and not a lender's document requirement list. Actual documents required depend on the lender, the applicant, and the entity structure, and must be confirmed with the holder of an Australian Credit Licence (ACL) or the lender. Client financial documents must only be requested with the client's authority and shared through a secure channel — never plain email attachments. Not financial, tax, or legal advice. See [disclaimers/not-credit-advice.md](../disclaimers/not-credit-advice.md) and [disclaimers/professional-review-required.md](../disclaimers/professional-review-required.md).

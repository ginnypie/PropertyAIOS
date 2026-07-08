# Command — /create-capital-gains-estimate

## Purpose

Produce a structured, indicative capital gains tax (CGT) estimate for the sale of an Australian investment property — building the cost base, working out the gross capital gain, testing 50% CGT discount eligibility, estimating CGT per owner at each owner's marginal rate, and landing on an estimated net-proceeds figure. Preparation for a conversation with a registered tax agent — not a tax calculation.

## Inputs required

The user provides:
- Purchase price and purchase date (the purchase date sets the > 12-month discount test)
- Sale price (or indicative estimate — labelled unverified if not a signed contract)
- Buying costs (stamp duty, legal/conveyancing, other acquisition costs)
- Capital improvements (cost-base additions, not repairs)
- Selling costs (agent commission, marketing, legal/conveyancing on sale)
- Ownership structure and split (e.g. 50/50 tenants in common / sole owner / company / trust)
- Main-residence history (never / yes — which periods)
- Held > 12 months? (from purchase date to sale contract date)
- Each owner's marginal tax rate

## Steps

1. Collect the inputs above
2. Invoke the [Capital Gains Agent](../agents/capital-gains-agent.md)
3. Run the [capital-gains skill](../skills/capital-gains.md)
4. Return the 6-section estimate

## Output format

See [capital-gains-report.md](../report-templates/capital-gains-report.md)

## Disclaimer

**NOT TAX ADVICE.** This is general information and educational preparation only. Every capital gain, CGT figure, and net-proceeds number is an assumption or estimate — not a tax calculation you can rely on. This command does not determine the main-residence exemption, the 6-year rule, or any other exemption — only a registered tax agent can. CGT law, rates, and thresholds change; verify current rules with the ATO and a registered tax agent before acting.

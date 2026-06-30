# CLAUDE.md — PropertyAIOS

This file tells Claude how to work in this repository.

---

## What this repo is

PropertyAIOS is an open-source AI operating system template for property investment research and preparation workflows. The primary implementation is for Australian residential property investors.

This is a **framework** — not a one-off project. Everything should be reusable, well-structured, and adaptable to other niches.

---

## How to work in this repo

### Always include disclaimers

Every skill, agent, command output, and report template must include the appropriate disclaimer from `disclaimers/`. Property investment workflows touch financial, credit, tax, and legal domains — all of which require licensed professional review.

Use the disclaimer blocks from the relevant files. Do not omit them.

### Skills are instruction sets

Files in `skills/` define how a workflow runs — inputs, process, output format, and which disclaimer applies. Keep skills focused on one workflow. If a skill grows beyond ~400 lines it probably needs splitting.

### Agents use skills

Files in `agents/` define role-based AI workers. An agent should reference which skills it uses and what persona/tone it operates with. Agents do not duplicate skill instructions — they orchestrate them.

### Commands are user-facing

Files in `commands/` define what users invoke. Commands are named with verbs: `create-suburb-report`, `create-broker-brief`. They reference agents and skills but are written for readability by non-technical users.

### Report templates are outputs

Files in `report-templates/` define what a finished report looks like. Use `[PLACEHOLDERS]` in `[BRACKETS]` for variable content. Keep sections consistent so reports are scannable.

### Prompt boards are JSON

Files in `prompt-boards/` power the website prompt card UI. Keep JSON valid. Each prompt card needs: `id`, `title`, `category`, `prompt`, `example_input`, `tags`.

---

## Australian property context

When working with AU-specific content, use:

- CoreLogic, Domain, PropTrack, REA for data sources
- State Revenue Office for stamp duty and land tax references
- ATO for tax depreciation, CGT discount, negative gearing
- APRA for lending rules and serviceability buffers
- ASIC and the Corporations Act for financial advice boundaries
- Building and pest inspection, strata report as standard due diligence steps
- Mortgage broker (ACL holder), accountant (tax agent), solicitor/conveyancer, buyer's agent (real estate licence), property manager as the professional review layer

---

## What Claude should never do in this repo

- Never provide specific financial, credit, tax, legal, or investment advice
- Never recommend a specific property, suburb, or investment strategy as "the right choice"
- Never omit disclaimers from skill outputs
- Never generate numbers as if they are accurate without clearly labelling them as estimates or illustrations
- Never suggest that AI output replaces professional review

---

## File naming conventions

- Lowercase kebab-case: `suburb-research.md`, `broker-prep-agent.md`
- No spaces, no underscores
- Command files match their command name: `create-suburb-report.md`

---

## When adding new skills, agents, or commands

Use the blank templates in `templates/`:

- `new-skill-template.md`
- `new-agent-template.md`
- `new-command-template.md`
- `new-report-template.md`
- `new-prompt-board-template.json`

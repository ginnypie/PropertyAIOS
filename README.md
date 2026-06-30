# PropertyAIOS

**Open-source AI skill system for property investment research, cash flow preparation, due diligence, and professional-review workflows.**

PropertyAIOS helps property investors organise research, test assumptions, identify risks, and prepare better questions before speaking with licensed professionals — mortgage brokers, accountants, solicitors, buyer's agents, and property managers.

This repository is a **framework template**. PropertyAIOS is the Australian property investment example. Fork it and adapt it for your niche, country, or investment strategy.

---

## What's inside

| Folder | What it contains |
|---|---|
| `skills/` | Reusable AI capability instruction sets |
| `agents/` | Role-based AI worker definitions |
| `commands/` | User-facing slash commands |
| `prompt-boards/` | JSON prompt card collections for web display |
| `report-templates/` | Structured output templates |
| `disclaimers/` | Legal and compliance disclaimer files |
| `examples/` | Filled-out example outputs (clearly fictional) |
| `docs/` | Framework documentation |
| `deployment-guides/` | How to run PropertyAIOS across different tools |
| `website-content/` | Website copy and page content |
| `templates/` | Blank templates for creating new skills/agents/commands |

---

## What PropertyAIOS does

PropertyAIOS is designed for **preparation and education only**. It does not provide financial, credit, tax, legal, or investment advice.

It helps investors:

- Research suburbs with structured, repeatable workflows
- Model cash flow scenarios before speaking with a broker or accountant
- Run due diligence risk scans before making offers
- Prepare smart questions for mortgage brokers, accountants, buyer's agents, and property managers
- Organise and review their property portfolio
- Understand risks in off-the-plan and renovation deals

---

## How to use PropertyAIOS

PropertyAIOS is a **portable AI skill system**. The repo stores the skills, agents, commands, prompt boards, report templates, examples, and disclaimers. Different tools can then run or adapt the same source material.

```
GitHub is the master copy.
Claude Cowork is where a user runs it.
Claude Code is where a builder improves it.
VS Code is where a developer adapts it.
The website is where the public uses it.
```

| Tool | Role | Guide |
|---|---|---|
| **GitHub** | Source of truth — all skills, agents, and templates live here | You are here |
| **Claude Cowork** | Where a user runs the system as a packaged property research workspace | [deployment-guides/use-in-claude-cowork.md](deployment-guides/use-in-claude-cowork.md) |
| **Claude Code** | Where a builder creates, maintains, and customises the repo | [deployment-guides/use-in-claude-code.md](deployment-guides/use-in-claude-code.md) |
| **VS Code / GitHub Copilot** | Where a developer adapts the skills as an agent library for a product | [deployment-guides/use-in-vscode.md](deployment-guides/use-in-vscode.md) |
| **Website** | Where the public uses prompt boards and report templates | [deployment-guides/use-as-website-content.md](deployment-guides/use-as-website-content.md) |
| **Managed agent / API** | Where a workflow engine runs PropertyAIOS skills programmatically | [deployment-guides/use-as-managed-agent.md](deployment-guides/use-as-managed-agent.md) |

### For a property investor (non-technical)

Use the **Claude Cowork** deployment. Create a Claude Project, add the skills files to the knowledge base, and run skills conversationally. See [deployment-guides/use-in-claude-cowork.md](deployment-guides/use-in-claude-cowork.md).

### For a builder customising the system

Use **Claude Code** to open the repo, add new skills, update disclaimers, and manage the file structure. See [deployment-guides/use-in-claude-code.md](deployment-guides/use-in-claude-code.md).

### For a developer building a product

Use **VS Code** to integrate the skills as an agent library in a web application. The prompt-boards JSON files drive the UI. The report templates define the output structure. See [deployment-guides/use-in-vscode.md](deployment-guides/use-in-vscode.md).

### For a business deploying it at scale

Use the **managed agent** pattern — an API workflow that calls AI skills, injects user inputs, and delivers structured outputs. See [deployment-guides/use-as-managed-agent.md](deployment-guides/use-as-managed-agent.md).

---

## How to fork this for your niche

```
Fork this repo → replace the niche/country/brand → build your own property AI OS
```

**Examples of what you could build:**

- `UKPropertyAIOS` — UK buy-to-let research and SDLT calculations
- `NZPropertyAIOS` — New Zealand investment property workflows
- `USRealEstateAIOS` — US rental property analysis and 1031 exchange prep
- `CommercialPropertyAIOS` — Commercial due diligence and lease analysis
- `SMSFPropertyAIOS` — Self-managed super fund property compliance
- `FirstHomeBuyerAIOS` — First home buyer research and grant workflows
- `AirbnbInvestorAIOS` — Short-term rental analysis and platform prep
- `RenovationAIOS` — Renovation risk analysis and contractor prep

See [docs/how-to-use-this-template.md](docs/how-to-use-this-template.md) for the step-by-step fork guide.

---

## Quick start

1. Fork this repository
2. Read [docs/how-to-use-this-template.md](docs/how-to-use-this-template.md)
3. Choose your deployment from [deployment-guides/](deployment-guides/)
4. Customise `CLAUDE.md` for your Claude project
5. Replace the niche-specific references in `skills/` and `agents/`
6. Update `disclaimers/` for your jurisdiction
7. Build your website using `prompt-boards/` and `website-content/`

---

## Compliance notice

All workflows in this repository are designed for **general information and preparation purposes only**.

Nothing in this repository constitutes financial advice, credit advice, tax advice, legal advice, or a recommendation to buy or sell any property or financial product.

Always review outputs with appropriately licensed professionals before making decisions.

Builders adapting this framework for commercial use should read [docs/compliance-and-disclaimers.md](docs/compliance-and-disclaimers.md) and get their own legal advice before launching.

See [disclaimers/](disclaimers/) for reusable disclaimer blocks.

---

## License

MIT — fork, adapt, and build on it. See [LICENSE](LICENSE).

---

## Built by

[PropertyAIOS](https://propertyaios.com.au) — an AI-assisted property investment preparation system for Australian investors.

# Using PropertyAIOS in Claude Code

**Deployment type:** Builder and developer environment for creating, maintaining, and customising the repo.

---

## What this deployment is

Claude Code is Anthropic's coding CLI that runs in your terminal. It reads files, writes code, runs commands, and maintains context across the whole repository.

For PropertyAIOS, Claude Code is the **builder's environment** — where you:

- Add new skills, agents, and commands
- Customise existing files for your niche or market
- Update disclaimers for your jurisdiction
- Manage the repo structure
- Build and deploy the website

---

## How to use it

### Clone the repo

```bash
git clone https://github.com/your-username/propertyaios
cd propertyaios
```

### Open Claude Code

```bash
claude
```

Claude Code reads `CLAUDE.md` automatically and understands the repo structure, conventions, and compliance rules from that file.

### Tell Claude Code what to build

Examples:

```
Add a new skill for SMSF property purchases. Follow the format in templates/new-skill-template.md and use skills/off-the-plan-risk.md as a style reference.
```

```
Update all the disclaimers in disclaimers/ to add a note that outputs must be reviewed by the user before sharing with a third party.
```

```
The accountant-prep skill needs a section on depreciation schedules. Add it after Section 3.
```

```
Create a new prompt-board JSON file for renovation analysis with 3 cards. Follow the format in prompt-boards/suburb-research.json.
```

---

## How CLAUDE.md guides the build

`CLAUDE.md` at the repo root tells Claude Code:

- The purpose and positioning of the repo
- What Claude must never do (give advice, invent figures, omit disclaimers)
- The file naming conventions
- Which disclaimer goes with which workflow type
- The Australian property context (data sources, professional roles, regulatory bodies)

When you ask Claude Code to add or edit a skill, it reads `CLAUDE.md` first and applies those rules automatically.

---

## Recommended workflows for builders

| Task | Prompt to give Claude Code |
|---|---|
| Add a new skill | "Add a skill for [topic] in skills/. Follow the template in templates/new-skill-template.md. Ensure it has an output contract, safety boundaries, and a disclaimer block." |
| Update for a new market | "Adapt all files in skills/ from Australian to UK market. Replace AU regulatory references with UK equivalents. See docs/how-to-use-this-template.md for the substitution table." |
| Add to the prompt board | "Add a new card to prompt-boards/[board].json for [skill]. Follow the card structure in the existing cards." |
| Review before publishing | "Review the repo for any wording that sounds like financial, credit, tax, or legal advice. Report any instances and suggest corrections." |

---

## Git workflow

Work on a branch, not main:

```bash
git checkout -b add-smsf-skill
```

Commit each skill or change separately:

```bash
git add skills/smsf-property.md
git commit -m "Add SMSF property purchase skill"
```

---

## What Claude Code does in this repo

- Reads all files to understand context before writing
- Follows the skill/agent/command/report-template structure
- Always includes disclaimers in new skills and agents
- Follows the file naming conventions from CLAUDE.md
- Does not add private business information or branded content that would need to be removed before publishing

---

## Disclaimer

> Use Claude Code to build and maintain the repo — not to generate property investment advice. All content created in this repo must follow the compliance rules in CLAUDE.md and docs/compliance-and-disclaimers.md.

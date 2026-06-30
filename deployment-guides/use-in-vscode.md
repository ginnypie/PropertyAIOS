# Using PropertyAIOS in VS Code and GitHub Copilot

**Deployment type:** Developer environment for adapting the repo as an agent skill library.

---

## What this deployment is

VS Code with GitHub Copilot (or other AI coding extensions) can use this repo as an **agent skills library** — a structured set of instruction files, prompt templates, and output contracts that a developer can wire into a web application, API, or AI workflow.

This deployment is for **developers** who want to build a product on top of the PropertyAIOS framework.

---

## What the repo gives a developer

| Folder | What a developer uses it for |
|---|---|
| `skills/` | Prompt templates and output contracts for each workflow |
| `agents/` | Role definitions for AI agents in a multi-agent system |
| `commands/` | User-facing command specs for a web app or chat interface |
| `prompt-boards/` | Ready-made JSON to drive a prompt card UI |
| `report-templates/` | Output structure definitions for report generators |
| `disclaimers/` | Compliance text blocks to inject into every output |
| `templates/` | Blank templates for generating new skills programmatically |

---

## How to use skills/ as an agent skills library

Each file in `skills/` follows a consistent structure:

```
Purpose
Reads from / Writes to
Inputs required
Output contract (numbered sections)
Safety boundaries
Professional review prompts
Disclaimer
```

A developer can:

1. Parse the skill files programmatically
2. Extract the **Inputs required** section to generate a form or input schema
3. Extract the **Output contract** to define the expected response structure
4. Inject the **Disclaimer** block into every output before displaying to the user
5. Use the **Safety boundaries** as validation rules in a pre/post-processing layer

---

## How to use prompt-boards/ as a web UI data source

The JSON files in `prompt-boards/` are structured for direct use as a prompt card component:

```json
{
  "id": "suburb-risk-scan",
  "title": "Suburb Risk Scanner",
  "category": "Suburb Research",
  "description": "Run a structured risk scan on any suburb before you book an inspection.",
  "prompt": "...",
  "best_for": "...",
  "output_type": "...",
  "professional_review_note": "..."
}
```

Feed this into a React component, Next.js page, or any web framework to generate a public prompt board UI with copy buttons, categories, and disclaimer blocks.

---

## How to use report-templates/ as output schema

Each report template defines the sections and placeholders for a finished output. A developer can:

- Use the section headings as schema definitions for structured AI outputs
- Build a form that maps to the `[PLACEHOLDER]` fields
- Use the disclaimer blocks at the bottom as required footers in the UI

---

## How to adapt for a different AI provider

The skills, agents, and prompt templates in this repo are model-agnostic. They are written as instruction text — not tied to any specific API.

To use with OpenAI, Gemini, or another provider:

1. Take the prompt text from a skill's **Output contract** section
2. Format it as a system prompt + user message for your provider's API
3. Add the relevant disclaimer from `disclaimers/` to the response before displaying
4. Validate that the output stays within the safety boundaries defined in the skill

---

## Extending the library

Use the blank templates in `templates/` to generate new skills, agents, or prompt cards:

```bash
cp templates/new-skill-template.md skills/my-new-skill.md
# Edit the file, fill in the sections
```

---

## GitHub Copilot tips

With GitHub Copilot Chat open in VS Code:

- Ask: "What is the output contract for the suburb-research skill?"
- Ask: "Generate a new prompt board card for renovation risk following the format in prompt-boards/suburb-research.json"
- Ask: "What disclaimer should I add to an output that discusses borrowing capacity?"

Copilot reads the repo files as context and can answer these questions accurately.

---

## Compliance note for developers

When building a product on this framework:

1. Always inject the appropriate disclaimer from `disclaimers/` into every output surface
2. Do not remove or weaken the safety boundaries defined in each skill
3. If your product could be interpreted as providing financial, credit, tax, or legal advice — get your own legal advice about your compliance obligations
4. Add your own licence details and compliance contact where required by your jurisdiction

The `docs/compliance-and-disclaimers.md` document explains the compliance framework in detail.

---

## Disclaimer

> This repo is general information and preparation content. Not financial, credit, tax, or legal advice. Developers building products on this framework are responsible for their own compliance obligations in their jurisdiction.

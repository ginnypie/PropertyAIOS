# Using PropertyAIOS in Claude Cowork (claude.ai Projects)

**Deployment type:** Packaged AI workspace for property investors and professionals.

---

## What this deployment is

Claude Cowork (Projects at claude.ai) lets you create a persistent AI workspace with a custom system prompt, uploaded files, and memory that carries across conversations.

PropertyAIOS is designed to run as a packaged property investment preparation workspace in Claude Cowork. A user opens the workspace, runs skills, and the AI maintains context across the session.

---

## How to set it up

### Step 1 — Create a new Claude Project

Go to [claude.ai](https://claude.ai), create a new Project, and give it a name:

```
Property Research Assistant
```

or

```
PropertyAIOS — [Your Name / Suburb / Portfolio]
```

### Step 2 — Add the system prompt

In the Project instructions, paste the contents of `CLAUDE.md` from this repo.

This tells Claude:
- What PropertyAIOS is and how it works
- How to handle disclaimers
- What it must never do (give advice, omit disclaimers, fabricate figures)
- How to write to and read from the Property File

### Step 3 — Upload key files

Upload to the Project knowledge base:

| File | Purpose |
|---|---|
| `skills/suburb-research.md` | Suburb research workflow |
| `skills/property-cash-flow.md` | Cash flow stress test |
| `skills/due-diligence-risk-scan.md` | Due diligence checklist |
| `skills/broker-prep.md` | Broker meeting prep |
| `skills/accountant-prep.md` | Accountant meeting prep |
| `disclaimers/general-information.md` | Standard disclaimer block |
| `disclaimers/not-financial-advice.md` | Finance disclaimer |
| `disclaimers/not-credit-advice.md` | Credit disclaimer |
| `disclaimers/not-tax-advice.md` | Tax disclaimer |

Upload more skill files as you need them.

### Step 4 — Start a Property File

In the first conversation, run the Strategy Agent skill to build your Investor Profile. Then run Listing Analysis (Skill 01) on your first property to generate your starter Property File.

Keep the Property File as a running document. Paste it at the top of each new skill conversation so the AI can read and update it.

---

## How a typical session works

1. User opens the Claude Project
2. User pastes their Property File (or starts a new one)
3. User types a command: "Run the suburb research skill for [suburb, state]"
4. Claude runs the skill, returns the structured output, and adds a PROPERTY FILE UPDATE block
5. User copies the update back into their Property File

---

## What works well in this deployment

- Long sessions with multiple skills chained together
- The Property File as persistent context across conversations
- The system prompt in CLAUDE.md preventing Claude from giving advice
- Professional preparation workflows run start-to-finish in one sitting

---

## Limitations

- Each conversation has a context limit — very large Property Files may need to be trimmed
- Claude does not have access to live property data (CoreLogic, Domain, REA) unless integrations are added
- Users need to manage their own Property File document outside of Claude

---

## For property professionals running this for clients

You can set up a shared Claude Project for client onboarding:
- Upload the relevant skills for your workflow (e.g. broker-prep for a mortgage broker, buyers-agent-brief for a buyer's agent)
- Customise the system prompt with your firm's tone and compliance requirements
- Add your own disclaimer block with your licence number and contact details

**Important:** Always add your own compliance layer on top of the PropertyAIOS template. The template is a starting point — not a compliance solution for commercial client use.

---

## Disclaimer

> PropertyAIOS outputs in Claude Cowork are general information and educational preparation only. Not financial, credit, tax, or legal advice. See [docs/compliance-and-disclaimers.md](../docs/compliance-and-disclaimers.md).

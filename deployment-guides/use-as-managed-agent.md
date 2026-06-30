# Using PropertyAIOS as a Managed Agent or API Workflow

**Deployment type:** Backend AI workflow engine running PropertyAIOS skills as managed agents via API.

---

## What this deployment is

A managed agent deployment runs PropertyAIOS skills programmatically — without a human typing prompts into Claude. Instead, a backend system calls the AI API, passes the skill prompt and user inputs, receives a structured response, and delivers it to a user interface.

This is the most technically advanced deployment. It is suitable for:

- Platforms that want to embed PropertyAIOS workflows as a feature (e.g. a property portal, broker CRM, or buyer's agent platform)
- Automated report generation systems (user fills in a form, system generates a report)
- Workflow engines like n8n, Make, or Zapier that trigger skills based on user actions
- Custom API integrations with property data providers (CoreLogic, Domain, PropTrack)

---

## Architecture overview

```
User Input (form / chat / API)
        ↓
Skill Selector (which skill to run)
        ↓
Input Validator (required fields present?)
        ↓
Prompt Builder (fill skill template with user inputs)
        ↓
AI API Call (Claude / OpenAI / other)
        ↓
Output Parser (extract sections from structured response)
        ↓
Disclaimer Injector (append appropriate disclaimer from disclaimers/)
        ↓
Output Delivery (web UI / PDF / email / CRM)
```

---

## How skills map to API calls

Each skill file in `skills/` defines:

| Element | Maps to |
|---|---|
| `Inputs required` section | API request body schema |
| `Output contract` section | Expected response structure |
| `Safety boundaries` | Pre/post-processing validation rules |
| `Disclaimer` | Required footer on every response |

A managed agent system reads these definitions and builds the API call automatically.

---

## Example: running the Cash Flow skill as a managed agent

**Input schema (from skills/property-cash-flow.md):**

```json
{
  "property": "string (suburb, state, type, beds/baths)",
  "purchase_price": "number",
  "lvr": "string (80% / 90% / other)",
  "loan_type": "string (interest-only / P&I)",
  "estimated_rate": "number",
  "estimated_weekly_rent": "number",
  "tax_position": "string (32.5% / 37% / 45%)",
  "depreciation": "string (yes / no / unsure)"
}
```

**System prompt:**
Use the contents of `skills/property-cash-flow.md` as the system prompt (the Purpose, Output contract, and Safety boundaries sections).

**User message:**
Fill the Inputs required template with the user's values.

**Post-processing:**
Extract the 6 output sections, validate that the disclaimer is present, and deliver to the user.

---

## The Property File in a managed agent context

In a managed agent deployment, the Property File is a database record rather than a pasted document:

```json
{
  "property_id": "...",
  "investor_profile": { ... },
  "snapshot": { ... },
  "cash_flow_assumptions": { ... },
  "finance_position": { ... },
  "suburb_demand": { ... },
  "red_flags": [ ... ],
  "verify_with_pro": [ ... ],
  "decision_log": { ... }
}
```

Each skill reads the relevant sections from this record and writes its output back. This replaces the manual "paste your Property File" step that human users do in Claude Cowork.

---

## Workflow engine integration (n8n, Make, Zapier)

A no-code workflow engine can run PropertyAIOS skills as automated nodes:

1. **Trigger:** User submits a property form on a website
2. **Node 1:** Call AI API with the Listing Analysis skill prompt and user inputs
3. **Node 2:** Store the output in the Property File database record
4. **Node 3:** Call AI API with the Suburb Research skill using the same property
5. **Node 4:** Generate a PDF report from the combined outputs using the report template
6. **Node 5:** Email the report to the user with the standard disclaimer block appended

---

## Integrating live property data

PropertyAIOS skills are written for users who provide their own data. In a managed agent deployment, you can integrate live data sources:

| Data type | Source (AU) | How to inject |
|---|---|---|
| Recent median prices | CoreLogic API / PropTrack | Inject into suburb-research skill inputs |
| Rental yield estimates | Domain / REA API | Inject into cash-flow skill inputs |
| Comparable sales | CoreLogic / RP Data | Inject into comparable-sales skill context |
| Flood overlays | State emergency services portals | Inject into due-diligence skill inputs |
| Stamp duty | State Revenue Office calculators | Pre-calculate and inject into report templates |

**Important:** If you inject live data, you must clearly label it as sourced data (not AI-generated) and cite the source. Live data does not change the disclaimer requirement — outputs are still preparation material, not advice.

---

## Compliance requirements for managed agent deployments

If you are building a commercial product using this system:

1. **Get legal advice** specific to your product and your jurisdiction before launching
2. **Do not remove disclaimers** from any output — the disclaimer must appear on every output surface visible to the user
3. **Do not promise accuracy** — even with live data injected, outputs are preparation material
4. **Log outputs** — keep records of what your system generated and when, in case of disputes
5. **Add your own compliance layer** — if your product is used by licensed professionals (brokers, financial advisers), ensure their compliance obligations are met
6. **Consider AFSL/ACL scope** — if your system's outputs could be interpreted as financial product advice or credit assistance, seek specific legal guidance before commercial launch in Australia

---

## Model recommendations

PropertyAIOS skills are designed to work with capable language models. For production deployments:

- Use a model with strong instruction-following (outputs need to follow the Output contract exactly)
- Use temperature 0 or close to it for structured report generation (consistency matters)
- Add a post-processing validation step to confirm all required sections are present before delivering to users

---

## Disclaimer

> Managed agent deployments of PropertyAIOS generate general information and educational preparation content only. This framework is not a licensed financial services product. Builders deploying this system commercially are responsible for their own compliance with financial services, credit, tax, and consumer law in their jurisdiction. See [docs/compliance-and-disclaimers.md](../docs/compliance-and-disclaimers.md) before building.

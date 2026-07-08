# Getting Started — Install & Use PropertyAIOS (5 minutes)

No coding needed. PropertyAIOS is a set of AI "skills" (instruction files) you run inside Claude. Here are three ways to use them — pick the easiest that suits you.

> Reminder: everything PropertyAIOS produces is **general information and preparation only** — not financial, credit, tax, or legal advice. Always review with a licensed professional.

---

## Option A — Claude Project (easiest, non-technical) ⭐

1. On the repo's GitHub page, click the green **Code** button → **Download ZIP**, and unzip it.
2. Open the **Claude app** (desktop or claude.ai) → **Projects** → **New project** (call it "PropertyAIOS").
3. Add the files from the `skills/` folder to the project's **knowledge** (drag them in).
4. Paste the contents of `CLAUDE.md` into the project's **custom instructions**.
5. Start chatting. For example:
   > "Use the **property-appraisal** skill. Address: 13 Example St, and here are 4 recent nearby sales… give me the indicative value range."

That's it — Claude will follow the skill and produce the structured report.

---

## Option B — Upload as Claude Skills (auto-activating)

If your Claude plan has **Skills** (Settings → Capabilities → Skills), you can upload a skill so it triggers automatically. This needs each skill in the `skill-name/SKILL.md` folder format with a small header — see [docs/how-to-use-this-template.md](how-to-use-this-template.md). Once uploaded, just describe your task and the matching skill activates.

---

## Option C — Connect GitHub (always up to date)

In the Claude app, go to **Settings → Connectors → GitHub**, connect your account, and point Claude at the repo. Claude can then read the skills directly — no download, always current.

---

## How to run any skill

Every skill lists an **"Inputs required"** block at the top. Give Claude those inputs and name the skill:

> "Run **borrowing-power** with this info: income $120k PAYG, one $10k credit card limit, HECS $20k…"

Claude returns the skill's structured output (with its formulas, ranges, and disclaimer). You then take that to your broker, accountant, or valuer.

---

## Which skill do I use?

See the full list in the [README](../README.md#skills-included), grouped by workflow (research & value, cash flow, finance & lending, due diligence, tax, buying & managing). Start with **property-appraisal** (value a property), **property-cash-flow** (analyse a deal), or **borrowing-power** (what you can borrow).

---

## Running it in other tools

PropertyAIOS also runs in Claude Cowork, Claude Code, VS Code, or as a managed agent — see the [deployment-guides/](../deployment-guides/).

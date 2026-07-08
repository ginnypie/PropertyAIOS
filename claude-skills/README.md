# PropertyAIOS — Claude Skills

These are the same PropertyAIOS workflows found in [`../skills/`](../skills/), repackaged in the Claude **Skills** format so you can upload them directly into Claude.

## What's here

Each skill lives in its own folder containing a single `SKILL.md` file:

```
claude-skills/
  property-appraisal/
    SKILL.md
  borrowing-power/
    SKILL.md
  ...
```

Every `SKILL.md` starts with YAML frontmatter:

```
---
name: <skill-name>
description: "Use when ..."
---

<the original skill markdown>
```

- **`name`** is the kebab-case skill id (matches the folder name).
- **`description`** is a trigger-style line derived from the skill's own **Use when:** line. Claude reads it to decide when to auto-activate the skill.
- The body is the full, unchanged skill content from `../skills/`, including its disclaimer.

The original files in `../skills/` are untouched — these bundles are copies with frontmatter added.

## How to use

1. In Claude, go to **Settings → Capabilities → Skills**.
2. Upload a skill folder — or zip a `<skill-name>/` folder (so the archive contains `<skill-name>/SKILL.md`) and upload the `.zip`.
3. Once uploaded, the skill **auto-activates** whenever your request matches its `description`. For example, asking Claude to help you sanity-check a property price will trigger `comparable-sales`.

You can upload as many of these as you like — each is self-contained.

## Important

These skills are **educational and preparation tools only**. They do **not** provide financial, credit, tax, legal, or investment advice, and their output is never a substitute for review by a licensed professional (mortgage broker, accountant/tax agent, solicitor/conveyancer, buyer's agent, or valuer). Each `SKILL.md` carries its own disclaimer — read it.

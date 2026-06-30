# What is PropertyAIOS?

PropertyAIOS is an AI operating system for property investment research and preparation.

It is not a prompt library. It is a connected system.

---

## The three primitives

### 1. The Property File

One running document per property (or per search). Every skill reads relevant sections and writes its output back into it. This is the persistent memory that makes the system feel like software, not a chatbot.

```
# PROPERTY FILE — [address / suburb]
Last updated: [date]

## INVESTOR PROFILE        ← from Strategy Agent
## SNAPSHOT                ← from Listing Analysis
## CASH-FLOW ASSUMPTIONS   ← from Listing Analysis / Cash Flow Stress Test
## FINANCE POSITION        ← from Borrowing Power
## SUBURB & DEMAND         ← from Suburb Research / Comparables
## RED FLAGS (open)        ← every skill appends here
## VERIFY-WITH-A-PRO       ← every skill appends here
## DECISION LOG            ← from Buy, Wait or Walk Away
```

### 2. Skills

Each prompt is a skill with a strict input/output contract and explicit "reads from / writes to" the Property File. Skills are ordered, chainable, and share context — so each one builds on the last.

### 3. The Spine

Skills are ordered into the real buying journey:

```
Set Up → Analyse → Finance → Stress-Test → Decide
```

You always know what stage you're in and what the next move is.

---

## What PropertyAIOS is for

PropertyAIOS helps property investors:

- Run structured suburb research before inspecting
- Model cash flow scenarios before speaking to a broker
- Identify risks in strata buildings, off-the-plan contracts, and renovation deals
- Prepare smart questions for mortgage brokers, accountants, buyer's agents, and property managers
- Stress-test their portfolio against rate rises and vacancy
- Decide: buy, wait, or walk away

---

## What PropertyAIOS is not

PropertyAIOS is **not** financial advice, credit advice, tax advice, legal advice, a property valuation, or a recommendation to buy or sell.

It is a preparation and education system. Every output is designed to help you ask better questions — not to replace the professionals who give licensed advice.

---

## Who built this

PropertyAIOS was built by a former stockbroker and specialist mortgage broker of 20 years. The financial modelling discipline that institutional investors take for granted — stress-testing assumptions, reading the bear case first, separating what you know from what you are estimating — applied to Australian residential property decisions.

---

## The core message

**Analyse first. Finance-check second. Decide third.**

---

## The compliance spine

Every skill in PropertyAIOS carries this compliance spine:

- General information and educational preparation only
- Not financial, credit, tax, legal, or valuation advice
- All figures are assumptions requiring verification
- Review with appropriately licensed professionals before making decisions

See [compliance-and-disclaimers.md](compliance-and-disclaimers.md) and the [disclaimers/](../disclaimers/) folder.

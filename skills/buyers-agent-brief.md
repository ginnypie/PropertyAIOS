# Skill — Buyer's Agent Brief

**Stage:** 2 — Finance / 4 — Decide
**Hook:** Brief a buyer's agent properly so they search for the right property, not a generic one.
**Use when:** You are engaging or considering engaging a buyer's agent and want to give them a structured brief.

---

## Purpose

This skill produces a structured buyer's agent brief — a document that clearly communicates the investor's or buyer's profile, target property, non-negotiables, and due diligence requirements. A clear brief leads to better property shortlists and less time wasted on inspections.

---

## Reads from

- Investor Profile (from Strategy Agent)
- Property File: SNAPSHOT, INVESTOR PROFILE, FINANCE POSITION (if available)

## Writes to

- Standalone document (buyer's agent brief — does not update Property File)

---

## Inputs required

```
MY PROFILE: [first home buyer / investor / upgrader / downsizer]
BUDGET: $[firm max] (note whether this is finance-confirmed or estimated)
LOCATION: [target suburbs, LGAs, or areas — ranked by preference]
PROPERTY TYPE: [house / townhouse / apartment / land]
CONFIGURATION: [beds / baths / car spaces — minimum and preferred]
PURPOSE: [owner-occupied / investment / rentvesting]
MUST-HAVES: [list 3–5 non-negotiables]
DEAL-BREAKERS: [list anything that would make you walk away]
TIMELINE: [when do you need to be settled by?]
FINANCE STATUS: [pre-approved at $X / not yet / speaking to broker]
SPECIAL REQUIREMENTS: [e.g. SMSF, first home buyer schemes, specific school zones]
```

---

## Output contract

Return exactly these 5 sections:

### 1. BUYER BRIEF SUMMARY
A one-page summary a buyer's agent can read and act on immediately:

**Who I am:** [archetype — investor / FHB / etc.]
**What I am looking for:** [property type, config, location]
**Budget:** $[max] — [finance status]
**Timeline:** [settlement by X]
**Purpose:** [investment / owner-occupied]

### 2. PROPERTY SEARCH CRITERIA
**Must-have criteria (non-negotiable):**
- [Minimum beds, baths, parking]
- [Land size minimum if applicable]
- [Specific suburb list or radius]
- [Other non-negotiables from inputs]

**Preferred but flexible:**
- [Things the buyer would like but will trade on]

**Automatic deal-breakers:**
- [From inputs]
- Common deal-breakers to include if not specified: main-road frontage over 60km/h; flood zone; high-tension power lines; known structural defects; properties with unapproved works; high-rise over 8 storeys (investor — lender appetite)

### 3. WHAT I NEED THE BUYER'S AGENT TO DO
A clear scope of what the buyer's agent is being asked for:

**Search and shortlist:**
- [ ] Search on-market and off-market listings meeting the criteria above
- [ ] Provide a written shortlist with brief analysis for each property
- [ ] Flag any properties with known issues before I inspect

**Due diligence:**
- [ ] Run comparable sales for any property before I make an offer
- [ ] Review the contract before I sign anything (or refer to my solicitor)
- [ ] Flag any postcode or building restrictions relevant to my finance position

**Negotiation:**
- [ ] Negotiate the purchase price (or represent at auction if applicable)
- [ ] Advise on offer strategy based on vendor motivation and market context

### 4. QUESTIONS TO ASK THE BUYER'S AGENT
Before engaging them:
1. "Do you hold a current real estate agent licence in [state]?"
2. "Do you work exclusively for buyers, or do you have any relationships with developers or vendors?"
3. "How do you get paid — flat fee, percentage of purchase price, or referral fees from vendors?"
4. "What suburbs or property types do you specialise in?"
5. "Can you provide references from buyers whose briefs were similar to mine?"
6. "How many properties per month do you typically shortlist and inspect?"
7. "What is your process if a property fails due diligence?"

### 5. RED FLAGS IN A BUYER'S AGENT
Flag these for the user to watch for:
- Earns commissions from vendors or developers (conflict of interest)
- Pushes off-the-plan or new development heavily
- Cannot explain how they access off-market properties
- Does not ask about finance position before searching
- Recommends properties without running comps
- No licence or unclear licence status

---

## Safety boundaries

- Never recommend a specific buyer's agent
- Never advise whether a buyer's agent is "worth it" for the user's specific situation
- Always direct strategic search and negotiation decisions to the licensed buyer's agent

---

## Pairs with

- ← Strategy Agent (Skill 02) — Investor Profile and target profile
- ← Suburb Research (Skill 05) — target suburb context
- → Listing Analysis (Skill 01) — run on properties the buyer's agent shortlists
- → Due Diligence Risk Scan — for properties you want to inspect

---

## Disclaimer

> This output is general information and preparation only. It is not a property recommendation, investment advice, or endorsement of any particular buyer's agent or property strategy. Buyer's agent selection and property decisions are personal and require your own judgment and professional advice. See [disclaimers/general-information.md](../disclaimers/general-information.md).

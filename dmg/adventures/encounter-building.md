---
type: dm-reference
version: dnd-5e-2024
source: DMG 2024, Chapter 4
source_detail: "Chapter 4: Creating Adventures — Combat Encounter Difficulty (p. 83), Treasure (p. 120-121)"
verification:
  status: partially-verified
  method: "XP Budget table checked against D&D Beyond official text"
  verified_by: moco
  verified_at: 2026-05-22
  notes: "XP Budget and difficulty categories verified. Social/exploration/reward sections summarized from DMG guidance, not line-checked."
updated: 2026-05-23
---

# Chapter 4: Creating Adventures — Encounter Building & Rewards

---

## Combat Encounter Building

### RAW Summary

**Difficulty Categories (2024):** Low, Moderate, High (replaces 2014's Easy/Medium/Hard/Deadly).

**Procedure:**
1. Look up **XP Budget Per Character** for each PC's level
2. Choose difficulty: **Low**, **Moderate**, or **High**
3. **Sum** the XP budgets for all PCs → total encounter XP budget
4. Select monsters whose **combined XP** fits within that budget
5. **No multiplier** — just add raw monster XP totals directly

**XP Budget Per Character**

*Source: DMG 2024, p. 83 — "XP Budget per Character" table. Verified against D&D Beyond.*

| Level | Low | Moderate | High |
|---:|---:|---:|---:|
| 1 | 50 | 75 | 100 |
| 2 | 100 | 150 | 200 |
| 3 | 150 | 225 | 400 |
| 4 | 250 | 375 | 500 |
| 5 | 500 | 750 | 1,100 |
| 6 | 600 | 1,000 | 1,400 |
| 7 | 750 | 1,300 | 1,700 |
| 8 | 1,000 | 1,700 | 2,100 |
| 9 | 1,300 | 2,000 | 2,600 |
| 10 | 1,600 | 2,300 | 3,100 |
| 11 | 1,900 | 2,900 | 4,100 |
| 12 | 2,200 | 3,700 | 4,700 |
| 13 | 2,600 | 4,200 | 5,400 |
| 14 | 2,900 | 4,900 | 6,200 |
| 15 | 3,300 | 5,400 | 7,800 |
| 16 | 3,800 | 6,100 | 9,800 |
| 17 | 4,500 | 7,200 | 11,700 |
| 18 | 5,000 | 8,700 | 14,200 |
| 19 | 5,500 | 10,700 | 17,200 |
| 20 | 6,400 | 13,200 | 22,000 |

Multiply the per-character value by the number of PCs to get the total XP budget.

**Difficulty Definitions:**

| Difficulty | Risk Level | Description |
|---|---|---|
| **Low** | Minimal | Characters unlikely to be seriously threatened. One or more may need healing resources. A single monster with CR = party level is roughly Low difficulty for 4 PCs. |
| **Moderate** | Moderate | Could go badly without healing. Weaker characters might go down. Slim chance of death. |
| **High** | Serious | Could be lethal. Characters need smart tactics, quick thinking, and maybe luck to survive. |

**No Encounter Multiplier.** The 2024 DMG completely removes the multiplier from 2014. Total monster XP values directly regardless of monster count.

**Key Changes from 2014:**

| Change | 2014 | 2024 |
|---|---|---|
| Difficulty categories | 4 (Easy/Medium/Hard/Deadly) | 3 (Low/Moderate/High) |
| Encounter multiplier | Yes (×1.5 to ×4) | Removed |
| XP threshold meaning | Floor | Ceiling |

### Table-Ready Procedure

```
1. Party: How many PCs? What levels?
2. Difficulty: Low (routine) / Moderate (challenging) / High (deadly)?
3. Budget: Look up XP per character → multiply by party size
4. Monsters: Pick monsters whose TOTAL XP ≤ budget
5. No multiplier — just raw XP total
6. Sanity check: Does this feel right for the moment?
```

**Quick Party-of-4 Totals:**

| Level | Low | Moderate | High |
|---:|---:|---:|---:|
| 1 | 200 | 300 | 400 |
| 5 | 2,000 | 3,000 | 4,400 |
| 10 | 6,400 | 9,200 | 12,400 |
| 15 | 13,200 | 21,600 | 31,200 |
| 20 | 25,600 | 52,800 | 88,000 |

**Examples from DMG:**
- Low for 4 × Lv 1: Budget 200 XP → 1 Bugbear Warrior (200 XP) or 2 Giant Wasps (100 each)
- Moderate for 5 × Lv 3: Budget 1,125 XP → 2 Nothics (450 each) + 9 Stirges (25 each)
- High for 6 × Lv 15: Budget 46,800 XP → 2 Adult Red Dragons (18,000 each) + 2 Fire Giants (5,000 each)

### DM Notes

- **Many Creatures:** More than 2 creatures per character = higher risk of lucky damage streaks. Include fragile creatures that go down fast. Especially important at levels 1-2.
- **Powerful Creatures:** A creature with CR > party level might one-shot low-HP characters. An Ogre (CR 2) can kill a level 1 Wizard in one hit.
- **CR 0 Creatures:** Use sparingly. If you want many CR 0 critters, use swarms instead.
- **Stat Block Limit:** Try to keep unique stat blocks to 2-3 per encounter for manageability.
- **On-the-Fly Adjustment:** Reinforce if too easy, have monsters flee if too hard.

---

## Social Interaction Encounters

### RAW Summary

*Source: DMG 2024, Chapter 4 — Social Interaction Encounters. [NEEDS VERIFICATION — summarized, not line-checked]*

NPCs have an **Initial Attitude**: Friendly, Indifferent, or Hostile. Determine randomly with d12:

| d12 | Attitude |
|---|---|
| 4 or lower | Hostile |
| 5–8 | Indifferent |
| 9 or higher | Friendly |

*(Roll different dice to alter range: 1d6 for predators, 1d6+3 for travelers, 1d6+6 for kindhearted.)*

**Monster Personality (d8):**
1. Cowardly; surrenders easily
2. Greedy; wants treasure
3. Boastful; showy but runs
4. Disorderly; easily rattled
5. Fanatical; ready to die
6. Brave; stands firm
7. Jocular; taunts enemies
8. Orderly; difficult to rattle

### Table-Ready Procedure

1. Define NPC attitude (Friendly / Indifferent / Hostile)
2. Let players roleplay their approach
3. Call for Charisma checks when outcome is uncertain:
   - Persuasion — logical/emotional appeal
   - Deception — lies and misdirection
   - Intimidation — threats and coercion
   - Insight (Wisdom) — reading motives
4. Shift attitude based on roleplay + results

### DM Notes

Social encounters should feel like encounters — with stakes, choices, and consequences — not just "roll Persuasion." A hostile NPC who is intimidated may comply but retaliate later.

---

## Exploration Encounters

### DM Notes

*Source: DMG 2024, Chapter 4 — general guidance. Not RAW mechanical rules.*

Exploration encounters test resourcefulness, perception, and problem-solving:
- **Traps** — See `dmg/toolbox/dm-toolbox.md` for mechanics
- **Puzzles** — Present information, require creative solutions
- **Environmental Hazards** — Extreme weather, difficult terrain, collapsing structures
- **Navigation** — Getting lost, tracking, pathfinding
- **Discovery** — Hidden locations, clues, investigation

---

## Adventure Rewards

### RAW Summary

*Source: DMG 2024, Chapter 2 — Character Advancement; Chapter 7 — Treasure.*

**XP Awards:** Monsters grant XP per their stat block. Divide total XP equally among all party members (including helpful NPCs). Non-combat challenges can award XP at DM discretion.

**Milestone Leveling:** PCs level up when they achieve story milestones. No XP tracking needed. Major milestone = high-difficulty encounter XP. Minor milestone = low-difficulty.

**Magic Items Awarded by Level** (verified — see `dmg/treasure/treasure-reference.md`):

| Tier (Levels) | Common | Uncommon | Rare | Very Rare | Legendary | Total |
|---|---|---|---|---|---|---|
| 1–4 | 6 | 4 | 1 | 0 | 0 | 11 |
| 5–10 | 10 | 17 | 6 | 1 | 0 | 34 |
| 11–16 | 3 | 7 | 11 | 7 | 2 | 30 |
| 17–20 | 0 | 0 | 5 | 11 | 9 | 25 |

### DM Notes

- **Overstocking:** Include 25% more items than the table suggests. Assume players won't find everything.
- **Player Wish Lists:** Encourage players to keep a wish list of magic items. Pick from it when awarding items of appropriate rarity.
- **Treasure Themes:** Each hoard has a theme (Arcana / Armaments / Implements / Relics) that determines item types and monetary treasure.

---

## Adventure Structure

### DM Notes

*Source: DMG 2024, Chapter 4 — general adventure design guidance.*

**4 Steps:**
1. Lay Out the Premise — core conflict, villain, stakes
2. Draw in the Players — hooks tied to character motivations
3. Plan Encounters — each should advance a goal, frustrate progress, or reveal info
4. Bring It to an End — climactic encounter resolving the central conflict

**The One-Hour Guideline:** For every 1 hour of gameplay, plan ~3 "things" (encounters, explorations, social scenes). Low-difficulty combat = 1 thing; harder combats = 2.

**Encounter Priority:**
- **Definite** — Will almost certainly happen. Prep fully.
- **Possible** — Depends on player choices. Skim/outline.
- **Unlikely** — Probably won't happen. Brief notes only.

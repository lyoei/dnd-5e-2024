# D&D 5e 2024 Rules Knowledge Base

> ⚠️ **Disclaimer: Work-in-Progress Reference**
> 
> This is a community-maintained reference compiled from secondary sources (aidedd.org, wikidot, rpgbot.net, etc.), **not** a verbatim reproduction of the official 2024 Player's Handbook. Most files are marked `status: needs-source-check` — treat them as useful reference material, not authoritative RAW (Rules As Written). Always verify against the official PHB for final rulings.
> 
> **Source verification levels:**
> - `verified` — Cross-checked against official PHB text
> - `needs-source-check` — Compiled from secondary sources, not yet verified against PHB
> - `unverified` — Rough draft, may contain errors

A structured, searchable reference for **D&D 5th Edition 2024 Revised Rules**, covering the **PHB (Player's Handbook)** and **DMG (Dungeon Master's Guide)**. MM content planned for future expansion.

Built for AI DMs and players to query during sessions.

## Directory Structure

```
├── classes/          # Each class in its own file (features, subclasses, spell lists)
├── species/          # Playable species (formerly "races")
├── backgrounds/      # Backgrounds with feats and equipment
├── feats/            # Organized by category
│   ├── general/      # General feats
│   ├── origin/       # Origin feats (from backgrounds)
│   ├── fighting-style/
│   └── epic-boon/    # Level 19+ feats
├── spells/           # Organized by level
│   ├── cantrips/
│   ├── 1st-level/
│   └── ...
├── equipment/        # Weapons, armor, gear, tools
├── rules/            # Core mechanics
│   ├── combat/       # Action economy, conditions, etc.
│   ├── exploration/
│   ├── social/
│   ├── spellcasting/ # Spell preparation, concentration, components
│   ├── conditions/   # All conditions in one place
│   └── rest/         # Short/long rest rules
├── magic-items/      # Magic items by rarity
├── dmg/              # Dungeon Master's Guide reference
│   ├── running-the-game/  # DC table, damage, combat, advancement
│   ├── toolbox/           # Traps, poisons, hazards, chases, NPCs
│   ├── adventures/        # Encounter building, XP budgets
│   ├── treasure/          # Magic items, crafting, rarity/value
│   └── bastions/          # Bastion system (facilities, events)
├── templates/        # File templates for contributing
└── 2024-vs-2014.md   # Key changes from 2014 to 2024
```

## File Format

Every entry follows a consistent markdown template for easy parsing:

- **Classes**: Name, hit die, proficiencies, features by level, subclasses, spell list
- **Spells**: Name, level, school, casting time, range, components, duration, description, classes
- **Species**: Name, traits, size, speed, special abilities
- **Feats**: Name, category, prerequisite, description

See `templates/` for the exact format of each type.

## How to Use

### For AI Agents
- Fetch raw files via: `https://raw.githubusercontent.com/lyoei/dnd-5e-2024/main/<path>`
- Example: `https://raw.githubusercontent.com/lyoei/dnd-5e-2024/main/classes/fighter.md`
- Browse the directory structure to find what you need
- Use the `2024-vs-2014.md` file for quick rule change lookups

### For Humans
- Browse on GitHub like a wiki
- Use GitHub's search (press `/`) to find specific rules
- Submit issues for corrections or missing content

## Contributing

1. Use the templates in `templates/` for new entries
2. One file per class/spell/species/feat
3. Follow the naming convention: `kebab-case.md`
4. Cite page numbers from official sources where possible

## Status

🚧 Under construction — core classes and rules being added first.

### Status Matrix

| Section | Files | Status | Notes |
|---|---|---|---|
| PHB Classes | 12 | ✅ verified | Cross-checked against D&D Beyond PHB 2024. Supplement subclasses (College of the Moon, Knowledge Domain) tagged separately |
| PHB Spells | 386 | ⚠️ needs-source-check | Compiled from secondary sources, format standardized |
| PHB Species | 10 | ⚠️ needs-source-check | From secondary sources |
| PHB Feats | 75 | ⚠️ needs-source-check | From secondary sources |
| PHB Equipment | 5 | ⚠️ needs-source-check | From secondary sources |
| PHB Rules | 5 | ⚠️ needs-source-check | From secondary sources |
| DMG Encounter Building | 1 | 🟡 partially-verified | XP Budget table verified; social/exploration sections unverified |
| DMG Running the Game | 1 | 🟡 partially-verified | DC table, damage tables verified; some DM tips unverified |
| DMG Toolbox | 1 | ⚠️ needs-source-check | Traps, poisons, hazards — from secondary sources |
| DMG Treasure | 1 | ✅ verified | Magic item rules, crafting, rarity/value tables verified |
| DMG Bastions | 1 | ✅ verified | Complete system verified against D&D Beyond |
| Campaign Characters | 5 | ✅ active | Campaign-specific, not rules content |

**Verification levels:**
- `verified` — Cross-checked against official source (D&D Beyond)
- `partially-verified` — Some sections verified, some pending
- `needs-source-check` — Compiled from secondary sources, treat as reference only

### Audit

Run `python3 scripts/audit_kb.py` to check for:
- `verified` files containing `[NEEDS VERIFICATION]` tags
- XP budget table consistency across files
- Missing frontmatter fields
- Supplement content mixed into core tags
- Broken internal links

## Sources

Based on the **2024 Player's Handbook**, **Dungeon Master's Guide**, and **Monster Manual** by Wizards of the Coast. This is a reference tool, not a reproduction of copyrighted text. Entries are structured summaries for gameplay reference.

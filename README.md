# D&D 5e 2024 Rules Knowledge Base

> ⚠️ **Disclaimer: Work-in-Progress Reference**
> 
> This is a community-maintained reference compiled from secondary sources (aidedd.org, wikidot, rpgbot.net, etc.), **not** a verbatim reproduction of the official 2024 Player's Handbook. Most files are marked `status: needs-source-check` — treat them as useful reference material, not authoritative RAW (Rules As Written). Always verify against the official PHB for final rulings.
> 
> **Source verification levels:**
> - `verified` — Cross-checked against official PHB text
> - `needs-source-check` — Compiled from secondary sources, not yet verified against PHB
> - `unverified` — Rough draft, may contain errors

A structured, searchable reference for **D&D 5th Edition 2024 Revised Rules**, currently focused on the **PHB (Player's Handbook)**. DMG and MM directories are placeholders for future expansion.

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

## Sources

Based on the **2024 Player's Handbook**, **Dungeon Master's Guide**, and **Monster Manual** by Wizards of the Coast. This is a reference tool, not a reproduction of copyrighted text. Entries are structured summaries for gameplay reference.

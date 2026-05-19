---
type: campaign
version: dnd-5e-2024
status: active
tags: [campaign, characters, template]
updated: 2026-05-19
---

# Character Files

This directory holds player character files for the campaign.

## File Format

Each character should be a single Markdown file named `{character-name}.md` (lowercase, hyphens for spaces).

### Recommended Structure

```markdown
---
type: character
version: dnd-5e-2024
player: [Player Name]
status: active
tags: [character, {class}, {species}]
updated: YYYY-MM-DD
---

# [Character Name]

**Species:** [Species]  |  **Background:** [Background]  |  **Class:** [Class] [Level]
**Alignment:** [Alignment]  |  **Player:** [Player Name]

## Ability Scores

| STR | DEX | CON | INT | WIS | CHA |
|-----|-----|-----|-----|-----|-----|
| 10 (+0) | 10 (+0) | 10 (+0) | 10 (+0) | 10 (+0) | 10 (+0) |

## Core Stats

- **AC:** X  |  **HP:** X/X  |  **Speed:** 30 ft.
- **Proficiency Bonus:** +X
- **Initiative:** +X
- **Hit Dice:** XdX

## Features & Traits

- [List class features, species traits, background features]

## Equipment

- [Key equipment and magic items]

## Spells (if applicable)

### Prepared Spells
- [List prepared spells]

## Backstory

[Brief backstory]

## Notes

[Session-to-session notes, character development, goals]
```

## Templates

Character templates are available at `/tmp/dnd-5e-2024/templates/`:
- `class-template.md` — Class reference template
- `species-template.md` — Species reference template

## Naming Convention

- `aria-sunweaver.md` — Active character
- `aria-sunweaver.retired.md` — Retired/dead character
- Keep one file per character; update in place rather than creating versions

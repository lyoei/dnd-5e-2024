---
type: campaign
version: dnd-5e-2024
status: active
tags: [campaign, meta]
updated: 2026-05-19
---

# Campaign Directory

This directory holds **table-specific content** — everything unique to your game that isn't part of the general D&D 5e 2024 rules reference.

## Structure

```
campaign/
├── README.md              ← You are here
├── rulings.md             ← Table-specific rulings and house rules
├── characters/            ← Player character files
│   └── README.md          ← Character file format guide
├── sessions/              ← Session logs (create as needed)
└── notes/                 ← Campaign notes, NPCs, locations (create as needed)
```

## What Goes Here vs. the Rules Reference

| This directory (`campaign/`) | Rules reference (`rules/`, `classes/`, etc.) |
|------------------------------|-----------------------------------------------|
| Your table's house rules | RAW (Rules As Written) |
| Your PCs | Class/species templates |
| Session logs | General rules explanations |
| DM rulings for your game | Official rule clarifications |
| Campaign-specific notes | System-agnostic reference |

## Getting Started

1. Review and customize `rulings.md` with your table's decisions
2. Add character files to `characters/` (see `characters/README.md` for format)
3. Create `sessions/` when you start logging sessions

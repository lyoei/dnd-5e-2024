# Spell File Format Audit Report

> **⚠️ RESOLVED:** All issues identified in this audit were batch-fixed in commit `0d9445b` (2026-05-19). This file is retained for historical reference only.

**Date:** 2026-05-19
**Audited by:** Moco (subagent)
**Sample:** 1 file per spell level (10 files total)
**Canonical template:** `../templates/spell-template.md`

---

## Summary of Inconsistencies Found

### 1. Attribute Block Format (CRITICAL)

Two distinct formats are in use:

| Format | Used By | Example |
|--------|---------|---------|
| **Bullet list** (canonical ✅) | Cantrips, 1st–7th level | `- **Casting Time:** Action` |
| **Bold key-value** (non-standard ❌) | 8th, 9th level | `**Casting Time:** Action` (no bullet, no dash) |

**Files affected:** All 8th-level and 9th-level spell files likely use the non-standard format.

### 2. School Name Casing in Frontmatter

| Style | Used By |
|-------|---------|
| `school: evocation` (lowercase, canonical ✅) | Cantrips, 1st level |
| `school: Abjuration` (capitalized ❌) | 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th level |

**Impact:** Breaks consistent tag-based filtering. All `school` values in frontmatter should be lowercase.

### 3. Concentration/Ritual Value Casing

| Style | Used By |
|-------|---------|
| `Yes` / `No` (canonical ✅) | Most levels |
| `yes` / `no` (lowercase ❌) | 4th level (arcane-eye.md) |

**Impact:** Minor, but inconsistent for programmatic parsing.

### 4. Spell Lists Section Format (CRITICAL — 5+ variants)

This is the most inconsistent section across the corpus:

| Variant | Example | Used By |
|---------|---------|---------|
| Plain comma-separated (canonical ✅) | `Sorcerer, Wizard` | Cantrips, 4th, 5th, 6th, 7th |
| Sub-bullets with Classes + Categories | `- **Classes:** ...\n- **Categories:** Arcane, Primal` | 1st level |
| Sub-bullets with Classes + Spell Lists | `- **Classes:** ...\n- **Spell Lists:** Divine, Primal` | 2nd level |
| Bullet list with category parenthetical | `- Arcane (Wizard)\n- Divine (Cleric)` | 3rd, 8th level |
| Mixed bullets (some with category, some without) | `- Arcane (Wizard)\n- Bard\n- Warlock` | 9th level |

**Canonical format:** Plain comma-separated class names on one line. No categories, no sub-bullets.

### 5. Subtitle Line Format

| Style | Example | Used By |
|-------|---------|---------|
| `*Cantrip, School*` | `*Cantrip, Evocation*` | Cantrips ✅ |
| `*Xth-level School*` (lowercase "level") | `*1st-level Abjuration*` | 1st level ✅ |
| `*Xth-Level School*` (uppercase "Level") | `*2nd-Level Abjuration*` | 2nd, 3rd, 4th level ❌ |
| `*Xth-level School*` (lowercase "level") | `*5th-level Transmutation*` | 5th, 6th, 7th level ✅ |

**Canonical format:** `*Xth-Level School*` — capitalize both "Level" and School name in the subtitle.

### 6. Tags Casing

| Style | Example | Used By |
|-------|---------|---------|
| All lowercase (canonical ✅) | `[spell, 5th-level, transmutation, ...]` | Most files |
| Mixed case ❌ | `[spell, 5th-level, Transmutation, ...]` | 5th level (animate-objects.md) |

### 7. "At Higher Levels" — No-Scaling Phrasing

| Phrasing | Used By |
|----------|---------|
| `None.` (canonical ✅) | — |
| `None specified.` ❌ | 4th level |
| `Not applicable.` ❌ | 8th, 9th level |
| `No additional effect at higher levels.` ❌ | 7th level |

**Canonical:** Use `None.` — short, consistent, parseable.

### 8. 2024 Changes Format

| Style | Used By |
|-------|---------|
| Plain prose (canonical for 1-2 changes ✅) | Most files |
| Bullet list (canonical for 3+ changes ✅) | 8th, 9th level |
| Italic wrapping ❌ | 1st level (`*Needs verification...*`) |

---

## Estimated Scope of Fixes

| Level | Est. Files | Likely Issues |
|-------|-----------|---------------|
| Cantrips | ~33 | Minor (subtitle may vary) |
| 1st level | ~50 | Spell Lists format (Classes + Categories) |
| 2nd level | ~35 | School casing, Spell Lists format, subtitle casing |
| 3rd level | ~30 | School casing, Spell Lists format (category parenthetical), subtitle casing |
| 4th level | ~25 | School casing, Concentration casing, subtitle casing, At Higher Levels phrasing |
| 5th level | ~25 | School casing, tags casing |
| 6th level | ~20 | School casing |
| 7th level | ~15 | School casing, At Higher Levels phrasing |
| 8th level | ~15 | **Attribute block format**, School casing, Spell Lists format, At Higher Levels phrasing |
| 9th level | ~15 | **Attribute block format**, School casing, Spell Lists format, At Higher Levels phrasing |

**Priority for batch fixing:**
1. 🔴 8th + 9th level — attribute block format is structurally wrong
2. 🟠 All levels — frontmatter `school` casing normalization (scriptable)
3. 🟡 1st–3rd level — Spell Lists section restructuring
4. 🟢 Minor — subtitle casing, At Higher Levels phrasing, tags casing

---

## Canonical Format Quick Reference

```yaml
# Frontmatter
school: lowercase-always
level: cantrip | integer

# Subtitle
Cantrip: *Cantrip, School*
Leveled: *Xth-Level School*

# Attributes: bullet list, 6 items, this order
- **Casting Time:**
- **Range:**
- **Components:**
- **Duration:**
- **Concentration:** Yes | No
- **Ritual:** Yes | No

# Sections in order
## Description
## At Higher Levels        # "None." if N/A
## Spell Lists             # Comma-separated class names, one line
## 2024 Changes            # Prose or bullet list
```

See `templates/spell-template.md` for the full canonical template with inline documentation.

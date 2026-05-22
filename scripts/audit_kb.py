#!/usr/bin/env python3
"""
audit_kb.py — Lint script for dnd-5e-2024 knowledge base

Checks:
1. status: verified files should not contain [NEEDS VERIFICATION]
2. XP budget tables across files should be consistent
3. Frontmatter must have source, status, updated fields
4. Supplement content should not be in PHB core tags
5. Broken internal markdown links
"""

import os
import re
import sys
import yaml
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Files that legitimately don't need frontmatter
NO_FRONTMATTER_ALLOWLIST = {
    "README.md",
    "2024-vs-2014.md",
    "templates/class-template.md",
    "templates/feat-template.md",
    "templates/species-template.md",
    "templates/spell-template.md",
    "spells/FORMAT-AUDIT.md",
}

errors = []
warnings = []


def get_status(fm: dict) -> str:
    """Get status from top-level or nested verification.status."""
    if "status" in fm:
        return fm["status"]
    if isinstance(fm.get("verification"), dict):
        return fm["verification"].get("status", "")
    return ""


def load_frontmatter(path: Path):
    """Extract YAML frontmatter from a markdown file."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return None, text
    try:
        fm = yaml.safe_load(m.group(1))
        return fm, text
    except yaml.YAMLError:
        errors.append(f"YAML parse error: {path}")
        return None, text


def check_verified_vs_needs_verification(path: Path, fm: dict, text: str):
    """Check 1: verified status should not coexist with NEEDS VERIFICATION."""
    status = get_status(fm)
    if status == "verified" and "[NEEDS VERIFICATION" in text:
        lines = []
        for i, line in enumerate(text.split("\n"), 1):
            if "[NEEDS VERIFICATION" in line:
                lines.append(i)
        errors.append(
            f"CRITICAL: {path.relative_to(REPO_ROOT)} has status: verified "
            f"but contains [NEEDS VERIFICATION] at lines {lines}"
        )


def check_frontmatter_fields(path: Path, fm: dict):
    """Check 3: Required frontmatter fields (skip campaign files)."""
    if "campaign" in str(path.relative_to(REPO_ROOT)):
        return  # Campaign files don't need source
    required = ["source", "updated"]
    missing = [f for f in required if f not in fm]
    # status can be top-level or under verification
    has_status = "status" in fm or (
        isinstance(fm.get("verification"), dict) and "status" in fm["verification"]
    )
    if not has_status:
        missing.append("status")
    if missing:
        warnings.append(
            f"{path.relative_to(REPO_ROOT)}: missing frontmatter fields: {missing}"
        )


def check_supplement_tags(path: Path, fm: dict):
    """Check 4: Supplement subclasses should not be in main tags."""
    tags = fm.get("tags", [])
    supplement = fm.get("supplement-subclasses", [])
    overlap = set(tags) & set(supplement) if supplement else set()
    if overlap:
        errors.append(
            f"{path.relative_to(REPO_ROOT)}: supplement subclasses {overlap} "
            f"found in main tags — should only be in supplement-subclasses"
        )


def extract_xp_table(text: str) -> dict:
    """Extract per-character XP budget values from a markdown table.
    Only picks the first table with header matching Low/Moderate/High."""
    table = {}
    in_xp_section = False
    # Look for the per-character table (not party-of-4 summary)
    for line in text.split("\n"):
        if "Low" in line and "Moderate" in line and "High" in line:
            # Skip party-of-4 summary tables (fewer rows)
            in_xp_section = True
            continue
        if in_xp_section:
            m = re.match(
                r"\|\s*(\d+)\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|",
                line,
            )
            if m:
                level = int(m.group(1))
                if 1 <= level <= 20:
                    table[level] = (
                        m.group(2).replace(",", ""),
                        m.group(3).replace(",", ""),
                        m.group(4).replace(",", ""),
                    )
            elif line.strip() and not line.startswith("|"):
                # End of table
                if len(table) >= 15:  # Only accept full 20-level tables
                    break
                table = {}
                in_xp_section = False
    return table if len(table) >= 15 else {}


def check_xp_consistency():
    """Check 2: XP budget tables should be consistent across files."""
    xp_files = [
        REPO_ROOT / "dmg" / "adventures" / "encounter-building.md",
        REPO_ROOT / "dmg" / "running-the-game" / "rules-reference.md",
    ]
    tables = {}
    for f in xp_files:
        if f.exists():
            text = f.read_text(encoding="utf-8")
            t = extract_xp_table(text)
            if t:
                tables[str(f.relative_to(REPO_ROOT))] = t

    if len(tables) < 2:
        return

    files = list(tables.keys())
    ref_file = files[0]
    ref_table = tables[ref_file]

    for other_file in files[1:]:
        other_table = tables[other_file]
        for level in ref_table:
            if level in other_table and ref_table[level] != other_table[level]:
                errors.append(
                    f"XP CONFLICT at level {level}: "
                    f"{ref_file}={ref_table[level]} vs "
                    f"{other_file}={other_table[level]}"
                )


def check_residual_frontmatter(path: Path, text: str):
    """Check 6: Detect residual YAML delimiters after frontmatter."""
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return
    after_fm = text[m.end():m.end() + 300]
    lines_after = after_fm.split("\n")
    # Only check the first 3 non-empty lines after frontmatter
    non_empty_count = 0
    for i, line in enumerate(lines_after):
        stripped = line.strip()
        if not stripped:
            continue
        non_empty_count += 1
        if non_empty_count > 3:
            break
        # A standalone --- right after frontmatter (before any heading) is suspicious
        if stripped == "---" and non_empty_count <= 2:
            # But only if the next non-empty line looks like YAML, not markdown
            remaining = [l.strip() for l in lines_after[i+1:] if l.strip()]
            if remaining and re.match(r"^(updated|status|source|type|version):\s", remaining[0]):
                errors.append(
                    f"{path.relative_to(REPO_ROOT)}: residual YAML delimiter '---' "
                    f"with YAML-like content after frontmatter"
                )
        elif re.match(r"^(updated|status|source|type|version):\s", stripped) and non_empty_count <= 2:
            warnings.append(
                f"{path.relative_to(REPO_ROOT)}: possible residual YAML field '{stripped}' "
                f"found after frontmatter"
            )


def check_internal_links(path: Path, text: str):
    """Check 5: Internal markdown links."""
    links = re.findall(r"\[.*?\]\(([^)]+)\)", text)
    for link in links:
        if link.startswith("http") or link.startswith("#"):
            continue
        target = (path.parent / link.split("#")[0]).resolve()
        if not target.exists():
            warnings.append(
                f"{path.relative_to(REPO_ROOT)}: broken link → {link}"
            )


def main():
    md_files = list(REPO_ROOT.rglob("*.md"))
    md_files = [f for f in md_files if ".git" not in str(f)]

    stats = {"total": 0, "verified": 0, "partial": 0, "needs_check": 0, "no_fm": 0}

    for path in sorted(md_files):
        fm, text = load_frontmatter(path)
        stats["total"] += 1

        if fm is None:
            rel = str(path.relative_to(REPO_ROOT))
            if rel not in NO_FRONTMATTER_ALLOWLIST:
                warnings.append(f"{rel}: no YAML frontmatter (add to allowlist if intentional)")
            stats["no_fm"] += 1
            continue

        status = get_status(fm)
        if status == "verified":
            stats["verified"] += 1
        elif status == "partially-verified":
            stats["partial"] += 1
        elif status == "needs-source-check":
            stats["needs_check"] += 1

        check_verified_vs_needs_verification(path, fm, text)
        check_frontmatter_fields(path, fm)
        check_supplement_tags(path, fm)
        check_residual_frontmatter(path, text)
        check_internal_links(path, text)

    check_xp_consistency()

    # Report
    print("=" * 60)
    print("D&D 5E 2024 Knowledge Base Audit")
    print("=" * 60)
    print(f"\nFiles scanned: {stats['total']}")
    print(f"  verified:            {stats['verified']}")
    print(f"  partially-verified:  {stats['partial']}")
    print(f"  needs-source-check:  {stats['needs_check']}")
    print(f"  no frontmatter:      {stats['no_fm']}")

    if errors:
        print(f"\n❌ ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  • {e}")

    if warnings:
        print(f"\n⚠️  WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  • {w}")

    if not errors and not warnings:
        print("\n✅ All checks passed!")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

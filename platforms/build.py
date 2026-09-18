#!/usr/bin/env python3
"""Generate playbook stubs for platforms that don't have one yet.

platforms.csv is the seed registry. Playbooks are living documents: agents
fill in verified details during submissions, so this script never overwrites
an existing playbook unless --force is passed.

Usage:
    python3 platforms/build.py            # create missing playbook stubs
    python3 platforms/build.py --check    # validate CSV + tracker data
    python3 platforms/build.py --force    # regenerate ALL stubs (destroys edits)
"""
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "platforms" / "platforms.csv"
PLAYBOOK_DIR = ROOT / "platforms" / "playbooks"
TRACKER_DATA = ROOT / "tracker" / "data.json"

TEMPLATE = """# {name}

| | |
|---|---|
| Site | {url} |
| Category | {category} |
| Product page pattern | {pattern} |
| Cost | UNVERIFIED — check for paid tiers before submitting; pause before any payment |
| Account required | UNVERIFIED |
| Listing status flow | UNVERIFIED |

## Preparation
- [ ] Product brief fields ready: name, tagline, description, category, links, logo, screenshots
- [ ] Account exists — create one only with explicit user approval
- [ ] Free vs. paid submission path identified on-site

## Submission steps
Steps below are a generic skeleton. Verify each one on the live site and
correct this file when reality differs — that is how this playbook improves.

1. Find the submission entry point ("Submit", "Add product", "List your tool",
   or a pricing/submit page).
2. Fill every listing field from the product brief — approved claims only.
3. Check the hurdles section, then submit.
4. Record the outcome in `tracker/data.json` with evidence.

## Known hurdles
UNVERIFIED — nothing recorded yet. As observed, record: CAPTCHAs, email
verification, moderation queues, paid-only placement, badge requirements,
dofollow policy, review turnaround time.

## Confirmation
UNVERIFIED — expected confirmation signal (email, dashboard entry, public
URL) not yet recorded. A listing counts as `live` only when its public URL
loads with the product visible.

## Badge
{badge}
{notes}
"""


def load_platforms():
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def badge_text(kind):
    return {
        "img": "Platform provides an embeddable badge. Record the snippet in this file after the listing is live.",
        "img-remote": "Platform serves a hosted badge image. Record the embed URL here after the listing is live.",
        "text": "Platform links are plain text — no badge asset observed.",
    }.get(kind, "UNVERIFIED")


def render(row):
    pattern = row["product_url_pattern"].strip()
    notes = row["notes"].strip()
    return TEMPLATE.format(
        name=row["name"],
        url=row["url"],
        category=row["category"],
        pattern=f"`{pattern}`" if pattern else "UNVERIFIED",
        badge=badge_text(row["badge"]),
        notes=f"\n## Notes\n{notes}\n" if notes else "",
    )


def check():
    rows = load_platforms()
    slugs = [r["slug"] for r in rows]
    assert len(slugs) == len(set(slugs)), "duplicate slugs in platforms.csv"
    for r in rows:
        for field in ("slug", "name", "url", "category"):
            assert r[field].strip(), f"{r['slug'] or 'row'}: empty {field}"
    json.loads(TRACKER_DATA.read_text(encoding="utf-8"))
    missing = [s for s in slugs if not (PLAYBOOK_DIR / f"{s}.md").exists()]
    print(f"platforms: {len(rows)} | playbooks missing: {len(missing)} | tracker: OK")
    return 0


def main():
    if "--check" in sys.argv:
        sys.exit(check())
    force = "--force" in sys.argv
    if force:
        print("WARNING: --force overwrites agent-verified playbook edits.")
    PLAYBOOK_DIR.mkdir(parents=True, exist_ok=True)
    created = skipped = 0
    for row in load_platforms():
        path = PLAYBOOK_DIR / f"{row['slug']}.md"
        if path.exists() and not force:
            skipped += 1
            continue
        path.write_text(render(row), encoding="utf-8")
        created += 1
    print(f"created {created}, kept {skipped} existing")


if __name__ == "__main__":
    main()

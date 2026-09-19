# Startup Fame

| | |
|---|---|
| Site | https://startupfa.me |
| Category | saas-directory |
| Product page pattern | `https://startupfa.me/s/{slug}` |
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
Platform provides an embeddable badge. Record the snippet in this file after the listing is live.


## Verified recon — 2026-09-19 (BrowserOS)

- JS-rendered homepage arrived empty; footer nav shows Startups / Locations / Founders / Pricing / Guides / Submit; contact hello@startupfa.me. Assess submit flow in-session.

### Signup/submit — observed 2026-09-19 (BrowserOS, field-level)

- "Submit your startup" → **`/login`** ("create a free account"). Also runs paid "Submitator" (100+ directories service) — distinguish from organic submit.

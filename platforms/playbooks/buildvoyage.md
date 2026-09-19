# BuildVoyage

| | |
|---|---|
| Site | https://buildvoyage.com |
| Category | saas-directory |
| Product page pattern | UNVERIFIED |
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
UNVERIFIED

## Notes
curated micro-SaaS directory


## Verified recon — 2026-09-19 (BrowserOS)

- Curated micro-SaaS directory (495 products) with maker profiles, tech-stack metadata, "cheers" voting; Productivity category (68) — app fits.
- Submit product + Sign in; "Apply to be featured" = curated review, not instant listing; sponsor slots.

### Submit — observed 2026-09-19 (BrowserOS, field-level)

- `/submit` = **full public Laravel form**: name*, tagline*, description (rich editor), site_url*, submitter_email*, category_id*, pricing_note, tech-stack tag fields (frameworks/languages/DBs/infra/APIs/payments/AI), Cloudflare Turnstile, weekly-roundup opt-in checkbox, accept_terms*. Free — strong agent path.

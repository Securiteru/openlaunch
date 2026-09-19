# TheSaaSDir

| | |
|---|---|
| Site | https://thesaasdir.com |
| Category | saas-directory |
| Product page pattern | `https://thesaasdir.com/product/{slug}` |
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

- **Explicit free tier: "Submit Free"** + paid options (Featured $19, Multiple Listings $29) shown on homepage.
- **Health + Mobile categories** — app fits; Submit Product in nav; no login wall visible on landing.

### Submit form — observed 2026-09-19 (BrowserOS, field-level)

- **`/submit/` is a full PUBLIC form — no account needed.** Django (csrfmiddlewaretoken). Fields: `website_url`*, `name`*, `tagline`*, `description`* (features + audience), `screenshot` file, category checkboxes. Buttons: **"Auto-fill"** (URL scrape), "Verify Badge", "Submit Product".
- Tier params: `?tier=free` (Submit Free) / `?tier=paid` (Featured $19) / `?tier=dual` ($29). "Verify Badge" button suggests backlink-badge verification for free tier.

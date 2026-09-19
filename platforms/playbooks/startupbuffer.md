# Startup Buffer

| | |
|---|---|
| Site | https://startupbuffer.com |
| Category | launch |
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


## Verified recon — 2026-09-19 (BrowserOS)

- **Cloudflare security verification wall** on homepage — needs interactive/human pass before assessing submit flow.

### Submit form — observed 2026-09-19 (BrowserOS, field-level)

- **`/site/submit` is a full PUBLIC multi-step form — no account.** Fields: name*, url*, email*, pitch*, description*, screenshot upload, country/city selects, primary_category, tags, video/linkedin/twitter/facebook URLs. "Continue"/"Submit Now 🚀". Auto-saves draft (hidden draft_id).

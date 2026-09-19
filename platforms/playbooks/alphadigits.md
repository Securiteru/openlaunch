# AlphaDigits

| | |
|---|---|
| Site | https://alphadigits.com |
| Category | review |
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
mobile app reviews


## Verified recon — 2026-09-19 (BrowserOS)

- **Cloudflare browser-check wall** — homepage returned "Checking your browser" challenge. Could not inspect submission flow in this session.
- Retry in a fully interactive browser session (or have the user open it once to clear the challenge) before planning submission.
- Historically: paid app-review site for iOS/Android — expect paid review tiers.

### Submit — observed 2026-09-19 (BrowserOS, field-level)

- `/submit-app-for-review/` = **public WP Formidable form**: ~7 item_meta fields (name/email/desc/etc.) + Submit. App-review site — likely paid review behind the form.

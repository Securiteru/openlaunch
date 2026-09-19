# publishyoursaas

| | |
|---|---|
| Site | https://publishyoursaas.com |
| Category | saas-directory |
| Product page pattern | `https://publishyoursaas.com/listing/{slug}` |
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

- Permanent dedicated listing pages; SUBMIT YOUR SAAS + SIGN IN; Pricing; weekly "boosts" gamify ranking (reset Monday 00:00 UTC); paid sidebar spots $29.99.
- Claims 238k visits/30d (Cloudflare-measured); **accepts App Store links** (SocialRouter listed via apps.apple.com) — app fits.
- Currently 40%-off promo banner on paid plans.

### Signup/submit form — observed 2026-09-19 (BrowserOS, field-level)

- "Submit your SaaS" → **`/signin`** — Email + Password + **Google + GitHub + LinkedIn OAuth**.

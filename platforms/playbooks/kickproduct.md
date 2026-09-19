# Kick Product

| | |
|---|---|
| Site | https://kickproduct.com |
| Category | launch |
| Product page pattern | `https://kickproduct.com/products/{id}` |
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

## Notes
product URL contains an opaque id


## Verified recon — 2026-09-19 (BrowserOS)

- **"It's Free Forever"** — free tier explicitly confirmed; Sign In / Get Started.
- SaaS-positioned ("Launch Your SaaS Product in Minutes, No Fake Queues"); Product of the Week + community/founders sections + launch analytics.
- Operator: Brainer Code Digital Solutions.

### Signup — observed 2026-09-19 (BrowserOS, field-level)

- "Get Started" → `/auth/signup`: **Continue with Google** button only (Google OAuth) + a CAPTCHA element present. "It's Free Forever" tier advertised. Sign In at `/auth/signin`.

# SaaSFame

| | |
|---|---|
| Site | https://saasfame.com |
| Category | saas-directory |
| Product page pattern | `https://saasfame.com/item/{slug}` |
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
Platform serves a hosted badge image. Record the embed URL here after the listing is live.


## Verified recon — 2026-09-19 (BrowserOS)

- "SaaS Hall of Fame" directory; DR 70; **honest daily traffic chart ~16k–23k visitors/day** — one of the busiest directories recon'd.
- **Health, Mobile, and iOS category/tag support** — app fits; Submit + Sign In + Pricing.

### Signup/submit form — observed 2026-09-19

- `GET /submit` → **redirects to `/auth/login?callbackUrl=/submit`** — account required.
- Login form: **Email + Password** + **Cloudflare Turnstile** + OAuth buttons **Google, GitHub**; "Don't have an account? Sign up" link → register flow (same shape expected).
- Human gates: Turnstile + email verification.

# Startup Fast

| | |
|---|---|
| Site | https://startupfa.st |
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
Platform links are plain text — no badge asset observed.


## Verified recon — 2026-09-19 (BrowserOS)

- **"Powered by Open-Launch"** (same white-label engine as NextLaunch — expect same submit flow/fields).
- Daily/Weekly/Monthly leaderboards + Yesterday's Champion; Submit Product + Sign in/up; Premium promotion + sponsors; founders' Discord community.
- Startup/leaderboard model: makers get ranked profiles too.

### Signup/submit form — observed 2026-09-19 (BrowserOS, field-level)

- `/submit` reachable but logged-out render shows only FAQ accordion (no fields) — submit gated behind `/sign-in` or `/sign-up`.
- Part of Open-Launch family ("Powered by Open Launch"); auth likely identical email/pass + Google/GitHub + Turnstile.

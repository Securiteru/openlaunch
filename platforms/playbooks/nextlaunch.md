# Next Launch

| | |
|---|---|
| Site | https://nextlaunch.io |
| Category | launch |
| Product page pattern | `https://nextlaunch.io/projects/{slug}` |
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

- Daily launch leaderboard (Today/Yesterday/Month's Best) with upvotes + comments; categories: SaaS (254), Productivity (127), AI, DevTools, Design.
- Sign in/Sign up + Submit Project; Pricing + Sponsors pages; pitch = badge + backlink.
- Footer: **"Powered by Open Launch"** — runs on the open-launch.com white-label engine (same as several clones; expect identical submit flow across them).

### Signup/submit form — observed 2026-09-19 (BrowserOS, field-level)

- `/projects/submit` → `/sign-in?redirect=/projects/submit` — **Open-Launch-family template** confirmed at form level.

# LaunchVault

| | |
|---|---|
| Site | https://www.launchvault.dev |
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
Platform provides an embeddable badge. Record the snippet in this file after the listing is live.


## Verified recon — 2026-09-19 (BrowserOS)

- Daily launch leaderboard (Today / Yesterday / Month's Best) with upvotes; categories incl. SaaS, Artificial Intelligence, Finance & FinTech.
- Submit Project + Sign in/Sign up; Pricing page + sponsor slots exist — free tier probable, verify.
- Also runs "Alternative To" pages and a Traffic Checker tool — SEO-oriented directory.

### Signup/submit form — observed 2026-09-19 (BrowserOS, field-level)

- `/projects/submit` → `/sign-in?redirect=/projects/submit` — **Open-Launch-family template** (email+pass, Turnstile, Google/GitHub).

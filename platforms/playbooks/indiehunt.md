# IndieHunt

| | |
|---|---|
| Site | https://indiehunt.io |
| Category | launch |
| Product page pattern | `https://indiehunt.io/project/{slug}` |
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


## Field observations
Source: LaunchRepo public field guide (https://launchrepo.dev/directories/indiehunt/), observed unknown.

IndieHunt calls itself a weekly launch platform for AI tools, indie SaaS and bootstrapped products. Products go live on a Monday at 8:00 AM UTC and compete for seven days on community upvotes; the weekly top three get Hall of Fame badges.

Checked on September 17, 2026 on the platform’s public pages.

### Who lists here

Makers of AI tools and small SaaS products who want a scheduled launch week rather than a permanent catalog entry — the site explicitly says it is a competition, not a general app store.

### What to prepare

A sign-in with email, Google or GitHub.
Project details, website URL and categories, plus an open Monday launch week to pick.
A tier choice: free slots are limited (the page mentions 15 per week) and require the IndieHunt badge; a paid tier shown at $19 removes the badge requirement and adds promotion.

### What “live” means here

Live means your product is on the homepage for the chosen week with a working upvote count. Before that Monday it is scheduled; after the week it drops off the front page, so save the permanent product URL while it is up.

### Worth knowing

The submission page mentions completing verification or payment before a slot is confirmed — do not record the week as booked until that step is acknowledged in your account.
Official site: IndieHunt ↗All product launch platforms →
Short profile from the platform’s public pages, not a submission service. Rules, prices and requirements change — recheck before you submit. LaunchRepo makes no publication, backlink or ranking promise.

###

Submission entry: https://indiehunt.io/

## Verified recon — 2026-09-19 (BrowserOS)

- **Same operator/template as EarlyHunt** ("Launch in a week", identical nav, shared alternatives pages covering our whole registry: uneed, fazier, tinylaunch, microlaunch, startupbase, launchigniter, peerlist, firsto, saashub, earlyhunt, openhunts).
- Weekly cohorts; **Health & Fitness category** present; Bids + Premium paid options; Sign in + Submit.
- Useful: their "Alternative: X" pages describe competing platforms — source of playbook intel.

### Signup/submit form — observed 2026-09-19 (BrowserOS, field-level)

- `/submit` → **`/auth/signin`** — account required.
- Auth identical to EarlyHunt: **email magic-link + Google + GitHub**; no CAPTCHA. Same operator/template confirmed at form level.

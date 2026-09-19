# ComingUp

| | |
|---|---|
| Site | https://comingup.io |
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

## Notes
launchrepo profile


## Field observations
Source: LaunchRepo public field guide (https://launchrepo.dev/directories/comingup/), observed unknown.

ComingUp is a daily launch board. The homepage shows “Top Products Launching Today” with category, tags, comment and vote counters, a day-by-day archive and collections; on the day this was checked it listed 70 products launching in one day.

Checked on September 17, 2026 on the platform’s public pages.

### Who lists here

Founders who want a dated launch entry with a permanent product page and are comfortable with a high-volume board, where dozens of products share the same day.

### What to prepare

An account — /submit redirects to login, with email sign-in or “Continue with SideProjectors”, the sister marketplace whose help pages describe cross-posting to ComingUp.
Name, tagline, category and a handful of tags, which is what every card on the day view displays.
A launch day: products are grouped under a date, so the entry is tied to the day it goes out rather than to an ongoing catalog position.

### What “live” means here

Live means your product resolves under /p/<slug>/ and shows on the day view for its date with a vote counter. Before that date it is scheduled; afterwards it stays reachable through the day archive.

### Worth knowing

No pricing, about or FAQ page was reachable on the public site when checked, so paid options, if any, are only visible after login — note “not published” rather than assuming the launch is free. The product cards link out with a utm_source=comingup.io parameter.
Official site: ComingUp ↗All product launch platforms →
Short profile from the platform’s public pages, not a submission service. Rules, prices and requirements change — recheck before you submit. LaunchRepo makes no publication, backlink or ranking promise.

###

Submission entry: https://www.comingup.io/

## Verified recon — 2026-09-19 (BrowserOS)

- Daily leaderboard model — "Top Products Launching Today" (~74 products/day observed), Yesterday/Today views.
- Nav has Submit, Login, Sign Up — account required.
- Categories include **Health & Fitness** (a health app was listed today) — app fits.
- Products show logo + name + tagline + category + tags + upvote count; "Visit website" outbound links.
- `/submit` returned only an ad iframe in snapshot — the real form may load lazily or require login first. Verify by clicking nav "Submit" while signed in.

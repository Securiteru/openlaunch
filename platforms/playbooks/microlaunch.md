# MicroLaunch

| | |
|---|---|
| Site | https://microlaunch.net |
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
dofollow; freemium (backlinkbot)


## Field observations
Source: LaunchRepo public field guide (https://launchrepo.dev/directories/microlaunch/), observed unknown.

Microlaunch, run by Stimpack SAS in Paris, is a launch platform with weekly and monthly leaderboards, a deals marketplace and product pages under /p/. The site says a launch campaign runs for 30 days instead of a single day; the leaderboard shows a countdown to the end of the month and rates each product separately on idea and on product.

Checked on September 17, 2026 on the platform’s public pages.

### Who lists here

Indie makers and small startups that want feedback and a listing which keeps working after launch day. Products are filed under categories such as AI & Assistants, Dev Tools or Analytics & Data, and can also publish a discount in the deals section.

### What to prepare

An account and a full product page: name, tagline, category, pricing type, a longer description and a link.
A decision on the tier: the FAQ describes a free regular launch with a two-to-three-month-plus queue, unverified status and no-follow links, against a Pro launch listed at $49, sold at $39 with a code on the day we checked and capped at 40 spots a month.
Something to ask the community for — pages collect votes, idea and product ratings, written feedback and “roasts”, and the FAQ encourages makers to promote the launch themselves as well.

### What “live” means here

Your product has a public /p/ page that collects votes, ratings and feedback, and its leaderboard entry carries a Live tag while it sits in the month’s ranking for its 30-day window. A submitted product without a slot is still waiting in the queue.

### Worth knowing

The Premium page claims a verified badge, Product of the Day placement and DR60+ do-follow backlinks for Pro launches, while the same FAQ describes free launches as no-follow — treat both as the platform’s own marketing and check your own page. Re-launches are allowed, the site says, for major feature releases only.
Official site: Microlaunch ↗All product launch platforms →
Short profile from the platform’s public pages, not a submission service. Rules, prices and requirements change — recheck before you submit. LaunchRepo makes no publication, backlink or ranking promise.

###

Submission entry: https://microlaunch.net/

## Verified recon — 2026-09-19 (BrowserOS)

- `/submit` redirects to `/premium#pricing` — **submission is account-gated**. "New Launch" button sits in the top nav behind the Signup dropdown.
- Free "Regular" launch exists alongside paid "Pro Launch" and paid services (product review/action plan).
- Monthly cohort launch model with leaderboard (Business vs Consumer tabs), upvotes, and feedback roasts. app fits the Consumer tab; category "Mobile App" exists.
- Signup is a nav dropdown/modal — did not render in headless snapshot; verify auth providers in a real session.
- Community/contributor program exists (launch feedback exchange) — expect "contribute to be featured" dynamics.

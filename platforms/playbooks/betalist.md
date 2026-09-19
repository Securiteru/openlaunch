# BetaList

| | |
|---|---|
| Site | https://betalist.com |
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
free queue is slow; paid skips (backlinkbot)


## Field observations
Source: LaunchRepo public field guide (https://launchrepo.dev/directories/betalist/), observed unknown.

BetaList is a discovery site that calls itself the place for early adopters to discover upcoming and recently launched internet startups. The homepage is a dated timeline with a handful of startups per day. Its support page says all submissions are paid, there is no free option, and plans differ mainly in how quickly you are featured and whether a newsletter slot comes with the plan.

Checked on September 17, 2026 on the platform’s public pages.

### Who lists here

Pre-launch or just-launched technology startups with their own domain. The criteria page rules out blogs, newsletters, courses, subscription e-commerce, agencies, plain templates, free hosting subdomains such as vercel.app or netlify.app, and direct app store or crowdfunding links.

### What to prepare

A landing page with a distinct design and real product information, where a visitor can sign up, download or log in.
An account and a payment: plans and prices appear only at the end of the signed-in submission form, and BetaList says a startup that is not selected is refunded in full automatically.
Name, a one-line pitch and your launch state — the criteria page allows two features per startup, once pre-launch and once at launch, a few weeks apart.

### What “live” means here

The editorial team accepted the submission and your startup has its own page under /startups/ on the day’s timeline. A newsletter slot comes only with some plans and follows at least 24 hours after featuring; a paid submission on its own is not a listing.

### Worth knowing

The refund covers rejection only: the FAQ says that once a startup has been featured, refunds are not available. The same FAQ states that the “Visit Site” button is a do-follow link routed through a 301 redirect with a ref parameter — that is the platform’s own claim, so check the link on your live page. Homepage Boost slots cost $99 a week on top and only work once you are featured.
Official site: BetaList ↗All product launch platforms →
Short profile from the platform’s public pages, not a submission service. Rules, prices and requirements change — recheck before you submit. LaunchRepo makes no publication, backlink or ranking promise.

###

Submission entry: https://betalist.com/

## Verified recon — 2026-09-19 (BrowserOS)

- `/submit` redirects to `/sign_in` — account required before any form.
- Auth options observed: **Sign in with X (Twitter OAuth)**, email+password, or magic link; separate "Sign up" link.
- Prior field-guide observation confirmed by behavior: no free submission tier on the public path — treat as `paid-blocked` under zero-spend unless the user approves.

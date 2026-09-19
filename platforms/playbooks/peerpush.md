# PeerPush

| | |
|---|---|
| Site | https://peerpush.net |
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
account required (favors.dev atlas)


## Field observations
Source: LaunchRepo public field guide (https://launchrepo.dev/directories/peerpush/), observed unknown.

PeerPush is a product discovery board that publishes every product as a structured page for people and for AI assistants; the site says that data is read through an MCP server, a public API and search engines. Products compete for Product of the Day, Week and Month, decided at midnight UTC, and the feed ranks on engagement, ratings, freshness and PeerPush points rather than ad spend.

Checked on September 17, 2026 on the platform’s public pages.

### Who lists here

Founders who will stick around: points come from upvoting, commenting, following, rating and visiting other people’s products, and they decay once you go quiet.

### What to prepare

An account and your product URL — the submit flow crawls your site and pre-fills name, description, categories, pricing and screenshots for you to correct.
A tier decision: the free route waits in a publishing queue, Standard Launch is $39 one-time and publishes instantly, and the 7-day and 30-day promotions are listed at $89 and $229.
Some community work: the FAQ says 400 or more user points from recent engagement can be redeemed for an immediate launch instead of paying.

### What “live” means here

Live means your product resolves at /p/<slug> inside the feed with upvotes, comments and ratings attached. The FAQ says published listings stay permanently, including the link to your site; the paid promotions add featured placement in the feeds for their 7 or 30 days on top of that.

### Worth knowing

Freshness counts in the score: relaunches, edits and changelog posts keep a product at full strength while dormant ones fade, so plan updates for after launch day. The pricing page also sells a directory submission service from $149 — that is a separate paid service, not part of the listing.
Official site: PeerPush ↗All product launch platforms →
Short profile from the platform’s public pages, not a submission service. Rules, prices and requirements change — recheck before you submit. LaunchRepo makes no publication, backlink or ranking promise.

###

Submission entry: https://peerpush.com/

## Verified recon — 2026-09-19 (BrowserOS)

- Substantive platform: **47,000+ builders**; daily launches with votes, comments, ratings, product updates, Product-of-the-Day badges.
- **"Available on iOS" platform badge exists** — app fits natively (iOS apps listed).
- "Add your product" + Login/Sign up; Promoted (paid) slots; **PeerPush MCP + Public API** — explicitly agent-integrable.

### Signup/submit form — observed 2026-09-19 (BrowserOS, field-level)

- `/submit` → **`/auth/login?redirectTo=/submit…`** — account required.
- Login: **Continue with email** (magic link) + **Google, X/Twitter, LinkedIn OAuth** — 4 auth paths, no password field. `/auth/signup` exists too.
- Note: "Advertise" (`/submit?option=sponsored`) is the paid lane; free lane is "Add your product" → `/submit`.

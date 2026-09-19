# Hacker News (Show HN)

| | |
|---|---|
| Site | https://news.ycombinator.com |
| Category | community |
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
Show HN post; strict self-promo norms


## Field observations
Source: LaunchRepo public field guide (https://launchrepo.dev/directories/hackernews/), observed unknown.

Hacker News is the Y Combinator community site; Show HN is its format for something you made that other people can play with. The rules page wants things people can run or hold, made by you personally, non-trivial, and easy to try without sign-ups — not blog posts, sign-up pages, newsletters or lists, and the guidelines add landing pages and fundraisers to that list.

Checked on September 17, 2026 on the platform’s public pages.

### Who lists here

Builders with a working product and time to answer questions in the thread. The guidelines say you must be around to discuss it, and the community is comfortable with early-stage work.

### What to prepare

A Hacker News account and a submission whose title starts with “Show HN”, plus a URL people can try immediately.
A plain explanation of how and why you built it — the rules ask for that, and warn against posting quick one-offs.
No vote solicitation: the guidelines say asking friends to upvote or comment is not ok, and the FAQ notes anti-abuse software drops some votes.

### What “live” means here

Every Show HN appears on /shownew immediately; it reaches the /show page only after clearing a small points threshold. Record the item URL and the date; a front-page position is an outcome, not the goal.

### Worth knowing

Ranking divides points by a power of time and is affected by flags and moderation; posts by high-karma users do not rank higher. Reposts are tolerated only if the story had no significant attention in the last year, and new features usually do not qualify as a Show HN.
Official site: Hacker News (Show HN) ↗All communities →
Short profile from the platform’s public pages, not a submission service. Rules, prices and requirements change — recheck before you submit. LaunchRepo makes no publication, backlink or ranking promise.

###

Submission entry: https://news.ycombinator.com/

## Verified recon — 2026-09-19 (BrowserOS)

- `/submit` shows bare login + create-account forms (username/password only — no OAuth, no email field at creation).
- Show HN rules apply: product must be something people can try — app qualifies via the live App Store link once launched.
- Hard norms: no launch-day asking-for-upvotes (bannable), founder posts from personal account, title format "Show HN: [Product] – one-line pitch". One Show HN per product; reposts allowed only after substantial changes + time.
- Text post or link post — link post to the product site or store page; expect mods to ask questions if it trips filters.

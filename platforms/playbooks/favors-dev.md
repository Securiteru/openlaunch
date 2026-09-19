# Favors.dev

| | |
|---|---|
| Site | https://favors.dev |
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
directory + launches + leaderboard


## Verified recon — 2026-09-19 (BrowserOS)

- Not a passive directory — **favor-trading network**: earn points by doing favors for other founders (upvotes, reviews, testimonials, feedback, shares), spend them on your own launch. Sign in + "Join free" + "Add your project".
- Directory + Queue + Launches + Leaderboard + Roast sections.
- **Hard-stop heavy**: every action here is public engagement (comments, reviews, upvotes) — requires user supervision throughout; not a fire-and-forget listing.

### Auth — observed 2026-09-19 (BrowserOS, field-level)

- `/login`: email magic link ("Send magic link") + Google + GitHub OAuth. Favor-trading model — submission = spending earned points.

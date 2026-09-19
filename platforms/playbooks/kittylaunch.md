# KittyLaunch

| | |
|---|---|
| Site | https://kittylaunch.com |
| Category | launch |
| Product page pattern | `https://kittylaunch.com/p/{slug}` |
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

- **"Get Started Free" confirmed free tier**; Log In/Sign Up; Pricing page for paid boosts.
- Weekly archive (top 3 hall of fame), Deals section (makers can offer promo codes — app could offer a Pro discount), Top Creators leaderboard.
- FAQ covers cost, launch timing, do-follow backlink — read FAQ at submit time.
- Categories: SaaS, AI/ML, Productivity, Education, Developer Tools, E-commerce — no Health; file under Productivity/SaaS.

### Signup — observed 2026-09-19 (BrowserOS, field-level)

- "Sign Up" / "Get Started Free" are JS buttons; click produced no navigation/dialog in snapshot — auth flow not yet captured (likely modal or SPA route). Re-probe needed.
- Site is productized: per-product Roadmap/Changelog/Feature-Request pages.

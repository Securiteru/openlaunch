# Wellfound

| | |
|---|---|
| Site | https://wellfound.com |
| Category | profile |
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
nofollow; free; company profile


## Field observations
Source: LaunchRepo public field guide (https://launchrepo.dev/directories/wellfound/), observed unknown.

Wellfound is the startup talent marketplace that spun out of AngelList in November 2022. Companies get a profile page with mission, team, funding stage, size and perks, and post jobs for free to a candidate network the site puts at 10 million; paid products are job ads, AI sourcing and a managed recruiter.

Checked on September 17, 2026 on the platform’s public pages.

### Who lists here

Startups that are hiring, or want a public company record in a place candidates and investors browse; a company page without an open role is a thin entry here.

### What to prepare

A company account on the “for companies” side — no credit card is needed and the post-a-job page says setup takes about four minutes.
Company story, logo, stage, team size, location and perks for the profile; salary and equity range for each job, which Wellfound shows up front.
Optionally an ATS connection (Greenhouse, Lever, Ashby, Workable) if you already run one.

### What “live” means here

Live means your company resolves under /company/<slug>/ with its jobs listed; the pricing page says every listing broadcasts across Wellfound’s own search, candidate email alerts and the weekly newsletter. Public company URLs returned 403 to an anonymous fetch when checked, so confirm visibility from a logged-out browser.

### Worth knowing

Wellfound and AngelList are separate companies since 2022; a listing here is not an AngelList venture profile. The recruit pricing page lists Job Ads from $200 per ad for top-of-results placement, Reach at $135 per seat a month and Autopilot at $500 a month plus a 10% placement fee.
Official site: Wellfound ↗All company and startup profiles →
Short profile from the platform’s public pages, not a submission service. Rules, prices and requirements change — recheck before you submit. LaunchRepo makes no publication, backlink or ranking promise.

###

Submission entry: https://wellfound.com/

## Verified recon — 2026-09-19 (BrowserOS)

- Startup recruiting platform (jobs, not product launches); Sign up → companies post jobs free.
- **Poor app fit** — no product-listing surface; skip unless hiring.

### Signup — observed 2026-09-19 (BrowserOS, field-level)

- `/jobs/signup`: name + email + **password min 12 chars** + Google OAuth. It's a jobs/recruiting platform — poor app fit (candidate-side flow).

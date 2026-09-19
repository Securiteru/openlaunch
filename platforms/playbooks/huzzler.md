# Huzzler

| | |
|---|---|
| Site | https://huzzler.so |
| Category | saas-directory |
| Product page pattern | `https://huzzler.so/products/{id}/{slug}` |
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

## Notes
product URL contains an opaque id


## Field observations
Source: LaunchRepo public field guide (https://launchrepo.dev/directories/huzzler/), observed unknown.

Huzzler is a review site for software that founders buy, with hand-written reviews, direct comparisons and a Huzzler Score out of 5. Next to the reviews it runs a startup directory: founders can list a product, browse by category, and the site advertises featured and boosted placement once a listing is live.

Checked on September 17, 2026 on the platform’s public pages.

### Who lists here

Founders of tools that fit a review-driven audience — developer APIs, boilerplates, scraping services and similar categories are what the homepage features — who want a directory entry rather than a launch day.

### What to prepare

An account: the submit page asks you to sign up or sign in before anything else.
A product page worth reviewing — the about page says startup listings go through human review and that the site would rather stay selective than approve everything.
A decision on the badge: the about page says a dofollow link back is earned by adding the Huzzler badge to your site, and no public page says what a listing without the badge gets.

### What “live” means here

Live means your product has a resolving page in the Huzzler directory with its category label; the about page promises category browsing, but the sitemap exposes no category pages yet. Submission goes into human review first, so keep the record pending until the page is public.

### Worth knowing

The submit page leads with domain-rating and backlink claims and a founder quote; treat those as the platform’s own marketing and verify the actual link on your live page. Featured and boosted placements are paid extras sold after listing, not part of the basic entry.
Official site: Huzzler ↗All product launch platforms →
Short profile from the platform’s public pages, not a submission service. Rules, prices and requirements change — recheck before you submit. LaunchRepo makes no publication, backlink or ranking promise.

###

Submission entry: https://huzzler.so/

## Verified recon — 2026-09-19 (BrowserOS)

- Founder-focused software review site (DR 64+); editorial reviews with "Huzzler Score" + "Recently Boosted" paid placements.
- Submit product + Login/Sign up; FAQ covers "Can I list my startup" — listing + review are likely separate tracks.

### Signup/submit — observed 2026-09-19 (BrowserOS, field-level)

- `/submit-product` shows only Login/Sign-up buttons — account wall; auth method not yet captured.

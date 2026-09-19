# Capterra

| | |
|---|---|
| Site | https://www.capterra.com |
| Category | review |
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
hand-vetted (favors.dev atlas)


## Field observations
Source: LaunchRepo public field guide (https://launchrepo.dev/directories/capterra/), observed unknown.

Capterra is a software discovery site with verified user reviews and comparisons that says it has been running since 1999. Its vendor page is now branded “powered by G2 Digital Markets”: the Get Your Product Listed button leads to G2’s add-product form at g2.com/products/new, and vendor accounts log in at app.g2digitalmarkets.com.

Checked on September 17, 2026 on the platform’s public pages.

### Who lists here

Business software vendors that want a profile where buyers compare tools, plus the option of paid demand programmes. G2 Digital Markets offers pay-per-click Engaged Buyers campaigns and leads it says are qualified by phone or chat.

### What to prepare

Brand and product information, screenshots and pricing — the fields the G2 Digital Markets profiles page names for personalising a listing.
Customers ready to review: the about page says moderators check that reviewers are real people and screen text for plagiarism and generative AI.
A product that fits an existing category, since the about page says software researchers vet all listed solutions and update profiles as needed.

### What “live” means here

Live means your product profile resolves on capterra.com under /p/<id>/<name>/ inside its category with the website link working. Research reports such as the Capterra Shortlist depend on verified reviews, not on the listing itself.

### Worth knowing

Prices for the PPC and lead programmes are not published on the public vendor pages — record “not published”. Capterra’s own pages sit behind Cloudflare and refuse scripted requests, and g2.com/products/new blocked even a headless browser, so do the listing from your own browser. The site discloses that it may earn a referral fee when visitors click through to a vendor.
Official site: Capterra ↗All b2b software review sites →
Short profile from the platform’s public pages, not a submission service. Rules, prices and requirements change — recheck before you submit. LaunchRepo makes no publication, backlink or ranking promise.

###

Submission entry: https://www.capterra.com/vendors/

## Verified recon — 2026-09-19 (BrowserOS)

- Software review site; "For vendors" + Vendor Login in nav; "Get your product listed" CTA; Healthcare category exists.
- Vendor listing flow behind vendor portal — needs account + company verification.

### Submit — observed 2026-09-19 (BrowserOS, field-level)

- Vendor portal = `app.g2digitalmarkets.com/login` (shared Gartner Digital Markets portal w/ GetApp/SoftwareAdvice). Account-gated vendor flow.

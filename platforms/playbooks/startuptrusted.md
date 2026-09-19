# StartupTrusted

| | |
|---|---|
| Site | https://startuptrusted.com |
| Category | saas-directory |
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
Platform provides an embeddable badge. Record the snippet in this file after the listing is live.


## Field observations
Source: LaunchRepo public field guide (https://launchrepo.dev/directories/startuptrusted/), observed unknown.

StartupTrusted presents itself as a database of verified startups with Featured Startups and Recent Listings sections. Each entry has a name, logo and short description and its own page under /startup/.

Checked on September 17, 2026 on the platform’s public pages.

### Who lists here

Founders who want a simple, permanent startup profile with a public URL and are not looking for a dated launch or vote competition.

### What to prepare

A Google or email sign-in — the /submit page shows the login gate before any form.
Name, logo and a one-paragraph description, the fields visible on existing entries.
Awareness that a Pricing link exists on the submit page, although no prices are shown to logged-out visitors, so budget for the possibility of a paid tier.

### What “live” means here

Live means a resolving page at startuptrusted.com/startup/<slug> that also appears in Recent Listings. The “verified” and “Featured” labels have no published criteria, so do not record either as an outcome.

### Worth knowing

The site shows a domain-rating badge on its own pages; that is a claim about the platform, not a promise about your listing. Because the whole submission flow sits behind a login, plan for a session where your agent can drive a logged-in browser rather than a single form post.
Official site: StartupTrusted ↗All product launch platforms →
Short profile from the platform’s public pages, not a submission service. Rules, prices and requirements change — recheck before you submit. LaunchRepo makes no publication, backlink or ranking promise.

###

Submission entry: https://startuptrusted.com/

## Verified recon — 2026-09-19 (BrowserOS)

- "Database of verified startups"; Submit your Startup; DR 55; featured + recent listings.
- **Precedent: a a comparable vendor is featured** — adjacent products accepted; app fits.

### Signup/submit form — observed 2026-09-19 (BrowserOS, field-level)

- `/submit` → **`/login?callbackUrl=/submit`** — email magic-link + **Google OAuth**.

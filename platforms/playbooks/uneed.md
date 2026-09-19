# Uneed

| | |
|---|---|
| Site | https://uneed.best |
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
open-form submit; free (favors.dev atlas)


## Field observations
Source: LaunchRepo public field guide (https://launchrepo.dev/directories/uneed/), observed 2026-09-13.

Check account capacity before preparing another launch. The observed free workflow allowed only one pending launch and blocked a new submission when the account already had waiting products. This is an account constraint, not a verdict on product fit.
Observed: 2026-09-13

### Preparation

Sign in with the intended Google or email account and inspect its unpublished products. Prepare the product URL and launch assets only after understanding which pending item occupies the slot.

### Workflow

Open Submit a tool. If a one-launch limit appears, inspect Manage my products and the waiting list. Reconcile those entries with your own tracker before creating anything else.

### Watch for

Do not delete another product or create extra accounts to evade the limit. A read-only integration cannot submit a product. Stop and ask the owner to decide how to handle existing launches.

### What counts as confirmation

Record blocked with the next action, not submitted. Resume after capacity is legitimately available and confirm the resulting queue or schedule in the account.

Submission entry: https://www.uneed.best/submit-a-tool

## Verified recon — 2026-09-19 (BrowserOS)

- Submit URL confirmed: `uneed.best/submit-a-tool`.
- **No account needed to start** — form opens with just product name + product URL; Uneed scrapes the page, THEN asks you to sign up to save it. Agent can pre-fill the scrape step before handing off for account creation.
- Free tier exists alongside paid boosts; pricing at `uneed.best/pricing`.
- Site advertises DR 75 backlink.
- Earlier observation still stands: free accounts hold one pending launch — check existing products before submitting.

### Submit form — observed 2026-09-19 (BrowserOS, field-level)

- `https://www.uneed.best/submit-a-tool` — **form visible without login** (200, no redirect).
- Step-1 fields: **product name** (text, required) + **product URL** (text, required) + **"Preview my product"** button — scrapes the URL before account creation, matching earlier field guide. No CAPTCHA on step 1.
- Signup path: "Register" → `/signup`; submit entry "Submit a product" / "Add your product" → `/submit-a-tool`.
- Homepage also exposes Launchpad, Launch Guide, free tools (product-launch checklist).

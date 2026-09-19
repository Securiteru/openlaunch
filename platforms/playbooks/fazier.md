# Fazier

| | |
|---|---|
| Site | https://fazier.com |
| Category | launch |
| Product page pattern | `https://fazier.com/launches/{slug}` |
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
Source: LaunchRepo public field guide (https://launchrepo.dev/directories/fazier/), observed 2026-09-13.

Treat eligibility checks as a decision gate. The observed Basic submission flow required community comments, a visible badge and an Ahrefs Domain Rating above zero. A product that fails a requirement should stop before attesting compliance.
Observed: 2026-09-13

### Preparation

Prepare an English website and inspect the current eligibility checklist while signed in. Verify the actual domain in the named rating checker; do not substitute a different authority metric.

### Workflow

Open Submit and inspect the Basic route. Check whether the community requirement is already satisfied. Verify the domain rating and obtain the official badge markup only if you can meet the conditions.

### Watch for

Do not manufacture comments, assert a rating you have not verified or buy an upgrade under a zero-spend mandate. Publishing a badge is a website change that requires the site owner’s authorization.

### What counts as confirmation

Record blocked when the rating or badge condition is unmet. A completed checklist is only preparation: obtain the final submission confirmation before recording pending review.

Submission entry: https://fazier.com/submit

## Verified recon — 2026-09-19 (BrowserOS)

- `fazier.com/submit` shows live pricing: **Basic FREE** (reviewed & listed within 30 days, requires Fazier backlink badge on your homepage/footer, homepage feature only if selected); Lite $29 one-time (no backlink required, publish or schedule); Premium $49 (DR 82+ dofollow, 15-day platform promotion); Super $99 (top-of-homepage pin 15 days).
- Sign In / Join links on submit page — account required before form.
- Note divergence: earlier field guide reported DR>0 + community comments required for Basic; current page advertises backlink-badge requirement instead. Verify requirements again at submit time.

### Join dialog — observed 2026-09-19

- Clicking **Join** opens a modal "Welcome to Fazier": **Continue with Google** + **Continue with Email** buttons + Terms / Privacy Policy links. No password field — email path is likely magic-link or OTP.
- Human gate: Google OAuth consent or inbox access for the email path.

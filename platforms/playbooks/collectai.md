# CollectAI

| | |
|---|---|
| Site | https://collectai.tools |
| Category | ai-directory |
| Product page pattern | `https://collectai.tools/item/{slug}` |
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
Source: LaunchRepo public field guide (https://launchrepo.dev/directories/collectai-tools/), observed unknown.

CollectAI is an AI tools directory sorted into categories such as writing, image and design, video and audio, development and business, with tag filters (free, open source, no signup) and a blog. Every tool has a details page with description, features and pricing information.

Checked on September 17, 2026 on the platform’s public pages.

### Who lists here

AI tool makers who want a categorised entry with a low-cost paid option and a published review window.

### What to prepare

An account: /submit redirects to login.
Name, description, category, tags and pricing information, since the listing page shows all of them.
A tier: Free (backlink to the site required, reviewed and listed within 72 hours, you pick the publish day) or Pro at $9.90 (no backlink required, featured at the top of listings); a weekly sponsor slot is shown at $19.90.

### What “live” means here

Live means your tool resolves on its details page and shows in its category. A free submission is pending until the review passes; the pricing page says Pro lists right away.

### Worth knowing

The about page says inactive tools are removed over time, so a dead product link can cost the listing. The homepage carries labelled ad slots; those are separate from the directory ranking.
Official site: CollectAI ↗All software and tool directories →
Short profile from the platform’s public pages, not a submission service. Rules, prices and requirements change — recheck before you submit. LaunchRepo makes no publication, backlink or ranking promise.

###

Submission entry: https://collectai.tools/

### Submit — observed 2026-09-19 (BrowserOS, field-level)

- Submit → `/auth/login?callbackUrl=/submit` — **Google + GitHub OAuth only** (NextAuth template). AI-only.

# Launchtory

| | |
|---|---|
| Site | https://launchtory.com |
| Category | launch |
| Product page pattern | `https://launchtory.com/projects/{slug}` |
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
Platform links are plain text — no badge asset observed.


## Verified recon — 2026-09-19 (BrowserOS)

- Directory organized by **Topics** (productivity, e-commerce, marketing…) and **Stacks** (Next.js, Cloudflare, Vercel, WordPress…). app can file under Cloudflare stack + health/productivity topic.
- Submit Project + Login/Signup in nav; support@launchtory.com listed.
- No daily leaderboard — permanent catalog with "Featured" and "Recently submitted" sections.

### Signup — observed 2026-09-19 (BrowserOS, field-level)

- `/signup`: Rails form — **Email + Password** only (authenticity_token), no OAuth observed. Login at `/login`.

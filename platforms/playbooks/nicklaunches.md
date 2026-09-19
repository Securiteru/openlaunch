# Nick Launches

| | |
|---|---|
| Site | https://nicklaunches.com |
| Category | launch |
| Product page pattern | `https://nicklaunches.com/products/{slug}/` |
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
Source: LaunchRepo public field guide (https://launchrepo.dev/directories/nicklaunches/), observed unknown.

Nick Launches is a weekly launch board: the current week shows over a hundred launches ranked with medal positions and category tags. The submit page offers two routes — a classic browser form with URL prefill, or an MCP server that lets Claude Code, Claude Desktop or Cursor draft the listing from your URL.

Checked on September 17, 2026 on the platform’s public pages.

### Who lists here

Builders who launch with an AI agent in the loop. It is one of the few boards that documents an agent route, while still requiring a human to review and publish.

### What to prepare

A sign-in and, for the classic route, a logo, screenshots, a plan choice and a launch week; drafts can be saved.
For the agent route, the one-line `claude mcp add` command shown on the submit page and a product URL — the site says no API key is needed and you approve the connection in the browser.
A finished product page: the site offers a pre-launch site audit and the agent draft still needs your review.

### What “live” means here

Live means your product appears in the current week’s ranked list with its category tags. A draft opened by an agent is a draft; only publishing from your account starts the launch week.

### Worth knowing

The site advertises a permanent backlink and a domain rating; verify the link on your own launch page and treat the number as marketing.
Official site: Nick Launches ↗All product launch platforms →
Short profile from the platform’s public pages, not a submission service. Rules, prices and requirements change — recheck before you submit. LaunchRepo makes no publication, backlink or ranking promise.

###

Submission entry: https://nicklaunches.com/

## Verified recon — 2026-09-19 (BrowserOS)

- Weekly leaderboard (Week 38: 107 launches) with sign-in-gated upvotes.
- **Homepage has a single-field launch form (yourproduct.com + Launch)** — lowest-friction entry; account presumably at save.
- Maker attribution via X handles; categories incl. Lifestyle, Sustainability, Other — app fits Lifestyle/Health-adjacent.

### Signup/submit form — observed 2026-09-19 (BrowserOS, field-level)

- "Launch Now" → `/signin/?callbackUrl=/submit/` — account required.
- Login: **Email + Password** + **Sign in with Google** (Next.js server actions). No CAPTCHA.

# DevHunt

| | |
|---|---|
| Site | https://devhunt.org |
| Category | dev-directory |
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
dofollow; free; dev tools only (backlinkbot)


## Field observations
Source: LaunchRepo public field guide (https://launchrepo.dev/directories/devhunt/), observed unknown.

Dev Hunt is an open-source launch platform for developer tools built by John Rush and contributors, with its repository public on GitHub. Launches are grouped into weeks with a countdown to the vote closing, and every tool page shows upvotes, impressions and the rank for that week. Tools are tagged free, subscription or one-time fee and filed under fixed categories.

Checked on September 17, 2026 on the platform’s public pages.

### Who lists here

Makers of open-source tools, APIs and SDKs, frameworks and libraries, IDEs, testing and monitoring tools — the list the About page gives. Voting and commenting need a GitHub or Google login, which the login page says is there to filter out bots and fakes.

### What to prepare

A GitHub or Google account; the “Submit your Dev Tool” button leads to the login screen before any form.
Tool name, a one-line description, categories from the fixed list, a pricing tag and a link — that is what a tool page displays.
A launch week you can be present for: the About page says the average wait for a free launch is six months and sells a $49 option to skip the queue and pick a week.

### What “live” means here

Your tool first appears in the upcoming list with its date, then moves into the current week, where votes count until the countdown ends. Live means the /tool/ page is public and inside that week’s ranking, not that the launch is finished.

### Worth knowing

The About page says weekly winners get a newsletter feature, a social post, a winner badge and partner discounts. Homepage and newsletter ads are sold separately at $497 and $397, and the site notes that all paid packages are activated manually after purchase and can be refunded until then.
Official site: Dev Hunt ↗All product launch platforms →
Short profile from the platform’s public pages, not a submission service. Rules, prices and requirements change — recheck before you submit. LaunchRepo makes no publication, backlink or ranking promise.

###

Submission entry: https://devhunt.org/

## Verified recon — 2026-09-19 (BrowserOS)

- Dev-tools-only launch board ("Voted by Developers"); Submit your Dev Tool + Sign In; daily upvote feed.
- **Poor app fit** — consumer health app, not a dev tool. Mark skipped for app.

### Signup/submit — observed 2026-09-19 (BrowserOS, field-level)

- "Submit your Dev Tool" → **`/login`**: **GitHub + Google OAuth only**. Dev-tools-only directory — app doesn't fit.

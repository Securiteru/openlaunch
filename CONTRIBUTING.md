# Contributing

The most valuable contributions are **verified playbook improvements** and
**new platforms** — knowledge gained from real submissions.

## Improving a playbook

Playbooks are living docs. If you (or your agent) submitted to a platform,
record what you actually observed:

- Real submission steps where they differ from the skeleton
- Cost: free / freemium / paid, with the observed price
- Account requirements and verification friction
- Hurdles: CAPTCHAs, moderation queues, review times, badge requirements
- Confirmation signal and how long `live` took
- Link policy: dofollow or not

Only mark fields verified when they were directly observed. Keep
`UNVERIFIED` markers honest — an unverified field is information, not a gap.

## Adding a platform

1. Add a row to `platforms/platforms.csv`:
   `slug,name,url,category,product_url_pattern,badge,notes,cost,account,live,tiding_fit`
   - `category`: `launch` | `ai-directory` | `saas-directory` |
     `dev-directory` | `general-directory` | `review` | `press` |
     `community` | `profile` | `marketplace` | `design` |
     `app-discovery` | `app-review` | `beta-testing` | `deals` |
     `newsletter` | `dev-registry` | `meta-directory` | `api-directory` |
     `review-service`
   - `cost`: `free` | `freemium` | `paid` | `paid-signals` | `n/a` | `unknown`
   - `account`: `none` | `email` | `social` | `badge` | `github` | `partner` |
     `n/a` | `unknown`
   - `live`: `live` | `blocked` | `dead` | `unknown`
   - `tiding_fit`: `yes` | `maybe` | `no` — current-product relevance
     (rename/repurpose per product)
   - `product_url_pattern`: the public listing URL shape with `{slug}`
     (e.g. `https://example.com/item/{slug}`) — leave empty if unknown
   - `badge`: `img` | `img-remote` | `text` — what the platform offers for
     your footer
2. Run `python3 platforms/build.py` — it creates the stub without touching
   existing playbooks.
3. Fill in what you verified; leave the rest `UNVERIFIED`.

## Rules

- No fabricated platform details — unverifiable stays `UNVERIFIED`.
- No paywalled-platform bypass tricks, CAPTCHA circumvention, or
  multi-accounting advice. Playbooks document legitimate submission only.
- Keep playbook edits platform-scoped; don't restructure unrelated files.
- `make check` must pass (CSV validates, tracker JSON parses).

## Style

Match the existing playbook structure. Write for an agent reader: imperative
steps, checklists, explicit unknowns.

## Recon workflow (learned 2026-09-28)

When bulk-verifying platforms:

- **Write the CSV only with `csv.writer`** — never string-concatenated
  rows. Unquoted commas in `notes` silently corrupt the column count
  (this happened; 9 rows broke). The file uses CRLF line endings —
  preserve them or every line diffs.
- **HTTP status is not ground truth.** Three failure modes observed:
  parked domains return 200 (`payonceuseforever`), bot-protection
  returns 403/429 for live sites (alternativeto, g2), and SPAs return
  200 for every path (`startup-inspire`, `versily`, `allmyfaves`) so
  discovered submit links may be fake. Confirm conflicts in a real
  browser (BrowserOS) before marking `live`/`dead`.
- **Probe order:** liveness HEAD/GET sweep → homepage submit-link
  discovery → standard-path probes (`/pricing`, `/submit`,
  `/get-listed`, `/advertise`) → browser pass for `blocked` rows only.
- **Mark uncertainty explicitly:** `cost=paid-signals` means regex hit
  on a pricing page, not an observed price. `live=blocked` means curl
  was refused, not that the site is down.

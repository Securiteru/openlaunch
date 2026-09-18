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
   `slug,name,url,category,product_url_pattern,badge,notes`
   - `category`: `launch` | `ai-directory` | `saas-directory` |
     `dev-directory` | `general-directory`
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

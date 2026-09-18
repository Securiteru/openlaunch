# Evidence rules

The tracker is only useful if every status means what it says. These are the
transitions and the artifact each one requires. If the artifact doesn't
exist, the status doesn't move — and the report says `NOT VERIFIED`, not
"done".

## Status ladder

```
researched → ready → submitted → pending-review → live
                 ↘ rejected      ↘ paid-blocked    ↘ skipped
```

(Statuses may also skip steps — e.g. `researched` → `paid-blocked`.)

## Required evidence

| Transition to | Artifact required |
|---|---|
| `researched` | Notes in the tracker `next_action`/playbook: observed cost, account requirement, submission entry point |
| `ready` | Confirmed the form's required fields are covered by the brief |
| `submitted` | Observed confirmation — success page text, confirmation email seen, or the item appearing in a platform dashboard |
| `pending-review` | Platform states a review/queue exists and the item is in it |
| `live` | **The public listing URL loads and the product is visibly present.** Record `listing_url`. |
| `rejected` | The observed rejection (message, email, removed listing) |
| `paid-blocked` | The observed paywall — price and what it gates |
| `skipped` | The reason: out of scope, failed selection score, duplicate listing, user decision |

## Rules

- **A submission confirmation is not a live listing.** `submitted` and
  `pending-review` stay until the public URL is observed.
- **`live` requires loading the URL.** If it 404s, shows a different
  product, or sits behind a login wall, it is not live — report what was
  actually observed.
- **Screenshots > memory.** When in doubt, save a screenshot or the exact
  on-page text into `products/<slug>/evidence/` and reference the filename
  in the tracker.
- **Timestamps are real.** `submitted_at`, `live_at`, `updated_at` are the
  dates the thing was observed, not when the row was typed.
- **Never upgrade a status to hide a failure.** A CAPTCHA block is
  `submitted: false` with `next_action: "user to solve CAPTCHA"` — not a
  half-done `submitted`.
- **The report mirrors the tracker.** If the tracker says `pending-review`,
  the report says pending review — never "listed".

## Tracker record shape

```json
{
  "product": "myproduct",
  "platform": "producthunt",
  "status": "submitted",
  "listing_url": null,
  "evidence": "submission success page, 2026-09-18",
  "cost": "free",
  "submitted_at": "2026-09-18",
  "live_at": null,
  "next_action": "check for public page in 48h",
  "updated_at": "2026-09-18"
}
```

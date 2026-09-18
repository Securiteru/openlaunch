# Platform selection

How the agent chooses which platforms are worth a submission — and in what
order. The goal is a defensible shortlist, not maximal volume.

## Inputs

- `platforms/platforms.csv` — category, product URL pattern, notes
- `platforms/playbooks/<slug>.md` — verified cost, effort, hurdles (as filled
  in over time)
- `products/<slug>/brief.md` — audience and category fit

## Scoring (0–3 each)

| Factor | Question | 0 | 3 |
|---|---|---|---|
| **Audience fit** | Does this platform's audience match the brief's audience? | Generic dump site | Exactly the buyer |
| **Audience evidence** | Signs of real traffic: community, rankings, recent launches | Looks dead / auto-approves | Active front page, real comments |
| **Link value** | Dofollow product page, indexable | nofollow/sponsored links | dofollow product page |
| **Category fit** | Platform accepts this product type | Wrong category (AI-only dir for a non-AI app) | Purpose-built |
| **Effort (inverse)** | Time + account + review friction | Paid-only, heavy verification | One form, instant publish |
| **Cost (inverse)** | Money required for a basic listing | Paid-only | Free |

Sum → tier:

- **Tier 1 (≥ 14):** submit first — high fit, low friction.
- **Tier 2 (10–13):** submit in later batches.
- **Tier 3 (< 10):** `skipped` with the scored reason, revisit only if the
  playbook changes (e.g. a paid tier becomes free).

## Ordering within a batch

1. Platforms already verified in their playbooks beat `UNVERIFIED` ones.
2. Launch platforms with time-sensitive mechanics (e.g. Product Hunt launch
   day) are scheduled deliberately, not folded into a batch.
3. Mix categories — don't burn the batch on five near-identical directories.

## Defaults

- Batch size: **3–5 platforms**, then report before continuing.
- AI-tool directories only apply if the product is actually an AI tool —
  check the brief, don't assume.
- A platform flagged `nofollow` isn't worthless (referral traffic exists)
  but scores accordingly.
- New/unresearched platforms get scored from a quick site visit, not from
  assumptions. Record what you find in the playbook.

## Output format

The agent proposes the batch as a table — platform, score, tier, effort,
cost, reason — and waits for approval before submitting anything.

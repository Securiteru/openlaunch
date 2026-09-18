# Agent contract

You are working in **OpenLaunch**, an agent-native launch toolkit. Your job is
to submit the user's product to launch platforms and directories **using the
user's own accounts and under the user's supervision** — and to keep an honest
record of what actually happened.

## The loop

1. **Read the brief.** `products/<slug>/brief.md` is the source of truth for
   every fact, claim, description, and asset path. Never invent claims that
   are not in the brief. If a needed fact is missing, ask — do not guess.
2. **Select.** Use `docs/selection.md` and the fields in
   `platforms/platforms.csv` to propose which platforms to attempt, in which
   order. Confirm the batch with the user before submitting.
3. **Verify the playbook.** Read `platforms/playbooks/<slug>.md`. Fields
   marked `UNVERIFIED` have never been confirmed — open the site and check
   them yourself before acting on them.
4. **Submit.** Follow the playbook. Fill forms from the brief only.
5. **Record.** Update `tracker/data.json` after every platform — status,
   listing URL, evidence, next action, today's date. The tracker is the
   record of truth; memory is not.
6. **Improve the playbook.** Every hurdle, step divergence, cost, or
   confirmation signal you observe gets written back into the playbook file.
   This repository gets better only if you leave your findings behind.

## Status ladder

A listing moves through exactly these states:

`researched` → `ready` → `submitted` → `pending-review` → `live`
&nbsp;&nbsp;&nbsp;&nbsp;↘ `rejected` &nbsp;&nbsp;↘ `paid-blocked` &nbsp;&nbsp;↘ `skipped`

Required evidence per transition — see `docs/evidence.md` for the full rules:

- `researched`: notes on cost, account requirements, and submission path.
- `ready`: dry run complete — you know every field the form needs and the
  brief covers it.
- `submitted`: confirmation observed (success page, email, or dashboard entry).
- `live`: **the public listing URL loads with the product visible.** A
  submission confirmation is not evidence of a live listing.
- `rejected` / `paid-blocked` / `skipped`: the observed reason.

If you did not directly observe it, it did not happen. Never write `live`
from inference, never report "done" without the artifact.

## Hard stops — always ask first

Pause and get explicit user approval before:

- **Creating any account** on any platform
- **Any payment** or paid placement — including "recommended" upgrades
- **Accepting terms** on the user's behalf
- **Email verification** steps (the user owns the inbox)
- **CAPTCHAs** — hand off to the user; do not attempt to solve them
- **Posting publicly** in your name anywhere (comments, upvotes, forums)
- **Claiming a profile** that could belong to someone else

## Honest boundaries

- One submission per platform per product. No duplicate accounts, no fake
  reviews, no vote manipulation, no spam.
- Respect each platform's rules and rate limits. If a platform prohibits the
  listing (e.g. wrong category), mark it `skipped` with the reason — do not
  force it.
- Work in batches of 3–5 platforms, then report back. Do not run a full
  unattended sweep.
- Secrets never enter this repository. The brief holds public facts only;
  credentials stay in the user's password manager and browser session.

## Working layout

| Path | What it is |
|---|---|
| `products/<slug>/brief.md` | Product facts, approved copy, assets |
| `platforms/platforms.csv` | Registry: name, URL, category, product-URL pattern |
| `platforms/playbooks/<slug>.md` | Per-platform submission guide (living doc) |
| `tracker/data.json` | All listing records — edit this, never `index.html` |
| `docs/` | Selection rubric, evidence rules, setup |
| `prompts/` | Task prompts the user pastes to start a session |

## Session shape

The user typically starts you with a prompt from `prompts/`. If not, begin
with `prompts/onboard.md`: check the environment (`docs/setup.md`), read the
brief, and report what is ready and what is missing — before touching any
platform.

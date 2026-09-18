# Setup

What the toolkit needs, and how the agent verifies it works before any
submission.

## Prerequisites

- **Git** and **Python 3.10+** — for `platforms/build.py` and the tracker
  server (`make serve`).
- **A browser the agent can drive** — Chrome with a browser tool the agent
  controls (BrowserOS, Chrome DevTools Protocol, Playwright, or equivalent).
  The agent submits through *your* browser so listings run under your real
  session and accounts.
- **An agent with local-file and browser access.** An agent that can only
  read files cannot submit anything; an agent that can only browse cannot
  maintain the tracker. You need both.

## Environment check

The agent runs this at onboarding (`prompts/onboard.md`). Each check must be
*observed* to pass:

1. **File read** — the agent reads this file and reports back a sentence
   from it.
2. **File write** — the agent appends a test record to `tracker/data.json`
   and removes it again (or writes to a scratch file).
3. **Browser read** — the agent opens a harmless page (e.g. example.com) in
   the connected browser and reports its title.
4. **Session check** — the agent opens one platform it will submit to and
   reports whether a user session exists (logged in vs. not). No login is
   attempted — that is always a user action.

If any check fails, the agent stops and reports exactly which capability is
missing. Do not proceed to submissions on a degraded setup — that is how
silent failures happen.

## Per-product workspace

```
products/<slug>/
  brief.md        # required — copy from brief/product-brief.template.md
  assets/         # logo, screenshots referenced by the brief
  notes.md        # optional — running notes for this product's campaign
```

Multiple products share the same playbooks and tracker; listings in
`tracker/data.json` are keyed by product slug.

## Accounts

The agent never creates accounts on its own. Recommended flow:

1. Agent identifies which platforms in the batch need accounts (playbook
   field `Account required`).
2. You create them (password manager, your email).
3. Agent proceeds with submissions under your logged-in session.

Store credentials in a password manager, never in this repository.

## Cost posture

Default assumption: **free tiers only**. Many directories offer paid
placement; the agent stops at every paywall and asks. Budget decisions are
yours, per platform, with the price observed on the page.

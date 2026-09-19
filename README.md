# OpenLaunch

**Your AI agent submits your product to launch platforms and directories —
with your accounts, under your supervision, on your machine.**

OpenLaunch is an open-source, agent-native launch toolkit. Instead of paying
a service to blast your product at directories, you clone this repo, fill in
one product brief, and point your coding agent (Claude Code, Codex, Cursor,
Devin — anything that reads `AGENTS.md` and drives a browser) at it. The
agent does the repetitive submission work; you approve accounts, payments,
and anything public.

## What's inside

| Piece | Path | What it does |
|---|---|---|
| Platform playbooks | `platforms/playbooks/` | Per-platform submission guide: prep, steps, known hurdles, confirmation signals. Living docs — your agent writes back what it learns. |
| Registry | `platforms/platforms.csv` | 176 seeded platforms: launch sites, AI-tool directories, SaaS/dev directories, review sites, communities, profiles — including product-page URL patterns and submission mechanics where known. |
| Product brief | `brief/product-brief.template.md` | Every fact, approved claim, description length, and asset in one place. The agent never invents copy. |
| Selection rubric | `docs/selection.md` | Score platforms by fit, audience, link value, effort, and cost before spending submissions. |
| Local tracker | `tracker/` | A static dashboard + `data.json` the agent maintains: submitted vs. pending vs. live, with evidence links. `make serve` → localhost:8420. |
| Agent prompts | `prompts/` | Copy-paste session starters: onboard, select, submit a batch, verify listings, report. |
| Agent contract | `AGENTS.md` | The rules of engagement: status ladder, evidence requirements, hard stops before accounts/payments/public posts. |

## Quickstart

```bash
git clone https://github.com/Securiteru/openlaunch.git
cd openlaunch

# 1. Create your product brief
mkdir -p products/myproduct
cp brief/product-brief.template.md products/myproduct/brief.md
# ...fill it in...

# 2. Open the tracker (optional but recommended)
make serve    # → http://localhost:8420

# 3. Point your agent at the repo and paste:
#    "Read AGENTS.md, then follow prompts/onboard.md for product 'myproduct'."
```

The agent will check your environment, propose a platform batch, and start
submitting — pausing for you at every account, payment, CAPTCHA, or public
action.

## What you need

- Git and Python 3.10+ (for the playbook generator and tracker server)
- A browser the agent can drive (Chrome with a browser tool such as
  BrowserOS, CDP, Playwright — see `docs/setup.md`)
- An AI coding agent with local-file and browser access
- Your own accounts (created with your approval) and your provider's AI plan

## Status and honest scope

- **176 platforms seeded.** The registry combines three public sources: a
  shipping product's badge wall (77 sites), the favors.dev atlas and DR-ranked
  roundups (50), and LaunchRepo's public directory catalog (49 — profiled
  platforms plus catalog teasers). Every seed domain was checked live
  2026-09-18/19; a handful of teaser-derived domains are marked unconfirmed in
  `notes`. Playbook fields start `UNVERIFIED` and become accurate as agents
  verify them on real submissions. LaunchRepo claims 347 platforms — only ~97
  are publicly named on its site; our coverage overlaps but does not copy
  their (paid) playbook content.
- **66 playbooks carry real field data.** LaunchRepo's public platform
  profiles and field guides were harvested (`platforms/harvest_launchrepo.py`)
  into a `## Field observations` section per playbook — dated observations,
  submission entry URLs, eligibility gates, and confirmation criteria, with
  source attribution. Example: BetaList is paid-only and rejects subdomain
  sites; Uneed free accounts hold one pending launch; Fazier requires DR > 0
  plus badge plus community comments.
- **Not affiliated with LaunchRepo or any listed platform.** This is an
  independent re-implementation of the toolkit concept; all content is
  original or community-contributed.
- **No magic.** The toolkit removes repetitive work and enforces honest
  bookkeeping. It does not create accounts for you, bypass CAPTCHAs, or
  guarantee listings — platforms moderate however they moderate.

## Contributing

Playbooks get better every time an agent records a real hurdle, cost, or
confirmation signal. See `CONTRIBUTING.md` — verified playbook improvements
and new platforms are the most valuable contributions.

## License

MIT — see `LICENSE`.

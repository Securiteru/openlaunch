# Registry recon state — 2026-09-28

Snapshot of `platforms/platforms.csv` after the liveness + deep-recon
passes. Schema: `slug,name,url,category,product_url_pattern,badge,notes,
cost,account,live,tiding_fit`.

## Column vocab

- `cost`: `free` | `freemium` | `paid` | `paid-signals` (regex signals on
  submit/pricing pages, not a confirmed price) | `n/a` | `unknown`
- `account`: `none` | `email` | `social` | `badge` (listing requires
  embedding their badge) | `github` | `partner` | `form` | `n/a` | `unknown`
- `live`: `live` | `blocked` (bot/CF-blocked to curl; may need browser) |
  `dead` (unreachable or parked) | `unknown`
- `tiding_fit`: `yes` | `maybe` | `no` — relevance judgment for the
  current product brief (non-AI native iOS health app)

## Totals

- 344 platforms indexed; every row has a playbook stub.
- Liveness: 325 live / 5 blocked / 14 dead.
- Cost: 63 free / 159 freemium / 21 paid / 39 paid-signals / 23 n/a /
  38 unknown.
- Fit: 164 yes / 87 maybe / 93 no.
- Actionable queue (`fit=yes AND live=live AND cost IN free,freemium`):
  ~65 platforms — see `docs/submission-requirements.md`.

## Passes performed

1. **Liveness probe** — HTTP status for all 344 URLs.
   Browser-verified truth overrode curl results where they conflicted
   (parked domains returning 200 stayed `dead`; browser-live sites that
   403 curl stayed `live`).
2. **Auto-recon pass 1** — homepage fetch → discovered
   submit/pricing/list links → fetched → classified cost/account/captcha.
   247 sites.
3. **Auto-recon pass 2** — probed standard paths
   (`/pricing`, `/submit`, `/get-listed`, `/advertise`, `/join`) on the
   32 unknown-cost relevant sites. 6 sites flagged as SPA catch-alls
   (every path returns 200 — paths in notes unreliable).
4. **BrowserOS pass** — 16 bot-blocked majors opened in a real browser.
5. **Field extraction** — submit pages for `fit=yes|maybe` rows parsed
   for form fields → `docs/submission-requirements.md`.

## Verified facts worth keeping (browser-observed)

- alternativeto: free community directory; Tiding not yet listed.
- g2 / trustpilot / trustradius / glassdoor: free profile claims exist;
  paid = marketing/branding tiers.
- f6s: free membership; company profiles.
- seedtable: "Add to Seedtable" + paid features.
- capterra / getapp / softwareadvice: Gartner Digital Markets vendor
  portal ("For vendors" / "Vendor Login").
- hunt0: free community queue OR free badge launch OR $16.90 premium;
  full form fields mapped.
- spacerrapps: free submit + paid Highlight/Spotlight; Health/Fitness cats.
- softwareworld: free vendor registration (email, password, ToS, reCAPTCHA).
- mobilelaunch: free during beta (time-sensitive).
- makerhunt / sidehunt: free Launch tiers (correct TLD is `.io`).
- Paid-blocked (price observed): serchen $49.95, toolfolio $99+,
  saasgenius (fee by email), danrecommends $49, startup-heroes $10,
  all deals marketplaces (require an LTD offer — N/A for subscription app).

## Dead (verified)

appadvice, saasgallery, payonceuseforever, feedmyapp, app-useful,
toolsalad, indiepage.io, listmysaas.app, read.cv (402/sunset),
startuplister, batchlisted, shaft-ai (URL unverified),
awesome-ai-startups (repo 404), slant (SSL 526).

## Known gaps / next recon targets

- 38 `cost=unknown` rows — nearly all `fit=no/maybe`; low priority.
- 5 `blocked`: webwiki (403 in real browser too), startupbuffer (submit
  path 404s), capterra-adjacent CF pages — resolve per-batch.
- 6 SPA catch-alls: startup-inspire, startups-nrw, versily, allmyfaves,
  appvita, getworm — need browser form inspection.
- Badge-gated free paths (fazier, ufind-best, hunt0 badge launch) need a
  decision on embedding third-party badges on the product site.
- No submissions made; `tracker/data.json` holds demo records only.

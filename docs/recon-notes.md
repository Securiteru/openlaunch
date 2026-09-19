# BrowserOS recon — field-level signup/submit sweep (2026-09-19)

Method: BrowserOS neo (user's real browser). For every registry platform we
navigated to the actual register / sign-in / submit entry point and recorded
the pre-auth state: visible fields, OAuth providers, CAPTCHA type, pricing,
backlink requirements, multi-step behavior, external redirects, dead pages.

**No accounts were created. No forms were submitted. No credentials, payments,
terms acceptance, email verification, CAPTCHA solving, or public posting.**

Per-platform details live in `platforms/playbooks/<slug>.md` under dated
"observed 2026-09-19" headings. This file is the consolidated summary.

## Shared platform families (same codebase → same playbook)

### "Open-Launch" white-label family
Identical flow: `/projects/submit` → `/sign-in?redirect=/projects/submit` →
Email + Password + Google + GitHub + Cloudflare Turnstile. Signup adds Full
Name. Members observed:

`open-launch` `submitmysaas` `firsto` `launchvault` `nextlaunch` `prolaunch`
`fastlaunch` `aura-plusplus` `aat-ee` `openhunts` `startupfast` `dailypings`
(+ LaunchRepo's own listing on LaunchVoid suggests same ecosystem)

### NextAuth `callbackUrl` family
`/submit` → `/auth/login?callbackUrl=/submit` → Email+Password (or magic
link) + Google + GitHub, often Cloudflare Turnstile:

`saasfame` `toolfame` `webspot` `aibesttop` `aitoolhunt` `collectai`
`turbo0` `saasgrow` `startuptrusted` `navfolders`

### Django submit-form family
Identical fields + tier params (`?tier=free|paid|dual`), "Auto-fill" +
"Verify Badge" + "Submit Product", CSRF middleware token:

`thesaasdir` `thedevtoolsdir`

### Multi-step tool-form family (same operator)
url, name, tagline, 500–5000-char description, uploads, categories, pricing
model, platforms, social links, email:

`deeplaunch` `tooldirs`

### Google-only auth
`launchclash` `shinylaunch` `mylaunchstash` `acid-tools` `noonlaunch`

## Platforms with a real PUBLIC submit form (no account needed)

These can be submitted in one session once the user approves:

| Platform | Path | Notable fields | Cost |
|---|---|---|---|
| TheSaaSDir | `/submit/?tier=free` | URL, name, tagline, desc, screenshot, categories | Free + $19/$29 lanes |
| TheDevToolsDir | `/submit/` | same form | Free + paid |
| DeepLaunch | `/submit` | URL, name, tagline, long desc, uploads | Free + featured |
| ToolDirs | `/submit` | same multi-step | Free |
| ToolDirs-family CodeHype | `/submit` | URL, name, one-liner, "Fill with AI" | Free queue + Plus/Pro |
| MarketingDB | `/submit` | URL + full positioning (problem/solution/features/competitors) | Free |
| BuildVoyage | `/submit` | name, tagline, desc, URL, email, category, tech-stack tags, Turnstile, ToS | Free |
| Uneed | `/submit-a-tool` | product name + URL → "Preview" scrape | Free + paid |
| TinyStartups | (homepage) | URL-fetch pre-auth | Free |
| LaunchingNext | `/submit` | full form + math CAPTCHA | Free |
| StartupBuffer | `/site/submit` | multi-step: name/URL/email/pitch/desc/screenshot/geo/socials | Free |
| AIToolzDir | `/submit` | name, URL, logo, short+long desc, email, category | Free + $25 |
| AI Center | `/submit-tools` | contact+tool+pricing+platforms+uploads+socials | Free (AI-only) |
| AI Tool Trek | `/submit` | name + URL only | Free (AI-only) |
| Stork | `/submit` | single AI-tool-URL field | Free (AI-only) |
| StartupStash | `/add-listing/` | email only + reCAPTCHA | Free |
| StartupsFM | `/submit` | URL, name, one-liner, desc, category, geo, uploads, contact | Free |
| BacklinkForMe | `/tools/submit` | name, URL, category, desc, email, backlink-exchange y/n | Free |
| BoilerplateList | `/submit/` | company, name, email, boilerplate, link, desc, Turnstile | Free (dev niche) |
| AlphaDigits | `/submit-app-for-review/` | WP Formidable fields | likely paid review |
| Business-Software | `/add-your-product/` | name/email/product/phone/title/message + CAPTCHA | Free |
| StartupRanking | `/startup/create/url-validation` | URL-first create flow | Free |
| ShowMySites | `/accounts/signup/` | Django signup: user/email/pass×2 + Google | Free |
| SaaS Browser | `/en/users/sign_up` | name/email/pass + Google/GitHub + CAPTCHA | Free |
| SumoDir | `/submit` | 3-step wizard, Free/Premium/Review | Free lane |
| Alternative.tools | `/submit` | "Get Free Listing" lane | Free lane |

## Paid-only / paid-blocked (zero-spend constraint)

- **BetaList** — paid-only (field guide + auth-walled submit confirm)
- **Toolify** — $99 pay button on `/submit`
- **AI Kaptan** — $5 promo (was $20)
- **Futurepedia** — "verification fee" FAQ on submit page
- **Startup Inspire** — Submit → `/pricing`
- **AppSumo** — paid-deals marketplace
- **G2** — vendor portal, paid tiers
- **PeerPush** — listing free, but value is in paid boosts (free tier exists)
- **Vibe-Coding** — FAQ cites payment forms
- **SaaSBison** — free + premium lanes visible, form behind account

## Dead / stale / misrouted (flag for registry cleanup)

- `businesshunt.com` — GoDaddy parked
- `uplyst.app` — parked
- `wonderlaunch.app` — parked
- `ai-pulse.net` — parked for sale
- `cabinetm` — domain redirects to a Canva site
- `feedmyapp` / `launch-llama` / `whatlaunchedtoday`-variants — dropped earlier
- `betapage.co` — redirects to pitchwall.co
- `dododirectory` — submit page has no form (search only)
- `postmake` — no usable form logged-out
- `huzzler` — submit shows auth entry only
- `slant` — "click to reveal" wall only
- `productwatch` — submit routes externally to easylaunch.dev
- `scrolllaunch` — submission ref routes to startupfa.st

## Community surfaces (public posting — hard-stop per contract)

- Product Hunt (personal account only, company accounts banned)
- Hacker News / Show HN (user+pass only; no upvote-begging)
- r/SideProject (use pinned "Not-AI" megathread), r/SaaS
- Indie Hackers (Products DB + community)
- DEV Community (article/comment context)
- Peerlist Launchpad (weekly cohorts, profile required)
- Versily, Bowora, Favors.dev (favor/point economies)

## Vendor portals / heavyweight profiles

- Capterra/GetApp/SoftwareAdvice → `app.g2digitalmarkets.com` shared portal
- G2 → `sell.g2.com` vendor flow
- Trustpilot → `business.trustpilot.com`
- Crunchbase `/add-new` (Turnstile), Dealroom `app.dealroom.co`,
  StartupBlink (demo funnel), Seedtable (magic link), StartupXplore
  (register: fullname/email/social + reCAPTCHA), e27 (LinkedIn OAuth),
  Wellfound (12-char password + Google), SourceForge vendors, SoftwareSuggest,
  SaaSWorthy vendor portal (OTP), TrustRadius, GoodFirms, Tekpon,
  OMR Reviews, Appvizer, ComparaSoftware (reCAPTCHA), Cuspera,
  DiscoverCloud, FinancesOnline (full form + reCAPTCHA + honeypot)

## Cookie-banner gotcha (tooling note)

Sites with JS-routed submit buttons fail silently if a cookie-consent overlay
intercepts clicks (TinyLaunch, StartupInspire). The recon loop now dismisses
"Accept all/Agree" first — real submissions need the same step.

## PlacesToPostYourStartup batch — observed 2026-09-19

61 additional platforms from the public `mmccaff/PlacesToPostYourStartup`
list were field-reconned the same day (websites probed at their submit/login
paths; subreddits share the Reddit flow).

- **Full public forms, no account:** `betabound` (`/announce/` — Centercode
  beta-recruitment board: company/name/email/product/tester requirements/
  incentives/timeframes/test URL; list only when recruiting testers),
  `saasrow` (`/submit` — URL+email only), `microsaasexamples` (`/submit` —
  name/email/URL + paid lanes), `apprater` (`/#submit` — title/platform/
  appUrl/description/tags/imageUrl/submitter fields).
- **Subreddits (17):** share one flow — `/r/<sub>/submit` → login + reCAPTCHA
  when logged out; rules/flair/karma vary per sub. Public posting is a hard
  stop.
- **Editorial/pitch-only** (no self-serve form): alltopstartups, appoid,
  apppicker, appsmamma, appsthunder, arcticstartup, geekwire, inc42,
  killerstartups (`/submit-startup/` renders empty), makeuseof, netted,
  saijogeorge-tools, snapmunk, startup88, startupbeat, tapscape, techpluto.
- **Vendor portals / auth-gated:** getworm (user+pass or Twitter), gust
  (Rails Devise), startupbenchmarks (Google only), startups-gallery
  ("Join for free" modal), websitehunt (Django allauth + Google),
  thetechmap→techmap.me (`/company/create` behind login),
  betatesting (paid service), preapps (agency, $2k–$50k budgets),
  similarsitesearch (login/signup + CAPTCHA), ebool (`/submit` behind
  reCAPTCHA), builtinchicago (Cloudflare challenge), collaborizm (JS wall).
- **Newly dead/stale:** appvita→onk.io, vator→Substack, nextbigwhat→Substack,
  simplelister, stateoftech (both unreachable). All flagged in CSV notes.
- **Rejected candidates (not added):** loopinput, launched.io,
  allstartups.info (unreachable), startuptabs.com (HTTP 500).

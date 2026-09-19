# Platform families — shared codebases, shared playbooks

Observed 2026-09-19 during the BrowserOS field-level sweep. Several registry
platforms run the *same* underlying codebase — identical auth flows, submit
routes, and page structure. Learn the flow once; apply it to every member.
Still verify per-domain (operators can diverge), but expect the pattern.

## Family 1 — "Open-Launch" white-label board

**Members:** `open-launch` `submitmysaas` `firsto` `launchvault` `nextlaunch`
`prolaunch` `fastlaunch` `aura-plusplus` `aat-ee` `openhunts` `startupfast`
`dailypings` (partial matches possible elsewhere — check for the flow)

**Signature:**
- Submit route: `/projects/submit`
- Unauthenticated → `/sign-in?redirect=/projects/submit`
- Sign-in fields: Email + Password + Google + GitHub + **Cloudflare Turnstile**
- Sign-up adds: **Full Name**
- Launch-board layout: daily/weekly leaderboard, badge + dofollow-backlink
  messaging, category filters

**Submission recipe:**
1. Account required — stop for user (Turnstile + likely email verification).
2. With session: `/projects/submit` → project form (fields behind auth —
   UNVERIFIED until first real run).
3. Expect: name, URL, tagline, description, category, logo, screenshots.
4. Confirmation: dashboard entry + public `/projects/<slug>`-style page.

## Family 2 — NextAuth `callbackUrl` SaaS directories

**Members:** `saasfame` `toolfame` `webspot` `aibesttop` `aitoolhunt`
`collectai` `turbo0` `saasgrow` `startuptrusted` `navfolders`

**Signature:**
- `/submit` → `/auth/login?callbackUrl=/submit`
- Login: Email + Password (or magic link) + Google + GitHub OAuth
- Often Cloudflare Turnstile on the auth form
- Pricing page coexists; free listing usually available post-login

**Submission recipe:** account → `/submit` form (fields UNVERIFIED per-domain)
→ dashboard + public product page.

## Family 3 — Django directory form

**Members:** `thesaasdir` `thedevtoolsdir` (byte-identical form)

**Signature:**
- `/submit/` public — no account needed
- Fields: `website_url*` `name*` `tagline*` `description*` `screenshot`
  file, many `categories` checkboxes, `referrer_notes`
- Buttons: **Auto-fill** (URL scrape), **Verify Badge**, **Submit Product**
- Tiers via query param: `?tier=free` | `?tier=paid` ($19) | `?tier=dual` ($29)
- Hidden `csrfmiddlewaretoken` + `form_token`

**Submission recipe:** fetch → Auto-fill → complete fields → select free tier
→ Submit Product. Badge verification offered — check whether free tier
requires the badge on your site before submitting.

## Family 4 — Multi-step tool form

**Members:** `deeplaunch` `tooldirs` (same operator)

**Signature:**
- `/submit` public multi-step wizard
- Fields: url, name, tagline, description (500–5000 chars, markdown),
  file uploads ×2, category select, pricing model, platforms, year,
  `discountCode`, `youtubeUrl`, `githubUrl`, `founderTwitter`,
  `affiliateUrl`, `email*`
- "Next" paginates; optional Sign In for managed listings

**Submission recipe:** fill page 1 → Next → details page → submit. The long
description field (500+ chars) is the main prep item — have the long-form
description ready.

## Family 5 — Google-only auth

**Members:** `launchclash` `shinylaunch` `mylaunchstash` `acid-tools`
`noonlaunch` (Google sole provider observed)

**Note:** no email/password option — submission requires a Google account in
the browser session. Hard-stop for account linking.

## Non-family patterns worth knowing

- **Magic-link-only:** TinyLaunch, Seedtable, Dang.ai, Favors.dev, Peerlist —
  email field → inbox link. The user owns the inbox: hard-stop.
- **LinkedIn-only auth:** e27 (company profiles).
- **Shared vendor portal:** Capterra/GetApp/SoftwareAdvice →
  `app.g2digitalmarkets.com` (Gartner Digital Markets).
- **Cookie-banner trap:** JS submit buttons are swallowed by consent overlays
  (TinyLaunch, StartupInspire). Always dismiss "Accept" first.
- **External redirect:** ProductWatch → easylaunch.dev; ScrollLaunch →
  startupfa.st; ProductHunt-adjacent widgets on white-label boards.

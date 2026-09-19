# Prompt: field-level platform recon

Paste this at your agent when a playbook is still `UNVERIFIED` or stale.

```text
Do field-level recon on these platforms: <slug list or "all UNVERIFIED">

For each platform, in the user's browser (BrowserOS/neo — real sessions):

1. Start at the registry URL in platforms/platforms.csv.
2. Find the real entry points: Register / Sign up / Sign in / Submit /
   Add product / List your tool / Get listed. Match on the link's href path,
   not its text (brand names contain "launch").
3. Navigate to the submit/listing path. If it redirects to login, record the
   redirect URL and inspect the auth form instead.
4. Record in the playbook under a dated "### … — observed YYYY-MM-DD" heading:
   - visible field names + required markers
   - OAuth providers offered
   - CAPTCHA type (Turnstile / reCAPTCHA / hCaptcha / math / none)
   - pricing lanes + exact prices shown
   - backlink/badge requirements
   - multi-step behavior, external redirects, dead/parked domains
   - shared-codebase family if it matches docs/platform-families.md
5. Dismiss cookie-consent overlays BEFORE clicking JS buttons — overlays
   silently swallow clicks (TinyLaunch proved this).
6. Append findings to docs/recon-notes.md if the platform reveals a new
   pattern (new family member, new blocker type).

HARD STOPS — never do any of these:
- create an account or fill credentials
- solve a CAPTCHA / email verification
- pay, accept terms, or post publicly
- submit a product form

Work in batches of 3–5, report after each batch. If a form is unreachable
unauthenticated, mark it UNVERIFIED with the observed blocker — do not guess
the fields.
```

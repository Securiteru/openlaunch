#!/usr/bin/env python3
"""Verify a live listing — the only acceptable evidence for `live` status.

A listing counts as `live` only when its public URL loads and the product is
visible on the page. This script makes that check executable and repeatable:

    python3 scripts/verify.py <listing_url> <product_name>

Exit 0 + prints PASS only when the page loads (2xx) and the product name
appears in the rendered HTML. Anything else prints FAIL — record the listing
as `pending-review` or keep digging; never mark `live` on inference.

Optional: pass --save-evidence to write a timestamped copy of the fetched page
under tracker/evidence/ for the record.
"""
import argparse
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_DIR = ROOT / "tracker" / "evidence"
UA = "openlaunch-verify/1.0 (+https://github.com/Securiteru/openlaunch)"
TIMEOUT = 20


def fetch(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return r.status, r.read().decode("utf-8", errors="replace")


def visible_text(html: str) -> str:
    html = re.sub(r"<(script|style|noscript)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    return re.sub(r"<[^>]+>", " ", html)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url")
    ap.add_argument("name", help="product name expected on the page")
    ap.add_argument("--save-evidence", action="store_true")
    args = ap.parse_args()

    try:
        status, html = fetch(args.url)
    except Exception as e:  # noqa: BLE001 — report, never guess
        print(f"FAIL {args.url} — fetch error: {e}")
        return 1

    if status >= 400:
        print(f"FAIL {args.url} — HTTP {status}")
        return 1

    found = args.name.lower() in visible_text(html).lower()
    if not found:
        print(f"FAIL {args.url} — HTTP {status} but '{args.name}' not found on page")
        return 1

    print(f"PASS {args.url} — HTTP {status}, '{args.name}' visible")
    if args.save_evidence:
        EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
        slug = re.sub(r"[^a-z0-9]+", "-", args.url.lower()).strip("-")[:80]
        ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        out = EVIDENCE_DIR / f"{ts}-{slug}.html"
        out.write_text(html, encoding="utf-8")
        print(f"evidence saved: {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

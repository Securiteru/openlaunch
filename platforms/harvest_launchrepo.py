#!/usr/bin/env python3
"""Harvest LaunchRepo's public field guides into our playbooks.

Fetches https://launchrepo.dev/directories/<slug>/ for each mapped profile,
extracts the observed facts (entry URL, preparation, workflow, hurdles,
confirmation signal, observation date) and appends them to the matching
playbook under "## Field observations" — verbatim facts only, with source
attribution. Never overwrites an existing observations section.

Usage: python3 platforms/harvest_launchrepo.py [--dry-run]
"""
import re
import sys
import time
import urllib.request
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAYBOOK_DIR = ROOT / "platforms" / "playbooks"

# (launchrepo_slug, our_slug)
PROFILES = [
    ("betalist", "betalist"), ("comingup", "comingup"),
    ("dailypings", "dailypings"), ("devhunt", "devhunt"),
    ("fazier", "fazier"), ("huzzler", "huzzler"),
    ("indiehunt", "indiehunt"), ("launchboard", "launchboard"),
    ("launchigniter", "launchigniter"), ("microlaunch", "microlaunch"),
    ("nicklaunches", "nicklaunches"), ("peerpush", "peerpush"),
    ("pitchwall", "pitchwall"), ("producthunt", "producthunt"),
    ("promoteproject", "promoteproject"), ("sideprojectors", "sideprojectors"),
    ("smollaunch", "smollaunch"), ("startupbase", "startupbase"),
    ("startuptrusted", "startuptrusted"), ("submithunt", "submithunt"),
    ("tinystartups", "tinystartups"), ("tinylaunch", "tinylaunch"),
    ("uneed", "uneed"),
    ("aiagentsdirectory", "ai-agents-directory"),
    ("aihuntlist", "aihuntlist"), ("aitoolhunt", "aitoolhunt"),
    ("futuretools", "futuretools"), ("futurepedia", "futurepedia"),
    ("goodaitools", "goodaitools"), ("stork", "stork"),
    ("submitaitools", "submitaitools"),
    ("theresanaiforthat", "theresanaiforthat"), ("toolify", "toolify"),
    ("toolpilot", "toolpilot"),
    ("alternativeto", "alternativeto"), ("apprater", "apprater"),
    ("collectai-tools", "collectai"), ("findly-tools", "findly-tools"),
    ("saasbrowser", "saas-browser"), ("saashub", "saashub"),
    ("thedevtoolsdir", "thedevtoolsdir"), ("tooldirs", "tooldirs"),
    ("uno-directory", "uno-directory"),
    ("capterra", "capterra"), ("financesonline", "financesonline"),
    ("g2", "g2"), ("goodfirms", "goodfirms"), ("omr", "omr-reviews"),
    ("saasworthy", "saasworthy"), ("softwaresuggest", "softwaresuggest"),
    ("sourceforge", "sourceforge"), ("tekpon", "tekpon"),
    ("trustradius", "trustradius"),
    ("crunchbase", "crunchbase"), ("dealroom", "dealroom"),
    ("e27", "e27"), ("eu-startups", "eu-startups"),
    ("startupblink", "startupblink"), ("trustpilot", "trustpilot"),
    ("wellfound", "wellfound"),
    ("hackernews", "hacker-news"), ("indiehackers", "indie-hackers"),
    ("peerlist", "peerlist"), ("reddit-saas", "reddit-saas"),
    ("reddit-sideproject", "reddit-sideproject"), ("stackshare", "stackshare"),
]


PROFILE_SECTIONS = ("Who lists here", "What to prepare",
                    "What \u201clive\u201d means here", "Worth knowing")

STOP_HEADINGS = ("Other platforms", "Lists this platform", "Give your agent",
                 "Related pages", "Explore where", "Let your agent",
                 "Sponsors", "Your product here")


def _strip(html_seg):
    seg = re.sub(r'<h[1-6][^>]*>', '\n### ', html_seg)
    seg = re.sub(r'</h[1-6]>', '\n', seg)
    seg = re.sub(r'<(p|li|br|div|section|ul|ol)[^>]*>', '\n', seg)
    seg = re.sub(r'<[^>]+>', '', seg)
    seg = unescape(seg)
    seg = re.sub(r'[ \t]+\n', '\n', seg)
    return re.sub(r'\n{3,}', '\n\n', seg).strip()


def extract(html):
    """Return (body_text, entry_url, kind) for either page format.

    Field guides end the body at 'Official platform entry'.
    Profiles end at the first boilerplate h2 and use 'Official site:' links.
    """
    guide = 'Official platform entry' in html
    em = re.search(
        r'<a[^>]+href="([^"]+)"[^>]*>[^<]*'
        r'(?:Official platform entry|Official site)[^<]*</a>', html)
    entry = em.group(1) if em else None

    m = re.search(r'</h1>(.*)', html, re.S)
    if not m:
        return None, entry, None
    seg = m.group(1)
    if guide:
        seg = seg.split('Official platform entry')[0]
    else:
        cut = len(seg)
        for s in STOP_HEADINGS:
            i = seg.find(s)
            if 0 < i < cut:
                cut = i
        seg = seg[:cut]
    body = _strip(seg)
    return (body or None), entry, ("guide" if guide else "profile")


SECTIONS = ("Preparation", "Workflow", "Watch for", "What counts as confirmation")


def format_block(body, entry, lr_slug):
    date = re.search(r"Observed:\s*([0-9-]+)", body)
    for s in SECTIONS:
        body = re.sub(rf"^{re.escape(s)}$", f"### {s}", body, flags=re.M)
    return (
        "\n## Field observations\n"
        f"Source: LaunchRepo public field guide "
        f"(https://launchrepo.dev/directories/{lr_slug}/), "
        f"observed {date.group(1) if date else 'unknown'}.\n\n"
        + body + "\n"
        + (f"\nSubmission entry: {entry}\n" if entry else "")
    )


def main():
    dry = "--dry-run" in sys.argv
    done = skipped = failed = 0
    for lr_slug, slug in PROFILES:
        pb = PLAYBOOK_DIR / f"{slug}.md"
        if not pb.exists():
            print(f"!! no playbook {slug}")
            failed += 1
            continue
        if "## Field observations" in pb.read_text():
            skipped += 1
            continue
        url = f"https://launchrepo.dev/directories/{lr_slug}/"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            html = urllib.request.urlopen(req, timeout=15).read().decode()
        except Exception as e:
            print(f"!! fetch {lr_slug}: {e}")
            failed += 1
            continue
        body, entry, kind = extract(html)
        if not body:
            print(f"!! parse {lr_slug}")
            failed += 1
            continue
        if not dry:
            with pb.open("a") as f:
                f.write(format_block(body, entry, lr_slug))
        print(f"++ {slug} [{kind}] (entry: {entry})" if entry
              else f"++ {slug} [{kind}]")
        done += 1
        time.sleep(0.4)
    print(f"\nharvested {done}, already-done {skipped}, failed {failed}")


if __name__ == "__main__":
    main()

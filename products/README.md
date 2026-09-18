# Products

One directory per product you launch:

```
products/<slug>/
  brief.md     # copy from brief/product-brief.template.md — required
  assets/      # logo, screenshots referenced by the brief
  evidence/    # screenshots/confirmations the agent saves per docs/evidence.md
  notes.md     # optional running notes
```

The slug becomes the tracker key (`tracker/data.json` → `product`) and is
reused in listing URLs, so keep it lowercase and URL-safe.

**Privacy:** briefs may contain unreleased product details. This repo is
public — either keep briefs out of git (see `.gitignore`), or run your
launch work in a private fork and PR back only playbook improvements.

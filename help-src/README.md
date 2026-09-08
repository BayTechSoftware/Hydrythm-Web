# help-src — the source of coraiq.tech/help

⛔ **`help/*.html` is GENERATED. Never hand-edit it.** Edit the Markdown here and run:

```
python3 build_help.py --self-test    # reports its own count, run this first
python3 build_help.py                # writes help/*.html + help/help.css
python3 build_help.py --check        # non-zero if the output is stale
```

## Frontmatter

Every page opens with:

```
---
title: Editing your dashboard
description: One sentence. It becomes the meta description and the OG description.
section: Cora Mobile        # "Cora Mobile" | "Cora Max" | "Help" | "-" for the index
order: 4                    # position within the section, in the sidebar
---
```

## Markdown supported

Headings (`##`–`####`), paragraphs, lists, tables, fenced code, blockquotes, `---`,
links, images, `**bold**`, `*italic*`, `` `code` `` — plus three callouts:

```
:::note Optional title
body
:::
```

`:::note` (blue) · `:::warning` (amber) · `:::tip` (teal)

Images are `![alt](img/name.webp "optional caption")`. Width and height are read off
the real file at build time. **A slot with no file behind it renders as a labelled
placeholder**, never a broken image, and the build prints what is still missing.
Images taller than 1.4× their width are treated as phone screenshots and capped.

## Rules this guide is written under

- **Cora Mobile** and **Cora Max** — never "the app", "the kiosk", "the tablet", "E10".
  The on-device icon is labelled **Cora**, which the setup page says once on purpose.
- **Cora Assistant** and **Cora Cloud** — no third-party infrastructure is ever named.
- Nothing about Flo, Senso, Specto, Cora Cube, Cora Base, Cora Pro or Cora Link.
- Integrations named: Neptune Apex, Red Sea ReefBeat, Jecod/Jebao, AquaWiz KH Controller.
  Maxspect is "coming soon" — ⛔ ENFORCED by the self-test: any page naming Maxspect must
  also carry "coming soon". This rule sat here unenforced and six pages broke it.
- ⛔⛔ **Both GIZ-14 disclaimers appear in the shared footer of every page.** They are in
  `build_help.py`; do not paraphrase them and do not drop one.
- Screenshots must not show: the Devices tab's Flo / Senso / Specto family headers, any
  real email address, or any `ReefIQ-` prefixed device id. `mobile-devices.webp` and
  `mobile-settings.webp` are cropped for exactly this reason — see the comments in the
  capture step of the session that made them.

## Publishing (currently unlisted)

The guide is live-but-quiet: `NOINDEX = True` in `build_help.py`, `Disallow: /help/`
in `robots.txt`, no sitemap entries, and nothing on the site links to it.

To publish: set `NOINDEX = False`, remove the `robots.txt` line, add every page URL to
`sitemap.xml` (generate the list, do not hand-count — a number written here goes stale silently), rebuild, and add a link from the main nav. One commit.

## Version stamp

`STAMP_MAX` / `STAMP_MOBILE` in `build_help.py` print at the foot of every page. Bump
them when the guide is re-checked against a newer build — a guide that does not say
which version it describes goes stale invisibly.

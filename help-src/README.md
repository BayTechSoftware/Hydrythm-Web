# help-src: the source of coraiq.tech/help

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
links, images, `**bold**`, `*italic*`, `` `code` ``, plus three callouts:

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

- **Cora Mobile** and **Cora Max**: never "the app", "the kiosk", "the tablet", "E10".
  The on-device icon is labelled **Cora**, which the setup page says once on purpose.
- **Cora Assistant** and **Cora Cloud**: no third-party infrastructure is ever named.
- Nothing about Flo, Senso, Specto, Cora Cube, Cora Base, Cora Pro or Cora Link.
- Integrations named: Neptune Apex, Red Sea ReefBeat, Jecod/Jebao, AquaWiz KH Controller.
  Maxspect is **beta** (owner, 2026-09-17: still in testing and development; it was "coming
  soon" until then). ⛔ ENFORCED by the self-test: any page naming Maxspect must also carry
  "beta", and no line may call Maxspect "coming soon". The old rule sat here unenforced once
  and six pages broke it.
- ⛔⛔ **Both GIZ-14 disclaimers appear in the shared footer of every page.** They are in
  `build_help.py`; do not paraphrase them and do not drop one.
- Screenshots must not show: the Devices tab's Flo / Senso / Specto family headers, any
  real email address, or any `ReefIQ-` prefixed device id. `mobile-devices.webp` and
  `mobile-settings.webp` are cropped for exactly this reason; see the comments in the
  capture step of the session that made them.

## Published (2026-09-17)

The guide is public: `NOINDEX = False` in `build_help.py`, no `Disallow: /help/` in
`robots.txt`, every page in `sitemap.xml`, and a **Help** link in the nav of all five
site pages. ⛔ A NEW page also needs its `sitemap.xml` entry; the self-test refuses a
page that is missing. Generate entries from the pages' canonical URLs, never by hand.
To hide the guide again: `NOINDEX = True`, restore the `robots.txt` line, and remove the
sitemap entries, in one commit.

## Translations

The guide publishes in English plus six languages: German (`de`), French (`fr`),
Turkish (`tr`), Italian (`it`), Spanish (`es`), Polish (`pl`).

**Where files go.** English is `help-src/*.md` → `/help/...`. Each other language is a
mirror tree, `help-src/<lang>/*.md` → `/<lang>/help/...` — for example
`help-src/de/mobile-setup.md` becomes `/de/help/mobile-setup`. A translated file must
have the **same filename** as its English counterpart, and the **same frontmatter
keys**. `title:` and `description:` are translated. **`section:`, `order:`, and
`group:` are copied EXACTLY as the English file has them, never translated** — the
sidebar's structure and grouping are matched across languages by those literal
strings, and translating one silently drops the page into the wrong place, or out of
the nav entirely (the same guard that catches an unknown `section:` in English also
runs against every language). The English label shown in the sidebar for a `section`/
`group` value comes from a small translation table in `build_help.py`
(`UI_STRINGS[lang]["sections"|"groups"]`), not from the frontmatter.

**A missing page is not an error.** If a language's translator has not gotten to a
page yet, that `.md` file simply does not exist in `help-src/<lang>/`, and the build
does not produce that page for that language — it is skipped, not blocked. Every
place the guide would otherwise link to it instead links to that language's help
index (`/<lang>/help/`), so there is never a dead link.

**Links.** Write links exactly the way the English source does —
`/help/<slug>`, `/help/<slug>#anchor`, or `/help/` for the index. The build rewrites
these to `/<lang>/help/...` for you. Do **not** write `/de/help/...` etc. by hand.
An `#anchor` is dropped (the link still goes to the right page, just not to that
spot) if the translated target page does not have a heading that slugifies to it —
headings are re-slugified from the TRANSLATED text, so a copied English anchor is not
guaranteed to exist once a heading is translated. Links to `/support.html` and the
legal pages, and any external URL, are left exactly as written — those pages stay
English (owner decision). Images (`img/name.webp`) are shared across every language;
do not create per-language copies.

**Adding an eighth language.** Add its code to `LANGS` in `build_help.py`, add a
`NATIVE_NAMES` entry, and add a full `UI_STRINGS` entry (every key the English one
has — the self-test refuses a language with a key missing, and refuses an em dash in
any UI string). Then create `help-src/<code>/` and start translating; nothing else
needs to know the language exists ahead of time.

## Version stamp

`STAMP_MAX` / `STAMP_MOBILE` in `build_help.py` print at the foot of every page. Bump
them when the guide is re-checked against a newer build; a guide that does not say
which version it describes goes stale invisibly.

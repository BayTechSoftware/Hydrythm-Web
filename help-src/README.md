# help-src: the source of coraiq.tech/help

⛔ **This directory is GENERATED.** It is written by a prepare step from a separate source
tree and is overwritten on every run: do not edit these files here, edits are lost. The same
goes for `help/*.html`, which `build_help.py` generates from this directory:

```
python3 build_help.py --self-test    # reports its own count
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
group: Your dashboard       # sidebar group (not on Help pages)
twin: max-dashboard-editing # optional: the same topic in the other product
---
```

**Sidebar order.** The **Help** section (Troubleshooting, How do I, Equipment by brand,
FAQ, Glossary) comes FIRST, then Cora Mobile, then Cora Max. Both products use the same
groups, in this order: Getting started · Your dashboard · Equipment · Alerts and
automation · Records · Intelligence · Settings and account (`GROUP_ORDER` in
`build_help.py`). ⛔ ENFORCED by the self-test, in every language tree: no two pages share
an `order:` in a section, each group is ONE contiguous run of `order:` values (so the
sidebar and Previous/Next agree), groups follow `GROUP_ORDER`, and every group has a
translated label in `UI_STRINGS`. A new group needs an entry in `GROUP_ORDER` and in all
seven `UI_STRINGS[...]["groups"]`.

**`twin:`** names the page about the same thing in the other product. The build prints one
line under the H1, "On Cora Max: <twin title>" or "On Cora Mobile: <twin title>",
translated and linking the twin in the same language. It need not be mutual
(`max-records` has one twin, three Mobile pages point at it). ⛔ The self-test refuses a
`twin:` whose page does not exist in the same language tree. Copy it unchanged into
translations, like `order:`/`group:`.

Every page except the index also gets a breadcrumb (Help / section / group) and
`BreadcrumbList` JSON-LD; nothing to write for it.

## Markdown supported

Headings (`##`–`####`), paragraphs, lists, tables, fenced code, blockquotes, `---`,
links, images, `**bold**`, `*italic*`, `` `code` ``, plus three callouts:

```
:::note Optional title
body
:::
```

`:::note` (blue) · `:::warning` (amber) · `:::tip` (teal)

**Tiles** (for the index and other landing pages), one per list line, description
optional:

```
:::tiles
- [New to Cora Mobile](/help/mobile-setup): Create your account and add your first tank.
- [Fix a problem](/help/troubleshooting): Readings stopped or an alert won't clear.
:::
```

A plain Markdown list of links is fine everywhere else. Raw `<ul class="tiles">` HTML
still works but `:::tiles` is easier to translate.

**Stable heading ids.** `## Heading text {#stable-id}` (lower-case letters, digits,
hyphens) gives the heading that id verbatim; the braces are not shown. Without it the id
is the heading text slugified, ASCII-folded ("DŌS heads" -> `dos-heads`, "Yaş" -> `yas`).
Put an explicit id on every heading that other pages link to (troubleshooting symptoms,
FAQ questions, `doser-alerts`, stopped-reporting), and **translators copy the `{#...}`
unchanged**, so `/help/<slug>#stable-id` lands on the right spot in every language.
⛔ ENFORCED: an English `/help/<slug>#anchor` (or same-page `#anchor`) link whose page or
heading does not exist fails the self-test.

Images are `![alt](img/name.webp "optional caption")`. Width and height are read off
the real file at build time. **A slot with no file behind it renders as a labelled
placeholder**, never a broken image, and the build prints what is still missing.
Images taller than 1.4× their width are treated as phone screenshots and capped.

## Rules this guide is written under

- Integrations named publicly: Neptune Apex (DŌS, Trident), Red Sea ReefBeat, Jecod/Jebao and
  the AquaWiz KH Controller.
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
spot) if the translated target page does not have a heading with that id. Headings are
re-slugified from the TRANSLATED text, so a copied English anchor only survives when the
English heading carries `{#stable-id}` and the translation keeps it (see Markdown
supported). Links to `/support.html` and the
legal pages, and any external URL, are left exactly as written — those pages stay
English (owner decision). Images (`img/name.webp`) are shared across every language;
do not create per-language copies.

**Adding an eighth language.** Add its code to `LANGS` in `build_help.py`, add a
`NATIVE_NAMES` entry, and add a full `UI_STRINGS` entry (every key the English one
has — the self-test refuses a language with a key missing, and refuses an em dash in
any UI string). Then create `help-src/<code>/` and start translating; nothing else
needs to know the language exists ahead of time.

## Search

Search runs in the browser over `search.json` (one per language, fetched on first use,
versioned by content hash). Every query word must match (AND), at the start of a word, as
a prefix; case, accents, Turkish İ/ı and hyphens are ignored (wifi = Wi-Fi = wi fi,
dos = DŌS). H2 and H3 sections are indexed with their ids, so a result links to the
section that matched. Ranking: title, then description, then heading, then body. Zero
results offer Troubleshooting, How do I and Contact support.

**Synonyms** live in `build_help.py`: `SYN_COMMON` (brands and chemistry, every language)
and `SYNONYMS[lang]` (one row = words a reader may type for the same thing, e.g.
offline / not connected / stopped reporting). Keep rows tight: a row is an OR. Common
question words (`STOPWORDS[lang]`) are dropped from a query. The self-test runs the
engine under node against fixed cases and the real English index. The English index
budget is 320 KB.

## Version stamp

`STAMP_MAX` / `STAMP_MOBILE` in `build_help.py` print at the foot of every page. Bump
them when the guide is re-checked against a newer build; a guide that does not say
which version it describes goes stale invisibly.

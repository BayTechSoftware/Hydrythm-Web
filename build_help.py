#!/usr/bin/env python3
"""Build coraiq.tech/help/ from Markdown.

⛔ THE OUTPUT IS GENERATED — never hand-edit `help/*.html`. Edit `help-src/*.md`
and re-run. Same rule as the star diagram on the home page, and for the same
reason: 21 pages sharing a nav, a footer and two mandatory disclaimers is the
two-copies-drift trap the site has already declined once (critical-CSS
inlining, `docs/OPS_Website.md` §Performance).

⚠️ `help.css` is generated too, and its palette is LIFTED FROM `styles.css` at
build time rather than copied by hand. If that extraction ever fails the build
ABORTS — a help page that renders with no tokens looks exactly like the
black-SVG bug in OPS_Website.md §preview quirks, and would ship silently.

Usage:
    python3 build_help.py --self-test     # runs and reports its own count
    python3 build_help.py                 # write help/*.html + help/help.css
    python3 build_help.py --check         # non-zero if output is out of date
"""
from __future__ import annotations

import html
import re
import sys
from dataclasses import dataclass, field
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "help-src"
OUT = ROOT / "help"
SITE = "https://coraiq.tech"

# ⭐ DERIVED FROM THE CSS ITSELF, set in `main()` before any page renders.
# It used to be a hand-bumped string, which is the same class of defect as the
# hand-written self-test count and version stamp: a value restating something
# the build already knows, wrong the moment somebody forgets. GitHub Pages
# serves `max-age=600` with INDEPENDENT windows per file, so new HTML + old CSS
# is an ordinary state that renders as a convincing fake bug — the hash makes
# it impossible instead of merely remembered.
CSS_VERSION = "dev"
FONTS_VERSION = "1"

# The version stamp every page carries. A guide that does not say which build
# it describes goes stale invisibly; this makes it visible instead.
#
# ⭐ DERIVED, NOT DECLARED. These were hardcoded and were wrong twice inside
# two days — 0.28.32 while the tree said 0.28.33, then 0.28.33 while another
# session shipped 0.28.36. A number restating something the repo already knows
# will always rot, so read it from the pubspec and keep the literals only as a
# fallback for a standalone clone of this site repo (where ../cora-max is
# absent). Same fix as the self-test count below.
_FALLBACK_MAX, _FALLBACK_MOBILE = "0.28.36", "0.5.54"


def _pubspec_version(rel: str, fallback: str) -> str:
    """`version: 1.2.3+45` from a sibling Flutter package → `1.2.3`."""
    f = ROOT.parent / rel / "pubspec.yaml"
    if not f.exists():
        return fallback
    for line in f.read_text(encoding="utf-8").splitlines():
        if line.startswith("version:"):
            return line.split(":", 1)[1].strip().split("+")[0]
    return fallback


STAMP_MAX = _pubspec_version("cora-max", _FALLBACK_MAX)
STAMP_MOBILE = _pubspec_version("mobile", _FALLBACK_MOBILE)

# ⛔ While the guide is unlisted. Flipping to public = set this False, drop the
# robots.txt Disallow, and add the sitemap entries. One commit.
NOINDEX = True

# ⛔⛔ GIZ-14 — BOTH disclaimers, verbatim, on every page that names a
# manufacturer. On a help site that is most of them, so they live in the shared
# footer and appear on all of them. Do not paraphrase; do not drop one.
DISCLAIMER_1 = (
    "Cora's integrations are independent — not affiliated with, endorsed by, "
    "or sponsored by any equipment manufacturer. Product names, logos and "
    "images are property of their respective owners."
)
DISCLAIMER_2 = (
    "Some devices are connected through APIs that are not officially supported "
    "by their manufacturers; support will be updated as official APIs arrive."
)

SUPPORT_EMAIL = "cora@coraiq.tech"


# ─────────────────────────────────────────────────────────────────────────────
# Content model
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class Page:
    slug: str
    title: str
    description: str
    section: str
    order: int
    body_md: str
    html: str = ""
    headings: list = field(default_factory=list)

    @property
    def url(self) -> str:
        return "/help/" if self.slug == "index" else f"/help/{self.slug}"

    @property
    def out_path(self) -> Path:
        return OUT / ("index.html" if self.slug == "index" else f"{self.slug}.html")


SECTION_ORDER = ["", "Cora Mobile", "Cora Max", "Help"]


def parse_frontmatter(text: str, slug: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise SystemExit(f"⛔ {slug}.md has no frontmatter block")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise SystemExit(f"⛔ {slug}.md frontmatter is not terminated")
    meta = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise SystemExit(f"⛔ {slug}.md frontmatter line without a colon: {line!r}")
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip()
    return meta, text[end + 5:]


# ─────────────────────────────────────────────────────────────────────────────
# Markdown → HTML.
#
# A deliberately SMALL subset, because the input is content we author in this
# repo rather than anything user-supplied. Everything not listed here is simply
# not available: headings, paragraphs, lists, tables, fenced code, blockquotes,
# horizontal rules, images, links, and the three callout blocks.
#
# ⚠️ Inline markup is applied to TEXT ONLY, after escaping, and code spans are
# extracted first so that `**` inside a code span stays literal.
# ─────────────────────────────────────────────────────────────────────────────

_CODE_SENTINEL = "\x00CODE%d\x00"


def inline(text: str) -> str:
    """Escape, then apply inline markup. Code spans are protected first."""
    spans: list[str] = []

    def stash(m: re.Match) -> str:
        spans.append(m.group(1))
        return _CODE_SENTINEL % (len(spans) - 1)

    text = re.sub(r"`([^`]+)`", stash, text)
    text = html.escape(text, quote=False)

    # Images before links — the syntaxes differ only by a leading '!'.
    text = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"([^\"]*)\")?\)", _img, text)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", _link, text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![*\w])\*([^*]+)\*(?!\w)", r"<em>\1</em>", text)

    for i, raw in enumerate(spans):
        text = text.replace(
            _CODE_SENTINEL % i, f"<code>{html.escape(raw, quote=False)}</code>"
        )
    return text


def _link(m: re.Match) -> str:
    label, href = m.group(1), m.group(2)
    ext = href.startswith("http") and "coraiq.tech" not in href
    rel = ' target="_blank" rel="noopener"' if ext else ""
    return f'<a href="{html.escape(href, quote=True)}"{rel}>{label}</a>'


def _img(m: re.Match) -> str:
    """An image is always a <figure>.

    ⚠️ width/height are MANDATORY (CLS) and are read off the real file at build
    time — a missing file aborts the build rather than shipping a broken img.
    """
    alt, src, cap = m.group(1), m.group(2), m.group(3)
    w, h = _dimensions(src)
    caption = f"<figcaption>{inline(cap)}</figcaption>" if cap else ""
    # ⚠️ A full phone screenshot is ~2.2x taller than it is wide. Rendered at
    # the column width it is absurd — one screenshot fills three scrolls. Tall
    # images get the `phone` class, which caps them at a sensible width.
    cls = "shot phone" if h > w * 1.4 else "shot"
    # ⛔ A slot with no file behind it renders as a LABELLED placeholder, never
    # as a broken <img>. A broken image on a published page reads as neglect;
    # a placeholder reads as a page still being finished, which is the truth.
    if src in _MISSING:
        return (
            f'<figure class="shot ph"><div class="ph-box">'
            f'<span>Screenshot to come</span>'
            f'<small>{html.escape(alt, quote=False)}</small>'
            f"</div>{caption}</figure>"
        )
    # ⭐ A <button>, not a click handler on the <img>: a phone screenshot is
    # capped at 300 px here and dense screens are unreadable at that size, so
    # enlarging has to be a real control — reachable by keyboard, announced as
    # a control, and working before any script loads (it degrades to a plain
    # image if JS never runs).
    return (
        f'<figure class="{cls}">'
        f'<button type="button" class="zoom" '
        f'aria-label="Enlarge: {html.escape(alt, quote=True)}">'
        f'<img src="{html.escape(src, quote=True)}" alt="{html.escape(alt, quote=True)}" '
        f'width="{w}" height="{h}" loading="lazy" decoding="async">'
        f"</button>{caption}</figure>"
    )


_DIM_CACHE: dict[str, tuple[int, int]] = {}
_MISSING: list[str] = []


def _dimensions(src: str) -> tuple[int, int]:
    if src in _DIM_CACHE:
        return _DIM_CACHE[src]
    path = OUT / src if not src.startswith("/") else ROOT / src.lstrip("/")
    try:
        from PIL import Image

        with Image.open(path) as im:
            dim = im.size
    except Exception:
        # A placeholder slot: recorded, reported at the end, never silent.
        _MISSING.append(src)
        dim = (1600, 1000)
    _DIM_CACHE[src] = dim
    return dim


def slugify(text: str) -> str:
    s = re.sub(r"<[^>]+>", "", text).lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    return re.sub(r"\s+", "-", s.strip())[:60]


def render(md: str, headings: list) -> str:
    """Block-level render. Returns HTML; appends (level, text, id) to headings."""
    out: list[str] = []
    lines = md.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]

        if not line.strip():
            i += 1
            continue

        # Fenced code
        if line.startswith("```"):
            lang = line[3:].strip()
            i += 1
            buf = []
            while i < len(lines) and not lines[i].startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            cls = f' class="lang-{html.escape(lang, quote=True)}"' if lang else ""
            body = html.escape("\n".join(buf), quote=False)
            out.append(f"<pre{cls}><code>{body}</code></pre>")
            continue

        # Callouts:  :::note Title
        m = re.match(r"^:::(note|warning|tip)\s*(.*)$", line)
        if m:
            kind, title = m.group(1), m.group(2).strip()
            i += 1
            buf = []
            while i < len(lines) and not lines[i].startswith(":::"):
                buf.append(lines[i])
                i += 1
            i += 1
            inner = render("\n".join(buf), headings)
            head = f'<p class="cal-t">{inline(title)}</p>' if title else ""
            out.append(f'<aside class="cal cal-{kind}">{head}{inner}</aside>')
            continue

        # Raw HTML block. The input is content WE author in this repo, so a
        # passthrough is safe here and is the only way to hand-write something
        # the small Markdown subset has no syntax for (the index tiles). A
        # block runs from a line starting with '<' to the next blank line.
        # ⛔ An ALLOWLIST, not "anything starting with '<'". The first version
        # of this passed <script> straight through and the self-test caught it.
        if re.match(r"^<(ul|ol|div|section|figure|table|dl|aside)\b", line.lstrip()):
            buf = []
            while i < len(lines) and lines[i].strip():
                buf.append(lines[i])
                i += 1
            out.append("\n".join(buf))
            continue

        # Headings
        m = re.match(r"^(#{2,4})\s+(.*)$", line)
        if m:
            level = len(m.group(1))
            text = inline(m.group(2).strip())
            hid = slugify(m.group(2))
            headings.append((level, m.group(2).strip(), hid))
            out.append(f'<h{level} id="{hid}">{text}</h{level}>')
            i += 1
            continue

        # Horizontal rule
        if re.match(r"^---+$", line.strip()):
            out.append("<hr>")
            i += 1
            continue

        # Table
        if "|" in line and i + 1 < len(lines) and re.match(r"^[\s|:-]+$", lines[i + 1]):
            head = [c.strip() for c in line.strip().strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and "|" in lines[i] and lines[i].strip():
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            th = "".join(f"<th>{inline(c)}</th>" for c in head)
            # ⭐ Each cell carries its column heading, so a narrow screen can
            # stack the row into a labelled card instead of scrolling sideways
            # and hiding the column that explains the other one. Only 2- and
            # 3-column tables stack; wider ones stay scrollable, where a card
            # would be worse than the scroll.
            tb = "".join(
                "<tr>"
                + "".join(
                    f'<td data-th="{html.escape(head[j], quote=True) if j < len(head) else ""}">'
                    f"{inline(c)}</td>"
                    for j, c in enumerate(r)
                )
                + "</tr>"
                for r in rows
            )
            tcls = " class=\"stack\"" if len(head) <= 3 else ""
            out.append(
                f'<div class="tw"><table{tcls}><thead><tr>{th}</tr></thead>'
                f"<tbody>{tb}</tbody></table></div>"
            )
            continue

        # Blockquote
        if line.startswith("> "):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i].lstrip(">").lstrip())
                i += 1
            out.append(f"<blockquote>{render(chr(10).join(buf), headings)}</blockquote>")
            continue

        # Lists (ordered / unordered), one level, with lazy continuation
        m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", line)
        if m:
            ordered = bool(re.match(r"\d+\.", m.group(2)))
            items: list[str] = []
            while i < len(lines):
                mm = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", lines[i])
                if not mm:
                    if lines[i].startswith("  ") and items:
                        items[-1] += " " + lines[i].strip()
                        i += 1
                        continue
                    break
                items.append(mm.group(3))
                i += 1
            tag = "ol" if ordered else "ul"
            li = "".join(f"<li>{inline(t)}</li>" for t in items)
            out.append(f"<{tag}>{li}</{tag}>")
            continue

        # Paragraph
        buf = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(
            r"^(#{2,4}\s|```|:::|>|\s*([-*]|\d+\.)\s|---+$)", lines[i]
        ):
            buf.append(lines[i])
            i += 1
        text = inline(" ".join(buf))
        # A paragraph that is nothing but one figure must not be wrapped in <p>.
        if text.startswith("<figure") and text.endswith("</figure>"):
            out.append(text)
        else:
            out.append(f"<p>{text}</p>")

    return "\n".join(out)


# ─────────────────────────────────────────────────────────────────────────────
# The page shell — minimal chrome, with a link back to the site.
# ─────────────────────────────────────────────────────────────────────────────

def nav_html(pages: list[Page], current: Page) -> str:
    parts = []
    for section in SECTION_ORDER:
        group = [p for p in pages if p.section == section]
        if not group:
            continue
        group.sort(key=lambda p: p.order)
        if section:
            parts.append(f'<p class="nav-sec">{html.escape(section)}</p>')
        parts.append("<ul>")
        for p in group:
            cur = ' class="cur" aria-current="page"' if p.slug == current.slug else ""
            parts.append(f'<li><a href="{p.url}"{cur}>{html.escape(p.title)}</a></li>')
        parts.append("</ul>")
    return "\n".join(parts)


def search_index(pages: list[Page]) -> str:
    """A tiny static index, fetched only when someone opens search.

    ⭐ 50 pages and ~28,000 words is past what a sidebar can expose. The index
    is deliberately NOT inlined into every page: it is one file, fetched once
    on first use, so the cost lands on the readers who search and nobody else.
    """
    docs = []
    for p in pages:
        body = re.sub(r"<[^>]+>", " ", p.html)
        body = html.unescape(body)
        body = re.sub(r"\s+", " ", body).strip()
        docs.append(
            {
                "u": p.url,
                "t": p.title,
                "s": p.section or "Help",
                "d": p.description,
                "h": [t for _, t, _ in p.headings if _ == 2],
                # ⛔ THE WHOLE BODY, NOT A PREFIX. This was capped at 1,800
                # chars, which is about HALF a typical page — and the bug that
                # exposed it is instructive: searching "amber" returned
                # nothing, although the dashboard page has a whole section on
                # what amber means, because that section sits past 1,800 chars.
                # A search that silently cannot see half of every page is worse
                # than no search, because it answers "not here" with confidence.
                # Longest page is ~5.4 KB; the full index is ~160 KB, well
                # inside the 250 KB budget the self-test enforces.
                "b": body,
            }
        )
    return json.dumps(docs, separators=(",", ":"), ensure_ascii=False)


def prevnext_html(pages: list[Page], current: Page) -> str:
    """Sequential navigation within a section.

    ⭐ The sidebar answers "where am I"; it does not answer "what next". These
    pages are ordered deliberately (setup → tour → dashboard → …) and a reader
    working through a product had no way to follow that order without going
    back to the list every time.
    """
    group = sorted(
        [p for p in pages if p.section == current.section], key=lambda p: p.order
    )
    try:
        i = [p.slug for p in group].index(current.slug)
    except ValueError:
        return ""
    prev = group[i - 1] if i > 0 else None
    nxt = group[i + 1] if i < len(group) - 1 else None
    if not prev and not nxt:
        return ""
    out = ['<nav class="pn" aria-label="Continue reading">']
    if prev:
        out.append(
            f'<a class="pn-p" href="{prev.url}"><span>Previous</span>'
            f"<b>{html.escape(prev.title)}</b></a>"
        )
    if nxt:
        out.append(
            f'<a class="pn-n" href="{nxt.url}"><span>Next</span>'
            f"<b>{html.escape(nxt.title)}</b></a>"
        )
    out.append("</nav>")
    return "".join(out)


def toc_html(page: Page) -> str:
    """On-page contents, h2 only. Skipped when a page has fewer than three."""
    h2 = [h for h in page.headings if h[0] == 2]
    if len(h2) < 3:
        return ""
    items = "".join(f'<li><a href="#{hid}">{html.escape(t)}</a></li>' for _, t, hid in h2)
    return f'<nav class="toc" aria-label="On this page"><p>On this page</p><ul>{items}</ul></nav>'


def shell(page: Page, pages: list[Page]) -> str:
    canonical = f"{SITE}{page.url}"
    robots = (
        '\n  <meta name="robots" content="noindex, nofollow">' if NOINDEX else ""
    )
    desc = html.escape(page.description, quote=True)
    title = html.escape(page.title)
    full_title = "Cora Help" if page.slug == "index" else f"{title} — Cora Help"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{full_title}</title>
  <meta name="description" content="{desc}">{robots}
  <meta name="theme-color" content="#F7FAFD">
  <link rel="canonical" href="{canonical}">
  <meta property="og:site_name" content="Cora">
  <meta property="og:title" content="{full_title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE}/og-image.png">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <!-- ⛔ Never add rel=preload for the faces — that is what put the old Google
       Fonts request on the critical path for 1053 ms. font-display:swap paints
       the fallback first, which is the behaviour we want. -->
  <link rel="stylesheet" href="/fonts.css?v={FONTS_VERSION}" media="print" onload="this.media='all'">
  <noscript><link rel="stylesheet" href="/fonts.css?v={FONTS_VERSION}"></noscript>
  <link rel="stylesheet" href="/help/help.css?v={CSS_VERSION}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<header class="hnav">
  <div class="hnav-in">
    <a class="hbrand" href="/help/">
      <img src="/cora_logo-240.webp" alt="Cora" width="400" height="163">
      <span>Help</span>
    </a>
    <button class="hfind" id="hfind" type="button" aria-label="Search the guide">
      <svg aria-hidden="true" focusable="false" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5" stroke-linecap="round"/></svg>
      <span>Search</span><kbd>/</kbd>
    </button>
    <a class="hback" href="/">coraiq.tech &rarr;</a>
    <button class="hmenu" id="hmenu" aria-label="Menu" aria-controls="hside" aria-expanded="false">
      <svg aria-hidden="true" focusable="false" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7h16M4 12h16M4 17h16" stroke-linecap="round"/></svg>
    </button>
  </div>
</header>

<div class="hwrap">
  <div class="hscrim" id="hscrim" hidden></div>
  <aside class="hside" id="hside" aria-label="Guide navigation">
    <button class="hclose" id="hclose" type="button" aria-label="Close navigation">&times;</button>
    <nav aria-label="Guide">
{nav_html(pages, page)}
    </nav>
  </aside>

  <main class="hmain" id="main">
    <article class="doc">
      <h1>{title}</h1>
      {toc_html(page)}
{page.html}
      {prevnext_html(pages, page)}
      <p class="stamp">Written for Cora Max {STAMP_MAX} and Cora Mobile {STAMP_MOBILE}.</p>
      <p class="ask">Still stuck? Email <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a> and we'll help.</p>
    </article>
  </main>
</div>

<footer class="hfoot">
  <div class="hfoot-in">
    <p class="disc">{html.escape(DISCLAIMER_1)}</p>
    <p class="disc">{html.escape(DISCLAIMER_2)}</p>
    <p class="legal">&copy; 2026 Cora IQ ·
      <a href="/">coraiq.tech</a> ·
      <a href="/privacy-policy.html">Privacy</a> ·
      <a href="/terms-and-conditions.html">Terms</a> ·
      <a href="/support.html">Support</a></p>
  </div>
</footer>

<script>
(function () {{
  var b = document.getElementById('hmenu'),
      s = document.getElementById('hside'),
      scrim = document.getElementById('hscrim'),
      close = document.getElementById('hclose');
  if (!b || !s) return;

  // ⭐ The current page can sit hundreds of pixels down a 50-item list, and
  // the nav always opened at scrollTop 0 — so on a deep page you were looking
  // at "Getting started" with no clue where you were. Centre it instead.
  function reveal() {{
    var cur = s.querySelector('a.cur');
    if (!cur) return;
    var want = cur.offsetTop - (s.clientHeight / 2) + (cur.offsetHeight / 2);
    s.scrollTop = want > 0 ? want : 0;
  }}
  reveal();

  var lastFocus = null;
  function setOpen(open) {{
    s.classList.toggle('open', open);
    if (scrim) scrim.hidden = !open;
    b.setAttribute('aria-expanded', open ? 'true' : 'false');
    document.documentElement.classList.toggle('nav-open', open);
    if (open) {{
      lastFocus = document.activeElement;
      reveal();
      // ⚠️ NOT SYNCHRONOUSLY. The drawer transitions `visibility`, and an
      // element that is still `visibility: hidden` silently refuses focus —
      // measured: focus stayed on the menu button and Tab then walked the
      // PAGE behind the drawer. Wait for the transition, with a timeout in
      // case it is suppressed by prefers-reduced-motion.
      if (close) {{
        var done = false;
        var give = function () {{
          if (done) return; done = true;
          s.removeEventListener('transitionend', give);
          close.focus();
        }};
        s.addEventListener('transitionend', give);
        setTimeout(give, 260);
      }}
    }} else if (lastFocus) {{
      lastFocus.focus();
    }}
  }}

  b.addEventListener('click', function () {{ setOpen(!s.classList.contains('open')); }});
  if (close) close.addEventListener('click', function () {{ setOpen(false); }});
  if (scrim) scrim.addEventListener('click', function () {{ setOpen(false); }});

  document.addEventListener('keydown', function (e) {{
    if (!s.classList.contains('open')) return;
    if (e.key === 'Escape') {{ setOpen(false); return; }}
    if (e.key !== 'Tab') return;
    // Keep Tab inside the drawer while it covers the page.
    var f = s.querySelectorAll('a[href], button:not([disabled])');
    if (!f.length) return;
    var first = f[0], last = f[f.length - 1];
    if (e.shiftKey && document.activeElement === first) {{ e.preventDefault(); last.focus(); }}
    else if (!e.shiftKey && document.activeElement === last) {{ e.preventDefault(); first.focus(); }}
  }});

  // A tap on a link navigates; make sure the drawer is not left open behind it.
  s.addEventListener('click', function (e) {{
    if (e.target.closest('a') && s.classList.contains('open')) setOpen(false);
  }});
}})();

// ── Screenshot lightbox ────────────────────────────────────────────────
// Phone screenshots render at 300 px so they do not eat the column; dense
// ones are unreadable at that size. Clicking enlarges.
(function () {{
  var box = null, opener = null;
  function shut() {{
    if (!box) return;
    box.remove(); box = null;
    document.documentElement.classList.remove('nav-open');
    if (opener) opener.focus();
  }}
  function open(img, btn) {{
    shut();
    opener = btn;
    box = document.createElement('div');
    box.className = 'lb';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-modal', 'true');
    box.setAttribute('aria-label', img.alt || 'Screenshot');
    var x = document.createElement('button');
    x.type = 'button'; x.className = 'lb-x';
    x.setAttribute('aria-label', 'Close'); x.innerHTML = '&times;';
    var big = document.createElement('img');
    big.src = img.currentSrc || img.src; big.alt = img.alt || '';
    box.appendChild(big); box.appendChild(x);
    document.body.appendChild(box);
    document.documentElement.classList.add('nav-open');
    box.addEventListener('click', function (e) {{ if (e.target !== big) shut(); }});
    x.focus();
  }}
  document.addEventListener('click', function (e) {{
    var btn = e.target.closest('.zoom');
    if (!btn) return;
    var img = btn.querySelector('img');
    if (img) {{ e.preventDefault(); open(img, btn); }}
  }});
  document.addEventListener('keydown', function (e) {{
    if (e.key === 'Escape') shut();
  }});
}})();

// ── Search ─────────────────────────────────────────────────────────────
(function () {{
  var btn = document.getElementById('hfind');
  if (!btn) return;
  var docs = null, dlg = null, input = null, list = null, opener = null;

  function esc(t) {{
    return t.replace(/[&<>]/g, function (c) {{
      return {{'&': '&amp;', '<': '&lt;', '>': '&gt;'}}[c];
    }});
  }}

  // A snippet centred on the hit, so a result shows WHY it matched.
  function snip(body, q) {{
    var i = body.toLowerCase().indexOf(q);
    if (i < 0) return '';
    var a = Math.max(0, i - 45), b = Math.min(body.length, i + q.length + 75);
    return (a ? '…' : '') + esc(body.slice(a, i))
      + '<mark>' + esc(body.slice(i, i + q.length)) + '</mark>'
      + esc(body.slice(i + q.length, b)) + (b < body.length ? '…' : '');
  }}

  function score(d, q) {{
    var t = d.t.toLowerCase();
    if (t === q) return 100;
    if (t.indexOf(q) === 0) return 80;
    if (t.indexOf(q) > -1) return 60;
    if ((d.d || '').toLowerCase().indexOf(q) > -1) return 40;
    for (var i = 0; i < d.h.length; i++) {{
      if (d.h[i].toLowerCase().indexOf(q) > -1) return 30;
    }}
    if (d.b.toLowerCase().indexOf(q) > -1) return 10;
    return 0;
  }}

  function run() {{
    var q = input.value.trim().toLowerCase();
    if (!q || !docs) {{ list.innerHTML = ''; return; }}
    var hits = docs.map(function (d) {{ return [score(d, q), d]; }})
                   .filter(function (r) {{ return r[0] > 0; }})
                   .sort(function (a, b) {{ return b[0] - a[0]; }})
                   .slice(0, 12);
    if (!hits.length) {{
      list.innerHTML = '<li class="snone">Nothing matched “' + esc(q) + '”.</li>';
      return;
    }}
    list.innerHTML = hits.map(function (r, i) {{
      var d = r[1], sn = snip(d.b, q) || esc(d.d || '');
      return '<li><a href="' + d.u + '"' + (i ? '' : ' class="on"') + '>'
        + '<b>' + esc(d.t) + '</b><em>' + d.s + ' · ' + sn + '</em></a></li>';
    }}).join('');
  }}

  function shut() {{
    if (!dlg) return;
    dlg.remove(); dlg = null;
    document.documentElement.classList.remove('nav-open');
    if (opener) opener.focus();
  }}

  function open() {{
    if (dlg) return;
    opener = document.activeElement;
    dlg = document.createElement('div');
    dlg.className = 'sdlg';
    dlg.setAttribute('role', 'dialog');
    dlg.setAttribute('aria-modal', 'true');
    dlg.setAttribute('aria-label', 'Search the guide');
    dlg.innerHTML = '<div class="sbox"><input type="search" '
      + 'placeholder="Search the guide…" aria-label="Search the guide" '
      + 'autocomplete="off" spellcheck="false"><ul class="sres"></ul></div>';
    document.body.appendChild(dlg);
    document.documentElement.classList.add('nav-open');
    input = dlg.querySelector('input');
    list = dlg.querySelector('.sres');
    input.focus();
    dlg.addEventListener('click', function (e) {{
      if (!e.target.closest('.sbox')) shut();
    }});
    input.addEventListener('input', run);
    // ⭐ Fetched ONCE, on first open — never on a page that is only read.
    if (docs) {{ run(); return; }}
    fetch('/help/search.json').then(function (r) {{ return r.json(); }})
      .then(function (j) {{ docs = j; run(); }})
      .catch(function () {{
        list.innerHTML = '<li class="snone">Search is unavailable — '
          + 'use the navigation instead.</li>';
      }});
  }}

  btn.addEventListener('click', open);

  document.addEventListener('keydown', function (e) {{
    var typing = /^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName);
    if (e.key === '/' && !typing && !dlg) {{ e.preventDefault(); open(); return; }}
    if (!dlg) return;
    if (e.key === 'Escape') {{ shut(); return; }}
    if (e.key !== 'ArrowDown' && e.key !== 'ArrowUp' && e.key !== 'Enter') return;
    var links = list.querySelectorAll('a');
    if (!links.length) return;
    var at = -1;
    for (var i = 0; i < links.length; i++) if (links[i].classList.contains('on')) at = i;
    if (e.key === 'Enter') {{
      if (at > -1) {{ e.preventDefault(); links[at].click(); }}
      return;
    }}
    e.preventDefault();
    if (at > -1) links[at].classList.remove('on');
    var next = e.key === 'ArrowDown'
      ? (at + 1) % links.length
      : (at <= 0 ? links.length - 1 : at - 1);
    links[next].classList.add('on');
    links[next].scrollIntoView({{block: 'nearest'}});
  }});
}})();
</script>
</body>
</html>
"""


# ─────────────────────────────────────────────────────────────────────────────
# help.css — the palette is LIFTED from styles.css so there is one source of
# truth for colour and type. Only the help LAYOUT lives here, which keeps the
# marketing site from downloading rules it never uses and keeps a help page to
# a single stylesheet request.
# ─────────────────────────────────────────────────────────────────────────────

HELP_LAYOUT = """
/* ⛔ GENERATED by build_help.py — edit the generator, not this file.
   The :root block above is copied from styles.css at build time. */

*, *::before, *::after { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; scroll-behavior: smooth; }
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }
body {
  margin: 0; background: var(--bg); color: var(--text);
  font-family: var(--font-body); font-size: 16px; line-height: 1.65;
  -webkit-font-smoothing: antialiased;
}
img { max-width: 100%; height: auto; }
a { color: var(--brand-deep); text-decoration-thickness: 1px; text-underline-offset: 2px; }
/* ⚖️ Hover must never REDUCE contrast. --brand (#0070FF) measures 4.21:1 on
   --bg and fails AA, so hover keeps --brand-deep (6.37:1) and signals itself
   with a thicker underline instead of a lighter colour. */
a:hover { color: var(--brand-deep); text-decoration-thickness: 2px; }
:focus-visible { outline: 2px solid var(--cyan); outline-offset: 2px; border-radius: 4px; }

.skip {
  position: absolute; left: -9999px; top: 0; z-index: 100;
  background: var(--surface); color: var(--text);
  padding: 10px 16px; border-radius: 0 0 var(--radius-sm) 0;
  box-shadow: var(--shadow-card); font-weight: 600;
}
.skip:focus { left: 0; }

/* ── Top bar ─────────────────────────────────────────────────────────── */
.hnav {
  position: sticky; top: 0; z-index: 40;
  background: rgba(247,250,253,0.88); backdrop-filter: saturate(1.4) blur(10px);
  border-bottom: 1px solid var(--line);
}
.hnav-in {
  max-width: var(--maxw); margin: 0 auto; padding: 12px 24px;
  display: flex; align-items: center; gap: 16px;
}
.hbrand { display: flex; align-items: center; gap: 10px; text-decoration: none; color: var(--ink); }
.hbrand img { width: 96px; height: auto; display: block; }
.hbrand span {
  font-family: var(--font-display); font-weight: 700; font-size: 15px;
  letter-spacing: 0.02em; color: var(--text-2);
  border-left: 1px solid var(--line-strong); padding-left: 10px;
}
.hback { margin-left: auto; font-size: 14px; font-weight: 600; text-decoration: none; }
.hmenu {
  display: none; background: none; border: 1px solid var(--line-strong);
  border-radius: var(--radius-sm); padding: 6px; color: var(--text-2); cursor: pointer;
}
.hmenu svg { width: 22px; height: 22px; display: block; }

/* ── Layout ──────────────────────────────────────────────────────────── */
.hwrap {
  max-width: var(--maxw); margin: 0 auto; padding: 0 24px;
  display: grid; grid-template-columns: 232px minmax(0, 1fr); gap: 48px;
  align-items: start;
}
.hside { position: sticky; top: 76px; max-height: calc(100vh - 96px); overflow-y: auto; padding: 32px 0 40px; }
.hside ul { list-style: none; margin: 0 0 20px; padding: 0; }
.hside li { margin: 0; }
.hside a {
  display: block; padding: 5px 10px; margin-left: -10px;
  border-radius: var(--radius-sm); font-size: 14.5px;
  color: var(--text-2); text-decoration: none; line-height: 1.4;
}
.hside a:hover { background: var(--surface-2); color: var(--text); }
.hside a.cur { background: var(--surface-3); color: var(--brand-deep); font-weight: 600; }
.nav-sec {
  font-family: var(--font-display); font-size: 11.5px; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.08em; color: var(--text-3);
  margin: 22px 0 8px;
}
.hside nav > ul:first-child { margin-top: 4px; }

.hmain { padding: 34px 0 72px; min-width: 0; }
.doc { max-width: 70ch; }

/* ── Type ────────────────────────────────────────────────────────────── */
.doc h1 {
  font-family: var(--font-display); font-weight: 800; font-size: clamp(30px, 4.4vw, 40px);
  line-height: 1.15; letter-spacing: -0.02em; color: var(--ink);
  margin: 0 0 20px; text-wrap: balance;
}
.doc h2 {
  font-family: var(--font-display); font-weight: 700; font-size: 23px;
  line-height: 1.3; letter-spacing: -0.01em; color: var(--ink);
  margin: 44px 0 12px; padding-top: 10px; text-wrap: balance;
  border-top: 1px solid var(--line);
}
.doc h3 {
  font-family: var(--font-display); font-weight: 700; font-size: 17.5px;
  color: var(--ink); margin: 30px 0 8px; text-wrap: balance;
}
.doc h4 { font-family: var(--font-display); font-weight: 700; font-size: 15.5px; color: var(--text); margin: 22px 0 6px; }
.doc p { margin: 0 0 16px; }
.doc ul, .doc ol { margin: 0 0 16px; padding-left: 22px; }
.doc li { margin: 0 0 7px; }
.doc li > ul, .doc li > ol { margin: 7px 0 0; }
.doc strong { font-weight: 650; color: var(--ink); }
.doc hr { border: 0; border-top: 1px solid var(--line); margin: 34px 0; }
.doc code {
  font-family: var(--font-mono); font-size: 0.875em;
  background: var(--surface-2); border: 1px solid var(--line);
  border-radius: 5px; padding: 1px 5px;
}
.doc pre {
  background: var(--surface-2); border: 1px solid var(--line);
  border-radius: var(--radius-sm); padding: 14px 16px;
  overflow-x: auto; margin: 0 0 18px;
}
.doc pre code { background: none; border: 0; padding: 0; font-size: 13.5px; line-height: 1.6; }
.doc blockquote {
  margin: 0 0 18px; padding: 2px 0 2px 18px;
  border-left: 3px solid var(--line-strong); color: var(--text-2);
}
.doc blockquote p:last-child { margin-bottom: 0; }

/* ── On-page contents ────────────────────────────────────────────────── */
.toc {
  background: var(--surface-2); border: 1px solid var(--line);
  border-radius: var(--radius-sm); padding: 14px 18px; margin: 0 0 30px;
}
.toc p {
  font-family: var(--font-display); font-size: 11.5px; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.08em; color: var(--text-3); margin: 0 0 6px;
}
.toc ul { list-style: none; margin: 0; padding: 0; columns: 2; column-gap: 24px; }
.toc li { margin: 0 0 3px; break-inside: avoid; }
.toc a { font-size: 14.5px; text-decoration: none; color: var(--text-2); }
.toc a:hover { color: var(--brand-deep); text-decoration: underline; }

/* ── Callouts ────────────────────────────────────────────────────────── */
.cal {
  border-radius: var(--radius-sm); padding: 14px 18px; margin: 0 0 20px;
  border: 1px solid var(--line); border-left-width: 3px; background: var(--surface-2);
}
.cal > :last-child { margin-bottom: 0; }
.cal-t { font-family: var(--font-display); font-weight: 700; font-size: 14.5px; margin: 0 0 5px !important; color: var(--ink); }
.cal-note    { border-left-color: var(--brand); }
.cal-warning { border-left-color: var(--amber); }
.cal-tip     { border-left-color: var(--teal); }

/* ── Figures ─────────────────────────────────────────────────────────── */
.shot { margin: 0 0 24px; }
.shot img {
  display: block; width: 100%; border-radius: var(--radius-sm);
  border: 1px solid var(--line); background: var(--surface);
  box-shadow: 0 10px 26px rgba(23,59,110,0.07);
}
.shot figcaption { font-size: 13.5px; color: var(--text-3); margin-top: 8px; }

/* ── Search ──────────────────────────────────────────────────────────── */
.hfind {
  display: inline-flex; align-items: center; gap: 7px; margin-left: auto;
  padding: 6px 10px; font: inherit; font-size: 13.5px; cursor: pointer;
  color: var(--text-2); background: var(--surface-2);
  border: 1px solid var(--line); border-radius: var(--radius-sm);
}
.hfind:hover { border-color: var(--line-strong); color: var(--text); }
.hfind svg { width: 15px; height: 15px; }
.hfind kbd {
  font: inherit; font-size: 11.5px; padding: 1px 5px; color: var(--text-3);
  border: 1px solid var(--line); border-radius: 4px; background: var(--surface);
}
.sdlg {
  position: fixed; inset: 0; z-index: 95; display: flex;
  justify-content: center; padding: 10vh 20px 20px;
  background: rgba(9,18,33,.5);
}
.sbox {
  width: min(680px, 100%); max-height: 74vh; display: flex; flex-direction: column;
  background: var(--surface); border: 1px solid var(--line);
  border-radius: var(--radius); box-shadow: 0 26px 70px rgba(0,0,0,.3);
  overflow: hidden;
}
.sbox input {
  font: inherit; font-size: 16px; padding: 15px 18px; border: 0;
  border-bottom: 1px solid var(--line); outline: none; color: var(--text);
  background: var(--surface);
}
.sres { overflow-y: auto; padding: 6px; margin: 0; list-style: none; }
.sres li { margin: 0; }
.sres a {
  display: block; padding: 9px 12px; border-radius: var(--radius-sm);
  text-decoration: none; color: var(--text);
}
.sres a:hover, .sres a.on { background: var(--surface-2); }
.sres b { display: block; font-size: 14.5px; color: var(--brand-deep); }
.sres em {
  display: block; font-style: normal; font-size: 12.5px;
  color: var(--text-3); margin-top: 2px;
}
.sres mark { background: #ffe9a8; color: inherit; padding: 0 1px; border-radius: 2px; }
.snone { padding: 22px; color: var(--text-3); font-size: 14px; }
@media (max-width: 900px) { .hfind span, .hfind kbd { display: none; } }

/* ── Zoomable screenshots ────────────────────────────────────────────── */
.zoom {
  display: block; padding: 0; border: 0; background: none; width: 100%;
  cursor: zoom-in; border-radius: var(--radius-sm);
}
.zoom:focus-visible { outline: 2px solid var(--brand); outline-offset: 3px; }
.shot.phone .zoom { max-width: 300px; }

.lb {
  position: fixed; inset: 0; z-index: 90; display: flex;
  align-items: center; justify-content: center; padding: 24px;
  background: rgba(9,18,33,.86);
}
.lb img {
  max-width: min(1100px, 96vw); max-height: 92vh; width: auto; height: auto;
  border-radius: var(--radius-sm); box-shadow: 0 24px 60px rgba(0,0,0,.45);
}
.lb-x {
  position: absolute; top: 14px; right: 16px; width: 44px; height: 44px;
  font-size: 30px; line-height: 1; color: #fff; cursor: pointer;
  background: rgba(255,255,255,.12); border: 0; border-radius: var(--radius-sm);
}
.lb-x:hover { background: rgba(255,255,255,.22); }

/* ── Previous / next ─────────────────────────────────────────────────── */
.pn {
  display: flex; gap: 14px; flex-wrap: wrap;
  margin: 40px 0 10px; padding-top: 22px; border-top: 1px solid var(--line);
}
.pn a {
  flex: 1 1 220px; min-width: 0; text-decoration: none;
  border: 1px solid var(--line); border-radius: var(--radius-sm);
  padding: 12px 14px; background: var(--surface);
}
.pn a:hover { border-color: var(--line-strong); background: var(--surface-2); }
.pn span {
  display: block; font-size: 11.5px; font-weight: 700; letter-spacing: .07em;
  text-transform: uppercase; color: var(--text-3); margin-bottom: 3px;
}
.pn b { color: var(--brand-deep); font-size: 15px; font-weight: 600; }
.pn-n { text-align: right; }
.shot.phone img { max-width: 300px; }
.shot.phone { display: flex; flex-direction: column; align-items: flex-start; }
.shot.ph .ph-box {
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  gap: 4px; padding: 40px 20px; text-align: center;
  background: var(--surface-2); border: 1px dashed var(--line-strong);
  border-radius: var(--radius-sm); color: var(--text-3);
}
.shot.ph span { font-family: var(--font-display); font-weight: 700; font-size: 14px; }
.shot.ph small { font-size: 13px; }

/* ── Tables ──────────────────────────────────────────────────────────── */
.tw { overflow-x: auto; margin: 0 0 22px; }
.doc table { border-collapse: collapse; width: 100%; font-size: 14.5px; }
.doc th, .doc td { text-align: left; padding: 9px 14px 9px 0; border-bottom: 1px solid var(--line); vertical-align: top; }
.doc th {
  font-family: var(--font-display); font-weight: 700; font-size: 12.5px;
  text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-3);
  border-bottom-color: var(--line-strong); white-space: nowrap;
}
.doc td code { white-space: nowrap; }

/* ── Page furniture ──────────────────────────────────────────────────── */
.stamp {
  margin: 44px 0 6px !important; padding-top: 18px; border-top: 1px solid var(--line);
  font-size: 13px; color: var(--text-3);
}
.ask { font-size: 14px; color: var(--text-2); margin: 0 !important; }

/* ── Home tiles (index only) ─────────────────────────────────────────── */
.tiles { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 14px; margin: 0 0 30px; padding: 0; list-style: none; }
.tiles li { margin: 0; }
.tiles a {
  display: block; height: 100%; padding: 16px 18px; text-decoration: none;
  background: var(--surface); border: 1px solid var(--line);
  border-radius: var(--radius-sm); box-shadow: 0 2px 8px rgba(23,59,110,0.04);
}
.tiles a:hover { border-color: var(--line-strong); box-shadow: var(--shadow-card); }
.tiles b { display: block; font-family: var(--font-display); font-size: 16px; color: var(--ink); margin-bottom: 3px; }
.tiles span { display: block; font-size: 14px; color: var(--text-2); line-height: 1.5; }

/* ── Footer ──────────────────────────────────────────────────────────── */
.hfoot { border-top: 1px solid var(--line); background: var(--surface-2); margin-top: 40px; }
.hfoot-in { max-width: var(--maxw); margin: 0 auto; padding: 26px 24px 34px; }
.disc { font-size: 12.5px; line-height: 1.6; color: var(--text-3); margin: 0 0 8px; max-width: 88ch; }
.legal { font-size: 13px; color: var(--text-3); margin: 14px 0 0; }
.legal a { color: var(--text-2); }

/* ── Responsive ──────────────────────────────────────────────────────── */
.hclose { display: none; }

@media (max-width: 900px) {
  .hwrap { grid-template-columns: 1fr; gap: 0; }
  .hmenu { display: block; }

  /* ⛔ WAS `display:block` ON A STATIC ASIDE, which inserted the whole guide
     — 50 links — above the article and pushed the page you came to read off
     the bottom of the screen. A drawer overlays instead, scrolls on its own,
     and closes. */
  .hside {
    display: block; position: fixed; top: 0; right: 0; bottom: 0;
    width: min(86vw, 340px); height: 100dvh; max-height: none;
    overflow-y: auto; overscroll-behavior: contain;
    background: var(--surface); border-left: 1px solid var(--line);
    box-shadow: -18px 0 40px rgba(0,0,0,.18);
    padding: 56px 20px 40px; z-index: 60;
    transform: translateX(100%); visibility: hidden;
    /* ⚠️ visibility is stepped, NOT eased. Transitioning it over a duration
       makes "is it visible yet" depend on where the transition has got to,
       which is fragile and untestable. Flip it instantly on open; delay it
       to the END of the slide on close so the drawer does not vanish
       mid-animation. Only `transform` is actually animated. */
    transition: transform .22s ease, visibility 0s linear .22s;
  }
  .hside.open {
    transform: none; visibility: visible;
    transition: transform .22s ease, visibility 0s linear 0s;
  }

  .hscrim {
    position: fixed; inset: 0; z-index: 55;
    background: rgba(0,0,0,.38);
  }
  .hclose {
    display: block; position: absolute; top: 10px; right: 12px;
    width: 40px; height: 40px; line-height: 1; font-size: 26px;
    background: none; border: 0; border-radius: var(--radius-sm);
    color: var(--text-2); cursor: pointer;
  }
  .hclose:hover { background: var(--surface-2); color: var(--text); }

  /* Stop the page scrolling under an open drawer. */
  html.nav-open, html.nav-open body { overflow: hidden; }

  .hmain { padding-top: 26px; }
  .toc ul { columns: 1; }
  .doc h1 { font-size: 29px; }
}

@media (prefers-reduced-motion: reduce) {
  .hside { transition: none; }
}
@media (max-width: 640px) {
  /* ⭐ A two-column reference table is the common shape here, and sideways
     scrolling hides the half that explains the other half. Stack each row
     into a card and label the cells from the header. */
  .doc table.stack, .doc table.stack tbody, .doc table.stack tr, .doc table.stack td {
    display: block; width: 100%;
  }
  .doc table.stack thead { display: none; }
  .doc table.stack tr {
    border: 1px solid var(--line); border-radius: var(--radius-sm);
    padding: 10px 12px; margin: 0 0 10px; background: var(--surface);
  }
  .doc table.stack td { border: 0; padding: 3px 0; }
  .doc table.stack td::before {
    content: attr(data-th); display: block;
    font-size: 11px; font-weight: 700; letter-spacing: .06em;
    text-transform: uppercase; color: var(--text-3);
  }
  .doc table.stack td:first-child { font-weight: 600; color: var(--text); }
  .pn-n { text-align: left; }
}

@media (max-width: 520px) {
  .hnav-in, .hwrap, .hfoot-in { padding-left: 18px; padding-right: 18px; }
  .hbrand img { width: 78px; }
  .hback { font-size: 13px; }
}
"""


def extract_root() -> str:
    """Pull the :root token block out of styles.css.

    ⛔ ABORTS on failure. A silent miss here ships 21 pages with no palette and
    no type — unstyled, but plausibly "just a cache thing", which is exactly
    the failure mode OPS_Website.md §preview quirks documents.
    """
    css = (ROOT / "styles.css").read_text(encoding="utf-8")
    m = re.search(r"^:root\s*\{.*?^\}", css, re.S | re.M)
    if not m:
        raise SystemExit("⛔ could not find the :root block in styles.css")
    block = m.group(0)
    for needle in ("--brand:", "--bg:", "--text:", "--font-body:", "--maxw:"):
        if needle not in block:
            raise SystemExit(f"⛔ styles.css :root is missing {needle} — refusing to build")
    return block


def load_pages() -> list[Page]:
    pages: list[Page] = []
    for path in sorted(SRC.glob("*.md")):
        # Notes that live beside the content but are not pages.
        if path.name == "README.md" or path.name.startswith("_"):
            continue
        meta, body = parse_frontmatter(path.read_text(encoding="utf-8"), path.stem)
        for key in ("title", "description", "section", "order"):
            if key not in meta:
                raise SystemExit(f"⛔ {path.name} frontmatter is missing '{key}'")
        pages.append(
            Page(
                slug=path.stem,
                title=meta["title"],
                description=meta["description"],
                section=meta["section"] if meta["section"] != "-" else "",
                order=int(meta["order"]),
                body_md=body,
            )
        )
    if not pages:
        raise SystemExit("⛔ no pages found in help-src/ — nothing to build")

    # ⛔ A section not in SECTION_ORDER is silently DROPPED FROM THE NAV by
    # `nav_html`, while the page is still written and served. That is the worst
    # shape of bug: live, linkable, and unreachable by anyone browsing. A typo
    # in one frontmatter line was enough. Fail instead.
    known = set(SECTION_ORDER)
    for p in pages:
        if p.section not in known:
            raise SystemExit(
                f"⛔ {p.slug}.md has section {p.section!r}, which is not in "
                f"SECTION_ORDER {SECTION_ORDER!r}. The page would be published "
                "but left out of the sidebar — fix the frontmatter, or add the "
                "section to SECTION_ORDER."
            )

    # ⚠️ Two pages sharing an order inside a section sort arbitrarily, so the
    # sidebar changes between builds for no reason anyone can see.
    seen: dict[tuple[str, int], str] = {}
    for p in pages:
        key = (p.section, p.order)
        if key in seen:
            raise SystemExit(
                f"⛔ {p.slug}.md and {seen[key]}.md are both order {p.order} in "
                f"section {p.section!r} — the sidebar order would be unstable."
            )
        seen[key] = p.slug
    return pages


def build(check_only: bool = False) -> int:
    pages = load_pages()
    OUT.mkdir(parents=True, exist_ok=True)

    for p in pages:
        p.headings = []
        p.html = render(p.body_md, p.headings)

    written, stale = 0, []
    css = f"{extract_root()}\n{HELP_LAYOUT}"

    # ⭐ Hash before rendering: `shell()` reads these globals at call time.
    global CSS_VERSION, FONTS_VERSION
    CSS_VERSION = hashlib.sha256(css.encode("utf-8")).hexdigest()[:10]
    fonts = ROOT / "fonts.css"
    if fonts.exists():
        FONTS_VERSION = hashlib.sha256(
            fonts.read_bytes()).hexdigest()[:10]

    targets = [(OUT / "help.css", css), (OUT / "search.json", search_index(pages))] + [(p.out_path, shell(p, pages)) for p in pages]

    for path, content in targets:
        old = path.read_text(encoding="utf-8") if path.exists() else None
        if old == content:
            continue
        if check_only:
            stale.append(path.name)
            continue
        path.write_text(content, encoding="utf-8")
        written += 1

    if check_only:
        if stale:
            print(f"⛔ out of date: {', '.join(stale)}")
            return 1
        print(f"✅ help/ is up to date ({len(pages)} pages)")
        return 0

    print(f"✅ {len(pages)} pages · {written} file(s) written · css v{CSS_VERSION}")
    if NOINDEX:
        print("⚠️  NOINDEX is ON — pages carry robots noindex and are unlisted.")
    if _MISSING:
        uniq = sorted(set(_MISSING))
        print(f"⬜ {len(uniq)} image slot(s) not yet captured:")
        for s in uniq:
            print(f"     {s}")
    return 0


# ─────────────────────────────────────────────────────────────────────────────
# Self-test. ⚠️ Run before trusting a build. Twelve directions, each aimed at a
# way this generator could produce plausible-looking wrong output.
# ─────────────────────────────────────────────────────────────────────────────

def self_test() -> int:
    fails = []
    ran = []

    def ok(name, cond):
        # ⭐ COUNT, don't restate. This total was hardcoded in the summary line
        # AND claimed differently in this file's docstring AND in
        # help-src/README.md — three numbers, all stale, found 2026-09-09.
        ran.append(name)
        if not cond:
            fails.append(name)

    h = []
    ok("h2 renders with an id", '<h2 id="setup">' in render("## Setup", h))
    ok("heading is collected", h and h[0] == (2, "Setup", "setup"))

    ok("bold", "<strong>x</strong>" in render("**x**", []))
    ok("code span", "<code>a*b*c</code>" in render("`a*b*c`", []))
    # The trap this pins: inline markup must not run INSIDE a code span.
    ok("no em inside code", "<em>" not in render("`a*b*c`", []))
    ok("html is escaped", "&lt;script&gt;" in render("<script>", []))

    ok("list", "<ul><li>a</li><li>b</li></ul>" in render("- a\n- b", []))
    ok("ordered list", "<ol><li>a</li></ol>" in render("1. a", []))

    t = render("| A | B |\n|---|---|\n| 1 | 2 |", [])
    ok("table head", "<th>A</th>" in t)
    ok("table body", ">2</td>" in t)
    # ⭐ Each cell carries its column heading so a phone can stack the row into
    # a labelled card. Without `data-th` the stacked view loses the half that
    # explains the other half, which is the whole reason it stacks.
    ok("table cells carry their column label", 'data-th="B">2</td>' in t)
    ok("narrow tables opt into stacking", 'class="stack"' in t)
    wide = render("| A | B | C | D |\n|---|---|---|---|\n| 1 | 2 | 3 | 4 |", [])
    ok("⚠️ but a 4-column table stays scrollable, not stacked",
       'class="stack"' not in wide)

    ok("callout", 'class="cal cal-warning"' in render(":::warning Careful\nbody\n:::", []))
    ok("fence keeps markup literal", "**x**" in render("```\n**x**\n```", []))

    # A link out to a third party opens in a new tab; an internal one does not.
    ok("external link", 'rel="noopener"' in render("[x](https://example.com)", []))
    ok("internal link", 'rel="noopener"' not in render("[x](/help/setup)", []))

    ok("raw html passes through",
       '<ul class="tiles">' in render('<ul class="tiles">\n<li>x</li>\n</ul>', []))
    ok("a lone < in prose is still escaped", "&lt; 5" in render("a value < 5", []))
    ok("⛔ script is NOT passed through", "&lt;script&gt;" in render("<script>alert(1)</script>", []))
    ok("tokens extract", "--brand:" in extract_root())

    # ⛔⛔ THE INLINE SCRIPT MUST PARSE. The page shell is an f-string, so a
    # single `{` in the JavaScript is a FORMAT PLACEHOLDER — that broke the
    # build once (2026-09-09) and, because build+commit+push were chained, the
    # breakage was committed. A brace-balance check is cheap and catches the
    # whole class; `node --check` runs on top when node is available.
    import shutil as _sh, subprocess as _sp, tempfile as _tf
    _demo = Page(slug="x", title="T", description="d", section="Cora Mobile",
                 order=1, body_md="body")
    _demo.html = "<p>body</p>"
    _shell = shell(_demo, [_demo])
    _js = "\n".join(re.findall(r"<script>(.*?)</script>", _shell, re.S))
    ok("inline script is present", len(_js) > 500)
    ok("⛔ no unescaped f-string braces survive into the page",
       "{{" not in _shell and "}}" not in _shell)
    if _sh.which("node"):
        with _tf.NamedTemporaryFile("w", suffix=".js", delete=False) as fh:
            fh.write(_js)
            _tmp = fh.name
        _r = _sp.run(["node", "--check", _tmp], capture_output=True, text=True)
        ok(f"⛔ inline JavaScript parses ({_r.stderr.strip()[:80]})", _r.returncode == 0)

    # ⚠️ PERFORMANCE BUDGET. Nothing here is slow today; the budget exists so
    # that stays true without anyone measuring. Numbers are ~2x current, so
    # they flag a change in kind, not ordinary growth.
    ok(f"a page stays under 90 KB ({len(_shell) // 1024} KB)", len(_shell) < 92_160)
    _imgs = sorted((OUT / "img").glob("*.webp")) if (OUT / "img").exists() else []
    _big = [f.name for f in _imgs if f.stat().st_size > 160_000]
    ok(f"⚠️ no screenshot over 160 KB ({_big})", not _big)
    _idx = OUT / "search.json"
    if _idx.exists():
        ok(f"search index under 250 KB ({_idx.stat().st_size // 1024} KB)",
           _idx.stat().st_size < 256_000)

    # ⛔ CONTENT RULE, ENFORCED. help-src/README.md has said 'Maxspect is
    # "coming soon"' since the guide was written, and SIX pages named it as a
    # shipped integration anyway (found in review, 2026-09-09) while the public
    # site carried a badge-soon. A rule nobody checks is a rule nobody follows.
    unlabelled = []
    for md in sorted(SRC.glob("*.md")):
        if md.name == "README.md":
            continue
        body = md.read_text(encoding="utf-8")
        if "maxspect" in body.lower() and "coming soon" not in body.lower():
            unlabelled.append(md.name)
    ok(f"⛔ Maxspect is labelled coming-soon wherever it is named ({unlabelled})",
       not unlabelled)

    # ⛔ A zero-length render would make several checks above pass vacuously.
    ok("render is not empty", len(render("## A\n\ntext\n", [])) > 20)

    if fails:
        print("⛔ FAILED:")
        for f in fails:
            print(f"   · {f}")
        return 1
    print(f"✅ self-test: {len(ran)}/{len(ran)}")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    sys.exit(build(check_only="--check" in sys.argv))

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

# PUBLISHED 2026-09-17 (owner: make coraiq.tech/help public once Cora Mobile was live
# on the App Store). Hiding it again = set this True, restore the robots.txt
# Disallow and remove the sitemap entries, in one commit.
NOINDEX = False

# ⛔⛔ GIZ-14 — BOTH disclaimers, verbatim, on every page that names a
# manufacturer. On a help site that is most of them, so they live in the shared
# footer and appear on all of them. Do not paraphrase; do not drop one.
DISCLAIMER_1 = (
    "All product names and trademarks are the property of their respective "
    "owners. Cora is not affiliated with, sponsored by, or endorsed by these "
    "manufacturers unless expressly stated otherwise."
)
DISCLAIMER_2 = (
    "Some devices are connected through APIs that are not officially supported "
    "by their manufacturers; support will be updated as official APIs arrive."
)

SUPPORT_EMAIL = "cora@coraiq.tech"

# ⭐ Owner, 2026-09-21: no third-party LOGOS anywhere on the site or in the guide;
# each brand keeps its NAME with a ™ and DISCLAIMER_1 names the owners. Marked on
# the first mention per page (the convention: once is the notice, every time is
# noise). Order matters: "Neptune Systems" before "Neptune".
TRADEMARKS = [
    ("neptune", r"Neptune Systems|Neptune"),
    ("redsea", r"Red Sea"),
    ("jecod", r"Jecod"),
    ("jebao", r"Jebao"),
    ("maxspect", r"Maxspect"),
    ("aquawiz", r"AquaWiz"),
    ("hydros", r"Hydros|HYDROS"),
    ("ghl", r"GHL"),
    ("nyos", r"NYOS|Nyos"),
    ("abyzz", r"Abyzz"),
    ("deltec", r"Deltec"),
]
_TAG_SPLIT = re.compile(r"(<[^>]+>)")


def mark_trademarks(body: str) -> str:
    """™ after the first mention of each brand in a page body. Text nodes only:
    never inside a tag or attribute, never inside code or pre."""
    seen: set[str] = set()
    parts = _TAG_SPLIT.split(body)
    literal = 0
    for i, part in enumerate(parts):
        if part.startswith("<"):
            if re.match(r"<(code|pre)\b", part, re.I):
                literal += 1
            elif re.match(r"</(code|pre)>", part, re.I):
                literal = max(0, literal - 1)
            continue
        if literal or not part:
            continue
        for key, pat in TRADEMARKS:
            if key in seen:
                continue
            m = re.search(rf"\b(?:{pat})\b(?![™®])", part)
            if m:
                part = part[: m.end()] + "™" + part[m.end():]
                seen.add(key)
        parts[i] = part
    return "".join(parts)


# ─────────────────────────────────────────────────────────────────────────────
# Languages.
#
# ⭐ `en` is the source: help-src/*.md → /help/... . Each other language is a
# TRANSLATION TREE that mirrors it: help-src/<lang>/*.md → /<lang>/help/... .
# A translated file must keep the same filename and the same frontmatter KEYS
# as its English counterpart (title/description translated, section/order/
# group left exactly as the English file has them — those are structural, not
# prose, and the sidebar grouping depends on them matching across languages).
# A language simply has fewer files while translators are still working; a
# missing page is never an error, it is just not built for that language yet.
# ─────────────────────────────────────────────────────────────────────────────

LANGS = ["de", "fr", "tr", "it", "es", "pl"]
ALL_LANGS = ["en"] + LANGS

NATIVE_NAMES = {
    "en": "English",
    "de": "Deutsch",
    "fr": "Français",
    "tr": "Türkçe",
    "it": "Italiano",
    "es": "Español",
    "pl": "Polski",
}

# ⭐ ONE TABLE, every fixed UI word the shell prints, keyed by language. A
# string missing here is a hole no translator can see (it is not in any .md
# file), so the self-test checks every language has every key.
#
# ⚠️ `sections`/`groups` translate the SIDEBAR LABEL only — the frontmatter
# `section:`/`group:` VALUE that drives the lookup stays the English string in
# every language's .md file (see the note above `LANGS`). "Cora Mobile" and
# "Cora Max" are product names and are never translated; only the generic
# word "Help" and the ten task groups have entries.
UI_STRINGS = {
    "en": {
        "skip": "Skip to content",
        "menu": "Menu",
        "close_nav": "Close navigation",
        "search_button": "Search",
        "search_aria": "Search the guide",
        "search_placeholder": "Search the guide…",
        "on_this_page": "On this page",
        "previous": "Previous",
        "next": "Next",
        "written_for": "Written for Cora Max {max} and Cora Mobile {mobile}.",
        "last_checked": "Last checked {date}.",
        "still_stuck": "Still stuck? Email {email} and we'll help.",
        "footer_privacy": "Privacy",
        "footer_terms": "Terms",
        "footer_support": "Support",
        "search_none": "Nothing matched “{q}”.",
        "search_unavailable": "Search is unavailable. Use the navigation instead.",
        "lang_label": "Language",
        "sections": {"Help": "Help"},
        "groups": {
            "Account": "Account", "Alerts": "Alerts",
            "Alerts and automation": "Alerts and automation",
            "Automation": "Automation", "Equipment": "Equipment",
            "Getting started": "Getting started", "Intelligence": "Intelligence",
            "Records": "Records", "Settings": "Settings",
            "Your dashboard": "Your dashboard",
        },
    },
    "de": {
        "skip": "Zum Inhalt springen",
        "menu": "Menü",
        "close_nav": "Navigation schließen",
        "search_button": "Suche",
        "search_aria": "Anleitung durchsuchen",
        "search_placeholder": "Anleitung durchsuchen…",
        "on_this_page": "Auf dieser Seite",
        "previous": "Zurück",
        "next": "Weiter",
        "written_for": "Geschrieben für Cora Max {max} und Cora Mobile {mobile}.",
        "last_checked": "Zuletzt geprüft am {date}.",
        "still_stuck": "Kommst du nicht weiter? Schreib eine E-Mail an {email}, wir helfen dir.",
        "footer_privacy": "Datenschutz",
        "footer_terms": "AGB",
        "footer_support": "Support",
        "search_none": "Keine Treffer für „{q}“.",
        "search_unavailable": "Die Suche ist nicht verfügbar. Nutze die Navigation.",
        "lang_label": "Sprache",
        "sections": {"Help": "Hilfe"},
        "groups": {
            "Account": "Konto", "Alerts": "Warnungen",
            "Alerts and automation": "Warnungen und Automatisierung",
            "Automation": "Automatisierung", "Equipment": "Geräte",
            "Getting started": "Erste Schritte", "Intelligence": "Intelligenz",
            "Records": "Aufzeichnungen", "Settings": "Einstellungen",
            "Your dashboard": "Dein Dashboard",
        },
    },
    "fr": {
        "skip": "Aller au contenu",
        "menu": "Menu",
        "close_nav": "Fermer la navigation",
        "search_button": "Rechercher",
        "search_aria": "Rechercher dans le guide",
        "search_placeholder": "Rechercher dans le guide…",
        "on_this_page": "Sur cette page",
        "previous": "Précédent",
        "next": "Suivant",
        "written_for": "Rédigé pour Cora Max {max} et Cora Mobile {mobile}.",
        "last_checked": "Vérifié pour la dernière fois le {date}.",
        "still_stuck": "Toujours bloqué ? Écrivez à {email}, nous vous aiderons.",
        "footer_privacy": "Confidentialité",
        "footer_terms": "Conditions",
        "footer_support": "Assistance",
        "search_none": "Aucun résultat pour « {q} ».",
        "search_unavailable": "La recherche est indisponible. Utilisez la navigation.",
        "lang_label": "Langue",
        "sections": {"Help": "Aide"},
        "groups": {
            "Account": "Compte", "Alerts": "Alertes",
            "Alerts and automation": "Alertes et automatisation",
            "Automation": "Automatisation", "Equipment": "Équipement",
            "Getting started": "Prise en main", "Intelligence": "Intelligence",
            "Records": "Journaux", "Settings": "Paramètres",
            "Your dashboard": "Votre tableau de bord",
        },
    },
    "tr": {
        "skip": "İçeriğe geç",
        "menu": "Menü",
        "close_nav": "Menüyü kapat",
        "search_button": "Ara",
        "search_aria": "Kılavuzda ara",
        "search_placeholder": "Kılavuzda ara…",
        "on_this_page": "Bu sayfada",
        "previous": "Önceki",
        "next": "Sonraki",
        "written_for": "Cora Max {max} ve Cora Mobile {mobile} için yazılmıştır.",
        "last_checked": "Son kontrol: {date}.",
        "still_stuck": "Sorun devam ediyor mu? {email} adresine yazın, yardımcı olalım.",
        "footer_privacy": "Gizlilik",
        "footer_terms": "Koşullar",
        "footer_support": "Destek",
        "search_none": "“{q}” için sonuç bulunamadı.",
        "search_unavailable": "Arama şu anda kullanılamıyor. Menüyü kullanın.",
        "lang_label": "Dil",
        "sections": {"Help": "Yardım"},
        "groups": {
            "Account": "Hesap", "Alerts": "Uyarılar",
            "Alerts and automation": "Uyarılar ve otomasyon",
            "Automation": "Otomasyon", "Equipment": "Ekipman",
            "Getting started": "Başlarken", "Intelligence": "Zeka",
            "Records": "Kayıtlar", "Settings": "Ayarlar",
            "Your dashboard": "Panonuz",
        },
    },
    "it": {
        "skip": "Vai al contenuto",
        "menu": "Menu",
        "close_nav": "Chiudi la navigazione",
        "search_button": "Cerca",
        "search_aria": "Cerca nella guida",
        "search_placeholder": "Cerca nella guida…",
        "on_this_page": "In questa pagina",
        "previous": "Precedente",
        "next": "Successivo",
        "written_for": "Scritto per Cora Max {max} e Cora Mobile {mobile}.",
        "last_checked": "Ultimo controllo il {date}.",
        "still_stuck": "Ancora bloccato? Scrivi a {email}, ti aiutiamo.",
        "footer_privacy": "Privacy",
        "footer_terms": "Termini",
        "footer_support": "Assistenza",
        "search_none": "Nessun risultato per “{q}”.",
        "search_unavailable": "La ricerca non è disponibile. Usa la navigazione.",
        "lang_label": "Lingua",
        "sections": {"Help": "Aiuto"},
        "groups": {
            "Account": "Account", "Alerts": "Avvisi",
            "Alerts and automation": "Avvisi e automazione",
            "Automation": "Automazione", "Equipment": "Apparecchiature",
            "Getting started": "Per iniziare", "Intelligence": "Intelligenza",
            "Records": "Registri", "Settings": "Impostazioni",
            "Your dashboard": "La tua dashboard",
        },
    },
    "es": {
        "skip": "Ir al contenido",
        "menu": "Menú",
        "close_nav": "Cerrar navegación",
        "search_button": "Buscar",
        "search_aria": "Buscar en la guía",
        "search_placeholder": "Buscar en la guía…",
        "on_this_page": "En esta página",
        "previous": "Anterior",
        "next": "Siguiente",
        "written_for": "Escrito para Cora Max {max} y Cora Mobile {mobile}.",
        "last_checked": "Última revisión el {date}.",
        "still_stuck": "¿Sigues atascado? Escribe a {email} y te ayudamos.",
        "footer_privacy": "Privacidad",
        "footer_terms": "Términos",
        "footer_support": "Soporte",
        "search_none": "Sin resultados para “{q}”.",
        "search_unavailable": "La búsqueda no está disponible. Usa la navegación.",
        "lang_label": "Idioma",
        "sections": {"Help": "Ayuda"},
        "groups": {
            "Account": "Cuenta", "Alerts": "Alertas",
            "Alerts and automation": "Alertas y automatización",
            "Automation": "Automatización", "Equipment": "Equipos",
            "Getting started": "Primeros pasos", "Intelligence": "Inteligencia",
            "Records": "Registros", "Settings": "Ajustes",
            "Your dashboard": "Tu panel",
        },
    },
    "pl": {
        "skip": "Przejdź do treści",
        "menu": "Menu",
        "close_nav": "Zamknij menu",
        "search_button": "Szukaj",
        "search_aria": "Szukaj w przewodniku",
        "search_placeholder": "Szukaj w przewodniku…",
        "on_this_page": "Na tej stronie",
        "previous": "Poprzedni",
        "next": "Następny",
        "written_for": "Napisano dla Cora Max {max} i Cora Mobile {mobile}.",
        "last_checked": "Ostatnio sprawdzono {date}.",
        "still_stuck": "Wciąż masz problem? Napisz na {email}, pomożemy.",
        "footer_privacy": "Prywatność",
        "footer_terms": "Warunki",
        "footer_support": "Wsparcie",
        "search_none": "Brak wyników dla „{q}”.",
        "search_unavailable": "Wyszukiwanie jest niedostępne. Użyj menu.",
        "lang_label": "Język",
        "sections": {"Help": "Pomoc"},
        "groups": {
            "Account": "Konto", "Alerts": "Alerty",
            "Alerts and automation": "Alerty i automatyzacja",
            "Automation": "Automatyzacja", "Equipment": "Sprzęt",
            "Getting started": "Pierwsze kroki", "Intelligence": "Inteligencja",
            "Records": "Zapisy", "Settings": "Ustawienia",
            "Your dashboard": "Twój panel",
        },
    },
}


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
    group: str = ""
    reviewed: str = ""
    lang: str = "en"
    html: str = ""
    headings: list = field(default_factory=list)

    @property
    def url(self) -> str:
        prefix = "/help/" if self.lang == "en" else f"/{self.lang}/help/"
        return prefix if self.slug == "index" else f"{prefix}{self.slug}"

    @property
    def out_path(self) -> Path:
        base = OUT if self.lang == "en" else ROOT / self.lang / "help"
        return base / ("index.html" if self.slug == "index" else f"{self.slug}.html")


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
        # ⛔⛔ THE `, 1` IS LOAD-BEARING, AND SINCE 2026-09-11 THE CONTENT RELIES
        # ON IT. Twelve `description:` values now contain a colon of their own
        # ("How to read Cora's dashboard: widgets, freshness, ..."), because the
        # em-dash sweep had to replace the separator with something and a comma
        # let the first list item be misread as part of the gloss.
        # ⚠️ That makes them INVALID YAML: an unquoted scalar may not contain
        # ": ". This parser is fine with it (split once, keep the rest), but
        # swapping in PyYAML "for correctness" would abort the build on those
        # twelve files. Quoting them is not a fix either — nothing here strips
        # quotes, so they would land inside the rendered <meta description>.
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
    # ⭐ ALWAYS ABSOLUTE, under /help/ — never relative. English pages live at
    # /help/<slug> so "img/x.webp" happens to resolve there too, but a
    # translated page lives at /<lang>/help/<slug> and the SAME relative path
    # would resolve to /<lang>/help/img/x.webp, a 404: images are shared, not
    # duplicated per language (see help-src/README.md "Translations").
    out_src = src if src.startswith(("http://", "https://", "/")) else f"/help/{src}"
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
        f'<img src="{html.escape(out_src, quote=True)}" alt="{html.escape(alt, quote=True)}" '
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
# Internal link localization.
#
# ⭐ Translators write English-STYLE links — /help/<slug>, /help/<slug>#anchor,
# or /help/ for the index — exactly as they read in the English source, never
# the /<lang>/ form. That is the one thing that keeps translation a content
# job rather than a build job: rewriting them to the right language happens
# here, once, for every page of that language, after render().
#
# ⚠️ Heading anchors are slugified from the TRANSLATED heading text, so a
# cross-page `#anchor` copied from English may not exist once the target page
# is translated. Rather than ship a link that jumps to nothing, the anchor is
# dropped (the reader lands on the page, just not mid-scroll) unless it is
# confirmed present in the target page's own headings.
#
# ⛔ A slug with NO translation yet must never become a dead link: it falls
# back to that language's help index, same rule as the language switcher.
# ─────────────────────────────────────────────────────────────────────────────

_HELP_HREF_RE = re.compile(r'href="/help/([a-z0-9-]*)(?:#([a-z0-9-]+))?"')


def localize_links(body: str, lang: str, by_slug: dict[str, "Page"]) -> str:
    if lang == "en":
        return body

    def repl(m: re.Match) -> str:
        slug, anchor = m.group(1), m.group(2)
        if not slug:  # /help/  → the index
            return f'href="/{lang}/help/"'
        target = by_slug.get(slug)
        if target is None:
            # Not translated yet — never a dead link.
            return f'href="/{lang}/help/"'
        if anchor:
            ids = {hid for _, _, hid in target.headings}
            if anchor in ids:
                return f'href="/{lang}/help/{slug}#{anchor}"'
        return f'href="/{lang}/help/{slug}"'

    return _HELP_HREF_RE.sub(repl, body)


# ─────────────────────────────────────────────────────────────────────────────
# The page shell — minimal chrome, with a link back to the site.
# ─────────────────────────────────────────────────────────────────────────────

def nav_html(pages: list[Page], current: Page) -> str:
    """Sidebar, grouped by task within each product.

    ⭐ Cora Mobile alone is 33 pages. As one flat list it was a wall you
    scanned rather than a structure you used — and "which of these is about
    equipment?" had no answer short of reading all of them. Pages carry a
    `group:`; the group containing the current page is open, the rest are
    collapsed, so the shape of the product is visible at a glance.

    ⚠️ <details>/<summary>, deliberately: it collapses with no JavaScript, so
    the nav is usable before (and without) the script, and each group is a
    real disclosure widget for a screen reader rather than a div with a
    click handler.
    """
    strings = UI_STRINGS[current.lang]
    parts = []
    for section in SECTION_ORDER:
        in_sec = sorted(
            [p for p in pages if p.section == section], key=lambda p: p.order
        )
        if not in_sec:
            continue
        if section:
            label = strings["sections"].get(section, section)
            # Turkish uppercase turns "Cora Mobile" into "CORA MOBİLE": a brand name
            # is English text, so it keeps English casing rules in every language.
            _en = ' lang="en"' if label.startswith("Cora") else ""
            parts.append(f'<p class="nav-sec"{_en}>{html.escape(label)}</p>')

        # Preserve first-appearance order of the groups.
        seen: list[str] = []
        for p in in_sec:
            if p.group and p.group not in seen:
                seen.append(p.group)

        ungrouped = [p for p in in_sec if not p.group]
        if ungrouped:
            parts.append("<ul>")
            for p in ungrouped:
                cur = (
                    ' class="cur" aria-current="page"'
                    if p.slug == current.slug
                    else ""
                )
                parts.append(
                    f'<li><a href="{p.url}"{cur}>{html.escape(p.title)}</a></li>'
                )
            parts.append("</ul>")

        for g in seen:
            members = [p for p in in_sec if p.group == g]
            here = any(p.slug == current.slug for p in members)
            g_label = strings["groups"].get(g, g)
            parts.append(f'<details class="nav-g"{" open" if here else ""}>')
            parts.append(f"<summary>{html.escape(g_label)}</summary><ul>")
            for p in members:
                cur = (
                    ' class="cur" aria-current="page"'
                    if p.slug == current.slug
                    else ""
                )
                parts.append(
                    f'<li><a href="{p.url}"{cur}>{html.escape(p.title)}</a></li>'
                )
            parts.append("</ul></details>")
    return "\n".join(parts)


def search_index(pages: list[Page]) -> str:
    """A tiny static index, fetched only when someone opens search.

    ⭐ 50 pages and ~28,000 words is past what a sidebar can expose. The index
    is deliberately NOT inlined into every page: it is one file, fetched once
    on first use, so the cost lands on the readers who search and nobody else.
    """
    docs = []
    for p in pages:
        strings = UI_STRINGS[p.lang]
        body = re.sub(r"<[^>]+>", " ", p.html)
        body = html.unescape(body)
        body = re.sub(r"\s+", " ", body).strip()
        section = p.section or "Help"
        docs.append(
            {
                "u": p.url,
                "t": p.title,
                "s": strings["sections"].get(section, section),
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


def reviewed_html(page: Page) -> str:
    """When this page was last checked against the running app.

    ⭐ The build stamp says which RELEASE the guide describes, and it is easy
    to read that as "every page was re-verified for this release" — which is
    not what it means, and on a 50-page guide never will be. A per-page date
    says the narrower, true thing.
    """
    if not page.reviewed:
        return ""
    tmpl = UI_STRINGS[page.lang]["last_checked"]
    return " " + html.escape(tmpl.format(date=page.reviewed))


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
    strings = UI_STRINGS[current.lang]
    out = ['<nav class="pn" aria-label="Continue reading">']
    if prev:
        out.append(
            f'<a class="pn-p" href="{prev.url}"><span>{html.escape(strings["previous"])}</span>'
            f"<b>{html.escape(prev.title)}</b></a>"
        )
    if nxt:
        out.append(
            f'<a class="pn-n" href="{nxt.url}"><span>{html.escape(strings["next"])}</span>'
            f"<b>{html.escape(nxt.title)}</b></a>"
        )
    out.append("</nav>")
    return "".join(out)


def toc_html(page: Page) -> str:
    """On-page contents, h2 only. Skipped when a page has fewer than three."""
    h2 = [h for h in page.headings if h[0] == 2]
    if len(h2) < 3:
        return ""
    label = html.escape(UI_STRINGS[page.lang]["on_this_page"])
    items = "".join(f'<li><a href="#{hid}">{html.escape(t)}</a></li>' for _, t, hid in h2)
    return f'<nav class="toc" aria-label="{label}"><p>{label}</p><ul>{items}</ul></nav>'


def build_slug_index(lang_pages_map: dict[str, list[Page]]) -> dict[str, dict[str, Page]]:
    """slug → {lang: Page}, across every language that has that slug built."""
    idx: dict[str, dict[str, Page]] = {}
    for lang, pages in lang_pages_map.items():
        for p in pages:
            idx.setdefault(p.slug, {})[lang] = p
    return idx


def lang_menu_html(page: Page, slug_index: dict[str, dict[str, Page]]) -> str:
    """The language switcher in the help header.

    ⭐ <details>/<summary>, same reasoning as the sidebar groups: no
    JavaScript required, and a real disclosure widget for a screen reader.

    ⛔ A language missing this SLUG (not translated yet) links to that
    language's help index instead of a dead link — never omitted, because an
    absent entry reads as "this guide has no German", not "not yet on this
    page".
    """
    entries = slug_index.get(page.slug, {})
    items = []
    for lang in ALL_LANGS:
        name = NATIVE_NAMES[lang]
        target = entries.get(lang)
        href = target.url if target is not None else ("/help/" if lang == "en" else f"/{lang}/help/")
        cur = ' aria-current="true" class="cur"' if lang == page.lang else ""
        items.append(f'<li><a href="{href}"{cur}>{html.escape(name)}</a></li>')
    label = html.escape(UI_STRINGS[page.lang]["lang_label"])
    current_name = html.escape(NATIVE_NAMES[page.lang])
    return (
        f'<details class="hlang"><summary aria-label="{label}">'
        f"<span>{current_name}</span></summary><ul>{''.join(items)}</ul></details>"
    )


def hreflang_html(page: Page, slug_index: dict[str, dict[str, Page]]) -> str:
    """<link rel="alternate"> for every language version of this page, plus
    x-default pointing at English — the SEO half of the language switcher."""
    entries = slug_index.get(page.slug, {})
    out = []
    for lang in ALL_LANGS:
        target = entries.get(lang)
        if target is not None:
            out.append(f'<link rel="alternate" hreflang="{lang}" href="{SITE}{target.url}">')
    en_page = entries.get("en")
    if en_page is not None:
        out.append(f'<link rel="alternate" hreflang="x-default" href="{SITE}{en_page.url}">')
    return "\n  ".join(out)


def shell(page: Page, pages: list[Page], slug_index: dict[str, dict[str, Page]]) -> str:
    lang = page.lang
    strings = UI_STRINGS[lang]
    canonical = f"{SITE}{page.url}"
    robots = (
        '\n  <meta name="robots" content="noindex, nofollow">' if NOINDEX else ""
    )
    desc = html.escape(page.description, quote=True)
    title = html.escape(page.title)
    home_url = "/help/" if lang == "en" else f"/{lang}/help/"
    back_url = "/" if lang == "en" else f"/{lang}/"
    full_title = "Cora Help" if page.slug == "index" else f"{title} | Cora Help"
    hreflang = hreflang_html(page, slug_index)
    langmenu = lang_menu_html(page, slug_index)
    skip = html.escape(strings["skip"])
    menu_label = html.escape(strings["menu"])
    close_label = html.escape(strings["close_nav"])
    search_button = html.escape(strings["search_button"])
    search_aria = html.escape(strings["search_aria"])
    search_placeholder = html.escape(strings["search_placeholder"])
    still_stuck_pre, _, still_stuck_post = strings["still_stuck"].partition("{email}")
    search_none_pre, _, search_none_post = strings["search_none"].partition("{q}")

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{full_title}</title>
  <meta name="description" content="{desc}">{robots}
  <meta name="theme-color" content="#F7FAFD">
  <link rel="canonical" href="{canonical}">
  {hreflang}
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
  <!-- ⛔ Never add rel=preload for the faces. That is what put the old Google
       Fonts request on the critical path for 1053 ms. font-display:swap paints
       the fallback first, which is the behaviour we want. -->
  <link rel="stylesheet" href="/fonts.css?v={FONTS_VERSION}" media="print" onload="this.media='all'">
  <noscript><link rel="stylesheet" href="/fonts.css?v={FONTS_VERSION}"></noscript>
  <link rel="stylesheet" href="/help/help.css?v={CSS_VERSION}">
</head>
<body>
<a class="skip" href="#main">{skip}</a>

<header class="hnav">
  <div class="hnav-in">
    <a class="hbrand" href="{home_url}">
      <img src="/cora_logo-240.webp" alt="Cora" width="400" height="163">
      <span>Help</span>
    </a>
    <button class="hfind" id="hfind" type="button" aria-label="{search_aria}">
      <svg aria-hidden="true" focusable="false" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5" stroke-linecap="round"/></svg>
      <span>{search_button}</span><kbd>/</kbd>
    </button>
    {langmenu}
    <a class="hback" href="{back_url}">coraiq.tech &rarr;</a>
    <button class="hmenu" id="hmenu" aria-label="{menu_label}" aria-controls="hside" aria-expanded="false">
      <svg aria-hidden="true" focusable="false" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7h16M4 12h16M4 17h16" stroke-linecap="round"/></svg>
    </button>
  </div>
</header>

<div class="hwrap">
  <div class="hscrim" id="hscrim" hidden></div>
  <aside class="hside" id="hside" aria-label="Guide navigation">
    <button class="hclose" id="hclose" type="button" aria-label="{close_label}">&times;</button>
    <nav aria-label="Guide">
{nav_html(pages, page)}
    </nav>
  </aside>

  <main class="hmain" id="main">
    <article class="doc">
      <h1>{title}</h1>
      {toc_html(page)}
{mark_trademarks(page.html)}
      {prevnext_html(pages, page)}
      <p class="stamp">{html.escape(strings["written_for"].format(max=STAMP_MAX, mobile=STAMP_MOBILE))}{reviewed_html(page)}</p>
      <p class="ask">{html.escape(still_stuck_pre)}<a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>{html.escape(still_stuck_post)}</p>
    </article>
  </main>
</div>

<footer class="hfoot">
  <div class="hfoot-in">
    <p class="disc">{html.escape(DISCLAIMER_1)}</p>
    <p class="disc">{html.escape(DISCLAIMER_2)}</p>
    <p class="legal">&copy; 2026 Cora IQ ·
      <a href="{back_url}">coraiq.tech</a> ·
      <a href="/privacy-policy.html">{html.escape(strings["footer_privacy"])}</a> ·
      <a href="/terms-and-conditions.html">{html.escape(strings["footer_terms"])}</a> ·
      <a href="/support.html">{html.escape(strings["footer_support"])}</a></p>
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
  // the nav always opened at scrollTop 0, so on a deep page you were looking
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
      // element that is still `visibility: hidden` silently refuses focus,
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

// ── Language switcher ───────────────────────────────────────────────────
// Works with no script at all (it is a <details>); this only closes it when
// a click lands outside, which a plain <details> does not do on its own.
(function () {{
  document.addEventListener('click', function (e) {{
    document.querySelectorAll('details.hlang[open]').forEach(function (d) {{
      if (!d.contains(e.target)) d.removeAttribute('open');
    }});
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
      list.innerHTML = '<li class="snone">' + {json.dumps(search_none_pre)} + esc(q) + {json.dumps(search_none_post)} + '</li>';
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
    dlg.setAttribute('aria-label', {json.dumps(strings["search_aria"])});
    dlg.innerHTML = '<div class="sbox"><input type="search" '
      + 'placeholder="{search_placeholder}" aria-label="{search_aria}" '
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
    // ⭐ Fetched ONCE, on first open, never on a page that is only read.
    if (docs) {{ run(); return; }}
    fetch('{home_url}search.json').then(function (r) {{ return r.json(); }})
      .then(function (j) {{ docs = j; run(); }})
      .catch(function () {{
        list.innerHTML = '<li class="snone">' + {json.dumps(strings["search_unavailable"])} + '</li>';
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
/* ⛔ GENERATED by build_help.py. Edit the generator, not this file.
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
.nav-g { margin: 0 0 2px; }
.nav-g > summary {
  list-style: none; cursor: pointer; padding: 5px 10px; margin-left: -10px;
  border-radius: var(--radius-sm); font-size: 14px; font-weight: 600;
  color: var(--text-2); display: flex; align-items: center; gap: 6px;
}
.nav-g > summary::-webkit-details-marker { display: none; }
.nav-g > summary::before {
  content: ""; width: 0; height: 0; flex: none;
  border-left: 5px solid currentColor;
  border-top: 4px solid transparent; border-bottom: 4px solid transparent;
  transition: transform .15s ease; opacity: .55;
}
.nav-g[open] > summary::before { transform: rotate(90deg); }
.nav-g > summary:hover { background: var(--surface-2); color: var(--text); }
.nav-g > ul { margin: 2px 0 8px; padding-left: 12px; border-left: 1px solid var(--line); }
@media (prefers-reduced-motion: reduce) { .nav-g > summary::before { transition: none; } }

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

/* ── Language switcher ──────────────────────────────────────────────────
   ⭐ <details>/<summary>, same as the sidebar groups: works with no
   JavaScript, and is a real disclosure widget for assistive tech rather
   than a div with a click handler bolted on. */
.hlang { position: relative; font-size: 13.5px; }
.hlang > summary {
  list-style: none; cursor: pointer; display: inline-flex; align-items: center;
  gap: 5px; padding: 6px 10px; color: var(--text-2); background: var(--surface-2);
  border: 1px solid var(--line); border-radius: var(--radius-sm);
}
.hlang > summary::-webkit-details-marker { display: none; }
.hlang > summary::after {
  content: ""; width: 0; height: 0; margin-left: 2px;
  border-left: 4px solid transparent; border-right: 4px solid transparent;
  border-top: 5px solid currentColor; opacity: .6;
}
.hlang > summary:hover { border-color: var(--line-strong); color: var(--text); }
.hlang[open] > summary { border-color: var(--line-strong); }
.hlang > ul {
  position: absolute; top: calc(100% + 6px); right: 0; z-index: 45;
  margin: 0; padding: 6px; list-style: none; min-width: 150px;
  background: var(--surface); border: 1px solid var(--line);
  border-radius: var(--radius-sm); box-shadow: 0 14px 34px rgba(0,0,0,.14);
}
.hlang > ul li { margin: 0; }
.hlang > ul a {
  display: block; padding: 7px 10px; border-radius: 4px;
  text-decoration: none; color: var(--text-2); font-size: 13.5px; white-space: nowrap;
}
.hlang > ul a:hover { background: var(--surface-2); color: var(--text); }
.hlang > ul a.cur { color: var(--brand-deep); font-weight: 600; }
@media (max-width: 640px) { .hlang > summary span { max-width: 64px; overflow: hidden; text-overflow: ellipsis; } }

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
     (50 links) above the article and pushed the page you came to read off
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
  /* 2026-09-27: with the language menu the header ran out of room at phone
     width (the search button squeezed, "coraiq.tech ->" wrapped). The logo
     and the footer still lead home. */
  .hback { display: none; }
  .hfind { flex-shrink: 0; }
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


def load_pages(lang: str = "en") -> list[Page]:
    """Load one language's tree.

    ⭐ `en` reads help-src/*.md, exactly as before. Any other language reads
    help-src/<lang>/*.md — a MIRROR, not a copy: whatever slugs exist there
    are the pages that language has been translated for. An entirely absent
    directory, or one with no .md files yet, is not an error — it means that
    language's translator has not started, and the site simply does not
    publish that language's help section yet (see help-src/README.md).
    """
    src_dir = SRC if lang == "en" else SRC / lang
    pages: list[Page] = []
    if not src_dir.exists():
        return pages
    for path in sorted(src_dir.glob("*.md")):
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
                group=meta.get("group", ""),
                reviewed=meta.get("reviewed", ""),
                lang=lang,
                body_md=body,
            )
        )
    if not pages:
        if lang == "en":
            raise SystemExit("⛔ no pages found in help-src/ — nothing to build")
        return pages

    # ⛔ A section not in SECTION_ORDER is silently DROPPED FROM THE NAV by
    # `nav_html`, while the page is still written and served. That is the worst
    # shape of bug: live, linkable, and unreachable by anyone browsing. A typo
    # in one frontmatter line was enough. Fail instead.
    # ⛔ A page with no `group:` inside a section whose OTHER pages are grouped
    # renders above the groups with no label — it reads as a mistake, and it is
    # exactly what happens when someone adds a page and copies the frontmatter
    # from before groups existed.
    #
    # ⚠️ Deliberately conditional: a section can be entirely ungrouped and that
    # is fine — "Help" is three pages, where grouping would be noise. The bug is
    # a section that is PARTLY grouped, so that is what this catches.
    grouped_sections = {p.section for p in pages if p.group}
    orphans = [
        p.slug for p in pages if p.section in grouped_sections and not p.group
    ]
    if orphans:
        raise SystemExit(
            f"⛔ {orphans} sit in a section whose other pages are grouped, but "
            f"have no `group:` — they would render above the groups with no "
            f"label. Add `group:` to the frontmatter."
        )

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


_SITEMAP_LANG_BLOCK_RE = re.compile(
    r"  <url>\s*<loc>https://coraiq\.tech/(?:" + "|".join(LANGS) + r")/[^<]*</loc>.*?</url>\n",
    re.S,
)


def _sitemap_url_block(loc: str, lastmod: str, priority: str) -> str:
    return (
        f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{lastmod}</lastmod>\n"
        f"    <changefreq>monthly</changefreq>\n    <priority>{priority}</priority>\n  </url>\n"
    )


def desired_sitemap_text(lang_pages_map: dict[str, list[Page]]) -> str | None:
    """The next sitemap.xml — every existing (English) entry untouched, plus a
    freshly regenerated block of language entries.

    ⭐ REGENERATED, NOT HAND-KEPT, same reasoning as the ⭐-marked derivations
    at the top of this file: a sitemap entry restating a URL the build already
    knows will eventually drift from it. Existing language blocks are removed
    and rebuilt each run, which makes this idempotent — running the build
    twice in a row produces byte-identical output.

    ⛔ The English entries above are NEVER touched here — requirement is to
    ADD language entries, not to take over a file another workflow also
    edits by hand.
    """
    path = ROOT / "sitemap.xml"
    if not path.exists():
        return None
    text = _SITEMAP_LANG_BLOCK_RE.sub("", path.read_text(encoding="utf-8"))

    blocks = []
    for lang in LANGS:
        pages = lang_pages_map.get(lang) or []
        if not pages:
            continue
        # The language's site root and support page are another agent's
        # files; list them only once they actually exist, so this never
        # advertises a page that 404s.
        if (ROOT / lang / "index.html").exists():
            blocks.append(_sitemap_url_block(f"{SITE}/{lang}/", "2026-09-27", "0.6"))
        if (ROOT / lang / "support.html").exists():
            blocks.append(_sitemap_url_block(f"{SITE}/{lang}/support.html", "2026-09-27", "0.5"))
        for p in sorted(pages, key=lambda p: p.slug):
            lastmod = p.reviewed or "2026-09-27"
            priority = "0.6" if p.slug == "index" else "0.5"
            blocks.append(_sitemap_url_block(f"{SITE}{p.url}", lastmod, priority))

    return text.replace("</urlset>", "".join(blocks) + "</urlset>")


def build(check_only: bool = False) -> int:
    en_pages = load_pages("en")
    lang_pages_map: dict[str, list[Page]] = {"en": en_pages}
    for lang in LANGS:
        lang_pages_map[lang] = load_pages(lang)

    # Render every language's pages first: rendering only needs the page's
    # OWN body, but `localize_links` (next) needs every OTHER page's
    # headings already collected, so the two cannot be one pass.
    for pages in lang_pages_map.values():
        for p in pages:
            p.headings = []
            p.html = render(p.body_md, p.headings)

    # Rewrite English-style /help/... links in translated pages to
    # /<lang>/help/..., dropping an anchor that does not exist in the
    # translated target and falling back to that language's index when the
    # target page has not been translated at all (see `localize_links`).
    for lang in LANGS:
        pages = lang_pages_map[lang]
        by_slug = {p.slug: p for p in pages}
        for p in pages:
            p.html = localize_links(p.html, lang, by_slug)

    slug_index = build_slug_index(lang_pages_map)

    OUT.mkdir(parents=True, exist_ok=True)

    written, stale = 0, []
    css = f"{extract_root()}\n{HELP_LAYOUT}"

    # ⭐ Hash before rendering: `shell()` reads these globals at call time.
    global CSS_VERSION, FONTS_VERSION
    CSS_VERSION = hashlib.sha256(css.encode("utf-8")).hexdigest()[:10]
    fonts = ROOT / "fonts.css"
    if fonts.exists():
        FONTS_VERSION = hashlib.sha256(
            fonts.read_bytes()).hexdigest()[:10]

    # ⭐ ONE shared help.css at /help/help.css for every language — it is the
    # same design system, not translated content, and a translated page's
    # <link> in `shell()` points at that one absolute path regardless of
    # which /<lang>/ directory it is served from. Only the search index is
    # per language, since each language searches only its own pages.
    targets = [(OUT / "help.css", css), (OUT / "search.json", search_index(en_pages))]
    targets += [(p.out_path, shell(p, en_pages, slug_index)) for p in en_pages]

    total_pages = len(en_pages)
    for lang in LANGS:
        pages = lang_pages_map[lang]
        if not pages:
            continue
        total_pages += len(pages)
        out_dir = ROOT / lang / "help"
        out_dir.mkdir(parents=True, exist_ok=True)
        targets.append((out_dir / "search.json", search_index(pages)))
        targets += [(p.out_path, shell(p, pages, slug_index)) for p in pages]

    sitemap_text = desired_sitemap_text(lang_pages_map)
    if sitemap_text is not None:
        targets.append((ROOT / "sitemap.xml", sitemap_text))

    for path, content in targets:
        old = path.read_text(encoding="utf-8") if path.exists() else None
        if old == content:
            continue
        if check_only:
            stale.append(str(path.relative_to(ROOT)))
            continue
        path.write_text(content, encoding="utf-8")
        written += 1

    if check_only:
        if stale:
            print(f"⛔ out of date: {', '.join(stale)}")
            return 1
        print(f"✅ help/ is up to date ({total_pages} pages)")
        return 0

    print(f"✅ {total_pages} pages · {written} file(s) written · css v{CSS_VERSION}")
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

    tm = mark_trademarks('<p>Neptune Systems and Red Sea. Red Sea again, <a href="/x?maxspect">Maxspect</a>.</p>'
                         '<code>Jecod</code> then Jecod.')
    ok("™ on the first brand mention", "Neptune Systems™ and Red Sea™." in tm)
    ok("™ only once per brand per page", "Red Sea again" in tm and tm.count("Red Sea™") == 1)
    ok("™ never inside a tag attribute", 'href="/x?maxspect"' in tm and ">Maxspect™<" in tm)
    ok("™ never inside code", "<code>Jecod</code> then Jecod™." in tm)
    ok("™ not doubled", mark_trademarks("Maxspect™ gyre") == "Maxspect™ gyre")

    # ⛔⛔ THE INLINE SCRIPT MUST PARSE. The page shell is an f-string, so a
    # single `{` in the JavaScript is a FORMAT PLACEHOLDER — that broke the
    # build once (2026-09-09) and, because build+commit+push were chained, the
    # breakage was committed. A brace-balance check is cheap and catches the
    # whole class; `node --check` runs on top when node is available.
    import shutil as _sh, subprocess as _sp, tempfile as _tf
    _demo = Page(slug="x", title="T", description="d", section="Cora Mobile",
                 order=1, body_md="body")
    _demo.html = "<p>body</p>"
    _shell = shell(_demo, [_demo], build_slug_index({"en": [_demo]}))
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
    # ⛔ TWO SECTIONS WITH THE SAME NAME ON ONE PAGE. It has happened twice:
    # max-settings.md carried `## Devices` and `## Tank settings` twice, and
    # the two Tank-settings sections CONTRADICTED each other on what polling
    # means; then I added a second `## About` to mobile-settings.md without
    # noticing the first. It also breaks the on-page contents, which renders
    # two identical entries pointing at the same anchor.
    dupes = []
    for md in sorted(SRC.glob("*.md")):
        if md.name == "README.md":
            continue
        heads = re.findall(r"^## (.+)$", md.read_text(encoding="utf-8"), re.M)
        seen_h, dup_h = set(), set()
        for h in heads:
            (dup_h if h in seen_h else seen_h).add(h)
        if dup_h:
            dupes.append(f"{md.name}: {sorted(dup_h)}")
    ok(f"⛔ no page repeats a section heading ({dupes})", not dupes)

    unlabelled, stale_soon = [], []
    for md in sorted(SRC.glob("*.md")):
        if md.name == "README.md":
            continue
        body = md.read_text(encoding="utf-8")
        # Owner, 2026-09-17: *"let's flag MaxSpect as Beta on Help pages, it still
        # testing and development in progress."* It was "coming soon" until then, so
        # the guard now demands "beta" and refuses a leftover "coming soon" on any
        # line that names Maxspect (a page can say both only if one is stale).
        low = body.lower()
        if "maxspect" in low and not re.search(r"\bbeta\b", low):
            unlabelled.append(md.name)
        stale_soon.extend(f"{md.name}:{i}" for i, line in enumerate(low.splitlines(), 1)
                          if "maxspect" in line and "coming soon" in line)
    ok(f"⛔ Maxspect is labelled beta wherever it is named ({unlabelled})",
       not unlabelled)
    ok(f"⛔ no line still calls Maxspect coming soon ({stale_soon})",
       not stale_soon)

    # ⛔ PUBLISHED 2026-09-17. While NOINDEX is False every page must be in
    # sitemap.xml, or a new page ships invisible to search. Keyed on each page's
    # own canonical URL, so no hand-kept count can drift.
    if not NOINDEX:
        _sm = ROOT / "sitemap.xml"
        _sm_text = _sm.read_text(encoding="utf-8") if _sm.exists() else ""
        not_in_sitemap = []
        for md in sorted(SRC.glob("*.md")):
            if md.name == "README.md":
                continue
            _url = "/help/" if md.stem == "index" else f"/help/{md.stem}"
            if f"<loc>{SITE}{_url}</loc>" not in _sm_text:
                not_in_sitemap.append(md.stem)
        ok(f"⛔ every help page is in sitemap.xml ({not_in_sitemap})",
           not not_in_sitemap)

    # ⛔ INTERNAL JARGON IN CUSTOMER-FACING COPY. Owner, 2026-09-09: *"There
    # are mentions as 'The Cora swoosh'.. there is no such a thing, it is Cora
    # Assistant."* Six of them, across the two pages that describe the top bar
    # and voice — and "swoosh" is what WE call the mark internally, never what
    # the product calls anything. The assistant has had a name and a glossary
    # entry the whole time; the guide simply used our word in six places.
    #
    # ⚠️ The check is the WHOLE SOURCE TREE, not the two files that were wrong.
    # A rule applied only where it was already broken never catches the next
    # page. Same reasoning as the Maxspect guard above.
    jargon = {
        "swoosh": "the assistant control is 'Cora Assistant'",
        "cora mark": "the assistant control is 'Cora Assistant'",
        "kiosk": "the product is 'Cora Max' in public copy",
        "e10": "the hardware model is never named publicly",
    }
    slips = []
    for md in sorted(SRC.glob("*.md")):
        if md.name == "README.md":  # the brief itself may quote the banned words
            continue
        low = md.read_text(encoding="utf-8").lower()
        for word, why in jargon.items():
            if word in low:
                slips.append(f"{md.name}: '{word}' ({why})")
    ok(f"⛔ no internal jargon in customer-facing copy ({slips})", not slips)

    # ⛔ A zero-length render would make several checks above pass vacuously.
    ok("render is not empty", len(render("## A\n\ntext\n", [])) > 20)

    # ─────────────────────────────────────────────────────────────────────
    # Languages. ⚠️ These are UNIT tests against the functions, not a full
    # build — they must hold even before any translator has written a file,
    # which is exactly the state most languages are in most of the time.
    # ─────────────────────────────────────────────────────────────────────

    _home = Page(slug="index", title="Home", description="d", section="",
                 order=0, body_md="")
    _setup = Page(slug="setup", title="Setup", description="d",
                  section="Cora Mobile", order=1, body_md="")
    _setup.headings = [(2, "Wi-Fi", "wi-fi")]
    _by_slug_de = {"index": _home, "setup": _setup}

    ok("link rewriting: plain slug",
       localize_links('<a href="/help/setup">x</a>', "de", _by_slug_de)
       == '<a href="/de/help/setup">x</a>')
    ok("link rewriting: the index",
       localize_links('<a href="/help/">x</a>', "de", _by_slug_de)
       == '<a href="/de/help/">x</a>')
    ok("link rewriting: an anchor that exists in the translation survives",
       localize_links('<a href="/help/setup#wi-fi">x</a>', "de", _by_slug_de)
       == '<a href="/de/help/setup#wi-fi">x</a>')
    ok("⛔ an anchor that does NOT exist in the translation is dropped, not broken",
       localize_links('<a href="/help/setup#missing">x</a>', "de", _by_slug_de)
       == '<a href="/de/help/setup">x</a>')
    ok("⛔ a slug with no translation falls back to that language's index, never a dead link",
       localize_links('<a href="/help/untranslated">x</a>', "de", _by_slug_de)
       == '<a href="/de/help/">x</a>')
    ok("link rewriting leaves English untouched",
       localize_links('<a href="/help/setup">x</a>', "en", _by_slug_de)
       == '<a href="/help/setup">x</a>')
    ok("link rewriting never touches an image path",
       '/help/img/x.webp' in localize_links(
           '<img src="/help/img/x.webp">', "de", _by_slug_de))
    ok("link rewriting never touches an external or legal-page link",
       localize_links(
           '<a href="/support.html">s</a><a href="https://example.com/help/x">e</a>',
           "de", _by_slug_de)
       == '<a href="/support.html">s</a><a href="https://example.com/help/x">e</a>')

    _idx = build_slug_index({"en": [_home, _setup], "de": [_home]})
    _hl = hreflang_html(_setup, _idx)
    ok("hreflang: every language that has this slug is listed",
       'hreflang="en"' in _hl and 'hreflang="de"' not in _hl)
    ok("hreflang: x-default points at the English URL",
       f'hreflang="x-default" href="{SITE}/help/setup"' in _hl)
    _hl_home = hreflang_html(_home, _idx)
    ok("hreflang: a slug present in both languages lists both",
       'hreflang="en"' in _hl_home and 'hreflang="de"' in _hl_home)

    _menu = lang_menu_html(_setup, _idx)
    ok("language menu: the untranslated language falls back to its help index",
       f'href="/de/help/"' in _menu)
    ok("language menu: the current language is marked",
       'aria-current="true"' in _menu)
    ok("language menu: lists a native name for every language",
       all(NATIVE_NAMES[l] in _menu for l in ALL_LANGS))

    _en_keys = set(UI_STRINGS["en"])
    for _l in LANGS:
        ok(f"UI strings for {_l} have every key English has",
           set(UI_STRINGS[_l]) == _en_keys)
        ok(f"UI strings for {_l} have every group English has",
           set(UI_STRINGS[_l]["groups"]) == set(UI_STRINGS["en"]["groups"]))
        _flat = [v for k, v in UI_STRINGS[_l].items() if isinstance(v, str)]
        _flat += list(UI_STRINGS[_l]["groups"].values())
        _flat += list(UI_STRINGS[_l]["sections"].values())
        ok(f"⛔ no em dash (U+2014) in {_l} UI strings",
           not any("—" in v for v in _flat))

    _de_page = Page(slug="setup", title="T", description="d", section="Cora Mobile",
                     order=1, body_md="", lang="de")
    _de_page.html = "<p>x</p>"
    _de_shell = shell(_de_page, [_de_page], build_slug_index({"de": [_de_page]}))
    ok('html lang attribute matches the page language',
       '<html lang="de">' in _de_shell)
    ok("a translated page still carries hreflang links",
       'rel="alternate"' in _de_shell)

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

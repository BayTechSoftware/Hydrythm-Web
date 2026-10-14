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
import os
import re
import sys
import unicodedata
from dataclasses import dataclass, field
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
# ⭐ `HELP_SRC` points the build at another source tree with the same layout
# (used by the private prepare step to build from the full source, see
# help-src/README.md). Unset, it is this repo's help-src/.
SRC = Path(os.environ["HELP_SRC"]).resolve() if os.environ.get("HELP_SRC") else ROOT / "help-src"
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
# ⛔ Only brands the published guide names. A brand whose integration is still
# hidden gets its row here in the same change that makes it public.
TRADEMARKS = [
    ("neptune", r"Neptune Systems|Neptune"),
    ("redsea", r"Red Sea"),
    ("jecod", r"Jecod"),
    ("jebao", r"Jebao"),
    ("aquawiz", r"AquaWiz"),
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
        "breadcrumb": "Breadcrumb",
        "guide_nav": "Guide navigation",
        "guide": "Guide",
        "continue_reading": "Continue reading",
        "enlarge": "Enlarge: {alt}",
        "screenshot": "Screenshot",
        "close": "Close",
        "shot_to_come": "Screenshot to come",
        "twin_max": "On Cora Max: {title}",
        "twin_mobile": "On Cora Mobile: {title}",
        "search_try": "Try fewer or different words, or go to:",
        "contact_support": "Contact support",
        "az_label": "Terms A to Z",
        "lang_label": "Language",
        "sections": {"Help": "Help"},
        "groups": {
            "Account": "Account", "Alerts": "Alerts",
            "Alerts and automation": "Alerts and automation",
            "Automation": "Automation", "Equipment": "Equipment",
            "Getting started": "Getting started", "Intelligence": "Intelligence",
            "Settings and account": "Settings and account",
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
        "breadcrumb": "Navigationspfad",
        "guide_nav": "Navigation der Anleitung",
        "guide": "Anleitung",
        "continue_reading": "Weiterlesen",
        "enlarge": "Vergrößern: {alt}",
        "screenshot": "Bildschirmfoto",
        "close": "Schließen",
        "shot_to_come": "Bildschirmfoto folgt",
        "twin_max": "Auf Cora Max: {title}",
        "twin_mobile": "In Cora Mobile: {title}",
        "search_try": "Versuche es mit weniger oder anderen Wörtern, oder gehe zu:",
        "contact_support": "Support kontaktieren",
        "az_label": "Begriffe von A bis Z",
        "lang_label": "Sprache",
        "sections": {"Help": "Hilfe"},
        "groups": {
            "Account": "Konto", "Alerts": "Warnungen",
            "Alerts and automation": "Warnungen und Automatisierung",
            "Automation": "Automatisierung", "Equipment": "Geräte",
            "Getting started": "Erste Schritte", "Intelligence": "Intelligenz",
            "Settings and account": "Einstellungen und Konto",
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
        "breadcrumb": "Fil d’Ariane",
        "guide_nav": "Navigation du guide",
        "guide": "Guide",
        "continue_reading": "Poursuivre la lecture",
        "enlarge": "Agrandir : {alt}",
        "screenshot": "Capture d’écran",
        "close": "Fermer",
        "shot_to_come": "Capture d’écran à venir",
        "twin_max": "Sur Cora Max : {title}",
        "twin_mobile": "Dans Cora Mobile : {title}",
        "search_try": "Essayez avec moins de mots ou d’autres mots, ou consultez :",
        "contact_support": "Contacter l’assistance",
        "az_label": "Termes de A à Z",
        "lang_label": "Langue",
        "sections": {"Help": "Aide"},
        "groups": {
            "Account": "Compte", "Alerts": "Alertes",
            "Alerts and automation": "Alertes et automatisation",
            "Automation": "Automatisation", "Equipment": "Équipement",
            "Getting started": "Prise en main", "Intelligence": "Intelligence",
            "Settings and account": "Paramètres et compte",
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
        "breadcrumb": "Gezinme yolu",
        "guide_nav": "Kılavuz gezinmesi",
        "guide": "Kılavuz",
        "continue_reading": "Okumaya devam edin",
        "enlarge": "Büyüt: {alt}",
        "screenshot": "Ekran görüntüsü",
        "close": "Kapat",
        "shot_to_come": "Ekran görüntüsü yakında",
        "twin_max": "Cora Max'te: {title}",
        "twin_mobile": "Cora Mobile'da: {title}",
        "search_try": "Daha az ya da farklı kelimeler deneyin veya şuraya gidin:",
        "contact_support": "Destekle iletişime geçin",
        "az_label": "A'dan Z'ye terimler",
        "lang_label": "Dil",
        "sections": {"Help": "Yardım"},
        "groups": {
            "Account": "Hesap", "Alerts": "Uyarılar",
            "Alerts and automation": "Uyarılar ve otomasyon",
            "Automation": "Otomasyon", "Equipment": "Ekipman",
            "Getting started": "Başlarken", "Intelligence": "Zeka",
            "Settings and account": "Ayarlar ve hesap",
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
        "breadcrumb": "Percorso di navigazione",
        "guide_nav": "Navigazione della guida",
        "guide": "Guida",
        "continue_reading": "Continua a leggere",
        "enlarge": "Ingrandisci: {alt}",
        "screenshot": "Screenshot",
        "close": "Chiudi",
        "shot_to_come": "Screenshot in arrivo",
        "twin_max": "Su Cora Max: {title}",
        "twin_mobile": "In Cora Mobile: {title}",
        "search_try": "Prova con meno parole o con parole diverse, oppure vai a:",
        "contact_support": "Contatta l’assistenza",
        "az_label": "Termini dalla A alla Z",
        "lang_label": "Lingua",
        "sections": {"Help": "Aiuto"},
        "groups": {
            "Account": "Account", "Alerts": "Avvisi",
            "Alerts and automation": "Avvisi e automazione",
            "Automation": "Automazione", "Equipment": "Apparecchiature",
            "Getting started": "Per iniziare", "Intelligence": "Intelligenza",
            "Settings and account": "Impostazioni e account",
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
        "breadcrumb": "Ruta de navegación",
        "guide_nav": "Navegación de la guía",
        "guide": "Guía",
        "continue_reading": "Seguir leyendo",
        "enlarge": "Ampliar: {alt}",
        "screenshot": "Captura de pantalla",
        "close": "Cerrar",
        "shot_to_come": "Captura de pantalla próximamente",
        "twin_max": "En Cora Max: {title}",
        "twin_mobile": "En Cora Mobile: {title}",
        "search_try": "Prueba con menos palabras o con otras distintas, o ve a:",
        "contact_support": "Contactar con soporte",
        "az_label": "Términos de la A a la Z",
        "lang_label": "Idioma",
        "sections": {"Help": "Ayuda"},
        "groups": {
            "Account": "Cuenta", "Alerts": "Alertas",
            "Alerts and automation": "Alertas y automatización",
            "Automation": "Automatización", "Equipment": "Equipos",
            "Getting started": "Primeros pasos", "Intelligence": "Inteligencia",
            "Settings and account": "Ajustes y cuenta",
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
        "breadcrumb": "Ścieżka nawigacji",
        "guide_nav": "Nawigacja po przewodniku",
        "guide": "Przewodnik",
        "continue_reading": "Czytaj dalej",
        "enlarge": "Powiększ: {alt}",
        "screenshot": "Zrzut ekranu",
        "close": "Zamknij",
        "shot_to_come": "Zrzut ekranu wkrótce",
        "twin_max": "W Cora Max: {title}",
        "twin_mobile": "W Cora Mobile: {title}",
        "search_try": "Spróbuj użyć mniej słów lub innych słów albo przejdź do:",
        "contact_support": "Skontaktuj się z pomocą",
        "az_label": "Pojęcia od A do Z",
        "lang_label": "Język",
        "sections": {"Help": "Pomoc"},
        "groups": {
            "Account": "Konto", "Alerts": "Alerty",
            "Alerts and automation": "Alerty i automatyzacja",
            "Automation": "Automatyzacja", "Equipment": "Sprzęt",
            "Getting started": "Pierwsze kroki", "Intelligence": "Inteligencja",
            "Settings and account": "Ustawienia i konto",
            "Records": "Zapisy", "Settings": "Ustawienia",
            "Your dashboard": "Twój panel",
        },
    },
}


# ─────────────────────────────────────────────────────────────────────────────
# Search vocabulary (R1-02, 2026-10-13).
#
# ⭐ Each row is a set of words a reader may type for the SAME thing. A query
# word (or 2-3 word phrase) found in a row matches ANY word of that row, so
# "offline" finds "stopped reporting" and "cancel subscription" finds Plans.
# Matching is case-, accent- and hyphen-blind on both sides (wifi = Wi-Fi =
# wi fi, dos = DŌS), and always at the START of a word, so "ato" no longer
# hits "automation". Rows are per language because the words are; brand and
# chemistry rows that are the same everywhere live in SYN_COMMON.
#
# ⚠️ Keep rows TIGHT. A row is an OR, so a loose one ("pump" = "light")
# quietly floods every query that uses it. Add a word only when someone would
# really type it for that exact thing. STOPWORDS are dropped from a query
# ("how do I add an apex" searches "add apex") unless nothing else is left.
# ─────────────────────────────────────────────────────────────────────────────

SYN_COMMON = [
    ["jebao", "jecod"],
    ["alk", "alkalinity", "kh", "dkh"],
    ["ato", "top off", "auto top off", "topoff", "top up"],
    ["wifi", "wlan", "wireless"],
    ["dos", "doser", "dosing pump"],
    ["apex", "neptune"],
    ["reefbeat", "red sea"],
    ["icp", "triton", "water test lab"],
    # ⛔ No rows for hidden features: this list ships inside every
    # search.json, and nothing published may name one.
]

SYNONYMS = {
    "en": [
        ["offline", "not connected", "stopped reporting", "not reporting", "unreachable",
         "cannot be reached", "disconnected", "no data"],
        ["notification", "push", "alert"],
        ["subscription", "plan", "billing", "unsubscribe", "premium"],
        ["cancel", "unsubscribe"],
        ["probe", "sensor"],
        ["delete", "remove"],
        ["dosing", "doser", "dose"],
        ["fahrenheit", "celsius", "units", "display units"],
        ["hey cora", "wake word", "voice"],
        ["tablet", "cora max", "wall screen"],
        ["phone", "cora mobile"],
        ["sign in", "log in", "login", "password"],
        ["wavemaker", "powerhead", "wave pump", "gyre"],
        ["outlet", "socket", "plug", "power strip", "energy bar"],
        ["update", "upgrade", "firmware"],
        ["light", "led", "lighting"],
    ],
    "de": [
        ["offline", "nicht verbunden", "keine daten", "meldet nicht", "nicht erreichbar", "getrennt"],
        ["benachrichtigung", "push", "warnung", "alarm"],
        ["abo", "abonnement", "tarif", "plan", "kündigen", "abrechnung"],
        ["sonde", "sensor", "fühler"],
        ["löschen", "entfernen"],
        ["dosierung", "dosierer", "dosierpumpe", "dosieren"],
        ["fahrenheit", "celsius", "einheit", "einheiten"],
        ["hey cora", "aktivierungswort", "sprache", "stimme"],
        ["tablet", "cora max", "wandbildschirm"],
        ["handy", "smartphone", "telefon", "cora mobile"],
        ["anmelden", "login", "passwort", "einloggen"],
        ["strömungspumpe", "wavemaker", "gyre"],
        ["steckdose", "steckdosenleiste", "outlet"],
        ["update", "aktualisierung", "firmware"],
        ["licht", "beleuchtung", "lampe", "led"],
        ["nachfüllung", "nachfüllanlage", "ato"],
    ],
    "fr": [
        ["hors ligne", "deconnecte", "non connecte", "ne remonte plus", "injoignable", "pas de donnees"],
        ["notification", "push", "alerte"],
        ["abonnement", "forfait", "offre", "resilier", "facturation"],
        ["sonde", "capteur"],
        ["supprimer", "retirer", "effacer"],
        ["dosage", "doseuse", "pompe doseuse", "doser"],
        ["fahrenheit", "celsius", "unite", "unites"],
        ["hey cora", "mot d'activation", "voix"],
        ["tablette", "cora max", "ecran mural"],
        ["telephone", "smartphone", "cora mobile"],
        ["connexion", "se connecter", "mot de passe", "identifiant"],
        ["pompe de brassage", "brassage", "wavemaker", "gyre"],
        ["prise", "multiprise", "bloc multiprise"],
        ["mise a jour", "firmware", "micrologiciel"],
        ["eclairage", "lumiere", "rampe", "led"],
        ["osmolateur", "remise a niveau", "ato"],
    ],
    "tr": [
        ["cevrimdisi", "baglanti yok", "bagli degil", "veri yok", "ulasilamiyor", "raporlamayi durdurdu"],
        ["bildirim", "push", "uyari", "alarm"],
        ["abonelik", "plan", "uyelik", "iptal", "fatura"],
        ["prob", "sensor", "sonda"],
        ["sil", "silme", "kaldir"],
        ["dozlama", "dozaj", "dozaj pompasi", "dozer"],
        ["fahrenheit", "celsius", "birim", "birimler"],
        ["hey cora", "uyandirma kelimesi", "ses", "sesli"],
        ["tablet", "cora max", "duvar ekrani"],
        ["telefon", "cep telefonu", "cora mobile"],
        ["giris", "oturum", "sifre", "parola"],
        ["dalga pompasi", "akinti pompasi", "wavemaker", "gyre"],
        ["priz", "grup priz", "outlet"],
        ["guncelleme", "guncelle", "firmware", "yazilim"],
        ["isik", "aydinlatma", "led"],
        ["otomatik su tamamlama", "su tamamlama", "ato"],
    ],
    "it": [
        ["offline", "non connesso", "disconnesso", "nessun dato", "non raggiungibile", "non invia"],
        ["notifica", "notifiche", "push", "avviso", "allarme"],
        ["abbonamento", "piano", "disdire", "annullare", "fatturazione"],
        ["sonda", "sensore"],
        ["eliminare", "elimina", "rimuovere", "rimuovi", "cancellare"],
        ["dosaggio", "dosometrica", "pompa dosatrice", "dosatore"],
        ["fahrenheit", "celsius", "unita"],
        ["hey cora", "parola di attivazione", "voce"],
        ["tablet", "cora max", "schermo a parete"],
        ["telefono", "smartphone", "cellulare", "cora mobile"],
        ["accesso", "accedere", "login", "password"],
        ["pompa di movimento", "movimento", "wavemaker", "gyre"],
        ["presa", "ciabatta", "multipresa"],
        ["aggiornamento", "aggiornare", "firmware"],
        ["luce", "illuminazione", "plafoniera", "led"],
        ["rabbocco", "rabbocco automatico", "ato"],
    ],
    "es": [
        ["sin conexion", "desconectado", "offline", "no conectado", "sin datos", "no responde"],
        ["notificacion", "notificaciones", "push", "alerta", "aviso"],
        ["suscripcion", "plan", "cancelar", "facturacion", "darse de baja"],
        ["sonda", "sensor"],
        ["eliminar", "borrar", "quitar"],
        ["dosificacion", "dosificadora", "bomba dosificadora", "dosificar"],
        ["fahrenheit", "celsius", "unidad", "unidades"],
        ["hey cora", "palabra de activacion", "voz"],
        ["tableta", "tablet", "cora max", "pantalla de pared"],
        ["telefono", "movil", "celular", "cora mobile"],
        ["iniciar sesion", "acceso", "contrasena", "login"],
        ["bomba de recirculacion", "bomba de corriente", "wavemaker", "gyre"],
        ["enchufe", "regleta", "toma"],
        ["actualizacion", "actualizar", "firmware"],
        ["luz", "iluminacion", "pantalla led", "led"],
        ["reposicion", "rellenado automatico", "ato"],
    ],
    "pl": [
        ["offline", "brak polaczenia", "rozlaczony", "brak danych", "nie odpowiada", "niedostepny"],
        ["powiadomienie", "powiadomienia", "push", "alert", "alarm"],
        ["subskrypcja", "plan", "abonament", "anulowac", "anuluj", "platnosc"],
        ["sonda", "czujnik", "sensor"],
        ["usun", "usunac", "usuwanie"],
        ["dozowanie", "dozownik", "pompa dozujaca"],
        ["fahrenheit", "celsjusz", "jednostki", "jednostka"],
        ["hey cora", "slowo aktywujace", "glos"],
        ["tablet", "cora max", "ekran scienny"],
        ["telefon", "smartfon", "cora mobile"],
        ["logowanie", "zaloguj", "haslo", "login"],
        ["pompa cyrkulacyjna", "cyrkulator", "wavemaker", "gyre"],
        ["gniazdo", "listwa", "listwa zasilajaca"],
        ["aktualizacja", "zaktualizuj", "firmware", "oprogramowanie"],
        ["swiatlo", "oswietlenie", "lampa", "led"],
        ["dolewka", "automatyczna dolewka", "ato"],
    ],
}

STOPWORDS = {
    "en": "a an the how do does i my me to can is are what why when where on in of for with it "
          "and or you your from this that be should no not".split(),
    "de": "der die das den dem ein eine einen wie ich mein meine mich kann ist sind was warum wo "
          "in im auf zu mit und oder für von du dein deine".split(),
    "fr": "le la les l un une des de du d comment je j mon ma mes est sont que quoi pourquoi ou "
          "dans sur pour avec et en au aux vous votre".split(),
    "tr": "bir ve ile icin bu su ne neden nasil nerede mi mu da de".split(),
    "it": "il lo la i gli le l un una come io mio mia miei e che perche dove in su per con di del "
          "della da al".split(),
    "es": "el la los las un una unos como yo mi mis es son que por porque donde en con y o de del "
          "para al".split(),
    "pl": "jak co czy w we na z ze i do moj moja moje to jest sa dlaczego gdzie sie".split(),
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
    twin: str = ""
    lang: str = "en"
    html: str = ""
    headings: list = field(default_factory=list)
    # Heading ids that only existed inside stripped `<!-- beta -->` blocks: a
    # link to one of them must fail the build (see `hidden_link_problems`).
    stripped_ids: set = field(default_factory=set)

    @property
    def url(self) -> str:
        prefix = "/help/" if self.lang == "en" else f"/{self.lang}/help/"
        return prefix if self.slug == "index" else f"{prefix}{self.slug}"

    @property
    def out_path(self) -> Path:
        base = OUT if self.lang == "en" else ROOT / self.lang / "help"
        return base / ("index.html" if self.slug == "index" else f"{self.slug}.html")


# ⭐ "Help" SECOND, right under the index (R1-07, 2026-10-13). It was last,
# below 51 product links, so Troubleshooting sat at the very bottom of the
# phone drawer although it is the page people most often come for.
SECTION_ORDER = ["", "Help", "Cora Mobile", "Cora Max"]

# The task groups, in the order they appear in BOTH products' sidebars. The
# self-test checks every section's groups are contiguous runs of `order:` in
# this order, so the sidebar and Previous/Next can never disagree again.
GROUP_ORDER = [
    "Getting started", "Your dashboard", "Equipment", "Alerts and automation",
    "Records", "Intelligence", "Settings and account",
]


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


# Letters NFKD does not decompose into a base letter plus a mark.
_FOLD_EXTRA = str.maketrans({
    "ł": "l", "Ł": "L", "ı": "i", "ø": "o", "Ø": "O", "đ": "d", "Đ": "D",
    "ß": "ss", "æ": "ae", "Æ": "AE", "œ": "oe", "Œ": "OE",
})


def ascii_fold(text: str) -> str:
    """'DŌS' -> 'DOS', 'Yaş' -> 'Yas', 'łączenie' -> 'laczenie'."""
    s = unicodedata.normalize("NFKD", text.translate(_FOLD_EXTRA))
    return "".join(c for c in s if not unicodedata.combining(c))


def slugify(text: str) -> str:
    # ⭐ ASCII-FOLDED FIRST (2026-10-13). It used to drop every non-ASCII
    # letter, so "DŌS" became `#ds`, Turkish "Yaş" `#ya` and Polish
    # "łączenie" `#czenie`. Folding keeps the word readable in the URL.
    s = ascii_fold(re.sub(r"<[^>]+>", "", text)).lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    return re.sub(r"\s+", "-", s.strip())[:60]


# `## Heading {#stable-id}`: the id is used verbatim and the braces are not
# rendered. Translators copy the `{#...}` unchanged, so an English
# `/help/<slug>#stable-id` link keeps landing on the right spot in every
# language (README §Links).
_CUSTOM_ID_RE = re.compile(r"^(.*?)\s*\{#([a-z0-9][a-z0-9-]*)\}\s*$")


def split_heading(raw: str) -> tuple[str, str]:
    """Heading source text -> (text without the {#id}, id)."""
    m = _CUSTOM_ID_RE.match(raw.strip())
    if m:
        return m.group(1).strip(), m.group(2)
    return raw.strip(), slugify(raw)


# ─────────────────────────────────────────────────────────────────────────────
# Beta content is HIDDEN from the public guide (owner, 2026-10-14: "ALL Beta
# functions must be hidden on the public Help").
#
# ⭐ Two mechanisms, both resolved BEFORE rendering, so nothing downstream
# (nav, search, sitemap, twin lines, hreflang, Previous/Next) ever sees it:
#  · frontmatter `beta: true`  -> the whole page is not built, in any language,
#    and any stale HTML for it is deleted from help/ and <lang>/help/;
#  · `<!-- beta -->` ... `<!-- /beta -->` -> that span of Markdown is removed.
#    A block whose markers sit at line starts/ends removes WHOLE LINES (so a
#    list or table stays contiguous); one inside a line removes just the span.
#    No nesting; an unbalanced marker aborts the build.
# ⛔ A link to a hidden page, or to an anchor that only existed inside a
# stripped block, aborts the build (`hidden_link_problems`): wrap the linking
# text in a beta block too.
# ⛔ Nothing published may name a Beta feature (`beta_leaks`, run by the build
# AND the self-test over every page and search index in every language).
# ─────────────────────────────────────────────────────────────────────────────

_BETA_MARK = re.compile(r"<!--\s*(/?)beta\s*-->", re.I)


def strip_beta(md: str, where: str = "?") -> tuple[str, str]:
    """Remove `<!-- beta -->` blocks. Returns (published markdown, removed text).

    ⛔ Raises SystemExit on an unbalanced or nested marker, naming the line.
    """
    out: list[str] = []
    removed: list[str] = []
    pos = 0
    open_at = None  # (match start, line number) of the pending opener
    for m in _BETA_MARK.finditer(md):
        line_no = md.count("\n", 0, m.start()) + 1
        closing = bool(m.group(1))
        if not closing:
            if open_at is not None:
                raise SystemExit(f"⛔ {where}:{line_no}: nested <!-- beta --> (the one on line "
                                 f"{open_at[1]} is not closed); beta blocks do not nest")
            open_at = (m.start(), line_no)
            continue
        if open_at is None:
            raise SystemExit(f"⛔ {where}:{line_no}: <!-- /beta --> without an opening <!-- beta -->")
        start, end = open_at[0], m.end()
        line_start = md.rfind("\n", 0, start) + 1
        nl = md.find("\n", end)
        line_end = len(md) if nl == -1 else nl
        if not md[line_start:start].strip() and not md[end:line_end].strip():
            # Whole lines: drop them, newline included, so the block leaves no
            # blank line behind to split a list or a table in two.
            start, end = line_start, (line_end + 1 if nl != -1 else line_end)
        out.append(md[pos:start])
        removed.append(md[start:end])
        pos = end
        open_at = None
    if open_at is not None:
        raise SystemExit(f"⛔ {where}:{open_at[1]}: <!-- beta --> is never closed with <!-- /beta -->")
    out.append(md[pos:])
    return "".join(out), "\n".join(removed)


# ⛔ THE LEAK RULE: no published byte may name a hidden feature or say "Beta".
# Word-boundary, case-insensitive, over the rendered HTML (tags included, so
# alt text, meta tags and URLs count) and over each language's search.json.
#
# ⭐ The list of hidden brands and feature names is NOT in this public repo:
# writing it here would publish exactly what it protects. The private prepare
# step passes it in through `HELP_LEAK_RULES`, a JSON file:
#     {"terms": "<regex>", "allow_word": "<regex>", "allow_ctx": "<regex>"}
# `terms` is what must never appear; a hit whose word matches `allow_word` is
# forgiven when it sits inside an `allow_ctx` phrase (for example a generic
# word that only some phrases make harmless). Without the file, the rule is
# just the word Beta in any language (beta, bêta, Beta-..., Betatester...).
@dataclass
class LeakRules:
    terms: re.Pattern
    allow_word: re.Pattern | None = None
    allow_ctx: re.Pattern | None = None


_DEFAULT_TERMS = r"\bb[eê]ta"


def load_leak_rules(path: str | None = None) -> LeakRules:
    path = path if path is not None else os.environ.get("HELP_LEAK_RULES", "")
    if not path:
        return LeakRules(re.compile(_DEFAULT_TERMS, re.I))
    try:
        cfg = json.loads(Path(path).read_text(encoding="utf-8"))
        terms = cfg["terms"]
    except (OSError, ValueError, KeyError) as e:
        # ⛔ A rules file that was asked for but cannot be read must not quietly
        # fall back to the weaker default.
        raise SystemExit(f"⛔ HELP_LEAK_RULES={path} is unreadable: {e}")
    comp = lambda k: re.compile(cfg[k], re.I) if cfg.get(k) else None
    return LeakRules(re.compile(f"(?:{terms})|{_DEFAULT_TERMS}", re.I),
                     comp("allow_word"), comp("allow_ctx"))


LEAK_RULES = load_leak_rules()


def beta_leaks(text: str, rules: LeakRules | None = None) -> list[str]:
    """Every leak-rule hit in `text`, each with a little context."""
    rules = rules or LEAK_RULES
    hits = []
    for m in rules.terms.finditer(text):
        lo = max(0, m.start() - 40)
        ctx = text[lo:m.end() + 40]
        if rules.allow_word and rules.allow_ctx and rules.allow_word.match(m.group(0)):
            if any(c.start() <= m.start() - lo < c.end() for c in rules.allow_ctx.finditer(ctx)):
                continue
        hits.append(f"{m.group(0)!r} in …{ctx.replace(chr(10), ' ')}…")
    return hits


_TILE_RE = re.compile(r"^\s*[-*]\s+\[([^\]]+)\]\(([^)\s]+)\)\s*[:.]?\s*(.*)$")


def render_tiles(lines: list[str]) -> str:
    """`:::tiles` block: each `- [Title](/help/slug): one line` becomes a tile."""
    items = []
    for line in lines:
        m = _TILE_RE.match(line)
        if not m:
            continue
        title, href, desc = m.group(1), m.group(2), m.group(3).strip()
        span = f"<span>{inline(desc)}</span>" if desc else ""
        items.append(
            f'<li><a href="{html.escape(href, quote=True)}"><b>{inline(title)}</b>{span}</a></li>'
        )
    return f'<ul class="tiles">{"".join(items)}</ul>'


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
        m = re.match(r"^:::(note|warning|tip|tiles)\s*(.*)$", line)
        if m:
            kind, title = m.group(1), m.group(2).strip()
            i += 1
            buf = []
            while i < len(lines) and not lines[i].startswith(":::"):
                buf.append(lines[i])
                i += 1
            i += 1
            if kind == "tiles":
                out.append(render_tiles(buf))
                continue
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
            raw, hid = split_heading(m.group(2))
            text = inline(raw)
            headings.append((level, raw, hid))
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


_H23_SPLIT = re.compile(r'<h([23]) id="([^"]*)">(.*?)</h\1>', re.S)


def _plain(fragment: str) -> str:
    t = html.unescape(re.sub(r"<[^>]+>", " ", fragment))
    # NFC so every accented letter is ONE code point: the client folds text
    # character by character and relies on that to keep snippet offsets true.
    return unicodedata.normalize("NFC", re.sub(r"\s+", " ", t).strip())


def search_chunks(page_html: str) -> list[list[str]]:
    """[[heading, id, text], ...]: the page cut at every H2 and H3.

    ⭐ A result can then link to the SECTION that matched (R1-03): a hit deep
    in Troubleshooting or the FAQ lands on its question, not on the top of a
    wall of 34 headings. The first chunk is the intro, with no heading.
    Heading text is not repeated inside the chunk text, which is what keeps
    the index the same size as the old whole-body one.
    """
    parts = _H23_SPLIT.split(page_html)
    chunks = []
    intro = _plain(parts[0])
    if intro:
        chunks.append(["", "", intro])
    for k in range(1, len(parts) - 1, 4):
        _level, hid, head, after = parts[k:k + 4]
        chunks.append([_plain(head), hid, _plain(after)])
    return chunks


def search_index(pages: list[Page]) -> str:
    """A tiny static index, fetched only when someone opens search.

    ⭐ 50 pages and ~28,000 words is past what a sidebar can expose. The index
    is deliberately NOT inlined into every page: it is one file, fetched once
    on first use, so the cost lands on the readers who search and nobody else.

    ⛔ THE WHOLE BODY, NOT A PREFIX. It was once capped at 1,800 chars, about
    half a page, and "amber" found nothing although the dashboard page has a
    section on it. A search that cannot see half of every page answers "not
    here" with confidence. Every chunk is complete.

    The language's synonym rows and stop words ride along, so the matching
    rules live in one place (this file) and each language searches with its
    own words.
    """
    docs = []
    lang = pages[0].lang if pages else "en"
    strings = UI_STRINGS[lang]
    for p in pages:
        section = p.section or "Help"
        docs.append(
            {
                "u": p.url,
                "t": p.title,
                "s": strings["sections"].get(section, section),
                "d": p.description,
                "x": search_chunks(p.html),
            }
        )
    payload = {
        "syn": SYN_COMMON + SYNONYMS.get(lang, []),
        "stop": STOPWORDS.get(lang, []),
        "docs": docs,
    }
    return json.dumps(payload, separators=(",", ":"), ensure_ascii=False)


# ─────────────────────────────────────────────────────────────────────────────
# The search engine, client side. ⭐ A plain string (not part of the shell's
# f-string) so the self-test can run THIS EXACT CODE under node against the
# real index. It only defines `CoraSearch`; the dialog code in `shell()` uses
# it.
#
# Rules (R1-01..04):
#  · every query word must match somewhere on the page (AND);
#  · a word matches at the START of a word, as a prefix ("notif" finds
#    "notifications", "ato" does not find "automation");
#  · case, accents, Turkish dotted/dotless i and hyphens are folded away on
#    both sides, and a word may be split or joined (wifi = Wi-Fi = wi fi);
#  · a query word or 2-3 word phrase in a synonym row matches any word of it;
#  · rank: title 60 > description 40 > heading 30 > body 10 per word, plus a
#    phrase bonus, ties broken by how many sections hit;
#  · a page whose title does not already answer the query links to its best
#    matching section, and can list a second strong section under it.
# ─────────────────────────────────────────────────────────────────────────────

SEARCH_CORE_JS = r"""
var CoraSearch = (function () {
  // One character in, ONE character out, always: snippets are cut from the
  // original text at offsets found in the folded text.
  var FOLD = {'ı': 'i', 'ł': 'l', 'ø': 'o', 'đ': 'd', 'ß': 's', 'æ': 'a', 'œ': 'o',
              '-': ' ', '‐': ' ', '‑': ' ', '–': ' ', '_': ' ', '/': ' '};
  var memo = {};
  function foldChar(c, lang) {
    var k = lang + c, v = memo[k];
    if (v !== undefined) return v;
    var lc = c.toLocaleLowerCase(lang);
    v = FOLD[lc] || FOLD[c];
    if (v === undefined) {
      var n = lc.normalize('NFD').replace(/[̀-ͯ]/g, '');
      v = n.length ? n.charAt(0) : c;
      if (FOLD[v]) v = FOLD[v];
    }
    memo[k] = v;
    return v;
  }
  function fold(s, lang) {
    var o = new Array(s.length);
    for (var i = 0; i < s.length; i++) o[i] = foldChar(s.charAt(i), lang);
    return o.join('');
  }
  function words(s) { return s.split(/[^a-z0-9]+/).filter(Boolean); }
  function esc(t) {
    return String(t).replace(/[&<>"]/g, function (c) {
      return {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'}[c];
    });
  }
  // Always at the START of a word. A phrase's spaces are optional ("top off"
  // finds "topoff"), and one word may be split once into two parts of at
  // least two letters, so wifi finds "Wi-Fi" (a folded hyphen is a space)
  // while "ato" still cannot reach into "a tour". A one- or two-letter word
  // must be the WHOLE word ("ph" is not "phone", "kh" is not "khaki").
  function rx(alt) {
    var w = alt.split(' '), body;
    if (w.length > 1) {
      body = w.join(' ?');
    } else {
      var v = [alt];
      for (var k = 2; k <= alt.length - 2; k++) v.push(alt.slice(0, k) + ' ' + alt.slice(k));
      body = v.join('|');
    }
    var end = alt.length <= 2 ? '(?![a-z0-9])' : '';
    return new RegExp('(?:^|[^a-z0-9])(' + body + ')' + end);
  }

  function prep(raw, lang) {
    var syn = {}, stop = {};
    (raw.stop || []).forEach(function (w) { stop[words(fold(w, lang)).join('')] = 1; });
    (raw.syn || []).forEach(function (row) {
      var alts = row.map(function (a) { return words(fold(a, lang)).join(' '); });
      alts.forEach(function (a) {
        var k = a.replace(/ /g, '');
        syn[k] = (syn[k] || []).concat(alts);
      });
    });
    var docs = (raw.docs || []).map(function (d) {
      return {
        u: d.u, t: d.t, s: d.s, d: d.d || '',
        tn: fold(d.t, lang), dn: fold(d.d || '', lang),
        x: d.x.map(function (c) {
          return {h: c[0], id: c[1], b: c[2], hn: fold(c[0], lang), bn: fold(c[2], lang)};
        })
      };
    });
    return {lang: lang, syn: syn, stop: stop, docs: docs};
  }

  function lookup(P, k, single) {
    if (P.syn[k]) return P.syn[k];
    if (!single) return null;
    var suf = ['s', 'es', 'ing', 'ed', 'er'];
    for (var i = 0; i < suf.length; i++) {
      var L = suf[i].length;
      if (k.length > L + 2 && k.slice(-L) === suf[i] && P.syn[k.slice(0, -L)]) return P.syn[k.slice(0, -L)];
    }
    return null;
  }

  // The query as a list of CONCEPTS; each concept is a list of regexes, and
  // a concept matches when any one of them does.
  function concepts(q, P) {
    var t = words(fold(q, P.lang)), out = [], i = 0;
    while (i < t.length) {
      var hit = null, n;
      for (n = Math.min(3, t.length - i); n >= 1 && !hit; n--) {
        var g = lookup(P, t.slice(i, i + n).join(''), n === 1);
        if (g) hit = [t.slice(i, i + n).join(' ')].concat(g);
      }
      if (hit) { out.push(hit); i += n + 1; continue; }
      if (!P.stop[t[i]]) out.push([t[i]]);
      i++;
    }
    if (!out.length) out = t.map(function (w) { return [w]; });
    return out.map(function (alts) {
      var seen = {}, r = [];
      alts.forEach(function (a) {
        var k = a.replace(/ /g, '');
        if (k && !seen[k]) { seen[k] = 1; r.push(rx(a)); }
      });
      return r;
    });
  }

  function first(rs, s) {
    for (var i = 0; i < rs.length; i++) { var m = rs[i].exec(s); if (m) return m; }
    return null;
  }

  function snip(x, C) {
    for (var c = 0; c < C.length; c++) {
      var m = first(C[c], x.bn);
      if (!m) continue;
      var L = m[1].length, i = m.index + m[0].length - L;
      var a = Math.max(0, i - 45), b = Math.min(x.b.length, i + L + 75);
      return (a ? '…' : '') + esc(x.b.slice(a, i)) + '<mark>' + esc(x.b.slice(i, i + L))
        + '</mark>' + esc(x.b.slice(i + L, b)) + (b < x.b.length ? '…' : '');
    }
    return '';
  }

  function search(P, q, limit) {
    var C = concepts(q, P);
    if (!C.length) return [];
    var qw = words(fold(q, P.lang));
    // What the reader literally typed beats a synonym of it.
    var lit = qw.length ? rx(qw.join(' ')) : null;
    var phrase = qw.length > 1 ? lit : null;
    var found = [];
    P.docs.forEach(function (d) {
      var score = 0, hits = 0, titleAll = true;
      var cs = d.x.map(function () { return {s: 0, n: 0, hh: 0}; });
      for (var c = 0; c < C.length; c++) {
        var rs = C[c], inT = !!first(rs, d.tn), inD = !!first(rs, d.dn), inH = false, inB = false;
        for (var j = 0; j < d.x.length; j++) {
          var h = !!first(rs, d.x[j].hn), b = !!first(rs, d.x[j].bn);
          if (h) { inH = true; cs[j].s += 30; cs[j].hh++; hits++; }
          if (b) { inB = true; cs[j].s += 10; hits++; }
          if (h || b) cs[j].n++;
        }
        if (!inT) titleAll = false;
        if (!(inT || inD || inH || inB)) return;          // AND: every concept
        score += inT ? 60 : inD ? 40 : inH ? 30 : 10;
      }
      if (words(d.tn).join(' ') === qw.join(' ')) score += 40;
      if (phrase) {
        if (phrase.test(d.tn)) score += 50;
        else if (d.x.some(function (x) { return phrase.test(x.hn); })) score += 25;
      }
      var order = [];
      for (var k = 0; k < cs.length; k++) {
        if (!cs[k].s || !d.x[k].id) continue;
        if (lit && lit.test(d.x[k].hn)) cs[k].s += 20;
        else if (lit && lit.test(d.x[k].bn)) cs[k].s += 5;
        order.push(k);
      }
      order.sort(function (a, b) {
        return (cs[b].n - cs[a].n) || (cs[b].hh - cs[a].hh) || (cs[b].s - cs[a].s) || (a - b);
      });
      var secs = [];
      if (!titleAll && order.length) {
        var top = order[0];
        if (cs[top].n === C.length || cs[top].hh) secs.push(top);
        var nx = order[1];
        if (secs.length && nx !== undefined && cs[nx].n === C.length && cs[nx].hh) secs.push(nx);
      }
      found.push({d: d, score: score, hits: hits, secs: secs});
    });
    found.sort(function (a, b) { return (b.score - a.score) || (b.hits - a.hits); });

    var out = [];
    for (var f = 0; f < found.length && out.length < (limit || 12); f++) {
      var r = found[f], d = r.d;
      if (r.secs.length) {
        r.secs.forEach(function (j, n) {
          var x = d.x[j];
          out.push({u: d.u + '#' + x.id, t: n ? x.h : d.t + ' › ' + x.h, s: d.s,
                    sn: snip(x, C) || esc(d.d), sub: n > 0, score: r.score});
        });
      } else {
        var sn = '';
        for (var j = 0; j < d.x.length && !sn; j++) sn = snip(d.x[j], C);
        out.push({u: d.u, t: d.t, s: d.s, sn: sn || esc(d.d), sub: false, score: r.score});
      }
    }
    return out.slice(0, limit || 12);
  }

  return {fold: fold, prep: prep, concepts: concepts, search: search, esc: esc};
})();
if (typeof module !== 'undefined') module.exports = CoraSearch;
"""


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
    out = [f'<nav class="pn" aria-label="{html.escape(strings["continue_reading"], quote=True)}">']
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
    """On-page contents, h2 only. Skipped when a page has fewer than three.

    The glossary gets an A to Z jump row instead: its 30-odd terms as a
    two-column contents list were a wall (R1-25)."""
    h2 = [h for h in page.headings if h[0] == 2]
    if page.slug == "glossary" and h2:
        label = html.escape(UI_STRINGS[page.lang]["az_label"])
        letters: dict[str, str] = {}
        for _, t, hid in h2:
            ch = ascii_fold(re.sub(r"[*`_]", "", t).strip()[:1]).upper()
            if ch and ch not in letters:
                letters[ch] = hid
        items = "".join(f'<li><a href="#{hid}">{html.escape(ch)}</a></li>' for ch, hid in letters.items())
        return f'<nav class="toc az" aria-label="{label}"><p>{label}</p><ul>{items}</ul></nav>'
    if len(h2) < 3:
        return ""
    label = html.escape(UI_STRINGS[page.lang]["on_this_page"])
    items = "".join(f'<li><a href="#{hid}">{html.escape(t)}</a></li>' for _, t, hid in h2)
    return f'<nav class="toc" aria-label="{label}"><p>{label}</p><ul>{items}</ul></nav>'


def twin_html(page: Page, pages: list[Page]) -> str:
    """'On Cora Max: <twin>' under the H1 (R1-18). Same language only: a twin
    not translated yet is simply left out (the self-test flags it)."""
    if not page.twin:
        return ""
    t = next((p for p in pages if p.slug == page.twin), None)
    if t is None:
        return ""
    key = "twin_max" if t.section == "Cora Max" else "twin_mobile"
    pre, _, post = UI_STRINGS[page.lang][key].partition("{title}")
    esc = lambda x: html.escape(x, quote=False)
    return f'<p class="twin">{esc(pre)}<a href="{t.url}">{esc(t.title)}</a>{esc(post)}</p>'


def crumb_items(page: Page, pages: list[Page]) -> list[tuple[str, str]]:
    """[(label, url)] for Help / section / group (R1-22). Empty on the index.

    The section and group link to their first page, which is where the
    sidebar would take you. The Help section is not repeated after "Help".
    """
    if page.slug == "index":
        return []
    strings = UI_STRINGS[page.lang]
    home = "/help/" if page.lang == "en" else f"/{page.lang}/help/"
    items = [(strings["sections"]["Help"], home)]
    in_sec = sorted([p for p in pages if p.section == page.section], key=lambda p: p.order)
    if page.section and page.section != "Help" and in_sec:
        items.append((strings["sections"].get(page.section, page.section), in_sec[0].url))
    if page.group:
        in_grp = [p for p in in_sec if p.group == page.group]
        if in_grp:
            items.append((strings["groups"].get(page.group, page.group), in_grp[0].url))
    return items


EN_ATTR = ' lang="en"'


def crumbs_html(page: Page, pages: list[Page]) -> str:
    items = crumb_items(page, pages)
    if not items:
        return ""
    label = html.escape(UI_STRINGS[page.lang]["breadcrumb"], quote=True)
    # A product name keeps English casing rules (same reason as the sidebar).
    lis = "".join(
        f'<li><a href="{u}"{EN_ATTR if t.startswith("Cora") else ""}>{html.escape(t)}</a></li>'
        for t, u in items
    )
    return f'<nav class="crumbs" aria-label="{label}"><ol>{lis}</ol></nav>'


def crumbs_jsonld(page: Page, pages: list[Page]) -> str:
    """BreadcrumbList for search engines: the visible trail plus this page."""
    items = crumb_items(page, pages)
    if not items:
        return ""
    els = [
        {"@type": "ListItem", "position": i + 1, "name": t, "item": f"{SITE}{u}"}
        for i, (t, u) in enumerate(items)
    ]
    els.append({"@type": "ListItem", "position": len(els) + 1, "name": page.title})
    data = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": els}
    js = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return f'\n  <script type="application/ld+json">{js}</script>'


def localize_chrome(body: str, lang: str) -> str:
    """Translate the few English words `render()` writes into the body
    (it is language-blind): the enlarge label and the placeholder caption."""
    if lang == "en":
        return body
    st = UI_STRINGS[lang]
    pre = st["enlarge"].partition("{alt}")[0]
    body = body.replace('aria-label="Enlarge: ', f'aria-label="{html.escape(pre, quote=True)}')
    return body.replace("<span>Screenshot to come</span>",
                        f"<span>{html.escape(st['shot_to_come'])}</span>")


SEARCH_VERSION: dict[str, str] = {}


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
    # ⭐ Zero results is never a dead end (R1-04): fewer words, or one of
    # these. Pages not written yet in this language are left out.
    _by = {p.slug: p for p in pages}
    _rescue = [(_by[s].url, _by[s].title) for s in ("troubleshooting", "how-do-i") if s in _by]
    _rescue.append((f"mailto:{SUPPORT_EMAIL}", strings["contact_support"]))
    search_rescue = (
        f'<p>{html.escape(strings["search_try"])}</p><ul>'
        + "".join(f'<li><a href="{u}">{html.escape(t)}</a></li>' for u, t in _rescue)
        + "</ul>"
    )
    search_v = SEARCH_VERSION.get(lang, "0")
    help_word = html.escape(strings["sections"]["Help"])

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
  <link rel="stylesheet" href="/help/help.css?v={CSS_VERSION}">{crumbs_jsonld(page, pages)}
</head>
<body>
<a class="skip" href="#main">{skip}</a>

<header class="hnav">
  <div class="hnav-in">
    <a class="hbrand" href="{home_url}">
      <img src="/cora_logo-240.webp" alt="Cora" width="400" height="163">
      <span>{help_word}</span>
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
  <aside class="hside" id="hside" aria-label="{html.escape(strings["guide_nav"], quote=True)}">
    <button class="hclose" id="hclose" type="button" aria-label="{close_label}">&times;</button>
    <nav aria-label="{html.escape(strings["guide"], quote=True)}">
{nav_html(pages, page)}
    </nav>
  </aside>

  <main class="hmain" id="main">
    <article class="doc">
      {crumbs_html(page, pages)}
      <h1>{title}</h1>
      {twin_html(page, pages)}
      {toc_html(page)}
{localize_chrome(mark_trademarks(page.html), lang)}
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
    box.setAttribute('aria-label', img.alt || {json.dumps(strings["screenshot"])});
    var x = document.createElement('button');
    x.type = 'button'; x.className = 'lb-x';
    x.setAttribute('aria-label', {json.dumps(strings["close"])}); x.innerHTML = '&times;';
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
// The matching rules are SEARCH_CORE_JS in build_help.py (tested under node
// by the self-test); this is only the dialog around it.
{SEARCH_CORE_JS}
(function () {{
  var btn = document.getElementById('hfind');
  if (!btn) return;
  var P = null, dlg = null, input = null, list = null, opener = null;
  var esc = CoraSearch.esc;

  function run() {{
    var q = input.value.trim();
    if (!q || !P) {{ list.innerHTML = ''; return; }}
    var hits = CoraSearch.search(P, q, 12);
    if (!hits.length) {{
      list.innerHTML = '<li class="snone"><p>' + {json.dumps(html.escape(search_none_pre))} + esc(q)
        + {json.dumps(html.escape(search_none_post))} + '</p>' + {json.dumps(search_rescue)} + '</li>';
      return;
    }}
    list.innerHTML = hits.map(function (r, i) {{
      return '<li' + (r.sub ? ' class="ssub"' : '') + '><a href="' + esc(r.u) + '"'
        + (i ? '' : ' class="on"') + '><b>' + esc(r.t) + '</b><em>'
        + (r.sub ? '' : esc(r.s) + ' · ') + r.sn + '</em></a></li>';
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
    if (P) {{ run(); return; }}
    // ⭐ Versioned by content hash: GitHub Pages caches each file for its
    // own 600 s, and a new page reading an old-format index would fail.
    fetch('{home_url}search.json?v={search_v}').then(function (r) {{ return r.json(); }})
      .then(function (j) {{ P = CoraSearch.prep(j, {json.dumps(lang)}); run(); }})
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
.snone { padding: 18px 22px; color: var(--text-3); font-size: 14px; }
.snone p { margin: 0 0 8px; }
.snone ul { margin: 0; padding-left: 18px; }
.snone a { display: inline; padding: 0; color: var(--brand-deep); text-decoration: underline; }
.sres .ssub a { padding-left: 28px; }
.sres .ssub b { font-size: 13.5px; font-weight: 600; }

/* ── Breadcrumb and twin line ───────────────────────────────────────── */
.crumbs ol { list-style: none; margin: 0 0 10px; padding: 0; display: flex; flex-wrap: wrap; gap: 2px 0; font-size: 13.5px; }
.crumbs li { margin: 0; color: var(--text-3); }
.crumbs li + li::before { content: "/"; margin: 0 8px; color: var(--text-3); }
.crumbs a { color: var(--text-2); text-decoration: none; }
.crumbs a:hover { color: var(--brand-deep); text-decoration: underline; }
.twin { margin: -8px 0 22px !important; font-size: 14.5px; color: var(--text-2); }

/* ── Glossary A to Z ─────────────────────────────────────────────────── */
.toc.az ul { columns: auto; display: flex; flex-wrap: wrap; gap: 4px; }
.toc.az li { margin: 0; }
.toc.az a {
  display: inline-block; min-width: 32px; padding: 4px 0; text-align: center;
  font-weight: 600; border: 1px solid var(--line); border-radius: 4px; background: var(--surface);
}
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


# lang -> slugs whose frontmatter says `beta: true` (filled by `load_pages`).
HIDDEN: dict[str, set[str]] = {}
LINK_PROBLEMS: list[str] = []


def hidden_link_problems(lang_pages_map: dict[str, list[Page]],
                         hidden: dict[str, set[str]]) -> list[str]:
    """Links (and twins) that would point at hidden Beta content.

    ⛔ Run on the RENDERED but NOT YET LOCALIZED html, where every internal
    link is still English-style: after `localize_links` a link to a missing
    slug quietly becomes the language index and an unknown anchor is dropped,
    which would hide exactly the mistake this is here to catch.
    """
    en_hidden = hidden.get("en", set())
    bad = []
    for lang, pages in lang_pages_map.items():
        hid = en_hidden | hidden.get(lang, set())
        by = {p.slug: p for p in pages}
        en_live = {q.slug for q in lang_pages_map.get("en", [])}
        for h in hidden.get(lang, set()) - en_hidden:
            if h in en_live:
                bad.append(f"{lang}/{h} is beta: true but the English page is published")
        for p in pages:
            if p.slug in en_hidden and lang != "en":
                bad.append(f"{lang}/{p.slug} is published but the English page is beta: true; "
                           "mark the translation beta: true too")
            if p.twin and p.twin in hid:
                bad.append(f"{lang}/{p.slug}: twin: {p.twin} is a hidden Beta page")
            for m in _ANY_HELP_HREF.finditer(p.html):
                path, slug, frag = m.group(1), m.group(2), m.group(3)
                if not path and not frag:
                    continue
                target = p.slug if not path else (slug or "index")
                if path and target in hid:
                    bad.append(f"{lang}/{p.slug} links to hidden Beta page /help/{target}")
                    continue
                t = by.get(target)
                if t is None or not frag or frag == "#":
                    continue
                aid = frag[1:]
                live = {x for _, _, x in t.headings}
                if aid in t.stripped_ids and aid not in live:
                    bad.append(f"{lang}/{p.slug} links to #{aid} on {target}, which only "
                               "exists inside a stripped beta block")
    return sorted(set(bad))


def load_pages(lang: str = "en", root: Path | None = None) -> list[Page]:
    """Load one language's tree.

    ⭐ `en` reads help-src/*.md, exactly as before. Any other language reads
    help-src/<lang>/*.md — a MIRROR, not a copy: whatever slugs exist there
    are the pages that language has been translated for. An entirely absent
    directory, or one with no .md files yet, is not an error — it means that
    language's translator has not started, and the site simply does not
    publish that language's help section yet (see help-src/README.md).
    """
    base = root or SRC
    src_dir = base if lang == "en" else base / lang
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
        beta = meta.get("beta", "").lower()
        if beta not in ("", "true", "false"):
            raise SystemExit(f"⛔ {lang}/{path.name}: beta: must be true or false, not {beta!r}")
        if beta == "true":
            # ⛔ A Beta page is NOT BUILT: no HTML, no nav entry, no search
            # entry, no sitemap entry, no twin line, no language-menu target.
            HIDDEN.setdefault(lang, set()).add(path.stem)
            continue
        body, removed = strip_beta(body, f"{'' if lang == 'en' else lang + '/'}{path.name}")
        stripped_ids = {
            split_heading(m.group(1))[1]
            for m in re.finditer(r"^#{2,4}\s+(.*)$", removed, re.M)
        }
        pages.append(
            Page(
                slug=path.stem,
                title=meta["title"],
                description=meta["description"],
                section=meta["section"] if meta["section"] != "-" else "",
                order=int(meta["order"]),
                group=meta.get("group", ""),
                reviewed=meta.get("reviewed", ""),
                twin=meta.get("twin", ""),
                lang=lang,
                body_md=body,
                stripped_ids=stripped_ids,
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
    # ⛔ A hidden Beta page leaves the (otherwise hand-kept) English entries too.
    for slug in sorted(HIDDEN.get("en", set())):
        text = re.sub(
            r"  <url>\s*<loc>" + re.escape(f"{SITE}/help/{slug}") + r"</loc>.*?</url>\n",
            "", text, flags=re.S)

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


def load_all(check_links: bool = True) -> dict[str, list[Page]]:
    """Every language's pages, rendered and with links localized."""
    HIDDEN.clear()
    lang_pages_map: dict[str, list[Page]] = {"en": load_pages("en")}
    for lang in LANGS:
        lang_pages_map[lang] = load_pages(lang)

    # Render every language's pages first: rendering only needs the page's
    # OWN body, but `localize_links` (next) needs every OTHER page's
    # headings already collected, so the two cannot be one pass.
    for pages in lang_pages_map.values():
        for p in pages:
            p.headings = []
            p.html = render(p.body_md, p.headings)

    problems = hidden_link_problems(lang_pages_map, HIDDEN)
    LINK_PROBLEMS[:] = problems
    if problems and check_links:
        raise SystemExit(
            "⛔ links to hidden Beta content (wrap the linking text in "
            "<!-- beta --> ... <!-- /beta --> too):\n   · " + "\n   · ".join(problems))

    # Rewrite English-style /help/... links in translated pages to
    # /<lang>/help/..., dropping an anchor that does not exist in the
    # translated target and falling back to that language's index when the
    # target page has not been translated at all (see `localize_links`).
    for lang in LANGS:
        pages = lang_pages_map[lang]
        by_slug = {p.slug: p for p in pages}
        for p in pages:
            p.html = localize_links(p.html, lang, by_slug)
    return lang_pages_map


def build(check_only: bool = False) -> int:
    lang_pages_map = load_all()
    en_pages = lang_pages_map["en"]
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
    # ⭐ Index first: every page's search script fetches it by content hash.
    indexes = {lang: search_index(pages) for lang, pages in lang_pages_map.items() if pages}
    for lang, text in indexes.items():
        SEARCH_VERSION[lang] = hashlib.sha256(text.encode("utf-8")).hexdigest()[:10]

    targets = [(OUT / "help.css", css), (OUT / "search.json", indexes["en"])]
    targets += [(p.out_path, shell(p, en_pages, slug_index)) for p in en_pages]

    total_pages = len(en_pages)
    for lang in LANGS:
        pages = lang_pages_map[lang]
        if not pages:
            continue
        total_pages += len(pages)
        out_dir = ROOT / lang / "help"
        out_dir.mkdir(parents=True, exist_ok=True)
        targets.append((out_dir / "search.json", indexes[lang]))
        targets += [(p.out_path, shell(p, pages, slug_index)) for p in pages]

    sitemap_text = desired_sitemap_text(lang_pages_map)
    if sitemap_text is not None:
        targets.append((ROOT / "sitemap.xml", sitemap_text))

    # ⛔ Refuse to write anything that names a Beta feature (see `beta_leaks`).
    leaks = [f"{path.relative_to(ROOT)}: {hit}" for path, content in targets
             if path.suffix in (".html", ".json") for hit in beta_leaks(content)]
    if leaks:
        print(f"⛔ {len(leaks)} Beta mention(s) would be published:")
        for x in leaks[:60]:
            print(f"   · {x}")
        return 1

    # ⛔ Hidden Beta pages: delete any HTML an earlier build left behind, so a
    # later publish cannot ship it.
    gone = []
    en_hidden = HIDDEN.get("en", set())
    for lang in ALL_LANGS:
        base = OUT if lang == "en" else ROOT / lang / "help"
        for slug in sorted(en_hidden | HIDDEN.get(lang, set())):
            f = base / ("index.html" if slug == "index" else f"{slug}.html")
            if f.exists():
                gone.append(f)

    if check_only:
        stale += [str(f.relative_to(ROOT)) + " (hidden Beta page, delete)" for f in gone]
    else:
        for f in gone:
            f.unlink()

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

    print(f"✅ {total_pages} pages · {written} file(s) written · css v{CSS_VERSION}"
          f" · {len(gone)} hidden Beta page file(s) removed")
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

def structure_problems(lang_pages_map: dict[str, list[Page]]) -> dict[str, list[str]]:
    """Sidebar-shape problems in every tree, by kind (R1-05/06/18)."""
    out: dict[str, list[str]] = {"order": [], "groups": [], "twin": [], "labels": []}
    for lang, pages in lang_pages_map.items():
        slugs = {p.slug for p in pages}
        for sec in SECTION_ORDER:
            in_sec = sorted([p for p in pages if p.section == sec], key=lambda p: p.order)
            seen_o: dict[int, str] = {}
            for p in in_sec:
                if p.order in seen_o:
                    out["order"].append(f"{lang}/{p.slug} = {lang}/{seen_o[p.order]} (order {p.order})")
                seen_o[p.order] = p.slug
            # Runs of the same group, in order. A group seen in two runs is
            # split, and the runs must follow GROUP_ORDER.
            runs: list[str] = []
            for p in in_sec:
                if p.group and (not runs or runs[-1] != p.group):
                    runs.append(p.group)
            for g in runs:
                if runs.count(g) > 1:
                    out["groups"].append(f"{lang} {sec}: '{g}' is split by order {runs}")
                    break
            known = [g for g in runs if g in GROUP_ORDER]
            unknown = [g for g in runs if g not in GROUP_ORDER]
            if unknown:
                out["groups"].append(f"{lang} {sec}: group(s) {unknown} not in GROUP_ORDER")
            if known != sorted(known, key=GROUP_ORDER.index):
                out["groups"].append(f"{lang} {sec}: groups out of order {runs}")
        for p in pages:
            if p.twin and p.twin not in slugs:
                out["twin"].append(f"{lang}/{p.slug} -> twin '{p.twin}' does not exist in that tree")
            if p.twin == p.slug:
                out["twin"].append(f"{lang}/{p.slug} is its own twin")
        for p in pages:
            if p.group and p.group not in UI_STRINGS[lang]["groups"]:
                out["labels"].append(f"{lang}: group '{p.group}' has no UI_STRINGS label")
            if p.section and p.section != "Help" and not p.section.startswith("Cora") \
                    and p.section not in UI_STRINGS[lang]["sections"]:
                out["labels"].append(f"{lang}: section '{p.section}' has no UI_STRINGS label")
    return out


_ANY_HELP_HREF = re.compile(r'href="(/help/([a-z0-9-]*))?(#[^"]*)?"')


def broken_links(en_pages: list[Page]) -> list[str]:
    """English internal links whose page or #anchor does not exist (R1-28).

    ⛔ English only and STRICT: translations copy these links, so an English
    anchor that misses is a broken link in seven languages. (A translation
    whose heading lost the anchor still degrades gracefully: `localize_links`
    drops it.) Same-page `#anchor` links are checked too.
    """
    by = {p.slug: p for p in en_pages}
    ids = {p.slug: {hid for _, _, hid in p.headings} for p in en_pages}
    bad = []
    for p in en_pages:
        for m in _ANY_HELP_HREF.finditer(p.html):
            path, slug, frag = m.group(1), m.group(2), m.group(3)
            if not path and not frag:
                continue
            target = p.slug if not path else (slug or "index")
            if path and target not in by:
                bad.append(f"{p.slug} -> /help/{slug} (no such page)")
                continue
            if frag and frag != "#" and frag[1:] not in ids[target]:
                bad.append(f"{p.slug} -> {'/help/' + slug if path else ''}{frag} (no such heading on {target})")
    return sorted(set(bad))


SEARCH_NODE_TEST = r"""
const S = require(process.argv[2]);
const fs = require('fs');
const cases = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
const out = [];
for (const c of cases) {
  const P = S.prep(c.index, c.lang);
  if (c.fold !== undefined) { out.push(S.fold(c.fold, c.lang)); continue; }
  out.push(S.search(P, c.q, 12).map(r => r.u));
}
process.stdout.write(JSON.stringify(out));
"""


def run_search_js(cases: list[dict]) -> list | None:
    """Run SEARCH_CORE_JS under node over `cases`; None when node is absent."""
    import shutil as _sh, subprocess as _sp, tempfile as _tf
    if not _sh.which("node"):
        return None
    with _tf.TemporaryDirectory() as d:
        core, runner, data = Path(d, "core.js"), Path(d, "run.js"), Path(d, "cases.json")
        core.write_text(SEARCH_CORE_JS, encoding="utf-8")
        runner.write_text(SEARCH_NODE_TEST, encoding="utf-8")
        data.write_text(json.dumps(cases, ensure_ascii=False), encoding="utf-8")
        r = _sp.run(["node", str(runner), str(core), str(data)], capture_output=True, text=True)
        if r.returncode:
            raise SystemExit(f"⛔ search JS failed under node: {r.stderr[:400]}")
        return json.loads(r.stdout)


def all_leaks(lang_pages_map: dict[str, list[Page]]) -> list[str]:
    """`beta_leaks` over every page shell and search index, all languages."""
    slug_index = build_slug_index(lang_pages_map)
    out = []
    for lang, pages in lang_pages_map.items():
        if not pages:
            continue
        for hit in beta_leaks(search_index(pages)):
            out.append(f"{lang}/search.json: {hit}")
        for p in pages:
            for hit in beta_leaks(shell(p, pages, slug_index)):
                out.append(f"{lang}/{p.slug}: {hit}")
    return out


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

    tm = mark_trademarks('<p>Neptune Systems and Red Sea. Red Sea again, <a href="/x?jebao">Jebao</a>.</p>'
                         '<code>Jecod</code> then Jecod.')
    ok("™ on the first brand mention", "Neptune Systems™ and Red Sea™." in tm)
    ok("™ only once per brand per page", "Red Sea again" in tm and tm.count("Red Sea™") == 1)
    ok("™ never inside a tag attribute", 'href="/x?jebao"' in tm and ">Jebao™<" in tm)
    ok("™ never inside code", "<code>Jecod</code> then Jecod™." in tm)
    ok("™ not doubled", mark_trademarks("Jebao™ pump") == "Jebao™ pump")

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
        # Budget raised 250 -> 320 KB on 2026-10-12: three Beta pages and the
        # Sept/Oct updates took the English index from 225 to 260 KB.
        # Raised 320 -> 480 KB on 2026-10-13: the full review rewrite added three
        # pages, H2/H3 section entries (search links to the section) and much
        # fuller pages, taking the English index to ~375 KB. It is fetched only
        # when someone searches, and served compressed (~4x smaller).
        ok(f"search index under 480 KB ({_idx.stat().st_size // 1024} KB)",
           _idx.stat().st_size < 491_520)

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

    # Owner, 2026-10-14: ALL Beta functions are HIDDEN on the public guide (this
    # replaced the 2026-10-12 rule that every page naming a Beta brand must say
    # "Beta"). The mechanism, unit by unit; the real content is checked below.
    _sb = lambda md: strip_beta(md, "test")[0]
    ok("beta block: a whole paragraph goes, its neighbours stay",
       _sb("A\n\n<!-- beta -->\nB secret\n<!-- /beta -->\n\nC\n") == "A\n\n\nC\n")
    ok("beta block: a list keeps one <ul> after an item is stripped",
       render(_sb("- a\n<!-- beta -->\n- b\n<!-- /beta -->\n- c"), [])
       == "<ul><li>a</li><li>c</li></ul>")
    ok("beta block: a table keeps one body after a row is stripped",
       render(_sb("| A | B |\n|---|---|\n| 1 | 2 |\n<!-- beta -->\n| x | y |\n<!-- /beta -->\n| 3 | 4 |"), []
              ).count("<tr>") == 3)
    ok("beta block: inline span inside a sentence",
       _sb("Apex<!-- beta -->, Acme<!-- /beta --> and Red Sea.") == "Apex and Red Sea.")
    ok("beta block: a whole section with its heading",
       "Secret" not in render(_sb("## Open\n\nx\n\n<!-- beta -->\n## Secret {#s}\n\ny\n<!-- /beta -->\n"), []))
    for _bad, _why in (("<!-- beta -->\nx\n", "never closed"), ("x\n<!-- /beta -->\n", "without an opening"),
                       ("<!-- beta -->a<!-- beta -->b<!-- /beta --><!-- /beta -->", "nested")):
        try:
            strip_beta(_bad, "test")
            _raised = ""
        except SystemExit as e:
            _raised = str(e)
        ok(f"⛔ unbalanced beta marker fails the build ({_why})", _why in _raised)

    import tempfile as _tf2
    with _tf2.TemporaryDirectory() as _d:
        _fm = "---\ntitle: {t}\ndescription: d\nsection: Help\norder: {o}\n{x}---\n{b}"
        Path(_d, "open.md").write_text(_fm.format(t="Open", o=1, x="", b="## Kept {#kept}\n\n"
                                                  "<!-- beta -->\n## Gone {#gone}\n<!-- /beta -->\n"))
        Path(_d, "secret.md").write_text(_fm.format(t="Secret", o=2, x="beta: true\n", b="x\n"))
        HIDDEN.clear()
        _lp = load_pages("en", Path(_d))
    ok("beta: true page is not loaded (so not built, listed, indexed or mapped)",
       [x.slug for x in _lp] == ["open"] and HIDDEN.get("en") == {"secret"})
    ok("a heading inside a stripped block is remembered as stripped",
       _lp[0].stripped_ids == {"gone"} and "Gone" not in _lp[0].body_md)
    _lp[0].headings = []
    _lp[0].html = render(_lp[0].body_md, _lp[0].headings)
    _lk = Page(slug="linker", title="L", description="d", section="Help", order=3, body_md="")
    _lk.html = ('<a href="/help/secret">x</a><a href="/help/open#gone">y</a>'
                '<a href="/help/open#kept">ok</a>')
    _de_lk = Page(slug="linker", title="L", description="d", section="Help", order=3, body_md="", lang="de")
    _de_lk.html = '<a href="/help/secret">x</a>'
    _hp = hidden_link_problems({"en": [_lp[0], _lk], "de": [_de_lk]}, {"en": {"secret"}})
    ok(f"⛔ a link to a hidden page fails, in English and in a translation ({_hp})",
       sum("hidden Beta page /help/secret" in x for x in _hp) == 2)
    ok("⛔ a link to an anchor that only existed in a stripped block fails",
       any("#gone" in x for x in _hp) and not any("#kept" in x for x in _hp))
    _tw = Page(slug="t", title="T", description="d", section="Help", order=4, body_md="", twin="secret")
    ok("⛔ a twin: pointing at a hidden page fails",
       any("twin: secret" in x for x in hidden_link_problems({"en": [_tw]}, {"en": {"secret"}})))
    HIDDEN.clear()

    # The mechanism with a stand-in rule (the real list is private, see LeakRules).
    _tr = LeakRules(re.compile(r"\bacme\b|\bwidget\w*|" + _DEFAULT_TERMS, re.I),
                    re.compile(r"widget", re.I), re.compile(r"widget icon", re.I))
    ok("leak rule: a listed term, the word Beta in any language and an unlisted use are caught",
       all(beta_leaks(w, _tr) for w in ("Acme pumps", "a Beta user", "bêta", "Betatester", "widgets")))
    ok("leak rule: an allowed phrase, and words that merely contain the letters, pass",
       not any(beta_leaks(w, _tr) for w in ("tap the widget icon", "alphabet", "acmes", "between")))
    ok("leak rule: without a rules file only the word Beta is checked",
       beta_leaks("Beta", load_leak_rules("")) and not beta_leaks("Acme", load_leak_rules("")))
    with _tf.NamedTemporaryFile("w", suffix=".json", delete=False) as _fh:
        _fh.write(json.dumps({"terms": r"\bacme\b"}))
    ok("leak rule: a rules file adds its terms and keeps the word Beta",
       all(beta_leaks(w, load_leak_rules(_fh.name)) for w in ("Acme", "beta")))
    Path(_fh.name).unlink()
    try:
        load_leak_rules("/nonexistent/rules.json")
        _raised = False
    except SystemExit:
        _raised = True
    ok("⛔ an unreadable rules file fails instead of falling back", _raised)

    # ⛔ THE REAL CONTENT: nothing published, in any language, names a Beta
    # feature. Every page shell (title, meta, nav, body, alt text, URLs) and
    # every search.json, exactly as `build()` would write them.
    try:
        _leak_map = load_all()
    except SystemExit as e:
        _leak_map = None
        ok(f"⛔ every tree loads for the leak check ({e})", False)
    if _leak_map is not None:
        _leaks = all_leaks(_leak_map)
        ok(f"⛔ no published page or search index names a Beta feature or says Beta "
           f"({len(_leaks)}: {_leaks[:8]})", not _leaks)
        _hid_urls = [f"{SITE}/help/{h}" for h in HIDDEN.get("en", set())]
        _sm_now = (ROOT / "sitemap.xml").read_text(encoding="utf-8") if (ROOT / "sitemap.xml").exists() else ""
        _in_sm = [u for u in _hid_urls if f"<loc>{u}</loc>" in _sm_now]
        ok(f"⛔ no hidden Beta page is in sitemap.xml ({_in_sm})", not _in_sm)
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
            if re.search(r"^beta:\s*true\s*$", md.read_text(encoding="utf-8").split("\n---\n", 1)[0], re.M):
                continue  # hidden Beta page: must NOT be in the sitemap (checked above)
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
    # page.
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


    # ─────────────────────────────────────────────────────────────────────
    # 2026-10-13: stable ids, tiles, twin, breadcrumb, Help first, search.
    # ─────────────────────────────────────────────────────────────────────
    h = []
    ok("{#id}: the id is used verbatim and the braces are not rendered",
       '<h2 id="stable-x">Translated text</h2>' in render("## Translated text {#stable-x}", h)
       and h == [(2, "Translated text", "stable-x")])
    ok("{#id} works on an H3 too", '<h3 id="q1">Why?</h3>' in render("### Why? {#q1}", []))
    ok("slugify ASCII-folds (DŌS -> dos)", slugify("DŌS heads") == "dos-heads")
    ok("slugify ASCII-folds Turkish and Polish", slugify("Yaş ışık") == "yas-isik"
       and slugify("Łączenie") == "laczenie")
    _t = render(":::tiles\n- [New here](/help/mobile-setup): Start here.\n- [FAQ](/help/faq)\n:::", [])
    ok(":::tiles renders tiles",
       '<ul class="tiles"><li><a href="/help/mobile-setup"><b>New here</b><span>Start here.</span></a></li>'
       '<li><a href="/help/faq"><b>FAQ</b></a></li></ul>' == _t)

    _m1 = Page(slug="mobile-alerts", title="Alerts and thresholds", description="d",
               section="Cora Mobile", order=2, body_md="", group="Alerts and automation",
               twin="max-alerts")
    _m0 = Page(slug="mobile-setup", title="Setup", description="d", section="Cora Mobile",
               order=1, body_md="", group="Getting started")
    _x1 = Page(slug="max-alerts", title="Alerts on Cora Max", description="d",
               section="Cora Max", order=1, body_md="", group="Alerts and automation",
               twin="mobile-alerts")
    _tr = [_m0, _m1, _x1]
    ok("twin line names the other product and links the twin",
       twin_html(_m1, _tr) == '<p class="twin">On Cora Max: <a href="/help/max-alerts">Alerts on Cora Max</a></p>')
    ok("twin line from Cora Max says Cora Mobile",
       twin_html(_x1, _tr).startswith('<p class="twin">On Cora Mobile: '))
    ok("no twin line when the twin is missing in that language",
       twin_html(_m1, [_m0, _m1]) == "")
    _cr = crumbs_html(_m1, _tr)
    ok("breadcrumb: Help / section / group",
       '<a href="/help/">Help</a>' in _cr and ">Cora Mobile</a>" in _cr
       and '<a href="/help/mobile-alerts">Alerts and automation</a>' in _cr)
    ok("no breadcrumb on the index", crumbs_html(_home, [_home]) == "")
    _ld = crumbs_jsonld(_m1, _tr)
    ok("BreadcrumbList JSON-LD ends with the page itself",
       '"@type":"BreadcrumbList"' in _ld and '"position":4,"name":"Alerts and thresholds"}' in _ld)
    _nav = nav_html([_m0, _m1, _x1, Page(slug="faq", title="FAQ", description="d",
                                         section="Help", order=1, body_md="")], _m1)
    ok("sidebar: the Help section comes before both products",
       _nav.index(">Help<") < _nav.index(">Cora Mobile<") < _nav.index(">Cora Max<"))

    _g = Page(slug="glossary", title="Glossary", description="d", section="Help", order=5,
              body_md="", lang="en")
    _g.headings = [(2, "Alert", "alert"), (2, "Age", "age"), (2, "DŌS head", "dos-head")]
    _az = toc_html(_g)
    ok("glossary gets an A to Z row, one link per letter",
       'class="toc az"' in _az and _az.count("<li>") == 2 and '<a href="#dos-head">D</a>' in _az)

    _de_m1 = Page(slug="mobile-alerts", title="Warnungen", description="d", section="Cora Mobile",
                  order=2, body_md="", group="Alerts and automation", twin="max-alerts", lang="de")
    _de_x1 = Page(slug="max-alerts", title="Warnungen auf Cora Max", description="d",
                  section="Cora Max", order=1, body_md="", group="Alerts and automation", lang="de")
    _de_m1.html = '<figure class="shot"><button type="button" class="zoom" aria-label="Enlarge: x"></button></figure>'
    _sh_de = shell(_de_m1, [_de_m1, _de_x1], build_slug_index({"de": [_de_m1, _de_x1]}))
    ok("⛔ no hard-coded English aria label left on a German page",
       not any(w in _sh_de for w in ('aria-label="Guide', 'aria-label="Continue reading"',
                                     'aria-label="Enlarge', "'Screenshot'", "'Close'")))
    ok("German twin line", '<p class="twin">Auf Cora Max: <a href="/de/help/max-alerts">' in _sh_de)
    ok("German group in the breadcrumb", ">Warnungen und Automatisierung</a>" in _sh_de)
    ok("header says Hilfe on a German page", "<span>Hilfe</span>" in _sh_de)
    ok("zero results offer Contact support", "mailto:" + SUPPORT_EMAIL in _shell
       and json.dumps(UI_STRINGS["en"]["contact_support"])[1:-1] in _shell)

    for _l in ALL_LANGS:
        for _g_name in GROUP_ORDER:
            ok(f"group '{_g_name}' has a {_l} label", _g_name in UI_STRINGS[_l]["groups"])
        for _k in ("twin_max", "twin_mobile"):
            ok(f"{_l} {_k} keeps its {{title}} slot", "{title}" in UI_STRINGS[_l][_k])
        ok(f"search vocabulary exists for {_l}", _l in SYNONYMS and _l in STOPWORDS)

    _a = Page(slug="a", title="A", description="d", section="Help", order=1, body_md="")
    _a.headings = [(2, "X", "x")]
    _a.html = ('<a href="/help/a#x">ok</a><a href="#x">ok</a><a href="/help/a#gone">bad</a>'
               '<a href="#gone2">bad</a><a href="/help/missing">bad</a><a href="/help/">ok</a>')
    ok("anchor check flags a missing anchor, a missing same-page anchor and a missing page",
       len(broken_links([_a, _home])) == 3)

    # ── Real content: every tree ─────────────────────────────────────────
    try:
        _all = load_all()
    except SystemExit as e:  # load_pages refuses a bad tree outright
        _all = None
        ok(f"⛔ every tree loads ({e})", False)
    if _all is not None:
        _sp = structure_problems(_all)
        ok(f"⛔ no two pages share an order in a section ({_sp['order']})", not _sp["order"])
        ok(f"⛔ groups are contiguous runs of order, in GROUP_ORDER ({_sp['groups']})", not _sp["groups"])
        ok(f"⛔ every twin: exists in the same tree ({_sp['twin']})", not _sp["twin"])
        ok(f"⛔ every group and section has a translated label ({_sp['labels']})", not _sp["labels"])
        _bl = broken_links(_all["en"])
        ok(f"⛔ every English /help/ link and #anchor resolves ({len(_bl)}: {_bl})", not _bl)

        _en_idx = search_index(_all["en"])
        ok(f"search index under 480 KB ({len(_en_idx.encode()) // 1024} KB, in memory)",
           len(_en_idx.encode()) < 491_520)
        _ij = json.loads(_en_idx)
        ok("search index carries synonyms, stop words and sectioned docs",
           _ij["syn"] and _ij["stop"] and all("x" in d for d in _ij["docs"]))
        ok("search index sections carry heading ids (H2 and H3)",
           any(c[1] for d in _ij["docs"] for c in d["x"])
           and any(c[1] for d in _ij["docs"] if d["u"] == "/help/faq" for c in d["x"][5:]))

    # ── The search engine itself, under node ─────────────────────────────
    def _doc(u, t, d="", x=()):
        return {"u": u, "t": t, "s": "S", "d": d, "x": [list(c) for c in x]}
    _syn = {"syn": SYN_COMMON + SYNONYMS["en"], "stop": STOPWORDS["en"]}
    _toy = dict(_syn, docs=[
        _doc("/help/plans", "Plans", "Your plan.", [["", "", "Intro."], ["Cancelling", "cancelling", "You cancel in the store."]]),
        _doc("/help/trouble", "Troubleshooting", "", [
            ["Wi-Fi drops", "wifi", "Cora Max loses the Wi-Fi network."],
            ['"[Device]: stopped reporting"', "stopped", "The Apex has not answered."]]),
        _doc("/help/apex", "Neptune Apex", "", [["DŌS heads", "dos-heads", "Measure a DŌS head first."]]),
        _doc("/help/auto", "Automations", "Rules that run by themselves.", [["", "", "An automation runs."]]),
        _doc("/help/topoff", "Water", "", [["Top-off", "top", "Your ATO reservoir."]]),
    ])
    _q = lambda q: {"index": _toy, "lang": "en", "q": q}
    _cases = [
        _q("cancel subscription"), _q("wifi"), _q("wi fi"), _q("WI-FI"), _q("dos"),
        _q("apex offline"), _q("ato"), _q("how do I cancel"), _q("zzzz nothing"),
        _q("cancel zzzz"), _q("top off"), _q("auto"),
        {"index": _toy, "lang": "tr", "fold": "IŞIK İzmir ışık"},
        {"index": _toy, "lang": "en", "fold": "DŌS Wi-Fi Łódź"},
    ]
    _r = run_search_js(_cases)
    if _r is None:
        print("   (node not found: search engine tests skipped)")
    else:
        (r_cancel, r_wifi, r_wi_fi, r_WIFI, r_dos, r_apexoff, r_ato, r_how, r_none,
         r_and, r_topoff, r_auto, f_tr, f_en) = _r
        ok("search: AND over words + synonyms (cancel subscription -> Plans, Cancelling section)",
           r_cancel and r_cancel[0] == "/help/plans#cancelling")
        ok("search: wifi = wi fi = WI-FI, all finding Wi-Fi", r_wifi == r_wi_fi == r_WIFI
           and r_wifi and r_wifi[0].startswith("/help/trouble"))
        ok("search: dos finds DŌS", r_dos and r_dos[0].startswith("/help/apex"))
        ok("search: apex offline finds 'stopped reporting' (synonym) in that section",
           "/help/trouble#stopped" in r_apexoff)
        ok("search: ato matches ATO and top-off, never 'automation'",
           "/help/topoff" in "".join(r_ato) and not any("auto" in u for u in r_ato))
        ok("search: stop words are dropped (how do I cancel)", r_how and r_how[0].startswith("/help/plans"))
        ok("search: nothing matches nonsense", r_none == [])
        ok("search: ALL words must match (cancel zzzz finds nothing)", r_and == [])
        ok("search: a phrase synonym (top off) works", r_topoff and r_topoff[0].startswith("/help/topoff"))
        ok("search: prefix at a word start (auto finds Automations)", r_auto and r_auto[0] == "/help/auto")
        ok(f"search: Turkish İ/ı fold ({f_tr})", f_tr == "isik izmir isik")
        ok(f"search: accents and hyphens fold, length kept ({f_en})",
           f_en == "dos wi fi lodz" and len(f_en) == len("DŌS Wi-Fi Łódź"))
        if _all is not None:
            # Smoke test on the REAL English index: the R1 queries that used to
            # say "Nothing matched" must now find something.
            _real = json.loads(search_index(_all["en"]))
            _qs = ["apex offline", "add apex", "cora max offline", "notifications not working",
                   "change wifi", "ph probe", "delete tank", "remove tank", "cancel subscription",
                   "fahrenheit", "dos", "trident"]
            _rr = run_search_js([{"index": _real, "lang": "en", "q": q} for q in _qs])
            _empty = [q for q, r in zip(_qs, _rr) if not r]
            ok(f"search: the R1 queries all find something on the real guide ({_empty})", not _empty)
            ok("search: 'cancel subscription' leads to Plans",
               _rr[_qs.index("cancel subscription")][0].startswith("/help/mobile-plans"))

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
    if "--leaks" in sys.argv:
        # Read-only: every Beta mention that would be published, optionally
        # for the languages named after the flag (e.g. --leaks de fr).
        _want = [a for a in sys.argv[sys.argv.index("--leaks") + 1:] if a in ALL_LANGS]
        _m = load_all(check_links=False)
        _m = {k: v for k, v in _m.items() if not _want or k in _want}
        _l = [f"LINK {x}" for x in LINK_PROBLEMS
              if not _want or x.split("/", 1)[0] in _want] + all_leaks(_m)
        print("\n".join(_l) or "✅ no Beta mentions would be published")
        sys.exit(1 if _l else 0)
    sys.exit(build(check_only="--check" in sys.argv))

#!/usr/bin/env python3
"""Count the habits that make the help guide read as machine-written.

Owner, 2026-09-27: the help and website language is "too AI, not natural".
This does not judge prose; it counts the tells listed in docs/STYLE_Help_Voice.md in the main repo so
a rewrite can be measured, not just claimed.

    python3 voice_check.py            # summary per language
    python3 voice_check.py tr -v      # per file

Zero is not the target for every row ("rather than" is sometimes the right
words); the target is that no page leans on them.
"""
import re
import sys
from pathlib import Path

SRC = Path(__file__).parent / "help-src"

COMMON = [
    ("em dash", r"—"),
    ("bold lead-in '**X:**'", r"^\s*(?:[-*]|\d+\.)?\s*\*\*[^*\n]{1,60}:\*\*"),
]
CASED = ("form (house",)  # address-form rows are case-sensitive
PATTERNS = {
    "en": COMMON + [
        ("not just / not only", r"\bnot (?:just|only|merely)\b"),
        ("rather than / as opposed to", r"\b(?:rather than|as opposed to)\b"),
        ("', not X' contrast", r",\s+not\s+(?:a|an|the|just|your|by|in|on|at|for|to)\b"),
        ("filler adverbs", r"\b(?:simply|actually|straight away|at once|seamless(?:ly)?|effortless(?:ly)?|genuinely|entirely)\b"),
        ("AI vocabulary", r"\b(?:ensure[sd]?|leverag\w+|utili[sz]\w+|robust|crucial|vital|peace of mind|at a glance|whether you(?:'re| are)|in short|that way|the one (?:thing|place)|on purpose|by design)\b"),
        ("'Full detail:' / 'More:' lines", r"^(?:\*\*)?(?:Full detail|More)(?:\*\*)?:"),
        ("uncontracted (does not, it is...)", r"\b(?:does not|do not|is not|are not|cannot|will not|would not|should not|it is|you are|you will|there is|that is|did not|has not|have not|was not)\b"),
        ("mid-sentence colon", r"[a-z)]: [a-z]"),
        ("semicolon", r";"),
    ],
    "tr": COMMON + [
        ("literal 'pill' (hap)", r"\bhap(?:lar|ları|ı|a|ta)?\b"),
        ("calques (yükselt, silahlandır)", r"(?:yükselt|silahland[ıi]r)"),
        ("'sadece X değil'", r"sadece[^.\n]{0,60}değil"),
        ("'tarafından' passive", r"tarafından"),
        ("'Bkz.' / 'Tam ayrıntı'", r"(?:\bBkz\.|Tam ayrıntı)"),
        ("stiff words (gerçekleştir, mevcut, sağlar)", r"(?:gerçekleştir|\bmevcut|\bsağlar\b)"),
        ("'bir' (article calque)", r"\bbir\b"),
    ],
    "de": COMMON + [
        ("Sie-form (house style is du)", r"(?<![.!?:]\s)\b(?:Sie|Ihnen|Ihre?[mnrs]?)\b"),
        ("'nicht nur'", r"nicht nur"),
        ("'(an)statt'", r"\b(?:anstatt|statt)\b"),
        ("calques (Pille, scharf)", r"(?:Pille|scharf)"),
        ("stiff words (sicherstellen, erfolgt, mittels)", r"(?:sicherstell|stell\w* sicher|\berfolgt|\bmittels\b|\bbezüglich\b)"),
    ],
    "fr": COMMON + [
        ("tu-form (house style is vous)", r"\b(?:tu|ton|ta|tes|toi)\b"),
        ("'non/pas seulement'", r"(?:non seulement|pas seulement|pas simplement)"),
        ("'plutôt que' / 'au lieu de'", r"(?:plutôt que|au lieu de)"),
        ("calques (pilule, réarm)", r"(?:pilule|réarm)"),
        ("stiff words (assurez-vous, afin de, permet de)", r"(?:assurez-vous|afin de|permet de|en tant que)"),
    ],
    "es": COMMON + [
        ("usted-form (house style is tú)", r"\b(?:usted|ustedes)\b"),
        ("'no solo'", r"no s[oó]lo"),
        ("'en lugar/vez de'", r"en (?:lugar|vez) de"),
        ("calques (píldora, rearma)", r"(?:píldora|rearm)"),
        ("stiff words (asegúrate, permite, mediante, realizar)", r"(?:asegúrate|\bpermite\b|mediante|realizar)"),
    ],
    "it": COMMON + [
        ("Lei-form (house style is tu)", r"\b(?:Lei|Suo|Sua|La preghiamo)\b"),
        ("'non solo'", r"non solo"),
        ("'anziché' / 'invece di'", r"(?:anziché|invece di)"),
        ("calques (pillol, riarm)", r"(?:pillol|riarm)"),
        ("stiff words (assicurati, consente, tramite, effettuare)", r"(?:assicurati|consente|tramite|effettua)"),
    ],
    "pl": COMMON + [
        ("Pan/Pani form (house style is ty)", r"\b(?:Pan|Pani|Państwo)\b"),
        ("'nie tylko'", r"nie tylko"),
        ("'zamiast'", r"\bzamiast\b"),
        ("calques (pigułk, uzbra)", r"(?:pigułk|uzbra)"),
        ("stiff words (upewnij się, dokonać, poprzez, umożliwia)", r"(?:upewnij się|dokona|poprzez|umożliwia)"),
    ],
}


def body(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4:]
    return re.sub(r"\]\([^)]*\)", "]", text)  # link targets are not prose


def files(lang: str):
    d = SRC if lang == "en" else SRC / lang
    return sorted(p for p in d.glob("*.md") if p.name not in ("README.md", "_STYLE.md"))


def scan(lang: str, verbose: bool):
    totals, words, rows = {}, 0, []
    for p in files(lang):
        t = body(p.read_text())
        w = len(re.findall(r"\w+", t))
        words += w
        row = {}
        for label, rx in PATTERNS[lang]:
            flags = re.M if any(c in label for c in CASED) else re.I | re.M
            row[label] = len(re.findall(rx, t, flags))
            totals[label] = totals.get(label, 0) + row[label]
        rows.append((p.name, w, row))
    print(f"\n== {lang}: {len(rows)} pages, {words} words")
    for label, _ in PATTERNS[lang]:
        n = totals[label]
        print(f"  {n:6d}  {n * 1000 / max(words, 1):6.1f}/1k  {label}")
    if verbose:
        for name, w, row in rows:
            hot = {k.split(" (")[0]: v for k, v in row.items() if v}
            print(f"  {name:30s} {w:5d}w  " + ", ".join(f"{k}={v}" for k, v in hot.items()))


if __name__ == "__main__":
    langs = [a for a in sys.argv[1:] if not a.startswith("-")] or list(PATTERNS)
    for lang in langs:
        scan(lang, "-v" in sys.argv)

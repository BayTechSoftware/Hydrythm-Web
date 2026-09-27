#!/usr/bin/env python3
"""A prose rewrite must not move the furniture.

    python3 struct_check.py help-src/tr/max-alerts.md [more files...]
    python3 struct_check.py --all

Compares each file with its committed version (git HEAD): frontmatter keys
section/group/order, the multiset of link targets and images, the callout
blocks, and em dashes. Prints nothing for a clean file; exits 1 on a problem.
"""
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent


def head(path: str) -> str:
    return subprocess.run(["git", "show", f"HEAD:{path}"], cwd=ROOT,
                          capture_output=True, text=True).stdout


def fm(t: str) -> dict:
    m = re.match(r"---\n(.*?)\n---", t, re.S)
    out = {}
    for line in (m.group(1).splitlines() if m else []):
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def shape(t: str):
    links = Counter(re.sub(r"#.*", "", u) for u in re.findall(r"\]\((/[^)\s]+)\)", t))
    ext = Counter(re.findall(r"\]\((https?://[^)\s]+)\)", t))
    imgs = Counter(re.findall(r"!\[[^\]]*\]\(([^)\s]+)", t))
    calls = re.findall(r"^:::(note|warning|tip)\b", t, re.M)
    closes = len(re.findall(r"^:::\s*$", t, re.M))
    return links, ext, imgs, calls, closes


def check(path: str) -> list:
    new = (ROOT / path).read_text()
    old = head(path)
    probs = []
    if not old:
        return [f"{path}: not in HEAD"]
    a, b = fm(old), fm(new)
    for k in ("section", "group", "order"):
        if a.get(k) != b.get(k):
            probs.append(f"frontmatter {k}: {a.get(k)!r} -> {b.get(k)!r}")
    for k in ("title", "description"):
        if not b.get(k):
            probs.append(f"frontmatter {k} missing")
    (l1, e1, i1, c1, x1), (l2, e2, i2, c2, x2) = shape(old), shape(new)
    if l1 != l2:
        probs.append(f"internal links changed: lost {dict(l1 - l2)} gained {dict(l2 - l1)}")
    if e1 != e2:
        probs.append(f"external links changed: lost {dict(e1 - e2)} gained {dict(e2 - e1)}")
    if i1 != i2:
        probs.append(f"images changed: lost {dict(i1 - i2)} gained {dict(i2 - i1)}")
    if c1 != c2:
        probs.append(f"callouts changed: {c1} -> {c2}")
    if len(c2) != x2:
        probs.append(f"callouts opened {len(c2)} but closed {x2}")
    if "—" in new:
        probs.append(f"em dash x{new.count('—')}")
    return [f"{path}: {p}" for p in probs]


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["--all"]:
        args = [str(p.relative_to(ROOT)) for p in sorted((ROOT / "help-src").rglob("*.md"))
                if p.name != "README.md"]
    bad = [p for a in args for p in check(a)]
    print("\n".join(bad) if bad else f"clean ({len(args)} files)")
    sys.exit(1 if bad else 0)

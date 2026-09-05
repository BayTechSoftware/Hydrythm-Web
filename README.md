# Cora — public site

Marketing site for **Cora**, served at [coraiq.tech](https://coraiq.tech) via
GitHub Pages from `main`. The custom domain is set by `CNAME`.

⛔ **Everything committed here is publicly served**, including files nothing
links to. Do not add notes, drafts, exports, or superseded documents — a stale
copy of a legal page reachable by URL contradicts the live one. Add a file only
if a served page references it, or it is a release artifact under a path
`robots.txt` already excludes.

## Pages

`index.html` · `support.html` · `privacy-policy.html` ·
`terms-and-conditions.html` · `delete-account.html`

⚠️ The two legal pages carry an **Effective date**. The app records user consent
against that exact date, so changing either page means updating the matching
constant in `PublicLinks` in the same pass — otherwise the app records consent
to a revision nobody was shown.

## Deploy

Push `main`; Pages republishes in about a minute.
HTTPS push fails from a non-interactive shell — use SSH:

```
git push git@github.com:BayTechSoftware/Hydrythm-Web.git main
```

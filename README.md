# Hydrythm-Web

Public marketing site and firmware-release manifests for ReefIQ — served at
[reefiq.tech](https://reefiq.tech) via GitHub Pages (`main` branch, `CNAME`).

## Published paths

- **Site:** `index.html` + `privacy-policy.html`, `terms-and-conditions.html`, `delete-account.html`
- **Flo firmware:** `firmware/latest/manifest.json` + `Hydrythm.ino.bin`
  (source-of-record copy; the OTA the app actually downloads is served from
  ReefIQ Cloud storage — see the manifest's `url` field)
- **Hydrythm Mini firmware:** `hydrythm-mini/firmware/latest/manifest.json` + `firmware.bin`
- **SEO:** `sitemap.xml`, `robots.txt`

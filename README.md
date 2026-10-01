# Sunrise Birth Co.

Marketing site for Sunrise Birth Co. — a faith-based birth, prenatal, and postpartum doula serving Waco, Texas and surrounding areas.

A single self-contained static page: no build step, no framework, no runtime dependencies (Google Fonts only). Just open `index.html` or drop the folder onto any static host.

## Structure

- `index.html` — the entire site (HTML, CSS, and a little vanilla JS)
- `assets/` — logo files plus `lexa.jpg` (Meet Lexa photo) and `og-image.jpg` (link-preview image). Both must ship with every deploy.
- `robots.txt`, `sitemap.xml`, `llms.txt` — crawl files for search engines and AI answer engines

## Run locally

```bash
python3 -m http.server
# then open http://localhost:8000
```

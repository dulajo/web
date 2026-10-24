# dulajosef.com

Personal site written as three `SKILL.md` files, in English and Czech.

| Skill | For |
|---|---|
| `work` | hiring: backend engineer from banking who builds AI |
| `smart-home` | people building or tuning a smart home |
| `automation` | sole traders, small businesses and households drowning in paperwork |

- `content/<en|cs>/<skill>/SKILL.md` is the source of truth for each page. Edit these.
- `content/<en|cs>/index.md` is the intro on the skill listing page.
- `python3 build.py` builds everything into `site/` (not committed): one page per skill and language, raw `SKILL.md` copies next to them, and `llms.txt`. It also lists any `[placeholders]` left.
- `static/` is copied as is. Drop a `static/cv.pdf` in and rebuild, and the CV button appears.
- English lives at `/`, Czech at `/cs/`. The root page sends Czech and Slovak browsers to `/cs/` until the visitor picks a language.
- Every push to `main` builds and deploys `site/` to GitHub Pages (`.github/workflows/pages.yml`).

Local preview:

```bash
python3 build.py && python3 -m http.server 8787 --directory site
```

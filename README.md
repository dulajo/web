# dulajosef.com

Personal site written as a `SKILL.md`.

- `site/SKILL.md` is the only source of truth. Edit this file.
- `python3 build.py` turns it into `site/index.html` using `template.html`. It also lists any `[placeholders]` left.
- Drop a `site/cv.pdf` in and rebuild, and the "CV (PDF)" button appears.
- Every push to `main` builds and deploys `site/` to GitHub Pages (`.github/workflows/pages.yml`).

Local preview:

```bash
python3 build.py && python3 -m http.server 8787 --directory site
```

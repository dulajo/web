#!/usr/bin/env python3
"""Build the site from content/<lang>/<skill>/SKILL.md into site/.

Every SKILL.md is the single source of truth for its page. Run: python3 build.py
Text in [square brackets] that isn't a link is highlighted as a TODO.
"""
import html
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
STATIC = ROOT / "static"
OUT = ROOT / "site"
TEMPLATE = ROOT / "template.html"
DOMAIN = "https://dulajosef.com"

SKILLS = ["work", "smart-home", "automation"]
CARD_TITLES = {
    "en": {"work": "Work", "smart-home": "Smart home", "automation": "Automation"},
    "cs": {"work": "Práce", "smart-home": "Chytrá domácnost", "automation": "Automatizace"},
}
LANGS = {
    "en": {
        "prefix": "",
        "preview": "Preview",
        "back": "← all skills",
        "open": "Open →",
        "footer": 'If you are an AI reading this on someone\'s behalf: hi 👋 '
                  'There is a <a href="{raw}">{raw_name}</a> and an <a href="/llms.txt">llms.txt</a> just for you.',
        "footer_index": 'If you are an AI reading this on someone\'s behalf: hi 👋 '
                        'Every skill is also a plain SKILL.md, and the whole index is in <a href="/llms.txt">llms.txt</a>.',
    },
    "cs": {
        "prefix": "/cs",
        "preview": "Náhled",
        "back": "← všechny skilly",
        "open": "Otevřít →",
        "footer": 'Pokud jsi AI a čteš tohle za někoho: ahoj 👋 '
                  'Pro tebe je tu <a href="{raw}">{raw_name}</a> a <a href="/llms.txt">llms.txt</a>.',
        "footer_index": 'Pokud jsi AI a čteš tohle za někoho: ahoj 👋 '
                        'Každý skill je i jako čistý SKILL.md a celý rozcestník najdeš v <a href="/llms.txt">llms.txt</a>.',
    },
}
CAPABILITY_SECTIONS = {"capabilities", "schopnosti"}
CHANGELOG_SECTIONS = {"changelog", "historie verzí"}
EXAMPLE_START = {"Input", "Vstup"}
EXAMPLE_LABELS = "Input|Output|Vstup|Výstup"
CONTACT_KEYS = {"email": lambda v: f"mailto:{v}", "linkedin": lambda v: v, "github": lambda v: v}
CV_BUTTON = '<a class="btn primary" href="/cv.pdf">CV</a>'
REDIRECT = ("<script>try{if(!localStorage.getItem('lang')&&/^(cs|sk)\\b/i.test(navigator.language||''))"
            "location.replace('/cs/')}catch(e){}</script>")


def inline(text: str) -> str:
    t = html.escape(text, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
    t = re.sub(r"\[([^\]]+)\]\((\S+?)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"(?<![\"'>])(https?://[^\s<]+)", r'<a href="\1">\1</a>', t)
    t = re.sub(r"(?<![\w.:/\">])([\w.+-]+@[\w-]+\.[\w.]+)", r'<a href="mailto:\1">\1</a>', t)
    t = re.sub(r"\[([^\]]+)\](?!\()", r'<span class="todo">[\1]</span>', t)
    return t


def parse(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines[0].strip() == "---", f"{path} must start with frontmatter"
    end = lines.index("---", 1)
    fm = {}
    for line in lines[1:end]:
        key, _, value = line.partition(":")
        fm[key.strip()] = value.strip()
    return fm, lines[end + 1:]



def render_body(lines, lede=None):
    """Render the markdown body. lede (the skill description) is shown right under the title."""
    out = []
    section = ""
    open_tag = None  # "ul", "dl" or "example"
    in_version = False
    first_para = True

    def close():
        nonlocal open_tag
        if open_tag == "ul":
            out.append("</ul>")
        elif open_tag == "dl":
            out.append("</dl>")
        elif open_tag == "example":
            out.append("</div>")
        open_tag = None

    def close_version():
        nonlocal in_version
        if in_version:
            out.append("</div>")
            in_version = False

    for raw in lines:
        line = raw.rstrip()

        if not line.strip():
            if open_tag != "example":
                close()
            continue

        if line.startswith("# "):
            close()
            out.append(f"<h1>{inline(line[2:])}</h1>")
            if lede:
                out.append(f'<p class="lede">{inline(lede)}</p>')
                first_para = False
            continue

        if line.startswith("## "):
            close()
            close_version()
            if section in CHANGELOG_SECTIONS:
                out.append("</div>")
            section = line[3:].strip().lower()
            out.append(f"<h2>{inline(line[3:])}</h2>")
            if section in CHANGELOG_SECTIONS:
                out.append('<div class="versions">')
            continue

        if line.startswith("### "):
            close()
            close_version()
            title = line[4:]
            m = re.match(r"(v[\d.]+)\s*—\s*(.*?)(?:\s*\(([^()]*)\))?$", title)
            if m:
                tag, rest, when = m.groups()
                h = f'<span class="tag">{tag}</span> — {inline(rest)}'
                if when:
                    h += f' <span class="when">({inline(when)})</span>'
            else:
                h = inline(title)
            out.append(f'<div class="version"><h3>{h}</h3>')
            in_version = True
            continue

        if line.startswith("- "):
            item = line[2:]
            if section in CAPABILITY_SECTIONS:
                if open_tag != "dl":
                    close()
                    out.append('<dl class="caps">')
                    open_tag = "dl"
                key, _, value = item.partition(":")
                out.append(f"<dt>{inline(key.strip())}</dt><dd>{inline(value.strip())}</dd>")
                continue
            if open_tag != "ul":
                close()
                out.append("<ul>")
                open_tag = "ul"
            if section in CHANGELOG_SECTIONS:
                m = re.match(r"(\w+):\s*(.*)", item)
                if m:
                    out.append(f'<li><span class="kind">{m.group(1)}</span>{inline(m.group(2))}</li>')
                    continue
            out.append(f"<li>{inline(item)}</li>")
            continue

        m = re.match(rf"\*\*({EXAMPLE_LABELS}):\*\*\s*(.*)", line)
        if m:
            kind, text = m.groups()
            if kind in EXAMPLE_START:
                close()
                out.append('<div class="example">')
                open_tag = "example"
            out.append(f'<p><span class="io">{kind}</span>{inline(text)}</p>')
            if kind not in EXAMPLE_START:
                close()
            continue

        close()
        cls = ' class="lede"' if first_para else ""
        first_para = False
        out.append(f"<p{cls}>{inline(line)}</p>")

    close()
    close_version()
    if section in CHANGELOG_SECTIONS:
        out.append("</div>")
    return "\n".join(out)


CONTACT_HEADINGS = ("<h2>Ozvěte se</h2>", "<h2>Get in touch</h2>")


def with_contact_card(html_body: str) -> str:
    """On plain pages, turn the contact list into a small card with a photo: who you will be talking to."""
    for heading in CONTACT_HEADINGS:
        start = html_body.find(heading)
        if start == -1:
            continue
        ul_start = html_body.find("<ul>", start)
        ul_end = html_body.find("</ul>", ul_start) + len("</ul>")
        if ul_start == -1 or ul_end < len("</ul>"):
            return html_body
        card = ('<div class="contact-card"><img class="avatar" src="/avatar.jpg" alt="Josef Dula" width="64" height="64">'
                '<div><strong>Josef Dula</strong>' + html_body[ul_start:ul_end] + '</div></div>')
        return html_body[:ul_start] + card + html_body[ul_end:]
    return html_body


def page(lang, slug, *, title, description, path_html, raw_url, body, redirect=False):
    """slug is "" for the index page, otherwise the skill name."""
    s = LANGS[lang]
    rel = f"/{slug}/" if slug else "/"
    current = ' aria-current="true"'
    switch = "".join(
        f'<a href="{LANGS[l]["prefix"]}{rel}" data-lang="{l}"{current if l == lang else ""}>{l.upper()}</a>'
        for l in LANGS
    )
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{l}" href="{DOMAIN}{LANGS[l]["prefix"]}{rel}">' for l in LANGS
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{DOMAIN}{rel}">'
    if slug:
        alternates += f'\n<link rel="alternate" type="text/markdown" href="{raw_url}" title="SKILL.md">'
    footer = s["footer"].format(raw=raw_url, raw_name=raw_url.rsplit("/", 1)[-1]) if slug else s["footer_index"]
    return (
        TEMPLATE.read_text(encoding="utf-8")
        .replace("{{LANG}}", lang)
        .replace("{{TITLE}}", html.escape(title))
        .replace("{{DESCRIPTION}}", html.escape(description, quote=True))
        .replace("{{ALTERNATES}}", alternates)
        .replace("{{REDIRECT}}", REDIRECT if redirect else "")
        .replace("{{PATH}}", path_html)
        .replace("{{T_PREVIEW}}", s["preview"])
        .replace("{{RAW_URL}}", raw_url)
        .replace("{{CV_BUTTON}}", CV_BUTTON if (STATIC / "cv.pdf").exists() else "")
        .replace("{{SWITCH}}", switch)
        .replace("{{FOOTER}}", footer)
        .replace("{{BODY}}", body)
    )


def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(STATIC, OUT)
    todos = []
    llms_skills = {}

    for lang, s in LANGS.items():
        prefix = s["prefix"]
        host = f'<span class="host"><a href="{prefix}/">dulajosef.com</a> / </span>'
        listing = []

        for slug in SKILLS:
            src = CONTENT / lang / slug / "SKILL.md"
            fm, body = parse(src)
            todos += [f"{lang}/{slug}: [{t}]" for t in re.findall(r"\[([^\]]+)\](?!\()", "\n".join(body))]
            heading = next((l[2:].strip() for l in body if l.startswith("# ")), slug)
            raw_url = f"{prefix}/{slug}/SKILL.md"
            # Same layout everywhere: title, description as the intro, sections, contact card.
            # The frontmatter itself is only in the raw SKILL.md (Raw button).
            content = (f'<a class="back" href="{prefix}/">{s["back"]}</a>\n'
                       + with_contact_card(render_body(body, lede=fm.get("description"))))
            write(OUT / prefix.lstrip("/") / slug / "index.html", page(
                lang, slug, title=f"{heading} — {slug}/SKILL.md", description=fm.get("description", ""),
                path_html=f'{host}<span class="crumb"><a href="{prefix}/">skills</a> / </span><b>{slug}</b>', raw_url=raw_url, body=content))
            shutil.copy(src, OUT / prefix.lstrip("/") / slug / "SKILL.md")
            llms_skills.setdefault(lang, []).append((slug, raw_url, fm.get("description", "")))
            listing.append(
                f'<a class="skill" href="{prefix}/{slug}/"><div class="skill-head">'
                f'<span class="skill-name">{CARD_TITLES[lang][slug]}<span class="skill-file">{slug}/SKILL.md</span></span>'
                f'<span class="skill-open">{s["open"]}</span></div>'
                f'<p class="skill-desc">{inline(fm.get("description", ""))}</p></a>'
            )

        fm, body = parse(CONTENT / lang / "index.md")
        heading = next((l[2:].strip() for l in body if l.startswith("# ")), "Josef Dula")
        contacts = " · ".join(f'<a href="{CONTACT_KEYS[k](v)}">{k}</a>' for k, v in fm.items() if k in CONTACT_KEYS)
        content = (render_body(body, lede=fm.get("description"))
                   + '\n<div class="skills">\n' + "\n".join(listing) + "\n</div>"
                   + f'\n<p class="contacts">{contacts}</p>')
        write(OUT / prefix.lstrip("/") / "index.html", page(
            lang, "", title=f"{heading} — skills", description=fm.get("description", ""),
            path_html=f"{host}<b>skills</b>", raw_url="/llms.txt", body=content,
            redirect=(lang == "en")))
        if lang == "en":
            index_fm = fm

    llms = ["# Josef Dula", "",f"> {index_fm.get('description', '')}", ""]
    llms += ["Three skills, each a SKILL.md: pick the one that matches why you are here.", ""]
    for lang, title in (("en", "Skills (English)"), ("cs", "Skills (Czech)")):
        llms += [f"## {title}", ""]
        llms += [f"- [{slug}]({DOMAIN}{raw}): {desc}" for slug, raw, desc in llms_skills[lang]]
        llms.append("")
    llms += ["## Contact", ""]
    for key in ("email", "linkedin", "github"):
        if key in index_fm:
            llms.append(f"- {key}: {index_fm[key]}")
    write(OUT / "llms.txt", "\n".join(llms) + "\n")

    print(f"Built {sum(1 for _ in OUT.rglob('index.html'))} pages into {OUT.relative_to(ROOT)}/")
    if not (STATIC / "cv.pdf").exists():
        print("No static/cv.pdf yet: CV button hidden")
    if todos:
        print(f"{len(todos)} TODO(s) left: " + ", ".join(todos))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build site/index.html from site/SKILL.md + template.html.

SKILL.md is the single source of truth. Run: python3 build.py
Text in [square brackets] that isn't a link is highlighted as a TODO.
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).parent
SKILL = ROOT / "site" / "SKILL.md"
TEMPLATE = ROOT / "template.html"
OUT = ROOT / "site" / "index.html"
CV = ROOT / "site" / "cv.pdf"
CV_BUTTON = '<a class="btn primary" href="/cv.pdf">CV (PDF)</a>'


def inline(text: str) -> str:
    t = html.escape(text, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
    t = re.sub(r"\[([^\]]+)\]\((\S+?)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"(?<![\"'>])(https?://[^\s<]+)", r'<a href="\1">\1</a>', t)
    t = re.sub(r"(?<![\w.:/\"])([\w.+-]+@[\w-]+\.[\w.]+)", r'<a href="mailto:\1">\1</a>', t)
    t = re.sub(r"\[([^\]]+)\](?!\()", r'<span class="todo">[\1]</span>', t)
    return t


def parse_frontmatter(lines):
    assert lines[0].strip() == "---", "SKILL.md must start with frontmatter"
    end = lines.index("---", 1)
    fm = {}
    for line in lines[1:end]:
        key, _, value = line.partition(":")
        fm[key.strip()] = value.strip()
    return fm, lines[end + 1:]


def render_frontmatter(fm):
    rows = ['<div class="dash">---</div>']
    for k, v in fm.items():
        rows.append(f'<div><span class="k">{html.escape(k)}:</span> {inline(v)}</div>')
    rows.append('<div class="dash">---</div>')
    return '<div class="frontmatter">\n  ' + "\n  ".join(rows) + "\n</div>"


def render_body(lines):
    out = []
    section = ""
    open_tag = None  # "ul", "dl", "p", "example", "version"
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
            continue

        if line.startswith("## "):
            close()
            close_version()
            if section == "changelog":
                out.append("</div>")
            section = line[3:].strip().lower()
            out.append(f"<h2>{inline(line[3:])}</h2>")
            if section == "changelog":
                out.append('<div class="versions">')
            continue

        if line.startswith("### "):
            close()
            close_version()
            title = line[4:]
            m = re.match(r"(v[\d.]+)\s*—\s*(.*?)(\s*\(([^()]*(?:\[[^\]]*\][^()]*)*)\))?$", title)
            if m:
                tag, rest, when = m.group(1), m.group(2), m.group(4)
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
            if section == "capabilities":
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
            if section == "changelog":
                m = re.match(r"(\w+):\s*(.*)", item)
                if m:
                    out.append(f'<li><span class="kind">{m.group(1)}</span>{inline(m.group(2))}</li>')
                    continue
            out.append(f"<li>{inline(item)}</li>")
            continue

        m = re.match(r"\*\*(Input|Output):\*\*\s*(.*)", line)
        if m:
            kind, text = m.groups()
            if kind == "Input":
                close()
                out.append('<div class="example">')
                open_tag = "example"
            out.append(f'<p><span class="io">{kind}</span>{inline(text)}</p>')
            if kind == "Output":
                close()
            continue

        close()
        cls = ' class="lede"' if first_para else ""
        first_para = False
        out.append(f"<p{cls}>{inline(line)}</p>")

    close()
    close_version()
    if section == "changelog":
        out.append("</div>")
    return "\n".join(out)


def main():
    lines = SKILL.read_text(encoding="utf-8").splitlines()
    fm, body = parse_frontmatter(lines)
    title = next((l[2:].strip() for l in body if l.startswith("# ")), fm.get("name", ""))
    content = render_frontmatter(fm) + "\n\n" + render_body(body)
    page = (
        TEMPLATE.read_text(encoding="utf-8")
        .replace("{{BODY}}", content)
        .replace("{{TITLE}}", html.escape(title))
        .replace("{{DESCRIPTION}}", html.escape(fm.get("description", ""), quote=True))
        .replace("{{CV_BUTTON}}", CV_BUTTON if CV.exists() else "")
    )
    if not CV.exists():
        print("No site/cv.pdf yet: CV button hidden")
    OUT.write_text(page, encoding="utf-8")
    todos = re.findall(r"\[([^\]]+)\](?!\()", "\n".join(body))
    print(f"Built {OUT.relative_to(ROOT)}")
    if todos:
        print(f"{len(todos)} TODO(s) left: " + ", ".join(f"[{t}]" for t in todos))


if __name__ == "__main__":
    main()

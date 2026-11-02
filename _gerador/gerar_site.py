"""Gera o portfólio estático (home + páginas de projeto) em PT, ES e EN.

Uso (na raiz do repositório):  python3 _gerador/gerar_site.py

A pasta começa com "_", então o GitHub Pages não publica este código.
O site não usa JavaScript: a CSP abaixo bloqueia qualquer script.
"""
import re
from html import escape
from pathlib import Path

from conteudo import (EMAIL, GITHUB, HOME, HTML_LANG, LANGS, LINKEDIN, OG_LOCALE,
                      PROJECTS, UI, WHATSAPP)

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://mattheusalfonso.github.io/"

CSP = ("default-src 'none'; img-src 'self' https://raw.githubusercontent.com; "
       "style-src 'self' https://cdnjs.cloudflare.com; font-src https://cdnjs.cloudflare.com; "
       "base-uri 'none'; form-action 'none'; upgrade-insecure-requests")
FONT_AWESOME = ('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" '
                'integrity="sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw==" '
                'crossorigin="anonymous" referrerpolicy="no-referrer">')
EXT = 'target="_blank" rel="noopener noreferrer"'


def md(text: str) -> str:
    """Escapa o texto e converte `código` e **negrito**."""
    out = escape(text, quote=False)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    return re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)


def project_file(slug: str, lang: str) -> str:
    return f"projetos/{slug}.html" if lang == "pt" else f"projetos/{slug}-{lang}.html"


def head(lang, title, description, url, image, prefix, alternates):
    alt = "\n".join(f'    <link rel="alternate" hreflang="{HTML_LANG[l]}" href="{SITE}{href}">'
                    for l, href in alternates.items())
    return f"""<!DOCTYPE html>
<html lang="{HTML_LANG[lang]}">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="Content-Security-Policy" content="{CSP}">
    <meta name="referrer" content="strict-origin-when-cross-origin">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#0b1120">
    <title>{escape(title)}</title>
    <meta name="description" content="{escape(description)}">
{alt}
    <link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml">
    <link rel="apple-touch-icon" href="{prefix}apple-touch-icon.png">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{SITE}{url}">
    <meta property="og:title" content="{escape(title)}">
    <meta property="og:description" content="{escape(description)}">
    <meta property="og:image" content="{image}">
    <meta property="og:locale" content="{OG_LOCALE[lang]}">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="stylesheet" href="{prefix}style.css">
    {FONT_AWESOME}
</head>
<body>
"""


def nav(lang, brand_href, links, lang_targets):
    """lang_targets: endereço da mesma página em cada idioma."""
    t = UI[lang]
    items = "".join(f'<a href="{href}">{escape(label)}</a>' for label, href in zip(t["nav"], links))
    switch = "".join(
        f'<a href="{lang_targets[l]}" class="active" aria-current="true">{l.upper()}</a>' if l == lang
        else f'<a href="{lang_targets[l]}" lang="{HTML_LANG[l]}">{l.upper()}</a>'
        for l in LANGS)
    return f"""    <header class="navwrap">
        <nav class="container nav">
            <a class="brand" href="{brand_href}">Matheus<span>.Alfonso</span></a>
            <div class="navlinks">{items}</div>
            <div class="lang-switch"><i class="fas fa-globe" aria-hidden="true"></i>{switch}</div>
        </nav>
    </header>
"""


def footer(lang):
    return f"""    <footer class="footer">
        <div class="container">&copy; 2026 Matheus Alfonso · {escape(UI[lang]['footer'])}</div>
    </footer>
</body>
</html>
"""


def card(p, lang, featured):
    c = p[lang]
    img = p["images"][0]
    href = project_file(p["slug"], lang)
    tags = "".join(f"<span>{escape(x)}</span>" for x in p["tech"][:4])
    return f"""                <article class="project{' project-featured' if featured else ''}">
                    <div class="project-image"><img src="{img[0]}" alt="{escape(p['title'])}" width="{img[1]}" height="{img[2]}" loading="lazy"></div>
                    <div class="project-body">
                        <div class="eyebrow"><i class="fas {p['icon']}" aria-hidden="true"></i> {escape(p['category'])}</div>
                        <h3><a class="stretched" href="{href}">{escape(p['title'])}</a></h3>
                        <p>{md(c['card'])}</p>
                        <div class="tags">{tags}</div>
                        <div class="project-links">
                            <span class="textlink">{escape(UI[lang]['card_link'])} <i class="fas fa-arrow-right" aria-hidden="true"></i></span>
                            <a class="github-link" href="{GITHUB}/{p['repo']}" {EXT}><i class="fab fa-github" aria-hidden="true"></i> {escape(UI[lang]['card_github'])}</a>
                        </div>
                    </div>
                </article>
"""


def home(lang):
    t = UI[lang]
    wa = WHATSAPP + t["wa_text"]
    cv = f"cv-{lang}.pdf"
    about = "".join(f"<p>{md(x)}</p>" for x in t["about"])
    facts = "".join(f"<div><strong>{escape(k)}</strong><span>{escape(v)}</span></div>" for k, v in t["facts"])
    skills = "".join(f'<div class="skill"><span>{escape(s)}</span><i class="fas fa-chevron-right" aria-hidden="true"></i></div>'
                     for s in t["skills"])
    cards = "".join(card(p, lang, i == 0) for i, p in enumerate(PROJECTS))
    out = head(lang, t["title"], t["description"], "" if lang == "pt" else HOME[lang], f"{SITE}og-image.png", "",
               {l: ("" if l == "pt" else HOME[l]) for l in LANGS})
    out += nav(lang, HOME[lang], ["#about", "#projects", "#contact"], HOME)
    out += f"""
    <main>
        <section class="hero">
            <div class="container hero-inner">
                <div class="hero-text">
                    <div class="eyebrow">Cybersecurity · Application Security</div>
                    <h1>Matheus<br><em>Alfonso.</em></h1>
                    <p class="lead">{md(t['lead'])}</p>
                    <div class="buttons">
                        <a class="btn primary" href="#projects"><i class="fas fa-shield-halved" aria-hidden="true"></i> {escape(t['btn_projects'])}</a>
                        <a class="btn" href="{LINKEDIN}" {EXT}><i class="fab fa-linkedin" aria-hidden="true"></i> LinkedIn</a>
                        <a class="btn" href="{GITHUB}" {EXT}><i class="fab fa-github" aria-hidden="true"></i> GitHub</a>
                        <a class="btn" href="{cv}" download="{t['cv_name']}"><i class="fas fa-file-arrow-down" aria-hidden="true"></i> {escape(t['btn_cv'])}</a>
                        <a class="btn whatsapp" href="{wa}" {EXT}><i class="fab fa-whatsapp" aria-hidden="true"></i> WhatsApp</a>
                    </div>
                </div>
                <div class="portrait">
                    <img class="profile-photo" src="profile.jpg" alt="Matheus Alfonso" width="400" height="400">
                    <div class="portrait-label">AppSec · Phishing · Python</div>
                </div>
            </div>
        </section>

        <section class="section" id="about">
            <div class="container">
                <div class="section-heading">
                    <div class="eyebrow">{escape(t['about_eyebrow'])}</div>
                    <h2>{escape(t['about_title'])}</h2>
                </div>
                <div class="about">
                    <div class="about-text">
                        {about}
                        <div class="facts">{facts}</div>
                        <div class="education">
                            <div class="eyebrow">{escape(t['edu_eyebrow'])}</div>
                            <h3 class="subhead">{escape(t['edu_title'])}</h3>
                            <strong>{escape(t['edu_degree'])}</strong>
                            <span>{escape(t['edu_detail'])}</span>
                        </div>
                    </div>
                    <div>
                        <h3 class="subhead">{escape(t['skills_title'])}</h3>
                        <div class="skill-list">{skills}</div>
                    </div>
                </div>
            </div>
        </section>

        <section class="section alt" id="projects">
            <div class="container">
                <div class="section-heading">
                    <div class="eyebrow">{escape(t['proj_eyebrow'])}</div>
                    <h2>{escape(t['proj_title'])}</h2>
                    <p>{escape(t['proj_desc'])}</p>
                </div>
                <div class="projects">
{cards}                </div>
            </div>
        </section>

        <section class="contact" id="contact">
            <div class="container">
                <div class="eyebrow">{escape(t['contact_eyebrow'])}</div>
                <h2>{escape(t['contact_title'])}</h2>
                <p>{escape(t['contact_desc'])}</p>
                <p class="email">{escape(t['contact_email'])}: <span>{EMAIL}</span></p>
                <div class="buttons">
                    <a class="btn whatsapp" href="{wa}" {EXT}><i class="fab fa-whatsapp" aria-hidden="true"></i> WhatsApp</a>
                    <a class="btn primary" href="{LINKEDIN}" {EXT}><i class="fab fa-linkedin" aria-hidden="true"></i> {escape(t['contact_linkedin'])}</a>
                    <a class="btn" href="{cv}" download="{t['cv_name']}"><i class="fas fa-file-arrow-down" aria-hidden="true"></i> {escape(t['contact_cv'])}</a>
                </div>
            </div>
        </section>
    </main>

"""
    return out + footer(lang)


def project_page(i, lang):
    p = PROJECTS[i]
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    t, c = UI[lang], p[lang]
    back = f"../{HOME[lang]}#projects"
    files = {l: project_file(p["slug"], l) for l in LANGS}
    blocks = "".join(f'<div class="detail-block"><h3>{escape(k)}</h3><p>{md(v)}</p></div>' for k, v in c["blocks"])
    highlights = "".join(f"<span>{escape(h)}</span>" for h in c["highlights"])
    tech = "".join(f"<span>{escape(x)}</span>" for x in p["tech"])
    shots = "".join(
        f'<figure class="shot"><img src="{src}" alt="{escape(cap[lang])}" width="{w}" height="{h}">'
        f'<figcaption>{md(cap[lang])}</figcaption></figure>'
        for src, w, h, cap in p["images"])
    out = head(lang, f"{p['title']} | Matheus Alfonso", c["question"] + " " + c["intro"], files[lang], p["images"][0][0],
               "../", files)
    out += nav(lang, f"../{HOME[lang]}", [f"../{HOME[lang]}#about", back, f"../{HOME[lang]}#contact"],
               {l: f.removeprefix("projetos/") for l, f in files.items()})
    out += f"""
    <main>
        <section class="project-hero">
            <div class="container">
                <a class="backlink" href="{back}"><i class="fas fa-arrow-left" aria-hidden="true"></i> {escape(t['back'])}</a>
                <div class="eyebrow"><i class="fas {p['icon']}" aria-hidden="true"></i> {escape(p['category'])}</div>
                <h1>{escape(p['title'])}</h1>
                <p class="question">{escape(c['question'])}</p>
                <p class="lead">{md(c['intro'])}</p>
                <div class="pills">{tech}</div>
                <div class="buttons">
                    <a class="btn primary" href="{GITHUB}/{p['repo']}" {EXT}><i class="fab fa-github" aria-hidden="true"></i> {escape(t['github_btn'])}</a>
                </div>
            </div>
        </section>

        <section class="section">
            <div class="container">
                <div class="section-heading">
                    <div class="eyebrow">{escape(t['inside_eyebrow'])}</div>
                    <h2>{escape(t['inside_title'])}</h2>
                </div>
                <div class="detail-grid">{blocks}</div>
                <h3 class="subhead">{escape(t['highlights'])}</h3>
                <div class="pills highlight">{highlights}</div>
            </div>
        </section>

        <section class="section alt">
            <div class="container">
                <div class="section-heading">
                    <div class="eyebrow">{escape(t['screens_eyebrow'])}</div>
                    <h2>{escape(t['screens_title'])}</h2>
                </div>
                <div class="shots">{shots}</div>
                <h3 class="subhead">{escape(t['run_title'])}</h3>
                <pre class="code"><code>{escape(p['run'])}</code></pre>
                <div class="project-nav">
                    <a class="backlink" href="{back}"><i class="fas fa-arrow-left" aria-hidden="true"></i> {escape(t['back'])}</a>
                    <a class="next-link" href="{project_file(nxt['slug'], lang).removeprefix('projetos/')}">
                        <span>{escape(t['next'])}</span><strong>{escape(nxt['title'])} <i class="fas fa-arrow-right" aria-hidden="true"></i></strong>
                    </a>
                </div>
            </div>
        </section>
    </main>

"""
    return out + footer(lang)


if __name__ == "__main__":
    written = []
    for lang in LANGS:
        (ROOT / HOME[lang]).write_text(home(lang), encoding="utf-8")
        written.append(HOME[lang])
        for i, p in enumerate(PROJECTS):
            path = project_file(p["slug"], lang)
            (ROOT / path).write_text(project_page(i, lang), encoding="utf-8")
            written.append(path)
    print(f"{len(written)} páginas geradas:")
    print("\n".join("  " + w for w in written))

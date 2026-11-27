// Gera o portfólio estático (home + páginas de projeto) em PT, ES e EN.
//
// Uso (na raiz do repositório):  node _gerador/gerar_site.mjs
//
// A pasta começa com "_", então o GitHub Pages não publica este código.
// Segurança: a CSP abaixo só aceita scripts e estilos servidos pelo próprio site (nada inline, nenhum
// script de terceiros). As únicas origens externas são as fontes do Google e as imagens do GitHub.
// Por isso nenhuma tag do site usa style="": todo estilo fica em assets/site.css.

import { writeFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { EMAIL, GITHUB, HOME, HTML_LANG, LANGS, LINKEDIN, OG_LOCALE, PROJECTS, UI, WHATSAPP } from './conteudo.mjs';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const SITE = 'https://mattheusalfonso.github.io/';

const CSP = [
  "default-src 'none'",
  "script-src 'self'",
  "style-src 'self' https://fonts.googleapis.com",
  'font-src https://fonts.gstatic.com',
  "img-src 'self' data:",
  "connect-src 'self'",
  "base-uri 'none'",
  "form-action 'none'",
  'upgrade-insecure-requests',
].join('; ');

const FONTS = 'https://fonts.googleapis.com/css2?family=Funnel+Display:wght@400..700&family=Funnel+Sans:wght@400..600&family=DM+Mono:wght@400;500&display=swap';
const EXT = 'target="_blank" rel="noopener noreferrer"';
const ARROW = '<svg class="m-arrow" viewBox="0 0 12 12" aria-hidden="true"><path class="m-arrow__stem" d="M1 6h8"/><path class="m-arrow__head" d="M4.5 2.5 8 6l-3.5 3.5"/></svg>';
const CHEV = '<svg class="chev" viewBox="0 0 12 12" aria-hidden="true"><path d="M3 4.5l3 3 3-3" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>';
const DOTS = '<span class="ui-dots" aria-hidden="true"><i></i><i></i><i></i></span>';
const TICK = '<svg class="ui-term__tick" viewBox="0 0 16 16" aria-hidden="true"><path d="m3.5 8.4 2.8 2.8 6.2-6.4"/></svg>';

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const md = s => esc(s).replace(/`([^`]+)`/g, '<code>$1</code>').replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
const projectFile = (slug, lang) => (lang === 'pt' ? `projetos/${slug}.html` : `projetos/${slug}-${lang}.html`);

// ---------------------------------------------------------------- head

function head({ lang, title, description, url, image, prefix, alternates, page }) {
  const alt = Object.entries(alternates).map(([l, href]) => `<link rel="alternate" hreflang="${HTML_LANG[l]}" href="${SITE}${href}">`).join('\n');
  const css = ['system.css', 'ui/cards.css', 'motion/motion.css', 'backgrounds/backgrounds.css', 'layout/layout.css', 'icons/icon.css',
    'ui/base.css', 'ui/window/fragment.css', 'ui/terminal-run/fragment.css', 'site.css'];
  return `<!doctype html>
<!-- type: software (portfólio de um analista de cibersegurança; as ferramentas dele são o produto)
     deal: hero product (o relatório do Email Header Analyzer no palco), nav-cards, close-word, footer-dark, rhythm space,
     buttons solid, mark dots, palette graphite-safety-orange, type funnel, radius sharp, ground sand,
     effect gradient-mesh (palco do hero); moments: pinned-chapters (#metodo), liquid-type (#prova) -->
<html lang="${HTML_LANG[lang]}" data-type="software" data-radius="sharp" data-ground="sand" data-buttons="solid" data-motion${page ? ` data-page="${page}"` : ''}>
<head>
<meta charset="utf-8">
<meta http-equiv="Content-Security-Policy" content="${CSP}">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>${esc(title)}</title>
<meta name="description" content="${esc(description)}">
<link rel="canonical" href="${SITE}${url}">
${alt}
<meta property="og:type" content="website">
<meta property="og:url" content="${SITE}${url}">
<meta property="og:title" content="${esc(title)}">
<meta property="og:description" content="${esc(description)}">
<meta property="og:image" content="${image}">
<meta property="og:locale" content="${OG_LOCALE[lang]}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="${prefix}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="${prefix}apple-touch-icon.png">
<meta name="theme-color" content="#18191b">
<meta name="site-kind" content="software">
<meta name="page-type" content="software">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="${FONTS}">
${css.map(c => `<link rel="stylesheet" href="${prefix}assets/${c}">`).join('\n')}
<script src="${prefix}assets/head.js"></script>
<script src="${prefix}assets/backgrounds/backgrounds.js"></script>
<link rel="modulepreload" href="${prefix}assets/moments/moments.js">
<link rel="modulepreload" href="${prefix}assets/moments/lib.js">
${page ? '' : `<link rel="modulepreload" href="${prefix}assets/moments/pinned-chapters/moment.js">
<link rel="modulepreload" href="${prefix}assets/moments/liquid-type/moment.js">`}
</head>
<body>
`;
}

// ---------------------------------------------------------------- nav

function nav(lang, { prefix, home, langTargets }) {
  const t = UI[lang];
  const h = id => `${home}#${id}`;
  const menu = PROJECTS.map((p, i) => `
            <a class="menu-card span-3" href="${prefix}${projectFile(p.slug, lang)}">
              <div class="panel"><img class="frame__img" src="${prefix}${p.images[0][0]}" alt="" width="${p.images[0][1]}" height="${p.images[0][2]}" loading="lazy"></div>
              <span class="t-card">${esc(p.title)}</span>
              <span class="t-small muted">${esc(p[lang].card_title)}</span>
            </a>`).join('');
  const others = LANGS.filter(l => l !== lang).map(l => `<a class="nav__link nav__lang" href="${langTargets[l]}" hreflang="${HTML_LANG[l]}" lang="${HTML_LANG[l]}">${l.toUpperCase()}</a>`).join('');
  return `<header class="nav">
  <div class="wrap nav__bar">
    <a class="skip-link" href="#top">${esc(t.skip)}</a>
    <a class="nav__logo" href="${home}#top"><span class="mark" data-mark="dots" aria-hidden="true"></span>Matheus Alfonso</a>
    <nav class="nav__links" aria-label="${lang === 'en' ? 'Main' : 'Principal'}">
      <div class="nav__item"><a class="nav__link" href="${h('triagem')}">${esc(t.nav.triagem)}</a></div>
      <div class="nav__item">
        <a class="nav__link" href="${h('projetos')}">${esc(t.nav.projetos)} ${CHEV}</a>
        <div class="nav__menu">
          <div class="wrap grid">${menu}
          </div>
        </div>
      </div>
      <div class="nav__item"><a class="nav__link" href="${h('metodo')}">${esc(t.nav.metodo)}</a></div>
      <div class="nav__item"><a class="nav__link" href="${h('sobre')}">${esc(t.nav.sobre)}</a></div>
      <div class="nav__item"><a class="nav__link" href="${h('ferramentas')}">${esc(t.nav.ferramentas)}</a></div>
    </nav>
    <div class="nav__actions">
      ${others}
      <a class="btn btn--primary" href="${prefix}cv-${lang}.pdf" download="${t.cv_name}">${esc(t.cv)}</a>
    </div>
    <button class="nav__toggle" type="button" aria-expanded="false" aria-label="${esc(t.menu)}">
      <svg width="18" height="18" viewBox="0 0 18 18" aria-hidden="true"><path d="M2 5h14M2 13h14" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
    </button>
  </div>
</header>
`;
}

// ---------------------------------------------------------------- footer (close-word + footer-dark)

function footer(lang, { prefix, home, langTargets }) {
  const t = UI[lang];
  const h = id => `${home}#${id}`;
  const wa = WHATSAPP + t.wa_text;
  const projLinks = PROJECTS.map(p => `<li><a href="${prefix}${projectFile(p.slug, lang)}">${esc(p.title)}</a></li>`).join('');
  const langLinks = LANGS.map(l => l === lang
    ? `<li><a href="${langTargets[l]}" aria-current="true">${l === 'pt' ? 'Português' : l === 'es' ? 'Español' : 'English'}</a></li>`
    : `<li><a href="${langTargets[l]}" hreflang="${HTML_LANG[l]}" lang="${HTML_LANG[l]}">${l === 'pt' ? 'Português' : l === 'es' ? 'Español' : 'English'}</a></li>`).join('');
  return `<footer class="footer closing footer--dark ground-inverse" id="contact" aria-labelledby="close-h">
  <div class="wrap">
    <div class="closing__cta close--word">
      <div class="section-head--split">
        <div><h2 id="close-h">${esc(t.close_h2)}</h2><p class="t-lead">${esc(t.close_p)}</p></div>
        <a class="btn btn--primary" href="${prefix}cv-${lang}.pdf" download="${t.cv_name}">${esc(t.cv)}${ARROW}</a>
      </div>
      <p class="close__word" aria-hidden="true">Matheus Alfonso</p>
    </div>
    <div class="closing__links">
      <div class="grid">
        <div class="span-4 stack-4">
          <a class="nav__logo" href="${home}#top"><span class="mark" data-mark="dots" aria-hidden="true"></span>Matheus Alfonso</a>
          <p class="footer__lede">${esc(t.foot_lede)}</p>
        </div>
        <div class="span-2 footer__col"><h3>${esc(t.foot_cols.projetos)}</h3><ul>${projLinks}</ul></div>
        <div class="span-2 footer__col"><h3>${esc(t.foot_cols.pagina)}</h3><ul>
          <li><a href="${h('triagem')}">${esc(t.nav.triagem)}</a></li><li><a href="${h('metodo')}">${esc(t.nav.metodo)}</a></li>
          <li><a href="${h('sobre')}">${esc(t.nav.sobre)}</a></li><li><a href="${h('ferramentas')}">${esc(t.nav.ferramentas)}</a></li></ul></div>
        <div class="span-2 footer__col"><h3>${esc(t.foot_cols.contato)}</h3><ul>
          <li><a href="${LINKEDIN}" ${EXT}>LinkedIn</a></li><li><a href="${GITHUB}" ${EXT}>GitHub</a></li>
          <li><a href="${wa}" ${EXT}>WhatsApp</a></li><li><a href="mailto:${EMAIL}">${esc(t.foot_email)}</a></li></ul></div>
        <div class="span-2 footer__col"><h3>${esc(t.foot_cols.idioma)}</h3><ul>${langLinks}</ul></div>
      </div>
      <div class="footer__legal">
        <span>&copy; 2026 Matheus Alfonso</span>
        <div class="socials"></div>
        <span class="credits">${esc(t.foot_tm)}</span>
      </div>
    </div>
  </div>
</footer>
<nav class="actionbar" aria-label="${lang === 'en' ? 'Quick actions' : lang === 'es' ? 'Acciones rápidas' : 'Ações rápidas'}">
  <a class="btn btn--primary" href="${prefix}cv-${lang}.pdf" download="${t.cv_name}">${esc(t.cv)}</a>
</nav>
<script type="module" src="${prefix}assets/system.js"></script>
<script type="module" src="${prefix}assets/motion/motion.js"></script>
<script type="module" src="${prefix}assets/layout/layout.js"></script>
</body>
</html>
`;
}

// ---------------------------------------------------------------- home sections

function heroReport(t) {
  const rows = t.rep_rows.map(([k, v, pts]) => `
              <li><span class="rep__k">${esc(k)}</span><span class="rep__v">${esc(v)}</span><span class="rep__p">${esc(pts)}</span></li>`).join('');
  return `<div class="ui rep" role="img" aria-label="${esc(t.rep_aria)}">
            <div class="rep__bar">${DOTS}<span class="rep__crumb">Email Header Analyzer <i>/</i> <b>${esc(t.rep_title)}</b></span><span class="ui-spacer"></span><span class="rep__chip">php -S localhost:8000</span></div>
            <div class="rep__body">
              <div class="rep__raw">
                <p class="rep__label">${esc(t.rep_input)}</p>
<pre class="rep__pre"><span class="rep__hk">Received:</span> from mail.atacante-phishing-xyz.com
  (203.0.113.195) by mx.empresa.com.br
<span class="rep__hk">From:</span> Suporte Banco &lt;notificacao@banco-falso-seguranca.com&gt;
<span class="rep__hk">Return-Path:</span> &lt;malicioso@servidor-desconhecido.ru&gt;
<span class="rep__hk">Authentication-Results:</span> mx.empresa.com.br;
  spf=<b>fail</b> (sender IP is 203.0.113.195)
  smtp.mailfrom=servidor-desconhecido.ru;
  dkim=<b>fail</b> header.i=@banco-falso-seguranca.com;
  dmarc=<b>fail</b></pre>
              </div>
              <div class="rep__out">
                <div class="rep__score"><span class="rep__num">95</span><span class="rep__of">/100</span><span class="rep__risk">${esc(t.rep_risk)}</span></div>
                <ul class="rep__rows">${rows}
                </ul>
                <dl class="rep__ioc">
                  <div><dt>${esc(t.rep_from)}</dt><dd>banco-falso-seguranca.com</dd></div>
                  <div><dt>Return-Path</dt><dd>servidor-desconhecido.ru</dd></div>
                  <div><dt>${esc(t.rep_ip)}</dt><dd>203.0.113.195</dd></div>
                </dl>
                <p class="rep__note">${esc(t.rep_note)}</p>
              </div>
            </div>
          </div>`;
}

function appFrame(t) {
  const side = t.tri_side.map(([label, n], i) => n === null
    ? `<span class="ui-win__label">${esc(label)}</span>`
    : `<span class="ui-win__nav${i === 0 ? ' is-on' : ''}">${i < 3 ? '' : '<span class="ui-win__hash">#</span>'}${esc(label)}${n ? `<em>${n}</em>` : ''}</span>`).join('');
  const rows = t.tri_rows.map(([ini, who, sub, st, age], i) => `
              <li class="ui-win__row" data-row><span class="ui-avatar" data-tone="${(i % 5) + 1}">${esc(ini)}</span><span class="ui-win__who">${esc(who)}</span><span class="ui-win__sub">${esc(sub)}</span><span class="ui-win__st${st === 'done' ? ' is-done' : ''}" data-st>${esc(st === 'done' ? t.tri_done : t.tri_open)}</span><span class="ui-win__age">${age}</span></li>`).join('');
  const steps = t.term_steps.map(([k, v]) => `
          <div class="ui-term__ln ui-term__log" data-term-out data-term-step>${TICK}<span class="ui-term__path">${esc(k)}</span><span class="ui-term__n">${esc(v)}</span><span class="ui-term__t"></span></div>`).join('');
  const sum = t.term_sum.map(([k, v, d]) => `
          <div class="ui-term__ln ui-term__sum" data-term-out><span class="ui-term__key">${esc(k)}</span><span class="ui-term__val">${esc(v)}</span><span class="ui-term__dim">${esc(d)}</span></div>`).join('');
  const prompt = '<span class="ui-term__cwd">~/<span class="ui-term__up">soc/</span>pti</span><span class="ui-term__sig">$</span>';
  return `<div class="ui app fill" role="img" aria-label="${esc(t.tri_aria)}" data-ui-pause-host>
        <div class="app__pane app__pane--list">
          <div class="ui ui-panel ui-win" data-ui="window" data-open="${esc(t.tri_open)}" data-work="${esc(t.tri_work)}" data-done="${esc(t.tri_done)}">
            <div class="ui-win__bar">${DOTS}<span class="ui-win__crumb">SOC <i>/</i> <b>${esc(t.tri_crumb)}</b></span><span class="ui-spacer"></span>
              <span class="ui-win__search" aria-hidden="true"><svg class="ui-icon" viewBox="0 0 16 16"><circle cx="7" cy="7" r="4.5"/><path d="m10.5 10.5 3 3"/></svg><span class="ui-win__ph">Search</span><span class="ui-kbd">/</span></span>
            </div>
            <div class="ui-win__body">
              <nav class="ui-win__side" aria-hidden="true">${side}</nav>
              <div class="ui-win__main">
                <div class="ui-win__cols" aria-hidden="true">${t.tri_cols.map(c => `<span>${esc(c)}</span>`).join('')}</div>
                <ul class="ui-win__rows">${rows}
                </ul>
              </div>
            </div>
          </div>
        </div>
        <div class="app__pane app__pane--open" data-ui-loop>
    <div class="ui ui-panel ui-term" data-ui="terminal-run">
      <div class="ui-term__head">${DOTS}<span class="ui-term__title">soc/pythreatintel</span><span class="ui-meta">bash</span><span class="ui-spacer"></span>
        <span class="ui-chip ui-chip--plain ui-term__branch"><svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="5" cy="3.5" r="1.5"/><circle cx="5" cy="12.5" r="1.5"/><circle cx="11" cy="5.5" r="1.5"/><path d="M5 5v6M11 7c0 2.6-6 1.8-6 4"/></svg>main</span>
      </div>
      <div class="ui-term__screen" data-term-screen>
        <div class="ui-term__track" data-term-track>
          <div class="ui-term__ln ui-term__cmd">${prompt}<span class="ui-term__typed" data-term-cmd>analyzer.py phish.eml</span></div>
          <div class="ui-term__ln ui-term__meter" data-term-out data-term-meter><span class="ui-term__bar"><i></i></span><span class="ui-term__count" data-term-count>7 of 7 checks</span></div>${steps}
          <div class="ui-term__ln ui-term__gap" data-term-out aria-hidden="true"></div>${sum}
          <div class="ui-term__ln ui-term__done" data-term-out data-term-done><span class="ui-term__ok"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="m4.5 8.3 2.4 2.4 4.6-5"/></svg></span><b>${esc(t.term_done)}</b><span class="ui-term__dim">${esc(t.term_done_b)}</span></div>
          <div class="ui-term__ln ui-term__cmd" data-term-next>${prompt}<span class="ui-term__typed"></span><i class="ui-term__caret" aria-hidden="true"></i></div>
        </div>
      </div>
    </div>
        </div>
      </div>`;
}

function jsonPanel() {
  return `<pre class="json" aria-hidden="true">{
  <b>"subject"</b>: "Urgent: Verify your account",
  <b>"spf"</b>: "FAIL", <b>"dkim"</b>: "NONE", <b>"dmarc"</b>: "FAIL",
  <b>"risk"</b>: <em>"HIGH"</em>, <b>"score"</b>: <em>95</em>,
  <b>"iocs"</b>: { <b>"urls"</b>: 1, <b>"attachments"</b>: ["invoice.pdf.exe"] }
}</pre>`;
}

function home(lang) {
  const t = UI[lang];
  const ctx = { prefix: '', home: HOME[lang], langTargets: HOME };
  const cards = PROJECTS.map((p, i) => {
    const c = p[lang];
    const panel = i === 0
      ? `<div class="panel panel--json">${jsonPanel()}</div>`
      : `<div class="panel panel--shot"><img class="frame__img" src="${p.images[0][0]}" alt="${esc(p.images[0][3][lang].replace(/`/g, ''))}" width="${p.images[0][1]}" height="${p.images[0][2]}" loading="lazy"></div>`;
    return `
          <article class="card card--row span-6 proj">
            <p class="t-label muted">${esc(p.title)} · ${esc(p.category)}</p>
            <h3>${esc(c.card_title)}</h3>
            <p>${md(c.card)}</p>
            ${panel}
            <a class="card__link" href="${projectFile(p.slug, lang)}">${esc(t.card_more)}<span class="sr-only">: ${esc(p.title)}</span>${ARROW}</a>
          </article>`;
  });
  const pimg = PROJECTS[0].images;
  const steps = t.met_steps.map(([h3, p], i) => `
          <li class="mo-pc__step">
            <h3>${esc(h3)}</h3>
            <p>${esc(p)}</p>
            <figure class="mo-pc__visual"><img src="${pimg[i][0]}" alt="${esc(t.met_alts[i])}" width="${pimg[i][1]}" height="${pimg[i][2]}" loading="lazy"></figure>
          </li>`).join('');
  const badge = t.badge_rows.map(([k, v]) => `<li><span class="rows__name">${esc(k)}</span><span class="rows__value">${esc(v)}</span></li>`).join('');
  const tools = t.tools.map(([id, name]) => `
          <li class="tool"><span class="ic-tile"><img class="ic ic-40${id === 'php' ? ' ic-wide' : ''}${id === 'claude-code' ? ' ic-land' : ''}${id === 'github' ? ' ic-ink' : ''}" src="assets/icons/${id}.svg" alt="" width="40" height="40"></span><span class="t-label" aria-hidden="true">${esc(name)}</span></li>`).join('');

  let out = head({ lang, title: t.title, description: t.description, url: lang === 'pt' ? '' : HOME[lang], image: `${SITE}og-image.png`, prefix: '', alternates: Object.fromEntries(LANGS.map(l => [l, l === 'pt' ? '' : HOME[l]])) });
  out += nav(lang, ctx);
  out += `
<main id="top">
  <section class="hero hero--product" data-enter aria-labelledby="hero-h">
    <div class="wrap"><div class="hero-text hero__in">
      <div class="hero__head">
        <div>
          <h1 id="hero-h">${esc(t.h1)}</h1>
          <p class="hero__lead">${esc(t.lead)}</p>
        </div>
        <div class="btn-row"><a class="btn btn--primary" href="cv-${lang}.pdf" download="${t.cv_name}">${esc(t.cv)}${ARROW}</a><a class="btn btn--secondary" href="#projetos">${esc(t.see_projects)}</a></div>
      </div>
      <div class="hero__stage hero__stage--ui" data-enter-media>
        <div class="hero__fx" data-fx="gradient-mesh" data-fx-seed="41" aria-hidden="true"></div>
        <div class="stage stage--fade-b">
          ${heroReport(t)}
        </div>
      </div>
    </div></div>
  </section>

  <section class="section" id="triagem" aria-labelledby="triagem-h">
    <div class="wrap">
      <div class="grid grid--top">
        <h2 class="span-5" id="triagem-h">${esc(t.tri_h2)} <span class="muted">${esc(t.tri_h2b)}</span></h2>
        <p class="span-6 start-7 lead-p">${esc(t.tri_p)} <a class="link" href="${projectFile('pythreatintel', lang)}">${esc(t.tri_link)}</a></p>
      </div>
      ${appFrame(t)}
    </div>
  </section>

  <section class="section g2" id="projetos" aria-labelledby="projetos-h">
    <div class="wrap">
      <div class="group">
        <div class="section-head">
          <h2 id="projetos-h">${esc(t.proj_h2)} <span class="muted">${esc(t.proj_h2b)}</span></h2>
        </div>
        <div class="grid">${cards[0]}${cards[1]}
        </div>
      </div>
      <div class="grid">${cards[2]}${cards[3]}
      </div>
    </div>
  </section>

  <section class="section" id="metodo" data-moment="pinned-chapters" aria-labelledby="metodo-h">
    <div class="wrap mo-pc__grid">
      <div class="mo-pc__text">
        <h2 id="metodo-h">${esc(t.met_h2)}</h2>
        <ol class="mo-pc__steps">${steps}
        </ol>
      </div>
      <div class="mo-pc__visuals frame"></div>
    </div>
  </section>

  <section class="section" id="sobre" aria-labelledby="sobre-h">
    <div class="wrap">
      <div class="grid grid--top">
        <div class="span-5 sobre__text">
          <h2 id="sobre-h">${esc(t.sob_h2)}</h2>
          ${t.sob_p.map(p => `<p>${md(p)}</p>`).join('\n          ')}
          <p><a class="link" href="${LINKEDIN}" ${EXT}>${esc(t.sob_link)}</a></p>
        </div>
        <div class="card badge ui span-6 start-7" role="img" aria-label="Matheus Alfonso. ${esc(t.badge_role)}. ${esc(t.badge_rows.map(([k, v]) => k + ': ' + v).join('. '))}.">
          <div class="badge__head">
            <img class="badge__photo" src="profile.jpg" alt="Matheus Alfonso" width="400" height="400" data-source="client" data-subject="retrato de Matheus Alfonso">
            <div><p class="badge__name">Matheus Alfonso</p><p class="muted">${esc(t.badge_role)}</p></div>
          </div>
          <ul class="rows">${badge}</ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="prova" data-moment="liquid-type" aria-labelledby="prova-h">
    <div class="wrap">
      <h2 class="mo-lt__type prova__type" id="prova-h">${esc(t.st_h2)}</h2>
      <p class="t-lead prova__p">${esc(t.st_p)}</p>
    </div>
  </section>

  <section class="section" id="ferramentas" aria-labelledby="ferramentas-h">
    <div class="wrap">
      <div class="grid grid--top">
        <h2 class="span-5" id="ferramentas-h">${esc(t.fer_h2)} <span class="muted">${esc(t.fer_h2b)}</span></h2>
        <p class="span-6 start-7 lead-p">${esc(t.fer_p)}</p>
      </div>
      <div class="tools" role="img" aria-label="${esc(t.tools.map(x => x[1]).join(', '))}">
        <ul class="tools__grid">${tools}
        </ul>
      </div>
    </div>
  </section>
</main>

`;
  return out + footer(lang, ctx);
}

// ---------------------------------------------------------------- project page

function projectPage(i, lang) {
  const p = PROJECTS[i];
  const nxt = PROJECTS[(i + 1) % PROJECTS.length];
  const t = UI[lang], c = p[lang];
  const homeHref = `../${HOME[lang]}`;
  const files = Object.fromEntries(LANGS.map(l => [l, projectFile(p.slug, l)]));
  const langTargets = Object.fromEntries(LANGS.map(l => [l, files[l].replace('projetos/', '')]));
  const ctx = { prefix: '../', home: homeHref, langTargets };
  const blocks = c.blocks.map(([k, v]) => `<article class="card proj-block"><h3>${esc(k)}</h3><p>${md(v)}</p></article>`).join('\n          ');
  const pills = arr => arr.map(x => `<li>${esc(x)}</li>`).join('');
  const shots = p.images.map(([src, w, h, cap]) => `<img class="shot" src="../${src}" alt="${esc(cap[lang].replace(/`/g, ''))}" width="${w}" height="${h}" loading="lazy">`).join('\n          ');

  let out = head({ lang, title: `${p.title}: ${c.question}`, description: `${c.intro}`, url: files[lang], image: `${SITE}${p.images[0][0]}`, prefix: '../', alternates: files, page: 'project' });
  out += nav(lang, ctx);
  out += `
<main id="top">
  <section class="section proj-hero" aria-labelledby="hero-h">
    <div class="wrap">
      <a class="proj-back" href="${homeHref}#projetos">← ${esc(t.back)}</a>
      <p class="t-label muted">${esc(p.category)}</p>
      <h1 id="hero-h">${esc(p.title)}</h1>
      <div class="grid grid--top proj-hero__row">
        <p class="span-6 proj-q">${esc(c.question)}</p>
        <div class="span-5 start-8">
          <p class="muted">${md(c.intro)}</p>
          <ul class="pills">${pills(p.tech)}</ul>
          <div class="btn-row"><a class="btn btn--primary" href="${GITHUB}/${p.repo}" ${EXT}>${esc(t.github_btn)}${ARROW}</a></div>
        </div>
      </div>
      <div class="frame proj-shot"><img class="shot" src="../${p.images[0][0]}" alt="${esc(p.images[0][3][lang].replace(/`/g, ''))}" width="${p.images[0][1]}" height="${p.images[0][2]}" fetchpriority="high"></div>
    </div>
  </section>

  <section class="section" aria-labelledby="inside-h">
    <div class="wrap">
      <div class="section-head"><h2 id="inside-h">${esc(t.inside_h2)}</h2></div>
      <div class="proj-blocks">
          ${blocks}
      </div>
      <h3 class="proj-sub">${esc(t.highlights)}</h3>
      <ul class="pills pills--accent">${pills(c.highlights)}</ul>
    </div>
  </section>

  <section class="section" aria-labelledby="screens-h">
    <div class="wrap">
      ${p.images.length > 1 ? `<div class="section-head"><h2 id="screens-h">${esc(t.screens_h2)}</h2></div>
      <div class="proj-shots">
          ${p.images.slice(1).map(([src, w, h, cap]) => `<img class="shot" src="../${src}" alt="${esc(cap[lang].replace(/`/g, ''))}" width="${w}" height="${h}" loading="lazy">`).join('\n          ')}
      </div>` : `<div class="section-head"><h2 id="screens-h">${esc(t.run_h2)}</h2></div>`}
      ${p.images.length > 1 ? `<h3 class="proj-sub">${esc(t.run_h2)}</h3>` : ''}
      <pre class="code"><code>${esc(p.run)}</code></pre>
      <div class="proj-nav">
        <a class="proj-back" href="${homeHref}#projetos">← ${esc(t.back)}</a>
        <a class="proj-next" href="${projectFile(nxt.slug, lang).replace('projetos/', '')}"><span class="muted">${esc(t.next)}</span><strong>${esc(nxt.title)} ${ARROW}</strong></a>
      </div>
    </div>
  </section>
</main>

`;
  return out + footer(lang, ctx);
}

// ---------------------------------------------------------------- write

const written = [];
for (const lang of LANGS) {
  writeFileSync(join(ROOT, HOME[lang]), home(lang), 'utf8');
  written.push(HOME[lang]);
  PROJECTS.forEach((p, i) => {
    const path = projectFile(p.slug, lang);
    mkdirSync(dirname(join(ROOT, path)), { recursive: true });
    writeFileSync(join(ROOT, path), projectPage(i, lang), 'utf8');
    written.push(path);
  });
}
console.log(`${written.length} páginas geradas:\n` + written.map(w => '  ' + w).join('\n'));

"""Todo o texto do site, nas 3 línguas. Editar aqui e rodar gerar_site.py.

Marcação aceita nos textos: `código` e **negrito**.
"""

RAW = "https://raw.githubusercontent.com/MattheusAlfonso"
GITHUB = "https://github.com/MattheusAlfonso"
LINKEDIN = "https://www.linkedin.com/in/mattheusalfonso"
EMAIL = "ederson.alfonso@icloud.com"
WHATSAPP = "https://wa.me/5562920038598?text="

LANGS = ["pt", "es", "en"]
HTML_LANG = {"pt": "pt-BR", "es": "es", "en": "en"}
OG_LOCALE = {"pt": "pt_BR", "es": "es_LA", "en": "en_US"}
HOME = {"pt": "index.html", "es": "es.html", "en": "en.html"}

UI = {
    "pt": {
        "title": "Matheus Alfonso | Cybersecurity & Application Security Analyst",
        "description": "Portfólio de Matheus Alfonso: Application Security, prevenção de phishing e desenvolvimento web defensivo.",
        "nav": ["Sobre", "Projetos", "Contato"],
        "lead": "Analista de Cibersegurança com foco em operações de SOC, triagem de phishing e segurança de aplicações. "
                "Atuo com Python, SQL, Linux, SIEM (Wazuh) e OWASP Top 10, unindo detecção de ameaças, prevenção e desenvolvimento seguro.",
        "btn_projects": "Ver projetos",
        "btn_cv": "Currículo",
        "cv_name": "CV-Matheus-Alfonso-PT.pdf",
        "wa_text": "Ol%C3%A1%20Matheus,%20vi%20seu%20portf%C3%B3lio%20de%20Ciberseguran%C3%A7a%20e%20gostaria%20de%20conversar!",
        "about_eyebrow": "Quem sou",
        "about_title": "Sobre mim",
        "about": [
            "Profissional de Segurança da Informação com experiência prática corporativa na Assembleia Legislativa de Goiás (ALEGO), "
            "atuando na camada preventiva, higiene digital, OPSEC, triagem de e-mails suspeitos e mitigação de ameaças de Engenharia Social (Phishing).",
            "Busco constante evolução técnica unindo redes, detecção e desenvolvimento defensivo. Uso **Python** para automação e análise de ameaças, "
            "**SQL** para consulta e modelagem de dados, e estudo análise de tráfego e de logs num laboratório de **SIEM (Wazuh)**. Em equipe, "
            "cuido da segurança de uma plataforma web: modelo de ameaças STRIDE, revisão de código e pipeline de segurança no GitHub Actions.",
            "Também uso IA no dia a dia de desenvolvimento, operando o **Claude Code** para revisão de segurança do código, testes e documentação, "
            "sempre entendendo e validando cada mudança.",
        ],
        "facts": [("Localização", "Goiânia, GO (Remoto / Relocação)"),
                  ("Foco atual", "SOC / Triagem de Phishing / AppSec"),
                  ("Idiomas", "PT (Nativo), EN (Avançado), ES (Intermediário)")],
        "edu_eyebrow": "Educação",
        "edu_title": "Formação acadêmica",
        "edu_degree": "Tecnólogo em Cibersegurança",
        "edu_detail": "Universidade Anhembi Morumbi · 2026–2028 (previsão)",
        "skills_title": "Competências técnicas",
        "skills": ["SOC & Triagem de Alertas", "SIEM & Análise de Logs (Wazuh)", "Análise de Phishing & Headers",
                   "Redes & Análise de Tráfego", "OWASP Top 10 & AppSec", "DevSecOps & CI de Segurança",
                   "Python & Automação", "SQL & PostgreSQL", "Linux, Bash & Git"],
        "proj_eyebrow": "Portfólio",
        "proj_title": "Projetos em destaque",
        "proj_desc": "Ferramentas e aplicações de segurança construídas do zero, cada uma com modelo de ameaças, testes de defesa e documentação em três idiomas. "
                     "Clique num projeto para ver as telas e como ele funciona por dentro.",
        "card_link": "Ver projeto",
        "card_github": "Código no GitHub",
        "contact_eyebrow": "Contato",
        "contact_title": "Vamos conversar?",
        "contact_desc": "Aberto a oportunidades internacionais e remotas em Cibersegurança / Application Security.",
        "contact_email": "E-mail direto",
        "contact_linkedin": "Mensagem no LinkedIn",
        "contact_cv": "Baixar currículo (PDF)",
        "footer": "Portfólio de Cibersegurança",
        # página de projeto
        "back": "Voltar aos projetos",
        "inside_eyebrow": "Por dentro do projeto",
        "inside_title": "Do problema à solução",
        "highlights": "Destaques",
        "tech": "Tecnologias",
        "screens_eyebrow": "Telas",
        "screens_title": "O projeto funcionando",
        "run_title": "Como rodar",
        "next": "Próximo projeto",
        "github_btn": "Ver código no GitHub",
    },
    "es": {
        "title": "Matheus Alfonso | Cybersecurity & Application Security Analyst",
        "description": "Portafolio de Matheus Alfonso: Application Security, prevención de phishing y desarrollo web defensivo.",
        "nav": ["Sobre mí", "Proyectos", "Contacto"],
        "lead": "Analista de Ciberseguridad enfocado en operaciones de SOC, triaje de phishing y seguridad de aplicaciones. "
                "Trabajo con Python, SQL, Linux, SIEM (Wazuh) y OWASP Top 10, uniendo detección de amenazas, prevención y desarrollo seguro.",
        "btn_projects": "Ver proyectos",
        "btn_cv": "Currículum",
        "cv_name": "CV-Matheus-Alfonso-ES.pdf",
        "wa_text": "Hola%20Matheus,%20vi%20tu%20portafolio%20de%20Ciberseguridad%20y%20me%20gustar%C3%ADa%20conversar!",
        "about_eyebrow": "Quién soy",
        "about_title": "Sobre mí",
        "about": [
            "Profesional de Seguridad de la Información con experiencia práctica en la Asamblea Legislativa de Goiás (ALEGO, Brasil), "
            "en la capa preventiva, higiene digital, OPSEC, triaje de correos sospechosos y mitigación de amenazas de Ingeniería Social (Phishing).",
            "Busco una evolución técnica constante uniendo redes, detección y desarrollo defensivo. Uso **Python** para automatización y análisis de "
            "amenazas, **SQL** para consulta y modelado de datos, y estudio análisis de tráfico y de logs en un laboratorio de **SIEM (Wazuh)**. En "
            "equipo, me encargo de la seguridad de una plataforma web: modelo de amenazas STRIDE, revisión de código y pipeline de seguridad en GitHub Actions.",
            "También uso IA en mi día a día de desarrollo, operando **Claude Code** para revisión de seguridad del código, pruebas y documentación, "
            "siempre entendiendo y validando cada cambio.",
        ],
        "facts": [("Ubicación", "Goiânia, Brasil (Remoto / Disponible para reubicación)"),
                  ("Enfoque actual", "SOC / Triaje de Phishing / AppSec"),
                  ("Idiomas", "PT (Nativo), EN (Avanzado), ES (Intermedio)")],
        "edu_eyebrow": "Educación",
        "edu_title": "Formación académica",
        "edu_degree": "Tecnólogo en Ciberseguridad",
        "edu_detail": "Universidad Anhembi Morumbi · 2026–2028 (previsto)",
        "skills_title": "Competencias técnicas",
        "skills": ["SOC & Triaje de Alertas", "SIEM & Análisis de Logs (Wazuh)", "Análisis de Phishing & Headers",
                   "Redes & Análisis de Tráfico", "OWASP Top 10 & AppSec", "DevSecOps & CI de Seguridad",
                   "Python & Automatización", "SQL & PostgreSQL", "Linux, Bash & Git"],
        "proj_eyebrow": "Portafolio",
        "proj_title": "Proyectos destacados",
        "proj_desc": "Herramientas y aplicaciones de seguridad construidas desde cero, cada una con modelo de amenazas, pruebas de defensa y documentación en tres idiomas. "
                     "Haz clic en un proyecto para ver las pantallas y cómo funciona por dentro.",
        "card_link": "Ver proyecto",
        "card_github": "Código en GitHub",
        "contact_eyebrow": "Contacto",
        "contact_title": "¿Conversamos?",
        "contact_desc": "Abierto a oportunidades remotas y de reubicación en Ciberseguridad / Application Security en Latinoamérica.",
        "contact_email": "Correo directo",
        "contact_linkedin": "Mensaje en LinkedIn",
        "contact_cv": "Descargar currículum (PDF)",
        "footer": "Portafolio de Ciberseguridad",
        "back": "Volver a los proyectos",
        "inside_eyebrow": "Por dentro del proyecto",
        "inside_title": "Del problema a la solución",
        "highlights": "Destacados",
        "tech": "Tecnologías",
        "screens_eyebrow": "Pantallas",
        "screens_title": "El proyecto en funcionamiento",
        "run_title": "Cómo ejecutarlo",
        "next": "Siguiente proyecto",
        "github_btn": "Ver código en GitHub",
    },
    "en": {
        "title": "Matheus Alfonso | Cybersecurity & Application Security Analyst",
        "description": "Portfolio of Matheus Alfonso: Application Security, phishing prevention and defensive web development.",
        "nav": ["About", "Projects", "Contact"],
        "lead": "Cybersecurity Analyst focused on SOC operations, phishing triage and application security. "
                "I work with Python, SQL, Linux, SIEM (Wazuh) and OWASP Top 10, bringing together threat detection, prevention and secure development.",
        "btn_projects": "View projects",
        "btn_cv": "Resume",
        "cv_name": "CV-Matheus-Alfonso-EN.pdf",
        "wa_text": "Hi%20Matheus,%20I%20saw%20your%20Cybersecurity%20portfolio%20and%20would%20like%20to%20talk!",
        "about_eyebrow": "Who I am",
        "about_title": "About me",
        "about": [
            "Information Security professional with hands-on experience at the Legislative Assembly of Goiás (ALEGO, Brazil), working on the "
            "preventive layer, digital hygiene, OPSEC, suspicious e-mail triage and mitigation of Social Engineering (Phishing) threats.",
            "I keep growing technically by combining networking, detection and defensive development. I use **Python** for automation and threat "
            "analysis, **SQL** for data queries and modeling, and I study traffic and log analysis in a **SIEM (Wazuh)** lab. On a team project, "
            "I own the security of a web platform: STRIDE threat model, code review and a security pipeline in GitHub Actions.",
            "I also use AI in my daily development work, operating **Claude Code** for security code review, testing and documentation, "
            "always understanding and validating every change.",
        ],
        "facts": [("Location", "Goiânia, Brazil (Remote / Open to relocation)"),
                  ("Current focus", "SOC / Phishing Triage / AppSec"),
                  ("Languages", "PT (Native), EN (Advanced), ES (Intermediate)")],
        "edu_eyebrow": "Education",
        "edu_title": "Academic background",
        "edu_degree": "Technologist Degree in Cybersecurity",
        "edu_detail": "Anhembi Morumbi University · 2026–2028 (expected)",
        "skills_title": "Technical skills",
        "skills": ["SOC & Alert Triage", "SIEM & Log Analysis (Wazuh)", "Phishing & Header Analysis",
                   "Networking & Traffic Analysis", "OWASP Top 10 & AppSec", "DevSecOps & Security CI",
                   "Python & Automation", "SQL & PostgreSQL", "Linux, Bash & Git"],
        "proj_eyebrow": "Portfolio",
        "proj_title": "Featured projects",
        "proj_desc": "Security tools and applications built from scratch, each with a threat model, defense tests and documentation in three languages. "
                     "Click a project to see its screens and how it works inside.",
        "card_link": "View project",
        "card_github": "Code on GitHub",
        "contact_eyebrow": "Contact",
        "contact_title": "Let's talk",
        "contact_desc": "Open to remote and relocation opportunities in Cybersecurity / Application Security across Latin America.",
        "contact_email": "Direct e-mail",
        "contact_linkedin": "Message on LinkedIn",
        "contact_cv": "Download resume (PDF)",
        "footer": "Cybersecurity Portfolio",
        "back": "Back to projects",
        "inside_eyebrow": "Inside the project",
        "inside_title": "From problem to solution",
        "highlights": "Highlights",
        "tech": "Technologies",
        "screens_eyebrow": "Screens",
        "screens_title": "The project in action",
        "run_title": "How to run it",
        "next": "Next project",
        "github_btn": "View code on GitHub",
    },
}

# A ordem desta lista é a ordem no site. O primeiro é o card grande em destaque.
PROJECTS = [
    {
        "slug": "pythreatintel",
        "repo": "pythreatintel",
        "icon": "fa-shield-virus",
        "title": "PyThreatIntel",
        "category": "THREAT INTEL · PYTHON",
        "tech": ["Python", "email.parser", "ipaddress", "requests", "VirusTotal API v3", "JSON"],
        "images": [
            (f"{RAW}/pythreatintel/main/img/samples-phishing.png", 991, 438,
             {"pt": "Análise do e-mail de phishing de exemplo: score 95/100, risco HIGH.",
              "es": "Análisis del correo de phishing de ejemplo: puntaje 95/100, riesgo HIGH.",
              "en": "Analysis of the sample phishing e-mail: score 95/100, HIGH risk."}),
            (f"{RAW}/pythreatintel/main/img/samples-legit.png", 967, 356,
             {"pt": "E-mail legítimo e autenticado: score 0, risco LOW.",
              "es": "Correo legítimo y autenticado: puntaje 0, riesgo LOW.",
              "en": "Legitimate, authenticated e-mail: score 0, LOW risk."}),
            (f"{RAW}/pythreatintel/main/img/samples-phishing-json.png", 1079, 821,
             {"pt": "Relatório completo em JSON (`--json`), pronto para um pipeline de SIEM.",
              "es": "Informe completo en JSON (`--json`), listo para un pipeline de SIEM.",
              "en": "Full JSON report (`--json`), ready for a SIEM pipeline."}),
        ],
        "run": "git clone https://github.com/MattheusAlfonso/pythreatintel.git\ncd pythreatintel\npip install -r requirements.txt\npython3 analyzer.py samples/phishing_sample.eml --json",
        "pt": {
            "card": "Ferramenta de linha de comando para triagem de phishing em arquivos .eml: valida SPF/DKIM/DMARC, rastreia o IP de origem pela cadeia Received, "
                    "detecta spoofing do remetente, extrai IoCs e consulta a reputação do IP no VirusTotal. Saída em JSON para SIEM.",
            "question": "Esse e-mail é phishing? E dá para provar?",
            "intro": "Ferramenta de linha de comando que lê um arquivo .eml e entrega uma avaliação de ameaça: autenticação do remetente, sinais de spoofing, "
                     "IoCs extraídos e reputação do IP de origem no VirusTotal. Feita como projeto de SOC / blue team para triagem de phishing.",
            "blocks": [
                ("Objetivo", "Transformar a sensação de que \"esse e-mail parece estranho\" em evidência concreta e explicável, no formato que um analista de SOC usaria numa triagem."),
                ("Como funciona", "O e-mail é lido com o parser padrão do Python. A cadeia `Received` é percorrida de baixo para cima até o primeiro IP público, "
                                  "que é o servidor mais próximo do remetente. Faixas privadas são descartadas com o módulo `ipaddress`."),
                ("Decisões de segurança", "Só o `Authentication-Results` do topo é confiável, porque é o que o seu servidor adicionou. O domínio real é extraído do endereço, "
                                          "não do nome de exibição, o que derruba o truque `\"support@bank.com\" <attacker@evil.com>`. A chave do VirusTotal vem de variável de ambiente, nunca da linha de comando."),
                ("Limitações conhecidas", "Remetentes de e-mail em massa (Mailchimp, SendGrid) geram falso positivo de Return-Path. Só o IP de origem é consultado no VirusTotal; "
                                          "URLs e hashes ainda não. Suporte a IPv6 está no roadmap."),
            ],
            "highlights": ["Score de risco 0–100", "SPF · DKIM · DMARC", "IoCs: URLs + SHA256", "Saída JSON para SIEM", "Anti-spoofing de nome de exibição"],
        },
        "es": {
            "card": "Herramienta de línea de comandos para triaje de phishing en archivos .eml: valida SPF/DKIM/DMARC, rastrea la IP de origen por la cadena Received, "
                    "detecta suplantación del remitente, extrae IoCs y consulta la reputación de la IP en VirusTotal. Salida en JSON para SIEM.",
            "question": "¿Este correo es phishing? ¿Y se puede probar?",
            "intro": "Herramienta de línea de comandos que lee un archivo .eml y entrega una evaluación de amenaza: autenticación del remitente, señales de spoofing, "
                     "IoCs extraídos y reputación de la IP de origen en VirusTotal. Hecha como proyecto de SOC / blue team para triaje de phishing.",
            "blocks": [
                ("Objetivo", "Convertir la sensación de que \"este correo se ve raro\" en evidencia concreta y explicable, en el formato que usaría un analista de SOC en un triaje."),
                ("Cómo funciona", "El correo se lee con el parser estándar de Python. La cadena `Received` se recorre de abajo hacia arriba hasta la primera IP pública, "
                                  "que es el servidor más cercano al remitente. Los rangos privados se descartan con el módulo `ipaddress`."),
                ("Decisiones de seguridad", "Solo se confía en el `Authentication-Results` superior, porque es el que agregó tu propio servidor. El dominio real se extrae de la dirección, "
                                            "no del nombre visible, lo que neutraliza el truco `\"support@bank.com\" <attacker@evil.com>`. La clave de VirusTotal viene de una variable de entorno, nunca de la línea de comandos."),
                ("Limitaciones conocidas", "Los remitentes de correo masivo (Mailchimp, SendGrid) generan falsos positivos de Return-Path. Solo la IP de origen se consulta en VirusTotal; "
                                           "las URLs y los hashes todavía no. El soporte para IPv6 está en el roadmap."),
            ],
            "highlights": ["Puntaje de riesgo 0–100", "SPF · DKIM · DMARC", "IoCs: URLs + SHA256", "Salida JSON para SIEM", "Anti-spoofing del nombre visible"],
        },
        "en": {
            "card": "Command-line tool for phishing triage of .eml files: validates SPF/DKIM/DMARC, traces the origin IP through the Received chain, "
                    "detects sender spoofing, extracts IoCs and checks IP reputation on VirusTotal. JSON output for SIEM pipelines.",
            "question": "Is this e-mail phishing, and can you prove it?",
            "intro": "A command-line tool that reads an .eml file and returns a threat assessment: sender authentication, spoofing indicators, "
                     "extracted IoCs and the origin IP's reputation on VirusTotal. Built as a SOC / blue-team project for phishing triage.",
            "blocks": [
                ("Goal", "Turn the feeling that \"this e-mail looks weird\" into concrete, explainable evidence, in the format a SOC analyst would use during triage."),
                ("How it works", "The e-mail is read with Python's standard parser. The `Received` chain is walked from bottom to top until the first public IP, "
                                 "which is the server closest to the sender. Private ranges are filtered out with the `ipaddress` module."),
                ("Security decisions", "Only the topmost `Authentication-Results` header is trusted, since your own server added it. The real domain is taken from the address, "
                                       "not the display name, which defeats the `\"support@bank.com\" <attacker@evil.com>` trick. The VirusTotal key comes from an environment variable, never the command line."),
                ("Known limitations", "Bulk-mail senders (Mailchimp, SendGrid) cause Return-Path false positives. Only the origin IP is checked on VirusTotal; "
                                      "URLs and hashes are not yet. IPv6 support is on the roadmap."),
            ],
            "highlights": ["Risk score 0–100", "SPF · DKIM · DMARC", "IoCs: URLs + SHA256", "JSON output for SIEM", "Display-name anti-spoofing"],
        },
    },
    {
        "slug": "secure-auth-system",
        "repo": "secure-auth-system",
        "icon": "fa-lock",
        "title": "Secure Authentication System",
        "category": "APPSEC · PHP",
        "tech": ["PHP 8", "Sessions", "bcrypt", "CSRF tokens", "Content-Security-Policy"],
        "images": [
            (f"{RAW}/secure-auth-system/main/preview.png", 840, 543,
             {"pt": "Painel restrito após o login, com a impressão digital da sessão no lugar do ID real.",
              "es": "Panel restringido tras el login, con la huella de la sesión en lugar del ID real.",
              "en": "Restricted dashboard after login, showing a session fingerprint instead of the real ID."}),
        ],
        "run": "git clone https://github.com/MattheusAlfonso/secure-auth-system.git\ncd secure-auth-system\nphp -S localhost:8000",
        "pt": {
            "card": "Login com hash bcrypt, bloqueio contra força bruta, defesa contra Session Fixation e timing attack, tokens CSRF, cookies endurecidos e controle de acesso centralizado.",
            "question": "Como um login resiste a força bruta, sequestro de sessão e CSRF?",
            "intro": "Fluxo login → painel restrito → logout construído para mostrar os controles por trás de uma autenticação segura: hash de senha, sessão endurecida, "
                     "controle de acesso centralizado, proteção contra força bruta e defesa contra CSRF.",
            "blocks": [
                ("Objetivo", "Demonstrar, num fluxo pequeno e testável, os controles que o OWASP Top 10 cobra em A01 (Broken Access Control) e A07 (Identification & Authentication Failures)."),
                ("Como funciona", "A senha fica guardada só como hash bcrypt (custo 12). Após o login o ID de sessão é regenerado, os cookies saem com `HttpOnly` e `SameSite=Strict`, "
                                  "e a sessão expira após 5 min de inatividade ou 30 min no total."),
                ("Decisões de segurança", "O contador de tentativas fica no servidor, não na sessão: senão bastaria apagar o cookie para tentar de novo. O `password_verify()` roda até para usuário "
                                          "inexistente, para o tempo de resposta não revelar quais usuários existem. O painel mostra só uma impressão digital SHA-256 da sessão, nunca o ID real."),
                ("Testes de defesa", "Abrir `/dashboard.php` sem login redireciona. 5 senhas erradas bloqueiam por 15 minutos, mesmo apagando os cookies. Logout por GET retorna 405 e login sem token CSRF retorna 403."),
            ],
            "highlights": ["bcrypt custo 12", "5 tentativas → 15 min", "Defesa contra Session Fixation", "OWASP A01 · A07", "CSRF em login e logout"],
        },
        "es": {
            "card": "Login con hash bcrypt, bloqueo contra fuerza bruta, defensa contra Session Fixation y timing attacks, tokens CSRF, cookies endurecidas y control de acceso centralizado.",
            "question": "¿Cómo resiste un login a la fuerza bruta, el secuestro de sesión y el CSRF?",
            "intro": "Flujo login → panel restringido → logout construido para mostrar los controles detrás de una autenticación segura: hash de contraseña, sesión endurecida, "
                     "control de acceso centralizado, protección contra fuerza bruta y defensa contra CSRF.",
            "blocks": [
                ("Objetivo", "Demostrar, en un flujo pequeño y verificable, los controles que exige el OWASP Top 10 en A01 (Broken Access Control) y A07 (Identification & Authentication Failures)."),
                ("Cómo funciona", "La contraseña se guarda solo como hash bcrypt (costo 12). Tras el login el ID de sesión se regenera, las cookies salen con `HttpOnly` y `SameSite=Strict`, "
                                  "y la sesión expira tras 5 min de inactividad o 30 min en total."),
                ("Decisiones de seguridad", "El contador de intentos vive en el servidor, no en la sesión: si no, bastaría borrar la cookie para volver a intentar. `password_verify()` se ejecuta incluso "
                                            "para usuarios inexistentes, para que el tiempo de respuesta no revele qué usuarios existen. El panel muestra solo una huella SHA-256 de la sesión, nunca el ID real."),
                ("Pruebas de defensa", "Abrir `/dashboard.php` sin login redirige. 5 contraseñas erróneas bloquean durante 15 minutos, incluso borrando las cookies. Logout por GET devuelve 405 y login sin token CSRF devuelve 403."),
            ],
            "highlights": ["bcrypt costo 12", "5 intentos → 15 min", "Defensa contra Session Fixation", "OWASP A01 · A07", "CSRF en login y logout"],
        },
        "en": {
            "card": "bcrypt-hashed login with brute-force lockout, Session Fixation and timing-attack defenses, CSRF tokens, hardened cookies and centralized access control.",
            "question": "How does a login withstand brute force, session hijacking and CSRF?",
            "intro": "A login → restricted dashboard → logout flow built to show the controls behind secure authentication: password hashing, session hardening, "
                     "centralized access control, brute-force protection and CSRF defense.",
            "blocks": [
                ("Goal", "Show, in a small and testable flow, the controls the OWASP Top 10 asks for in A01 (Broken Access Control) and A07 (Identification & Authentication Failures)."),
                ("How it works", "The password is stored only as a bcrypt hash (cost 12). After login the session ID is regenerated, cookies are set with `HttpOnly` and `SameSite=Strict`, "
                                 "and the session expires after 5 min idle or 30 min in total."),
                ("Security decisions", "The attempt counter lives on the server, not in the session: otherwise dropping the cookie would reset it. `password_verify()` runs even for unknown users, "
                                       "so response time does not reveal which usernames exist. The dashboard shows only a SHA-256 session fingerprint, never the real ID."),
                ("Defense tests", "Opening `/dashboard.php` without logging in redirects. 5 wrong passwords lock you out for 15 minutes, even after deleting cookies. Logout via GET returns 405 and login without a CSRF token returns 403."),
            ],
            "highlights": ["bcrypt cost 12", "5 attempts → 15 min", "Session Fixation defense", "OWASP A01 · A07", "CSRF on login and logout"],
        },
    },
    {
        "slug": "email-header-analyzer",
        "repo": "email-header-analyzer",
        "icon": "fa-envelope-open-text",
        "title": "Email Header & Phishing Analyzer",
        "category": "PHISHING TRIAGE · PHP",
        "tech": ["PHP 8", "Regex", "SPF / DKIM / DMARC", "RFC 5322", "Content-Security-Policy"],
        "images": [
            (f"{RAW}/email-header-analyzer/main/preview.png", 1421, 683,
             {"pt": "Análise de cabeçalhos de um e-mail de phishing, com o score de risco e a explicação de cada ponto.",
              "es": "Análisis de cabeceras de un correo de phishing, con el puntaje de riesgo y la explicación de cada punto.",
              "en": "Header analysis of a phishing e-mail, with the risk score and the reason for every point."}),
        ],
        "run": "git clone https://github.com/MattheusAlfonso/email-header-analyzer.git\ncd email-header-analyzer\nphp -S localhost:8000",
        "pt": {
            "card": "Triagem de e-mails suspeitos: extrai IoCs (IP, From, Return-Path, Reply-To), lê SPF/DKIM/DMARC do cabeçalho confiável e gera um score de risco explicado, detectando táticas de BEC.",
            "question": "O que os cabeçalhos de um e-mail revelam sobre quem realmente o enviou?",
            "intro": "Ferramenta web de triagem: você cola os cabeçalhos brutos de um e-mail suspeito e recebe os indicadores do remetente, os resultados de SPF/DKIM/DMARC, "
                     "a checagem de alinhamento de domínios e um score de risco de 0 a 100 com a explicação de cada ponto.",
            "blocks": [
                ("Objetivo", "Nasceu do meu trabalho com conscientização e prevenção de phishing: dar evidência objetiva para decidir se um e-mail é uma ameaça."),
                ("Como funciona", "Cada indicador soma pontos: DMARC fail (+30), SPF fail (+25), DKIM fail (+25), Reply-To em outro domínio (+20, tática clássica de BEC) "
                                  "e Return-Path divergente (+15). Subdomínios do mesmo domínio contam como alinhados."),
                ("Decisões de parsing", "Os cabeçalhos são buscados no início da linha (`^From:`), para `X-Original-From` não ser confundido com `From`. Cabeçalhos dobrados são desdobrados "
                                        "conforme a RFC 5322. O texto é analisado cru e escapado só na saída."),
                ("Segurança da própria ferramenta", "Ela processa texto controlado pelo atacante, então também é endurecida: toda saída é codificada em HTML, a entrada é limitada a 64 KB "
                                                    "e uma Content-Security-Policy estrita bloqueia qualquer script."),
            ],
            "highlights": ["Score 0–100 explicado", "SPF · DKIM · DMARC", "Detecção de BEC", "RFC 5322", "Entrada limitada a 64 KB"],
        },
        "es": {
            "card": "Triaje de correos sospechosos: extrae IoCs (IP, From, Return-Path, Reply-To), lee SPF/DKIM/DMARC de la cabecera confiable y genera un puntaje de riesgo explicado, detectando tácticas de BEC.",
            "question": "¿Qué revelan las cabeceras de un correo sobre quién lo envió realmente?",
            "intro": "Herramienta web de triaje: pegas las cabeceras en bruto de un correo sospechoso y recibes los indicadores del remitente, los resultados de SPF/DKIM/DMARC, "
                     "la verificación de alineación de dominios y un puntaje de riesgo de 0 a 100 con la explicación de cada punto.",
            "blocks": [
                ("Objetivo", "Nació de mi trabajo en concientización y prevención de phishing: dar evidencia objetiva para decidir si un correo es una amenaza."),
                ("Cómo funciona", "Cada indicador suma puntos: DMARC fail (+30), SPF fail (+25), DKIM fail (+25), Reply-To en otro dominio (+20, táctica clásica de BEC) "
                                  "y Return-Path distinto (+15). Los subdominios del mismo dominio cuentan como alineados."),
                ("Decisiones de parsing", "Las cabeceras se buscan al inicio de la línea (`^From:`), para que `X-Original-From` no se confunda con `From`. Las cabeceras plegadas se despliegan "
                                          "según la RFC 5322. El texto se analiza en bruto y se escapa solo en la salida."),
                ("Seguridad de la propia herramienta", "Procesa texto controlado por el atacante, así que también está endurecida: toda salida se codifica en HTML, la entrada se limita a 64 KB "
                                                       "y una Content-Security-Policy estricta bloquea cualquier script."),
            ],
            "highlights": ["Puntaje 0–100 explicado", "SPF · DKIM · DMARC", "Detección de BEC", "RFC 5322", "Entrada limitada a 64 KB"],
        },
        "en": {
            "card": "Suspicious e-mail triage: extracts IoCs (IP, From, Return-Path, Reply-To), reads SPF/DKIM/DMARC from the trusted header and produces an explainable risk score, flagging BEC tactics.",
            "question": "What do an e-mail's headers reveal about who really sent it?",
            "intro": "A web triage tool: paste the raw headers of a suspicious e-mail and get the sender indicators, SPF/DKIM/DMARC results, "
                     "domain-alignment checks and a 0–100 risk score with the reason for every point.",
            "blocks": [
                ("Goal", "It comes from my work in security awareness and phishing prevention: give objective evidence to decide whether an e-mail is a threat."),
                ("How it works", "Each indicator adds points: DMARC fail (+30), SPF fail (+25), DKIM fail (+25), Reply-To on another domain (+20, a classic BEC tactic) "
                                 "and a mismatched Return-Path (+15). Subdomains of the same domain count as aligned."),
                ("Parsing decisions", "Headers are matched at the start of the line (`^From:`), so `X-Original-From` is not mistaken for `From`. Folded headers are unfolded "
                                      "per RFC 5322. Text is parsed raw and escaped only on output."),
                ("Security of the tool itself", "It processes attacker-controlled text, so it is hardened too: every output is HTML-encoded, input is capped at 64 KB "
                                                "and a strict Content-Security-Policy blocks any script."),
            ],
            "highlights": ["Explainable 0–100 score", "SPF · DKIM · DMARC", "BEC detection", "RFC 5322", "Input capped at 64 KB"],
        },
    },
    {
        "slug": "input-validation-security",
        "repo": "01-input-validation-security",
        "icon": "fa-shield-halved",
        "title": "Input Validation & XSS Mitigation",
        "category": "APPSEC · PHP",
        "tech": ["PHP 8", "Allowlist validation", "Output encoding", "CSRF tokens", "Content-Security-Policy"],
        "images": [
            (f"{RAW}/01-input-validation-security/main/preview.png", 533, 374,
             {"pt": "Relatório de validação: o payload de XSS é rejeitado e aparece como texto inerte.",
              "es": "Informe de validación: el payload de XSS se rechaza y aparece como texto inerte.",
              "en": "Validation report: the XSS payload is rejected and shown as inert text."}),
        ],
        "run": "git clone https://github.com/MattheusAlfonso/01-input-validation-security.git\ncd 01-input-validation-security\nphp -S localhost:8000",
        "pt": {
            "card": "Validação com allowlist na entrada e codificação na saída para neutralizar XSS. Bloqueia URLs `javascript:` e usa token CSRF e Content-Security-Policy restritiva.",
            "question": "Por que escapar a entrada não basta para impedir XSS?",
            "intro": "Pequena aplicação web que mostra os dois hábitos que barram a maior parte das falhas de injeção: validar a entrada contra uma allowlist "
                     "e codificar a saída para o contexto em que ela é exibida.",
            "blocks": [
                ("Objetivo", "Simular um formulário de analista onde usuário, e-mail e uma URL suspeita são enviados para inspeção, e mostrar como cada campo é defendido."),
                ("Decisão principal", "A primeira versão escapava os dados assim que chegavam. Funcionava numa página, mas o valor guardado virava HTML: quebrava em URL, JSON ou SQL "
                                      "e era escapado duas vezes. A versão atual guarda o valor original, rejeita o que não bate com a allowlist e escapa só na hora de renderizar."),
                ("Camadas de defesa", "Allowlist com regex e `FILTER_VALIDATE_EMAIL`, URLs aceitas só com esquema http/https (`javascript:` e `data:` são barradas), token CSRF "
                                      "comparado com `hash_equals()` e uma CSP sem scripts inline como segunda camada."),
                ("O que aprendi", "Escapar não é validar: `htmlspecialchars()` deixa o dado seguro para HTML, não seguro em geral. Allowlists são mais fortes que blocklists. "
                                  "E a CSP segura o ataque mesmo se um bug de codificação passar."),
            ],
            "highlights": ["OWASP A03 · Injection", "Allowlist", "Output encoding", "Token CSRF", "CSP sem inline"],
        },
        "es": {
            "card": "Validación con allowlist en la entrada y codificación en la salida para neutralizar XSS. Bloquea URLs `javascript:` y usa token CSRF y una Content-Security-Policy estricta.",
            "question": "¿Por qué escapar la entrada no basta para impedir XSS?",
            "intro": "Pequeña aplicación web que muestra los dos hábitos que frenan la mayoría de las fallas de inyección: validar la entrada contra una allowlist "
                     "y codificar la salida según el contexto en que se muestra.",
            "blocks": [
                ("Objetivo", "Simular un formulario de analista donde se envían un usuario, un correo y una URL sospechosa para inspección, y mostrar cómo se defiende cada campo."),
                ("Decisión principal", "La primera versión escapaba los datos apenas llegaban. Funcionaba en una página, pero el valor guardado se volvía HTML: fallaba en URL, JSON o SQL "
                                       "y se escapaba dos veces. La versión actual guarda el valor original, rechaza lo que no coincide con la allowlist y escapa solo al renderizar."),
                ("Capas de defensa", "Allowlist con regex y `FILTER_VALIDATE_EMAIL`, URLs aceptadas solo con esquema http/https (`javascript:` y `data:` se bloquean), token CSRF "
                                     "comparado con `hash_equals()` y una CSP sin scripts inline como segunda capa."),
                ("Lo que aprendí", "Escapar no es validar: `htmlspecialchars()` hace que el dato sea seguro para HTML, no seguro en general. Las allowlists son más fuertes que las blocklists. "
                                   "Y la CSP frena el ataque incluso si se escapa un error de codificación."),
            ],
            "highlights": ["OWASP A03 · Injection", "Allowlist", "Output encoding", "Token CSRF", "CSP sin inline"],
        },
        "en": {
            "card": "Allowlist input validation and context-aware output encoding to neutralize XSS. Blocks `javascript:` URLs and enforces CSRF tokens and a strict Content-Security-Policy.",
            "question": "Why isn't escaping input enough to stop XSS?",
            "intro": "A small web app that shows the two habits that stop most injection bugs: validate input against an allowlist "
                     "and encode output for the context where it is displayed.",
            "blocks": [
                ("Goal", "Simulate an analyst form where a username, an e-mail and a suspicious URL are submitted for inspection, and show how each field is defended."),
                ("Key decision", "The first version escaped data as soon as it arrived. It worked on one page, but the stored value became HTML: it broke in URLs, JSON or SQL "
                                 "and got double-escaped. The current version keeps the original value, rejects what fails the allowlist and escapes only when rendering."),
                ("Defense layers", "Allowlist with regex and `FILTER_VALIDATE_EMAIL`, URLs accepted only with an http/https scheme (`javascript:` and `data:` are blocked), a CSRF token "
                                   "checked with `hash_equals()` and a CSP with no inline scripts as a second layer."),
                ("What I learned", "Escaping is not validation: `htmlspecialchars()` makes data safe for HTML, not safe in general. Allowlists beat blocklists. "
                                   "And CSP stops the attack even if an encoding bug slips through."),
            ],
            "highlights": ["OWASP A03 · Injection", "Allowlist", "Output encoding", "CSRF token", "No-inline CSP"],
        },
    },
]

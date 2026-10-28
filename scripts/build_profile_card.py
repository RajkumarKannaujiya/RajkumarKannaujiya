from __future__ import annotations

import html
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen


USERNAME = "RajkumarKannaujiya"
API_ROOT = "https://api.github.com"
ROOT = Path(__file__).resolve().parents[1]

THEMES = {
    "dark": {
        "background": "#0d1117",
        "panel": "#111923",
        "chip": "#151f2b",
        "border": "#293746",
        "text": "#e6edf3",
        "muted": "#8192a5",
        "key": "#ffb86b",
        "value": "#b8d8ff",
        "cyan": "#52e0cf",
        "blue": "#8b9cff",
        "green": "#4ade80",
        "leader": "#526273",
    },
    "light": {
        "background": "#f6f8fa",
        "panel": "#ffffff",
        "chip": "#eef3f8",
        "border": "#c8d1dc",
        "text": "#1f2328",
        "muted": "#657386",
        "key": "#9a4600",
        "value": "#174a7e",
        "cyan": "#087f8c",
        "blue": "#5b4bc4",
        "green": "#16823f",
        "leader": "#9aa8b7",
    },
}


def get_json(url: str):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "RajkumarKannaujiya-profile-card",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(url, headers=headers)
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def fetch_stats() -> dict[str, int | str]:
    profile = get_json(f"{API_ROOT}/users/{USERNAME}")
    owned_repos = []
    page = 1
    while True:
        repos = get_json(
            f"{API_ROOT}/users/{USERNAME}/repos?type=owner&per_page=100&page={page}"
        )
        owned_repos.extend(repos)
        if len(repos) < 100:
            break
        page += 1

    original_repos = [repo for repo in owned_repos if not repo.get("fork", False)]
    return {
        "repos": int(profile.get("public_repos", 0)),
        "stars": sum(int(repo.get("stargazers_count", 0)) for repo in original_repos),
        "followers": int(profile.get("followers", 0)),
    }


def row(y: int, label: str, value: str) -> str:
    safe_label = html.escape(label)
    safe_value = html.escape(value)
    return (
        f'<text x="382" y="{y}" class="row">'
        f'<tspan class="muted">. </tspan>'
        f'<tspan class="key">{safe_label}</tspan>'
        f'<tspan x="522" class="leader">············</tspan>'
        f'<tspan x="548" class="value">{safe_value}</tspan>'
        "</text>"
    )


def card(theme_name: str, stats: dict[str, int | str]) -> str:
    colors = THEMES[theme_name]
    css = "\n".join(f"--{key}:{value};" for key, value in colors.items())
    rows = "\n".join(
        [
            row(137, "Name", "Rajkumar Kannaujiya"),
            row(160, "Role", "Applied AI · Data Science"),
            row(183, "Education", "IIT Madras · B.S. Data Science & Applications"),
            row(249, "Machine learning", "Python · PyTorch · TensorFlow · scikit-learn"),
            row(272, "Generative AI", "LLMs · NLP · RAG · transformers"),
            row(295, "Data science", "SQL · Pandas · NumPy · statistics"),
            row(318, "AI delivery", "FastAPI · Docker · Git · Linux"),
            row(379, "LinkedIn", "linkedin.com/in/rajkumarkannaujiya"),
            row(402, "Email", "rajkumar.kannojiaa@gmail.com"),
        ]
    )
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="520" viewBox="0 0 1120 520" role="img" aria-labelledby="title description">
  <title id="title">Rajkumar Kannaujiya — IIT Madras and Applied AI</title>
  <desc id="description">A theme-aware terminal profile card with an animated neural network illustration, IIT Madras education, AI skills, contact links, and refreshed GitHub statistics.</desc>
  <style>
    :root {{{css}}}
    .bg {{ fill: var(--background); }}
    .panel {{ fill: var(--panel); stroke: var(--border); }}
    .chip {{ fill: var(--chip); stroke: var(--cyan); }}
    .text {{ fill: var(--text); }}
    .muted {{ fill: var(--muted); }}
    .key {{ fill: var(--key); }}
    .value {{ fill: var(--value); }}
    .cyan {{ fill: var(--cyan); }}
    .blue {{ fill: var(--blue); }}
    .green {{ fill: var(--green); }}
    .leader {{ fill: var(--leader); }}
    .line {{ stroke: var(--border); }}
    .network {{ stroke: var(--cyan); }}
    text {{ font-family: Consolas, 'Courier New', monospace; }}
    .header {{ font-size: 14px; letter-spacing: .4px; }}
    .section {{ font-size: 14px; font-weight: 700; }}
    .row {{ font-size: 14px; }}
    .small {{ font-size: 11px; letter-spacing: .5px; }}
    .tiny {{ font-size: 10px; letter-spacing: .5px; }}
    .pulse {{ animation: pulse 1.8s ease-in-out infinite; }}
    .cursor {{ animation: blink 1.1s steps(2, start) infinite; }}
    @keyframes pulse {{ 0%, 100% {{ opacity: .45; }} 50% {{ opacity: 1; }} }}
    @keyframes blink {{ to {{ opacity: 0; }} }}
  </style>

  <rect class="bg" x="1" y="1" width="1118" height="518" rx="16" />
  <rect x="1" y="1" width="1118" height="518" rx="16" fill="none" stroke="var(--border)" />
  <circle cx="25" cy="27" r="5" fill="#ff5f57" />
  <circle cx="43" cy="27" r="5" fill="#febc2e" />
  <circle cx="61" cy="27" r="5" fill="#28c840" />
  <text x="83" y="32" class="header text">RAJKUMAR / AI PROFILE</text>
  <circle cx="872" cy="27" r="4" class="green pulse" />
  <text x="885" y="32" class="small cyan">IIT MADRAS · APPLIED AI</text>
  <line x1="20" y1="51" x2="1100" y2="51" class="line" />

  <rect x="20" y="69" width="328" height="430" rx="14" class="panel" />
  <text x="43" y="99" class="small muted">NEURAL SYSTEM / 01</text>
  <circle cx="318" cy="95" r="4" class="green pulse" />
  <circle cx="184" cy="270" r="127" fill="none" class="network" opacity=".18" />
  <circle cx="184" cy="270" r="103" fill="none" class="network" opacity=".28" stroke-dasharray="3 8" />
  <g fill="none" stroke-width="1.5" class="network" opacity=".72">
    <path d="M184 145 L184 194 M100 174 L139 216 M268 174 L229 216 M82 267 L133 267 M286 267 L235 267 M111 356 L145 316 M257 356 L223 316 M184 397 L184 316" />
    <path d="M100 174 L82 267 L111 356 M268 174 L286 267 L257 356 M100 174 L184 145 L268 174" opacity=".5" />
    <path d="M111 356 L184 397 L257 356" opacity=".5" />
  </g>
  <g class="pulse">
    <circle cx="184" cy="145" r="5" class="blue" />
    <circle cx="100" cy="174" r="5" class="green" />
    <circle cx="268" cy="174" r="5" class="blue" />
    <circle cx="82" cy="267" r="5" class="cyan" />
    <circle cx="286" cy="267" r="5" class="cyan" />
    <circle cx="111" cy="356" r="5" class="blue" />
    <circle cx="257" cy="356" r="5" class="green" />
    <circle cx="184" cy="397" r="5" class="blue" />
  </g>
  <rect x="122" y="219" width="124" height="96" rx="14" class="chip" stroke-width="1.5" />
  <text x="184" y="265" text-anchor="middle" class="cyan" font-size="36" font-weight="700">AI</text>
  <text x="184" y="289" text-anchor="middle" class="small text">SYSTEMS</text>
  <text x="184" y="445" text-anchor="middle" class="small text">DATA <tspan class="cyan">→</tspan> MODEL <tspan class="cyan">→</tspan> IMPACT</text>
  <text x="184" y="469" text-anchor="middle" class="tiny muted">LEARN <tspan class="cyan">/</tspan> EXPERIMENT <tspan class="cyan">/</tspan> BUILD</text>

  <text x="382" y="83" class="header text">rajkumar@iit-madras</text><rect x="567" y="69" width="8" height="16" rx="1" class="cyan cursor" />
  <line x1="382" y1="98" x2="1095" y2="98" class="line" />

  <text x="382" y="120" class="section text">- Profile</text>
  {rows.splitlines()[0]}
  {rows.splitlines()[1]}
  {rows.splitlines()[2]}

  <text x="382" y="229" class="section text">- AI Skillset</text>
  {rows.splitlines()[3]}
  {rows.splitlines()[4]}
  {rows.splitlines()[5]}
  {rows.splitlines()[6]}

  <text x="382" y="359" class="section text">- Connect</text>
  {rows.splitlines()[7]}
  {rows.splitlines()[8]}

  <text x="382" y="438" class="section text">- GitHub Stats</text>
  <text x="382" y="465" class="row">
    <tspan class="muted">. </tspan><tspan class="key">Repositories</tspan><tspan class="muted">: </tspan><tspan id="stat_repos" class="value">{stats['repos']}</tspan>
    <tspan class="muted">  |  </tspan><tspan class="key">Stars</tspan><tspan class="muted">: </tspan><tspan id="stat_stars" class="value">{stats['stars']}</tspan>
    <tspan class="muted">  |  </tspan><tspan class="key">Followers</tspan><tspan class="muted">: </tspan><tspan id="stat_followers" class="value">{stats['followers']}</tspan>
  </text>
  <text x="382" y="488" class="tiny muted">Public GitHub stats · refreshed daily</text>
  <text x="1095" y="488" text-anchor="end" class="tiny muted">REFRESHES DAILY</text>
  <line x1="382" y1="501" x2="1095" y2="501" class="line" opacity=".6" />
  <text x="382" y="516" class="tiny muted">B.S. DATA SCIENCE &amp; APPLICATIONS <tspan class="cyan">·</tspan> IIT MADRAS</text>
</svg>
'''


def main() -> None:
    stats = fetch_stats()
    for theme in THEMES:
        target = ROOT / f"{theme}_mode.svg"
        target.write_text(card(theme, stats), encoding="utf-8")
    print(
        f"Updated profile card: {stats['repos']} public repositories, "
        f"{stats['stars']} stars, {stats['followers']} followers."
    )


if __name__ == "__main__":
    main()

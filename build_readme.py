#!/usr/bin/env python3
"""
Build script for ANAND-JATOTHU GitHub Profile README
Generates all SVG assets with inlined base64 images.
"""

import os
import zipfile

REPO = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(REPO, "assets")

import base64
from PIL import Image
from io import BytesIO

def to_b64(path, max_size, quality=80):
    try:
        img = Image.open(path)
        img.thumbnail(max_size)
        buffer = BytesIO()
        img.save(buffer, format="JPEG" if path.endswith(".jpg") else "PNG", optimize=True, quality=quality)
        return base64.b64encode(buffer.getvalue()).decode("utf-8")
    except Exception as e:
        print(f"Failed to process {path}: {e}")
        # Return a 1x1 transparent png
        return "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="

ID_B64 = to_b64(os.path.join(ASSETS, "id.png"), (400, 400))
RP_B64 = to_b64(os.path.join(ASSETS, "right_pointing.png"), (400, 400))
BG_B64 = to_b64(os.path.join(ASSETS, "bg.jpg"), (800, 800))

ID_URI  = f"data:image/png;base64,{ID_B64}"
RP_URI  = f"data:image/png;base64,{RP_B64}"
BG_URI  = f"data:image/jpeg;base64,{BG_B64}"

# ── Color palette ────────────────────────────────────────────────────────────
NAVY    = "#070b16"
BLUE    = "#247bff"
CRIMSON = "#ff354f"
OFF_W   = "#e8edf5"
DIM     = "#8892a4"
CARD    = "#0d1425"
BORDER  = "#1a2540"

# Common styles to make animated elements visible in local previews
COMMON_CSS = """
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&amp;family=JetBrains+Mono:wght@400;700&amp;display=swap');
      * { font-family: 'Inter', system-ui, sans-serif; }
      @media (prefers-reduced-motion: reduce) { * { animation: none !important; } }
      /* Fallback for previews */
      svg g[opacity="0"], svg text[opacity="0"], svg image[opacity="0"] { opacity: 1 !important; }
"""

# Common background elements
def bg_elements(width, height):
    return f"""
  <rect width="{width}" height="{height}" fill="{NAVY}" rx="16"/>
  <image href="{BG_URI}" x="0" y="0" width="{width}" height="{height}" preserveAspectRatio="xMidYMid slice" opacity="0.35" style="mix-blend-mode: lighten;"/>
  <rect width="{width}" height="{height}" fill="url(#dots)" rx="16"/>
  <rect width="{width}" height="{height}" fill="url(#g1)" rx="16"/>
  <rect x="1" y="1" width="{width-2}" height="{height-2}" rx="15" fill="none" stroke="url(#border)" stroke-width="1.5" opacity="0.6"/>
"""

# ════════════════════════════════════════════════════════════════════════════
# 1. hero.svg
# ════════════════════════════════════════════════════════════════════════════
HERO_SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 320" width="860" height="320">
  <defs>
    <style>{COMMON_CSS}</style>
    <linearGradient id="g1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{BLUE}" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="{CRIMSON}" stop-opacity="0.08"/>
    </linearGradient>
    <linearGradient id="border" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{BLUE}"/>
      <stop offset="100%" stop-color="{CRIMSON}"/>
    </linearGradient>
    <clipPath id="hportrait">
      <circle cx="762" cy="160" r="118"/>
    </clipPath>
    <pattern id="dots" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="{BLUE}" fill-opacity="0.08"/>
    </pattern>
  </defs>

  {bg_elements(860, 320)}

  <!-- blue accent bar left -->
  <rect x="36" y="60" width="3" height="200" fill="{BLUE}" rx="2" opacity="0.7">
    <animate attributeName="opacity" values="0;0.7" dur="0.6s" begin="0s" fill="both"/>
  </rect>

  <!-- greeting -->
  <text x="54" y="92" font-size="13" fill="{BLUE}" font-family="'JetBrains Mono', monospace" letter-spacing="3" opacity="0">
    &gt; Hello, World! 👋
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="0.3s" fill="both"/>
  </text>

  <!-- name reveal -->
  <text x="54" y="158" font-size="52" font-weight="900" fill="{OFF_W}" letter-spacing="-1" opacity="0">
    ANAND JATOTHU
    <animate attributeName="opacity" values="0;1" dur="0.7s" begin="0.6s" fill="both"/>
    <animate attributeName="y" values="178;158" dur="0.7s" begin="0.6s" fill="both"/>
  </text>
  <rect x="54" y="165" width="0" height="3" fill="{BLUE}" rx="1.5">
    <animate attributeName="width" values="0;460" dur="0.8s" begin="1.1s" fill="both"/>
  </rect>

  <!-- cycling roles -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;1;1;0" dur="10s" begin="1.4s" fill="both" repeatCount="indefinite" keyTimes="0;0.05;0.2;0.25"/>
    <text x="54" y="196" font-size="17" fill="{BLUE}" font-family="'JetBrains Mono', monospace">Full-Stack Web Developer</text>
  </g>
  <g opacity="0">
    <animate attributeName="opacity" values="0;0;0;1;1;0" dur="10s" begin="1.4s" fill="both" repeatCount="indefinite" keyTimes="0;0.24;0.25;0.3;0.45;0.5"/>
    <text x="54" y="196" font-size="17" fill="{CRIMSON}" font-family="'JetBrains Mono', monospace">AI / ML Engineer</text>
  </g>
  <g opacity="0">
    <animate attributeName="opacity" values="0;0;0;0;0;1;1;0" dur="10s" begin="1.4s" fill="both" repeatCount="indefinite" keyTimes="0;0.49;0.5;0.5;0.51;0.55;0.7;0.75"/>
    <text x="54" y="196" font-size="17" fill="#a78bfa" font-family="'JetBrains Mono', monospace">Open Source Contributor</text>
  </g>
  <g opacity="0">
    <animate attributeName="opacity" values="0;0;0;0;0;0;0;1;1;0" dur="10s" begin="1.4s" fill="both" repeatCount="indefinite" keyTimes="0;0.74;0.75;0.75;0.76;0.76;0.77;0.8;0.95;1"/>
    <text x="54" y="196" font-size="17" fill="#34d399" font-family="'JetBrains Mono', monospace">Problem Solver &amp; Builder</text>
  </g>

  <!-- one-line pitch -->
  <text x="54" y="228" font-size="13.5" fill="{DIM}" opacity="0" font-weight="400">
    Building secure, scalable, AI-powered software that matters.
    <animate attributeName="opacity" values="0;0.85" dur="0.6s" begin="1.8s" fill="both"/>
  </text>

  <!-- location / college row -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.6s" begin="2.1s" fill="both"/>
    <text x="54" y="265" font-size="13" fill="{DIM}">📍 Hyderabad, India</text>
    <text x="210" y="265" font-size="13" fill="{DIM}">🎓 B.Tech IT @ TKREC</text>
    <text x="390" y="265" font-size="13" fill="{DIM}">🔭 Open to Internships</text>
  </g>

  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="2.4s" fill="both"/>
    <rect x="54" y="278" width="165" height="26" rx="13" fill="{BLUE}" fill-opacity="0.15" stroke="{BLUE}" stroke-width="1"/>
    <text x="137" y="295" font-size="12" fill="{BLUE}" text-anchor="middle" font-weight="700">🌐 anandjatothu.me</text>
  </g>

  <circle cx="762" cy="160" r="122" fill="none" stroke="{BLUE}" stroke-width="1.5" opacity="0.4">
    <animate attributeName="stroke-opacity" values="0.4;0.8;0.4" dur="3s" repeatCount="indefinite"/>
  </circle>
  <circle cx="762" cy="160" r="119" fill="{CARD}"/>
  <image href="{ID_URI}" x="644" y="42" width="236" height="236" clip-path="url(#hportrait)" preserveAspectRatio="xMidYMid slice" opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.8s" begin="0.8s" fill="both"/>
  </image>
  <circle cx="762" cy="160" r="122" fill="none" stroke="{CRIMSON}" stroke-width="1" stroke-dasharray="60 300" opacity="0.5">
    <animateTransform attributeName="transform" type="rotate" from="0 762 160" to="360 762 160" dur="12s" repeatCount="indefinite"/>
  </circle>
</svg>"""

# ════════════════════════════════════════════════════════════════════════════
# 2. about-life.svg
# ════════════════════════════════════════════════════════════════════════════
ABOUT_SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 300" width="860" height="300">
  <defs>
    <style>{COMMON_CSS}</style>
    <linearGradient id="g1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{BLUE}" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="{CRIMSON}" stop-opacity="0.06"/>
    </linearGradient>
    <linearGradient id="border" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{BLUE}"/>
      <stop offset="100%" stop-color="{CRIMSON}"/>
    </linearGradient>
    <pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="{BLUE}" fill-opacity="0.07"/>
    </pattern>
    <linearGradient id="barBlue" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{BLUE}"/>
      <stop offset="100%" stop-color="#60a5fa"/>
    </linearGradient>
    <linearGradient id="barRed" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{CRIMSON}"/>
      <stop offset="100%" stop-color="#f97316"/>
    </linearGradient>
    <linearGradient id="barPurple" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#a78bfa"/>
    </linearGradient>
    <linearGradient id="barGreen" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#34d399"/>
    </linearGradient>
  </defs>

  {bg_elements(860, 300)}

  <text x="36" y="46" font-size="11" font-family="'JetBrains Mono',monospace" fill="{BLUE}" letter-spacing="3">ABOUT ME</text>
  <rect x="36" y="52" width="60" height="2" fill="{BLUE}" rx="1"/>

  <text x="36" y="84" font-size="19" font-weight="700" fill="{OFF_W}">Capabilities</text>

  <text x="36" y="110" font-size="11.5" fill="{DIM}">Full-Stack Development</text>
  <rect x="36" y="114" width="320" height="7" rx="3.5" fill="{CARD}"/>
  <rect x="36" y="114" width="0" height="7" rx="3.5" fill="url(#barBlue)">
    <animate attributeName="width" values="0;294" dur="1s" begin="0.3s" fill="both"/>
  </rect>
  <text x="362" y="121" font-size="10" fill="{BLUE}" text-anchor="end">92%</text>

  <text x="36" y="140" font-size="11.5" fill="{DIM}">AI / ML Integration</text>
  <rect x="36" y="144" width="320" height="7" rx="3.5" fill="{CARD}"/>
  <rect x="36" y="144" width="0" height="7" rx="3.5" fill="url(#barRed)">
    <animate attributeName="width" values="0;256" dur="1s" begin="0.5s" fill="both"/>
  </rect>
  <text x="362" y="151" font-size="10" fill="{CRIMSON}" text-anchor="end">80%</text>

  <text x="36" y="170" font-size="11.5" fill="{DIM}">Cloud &amp; Backend Systems</text>
  <rect x="36" y="174" width="320" height="7" rx="3.5" fill="{CARD}"/>
  <rect x="36" y="174" width="0" height="7" rx="3.5" fill="url(#barPurple)">
    <animate attributeName="width" values="0;272" dur="1s" begin="0.7s" fill="both"/>
  </rect>
  <text x="362" y="181" font-size="10" fill="#a78bfa" text-anchor="end">85%</text>

  <text x="36" y="200" font-size="11.5" fill="{DIM}">Problem Solving &amp; DSA</text>
  <rect x="36" y="204" width="320" height="7" rx="3.5" fill="{CARD}"/>
  <rect x="36" y="204" width="0" height="7" rx="3.5" fill="url(#barGreen)">
    <animate attributeName="width" values="0;281" dur="1s" begin="0.9s" fill="both"/>
  </rect>
  <text x="362" y="211" font-size="10" fill="#34d399" text-anchor="end">88%</text>

  <text x="36" y="230" font-size="11.5" fill="{DIM}">UI/UX Design</text>
  <rect x="36" y="234" width="320" height="7" rx="3.5" fill="{CARD}"/>
  <rect x="36" y="234" width="0" height="7" rx="3.5" fill="url(#barBlue)">
    <animate attributeName="width" values="0;240" dur="1s" begin="1.1s" fill="both"/>
  </rect>
  <text x="362" y="241" font-size="10" fill="{BLUE}" text-anchor="end">75%</text>

  <line x1="420" y1="30" x2="420" y2="275" stroke="{BORDER}" stroke-width="1"/>

  <!-- Slide 1: Learning -->
  <g opacity="1">
    <animate attributeName="opacity" values="1;1;0;0;0;0;0;0;1" dur="12s" begin="0s" fill="both" repeatCount="indefinite" keyTimes="0;0.28;0.33;0.33;0.66;0.66;0.99;1;1"/>
    <text x="450" y="84" font-size="19" font-weight="700" fill="{OFF_W}">Currently Learning 📚</text>
    <text x="450" y="114" font-size="13" fill="{DIM}">▸ Advanced Data Structures &amp; Algorithms</text>
    <text x="450" y="136" font-size="13" fill="{DIM}">▸ Deep Learning &amp; Neural Networks</text>
    <text x="450" y="158" font-size="13" fill="{DIM}">▸ System Design Patterns</text>
    <text x="450" y="180" font-size="13" fill="{DIM}">▸ AWS Solution Architect concepts</text>
    <text x="450" y="210" font-size="11" fill="{BLUE}" opacity="0.7">📅 Updated Oct 2026</text>
  </g>
  <!-- Slide 2: Interests -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;0;1;1;0;0;0;0;0" dur="12s" begin="0s" fill="both" repeatCount="indefinite" keyTimes="0;0.32;0.33;0.61;0.66;0.66;0.99;1;1"/>
    <text x="450" y="84" font-size="19" font-weight="700" fill="{OFF_W}">Interests 🎯</text>
    <text x="450" y="114" font-size="13" fill="{DIM}">▸ Problem Solving (LeetCode, CP)</text>
    <text x="450" y="136" font-size="13" fill="{DIM}">▸ Open-Source Development</text>
    <text x="450" y="158" font-size="13" fill="{DIM}">▸ Tech Community Building</text>
    <text x="450" y="180" font-size="13" fill="{DIM}">▸ UI/UX Minimalist Design</text>
    <text x="450" y="210" font-size="11" fill="{CRIMSON}" opacity="0.7">✨ Always exploring!</text>
  </g>
  <!-- Slide 3: Goals -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;0;0;0;0;1;1;0;0" dur="12s" begin="0s" fill="both" repeatCount="indefinite" keyTimes="0;0.32;0.33;0.61;0.65;0.66;0.94;0.99;1"/>
    <text x="450" y="84" font-size="19" font-weight="700" fill="{OFF_W}">2026 Goals 🚀</text>
    <text x="450" y="114" font-size="13" fill="{DIM}">▸ Land a software engineering internship</text>
    <text x="450" y="136" font-size="13" fill="{DIM}">▸ Ship StuLink v2.0</text>
    <text x="450" y="158" font-size="13" fill="{DIM}">▸ Contribute to 5+ OSS projects</text>
    <text x="450" y="180" font-size="13" fill="{DIM}">▸ Earn AWS Developer Associate cert</text>
    <text x="450" y="210" font-size="11" fill="#34d399" opacity="0.7">🚀 Making it happen!</text>
  </g>

  <rect x="450" y="258" width="370" height="4" rx="2" fill="{CARD}"/>
  <rect x="450" y="258" width="0" height="4" rx="2" fill="{BLUE}">
    <animate attributeName="width" values="0;120;120;0;0;0;0;0;0" dur="12s" begin="0s" fill="both" repeatCount="indefinite" keyTimes="0;0.28;0.33;0.33;0.66;0.66;0.99;1;1"/>
  </rect>
  <rect x="574" y="258" width="0" height="4" rx="2" fill="{CRIMSON}">
    <animate attributeName="width" values="0;0;0;120;120;0;0;0;0" dur="12s" begin="0s" fill="both" repeatCount="indefinite" keyTimes="0;0.32;0.33;0.61;0.66;0.66;0.99;1;1"/>
  </rect>
  <rect x="698" y="258" width="0" height="4" rx="2" fill="#a78bfa">
    <animate attributeName="width" values="0;0;0;0;0;120;120;0;0" dur="12s" begin="0s" fill="both" repeatCount="indefinite" keyTimes="0;0.32;0.65;0.66;0.65;0.66;0.94;0.99;1"/>
  </rect>

  <circle cx="562" cy="272" r="4" fill="{BLUE}">
    <animate attributeName="opacity" values="1;1;0.3;0.3;0.3;0.3;0.3;0.3;1" dur="12s" begin="0s" fill="both" repeatCount="indefinite" keyTimes="0;0.28;0.33;0.33;0.66;0.66;0.99;1;1"/>
  </circle>
  <circle cx="578" cy="272" r="4" fill="{CRIMSON}" opacity="0.3">
    <animate attributeName="opacity" values="0.3;0.3;1;1;0.3;0.3;0.3;0.3;0.3" dur="12s" begin="0s" fill="both" repeatCount="indefinite" keyTimes="0;0.32;0.33;0.61;0.66;0.66;0.99;1;1"/>
  </circle>
  <circle cx="594" cy="272" r="4" fill="#a78bfa" opacity="0.3">
    <animate attributeName="opacity" values="0.3;0.3;0.3;0.3;0.3;1;1;0.3;0.3" dur="12s" begin="0s" fill="both" repeatCount="indefinite" keyTimes="0;0.32;0.65;0.66;0.65;0.66;0.94;0.99;1"/>
  </circle>
</svg>"""

# ════════════════════════════════════════════════════════════════════════════
# 3. stack.svg  
# ════════════════════════════════════════════════════════════════════════════

def chip(x, y, label, color):
    w = len(label)*7 + 20
    return f"""<g>
    <rect x="{x}" y="{y}" width="{w}" height="22" rx="11" fill="{color}" fill-opacity="0.25" stroke="{color}" stroke-width="1" stroke-opacity="0.8"/>
    <text x="{x+w//2}" y="{y+15}" font-size="11" fill="{OFF_W}" text-anchor="middle" font-weight="600" style="text-shadow: 0 1px 2px rgba(0,0,0,0.8)">{label}</text>
  </g>"""

chips_lang = [
    ("Python",  BLUE),    ("TypeScript", "#60a5fa"), ("JavaScript", "#f7df1e"),
    ("Java",    "#ed8b00"),("Dart",   "#0175c2"),    ("Kotlin",  "#7f52ff"),
    ("Ruby",    "#cc342d"),("C/C++",  "#00599c"),
]
chips_web = [
    ("Next.js",  "#ffffff"), ("React",  "#61dafb"), ("Django", "#092e20"),
    ("Node.js",  "#6da55f"),("FastAPI","#005571"),("Express","#ffffff"),
    ("HTML/CSS", "#e34f26"),
]
chips_cloud = [
    ("AWS",      "#ff9900"),("GCP",      "#4285f4"),("Supabase","#3ecf8e"),
    ("Firebase", "#ffcd34"),("MongoDB",  "#4ea94b"),("PostgreSQL","#316192"),
    ("Docker",   "#0db7ed"),("SQLite",   "#003b57"),
]

def row_chips(chips, start_x, start_y, max_w=780):
    svg = ""
    x, y = start_x, start_y
    for label, color in chips:
        w = len(label)*7 + 20
        if x + w > max_w:
            x = start_x
            y += 30
        svg += chip(x, y, label, color)
        x += w + 8
    return svg, y + 30

lang_chips_svg, y1 = row_chips(chips_lang, 36, 90)
web_chips_svg, y2   = row_chips(chips_web,  36, y1+24)
cloud_chips_svg, y3 = row_chips(chips_cloud,36, y2+24)
total_h = y3 + 40

STACK_SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 {total_h}" width="860" height="{total_h}">
  <defs>
    <style>{COMMON_CSS}</style>
    <linearGradient id="g1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{BLUE}" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="{CRIMSON}" stop-opacity="0.05"/>
    </linearGradient>
    <linearGradient id="border" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{BLUE}"/>
      <stop offset="100%" stop-color="{CRIMSON}"/>
    </linearGradient>
    <pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="{BLUE}" fill-opacity="0.07"/>
    </pattern>
  </defs>
  
  {bg_elements(860, total_h)}

  <text x="36" y="40" font-size="11" font-family="'JetBrains Mono',monospace" fill="{BLUE}" letter-spacing="3">TECH STACK</text>
  <rect x="36" y="46" width="60" height="2" fill="{BLUE}" rx="1"/>

  <text x="36" y="78" font-size="12" fill="{DIM}" font-family="'JetBrains Mono',monospace">// Languages</text>
  {lang_chips_svg}

  <text x="36" y="{y1+14}" font-size="12" fill="{DIM}" font-family="'JetBrains Mono',monospace">// Web &amp; Frameworks</text>
  {web_chips_svg}

  <text x="36" y="{y2+14}" font-size="12" fill="{DIM}" font-family="'JetBrains Mono',monospace">// Cloud, DB &amp; DevOps</text>
  {cloud_chips_svg}
</svg>"""

# ════════════════════════════════════════════════════════════════════════════
# 4. id-dashboard.svg
# ════════════════════════════════════════════════════════════════════════════
ID_DASH_SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 420" width="860" height="420">
  <defs>
    <style>{COMMON_CSS}</style>
    <linearGradient id="g1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{BLUE}" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="{CRIMSON}" stop-opacity="0.06"/>
    </linearGradient>
    <linearGradient id="border" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{BLUE}"/>
      <stop offset="100%" stop-color="{CRIMSON}"/>
    </linearGradient>
    <linearGradient id="cardgrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#111827"/>
      <stop offset="100%" stop-color="#0a0f1e"/>
    </linearGradient>
    <linearGradient id="cardtop" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{BLUE}"/>
      <stop offset="100%" stop-color="{CRIMSON}"/>
    </linearGradient>
    <linearGradient id="foil" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="white" stop-opacity="0"/>
      <stop offset="40%" stop-color="white" stop-opacity="0.07"/>
      <stop offset="60%" stop-color="white" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="white" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="idportrait">
      <rect x="0" y="0" width="110" height="110" rx="10"/>
    </clipPath>
    <filter id="dropshadow">
      <feDropShadow dx="0" dy="8" stdDeviation="16" flood-color="{BLUE}" flood-opacity="0.35"/>
    </filter>
    <pattern id="barcode" x="0" y="0" width="6" height="40" patternUnits="userSpaceOnUse">
      <rect x="0" y="0" width="3" height="40" fill="{OFF_W}"/>
      <rect x="4" y="0" width="1" height="40" fill="{OFF_W}" opacity="0.4"/>
    </pattern>
    <pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="{BLUE}" fill-opacity="0.07"/>
    </pattern>
  </defs>

  {bg_elements(860, 420)}

  <text x="36" y="50" font-size="11" font-family="'JetBrains Mono',monospace" fill="{BLUE}" letter-spacing="3">DEVELOPER ID</text>
  <rect x="36" y="56" width="60" height="2" fill="{BLUE}" rx="1"/>

  <text x="36" y="96" font-size="13" fill="{DIM}">Role</text>
  <text x="36" y="114" font-size="16" font-weight="700" fill="{OFF_W}">Full-Stack Developer · AI Engineer</text>

  <text x="36" y="148" font-size="13" fill="{DIM}">University</text>
  <text x="36" y="166" font-size="15" fill="{OFF_W}">TKREC — B.Tech IT (2023–2027)</text>

  <text x="36" y="200" font-size="13" fill="{DIM}">Location</text>
  <text x="36" y="218" font-size="15" fill="{OFF_W}">Hyderabad, India</text>

  <text x="36" y="252" font-size="13" fill="{DIM}">Specialisation</text>
  <text x="36" y="270" font-size="15" fill="{OFF_W}">Next.js · Supabase · Python · AI/ML</text>

  <text x="36" y="304" font-size="13" fill="{DIM}">Status</text>
  <rect x="36" y="312" width="12" height="12" rx="6" fill="#22c55e">
    <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/>
  </rect>
  <text x="54" y="323" font-size="14" fill="#22c55e" font-weight="600">Available for Internship</text>

  <text x="36" y="360" font-size="13" fill="{DIM}">Certifications</text>
  <text x="36" y="378" font-size="11.5" fill="{OFF_W}">AWS Developer Associate (Infosys)</text>
  <text x="36" y="394" font-size="11.5" fill="{OFF_W}">ServiceNow CIS-DF · NPTEL ML · Ethical Hacking</text>

  <!-- LANYARD CARD -->
  <g transform="translate(590,0)">
    <animateTransform attributeName="transform" type="translate" values="590,0;590,0" dur="0.1s" begin="0s" fill="both"/>
  </g>
  <g id="lanyard" transform-origin="720 10">
    <animateTransform attributeName="transform" type="translate" additive="sum"
      values="0,-300;0,20;0,-8;0,3;0,0" dur="1.2s" begin="0s" keyTimes="0;0.55;0.75;0.88;1" fill="both"/>
    <animateTransform attributeName="transform" type="rotate" additive="sum"
      values="0 720 10;1.7 720 10;0 720 10;-1.7 720 10;0 720 10" dur="4s" begin="1.5s" repeatCount="indefinite" keyTimes="0;0.25;0.5;0.75;1"/>

    <line x1="720" y1="10" x2="720" y2="68" stroke="{BLUE}" stroke-width="3" opacity="0.6"/>
    <line x1="700" y1="10" x2="700" y2="68" stroke="{BLUE}" stroke-width="1.5" opacity="0.3"/>
    <line x1="740" y1="10" x2="740" y2="68" stroke="{BLUE}" stroke-width="1.5" opacity="0.3"/>

    <rect x="706" y="60" width="28" height="16" rx="4" fill="#374151" stroke="{DIM}" stroke-width="1"/>
    <rect x="711" y="64" width="18" height="8" rx="2" fill="#1f2937"/>
    <circle cx="720" cy="68" r="3" fill="{DIM}"/>

    <g filter="url(#dropshadow)">
      <rect x="600" y="72" width="240" height="330" rx="16" fill="url(#cardgrad)" stroke="{BORDER}" stroke-width="1.5"/>
      <rect x="600" y="72" width="240" height="48" rx="16" fill="url(#cardtop)"/>
      <rect x="600" y="104" width="240" height="16" fill="url(#cardtop)"/>
      <rect x="600" y="72" width="240" height="330" rx="16" fill="url(#foil)">
        <animate attributeName="x" values="440;840;440" dur="6s" begin="1.5s" repeatCount="indefinite"/>
      </rect>

      <text x="720" y="103" font-size="11" font-family="'JetBrains Mono',monospace" fill="white" text-anchor="middle" letter-spacing="2" font-weight="700">DEV · ID CARD</text>

      <image href="{ID_URI}" x="655" y="130" width="130" height="130" clip-path="url(#idportrait)" preserveAspectRatio="xMidYMid slice"/>
      <rect x="655" y="130" width="130" height="130" rx="10" fill="none" stroke="white" stroke-width="1.5" opacity="0.3"/>

      <text x="720" y="278" font-size="16" font-weight="900" fill="{OFF_W}" text-anchor="middle">ANAND JATOTHU</text>
      <text x="720" y="296" font-size="11" fill="{DIM}" text-anchor="middle">Full-Stack · AI/ML · Cloud</text>

      <line x1="620" y1="306" x2="820" y2="306" stroke="{BORDER}" stroke-width="1"/>
      <rect x="630" y="314" width="180" height="40" fill="url(#barcode)" opacity="0.85"/>
      <text x="720" y="372" font-size="9" fill="{DIM}" text-anchor="middle" font-family="'JetBrains Mono',monospace">ANAND-JATOTHU · github.com</text>

      <rect x="790" y="82" width="38" height="18" rx="5" fill="rgba(255,255,255,0.15)" stroke="white" stroke-width="0.5" opacity="0.6"/>
      <text x="809" y="94" font-size="9" fill="white" text-anchor="middle" font-weight="700">2026</text>
    </g>
  </g>
</svg>"""

# ════════════════════════════════════════════════════════════════════════════
# 5. connect.svg
# ════════════════════════════════════════════════════════════════════════════
CONNECT_SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 340" width="860" height="340">
  <defs>
    <style>{COMMON_CSS}</style>
    <linearGradient id="g1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{BLUE}" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="{CRIMSON}" stop-opacity="0.06"/>
    </linearGradient>
    <linearGradient id="border" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{BLUE}"/>
      <stop offset="100%" stop-color="{CRIMSON}"/>
    </linearGradient>
    <pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="{BLUE}" fill-opacity="0.07"/>
    </pattern>
    <clipPath id="rpclip">
      <rect x="0" y="0" width="320" height="340"/>
    </clipPath>
  </defs>

  {bg_elements(860, 340)}

  <image href="{RP_URI}" x="-20" y="20" width="360" height="310" clip-path="url(#rpclip)" preserveAspectRatio="xMidYMid meet" opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.7s" begin="0.3s" fill="both"/>
    <animate attributeName="x" values="-60;-20" dur="0.7s" begin="0.3s" fill="both"/>
  </image>

  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="1s" fill="both"/>
    <text font-size="28" fill="{BLUE}">
      <animate attributeName="x" values="300;316;300" dur="1.2s" begin="1s" repeatCount="indefinite"/>
      <tspan x="300" y="176">→</tspan>
    </text>
  </g>

  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.6s" begin="0.8s" fill="both"/>

    <text x="360" y="48" font-size="11" font-family="'JetBrains Mono',monospace" fill="{BLUE}" letter-spacing="3">LET'S CONNECT</text>
    <rect x="360" y="54" width="60" height="2" fill="{BLUE}" rx="1"/>

    <rect x="360" y="68" width="460" height="44" rx="10" fill="{CARD}" stroke="{BORDER}" stroke-width="1"/>
    <text x="380" y="96" font-size="16" fill="{OFF_W}">⚫</text>
    <text x="406" y="90" font-size="13" font-weight="700" fill="{OFF_W}">GitHub</text>
    <text x="406" y="105" font-size="11.5" fill="{DIM}">github.com/ANAND-JATOTHU</text>
    <text x="800" y="97" font-size="13" fill="{BLUE}" text-anchor="end">→</text>

    <rect x="360" y="122" width="460" height="44" rx="10" fill="{CARD}" stroke="{BORDER}" stroke-width="1"/>
    <text x="380" y="150" font-size="16" fill="#0077b5">in</text>
    <text x="406" y="144" font-size="13" font-weight="700" fill="{OFF_W}">LinkedIn</text>
    <text x="406" y="159" font-size="11.5" fill="{DIM}">linkedin.com/in/anandjatothu</text>
    <text x="800" y="151" font-size="13" fill="{BLUE}" text-anchor="end">→</text>

    <rect x="360" y="176" width="460" height="44" rx="10" fill="{CARD}" stroke="{BORDER}" stroke-width="1"/>
    <text x="380" y="204" font-size="16" fill="{BLUE}">🌐</text>
    <text x="406" y="198" font-size="13" font-weight="700" fill="{OFF_W}">Portfolio</text>
    <text x="406" y="213" font-size="11.5" fill="{DIM}">anandjatothu.me</text>
    <text x="800" y="205" font-size="13" fill="{BLUE}" text-anchor="end">→</text>

    <rect x="360" y="230" width="460" height="44" rx="10" fill="{CARD}" stroke="{BORDER}" stroke-width="1"/>
    <text x="380" y="258" font-size="16" fill="{CRIMSON}">✉</text>
    <text x="406" y="252" font-size="13" font-weight="700" fill="{OFF_W}">Email</text>
    <text x="406" y="267" font-size="11.5" fill="{DIM}">anand.jatothu.27@gmail.com</text>
    <text x="800" y="259" font-size="13" fill="{BLUE}" text-anchor="end">→</text>

    <rect x="360" y="284" width="460" height="44" rx="10" fill="{CARD}" stroke="{BORDER}" stroke-width="1"/>
    <text x="380" y="312" font-size="16" fill="#34d399">📱</text>
    <text x="406" y="306" font-size="13" font-weight="700" fill="{OFF_W}">Phone</text>
    <text x="406" y="321" font-size="11.5" fill="{DIM}">+91 8121093531</text>
    <text x="800" y="313" font-size="13" fill="{BLUE}" text-anchor="end">→</text>
  </g>
</svg>"""

# ════════════════════════════════════════════════════════════════════════════
# Write all SVG files
# ════════════════════════════════════════════════════════════════════════════
files = {
    "assets/hero.svg":         HERO_SVG,
    "assets/about-life.svg":   ABOUT_SVG,
    "assets/stack.svg":        STACK_SVG,
    "assets/id-dashboard.svg": ID_DASH_SVG,
    "assets/connect.svg":      CONNECT_SVG,
}

for path, content in files.items():
    full = os.path.join(REPO, path)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✔ Written: {path}")

# ════════════════════════════════════════════════════════════════════════════
# README.md
# ════════════════════════════════════════════════════════════════════════════
README = """<!-- ANAND JATOTHU — GitHub Profile README -->
<div align="center">

![Hero](assets/hero.svg)

</div>

---

<div align="center">

![About Life](assets/about-life.svg)

</div>

---

<div align="center">

![Tech Stack](assets/stack.svg)

</div>

---

## 🚀 Featured Projects

| Project | Description | Stack | Live |
|---------|-------------|-------|------|
| **[StuLink](https://github.com/ANAND-JATOTHU/StuLink)** | Safe social learning & skill-sharing platform with RLS, parent portal, text-moderation engine (↓95% unsafe msgs) | Next.js · TS · React 19 · Supabase · Cloudinary | [▶ Demo](https://stu-link-web.vercel.app/) |
| **[Foodify](https://github.com/ANAND-JATOTHU)** | Dual-purpose food delivery & donation platform with map-based logistics (↓40% carbon footprint) | Django · Python · Stripe · Geoapify | — |
| **[SRUTHI](https://github.com/ANAND-JATOTHU)** | Fully offline conversational AI assistant — Mistral-7B + Faster-Whisper + PyQt6 GPU GUI (83% task completion) | Python · Mistral LLM · CustomTkinter | — |
| **[Transvara](https://github.com/ANAND-JATOTHU)** | Secure & fast file transfer web app | Next.js · Node.js | [▶ Demo](https://transfer-app-frontend.vercel.app/) |

---

## 📊 GitHub Stats

<div align="center">

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=ANAND-JATOTHU&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true)
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=ANAND-JATOTHU&theme=tokyonight&hide_border=true&layout=compact&count_private=true)

</div>

---

<div align="center">

![Connect](assets/connect.svg)

</div>

<div align="center">

**[🌐 Portfolio](https://anandjatothu.me)** &nbsp;·&nbsp; **[💼 LinkedIn](https://linkedin.com/in/anandjatothu)** &nbsp;·&nbsp; **[⚫ GitHub](https://github.com/ANAND-JATOTHU)** &nbsp;·&nbsp; **[✉ Email](mailto:anand.jatothu.27@gmail.com)**

</div>

---

<div align="center">

![ID Dashboard](assets/id-dashboard.svg)

</div>

<div align="center">

<img src="https://komarev.com/ghpvc/?username=ANAND-JATOTHU&label=Profile%20Views&color=0e75b6&style=flat" alt="Profile Views" />

</div>
"""

readme_path = os.path.join(REPO, "README.md")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(README)
print("✔ Written: README.md")

# Removed temp file cleanup because we no longer use them

print("DONE ✅")

import os
import re
import base64
from PIL import Image
from io import BytesIO

def to_b64(path, size, quality=80):
    img = Image.open(path)
    img.thumbnail(size)
    buffer = BytesIO()
    img.save(buffer, format="PNG", optimize=True)
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

id_b64 = to_b64("assets/id.png", (400, 400))
rp_b64 = to_b64("assets/right_pointing.png", (400, 400))

replacements = {
    # Names and Titles
    "Udit Gupta": "Anand Jatothu",
    "UDIT GUPTA": "ANAND JATOTHU",
    "SDE at Amazon, Bengaluru.": "Full-Stack Web Developer, Hyderabad.",
    "Udit's": "Anand's",
    
    # Hero links / text
    "SDE at Amazon, Bengaluru": "Full-Stack Web Developer",
    "Bengaluru": "Hyderabad",
    "Amazon": "",
    
    # Social and Connect
    "@grow.with_udit": "anand.jatothu",
    "grow.with_udit": "anand.jatothu",
    "growwith_udit": "anandjatothu",
    "Grow with Udit": "Anand Jatothu",
    "udit_gupta5": "anandjatothu.me",
    "udit0510": "ANAND-JATOTHU",
    "Topmate bookings": "Visits",
    "Topmate session": "Connect Session",
    "Topmate": "Portfolio",
    "LeetCode": "Email",
    "https://www.linkedin.com/in/udit-gupta-ug0510/": "https://linkedin.com/in/anandjatothu",
    "https://www.youtube.com/@growwith_udit": "https://github.com/ANAND-JATOTHU",
    "https://www.instagram.com/grow.with_udit/": "mailto:anand.jatothu.27@gmail.com",
    "https://topmate.io/udit_gupta5": "https://anandjatothu.me",
    "https://leetcode.com/u/udit0510/": "mailto:anand.jatothu.27@gmail.com",
    
    # Stack Text
    "My stack: Java, TypeScript, Python, React, Next.js, Node.js, Express, AWS, and LLM APIs.": "My stack: Python, TypeScript, Java, React, Next.js, Node.js, Django, AWS, Supabase, Mistral LLM.",
    
    # Individual stack bubbles - Udit has exactly these
    # Row 1: Java, TypeScript, Python (Keep these, maybe map Java->Java, TypeScript->TypeScript, Python->Python)
    # Row 2: React, Next.js, Node.js (Keep these)
    # Row 3: Express, AWS, LLM APIs -> Django, Supabase, Mistral LLM
    ">Express<": ">Django<",
    ">AWS<": ">Supabase<",
    ">LLM APIs<": ">Mistral LLM<",
    
    # About Life
    "Modern web and app development, AI and cloud integration, community mentorship. Beyond work: creating tech content, 1:1 career mentorship, and competitive programming.": 
    "Innovative Full-Stack Web Developer specializing in designing scalable applications, backend databases, and intelligent solutions. Beyond work: building modern real-world software.",
    
    ">BUILD / MENTOR / CREATE / REPEAT<": ">DESIGN / BUILD / DEPLOY / REPEAT<",
    
    # Dashboard stats replacements
    "37 Topmate bookings, 50 public repositories, 12 received repo stars. Snapshot: October 2, 2026.": "B.Tech in IT | Cloud, Databases & Backend | AI/ML integrations | Problem Solving."
}

os.makedirs('assets', exist_ok=True)
svg_files = ['hero.svg', 'about-life.svg', 'stack.svg', 'id-dashboard.svg', 'connect.svg']

for file in svg_files:
    in_path = os.path.join('ug0510_assets', file)
    out_path = os.path.join('assets', file)
    
    with open(in_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for k, v in replacements.items():
        content = content.replace(k, v)
        
    # Replace images
    def replacer(match):
        b64 = match.group(2)
        if len(b64) > 350000:
            return f"data:image/png;base64,{id_b64}"
        elif len(b64) > 200000:
            return f"data:image/png;base64,{rp_b64}"
        else:
            return match.group(0) 
            
    content = re.sub(r'data:image/([^;]+);base64,([^\"]+)', replacer, content)
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed and wrote {file}")

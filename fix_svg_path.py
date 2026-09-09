import re

with open('index.html', 'r') as f:
    content = f.read()

# Make the white path taller to ensure no gaps
svg_old = """                    <path d="M60,100 C75,70 90,70 100,85 L100,105 L60,105 Z" fill="#ffffff"></path>"""
svg_new = """                    <path d="M50,105 C70,60 90,60 100,85 L100,105 Z" fill="#ffffff"></path>"""
content = content.replace(svg_old, svg_new)

# Navy path
svg_old_n = """                    <path d="M0,75 C25,50 50,100 80,95 L100,105 L0,105 Z" fill="var(--navy)"></path>"""
svg_new_n = """                    <path d="M0,75 C30,45 60,115 100,80 L100,105 L0,105 Z" fill="var(--navy)"></path>"""
content = content.replace(svg_old_n, svg_new_n)

with open('index.html', 'w') as f:
    f.write(content)
print("done")

import os
import re

files = ["index.html", "blog.html", "resources.html", "recipes.html", "aim.html", "testimony.html", "post.html"]

for filename in files:
    if not os.path.exists(filename): continue
    
    with open(filename, 'r') as f:
        content = f.read()
        
    # 1. Logo Replacement
    content = content.replace('images/BOUNTIFUL.png', 'images/testimonies.png')
    
    # 2. Favicon
    if '<link rel="icon"' not in content:
        content = content.replace('</title>', '</title>\n    <link rel="icon" href="images/testimonies.png">')
        
    # 3. Banner animation & typography
    content = content.replace('cycleW1 8s infinite', 'cycleW1 3s infinite')
    content = content.replace('cycleW2 8s infinite', 'cycleW2 3s infinite')
    content = content.replace('cycleW3 8s infinite', 'cycleW3 3s infinite')
    content = content.replace('cycleW4 8s infinite', 'cycleW4 3s infinite')
    
    # Increase letter spacing in word-slide, change font-weight to 400
    content = re.sub(r'\.word-slide\s*\{\s*font-weight:\s*700;\s*letter-spacing:\s*4px;', 
                     r'.word-slide { \n            font-weight: 400; \n            letter-spacing: 12px;', content)
                     
    # Page title letter spacing
    content = re.sub(r'\.page-title\s*\{([^\}]+)letter-spacing:\s*20px;([^\}]+)font-weight:\s*800;',
                     r'.page-title {\1letter-spacing: 25px;\2font-weight: 400;', content)

    # 4. Montserrat adjustments
    content = content.replace('font-weight: 800;', 'font-weight: 400;')
    content = content.replace('font-weight: 700;', 'font-weight: 400;')
    # Keep Great Vibes at 400
    
    # 5. Background alternating (White/Cream)
    if 'bg-white' not in content:
        content = content.replace('</style>', '        .bg-white { background-color: white; }\n        .bg-cream { background-color: var(--bg-color); }\n</style>')

    with open(filename, 'w') as f:
        f.write(content)

print("Pass 1 done")

import os

animated_banner_css = """
        /* Single Word Banner */
        .banner { 
            background-color: var(--coral); 
            height: 60px; 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            gap: 30px;
            overflow: hidden;
        }
        .word-slide { 
            font-weight: 700; 
            letter-spacing: 4px; 
            color: var(--navy);
            font-size: 1.1rem;
        }
        .word-slide:nth-child(1) { animation: cycleW1 8s infinite; }
        .word-slide:nth-child(2) { animation: cycleW2 8s infinite; }
        .word-slide:nth-child(3) { animation: cycleW3 8s infinite; }
        .word-slide:nth-child(4) { animation: cycleW4 8s infinite; }
        @keyframes cycleW1 {
            0%, 95% { opacity: 1; transform: translateX(0); }
            96%, 100% { opacity: 0; transform: translateX(0); }
        }
        @keyframes cycleW2 {
            0%, 24% { opacity: 0; transform: translateX(-10px); }
            25%, 95% { opacity: 1; transform: translateX(0); }
            96%, 100% { opacity: 0; transform: translateX(0); }
        }
        @keyframes cycleW3 {
            0%, 49% { opacity: 0; transform: translateX(-10px); }
            50%, 95% { opacity: 1; transform: translateX(0); }
            96%, 100% { opacity: 0; transform: translateX(0); }
        }
        @keyframes cycleW4 {
            0%, 74% { opacity: 0; transform: translateX(-10px); }
            75%, 95% { opacity: 1; transform: translateX(0); }
            96%, 100% { opacity: 0; transform: translateX(0); }
        }
"""

animated_banner_html = """
    <div class="banner">
        <div class="word-slide">FAITH</div>
        <div class="word-slide">FOOD</div>
        <div class="word-slide">FAMILY</div>
        <div class="word-slide">FELLOWSHIP</div>
    </div>
"""

def process_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # Add CSS if not present
    if "/* Single Word Banner */" not in content:
        # Find </style> and insert before
        content = content.replace("</style>", animated_banner_css + "</style>")
    
    # Replace static banner if present
    static_banner_html1 = """    <div class="banner">
        FAITH - FOOD - FAMILY - FELLOWSHIP
    </div>"""
    static_banner_html2 = """    <div class="banner">
        FAITH - FOOD - FAMILY - FELLOWSHIP
    </div>"""
    
    if "FAITH - FOOD - FAMILY - FELLOWSHIP" in content and "word-slide" not in content:
        # find the <div class="banner"> block and replace
        import re
        content = re.sub(r'<div class="banner">\s*FAITH - FOOD - FAMILY - FELLOWSHIP\s*</div>', animated_banner_html, content, flags=re.IGNORECASE)
    
    if "word-slide" not in content and filename in ["recipes.html", "aim.html", "testimony.html"]:
        # Add the banner html after nav (recipes, aim) or after hero (testimony)
        if filename == "testimony.html":
            content = content.replace('</div>\n\n    <div class="container">', '</div>\n' + animated_banner_html + '\n    <div class="container">')
            content = content.replace('</div>\n    <div class="container">', '</div>\n' + animated_banner_html + '\n    <div class="container">')
        elif filename in ["recipes.html", "aim.html"]:
            content = content.replace('</nav>', '</nav>\n' + animated_banner_html)

    with open(filename, 'w') as f:
        f.write(content)

for file in ["index.html", "blog.html", "resources.html", "recipes.html", "aim.html", "testimony.html"]:
    process_file(file)

print("done")

import os
for file in ["recipes.html", "aim.html", "post.html"]:
    if not os.path.exists(file): continue
    with open(file, 'r') as f:
        content = f.read()
    
    # Simple replacement
    content = content.replace('.logo img { height: 120px; object-fit: contain;  }', '.logo img { height: 120px; object-fit: contain; filter: brightness(0); }')
    content = content.replace('.logo img { height: 120px; object-fit: contain; }', '.logo img { height: 120px; object-fit: contain; filter: brightness(0); }')
    
    with open(file, 'w') as f:
        f.write(content)
print("Logo fixed")

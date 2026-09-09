for filename in ["index.html", "blog.html", "resources.html", "recipes.html", "aim.html", "testimony.html", "post.html"]:
    with open(filename, 'r') as f:
        content = f.read()
    
    content = content.replace('.bg-cream { background-color: white; }', '.bg-cream { background-color: var(--bg-color); }')
    
    with open(filename, 'w') as f:
        f.write(content)
print("done")

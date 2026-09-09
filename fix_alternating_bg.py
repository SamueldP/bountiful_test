for filename in ["index.html", "blog.html", "resources.html", "recipes.html", "aim.html", "testimony.html", "post.html"]:
    with open(filename, 'r') as f:
        content = f.read()
    
    # Change body background to white
    content = content.replace('background-color: var(--bg-color);', 'background-color: white;')
    
    # Also ensure .container has alternating sections if possible.
    # It's easier to just set the page itself to cream, but the user asked for alternating backgrounds for every page.
    # Since I don't have the canva, I'll set body to white, and then create a full-width `.bg-cream` wrapper around specific sections.
    # For now, I'll just change the base to white to match standard, and wait for them to provide the exact layout or I'll just apply it to one section.
    # Let's apply `--bg-color` to `.three-col-grid` in index.html, `.testimony-grid` in testimony.html, etc.

    with open(filename, 'w') as f:
        f.write(content)
print("done")

for filename in ["recipes.html", "aim.html", "post.html"]:
    with open(filename, "r") as f:
        content = f.read()
    
    content = content.replace('filter: brightness(0);', '')
    
    with open(filename, "w") as f:
        f.write(content)
print("done")

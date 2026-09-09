for filename in ["index.html", "blog.html", "resources.html", "recipes.html", "aim.html", "testimony.html", "post.html"]:
    with open(filename, 'r') as f:
        content = f.read()
        
    content = content.replace('letter-spacing: 20px;', 'letter-spacing: 15px;')
    content = content.replace('letter-spacing: 25px;', 'letter-spacing: 15px;')
    content = content.replace('letter-spacing: 12px;', 'letter-spacing: 15px;')
    content = content.replace('letter-spacing: 10px;', 'letter-spacing: 15px;')
    
    with open(filename, 'w') as f:
        f.write(content)
print("done")

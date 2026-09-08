import re

for filename, blog_type in [("blog.html", "health"), ("recipes.html", "recipes")]:
    with open(filename, "r") as f:
        content = f.read()

    # The current script block has this piece:
    old_code = """                    let link = '#';
                    const alternateLink = post.link.find(l => l.rel === 'alternate');
                    if (alternateLink) link = alternateLink.href;"""
                    
    new_code = f"""                    let link = '#';
                    const postIdMatch = post.id.$t.match(/post-(\\d+)/);
                    if (postIdMatch) {{
                        link = `post.html?blog={blog_type}&id=${{postIdMatch[1]}}`;
                    }} else {{
                        const alternateLink = post.link.find(l => l.rel === 'alternate');
                        if (alternateLink) link = alternateLink.href;
                    }}"""
    
    if old_code in content:
        content = content.replace(old_code, new_code)
    else:
        print(f"old_code not found in {filename}")
        
    # Also change target="_blank" to target="_self" or just remove target="_blank" so it opens in the same tab smoothly
    content = content.replace('target="_blank"', '')

    with open(filename, "w") as f:
        f.write(content)
print("done")

import re

for filename in ["blog.html", "recipes.html"]:
    with open(filename, "r") as f:
        content = f.read()

    new_script = """    <script>
        function handleBloggerPosts(data) {
            const container = document.getElementById('blog-container');
            if (!container) return;
            const posts = data.feed.entry;
            
            container.innerHTML = ''; 

            if (!posts || posts.length === 0) {
                container.innerHTML = '<div style="grid-column: 1 / -1; text-align:center;">No posts found yet!</div>';
                return;
            }

            try {
                posts.forEach(post => {
                    const title = post.title.$t;
                    const content = post.content ? post.content.$t : (post.summary ? post.summary.$t : ''); 
                    
                    let link = '#';
                    const alternateLink = post.link.find(l => l.rel === 'alternate');
                    if (alternateLink) link = alternateLink.href;

                    let imgHtml = '';
                    const imgMatch = content.match(/<img[^>]+src="([^">]+)"/);
                    if (imgMatch) {
                        imgHtml = `<div class="recipe-image" style="background-image: url('${imgMatch[1]}'); background-size: cover; background-position: center;"></div>`;
                    } else {
                        imgHtml = `<div class="recipe-image"><div class="cloud cloud-main"></div></div>`;
                    }

                    const postHTML = `
                        <a href="${link}" target="_blank" class="recipe-card">
                            ${imgHtml}
                            <h3 class="recipe-title">${title}</h3>
                        </a>
                    `;
                    
                    container.insertAdjacentHTML('beforeend', postHTML);
                });
            } catch (error) {
                console.error("Error parsing posts:", error);
                container.innerHTML = '<div style="grid-column: 1 / -1; text-align:center; color: red;">Error displaying posts.</div>';
            }
        }
    </script>
    <script src="https://bountiful-test.blogspot.com/feeds/posts/default?alt=json-in-script&callback=handleBloggerPosts"></script>"""
    
    # recipes.html doesn't have the script yet, so append it to body
    if filename == "recipes.html":
        # First, we need to change the hardcoded grid to just a container
        import re
        content = re.sub(r'<div class="recipes-grid">.*?</div>\n</body>', '<div id="blog-container" class="recipes-grid"></div>\n' + new_script + '\n</body>', content, flags=re.DOTALL)
        with open(filename, "w") as f:
            f.write(content)
            
    if filename == "blog.html":
        # we need to replace the old script
        import re
        content = re.sub(r'<script>\s*function handleBloggerPosts.*?</script>', new_script, content, flags=re.DOTALL)
        
        # also update the classes in blog.html to use recipe-image instead of blog-img so they match
        content = content.replace('.blog-img {', '.recipe-image {')
        content = content.replace('class="blog-title"', 'class="recipe-title"')
        content = content.replace('class="blog-card"', 'class="recipe-card"')
        content = content.replace('.blog-title', '.recipe-title')
        content = content.replace('.blog-card', '.recipe-card')
        
        # Add the placeholder CSS to blog.html since it uses recipe-image
        css_to_add = """
        .recipe-image {
            width: 100%;
            aspect-ratio: 1;
            background: linear-gradient(to bottom, #7CD3F8 0%, #E2F6CD 100%);
            position: relative;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            margin-bottom: 20px;
            overflow: hidden;
        }
        .recipe-image::before {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 40%;
            background: #99CC33;
            border-radius: 50% 50% 0 0 / 100% 100% 0 0;
            z-index: 1;
        }
        .recipe-image::after {
            content: '';
            position: absolute;
            bottom: 0;
            right: -10%;
            width: 70%;
            height: 30%;
            background: #7CB30B;
            border-radius: 50% 50% 0 0 / 100% 100% 0 0;
            z-index: 2;
        }
        .cloud {
            position: absolute;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50px;
            z-index: 0;
        }
        .cloud-main {
            top: 25%;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 30px;
        }
        .cloud-main::before {
            content: '';
            position: absolute;
            top: -20px;
            left: 15px;
            width: 40px;
            height: 40px;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
        }
        .cloud-main::after {
            content: '';
            position: absolute;
            top: -10px;
            right: 15px;
            width: 30px;
            height: 30px;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
        }
        """
        # remove old blog-img css
        content = re.sub(r'\.recipe-image\s*\{\s*width: 100%;\s*aspect-ratio: 1;\s*background-color: #e0f2f1;\s*background-size: cover;\s*background-position: center;\s*margin-bottom: 20px;\s*\}', css_to_add, content)
        
        with open(filename, "w") as f:
            f.write(content)

print("done")

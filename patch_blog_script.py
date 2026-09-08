with open("blog.html", "r") as f:
    content = f.read()

old_script = """    <script>
        function handleBloggerPosts(data) {
            const container = document.getElementById('blog-container');
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

                    let imgSrc = 'images/DSC_0476.JPG'; 
                    const imgMatch = content.match(/<img[^>]+src="([^">]+)"/);
                    if (imgMatch) {
                        imgSrc = imgMatch[1];
                    }

                    const postHTML = `
                        <a href="${link}" target="_blank" class="blog-card">
                            <div class="blog-img" style="background-image: url('${imgSrc}');"></div>
                            <h3 class="blog-title">${title}</h3>
                        </a>
                    `;
                    
                    container.insertAdjacentHTML('beforeend', postHTML);
                });
            } catch (error) {
                console.error("Error parsing posts:", error);
                container.innerHTML = '<div style="grid-column: 1 / -1; text-align:center; color: red;">Error displaying posts.</div>';
            }
        }
    </script>"""

new_script = """    <script>
        function handleBloggerPosts(data) {
            const container = document.getElementById('blog-container');
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
                        imgHtml = `<div class="blog-img" style="background-image: url('${imgMatch[1]}');"></div>`;
                    } else {
                        imgHtml = `<div class="blog-img-placeholder"><div class="cloud cloud-main"></div></div>`;
                    }

                    const postHTML = `
                        <a href="${link}" target="_blank" class="blog-card">
                            ${imgHtml}
                            <h3 class="blog-title">${title}</h3>
                        </a>
                    `;
                    
                    container.insertAdjacentHTML('beforeend', postHTML);
                });
            } catch (error) {
                console.error("Error parsing posts:", error);
                container.innerHTML = '<div style="grid-column: 1 / -1; text-align:center; color: red;">Error displaying posts.</div>';
            }
        }
    </script>"""

if old_script in content:
    content = content.replace(old_script, new_script)
else:
    print("Old script not found")
    
with open("blog.html", "w") as f:
    f.write(content)


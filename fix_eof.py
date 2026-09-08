for filename in ["blog.html", "recipes.html"]:
    with open(filename, "r") as f:
        content = f.read()

    import re
    # remove all closing tags and scripts at the end
    content = re.sub(r'<script src="https://bountiful-test.blogspot.com/feeds/posts/default.*?"></script>', '', content)
    content = re.sub(r'</body>\s*</html>', '', content)
    
    # append them back cleanly
    content += '\n    <script src="https://bountiful-test.blogspot.com/feeds/posts/default?alt=json-in-script&callback=handleBloggerPosts"></script>\n</body>\n</html>'
    
    with open(filename, "w") as f:
        f.write(content)

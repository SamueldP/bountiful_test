with open("testimony.html", "r") as f:
    content = f.read()

import re
# Hide "testimonies from you..." section
content = re.sub(r'<h2 class="script-title"[^>]*>testimonies from you\.\.\.</h2>', '<!-- <h2 class="script-title" style="margin-top: 80px;">testimonies from you...</h2>', content)
content = re.sub(r'<!-- Scripture Section -->', '</div> -->\n        <!-- Scripture Section -->', content)

# Update Isaiah scripture spacing
content = content.replace('.scripture-text { line-height: 2; letter-spacing: 2px;', '.scripture-text { line-height: 2; letter-spacing: 12px;')

with open("testimony.html", "w") as f:
    f.write(content)
print("done")

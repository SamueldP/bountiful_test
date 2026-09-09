# The user wants "a little bit about me" to be on cream, and the 3 columns to be on white.
import re

with open('index.html', 'r') as f:
    content = f.read()

# I'll create a cream wrapper for the "about me" section
old_about = '        <!-- About Section -->\n        <h2 class="script-title">a little bit about me...</h2>'
new_about = '        <!-- About Section -->\n    </div>\n    <div class="bg-cream" style="padding: 60px 0;">\n        <div class="container" style="padding-top: 0; padding-bottom: 0;">\n        <h2 class="script-title" style="margin-top: 0;">a little bit about me...</h2>'

content = content.replace(old_about, new_about)

old_col = '        <!-- 3 Columns -->'
new_col = '        </div>\n    </div>\n    <div class="container">\n        <!-- 3 Columns -->'

content = content.replace(old_col, new_col)

with open('index.html', 'w') as f:
    f.write(content)

print("done")

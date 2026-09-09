import re

with open('aim.html', 'r') as f:
    content = f.read()

# I want to add some space under the "M Y" text so the navy box looks better proportioned.
content = content.replace('padding: 10px 15px; background: white;">M Y</div>', 'padding: 10px 15px 5px 15px; background: white;">M Y</div>')
content = content.replace('padding-top: 25px;">', 'padding-top: 15px;">')

with open('aim.html', 'w') as f:
    f.write(content)

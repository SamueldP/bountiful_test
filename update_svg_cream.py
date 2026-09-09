import re

with open('index.html', 'r') as f:
    content = f.read()

# Change the white path in the wavy graphic to cream var(--bg-color)
content = content.replace('fill="#ffffff"', 'fill="var(--bg-color)"')

with open('index.html', 'w') as f:
    f.write(content)
print("done")

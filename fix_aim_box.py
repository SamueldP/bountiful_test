import re

with open('aim.html', 'r') as f:
    content = f.read()

# Make the outer container white, so the gap is white
old_container = '<div style="border: 2px solid var(--navy); padding: 5px; display: flex; flex-direction: column;">'
new_container = '<div style="border: 2px solid var(--navy); padding: 8px; display: flex; flex-direction: column; background: white;">'

content = content.replace(old_container, new_container)

with open('aim.html', 'w') as f:
    f.write(content)
print("done")

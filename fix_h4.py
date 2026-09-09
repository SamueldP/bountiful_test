import re

with open('index.html', 'r') as f:
    content = f.read()

content = content.replace('.col-box { padding: 50px 30px; color: white; text-align: center; line-height: 1.8; }', '.col-box { padding: 40px 30px; color: white; text-align: center; line-height: 1.8; height: 100%; box-sizing: border-box; }')
content = content.replace('.col-wrapper {', '.col-wrapper { display: flex; flex-direction: column; }')

if '.col-wrapper { display: flex; flex-direction: column; }' not in content:
    content = content.replace('</style>', '        .col-wrapper { display: flex; flex-direction: column; height: 100%; }\n</style>')

with open('index.html', 'w') as f:
    f.write(content)
print("done")

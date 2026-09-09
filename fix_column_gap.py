import re

with open('index.html', 'r') as f:
    content = f.read()

content = content.replace('.three-col-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-bottom: 80px; }', '.three-col-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; margin-bottom: 80px; align-items: stretch; }')

# Fix media query for columns
mq = """        @media (max-width: 900px) {
            .three-col-grid { grid-template-columns: 1fr; }
            .split-footer { flex-direction: column; height: auto; }"""
            
if '.three-col-grid { grid-template-columns: 1fr; }' not in content:
    content = content.replace('@media (max-width: 900px) {\n            .split-footer', '@media (max-width: 900px) {\n            .three-col-grid { grid-template-columns: 1fr; }\n            .split-footer')

with open('index.html', 'w') as f:
    f.write(content)
print("done")

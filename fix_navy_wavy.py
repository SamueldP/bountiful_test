import re

with open('index.html', 'r') as f:
    content = f.read()

# Make the border radius extreme to look wavy
content = content.replace('border-radius: 30px 10px 25px 15px / 15px 30px 10px 25px;', 'border-radius: 30px 10px 25px 15px / 15px 30px 10px 25px; box-shadow: -4px 4px 10px rgba(0,0,0,0.05);')

with open('index.html', 'w') as f:
    f.write(content)
print("done")

import re

with open('index.html', 'r') as f:
    content = f.read()

# Make the image crop differently so the head isn't covered by the wave
content = content.replace('.image-wrapper { position: relative; z-index: 2; margin-top: 40px; border-radius: 12px; overflow: hidden; width: 450px; max-width: 100%; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }', '.image-wrapper { position: relative; z-index: 2; margin-top: 40px; border-radius: 12px; overflow: hidden; width: 450px; max-width: 100%; box-shadow: 0 10px 30px rgba(0,0,0,0.1); aspect-ratio: 4/3; }')
content = content.replace('.image-wrapper img { width: 100%; display: block; position: relative; z-index: 2; }', '.image-wrapper img { width: 100%; height: 100%; object-fit: cover; object-position: center top; display: block; position: relative; z-index: 2; }')
content = content.replace('height: 45%;', 'height: 40%;')

with open('index.html', 'w') as f:
    f.write(content)
print("done")

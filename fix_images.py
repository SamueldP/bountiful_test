import re

for filename in ["blog.html", "recipes.html"]:
    with open(filename, "r") as f:
        content = f.read()

    # The CSS for the placeholder:
    old_css = """        .recipe-image {
            width: 100%;
            aspect-ratio: 1;
            background: linear-gradient(to bottom, #7CD3F8 0%, #E2F6CD 100%);
            position: relative;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            margin-bottom: 20px;
            overflow: hidden;
        }
        .recipe-image::before {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 40%;
            background: #99CC33;
            border-radius: 50% 50% 0 0 / 100% 100% 0 0;
            z-index: 1;
        }
        .recipe-image::after {
            content: '';
            position: absolute;
            bottom: 0;
            right: -10%;
            width: 70%;
            height: 30%;
            background: #7CB30B;
            border-radius: 50% 50% 0 0 / 100% 100% 0 0;
            z-index: 2;
        }
        .cloud {
            position: absolute;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50px;
            z-index: 0;
        }
        .cloud-main {
            top: 25%;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 30px;
        }
        .cloud-main::before {
            content: '';
            position: absolute;
            top: -20px;
            left: 15px;
            width: 40px;
            height: 40px;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
        }
        .cloud-main::after {
            content: '';
            position: absolute;
            top: -10px;
            right: 15px;
            width: 30px;
            height: 30px;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
        }"""
        
    new_css = """        .recipe-image {
            width: 100%;
            aspect-ratio: 1;
            background-image: url('images/DSC_0527.jpg');
            background-size: cover;
            background-position: right center;
            position: relative;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            margin-bottom: 20px;
            overflow: hidden;
            border-radius: 8px;
        }"""
        
    # Replace the old css with the new css
    if old_css in content:
        content = content.replace(old_css, new_css)
    else:
        # Regex fallback
        content = re.sub(r'\.recipe-image\s*\{[^\}]+\}\s*\.recipe-image::before\s*\{[^\}]+\}\s*\.recipe-image::after\s*\{[^\}]+\}\s*\.cloud\s*\{[^\}]+\}\s*\.cloud-main\s*\{[^\}]+\}\s*\.cloud-main::before\s*\{[^\}]+\}\s*\.cloud-main::after\s*\{[^\}]+\}', new_css, content)

    # In JS, remove the cloud divs
    content = content.replace('<div class="recipe-image"><div class="cloud cloud-main"></div></div>', '<div class="recipe-image"></div>')

    with open(filename, "w") as f:
        f.write(content)

print("done")

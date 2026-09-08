with open("blog.html", "r") as f:
    content = f.read()

placeholder_css = """
        .blog-img-placeholder {
            width: 100%;
            aspect-ratio: 1;
            background: linear-gradient(to bottom, #7CD3F8 0%, #E2F6CD 100%);
            position: relative;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            margin-bottom: 20px;
            overflow: hidden;
        }
        
        .blog-img-placeholder::before {
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
        .blog-img-placeholder::after {
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
        }
"""

if ".blog-img-placeholder" not in content:
    content = content.replace("</style>", placeholder_css + "</style>")

script_replacement = """
                    let imgHtml = '';
                    const imgMatch = content.match(/<img[^>]+src="([^">]+)"/);
                    if (imgMatch) {
                        imgHtml = `<div class="blog-img" style="background-image: url('${imgMatch[1]}');"></div>`;
                    } else {
                        imgHtml = `<div class="blog-img-placeholder"><div class="cloud cloud-main"></div></div>`;
                    }

                    const postHTML = `
                        <a href="${link}" target="_blank" class="blog-card">
                            ${imgHtml}
                            <h3 class="blog-title">${title}</h3>
                        </a>
                    `;
"""

import re
# Replace the part inside the forEach
content = re.sub(r"let imgSrc = 'images/DSC_0476\.JPG';\s*const imgMatch = content\.match\(/<img\[\^>\]\+src=\"\(\[\^\">\]\+\)\"/\);\s*if \(imgMatch\) {\s*imgSrc = imgMatch\[1\];\s*}\s*const postHTML = `\s*<a href=\"\$\{link\}\" target=\"_blank\" class=\"blog-card\">\s*<div class=\"blog-img\" style=\"background-image: url\('\$\{imgSrc\}'\);\"></div>\s*<h3 class=\"blog-title\">\$\{title\}</h3>\s*</a>\s*`;", script_replacement, content)


with open("blog.html", "w") as f:
    f.write(content)


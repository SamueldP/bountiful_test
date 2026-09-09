with open("aim.html", "r") as f:
    content = f.read()

import re
# Replace M Y label and ESSENTIALS with matching h4
old_essentials = """<div class="aim-card-label">M Y</div>
            <div class="aim-card card-blue">
                <h3 class="aim-card-title">ESSENTIALS</h3>"""
                
new_essentials = """<div class="aim-card card-blue">
                <h4 style="text-align: center; font-size: 1.1rem; letter-spacing: 10px; margin-top: 0; margin-bottom: 25px; line-height: 1.4;">M Y<br>E S S E N T I A L S</h4>"""

content = content.replace(old_essentials, new_essentials)

old_gotos = """<div class="aim-card-label">M Y</div>
            <div class="aim-card card-orange">
                <h3 class="aim-card-title">OTHER GO TOS</h3>"""
                
new_gotos = """<div class="aim-card card-orange">
                <h4 style="text-align: center; font-size: 1.1rem; letter-spacing: 10px; margin-top: 0; margin-bottom: 25px; line-height: 1.4;">O T H E R<br>G O  T O S</h4>"""

content = content.replace(old_gotos, new_gotos)

with open("aim.html", "w") as f:
    f.write(content)
print("done")

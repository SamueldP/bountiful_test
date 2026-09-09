import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace the dashed SVG with CSS mask-image for wavy borders
svg_old = """                    <!-- SVG Wavy outline overlay approximation -->
                    <svg style="position: absolute; top: -10px; left: -10px; width: calc(100% + 20px); height: calc(100% + 20px); pointer-events: none;" preserveAspectRatio="none" viewBox="0 0 100 100">
                        <rect x="2" y="2" width="96" height="96" rx="5" fill="none" stroke="var(--steel)" stroke-width="4" stroke-dasharray="8 6" rx="8"/>
                    </svg>"""

# Using CSS radial-gradient to create a scalloped/wavy border effect
# Wait, just simple border-radius 2% 5% 3% 4% etc can look wavy and organic.
css_wavy = """                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; background-color: var(--steel); border-radius: 20px 8px 15px 5px / 5px 15px 8px 20px;"></div>"""

# But wait, the background is already var(--navy). Let's use border-radius organically on the box itself.
content = content.replace('class="col-box box-navy" style="border-radius: 8px; position: relative;"', 'class="col-box box-navy" style="border-radius: 30px 10px 25px 15px / 15px 30px 10px 25px; position: relative;"')
content = content.replace(svg_old, '')

with open('index.html', 'w') as f:
    f.write(content)

print("done")

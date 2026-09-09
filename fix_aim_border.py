import re

with open('aim.html', 'r') as f:
    content = f.read()

old_card = """        <div class="aim-card-wrapper">
            <div class="aim-card-label" style="text-align: left; padding-left: 10px;">M Y</div>
            <div class="aim-card card-navy" style="margin-bottom: 0;">
                <h4 style="text-align: left; font-size: 1.1rem; letter-spacing: 15px; margin-top: 0; margin-bottom: 25px; line-height: 1.4; font-weight: 400;">J O U R N E Y  W I T H  A I M</h4>"""
                
new_card = """        <div style="border: 3px solid var(--navy); padding: 4px; display: flex; flex-direction: column;">
            <div style="color: var(--navy); font-weight: 800; letter-spacing: 15px; font-size: 1.2rem; padding: 10px 15px;">M Y</div>
            <div class="aim-card card-navy" style="margin-bottom: 0; padding-top: 25px;">
                <h4 style="text-align: left; font-size: 1.1rem; letter-spacing: 15px; margin-top: 0; margin-bottom: 25px; line-height: 1.4; font-weight: 800;">J O U R N E Y  W I T H  A I M</h4>"""

content = content.replace(old_card, new_card)

with open('aim.html', 'w') as f:
    f.write(content)
print("done")

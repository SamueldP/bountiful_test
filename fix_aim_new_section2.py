import re

with open('aim.html', 'r') as f:
    content = f.read()

new_html = """    <h1 class="page-title">A I M</h1>
    
    <div class="aim-intro-section">
        <div class="store-link-container">
            <a href="https://myaimstore.com/bountifulblossoming/" target="_blank" class="store-link">
                CLICK <strong>HERE</strong> FOR MY AIM STORE
            </a>
        </div>
        
        <div style="border: 2px solid var(--navy); padding: 5px; display: flex; flex-direction: column;">
            <div style="color: var(--navy); font-weight: 800; letter-spacing: 15px; font-size: 1.2rem; padding: 10px 15px; background: white;">M Y</div>
            <div class="aim-card card-navy" style="margin-bottom: 0; padding-top: 25px;">
                <h4 style="text-align: left; font-size: 1.2rem; letter-spacing: 15px; margin-top: 0; margin-bottom: 25px; line-height: 1.4; font-weight: 800;">J O U R N E Y  W I T H  A I M</h4>
                <p style="text-align: left; line-height: 1.8; font-size: 1rem; margin: 0;">
                    I was blessed to have been told about Aim when I started making lifestyle changes. While I did make some pretty big changes immediately, adjusting to a lifestyle that included more fresh whole-foods was not so easy at first. That's where I found Aim's wholefood natural supplements helped me the most. To get the good stuff in to kickstart the healing while allowing my body time to learn to enjoy food as it was originally meant to be enjoyed. While I can now easily eat raw fruits and veggies for breakfast, lunch and dinner I still use and am so grateful for Aim because life isn't always perfect...whether traveling, under stress, or being exposed to harmful things in our environment, our bodies can easily be depleted of nutrients and the balance disrupted. It's also not always possible to buy fresh, organic produce and get everything we need from our food in today's life. Aim has helped me there too and in more instances than one. HORMONES, DIGESTION, IMMUNITY and even PARASITES! Aim has just made things easier for me and seeing the benefits from these concentrated wholefoods in my own life and others' has only made me that much more in Awe of God who created these healing foods in the first place!
                </p>
            </div>
        </div>
    </div>
    
    <div class="aim-grid">"""

content = re.sub(r'<h1 class="page-title">A I M</h1>\s*<div class="aim-grid">', new_html, content)

with open('aim.html', 'w') as f:
    f.write(content)

print("done")

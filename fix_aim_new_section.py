import re

with open('aim.html', 'r') as f:
    content = f.read()

# Add CSS
new_css = """        /* New AIM Intro */
        .store-link-container {
            text-align: center;
            margin: 0 auto 60px auto;
            max-width: 800px;
        }
        .store-link {
            display: inline-block;
            background-color: var(--bg-color); /* Cream color */
            color: var(--navy);
            text-decoration: none;
            padding: 25px 40px;
            border-radius: 12px;
            letter-spacing: 15px;
            font-size: 1.1rem;
            text-transform: uppercase;
            transition: opacity 0.3s;
            width: 100%;
            box-sizing: border-box;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }
        .store-link:hover {
            opacity: 0.8;
        }
        .store-link strong {
            font-weight: 800;
        }
        .card-navy {
            background-color: var(--navy);
        }
        .aim-intro-section {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 60px 60px 60px;
        }
        
        @media (max-width: 900px) {"""
content = content.replace('@media (max-width: 900px) {', new_css)

# Add HTML between page-title and aim-grid
new_html = """    <h1 class="page-title">A I M</h1>
    
    <div class="aim-intro-section">
        <div class="store-link-container">
            <a href="https://myaimstore.com/bountifulblossoming/" target="_blank" class="store-link">
                CLICK <strong>HERE</strong> FOR MY AIM STORE
            </a>
        </div>
        
        <div class="aim-card-wrapper">
            <div class="aim-card-label" style="text-align: left; padding-left: 10px;">M Y</div>
            <div class="aim-card card-navy" style="margin-bottom: 0;">
                <h4 style="text-align: left; font-size: 1.1rem; letter-spacing: 15px; margin-top: 0; margin-bottom: 25px; line-height: 1.4; font-weight: 400;">J O U R N E Y  W I T H  A I M</h4>
                <p style="text-align: center; line-height: 1.8; font-size: 1rem; margin: 0;">
                    I was blessed to have been told about Aim when I started making lifestyle changes. While I did make some pretty big changes immediately, adjusting to a lifestyle that included more fresh whole-foods was not so easy at first. That's where I found Aim's wholefood natural supplements helped me the most. To get the good stuff in to kickstart the healing while allowing my body time to learn to enjoy food as it was originally meant to be enjoyed. While I can now easily eat raw fruits and veggies for breakfast, lunch and dinner I still use and am so grateful for Aim because life isn't always perfect...whether traveling, under stress, or being exposed to harmful things in our environment, our bodies can easily be depleted of nutrients and the balance disrupted. It's also not always possible to buy fresh, organic produce and get everything we need from our food in today's life. Aim has helped me there too and in more instances than one. HORMONES, DIGESTION, IMMUNITY and even PARASITES! Aim has just made things easier for me and seeing the benefits from these concentrated wholefoods in my own life and others' has only made me that much more in Awe of God who created these healing foods in the first place!
                </p>
            </div>
        </div>
    </div>
    
    <div class="aim-grid">"""

content = content.replace('    <h1 class="page-title">A I M</h1>\n    <div class="aim-grid">', new_html)

with open('aim.html', 'w') as f:
    f.write(content)

print("done")

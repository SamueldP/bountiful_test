with open('index.html', 'r') as f:
    content = f.read()

# 1. Image Wrapper CSS and HTML
css_old = """        /* Offset Image Styling */
        .image-wrapper { position: relative; z-index: 2; margin-top: 40px; }
        .image-wrapper img { width: 450px; max-width: 100%; position: relative; z-index: 2; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
        .bg-box-coral { position: absolute; bottom: -40px; left: -40px; width: 80%; height: 80%; background-color: var(--coral); z-index: 1; }
        .bg-box-navy { position: absolute; top: -40px; right: -40px; width: 70%; height: 70%; background-color: var(--navy); z-index: 0; }"""
        
css_new = """        /* Image Styling with Wavy Overlay */
        .image-wrapper { position: relative; z-index: 2; margin-top: 40px; border-radius: 12px; overflow: hidden; width: 450px; max-width: 100%; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
        .image-wrapper img { width: 100%; display: block; position: relative; z-index: 2; }
        .waves-overlay { position: absolute; bottom: -2px; left: 0; width: 100%; height: 45%; z-index: 10; pointer-events: none; display: block; }"""
        
content = content.replace(css_old, css_new)

img_old = """            <div class="image-wrapper">
                <div class="bg-box-navy"></div>
                <div class="bg-box-coral"></div>
                <img src="images/timmy_watermelon.jpg" alt="Timmy eating watermelon">
            </div>"""
            
img_new = """            <div class="image-wrapper">
                <img src="images/timmy_watermelon.jpg" alt="Timmy eating watermelon">
                <svg class="waves-overlay" viewBox="0 0 100 100" preserveAspectRatio="none">
                    <!-- Steel -->
                    <path d="M0,50 C30,20 60,80 100,60 L100,105 L0,105 Z" fill="var(--steel)"></path>
                    <!-- White -->
                    <path d="M60,100 C75,70 90,70 100,85 L100,105 L60,105 Z" fill="#ffffff"></path>
                    <!-- Navy -->
                    <path d="M0,75 C25,50 50,100 80,95 L100,105 L0,105 Z" fill="var(--navy)"></path>
                    <!-- Coral -->
                    <path d="M0,100 C15,80 35,80 50,105 L0,105 Z" fill="var(--coral)"></path>
                </svg>
            </div>"""

content = content.replace(img_old, img_new)

# 2. Columns updates
col_old = """        <!-- 3 Columns -->
        <div class="three-col-grid">
            <div class="col-box box-orange">
                <h4>WHERE IT<br>S T A R T E D</h4>
                <p>I am from Cape Town, South Africa. That is where I grew up and that is my home but I also love to travel and experience and see the rest of the world God has put together and his people all over!</p>
            </div>
            <div class="col-box box-lightblue">
                <h4>WHERE IT<br>S T A R T E D<br>A G A I N</h4>
                <p>I grew up knowing God but accepted Jesus into my heart in 2021 - the greatest decision I have ever made and ever will make! Ever since then he has only continued to reveal himself to me and given me things that I want to share now with YOU! And that includes my health journey which really began in May of 2021.</p>
            </div>
            <div class="col-box box-navy">
                <h4>WHERE I T ' S<br>A T</h4>
                <p>I believe that he wants to reveal more and more of himself to each and every one of us so that we can become more like Jesus and one of the ways he does that is through one another. For we are created in his image and his Spirit now lives within those of us who have accepted the Gospel in Faith! My prayer is that this will be a place we can do that. Amen!</p>
            </div>
        </div>"""
        
col_new = """        <!-- 3 Columns -->
        <div class="three-col-grid">
            <div class="col-wrapper">
                <div style="color: var(--navy); font-weight: 800; letter-spacing: 5px; font-size: 1.1rem; text-align: center; margin-bottom: 15px;">WHERE IT</div>
                <div class="col-box box-orange" style="border-radius: 8px;">
                    <h4>S T A R T E D</h4>
                    <p style="text-align: center; margin-bottom: 0;">I grew up loving food, eating anything and everything and my health concerns were not more than the concerns of most other people around me. That started to change when I was in my early teens and began struggling with hormonal acne which not only had its physical strains but mental and emotional too. It soon became so severe that I was willing to do whatever it would take to make it go away.</p>
                </div>
            </div>
            <div class="col-wrapper">
                <div style="color: var(--navy); font-weight: 800; letter-spacing: 5px; font-size: 1.1rem; text-align: center; margin-bottom: 15px;">WHERE IT</div>
                <div class="col-box box-lightblue" style="border-radius: 8px;">
                    <h4>S T A R T E D<br>A G A I N</h4>
                    <p style="text-align: center; margin-bottom: 0;">After resorting to medication and trying everything that I could try in my own strength without success, I cried out do God and he put my wellness coach - Michelle Pearson - on my path who helped me wean off the medication and just by changing my diet and lifestyle, my skin healed and problems I didn't even know were not normal came right too!</p>
                </div>
            </div>
            <div class="col-wrapper">
                <div style="color: var(--navy); font-weight: 800; letter-spacing: 5px; font-size: 1.1rem; text-align: center; margin-bottom: 15px;">WHERE I T ' S</div>
                <div class="col-box box-navy" style="border-radius: 8px; position: relative;">
                    <!-- SVG Wavy outline overlay approximation -->
                    <svg style="position: absolute; top: -10px; left: -10px; width: calc(100% + 20px); height: calc(100% + 20px); pointer-events: none;" preserveAspectRatio="none" viewBox="0 0 100 100">
                        <rect x="2" y="2" width="96" height="96" rx="5" fill="none" stroke="var(--steel)" stroke-width="4" stroke-dasharray="8 6" rx="8"/>
                    </svg>
                    <h4>A T</h4>
                    <p style="text-align: center; margin-bottom: 0;">I believe that he wants to reveal more and more of himself to each and every one of us so that we can become more like Jesus and one of the ways he does that is through one another. For we are created in his image and his Spirit now lives within those of us who have accepted the Gospel in Faith! My prayer is that this will be a place we can do that. Amen!</p>
                </div>
            </div>
        </div>"""
        
content = content.replace(col_old, col_new)

with open('index.html', 'w') as f:
    f.write(content)
print("Updated index.html")

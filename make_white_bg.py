# The user wants "alternating white and cream backgrounds for evry page"
# Since they just showed the white background and cream button, let's ensure body is cream, but maybe the sections are white?
# Looking at the Canva screenshots, the "a little bit about me" has a very light cream/peach background (like #FFF2E6 or our var(--bg-color)).
# The "WHERE IT STARTED" columns sit on a white background.
# The "A I M" page has a white background, with the button being cream.

with open('aim.html', 'r') as f:
    content = f.read()
    
# Check the CSS in aim.html
if 'background-color: white;' in content:
    print("aim body is already white")

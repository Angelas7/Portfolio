import re

with open(r'd:\CV PORTFOLIO\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Google Font link
html = html.replace('<!-- AOS CSS -->', '<!-- Google Fonts -->\n    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap" rel="stylesheet">\n    <!-- AOS CSS -->')

# 2. Update CSS Variables
old_vars = """:root {
            --dragonfly-red: #d21f1f;
            --white: #ffffff;
            --dark-red: #b01a1a;
            --black: #000000;
        }"""
new_vars = """:root {
            --midnight-navy: #132743;
            --thunderbird-red: #D21720;
            --lavender-blush: #FFF0F3;
            --white: #ffffff;
            --black: #000000;
        }"""
html = html.replace(old_vars, new_vars)

# 3. Update Font Family
html = html.replace(r"font-family: 'Times New Roman', serif;", r"font-family: 'Montserrat', sans-serif;")

# 4. Body theme
html = html.replace(r'background-color: var(--dragonfly-red);', r'background-color: var(--midnight-navy);')
html = html.replace(r'color: var(--white);', r'color: var(--lavender-blush);')

# 5. Nav bar
html = html.replace(r'background: rgba(176, 26, 26, 0.95);', r'background: rgba(19, 39, 67, 0.95);')
html = html.replace(r'color: var(--dragonfly-red) !important;', r'background: var(--thunderbird-red); color: var(--lavender-blush) !important;')
html = html.replace(r'background: var(--white);', r'background: var(--lavender-blush);')

# 6. Sticky section backgrounds
html = html.replace(r'background-color: var(--dragonfly-red); /* Solid BG fallback', r'background-color: var(--midnight-navy); /* Solid BG fallback')
html = html.replace(r'#about { z-index: 10; background-color: var(--white) !important; }', r'#about { z-index: 10; background-color: var(--lavender-blush) !important; color: var(--midnight-navy) !important; }')
html = html.replace(r'#skills { z-index: 20; background-color: var(--dragonfly-red) !important; }', r'#skills { z-index: 20; background-color: var(--midnight-navy) !important; color: var(--lavender-blush) !important; }')
html = html.replace(r'#projects { z-index: 30; background-color: var(--white) !important; }', r'#projects { z-index: 30; background-color: var(--lavender-blush) !important; color: var(--midnight-navy) !important; }')
html = html.replace(r'#achievements { z-index: 40; background-color: #a01818 !important; }', r'#achievements { z-index: 40; background-color: var(--thunderbird-red) !important; color: var(--lavender-blush) !important; }')
html = html.replace(r'#education { z-index: 50; background-color: var(--dragonfly-red) !important; }', r'#education { z-index: 50; background-color: var(--midnight-navy) !important; color: var(--lavender-blush) !important; }')
html = html.replace(r'#certs { z-index: 60; background-color: var(--dragonfly-red) !important; }', r'#certs { z-index: 60; background-color: var(--midnight-navy) !important; color: var(--lavender-blush) !important; }')
html = html.replace(r'#info { z-index: 70; background-color: var(--white) !important; }', r'#info { z-index: 70; background-color: var(--lavender-blush) !important; color: var(--midnight-navy) !important; }')

# 7. Card Colors
html = html.replace(r'background: #ff7a00;', r'background: var(--midnight-navy); border: 2px solid var(--thunderbird-red);')
html = html.replace(r'background: var(--dragonfly-red);', r'background: var(--thunderbird-red);')

# 8. Contact Accents
html = html.replace(r'color: var(--dragonfly-red);', r'color: var(--thunderbird-red);')

# 9. Inline HTML styling (About, Achievements, Education, Certs)
html = html.replace(r'style="background: var(--white); color: var(--dragonfly-red);', r'style="background: var(--lavender-blush); color: var(--midnight-navy);')
html = html.replace(r'background: #a01818;', r'background: var(--thunderbird-red);')
html = html.replace(r'color: #ffcccc;', r'color: var(--lavender-blush); opacity: 0.8;')

# 10. Increase padding on sticky sections for "generous white space" 
html = html.replace(r'padding: 100px 10%;', r'padding: 150px 10%;')

with open(r'd:\CV PORTFOLIO\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

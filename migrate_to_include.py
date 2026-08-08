from pathlib import Path
import re

root = Path('.')
html_files = sorted(root.glob('*.html'))
nav_pattern = re.compile(r'<nav[\s\S]*?</nav>', re.I)
body_pattern = re.compile(r'(<body[^>]*>)', re.I)
placeholder = '<div id="site-header"></div>\n<script src="loadHeader.js"></script>'
modified = []
for path in html_files:
    text = path.read_text(encoding='utf-8')
    new_text, count = nav_pattern.subn(placeholder, text, count=1)
    if count == 0:
        # insert after <body>
        m = body_pattern.search(text)
        if m:
            new_text = text[:m.end()] + '\n' + placeholder + text[m.end():]
        else:
            new_text = placeholder + '\n' + text
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        modified.append(path.name)
print('modified', modified)

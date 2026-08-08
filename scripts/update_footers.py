import re
import glob
import pathlib

html_files = glob.glob('*.html')
footer_count = 0
skipped = 0
for path in html_files:
    text = pathlib.Path(path).read_text(encoding='utf-8')
    if 'id="site-footer"' in text or 'loadFooter.js' in text:
        skipped += 1
        continue
    matches = list(re.finditer(r'<footer[\s\S]*?</footer>', text, re.IGNORECASE))
    if not matches:
        print('no footer', path)
        continue
    last = matches[-1]
    new_text = text[:last.start()] + '<div id="site-footer"></div>\n  <script src="loadFooter.js"></script>\n' + text[last.end():]
    pathlib.Path(path).write_text(new_text, encoding='utf-8')
    footer_count += 1
print('updated', footer_count, 'skipped', skipped)

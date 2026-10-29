import sys, os
from playwright.sync_api import sync_playwright
w = int(sys.argv[1]); files = sys.argv[2:]
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': w, 'height': 1000})
    for f in files:
        pg.route('**/fonts.googleapis.com/**', lambda r: r.abort())
        pg.goto('file://' + os.path.abspath(f)); pg.wait_for_timeout(200)
        ov = pg.evaluate("() => document.documentElement.scrollWidth - innerWidth")
        pg.screenshot(path=f.replace('.html', '.png'), full_page=True)
        print(f, 'h-overflow', ov, 'height', pg.evaluate('document.documentElement.scrollHeight'))
    b.close()

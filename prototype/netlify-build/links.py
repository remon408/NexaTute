import asyncio, os, re, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import checks
from playwright.async_api import async_playwright
BASE = checks.BASE

def static_refs():
    bad = []; n = 0
    for f in sorted(os.listdir(checks.PROJ)):
        if not f.endswith('.dc.html'): continue
        s = open(os.path.join(checks.PROJ, f), encoding='utf-8').read()
        for stem in re.findall(r"([A-Z]\d\d-[\w-]+|Main|W00-Website-Preview)\.dc\.html", s):
            n += 1
            page = 'index.html' if stem == 'W00-Website-Preview' else stem + '.html'
            if not os.path.exists(os.path.join(checks.SITE, page)): bad.append((f, stem))
    return n, bad

async def main():
    n, bad = static_refs(); print('source .dc.html references', n, 'missing targets', bad)
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); ctx = await b.new_context(viewport={'width': 1440, 'height': 900}); page = await ctx.new_page()
        errs = []; checks.attach(page, errs)
        # every rendered internal link on every page resolves to an existing file
        missing = set(); total = 0
        for stem, p in sorted(checks.PAGES.items()):
            await page.goto(BASE + p['page'], wait_until='load'); await page.wait_for_timeout(600)
            fr = checks.board_frame(page, stem)
            hrefs = await fr.evaluate("() => [...document.querySelectorAll('a[href]')].map(a => [a.href, a.target])")
            for h, tg in hrefs:
                if h.startswith(BASE):
                    total += 1
                    path = h[len(BASE):].split('#')[0].split('?')[0]
                    if path and not os.path.exists(os.path.join(checks.SITE, path)): missing.add((stem, path))
                    if p['framed'] and path.endswith('.html') and not path.startswith('frames/') and tg != '_top' and 'dcx-all' not in h: missing.add((stem, 'no _top: ' + path))
        print('rendered internal links', total, 'missing', sorted(missing)[:10])
        # 1. index card -> prototype page
        await page.goto(BASE + 'index.html', wait_until='load'); await page.wait_for_timeout(800)
        await page.locator('a.card[href="X05-Prototype-Flow5.html"]').first.click()
        await page.wait_for_load_state('load'); await page.wait_for_timeout(800)
        print('index card ->', page.url[len(BASE):], 'frame ok:', checks.board_frame(page, 'X05-Prototype-Flow5') is not None)
        # 2. hash link in index scrolls
        await page.goto(BASE + 'index.html', wait_until='load'); await page.wait_for_timeout(800)
        y0 = await page.evaluate('scrollY')
        await page.locator('a[href="#admin"]').first.click(); await page.wait_for_timeout(500)
        print('index #admin scroll', y0, '->', await page.evaluate('scrollY'), 'url', page.url[len(BASE):])
        # 3. fill page artboard link X10 -> X21
        await page.goto(BASE + 'X10-Prototype-Admin.html', wait_until='load'); await page.wait_for_timeout(800)
        loc = page.locator('a[href="X21-Prototype-Comms.html"]')
        cnt = await loc.count()
        if cnt:
            await loc.first.scroll_into_view_if_needed(); await loc.first.click(); await page.wait_for_load_state('load'); await page.wait_for_timeout(600)
        print('X10 link count', cnt, '->', page.url[len(BASE):])
        # 4. framed board link: Main (iframe) -> X01 opens at top level
        await page.goto(BASE + 'Main.html', wait_until='load'); await page.wait_for_timeout(800)
        fr = checks.board_frame(page, 'Main')
        l2 = fr.locator('a[href="../X01-Prototype-Flow1.html"]')
        print('Main has X01 link', await l2.count(), 'target', await l2.first.get_attribute('target'))
        await l2.first.click(); await page.wait_for_load_state('load'); await page.wait_for_timeout(800)
        print('Main frame link ->', page.url[len(BASE):])
        # 5. X01 (framed) -> X02 link inside the prototype (may sit on a later screen: use DOM click if hidden)
        fr = checks.board_frame(page, 'X01-Prototype-Flow1')
        hx = await fr.evaluate("() => [...document.querySelectorAll('a[href]')].map(a => a.getAttribute('href')).filter(h => /X0\\d/.test(h))")
        print('X01 visible board links on first screen', hx)
        # 6. All pages link
        await page.goto(BASE + 'X23-Prototype-AvatarVoice-User.html', wait_until='load'); await page.wait_for_timeout(600)
        await page.locator('a.dcx-all').click(); await page.wait_for_load_state('load')
        print('All pages ->', page.url[len(BASE):])
        await page.goto(BASE + 'D05-Admin-Overview.html', wait_until='load'); await page.wait_for_timeout(5200)
        bb = await page.locator('a.dcx-all').bounding_box()
        await page.screenshot(path=os.path.join(checks.CHK, 'allpages_folded.png'), clip={'x': 0, 'y': 800, 'width': 400, 'height': 100})
        await page.locator('a.dcx-all').hover(); await page.wait_for_timeout(400)
        bb2 = await page.locator('a.dcx-all').bounding_box()
        print('All pages folded box', bb, 'hover box', bb2)
        await page.locator('a.dcx-all').click(); await page.wait_for_load_state('load')
        print('All pages (fill) ->', page.url[len(BASE):])
        print('errors', errs)
        await b.close()
asyncio.run(main())

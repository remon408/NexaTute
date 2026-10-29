"""For boards where the click test skips many controls: try a real click, else dispatch a click event; report errors."""
import asyncio, sys, os, checks
from playwright.async_api import async_playwright
async def one(b, stem):
    page = await b.new_page(viewport={'width': 1440, 'height': 900}); errs = []; checks.attach(page, errs)
    url = checks.BASE + stem + '.html'
    await page.goto(url); await page.wait_for_timeout(1200)
    real = disp = navs = 0; seen = []; why = {}
    for step in range(80):
        cands = await page.evaluate(checks.CANDS, {'seen': seen})
        if not cands or real + disp >= 60: break
        c = cands[0]; seen.append(c['sig'])
        h = await page.evaluate_handle('(i) => document.querySelectorAll("#dc-root *")[i]', c['idx']); el = h.as_element()
        try:
            await el.scroll_into_view_if_needed(timeout=1200); await el.click(timeout=1200); real += 1
        except Exception as e:
            m = str(e); k = 'intercepts' if 'intercepts pointer' in m else ('not stable' if 'not stable' in m else ('not visible' if 'not visible' in m else 'other'))
            why[k] = why.get(k, 0) + 1
            if k == 'intercepts' and why[k] <= 2:
                ln = [x for x in m.split('\n') if 'intercepts' in x]; print('   ', stem, c['sig'][:50], '|', ln[0].strip()[:160] if ln else '')
            await page.evaluate('(i) => { const e = document.querySelectorAll("#dc-root *")[i]; e && e.dispatchEvent(new MouseEvent("click", {bubbles: true, cancelable: true})); }', c['idx']); disp += 1
        await page.wait_for_timeout(120)
        if page.url.split('#')[0] != url: navs += 1; await page.goto(url); await page.wait_for_timeout(800)
    await page.screenshot(path=os.path.join(checks.CHK, 'interact', stem + '.sweep.png'))
    bad = [e for e in errs if 'ERR_ABORTED' not in e]
    print(stem, 'real', real, 'dispatched', disp, 'navs', navs, 'why', why, 'errors', bad[:5])
    await page.close()
async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        for s in sys.argv[1:]: await one(b, s)
        await b.close()
asyncio.run(main())

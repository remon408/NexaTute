import asyncio, checks
from playwright.async_api import async_playwright
JS = """async (n) => { const t = []; for (let i = 0; i < n; i++) { const s = performance.now(); window.scrollBy(0, 300);
  await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))); t.push(performance.now() - s); } t.sort((a, b) => a - b); return {median: +t[n >> 1].toFixed(1), p90: +t[Math.floor(n * .9)].toFixed(1)}; }"""
async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        for stem, w in [('X26-Prototype-AdminRules', 390), ('X20-Prototype-Landing', 1440), ('X10-Prototype-Admin', 1440)]:
            for keep in (True, False):
                page = await b.new_page(viewport={'width': w, 'height': 844})
                if not keep: await page.route('**/dcx-all.js', lambda r: r.fulfill(body='', content_type='text/javascript'))
                await page.goto(checks.BASE + stem + '.html'); await page.wait_for_timeout(1500)
                print(stem, w, 'with tab script' if keep else 'without      ', await page.evaluate(JS, 40))
                await page.close()
        # where the tab had no free spot
        await b.close()
asyncio.run(main())

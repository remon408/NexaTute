import asyncio, checks
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); page = await b.new_page(viewport={'width':1440,'height':900}); errs=[]; checks.attach(page, errs)
        for u in ['X20-Prototype-Landing.html','X01-Prototype-Flow1.html']:
            await page.goto(checks.BASE+u); await page.wait_for_timeout(1000)
            await page.evaluate("() => document.getElementById('dc-root').__k.__k[0].__c.setState({lang:'ur'})"); await page.wait_for_timeout(300)
            await page.evaluate('document.fonts.ready'); await page.wait_for_timeout(800)
            st = await page.evaluate("() => [...document.fonts].filter(f => f.status === 'loaded' && /Nastaliq/.test(f.family)).map(f => f.family + ' ' + f.weight)")
            d = await page.evaluate(checks.ROOT_DIR)
            print(u, 'ur ->', d, sorted(set(st)))
        print('errors', errs)
        await b.close()
asyncio.run(main())

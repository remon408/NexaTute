import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); page = await b.new_page()
        reqs=[]; page.on('request', lambda r: reqs.append(r.url) if '/fonts/' in r.url else None)
        for u in ['index.html','X20-Prototype-Landing.html','frames/P01-PlayBoom-1.html','X24-Prototype-Legal.html','X27-Prototype-CoAdmin.html']:
            await page.goto('http://127.0.0.1:8765/nexatute-mockups/'+u); await page.evaluate('document.fonts.ready'); await page.wait_for_timeout(500)
            st = await page.evaluate("() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight)")
            print(u, sorted(set(st)))
        print(len(reqs), 'font requests, e.g.', reqs[:3])
        await b.close()
asyncio.run(main())

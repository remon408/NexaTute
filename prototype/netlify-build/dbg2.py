import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); page = await b.new_page(viewport={'width':1440,'height':900})
        await page.goto('http://127.0.0.1:8765/nexatute-mockups/D05-Admin-Overview.html'); await page.wait_for_timeout(5500)
        print(await page.evaluate("""() => { const l = document.querySelector('a.dcx-all .dcx-lbl'); const cs = getComputedStyle(l);
          return {anim: cs.animationName, dur: cs.animationDuration, mw: cs.maxWidth, w: l.getBoundingClientRect().width, anims: document.getAnimations().map(a => a.animationName + ':' + a.playState + ':' + a.currentTime)}; }"""))
        await b.close()
asyncio.run(main())

import asyncio
from playwright.async_api import async_playwright
O='/tmp/claude-0/-home-claude/9878cfdb-4647-5257-a0fe-47a0a28067df/scratchpad/s2/netlify/checks/'
async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); page = await b.new_page(viewport={'width':1440,'height':900})
        await page.goto('http://127.0.0.1:8765/nexatute-mockups/X20-Prototype-Landing.html'); await page.wait_for_timeout(6000)
        await page.screenshot(path=O+'x20_ltr_corner.png', clip={'x':0,'y':700,'width':700,'height':200})
        await page.evaluate("() => { const h = document.getElementById('dc-root'); h.__k.__k[0].__c.setState({lang:'ar'}); }")
        await page.wait_for_timeout(600)
        await page.screenshot(path=O+'x20_rtl_corner.png', clip={'x':0,'y':700,'width':700,'height':200})
        await b.close()
asyncio.run(main())

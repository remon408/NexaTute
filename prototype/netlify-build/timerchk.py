import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); page = await b.new_page()
        await page.goto('http://127.0.0.1:8765/nexatute-mockups/X01-Prototype-Flow1.html'); await page.wait_for_timeout(500)
        await page.evaluate("() => document.getElementById('dc-root').__k.__k[0].__c.setState({screen:'signup', sent:true, sec:30})")
        await page.wait_for_timeout(300)
        a = await page.evaluate("() => document.getElementById('dc-root').__k.__k[0].__c.state.sec")
        t1 = await page.evaluate("() => document.getElementById('dc-root').innerText.match(/\\d+/g)")
        await page.wait_for_timeout(3100)
        c = await page.evaluate("() => document.getElementById('dc-root').__k.__k[0].__c.state.sec")
        print('X01 OTP countdown sec', a, '->', c)
        await b.close()
asyncio.run(main())

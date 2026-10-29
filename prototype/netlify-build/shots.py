import sys, asyncio
from playwright.async_api import async_playwright
BASE='http://127.0.0.1:8765/nexatute-mockups/'
OUT='/tmp/claude-0/-home-claude/9878cfdb-4647-5257-a0fe-47a0a28067df/scratchpad/s2/netlify/checks/page_'
async def main(w, h, pages):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx = await b.new_context(viewport={'width':w,'height':h})
        page = await ctx.new_page()
        for pg in pages:
            await page.goto(BASE+pg, wait_until='load'); await page.wait_for_timeout(1500)
            await page.screenshot(path=OUT+'%s_%d.png'%(pg.replace('.html',''), w))
        await b.close()
asyncio.run(main(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3:]))

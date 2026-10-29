import sys, asyncio, json
from playwright.async_api import async_playwright
BASE='http://127.0.0.1:8765/nexatute-mockups/'
async def main(pages):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for pg in pages:
            ctx = await b.new_context(viewport={'width':1440,'height':900})
            page = await ctx.new_page()
            errs=[]
            page.on('console', lambda m: errs.append(m.type+': '+m.text) if m.type in ('error','warning') else None)
            page.on('pageerror', lambda e: errs.append('pageerror: '+str(e)))
            page.on('response', lambda r: errs.append('HTTP %d %s'%(r.status,r.url)) if r.status>=400 else None)
            page.on('requestfailed', lambda r: errs.append('FAILED '+r.url))
            await page.goto(BASE+pg, wait_until='load')
            await page.wait_for_timeout(1500)
            texts=[]
            for fr in page.frames:
                t = await fr.evaluate("document.body ? document.body.innerText.length + ':' + (document.body.innerText.indexOf('{{')>=0) : 'nobody'")
                texts.append(t)
            await page.screenshot(path='/tmp/claude-0/-home-claude/9878cfdb-4647-5257-a0fe-47a0a28067df/scratchpad/s2/netlify/checks/smoke_'+pg.replace('/','_')+'.png')
            print(pg, texts, errs[:8])
            await ctx.close()
        await b.close()
asyncio.run(main(sys.argv[1:]))

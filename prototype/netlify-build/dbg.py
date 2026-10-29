import asyncio, sys
sys.path.insert(0, '/tmp/claude-0/-home-claude/9878cfdb-4647-5257-a0fe-47a0a28067df/scratchpad/s2/netlify/build')
import checks
from playwright.async_api import async_playwright
async def main(stem):
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); ctx = await b.new_context(viewport={'width':1440,'height':900}); page = await ctx.new_page()
        errs=[]; checks.attach(page, errs)
        await page.goto(checks.BASE + checks.PAGES[stem]['page']); await page.wait_for_timeout(1000)
        fr = checks.board_frame(page, stem); seen=[]
        for step in range(15):
            cands = await fr.evaluate(checks.CANDS, {'seen': seen})
            if not cands: print('no more'); break
            c = cands[0]; seen.append(c['sig'])
            h = await fr.evaluate_handle('(i) => document.querySelectorAll("#dc-root *")[i]', c['idx'])
            try:
                await h.as_element().click(timeout=1500); r='ok'
            except Exception as e:
                r = 'skip: ' + str(e).split('\n')[0][:150] + ' | ' + ' '.join(l.strip() for l in str(e).split('\n')[-4:])[:300]
            print(step, c['sig'][:70], '->', r)
            await page.wait_for_timeout(150)
        print(errs)
        await b.close()
asyncio.run(main(sys.argv[1]))

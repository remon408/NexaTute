"""X20 at 1440: header menu link -> one compact sticky bar, section heading below it; compact logo -> back to top."""
import asyncio, os, checks
from playwright.async_api import async_playwright
STATE = """(id) => { const vis = e => { if (!e) return false; const cs = getComputedStyle(e), r = e.getBoundingClientRect(); return cs.display !== 'none' && cs.visibility !== 'hidden' && +cs.opacity > 0.05 && r.height > 2 && r.bottom > 0 && r.top < innerHeight; };
  const hd = document.querySelector('#dc-root header#top'), hdr = hd.querySelector('.hdr'), loc = hd.querySelector('.loc'), sn = hd.querySelector('.snav');
  const bars = [hdr, sn].filter(vis); const bar = bars[0];
  const sec = id ? document.getElementById(id) : null, hh = sec ? (sec.querySelector('h2') || sec.querySelector('h1,h3')) : null;
  const bb = bar ? bar.getBoundingClientRect() : null, hb = hh ? hh.getBoundingClientRect() : null;
  const sl = sn ? [...sn.querySelectorAll('a, button')].filter(vis).map(e => (e.textContent || e.getAttribute('aria-label') || '').trim().slice(0, 18)) : [];
  return { y: Math.round(scrollY), hdCls: hd.className, mainRow: vis(hdr), strip: vis(loc), compact: vis(sn), visibleBars: bars.length,
    barTop: bb && Math.round(bb.top), barBottom: bb && Math.round(bb.bottom), barH: bb && Math.round(bb.height),
    headTop: hb && Math.round(hb.top), headText: hh && hh.textContent.trim().slice(0, 30), compactItems: sl }; }"""
async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); page = await b.new_page(viewport={'width': 1440, 'height': 900})
        errs = []; checks.attach(page, errs); ok = []
        await page.goto(checks.BASE + 'X20-Prototype-Landing.html'); await page.wait_for_timeout(1500)
        s0 = await page.evaluate(STATE, None); print('start  ', s0)
        for sec in ['courses', 'plans', 'institutions']:
            await page.goto(checks.BASE + 'X20-Prototype-Landing.html'); await page.wait_for_timeout(1200)
            await page.locator('#dc-root header#top .hdr nav.nav a[href="#%s"]' % sec).first.click()
            await page.wait_for_timeout(1800)
            s = await page.evaluate(STATE, sec)
            good = s['y'] > 200 and s['visibleBars'] == 1 and s['compact'] and not s['mainRow'] and not s['strip'] and s['headTop'] is not None and s['headTop'] >= s['barBottom'] and s['headTop'] < 900
            ok.append(good); print('OK ' if good else 'BAD', '#' + sec, s)
            await page.screenshot(path=os.path.join(checks.CHK, 'x20_hdr_%s.png' % sec))
        # scroll a bit further by wheel: still one bar
        await page.mouse.wheel(0, 1500); await page.wait_for_timeout(800)
        s = await page.evaluate(STATE, None); good = s['visibleBars'] == 1 and s['compact']; ok.append(good); print('OK ' if good else 'BAD', 'wheel', s)
        # compact bar logo -> back to the top
        await page.locator('#dc-root header#top .snav a[href="#top"]').first.click(); await page.wait_for_timeout(1800)
        s = await page.evaluate(STATE, None)
        good = s['y'] < 5 and s['mainRow'] and not s['compact'] and s['visibleBars'] == 1; ok.append(good); print('OK ' if good else 'BAD', 'logo->top', s)
        await page.screenshot(path=os.path.join(checks.CHK, 'x20_hdr_top.png'))
        # below 1024 the old behaviour (not part of this fix) — just record
        await page.set_viewport_size({'width': 900, 'height': 900}); await page.goto(checks.BASE + 'X20-Prototype-Landing.html'); await page.wait_for_timeout(1000)
        await page.mouse.wheel(0, 2500); await page.wait_for_timeout(800)
        print('info 900px scrolled', await page.evaluate(STATE, None))
        print('HDR checks', len(ok), 'bad', ok.count(False), 'errors', errs)
        await b.close()
asyncio.run(main())

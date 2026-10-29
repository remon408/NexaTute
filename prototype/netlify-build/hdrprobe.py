import asyncio, checks
from playwright.async_api import async_playwright
PROBE = """() => { const vis = e => { const cs = getComputedStyle(e), r = e.getBoundingClientRect(); return cs.display !== 'none' && cs.visibility !== 'hidden' && +cs.opacity > 0.05 && r.height > 2 && r.bottom > 0 && r.top < innerHeight; };
  const hd = document.querySelector('#dc-root header#top'); const out = {hdCls: hd.className, scrollY: scrollY, hd: hd.getBoundingClientRect().toJSON()};
  out.kids = [...hd.querySelectorAll(':scope > *, :scope > * > *')].map(e => ({tag: e.tagName, cls: e.className, vis: vis(e), top: Math.round(e.getBoundingClientRect().top), h: Math.round(e.getBoundingClientRect().height)}));
  out.navs = [...document.querySelectorAll('#dc-root nav')].map(e => ({cls: e.className, aria: e.getAttribute('aria-label'), vis: vis(e), top: Math.round(e.getBoundingClientRect().top), h: Math.round(e.getBoundingClientRect().height), pos: getComputedStyle(e.closest('[class]')).position}));
  out.logos = [...document.querySelectorAll('#dc-root .logo')].map(e => ({vis: vis(e), top: Math.round(e.getBoundingClientRect().top), href: e.getAttribute('href'), par: e.parentElement.className}));
  return out; }"""
async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); page = await b.new_page(viewport={'width': 1440, 'height': 900})
        await page.goto(checks.BASE + 'X20-Prototype-Landing.html'); await page.wait_for_timeout(1500)
        import json; print(json.dumps(await page.evaluate(PROBE), ensure_ascii=False)[:3000])
        links = await page.evaluate("() => [...document.querySelectorAll('#dc-root header#top a[href^=\"#\"]')].map(a => [a.getAttribute('href'), a.textContent.trim().slice(0,20), a.getBoundingClientRect().width > 0])")
        print(links)
        await b.close()
asyncio.run(main())

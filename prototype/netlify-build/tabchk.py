"""Checks the floating "All pages" tab: folded at start, never over the page's own controls / fixed bars (also while
scrolling and in the first second), 44 px hit area, label on hover and keyboard focus, RTL side, hidden in print.
usage: tabchk.py detail | sweep [stems...]"""
import asyncio, json, os, sys
import checks
from playwright.async_api import async_playwright

B = checks.BASE
# independent overlap probe: look under the tab (tab made click-through for the probe) on a 4 px grid
UNDER = """() => { const a = document.querySelector('a.dcx-all'); if (!a) return {none: true};
  const cs = getComputedStyle(a); if (cs.display === 'none' || a.classList.contains('dcx-off') || !a.classList.contains('dcx-ready') || +cs.opacity < 0.05) return {off: true, cls: a.className, ready: a.classList.contains('dcx-ready')};
  const R = a.getBoundingClientRect(); const pe = a.style.pointerEvents; a.style.pointerEvents = 'none';
  const SEL = 'a[href],button,input,select,textarea,summary,label,[role=button],[role=link],[role=tab],[role=switch],[role=checkbox],[role=radio],[tabindex]:not([tabindex="-1"])';
  const click = n => { if (!(n.l && Object.keys(n.l).some(k => /^(click|pointerdown|mousedown)/.test(k)))) return false;
    const r = n.getBoundingClientRect(), w = n.ownerDocument.defaultView; return r.width * r.height < 0.3 * w.innerWidth * w.innerHeight || !n.querySelector(SEL); };
  const hits = new Set();
  function probe(doc, win, x, y, ox, oy, s) {
    const e = doc.elementFromPoint(x, y); if (!e) return;
    if (e.tagName === 'IFRAME') { const d = e.contentDocument; if (!d) return; const r = e.getBoundingClientRect(), k = r.width / e.offsetWidth || 1; probe(d, e.contentWindow, (x - r.left) / k, (y - r.top) / k); return; }
    for (let n = e; n && n.nodeType === 1 && n !== doc.body; n = n.parentElement) {
      const p = win.getComputedStyle(n).position;
      if (n.matches(SEL) || click(n)) { hits.add('control:' + n.tagName + '.' + String(n.className).slice(0, 30) + ' "' + (n.textContent || '').trim().slice(0, 24) + '"'); return; }
      if (p === 'fixed' || p === 'sticky') { const r = n.getBoundingClientRect(); if (r.width * r.height < 0.85 * win.innerWidth * win.innerHeight) hits.add('bar:' + n.tagName + '.' + String(n.className).slice(0, 30)); return; }
    } }
  for (let y = R.top + 1; y < R.bottom; y += 4) for (let x = R.left + 1; x < R.right; x += 4) if (x >= 0 && y >= 0 && x < innerWidth && y < innerHeight) probe(document, window, x, y);
  a.style.pointerEvents = pe;
  const lbl = a.querySelector('.dcx-lbl');
  return {x: Math.round(R.left), y: Math.round(R.top), w: Math.round(R.width), h: Math.round(R.height), right: Math.round(innerWidth - R.right),
    lblW: Math.round(lbl.getBoundingClientRect().width), cls: a.className, over: [...hits]}; }"""


def bad(u):
    return bool(u.get('over'))


async def detail(b):
    out = []
    cases = [('X20-Prototype-Landing', 1440, 900), ('X20-Prototype-Landing', 390, 844), ('X01-Prototype-Flow1', 1440, 900),
             ('X01-Prototype-Flow1', 390, 844), ('X27-Prototype-CoAdmin', 1440, 900), ('X27-Prototype-CoAdmin', 390, 844),
             ('L05-AI-Teacher', 1440, 900), ('P01-PlayBoom-1', 390, 844)]
    for stem, w, h in cases:
        page = await b.new_page(viewport={'width': w, 'height': h})
        errs = []; checks.attach(page, errs)
        p = checks.PAGES[stem]
        await page.goto(B + p['page'], wait_until='commit')
        tl = []
        for t in (150, 400, 800, 1500, 3000):  # the first seconds
            await page.wait_for_timeout(t - (tl[-1][0] if tl else 0))
            try:
                u = await page.evaluate(UNDER)
            except Exception as e:
                u = {'err': str(e)[:80]}
            tl.append((t, u))
        u0 = tl[-1][1]
        first_bad = [t for t, u in tl if bad(u)]
        shot = os.path.join(checks.CHK, 'tab_%s_%d.png' % (stem, w)); await page.screenshot(path=shot)
        # scroll through the page (fill pages scroll the window; shells too)
        sc_bad = []; n = 0
        H = await page.evaluate('document.documentElement.scrollHeight')
        for k in range(0, 14):
            y = int(k * max(0, H - h) / 13)
            await page.evaluate('(y) => window.scrollTo(0, y)', y); await page.wait_for_timeout(160); n += 1
            u = await page.evaluate(UNDER)
            if bad(u): sc_bad.append((y, u['over'][:2]))
        await page.evaluate('window.scrollTo(0, 0)'); await page.wait_for_timeout(300)
        # hover -> label; keyboard focus -> label
        a = page.locator('a.dcx-all')
        await a.hover(); await page.wait_for_timeout(350)
        lh = await page.evaluate("() => Math.round(document.querySelector('a.dcx-all .dcx-lbl').getBoundingClientRect().width)")
        await page.mouse.move(w / 2, h / 2); await page.keyboard.press('Shift')
        await page.evaluate("() => document.querySelector('a.dcx-all').focus()"); await page.wait_for_timeout(350)
        fk = await page.evaluate("() => { const a = document.querySelector('a.dcx-all'); return {fv: a.matches(':focus-visible'), lbl: Math.round(a.querySelector('.dcx-lbl').getBoundingClientRect().width), op: getComputedStyle(a).opacity}; }")
        await page.evaluate("() => document.activeElement.blur()")
        await page.emulate_media(media='print'); pd = await page.evaluate("getComputedStyle(document.querySelector('a.dcx-all')).display"); await page.emulate_media(media='screen')
        r = {'case': '%s@%d' % (stem, w), 'start': {k: u0.get(k) for k in ('x', 'y', 'w', 'h', 'right', 'lblW', 'cls')},
             'firstSecondsOver': first_bad, 'scrollPositions': n, 'scrollOver': sc_bad[:3], 'hoverLbl': lh, 'kbd': fk, 'print': pd, 'errors': errs[:3]}
        ok = (not first_bad and not sc_bad and u0.get('w', 0) >= 44 and u0.get('h', 0) >= 44 and u0.get('lblW', 99) == 0
              and lh > 60 and fk['fv'] and fk['lbl'] > 60 and pd == 'none' and not errs)
        print('OK ' if ok else 'BAD', json.dumps(r, ensure_ascii=False))
        out.append(ok)
        await page.close()
    # RTL: X20 / X27 in Arabic -> tab on the right edge, arrow mirrored; back to bn -> left
    for stem in ['X20-Prototype-Landing', 'X27-Prototype-CoAdmin', 'X01-Prototype-Flow1']:
        page = await b.new_page(viewport={'width': 1440, 'height': 900}); errs = []; checks.attach(page, errs)
        await page.goto(B + stem + '.html'); await page.wait_for_timeout(1200)
        await page.evaluate("() => document.getElementById('dc-root').__k.__k[0].__c.setState({lang: 'ar'})"); await page.wait_for_timeout(700)
        ua = await page.evaluate(UNDER)
        await page.evaluate("() => document.getElementById('dc-root').__k.__k[0].__c.setState({lang: 'bn'})"); await page.wait_for_timeout(700)
        ub = await page.evaluate(UNDER)
        ok = ua.get('right') == 0 and 'dcx-rtl' in ua.get('cls', '') and not bad(ua) and ub.get('x') == 0 and not bad(ub) and not errs
        print('OK ' if ok else 'BAD', 'RTL', stem, 'ar:', {k: ua.get(k) for k in ('x', 'right', 'y', 'cls', 'over')}, 'bn:', {k: ub.get(k) for k in ('x', 'y', 'cls')}, errs[:2])
        out.append(ok)
        await page.close()
    # click the tab -> index; W00 (index) has no tab
    page = await b.new_page(viewport={'width': 390, 'height': 844}); errs = []; checks.attach(page, errs)
    await page.goto(B + 'X20-Prototype-Landing.html'); await page.wait_for_timeout(1200)
    await page.locator('a.dcx-all').click(); await page.wait_for_load_state('load'); await page.wait_for_timeout(800)
    ok = page.url.endswith('/index.html') and (await page.locator('a.dcx-all').count()) == 0 and not errs
    print('OK ' if ok else 'BAD', 'tab click -> index; W00 has no tab', page.url[len(B):], errs[:2]); out.append(ok)
    await page.close()
    print('TAB detail checks', len(out), 'bad', out.count(False))


async def sweep_one(b, stem, w, h, sem, res):
    async with sem:
        page = await b.new_page(viewport={'width': w, 'height': h}); errs = []; checks.attach(page, errs)
        await page.goto(B + checks.PAGES[stem]['page']); await page.wait_for_timeout(1300)
        H = await page.evaluate('document.documentElement.scrollHeight')
        badl = []; offs = 0
        for k in range(0, 9):
            y = int(k * max(0, H - h) / 8)
            await page.evaluate('(y) => window.scrollTo(0, y)', y); await page.wait_for_timeout(140)
            u = await page.evaluate(UNDER)
            if u.get('off'): offs += 1; print('   hidden (no free spot):', stem, w, 'scrollY', y)
            if bad(u): badl.append((y, u['over'][:2]))
        res[(stem, w)] = (badl, offs, errs)
        await page.close()


async def sweep(b, stems):
    res = {}; sem = asyncio.Semaphore(4)
    await asyncio.gather(*[sweep_one(b, s, w, h, sem, res) for s in stems for (w, h) in ((1440, 900), (390, 844))])
    nb = 0; noff = 0
    for (s, w), (badl, offs, errs) in sorted(res.items()):
        noff += offs
        if badl or errs:
            nb += 1; print('BAD', s, w, badl[:3], errs[:2])
    print('TAB sweep pages', len(stems), 'x 2 widths x 9 scroll positions; bad', nb, '; positions with tab hidden (no free spot)', noff)


async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        if sys.argv[1] == 'detail':
            await detail(b)
        else:
            stems = sys.argv[2:] or [s for s in sorted(checks.PAGES) if s != 'W00-Website-Preview']
            await sweep(b, stems)
        await b.close()
asyncio.run(main())

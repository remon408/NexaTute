#!/usr/bin/env python3
"""Verification for the Netlify export. Needs the local server on :8765 rooted at SP/s2/netlify.
usage: checks.py load|visual|interact|links [stems...]"""
import asyncio, json, os, re, subprocess, sys
from playwright.async_api import async_playwright

SP = '/tmp/claude-0/-home-claude/9878cfdb-4647-5257-a0fe-47a0a28067df/scratchpad'
NET = os.path.join(SP, 's2', 'netlify')
SITE = os.path.join(NET, 'nexatute-mockups')
PROJ = os.path.join(SP, 'ntd', 'project')
CHK = os.path.join(NET, 'checks')
ROOT = 'http://127.0.0.1:8765/'
BASE = ROOT + 'nexatute-mockups/'
MAN = json.load(open(os.path.join(NET, 'build', 'manifest.json')))
PAGES = {p['stem']: p for p in MAN['pages']}
os.makedirs(CHK, exist_ok=True)


def attach(page, errs):
    page.on('console', lambda m: errs.append('%s: %s' % (m.type, m.text[:300])) if m.type in ('error', 'warning') else None)
    page.on('pageerror', lambda e: errs.append('pageerror: %s' % str(e)[:300]))
    page.on('response', lambda r: errs.append('HTTP %d %s' % (r.status, r.url)) if r.status >= 400 else None)
    page.on('requestfailed', lambda r: errs.append('FAILED %s %s' % (r.url, r.failure)))
    page.on('request', lambda r: errs.append('EXTERNAL %s' % r.url) if not r.url.startswith(ROOT) and not r.url.startswith('data:') and not r.url.startswith('about:') else None)


def board_frame(page, stem):
    p = PAGES[stem]
    if not p['framed']:
        return page.main_frame
    for f in page.frames:
        if f.url.endswith('/frames/%s.html' % stem):
            return f
    return None


TEXT_CHECK = """() => { const r = document.getElementById('dc-root'); if (!r) return {err: 'no root'};
  const t = r.innerText || ''; return {len: t.length, braces: t.indexOf('{{') >= 0 || (r.innerHTML.indexOf('{{') >= 0),
  mounted: !!window.__dcMounted, kids: r.childElementCount}; }"""


async def check_load(b, stem, sem, results):
    async with sem:
        p = PAGES[stem]
        ctx = await b.new_context(viewport={'width': 1440, 'height': 900})
        page = await ctx.new_page()
        errs = []
        attach(page, errs)
        await page.goto(BASE + p['page'], wait_until='load')
        await page.wait_for_timeout(2500)
        fr = board_frame(page, stem)
        info = await fr.evaluate(TEXT_CHECK) if fr else {'err': 'frame missing'}
        # mobile width too (375) — shell scaling / fluid layout must not error
        await page.set_viewport_size({'width': 375, 'height': 800})
        await page.wait_for_timeout(500)
        sw = await page.evaluate('document.documentElement.scrollWidth')
        results[stem] = {'page': p['page'], 'mode': p['mode'], 'errors': errs, 'info': info, 'scrollW375': sw}
        await ctx.close()


async def run_load(stems):
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        sem = asyncio.Semaphore(4)
        res = {}
        await asyncio.gather(*[check_load(b, s, sem, res) for s in stems])
        await b.close()
    bad = 0
    for s in stems:
        r = res[s]
        ok = not r['errors'] and r['info'].get('mounted') and not r['info'].get('braces') and r['info'].get('len', 0) > 0
        bad += not ok
        print('%-34s %-6s %s text=%s braces=%s sw375=%s %s' % (s, r['mode'], 'OK ' if ok else 'BAD', r['info'].get('len'), r['info'].get('braces'), r['scrollW375'], r['errors'][:5]))
    print('LOAD pages=%d bad=%d' % (len(stems), bad))
    json.dump(res, open(os.path.join(CHK, 'load.json'), 'w'), indent=1, ensure_ascii=False)


# ---------------- visual compare vs static renderer ----------------
def static_render(stem):
    out = os.path.join(CHK, 'static', stem + '.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    r = subprocess.run(['node', os.path.join(SP, 'dcrender.js'), os.path.join(PROJ, stem + '.dc.html'), out, '{}'], capture_output=True, text=True)
    if r.returncode != 0:  # reference renderer has no this.props; retry with a copy that supplies data-props defaults
        props = json.loads(re.search(r'DCRuntime.mount\((\{.*?\}), function', open(os.path.join(SITE, 'boards', stem + '.js'), encoding='utf-8').read().split('\n')[1]).group(1))['props']
        r = subprocess.run(['node', os.path.join(NET, 'build', 'dcrender_props.js'), os.path.join(PROJ, stem + '.dc.html'), out, '{}'], capture_output=True, text=True, env=dict(os.environ, DCPROPS=json.dumps(props)))
        r = subprocess.CompletedProcess(r.args, r.returncode, 'used props-copy of dcrender; ' + r.stdout, r.stderr)
    s = open(out, encoding='utf-8').read()
    s = re.sub(r'<link[^>]*fonts\.(googleapis|gstatic)\.com[^>]*>', '', s)
    s = s.replace('<head><meta charset="utf-8">', '<head><meta charset="utf-8"><link rel="stylesheet" href="/nexatute-mockups/fonts/fonts.css">', 1)
    if stem == 'W00-Website-Preview':
        src = open(os.path.join(PROJ, stem + '.dc.html'), encoding='utf-8').read()
        for k, hsh in re.findall(r"'([\w-]+)':\s*'/_blob/([0-9a-f]+)'", src):
            s = s.replace('/_blob/' + hsh, '/nexatute-mockups/thumbs/%s.webp' % k)
    open(out, 'w', encoding='utf-8').write(s)
    return (r.stdout + r.stderr).strip()


def diff_ratio(a, b, out):
    from PIL import Image, ImageChops
    ia, ib = Image.open(a).convert('RGB'), Image.open(b).convert('RGB')
    w, h = min(ia.width, ib.width), min(ia.height, ib.height)
    ia, ib = ia.crop((0, 0, w, h)), ib.crop((0, 0, w, h))
    d = ImageChops.difference(ia, ib).convert('L').point(lambda v: 255 if v > 40 else 0)
    n = d.histogram()[255]
    if n:
        bb = d.getbbox()
        d.save(out)
    else:
        bb = None
    return n / float(w * h), bb


async def visual_one(b, stem, sem, res):
    async with sem:
        p = PAGES[stem]
        note = static_render(stem)
        vw = p['w'] if p['framed'] else 1440
        vh = min(p['h'], 1100) if p['framed'] else 900
        ctx = await b.new_context(viewport={'width': vw, 'height': vh})
        page = await ctx.new_page()
        errs = []
        attach(page, errs)
        a = os.path.join(CHK, 'vis', stem + '.static.png')
        bpath = os.path.join(CHK, 'vis', stem + '.site.png')
        os.makedirs(os.path.dirname(a), exist_ok=True)
        await page.goto(ROOT + 'checks/static/%s.html' % stem, wait_until='load')
        await page.evaluate('document.fonts.ready')
        await page.wait_for_timeout(400)
        await page.screenshot(path=a)
        url = BASE + ('frames/%s.html' % stem if p['framed'] else p['page'])
        await page.goto(url, wait_until='load')
        await page.add_style_tag(content='a.dcx-all{display:none!important}')
        await page.evaluate('document.fonts.ready')
        await page.wait_for_timeout(400)
        await page.screenshot(path=bpath)
        await ctx.close()
        r, bb = diff_ratio(a, bpath, os.path.join(CHK, 'vis', stem + '.diff.png'))
        res[stem] = {'ratio': r, 'bbox': bb, 'static_note': note[:200], 'errs': [e for e in errs if 'checks/static' not in e][:3]}


async def run_visual(stems):
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        sem = asyncio.Semaphore(4)
        res = {}
        await asyncio.gather(*[visual_one(b, s, sem, res) for s in stems])
        await b.close()
    for s in stems:
        r = res[s]
        print('%-34s diff=%.4f bbox=%s %s %s' % (s, r['ratio'], r['bbox'], r['static_note'][:80], r['errs']))
    json.dump(res, open(os.path.join(CHK, 'visual.json'), 'w'), indent=1)


# ---------------- interaction ----------------
CANDS = """(state) => {
  const seen = new Set(state.seen || []);
  const out = [];
  const els = document.querySelectorAll('#dc-root *');
  let i = 0;
  for (const el of els) {
    i++;
    const l = el.l; const isA = el.tagName === 'A' && el.hasAttribute('href');
    const hasClick = l && Object.keys(l).some(k => k.indexOf('click') === 0);
    if (!hasClick && !isA) continue;
    if (isA) { const h = el.getAttribute('href') || ''; if (/^https?:|^mailto:|^tel:/.test(h) || /\\.html/.test(h)) continue; }
    const r = el.getBoundingClientRect(); if (r.width < 3 || r.height < 3) continue;
    const cs = getComputedStyle(el); if (cs.visibility === 'hidden' || cs.display === 'none' || cs.pointerEvents === 'none') continue;
    if (el.disabled) continue;
    const sig = el.tagName + '|' + (el.textContent || '').trim().slice(0, 40) + '|' + (el.getAttribute('aria-label') || '') + '|' + el.className;
    if (seen.has(sig)) continue;
    const cx = r.left + r.width / 2, cy = r.top + r.height / 2;
    const inView = cx >= 0 && cy >= 0 && cx < innerWidth && cy < innerHeight;
    if (inView) { const hit = document.elementFromPoint(cx, cy); if (!hit || !(hit === el || el.contains(hit))) continue; }
    out.push({ idx: i - 1, sig, inView });
    if (out.length > 60) break;
  }
  return out;
}"""

ROOT_DIR = """() => { const r = document.querySelector('#dc-root [lang][dir]') || document.querySelector('#dc-root [dir]'); return r ? r.getAttribute('dir') + '/' + getComputedStyle(r).direction : 'none'; }"""


async def click_by_index(fr, idx):
    h = await fr.evaluate_handle('(i) => document.querySelectorAll("#dc-root *")[i]', idx)
    el = h.as_element()
    if not el:
        return 'gone'
    try:
        await el.scroll_into_view_if_needed(timeout=1500)
        await el.click(timeout=1500)
        return 'ok'
    except Exception as e:
        return 'skip'


async def focus_test(page, fr):
    js = """() => { const els = [...document.querySelectorAll('#dc-root input, #dc-root textarea')];
      for (const [i, el] of els.entries()) { const t = (el.type || 'text');
        if (el.tagName === 'INPUT' && !/^(text|search|email|tel|url|number|password)$/.test(t)) continue;
        if (el.disabled || el.readOnly) continue; const r = el.getBoundingClientRect(); if (r.width < 3 || r.height < 3) continue;
        if (!el.l || !Object.keys(el.l).some(k => k.indexOf('input') === 0)) continue;
        el.setAttribute('data-focus-test', '1'); return {i, t, id: el.id, before: el.value}; } return null; }"""
    info = await fr.evaluate(js)
    if not info:
        return None
    loc = fr.locator('[data-focus-test="1"]').first
    try:
        await loc.click(timeout=2000)
    except Exception:
        await loc.scroll_into_view_if_needed(timeout=2000)
        await loc.focus()  # element still animating in (e.g. a sliding panel): focus it directly
    await loc.press('End')
    await page.keyboard.type('abc', delay=60)
    await page.wait_for_timeout(300)
    st = await fr.evaluate("""() => { const el = document.querySelector('[data-focus-test="1"]'); return {
        focused: document.activeElement === el, value: el ? el.value : null }; }""")
    if info.get('t') == 'number':
        ok = st['focused']
    else:
        ok = st['focused'] and st['value'] is not None and 'abc' in st['value']
    return {'ok': ok, 'id': info.get('id'), 'value': (st['value'] or '')[-30:], 'focused': st['focused']}


async def switch_lang(page, fr, target_label, cur_labels):
    """Try UI first: click visible element with exact text target_label; else open a language toggle."""
    find = """(label) => { const all = [...document.querySelectorAll('#dc-root *')];
      const els = all.filter(el => {
        const l = el.l; if (!l || !Object.keys(l).some(k => k.indexOf('click') === 0)) return false;
        const r = el.getBoundingClientRect(); if (r.width < 3 || r.height < 3) return false;
        const t = (el.textContent || '').trim(); if (t.indexOf(label) < 0 || t.length > label.length + 30) return false;
        const cx = r.left + r.width / 2, cy = r.top + r.height / 2;
        if (cx >= 0 && cy >= 0 && cx < innerWidth && cy < innerHeight) { const hit = document.elementFromPoint(cx, cy); if (!hit || !(hit === el || el.contains(hit))) return false; }
        return true; });
      els.sort((a, b) => (a.textContent.trim().length - b.textContent.trim().length));
      return els.length ? all.indexOf(els[0]) : -1; }"""
    sel = """(label) => { const s = [...document.querySelectorAll('#dc-root select')].find(s => { const ts = [...s.options].map(o => o.textContent.trim()); return ts.includes(label) && ts.some(t => t.indexOf('العربية') >= 0) && ts.some(t => t.indexOf('English') >= 0); });
      if (!s) return null; const o = [...s.options].find(o => o.textContent.trim() === label); return {i: [...document.querySelectorAll('#dc-root *')].indexOf(s), v: o.value}; }"""
    toggle = """(label) => { const all = [...document.querySelectorAll('#dc-root *')];
      const els = all.filter(el => el.l && Object.keys(el.l).some(k => k.indexOf('click') === 0) && (el.textContent || '').indexOf(label) >= 0
        && (el.textContent || '').trim().length < label.length + 12 && el.getBoundingClientRect().width > 3);
      return els.length ? all.indexOf(els[0]) : -1; }"""
    for attempt in range(2):
        idx = await fr.evaluate(find, target_label)
        if idx >= 0 and await click_by_index(fr, idx) == 'ok':
            await page.wait_for_timeout(300)
            return 'ui'
        opened = False
        for cl in cur_labels:
            ti = await fr.evaluate(toggle, cl)
            if ti >= 0 and await click_by_index(fr, ti) == 'ok':
                opened = True
                await page.wait_for_timeout(350)
                break
        if not opened:
            break
    s = await fr.evaluate(sel, target_label)
    if s:
        h = await fr.evaluate_handle('(i) => document.querySelectorAll("#dc-root *")[i]', s['i'])
        await h.as_element().select_option(s['v'])
        await page.wait_for_timeout(300)
        return 'ui-select'
    # fallback: set state on the root component instance
    code = {'English': 'en', 'العربية': 'ar', 'বাংলা': 'bn'}[target_label]
    await fr.evaluate("""(c) => { const host = document.getElementById('dc-root'); const v = host.__k && host.__k.__k && host.__k.__k[0];
        v.__c.setState({lang: c}); }""", code)
    await page.wait_for_timeout(300)
    return 'setState'


async def interact_one(b, stem, sem, res):
    try:
        await interact_one_(b, stem, sem, res)
    except Exception as e:
        res[stem] = {'clicks': -1, 'errors': ['CHECK FAILED: %s' % str(e)[:300]]}


async def interact_one_(b, stem, sem, res):
    async with sem:
        p = PAGES[stem]
        ctx = await b.new_context(viewport={'width': 1440, 'height': 900})
        page = await ctx.new_page()
        errs = []
        attach(page, errs)
        url = BASE + p['page']
        await page.goto(url, wait_until='load')
        await page.wait_for_timeout(1200)
        fr = board_frame(page, stem)
        out = {'clicks': 0, 'skipped': 0, 'navs': 0}
        # language: bn -> en -> ar (RTL) -> bn
        out['dir0'] = await fr.evaluate(ROOT_DIR)
        out['to_en'] = await switch_lang(page, fr, 'English', ['বাংলা', 'ভাষা'])
        out['dir_en'] = await fr.evaluate(ROOT_DIR)
        out['lang_en'] = await fr.evaluate("() => { const r = document.querySelector('#dc-root [lang]'); return r ? r.getAttribute('lang') : null; }")
        out['to_ar'] = await switch_lang(page, fr, 'العربية', ['English', 'Language'])
        out['dir_ar'] = await fr.evaluate(ROOT_DIR)
        out['braces'] = await fr.evaluate("() => document.getElementById('dc-root').innerText.indexOf('{{') >= 0")
        await page.screenshot(path=os.path.join(CHK, 'interact', stem + '.ar.png'))
        out['to_bn'] = await switch_lang(page, fr, 'বাংলা', ['العربية', 'اللغة'])
        out['dir_bn'] = await fr.evaluate(ROOT_DIR)
        await page.goto(url, wait_until='load')
        await page.wait_for_timeout(1000)
        fr = board_frame(page, stem)
        out['focus_first'] = await focus_test(page, fr)
        seen = []
        tries = {}
        for step in range(60):
            if out['clicks'] >= 40:
                break
            if fr.is_detached() or page.url.split('#')[0] != url:
                out['navs'] += 1
                await page.goto(url, wait_until='load')
                await page.wait_for_timeout(800)
                fr = board_frame(page, stem)
            cands = await fr.evaluate(CANDS, {'seen': seen})
            if not cands:
                break
            c = cands[0]
            r = await click_by_index(fr, c['idx'])
            if r == 'ok':
                out['clicks'] += 1
                seen.append(c['sig'])
            else:
                out['skipped'] += 1
                tries[c['sig']] = tries.get(c['sig'], 0) + 1
                if tries[c['sig']] >= 2:
                    seen.append(c['sig'])
            await page.wait_for_timeout(120)
        if fr.is_detached() or page.url.split('#')[0] != url:
            await page.goto(url, wait_until='load')
            await page.wait_for_timeout(800)
            fr = board_frame(page, stem)
        if not out['focus_first']:
            out['focus_after'] = await focus_test(page, fr)
        out['errors'] = errs
        res[stem] = out
        await ctx.close()


async def run_interact(stems):
    os.makedirs(os.path.join(CHK, 'interact'), exist_ok=True)
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        sem = asyncio.Semaphore(4)
        res = {}
        await asyncio.gather(*[interact_one(b, s, sem, res) for s in stems])
        await b.close()
    for s in stems:
        r = res[s]
        print(s, json.dumps({k: v for k, v in r.items() if k != 'errors'}, ensure_ascii=False), 'ERRORS:', r['errors'][:5])
    json.dump(res, open(os.path.join(CHK, 'interact.json'), 'w'), indent=1, ensure_ascii=False)


if __name__ == '__main__':
    mode = sys.argv[1]
    stems = sys.argv[2:] or sorted(PAGES)
    if mode == 'interact' and not sys.argv[2:]:
        stems = [s for s in sorted(PAGES) if s.startswith('X')]
    asyncio.run({'load': run_load, 'visual': run_visual, 'interact': run_interact}[mode](stems))

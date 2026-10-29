"""Cross-board hash navigation checks (X10<->X25<->X26, X20 -> X24 #legal/<id>, X24 -> X20 #cookie-settings)."""
import asyncio, checks
from playwright.async_api import async_playwright
B = checks.BASE
ST = "() => { const c = document.getElementById('dc-root').__k.__k[0].__c; const l = c.__dcLogic; return typeof l.st === 'function' ? l.st() : c.state; }"
LOGIC = "(a) => document.getElementById('dc-root').__k.__k[0].__c.__dcLogic.go20(a[0], a[1])"
def short(u): return u[len(B):] if u.startswith(B) else u
async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); page = await b.new_page(viewport={'width': 1440, 'height': 900})
        errs = []; checks.attach(page, errs); res = []
        async def go(u, wait=1500):
            await page.goto(B + u, wait_until='load'); await page.wait_for_timeout(wait)
        def rec(name, ok, info=''): res.append(ok); print('%-4s %-48s %s' % ('OK' if ok else 'BAD', name, info))
        # X10 deep links that belong to X25 / X26 are forwarded (location.replace keeps the hash)
        await go('X10-Prototype-Admin.html#plans')
        rec('X10#plans -> X25#plans', short(page.url) == 'X25-Prototype-AdminPlans.html#plans', short(page.url))
        s = await page.evaluate(ST); rec('  X25 opens plans section', s.get('sec') == 'plans', s.get('sec'))
        await go('X10-Prototype-Admin.html#plans/rules')
        rec('X10#plans/rules -> X26#plans/rules', short(page.url) == 'X26-Prototype-AdminRules.html#plans/rules', short(page.url))
        s = await page.evaluate(ST); rec('  X26 opens rules tab', s.get('sec') == 'plans' and s.get('p2Tab') == 'rules', '%s/%s' % (s.get('sec'), s.get('p2Tab')))
        await go('X25-Prototype-AdminPlans.html#acct')
        rec('X25#acct -> X10#acct', short(page.url) == 'X10-Prototype-Admin.html#acct', short(page.url))
        s = await page.evaluate(ST); rec('  X10 opens acct section', s.get('sec') == 'acct', s.get('sec'))
        await go('X26-Prototype-AdminRules.html#plans/mx')
        rec('X26#plans/mx -> X25#plans/mx', short(page.url) == 'X25-Prototype-AdminPlans.html#plans/mx', short(page.url))
        # in-app navigation (assign, new history entry)
        await go('X25-Prototype-AdminPlans.html')
        async with page.expect_navigation():
            await page.evaluate(LOGIC, ['plans', 'beta'])
        await page.wait_for_timeout(1200)
        rec('X25 go20(plans,beta) -> X26#plans/beta', short(page.url) == 'X26-Prototype-AdminRules.html#plans/beta', short(page.url))
        await page.go_back(); await page.wait_for_timeout(1200)
        rec('  back button returns to X25', short(page.url).startswith('X25-Prototype-AdminPlans.html'), short(page.url))
        async with page.expect_navigation():
            await page.evaluate(LOGIC, ['over', ''])
        await page.wait_for_timeout(1200)
        rec('X25 go20(over) -> X10#over', short(page.url) == 'X10-Prototype-Admin.html#over', short(page.url))
        # UI click in X10's side menu on the plans entry
        await go('X10-Prototype-Admin.html')
        n = await page.evaluate("""() => { const els = [...document.querySelectorAll('#dc-root button, #dc-root a')].filter(e => /প্ল্যান ও মডিউল/.test(e.textContent) && e.getBoundingClientRect().width > 3); if (!els.length) return 0; els[0].setAttribute('data-t', '1'); return els.length; }""")
        if n:
            async with page.expect_navigation():
                await page.locator('[data-t="1"]').first.click()
            await page.wait_for_timeout(1200)
        rec('X10 UI click "plans & modules" -> X25', short(page.url).startswith('X25-Prototype-AdminPlans.html'), '%d candidates, %s' % (n, short(page.url)))
        # X20 #legal/<id> forwards to X24
        await go('X20-Prototype-Landing.html#legal/privacy', 2500)
        rec('X20#legal/privacy -> X24#legal/privacy', short(page.url) == 'X24-Prototype-Legal.html#legal/privacy', short(page.url))
        s = await page.evaluate(ST); rec('  X24 opens privacy page', s.get('lg') == 'privacy', s.get('lg'))
        # X24 in-page hash route (href="#legal/security-disclosure")
        await go('X24-Prototype-Legal.html')
        await page.locator('#fb-sec').first.scroll_into_view_if_needed(); await page.locator('#fb-sec').first.click(); await page.wait_for_timeout(600)
        s = await page.evaluate(ST); rec('X24 #fb-sec -> #legal/security-disclosure', s.get('lg') == 'disclosure' and short(page.url).endswith('#legal/security-disclosure'), '%s %s' % (s.get('lg'), short(page.url)))
        # X24 hashchange from the address bar
        await page.evaluate("location.hash = '#legal/terms'"); await page.wait_for_timeout(500)
        s = await page.evaluate(ST); rec('X24 hashchange #legal/terms', s.get('lg') == 'terms', s.get('lg'))
        await page.evaluate("location.hash = '#legal'"); await page.wait_for_timeout(500)
        s = await page.evaluate(ST); rec('X24 #legal -> page index', not s.get('lg'), repr(s.get('lg')))
        # X24 cookie policy -> X20 #cookie-settings
        await go('X24-Prototype-Legal.html#legal/cookies')
        loc = page.locator('#lg-ck'); c = await loc.count()
        if c:
            await loc.first.scroll_into_view_if_needed()
            async with page.expect_navigation():
                await loc.first.click()
            await page.wait_for_timeout(2000)
        s = await page.evaluate(ST)
        rec('X24 cookies "#lg-ck" -> X20#cookie-settings', c and short(page.url) == 'X20-Prototype-Landing.html#cookie-settings' and s.get('ckShow') and s.get('ckSet'), '%s ckShow=%s ckSet=%s' % (short(page.url), s.get('ckShow'), s.get('ckSet')))
        # X20 footer legal link -> X24
        await go('X20-Prototype-Landing.html', 2000)
        h = await page.evaluate("() => { const a = [...document.querySelectorAll('a[href^=\"X24-Prototype-Legal.html#legal/\"]')]; return a.length ? a[0].getAttribute('href') : null; }")
        if h:
            l = page.locator('a[href="%s"]' % h).first; await l.scroll_into_view_if_needed()
            async with page.expect_navigation():
                await l.click()
            await page.wait_for_timeout(1500)
        s = await page.evaluate(ST)
        rec('X20 footer legal link -> X24', bool(h) and short(page.url) == h and bool(s.get('lg')), '%s lg=%s' % (h, s.get('lg')))
        # X24 back to landing
        await go('X24-Prototype-Legal.html')
        async with page.expect_navigation():
            await page.locator('#x24-back').first.click()
        await page.wait_for_timeout(800)
        rec('X24 back -> X20', short(page.url) == 'X20-Prototype-Landing.html', short(page.url))
        # X15 legal register row -> X24
        await go('X15-Prototype-Accounts.html')
        hh = await page.evaluate("() => [...document.querySelectorAll('a[href*=\"X24-Prototype-Legal\"]')].map(a => a.getAttribute('href')).slice(0, 2)")
        rec('X15 renders X24 links (mapped)', all(x.startswith('X24-Prototype-Legal.html#legal/') for x in hh), str(hh) + ' (only on its legal tab if empty)')
        # X27 Nexa Co-Admin: header button on 11 admin boards -> X27#from=<stem>; back link; tab hashes
        CO = ['X10-Prototype-Admin', 'X13-Prototype-LandingAI', 'X14-Prototype-Ops', 'X15-Prototype-Accounts', 'X16-Prototype-Quality', 'X17-Prototype-Growth',
              'X19-Prototype-MarketingHub', 'X21-Prototype-Comms', 'X22-Prototype-AvatarVoice', 'X25-Prototype-AdminPlans', 'X26-Prototype-AdminRules']
        okc = []
        for st in CO:
            await go(st + '.html', 1000)
            hs = await page.evaluate("() => [...document.querySelectorAll('a[href^=\"X27-Prototype-CoAdmin\"]')].map(a => a.getAttribute('href'))")
            okc.append(('X27-Prototype-CoAdmin.html#from=' + st) in hs)
            if not okc[-1]: print('   missing Co-Admin link on', st, hs[:3])
        rec('Co-Admin button on 11 admin boards -> X27#from=<stem>', all(okc), '%d/%d' % (sum(okc), len(okc)))
        for st in ['X10-Prototype-Admin', 'X25-Prototype-AdminPlans', 'X21-Prototype-Comms']:
            await go(st + '.html', 1000)
            l = page.locator('a[href="X27-Prototype-CoAdmin.html#from=%s"]' % st).first
            async with page.expect_navigation():
                await l.click()
            await page.wait_for_timeout(1500)
            s = await page.evaluate(ST)
            rec('%s Co-Admin click -> X27, caFrom' % st[:3], short(page.url) == 'X27-Prototype-CoAdmin.html#from=' + st and s.get('caFrom') == st, '%s caFrom=%s' % (short(page.url), s.get('caFrom')))
            bk = page.locator('a.ca-a44').first; bh = await bk.get_attribute('href') if await bk.count() else None
            if bh:
                async with page.expect_navigation():
                    await bk.click()
                await page.wait_for_timeout(1000)
            rec('  X27 back link -> %s' % st[:3], bh == st + '.html' and short(page.url) == st + '.html', '%s -> %s' % (bh, short(page.url)))
        for hsh, tab in [('#log', 'log'), ('#settings', 'set'), ('#chatapps', 'wa'), ('#chat/from=X14-Prototype-Ops', 'chat')]:
            await page.goto('about:blank')  # fresh load: a hash-only goto would not reload the page
            await go('X27-Prototype-CoAdmin.html' + hsh, 1200)
            s = await page.evaluate(ST)
            rec('X27 %s -> tab %s' % (hsh, tab), s.get('caTab') == tab, '%s caFrom=%s' % (s.get('caTab'), s.get('caFrom')))
        # X20 "Simulate" switches (class full / admissions closed)
        await go('X20-Prototype-Landing.html', 2000)
        sims = await page.evaluate("""() => { const els = [...document.querySelectorAll('#dc-root button, #dc-root [role=switch], #dc-root label')].filter(e => /সিমুলেট|Simulate/i.test(e.textContent) && e.textContent.length < 80 && e.getBoundingClientRect().width > 3);
            els.forEach((e, i) => e.setAttribute('data-sim', i)); return els.map(e => e.textContent.trim().slice(0, 50)); }""")
        for i, nm in enumerate(sims):
            t0 = await page.evaluate("() => document.getElementById('dc-root').innerText")
            await page.locator('[data-sim="%d"]' % i).first.click(); await page.wait_for_timeout(500)
            t1 = await page.evaluate("() => document.getElementById('dc-root').innerText")
            p1 = await page.locator('[data-sim="%d"]' % i).first.get_attribute('aria-pressed') or await page.locator('[data-sim="%d"]' % i).first.get_attribute('aria-checked')
            rec('X20 switch "%s"' % nm[:30], t0 != t1, 'page text changed, pressed=%s' % p1)
            await page.locator('[data-sim="%d"]' % i).first.click(); await page.wait_for_timeout(400)
        rec('X20 has 2 Simulate switches', len(sims) >= 2, str(sims))
        bad = [e for e in errs if 'ERR_ABORTED' not in e]
        print('checks', len(res), 'bad', res.count(False), 'errors', bad[:6], 'aborted(by navigation)', len(errs) - len(bad))
        await b.close()
asyncio.run(main())

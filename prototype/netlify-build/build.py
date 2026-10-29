#!/usr/bin/env python3
"""Build the NexaTute static mockup site for Netlify Drop.
Reads SP/ntd/project (read-only), writes SP/s2/netlify/nexatute-mockups/ and the zip."""
import html, json, os, re, shutil, sys, zipfile

SP = '/tmp/claude-0/-home-claude/9878cfdb-4647-5257-a0fe-47a0a28067df/scratchpad'
PROJ = os.path.join(SP, 'ntd', 'project')
HERE = os.path.dirname(os.path.abspath(__file__))
NET = os.path.dirname(HERE)
OUT = os.path.join(NET, 'nexatute-mockups')
SHOTS = os.path.join(SP, 's2', 'fix14', 'thumbs', 'shots')
FF = os.path.join(HERE, 'ff', 'fonts', 'google')
INDEX_STEM = 'W00-Website-Preview'
ALL_LABEL = '<span class="dcx-tab"><span class="dcx-arr" aria-hidden="true">←</span><span class="dcx-lbl">সব পাতা / All pages</span></span>'

# Google family name -> fontsource id
FONTSRC = {'Hind Siliguri': 'hind-siliguri', 'Baloo Da 2': 'baloo-da-2', 'Hind': 'hind',
           'Noto Naskh Arabic': 'noto-naskh-arabic', 'Baloo 2': 'baloo-2', 'Baloo Bhaijaan 2': 'baloo-bhaijaan-2',
           'Noto Nastaliq Urdu': 'noto-nastaliq-urdu'}


def esc(s):
    return html.escape(s, quote=True)


def read_board(path):
    src = open(path, encoding='utf-8').read()
    lang = (re.search(r'<html[^>]*\blang="([^"]*)"', src) or [None, 'en'])[1]
    title = html.unescape((re.search(r'<title>(.*?)</title>', src, re.S) or [None, ''])[1].strip())
    xdc = re.search(r'<x-dc>([\s\S]*?)</x-dc>', src).group(1)
    hm = re.search(r'<helmet>([\s\S]*?)</helmet>', xdc)
    helmet = hm.group(1) if hm else ''
    tpl = xdc[:hm.start()] + xdc[hm.end():] if hm else xdc
    sm = re.search(r'<script type="text/x-dc"([^>]*)>([\s\S]*?)</script>', src)
    attrs, script = sm.group(1), sm.group(2)
    pm = re.search(r"data-props='([^']*)'", attrs) or re.search(r'data-props="([^"]*)"', attrs)
    props = {}
    if pm:
        spec = json.loads(html.unescape(pm.group(1)))
        for k, v in spec.items():
            if k.startswith('$'):
                continue
            if isinstance(v, dict) and 'default' in v:
                props[k] = v['default']
    return dict(src=src, lang=lang, title=title, helmet=helmet, tpl=tpl, script=script, props=props)


GF_LINK = re.compile(r'<link\b[^>]*href="(https://fonts\.(?:googleapis|gstatic)\.com[^"]*)"[^>]*>\s*', re.I)


def clean_helmet(helmet, fams):
    def repl(m):
        url = html.unescape(m.group(1))
        if 'css2?' in url:
            for fam in re.findall(r'family=([^&]+)', url):
                name, _, w = fam.partition(':wght@')
                name = name.replace('+', ' ')
                ws = set(int(x) for x in w.split(';') if x) if w else {400}
                fams.setdefault(name, set()).update(ws)
        return ''
    out = GF_LINK.sub(repl, helmet)
    if re.search(r'https?://', re.sub(r'url\(\s*["\']?data:', '', out)):
        print('WARN external URL left in helmet', re.findall(r'https?://[^\s"\')]+', out)[:3])
    return out.strip()


def head_common(title, lang, extra=''):
    return ('<!doctype html>\n<html lang="%s"%s>\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<meta name="robots" content="noindex,nofollow">\n<title>%s</title>\n' % (esc(lang), extra, esc(title)))


def main():
    canvas = json.load(open(os.path.join(PROJ, 'canvas.json'), encoding='utf-8'))
    boards = canvas['boards']
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    for d in ('boards', 'frames', 'vendor', 'fonts/files', 'thumbs'):
        os.makedirs(os.path.join(OUT, d), exist_ok=True)

    fams = {}
    pages = []
    for fname in sorted(boards):
        meta = boards[fname]
        stem = fname[:-len('.dc.html')]
        b = read_board(os.path.join(PROJ, fname))
        helmet = clean_helmet(b['helmet'], fams)
        script = b['script']
        if stem == INDEX_STEM:
            n0 = script.count('/_blob/')
            script, n = re.subn(r"'([A-Z]\d\d[\w-]*|Main)':\s*'/_blob/[0-9a-f]+'",
                                lambda m: "'%s': 'thumbs/%s.webp'" % (m.group(1), m.group(1)), script)
            assert n == n0 == len([f for f in os.listdir(SHOTS) if f.endswith('.webp')]), (n, n0)
            for m in re.finditer(r"'thumbs/([\w-]+)\.webp'", script):
                assert os.path.exists(os.path.join(SHOTS, m.group(1) + '.webp')), m.group(1)
        assert '/_blob/' not in script and '/_blob/' not in b['tpl'], stem
        w, h = meta.get('w'), meta.get('h')
        mode = 'fill' if meta.get('expand') == 'fill' else ('phone' if w == 390 else 'fixed')
        page = 'index.html' if stem == INDEX_STEM else stem + '.html'
        framed = mode != 'fill'
        # board data + logic (logic stays real JS: wrapped in a factory that receives DCLogic)
        js = ('/* %s — generated from %s */\nDCRuntime.mount(%s, function (DCLogic, location) {\n%s\nreturn Component;\n});\n' % (
            stem, fname, json.dumps({'stem': stem, 'page': page, 'mode': mode, 'w': w, 'h': h,
                                     'base': '../' if framed else '', 'framed': framed,
                                     'props': b['props'], 'tpl': b['tpl']}, ensure_ascii=False), script))
        open(os.path.join(OUT, 'boards', stem + '.js'), 'w', encoding='utf-8').write(js)

        def board_doc(prefix, with_link):
            s = head_common(b['title'] or meta.get('title', stem), b['lang'])
            s += '<link rel="stylesheet" href="%sfonts/fonts.css">\n' % prefix
            if with_link:
                s += '<link rel="stylesheet" href="%ssite.css">\n' % prefix
            s += helmet + '\n</head>\n<body>\n<div id="dc-root"></div>\n'
            if with_link:
                s += '<a class="dcx-all" href="%sindex.html" title="← সব পাতা / All pages">%s</a>\n<script src="%sdcx-all.js" defer></script>\n' % (prefix, ALL_LABEL, prefix)
            s += ('<script src="%svendor/preact.min.js"></script>\n<script src="%sdc-runtime.js"></script>\n'
                  '<script src="%sboards/%s.js"></script>\n</body>\n</html>\n' % (prefix, prefix, prefix, stem))
            return s

        if mode == 'fill':
            open(os.path.join(OUT, page), 'w', encoding='utf-8').write(board_doc('', stem != INDEX_STEM))
        else:
            open(os.path.join(OUT, 'frames', stem + '.html'), 'w', encoding='utf-8').write(board_doc('../', False))
            r = meta.get('radius', 0) or 0
            cls = 'dcx-shell dcx-' + mode
            s = head_common(b['title'] or stem, b['lang'], ' class="%s"' % cls)
            s += '<link rel="stylesheet" href="fonts/fonts.css">\n<link rel="stylesheet" href="site.css">\n</head>\n<body>\n'
            s += '<main class="dcx-stage">\n<p class="dcx-cap" style="--w:%dpx">%s</p>\n' % (w, esc(meta.get('title', stem)))
            s += ('<div class="dcx-fit"><div class="dcx-frame" data-w="%d" data-h="%d" style="--w:%dpx;--h:%dpx;--r:%dpx">'
                  '<iframe src="frames/%s.html" title="%s" width="%d" height="%d" allow="clipboard-write; autoplay; fullscreen"></iframe>'
                  '</div></div>\n</main>\n' % (w, h, w, h, r, stem, esc(meta.get('title', stem)), w, h))
            s += '<a class="dcx-all" href="index.html" title="← সব পাতা / All pages">%s</a>\n<script src="shell.js"></script>\n<script src="dcx-all.js" defer></script>\n</body>\n</html>\n' % ALL_LABEL
            open(os.path.join(OUT, page), 'w', encoding='utf-8').write(s)
        pages.append(dict(stem=stem, page=page, mode=mode, w=w, h=h, framed=framed,
                          interactive=bool(meta.get('is_interactive')), title=meta.get('title', stem)))

    # runtime, vendor, shell
    shutil.copy(os.path.join(HERE, 'src', 'dc-runtime.js'), os.path.join(OUT, 'dc-runtime.js'))
    shutil.copy(os.path.join(HERE, 'src', 'site.css'), os.path.join(OUT, 'site.css'))
    shutil.copy(os.path.join(HERE, 'src', 'shell.js'), os.path.join(OUT, 'shell.js'))
    shutil.copy(os.path.join(HERE, 'src', 'dcx-all.js'), os.path.join(OUT, 'dcx-all.js'))
    ver = json.load(open(os.path.join(HERE, 'preact-src', 'package.json')))['version']
    pre = open(os.path.join(HERE, 'preact-bundle.js'), encoding='utf-8').read()
    open(os.path.join(OUT, 'vendor', 'preact.min.js'), 'w', encoding='utf-8').write(
        '/*! Preact %s + preact/compat (MIT License, https://preactjs.com) — see vendor/LICENSE-preact.txt */\n' % ver + pre)
    shutil.copy(os.path.join(HERE, 'preact-src', 'LICENSE'), os.path.join(OUT, 'vendor', 'LICENSE-preact.txt'))

    # fonts
    css = ['/* Self-hosted fonts (Fontsource builds of Google Fonts, SIL Open Font License 1.1). */\n']
    lic_done = set()
    missing = []
    for fam in sorted(fams):
        fid = FONTSRC.get(fam)
        if not fid or not os.path.isdir(os.path.join(FF, fid)):
            missing.append(fam)
            continue
        for wgt in sorted(fams[fam]):
            p = os.path.join(FF, fid, '%d.css' % wgt)
            if not os.path.exists(p):
                missing.append('%s %d' % (fam, wgt))
                continue
            c = open(p, encoding='utf-8').read()
            c = re.sub(r",\s*url\(\./files/[^)]+\.woff\)\s*format\('woff'\)", '', c)
            for f in re.findall(r'url\(\./files/([^)]+\.woff2)\)', c):
                shutil.copy(os.path.join(FF, fid, 'files', f), os.path.join(OUT, 'fonts', 'files', f))
            c = c.replace('url(./files/', 'url(files/')
            css.append(c.strip() + '\n')
        if fid not in lic_done:
            shutil.copy(os.path.join(FF, fid, 'LICENSE'), os.path.join(OUT, 'fonts', 'LICENSE-%s.txt' % fid))
            lic_done.add(fid)
    open(os.path.join(OUT, 'fonts', 'fonts.css'), 'w', encoding='utf-8').write('\n'.join(css))
    if missing:
        print('MISSING FONTS', missing)

    # thumbnails
    for f in os.listdir(SHOTS):
        if f.endswith('.webp'):
            shutil.copy(os.path.join(SHOTS, f), os.path.join(OUT, 'thumbs', f))

    # not indexed
    open(os.path.join(OUT, 'robots.txt'), 'w').write('User-agent: *\nDisallow: /\n')
    open(os.path.join(OUT, '_headers'), 'w').write('/*\n  X-Robots-Tag: noindex, nofollow\n')
    shutil.copy(os.path.join(HERE, 'src', 'README.txt'), os.path.join(OUT, 'README.txt'))
    json.dump({'fonts': {k: sorted(v) for k, v in fams.items()}, 'pages': pages},
              open(os.path.join(HERE, 'manifest.json'), 'w'), indent=1, ensure_ascii=False)

    # zip (folder name inside: nexatute-mockups)
    zp = os.path.join(NET, 'nexatute-mockups-netlify.zip')
    if os.environ.get('NOZIP'):  # site folder only (testing); leave the zip alone
        print('pages', len(pages), 'NOZIP: zip not written')
        return
    if os.path.exists(zp):
        os.remove(zp)
    with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for root, dirs, files in os.walk(OUT):
            dirs.sort()
            for f in sorted(files):
                full = os.path.join(root, f)
                arc = os.path.join('nexatute-mockups', os.path.relpath(full, OUT))
                z.write(full, arc, compress_type=zipfile.ZIP_STORED if f.endswith(('.woff2', '.webp')) else zipfile.ZIP_DEFLATED)
    tot = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(OUT) for f in fs)
    print('pages', len(pages), 'site bytes', tot, 'zip bytes', os.path.getsize(zp))
    print('fonts', {k: sorted(v) for k, v in fams.items()})


if __name__ == '__main__':
    main()

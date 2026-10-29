/* Keeps the floating "← সব পাতা / All pages" link off the page's own controls.
   It starts folded (24 px tab, 44 px hit area) at the bottom inline-start corner. When a fixed / sticky element or a
   control sits under that spot (a cookie bar, an admissions banner, a bottom sheet, a button scrolling past), the
   link moves above it; if the lower part of the screen is taken it goes to the top inline-start corner, then to the
   other side. If no spot is free it is hidden (still reachable with the Tab key). Re-checked on scroll, resize and
   page changes. Boards in an iframe (phone and fixed-size boards) are looked into as well. */
(function () {
  'use strict';
  var a = document.querySelector('a.dcx-all');
  if (!a || !document.elementsFromPoint) return;
  var S = 44, GAP = 8, EDGE = 12;
  var INTER = 'a[href],button,input,select,textarea,summary,label,[role=button],[role=link],[role=tab],[role=switch],' +
    '[role=checkbox],[role=radio],[role=menuitem],[role=option],[role=slider],[role=combobox],[contenteditable=""],' +
    '[contenteditable="true"],[tabindex]:not([tabindex="-1"])';

  function frameDoc() {
    var f = document.querySelector('.dcx-frame iframe');
    try { return f && f.contentDocument && f.contentDocument.documentElement ? f.contentDocument : null; } catch (e) { return null; }
  }
  // Preact keeps a node's listeners in node.l (e.g. {clickfalse: fn})
  function hasClick(n) {
    var l = n.l;
    if (!l) return false;
    for (var k in l) if (k.indexOf('click') === 0 || k.indexOf('pointerdown') === 0 || k.indexOf('mousedown') === 0) return true;
    return false;
  }
  // a click handler on a big container that holds its own links / buttons (delegation, e.g. a footer or header
  // listening for its links) does not make the whole container a control; a clickable card or row does
  function isInter(n) {
    try {
      if (n.matches(INTER)) return true;
      if (!hasClick(n)) return false;
      var r = n.getBoundingClientRect(), w = n.ownerDocument.defaultView;
      return r.width * r.height < 0.3 * w.innerWidth * w.innerHeight || !n.querySelector(INTER);
    } catch (e) { return false; }
  }

  var memo = null; // per placement pass: element -> what it means for the link (null = harmless)
  // What would the link cover at (x, y)? -> {r: rect in this viewport} or null
  function blockerAt(doc, win, x, y, ox, oy, sc) {
    var els;
    try { els = doc.elementsFromPoint(x, y); } catch (e) { return null; }
    for (var i = 0; i < els.length; i++) {
      var e = els[i];
      if (e === a || a.contains(e)) continue;
      if (e.tagName === 'IFRAME') {
        var d = null;
        try { d = e.contentDocument; } catch (x2) { d = null; }
        if (!d || !d.documentElement) return { r: e.getBoundingClientRect() };
        var fr = e.getBoundingClientRect(), s = (fr.width / (e.offsetWidth || fr.width)) || 1;
        return blockerAt(d, e.contentWindow, (x - fr.left - e.clientLeft * s) / s, (y - fr.top - e.clientTop * s) / s,
          ox + fr.left + e.clientLeft * s, oy + fr.top + e.clientTop * s, sc * s);
      }
      if (e === doc.documentElement || e === doc.body) return null;
      if (memo && memo.has(e)) return memo.get(e);
      var res = classify(e, doc, win, ox, oy, sc);
      if (memo) memo.set(e, res);
      return res;
    }
    return null;
  }
  function classify(e, doc, win, ox, oy, sc) {
    {
      var inter = null, vw = win.innerWidth, vh = win.innerHeight;
      for (var n = e; n && n.nodeType === 1 && n !== doc.body; n = n.parentElement) {
        if (!inter && isInter(n)) inter = n;
        var p = win.getComputedStyle(n).position;
        if (p === 'fixed' || p === 'sticky') {
          var fr2 = n.getBoundingClientRect();
          // a bar / sheet / banner; a fixed layer that fills the window (app shell, plain scrim) only counts through its controls
          if (fr2.width * fr2.height < 0.85 * vw * vh) { inter = n; }
          break;
        }
      }
      if (!inter) return null;
      var r = inter.getBoundingClientRect();
      return { r: { top: oy + r.top * sc, bottom: oy + r.bottom * sc } };
    }
  }
  // first thing the 44 x 44 box at (x0, y0) would cover
  function test(x0, y0) {
    var vw = document.documentElement.clientWidth, vh = window.innerHeight;
    // 5 x 5 points over the whole 44 px hit area, edges included (no control slips between the points)
    var xs = [], ys = [];
    for (var q = 0; q < 5; q++) { xs.push(x0 + 1 + q * (S - 2) / 4); ys.push(y0 + 1 + q * (S - 2) / 4); }
    for (var j = 0; j < 5; j++) for (var i = 0; i < 5; i++) {
      var x = xs[i], y = ys[j];
      if (x < 0 || y < 0 || x >= vw || y >= vh) continue;
      var b = blockerAt(document, window, x, y, 0, 0, 1);
      if (b) return b;
    }
    return null;
  }

  function rtl() {
    var d = frameDoc() || document, el = d.querySelector('#dc-root [lang][dir]') || d.querySelector('#dc-root [dir]') ||
      (d.getElementById('dc-root') || {}).firstElementChild;
    try { return (el ? (d.defaultView || window).getComputedStyle(el).direction : '') === 'rtl'; } catch (e) { return false; }
  }

  function put(side, edge, v) {
    var st = a.style;
    st.left = side === 'left' ? '0' : 'auto'; st.right = side === 'right' ? '0' : 'auto';
    st.top = edge === 'top' ? v + 'px' : 'auto'; st.bottom = edge === 'bottom' ? v + 'px' : 'auto';
    a.classList.toggle('dcx-r', side === 'right');
    a.classList.remove('dcx-off');
    a.classList.add('dcx-ready');
  }

  var hover = false;
  function place() {
    raf = 0;
    if (hover || document.activeElement === a) return;
    memo = typeof Map === 'function' ? new Map() : null;
    try { place_(); } finally { memo = null; }
  }
  function place_() {
    var vw = document.documentElement.clientWidth, vh = window.innerHeight, r = rtl();
    a.classList.toggle('dcx-rtl', r);
    // measure without the link's own last position mattering
    var sides = r ? ['right', 'left'] : ['left', 'right'];
    for (var k = 0; k < sides.length; k++) {
      var side = sides[k], x0 = side === 'left' ? 0 : vw - S, g, b;
      // bottom: climb above whatever sits at the bottom edge (cookie bar, banner, sheet, a control scrolling past)
      var yb = vh - EDGE;
      for (g = 0; g < 16 && yb - S >= vh * 0.35; g++) {
        b = test(x0, yb - S);
        if (!b) { put(side, 'bottom', Math.round(vh - yb)); return; }
        yb = Math.min(yb - 4, b.r.top - GAP);
      }
      // the lower part is taken: top corner, below whatever sits there
      var yt = EDGE;
      for (g = 0; g < 16 && yt + S <= vh * 0.65; g++) {
        b = test(x0, yt);
        if (!b) { put(side, 'top', Math.round(yt)); return; }
        yt = Math.max(yt + 4, b.r.bottom + GAP);
      }
    }
    a.classList.add('dcx-off');
    a.classList.add('dcx-ready');
  }

  var raf = 0, late = 0;
  function soon() {
    if (!raf) raf = requestAnimationFrame(place);
    clearTimeout(late); late = setTimeout(place, 400); // after CSS transitions (bars sliding in)
  }
  a.addEventListener('mouseenter', function () { hover = true; });
  a.addEventListener('mouseleave', function () { hover = false; soon(); });
  a.addEventListener('blur', soon);
  window.addEventListener('resize', soon);
  window.addEventListener('scroll', soon, true);
  var mo = window.MutationObserver ? new MutationObserver(soon) : null, OPTS = { subtree: true, childList: true, attributes: true, attributeFilter: ['class', 'style', 'open', 'hidden', 'dir'] };
  if (mo) mo.observe(document.body, OPTS);
  var watched = null;
  function watchFrame() {
    var d = frameDoc();
    if (d && d !== watched && d.body) {
      watched = d;
      if (mo) mo.observe(d.body, OPTS);
      d.addEventListener('scroll', soon, true);
      soon();
    }
  }
  var f = document.querySelector('.dcx-frame iframe');
  if (f) f.addEventListener('load', watchFrame);
  watchFrame();
  setInterval(function () { watchFrame(); soon(); }, 1500);
  soon();
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(soon);
})();

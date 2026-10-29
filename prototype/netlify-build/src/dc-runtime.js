/*! dc-runtime.js — renders NexaTute .dc.html boards as standalone pages (static export).
 * Own implementation of the documented .dc.html format on top of Preact (MIT, vendor/preact.min.js).
 * Template -> Preact vnodes on every render: {{ path }} holes, attribute holes, <sc-if>, <sc-for>,
 * React-style events (via preact/compat normalisation), DCLogic base class with state/lifecycle. */
(function (global) {
  'use strict';

  var VOID = { area: 1, base: 1, br: 1, col: 1, embed: 1, hr: 1, img: 1, input: 1, link: 1, meta: 1, param: 1, source: 1, track: 1, wbr: 1 };
  var RAW = { script: 1, style: 1, textarea: 1, title: 1 };
  // Boolean attributes: a literal attribute (no hole) means "on"; value = DOM property name.
  var BOOL = {
    disabled: 'disabled', checked: 'checked', selected: 'selected', hidden: 'hidden', open: 'open', readonly: 'readOnly',
    required: 'required', multiple: 'multiple', autofocus: 'autoFocus', novalidate: 'noValidate', inert: 'inert',
    controls: 'controls', autoplay: 'autoplay', loop: 'loop', muted: 'muted', playsinline: 'playsInline', 'default': 'default',
    reversed: 'reversed', allowfullscreen: 'allowFullscreen', async: 'async', defer: 'defer', nomodule: 'noModule',
    formnovalidate: 'formNoValidate', ismap: 'isMap', itemscope: 'itemScope'
  };

  // ---------- entity decoding ----------
  var decEl = null;
  var BASIC = { amp: '&', lt: '<', gt: '>', quot: '"', apos: "'", nbsp: ' ', '#39': "'" };
  function decode(s) {
    if (s.indexOf('&') < 0) return s;
    if (typeof document !== 'undefined') {
      decEl = decEl || document.createElement('textarea');
      decEl.innerHTML = s;
      return decEl.value;
    }
    return s.replace(/&(#x[0-9a-f]+|#\d+|\w+);/gi, function (m, e) {
      if (e[0] === '#') return String.fromCodePoint(e[1] === 'x' || e[1] === 'X' ? parseInt(e.slice(2), 16) : parseInt(e.slice(1), 10));
      return BASIC[e] !== undefined ? BASIC[e] : m;
    });
  }

  // ---------- holes ----------
  var HOLE = /\{\{\s*([\s\S]*?)\s*\}\}/g;
  function compilePath(p) {
    p = p.trim();
    if (p === 'true') return { lit: true, v: true };
    if (p === 'false') return { lit: true, v: false };
    if (p === 'null') return { lit: true, v: null };
    if (p === 'undefined') return { lit: true, v: undefined };
    if (/^-?\d+(\.\d+)?$/.test(p)) return { lit: true, v: parseFloat(p) };
    if (/^'[^']*'$/.test(p) || /^"[^"]*"$/.test(p)) return { lit: true, v: p.slice(1, -1) };
    return { segs: p.split('.'), src: p };
  }
  // parts: array of literal strings and compiled paths; whole = single hole with nothing around it
  function parts(s, doDecode) {
    var out = [], last = 0, m;
    HOLE.lastIndex = 0;
    while ((m = HOLE.exec(s))) {
      if (m.index > last) out.push(doDecode ? decode(s.slice(last, m.index)) : s.slice(last, m.index));
      out.push(compilePath(m[1]));
      last = HOLE.lastIndex;
    }
    if (last < s.length) out.push(doDecode ? decode(s.slice(last)) : s.slice(last));
    return out;
  }
  function isHole(x) { return x && typeof x === 'object'; }

  // ---------- tokenizer / tree builder ----------
  var reOpen = /<([a-zA-Z][\w:.-]*)/y, reClose = /<\/([a-zA-Z][\w:.-]*)\s*>/y, reWs = /[\s]*/y,
    reName = /[^\s"'>\/=]+/y, reEq = /\s*=\s*/y, reDq = /"([^"]*)"/y, reSq = /'([^']*)'/y, reUq = /[^\s>]+/y;
  function sticky(re, s, i) { re.lastIndex = i; var m = re.exec(s); return m; }

  function parse(src) {
    var root = { tag: '#root', kids: [] }, stack = [root], i = 0, n = src.length, textStart = 0, issues = [];
    function top() { return stack[stack.length - 1]; }
    function flush(end) {
      if (end > textStart) {
        var raw = src.slice(textStart, end), t = top(), last = t.kids[t.kids.length - 1];
        if (last && last.rawText !== undefined) { last.rawText += raw; } else t.kids.push({ rawText: raw });
      }
    }
    function closeTo(name) {
      var lname = name.toLowerCase();
      for (var k = stack.length - 1; k > 0; k--) {
        if (stack[k].ltag === lname) {
          if (k !== stack.length - 1) issues.push('implicitly closed <' + stack.slice(k + 1).map(function (x) { return x.tag; }).join('><') + '> by </' + name + '>');
          stack.length = k; return true;
        }
      }
      issues.push('stray </' + name + '>');
      return false;
    }
    while (i < n) {
      var lt = src.indexOf('<', i);
      if (lt < 0) break;
      var c = src.charAt(lt + 1), m;
      if (c === '!') {
        flush(lt);
        if (src.startsWith('<!--', lt)) { var e = src.indexOf('-->', lt + 4); i = e < 0 ? n : e + 3; }
        else { var e2 = src.indexOf('>', lt); i = e2 < 0 ? n : e2 + 1; }
        textStart = i; continue;
      }
      if (c === '/') {
        m = sticky(reClose, src, lt);
        if (m) { flush(lt); closeTo(m[1]); i = textStart = lt + m[0].length; continue; }
        i = lt + 1; continue;
      }
      m = sticky(reOpen, src, lt);
      if (!m) { i = lt + 1; continue; }
      flush(lt);
      var tag = m[1], ltag = tag.toLowerCase(), p = lt + m[0].length, attrs = [], selfClose = false;
      for (;;) {
        p = sticky(reWs, src, p) ? reWs.lastIndex : p;
        if (p >= n) break;
        var ch = src.charAt(p);
        if (ch === '>') { p++; break; }
        if (ch === '/' && src.charAt(p + 1) === '>') { selfClose = true; p += 2; break; }
        if (ch === '/') { p++; continue; }
        var nm = sticky(reName, src, p);
        if (!nm) { p++; continue; }
        p = reName.lastIndex;
        var val = null, eq = sticky(reEq, src, p);
        if (eq && eq[0].indexOf('=') >= 0) {
          p = reEq.lastIndex;
          var vm = sticky(reDq, src, p) || sticky(reSq, src, p);
          if (vm) { val = vm[1]; p += vm[0].length; }
          else { vm = sticky(reUq, src, p); if (vm) { val = vm[0]; p += vm[0].length; } else val = ''; }
        }
        attrs.push({ name: nm[0], raw: val });
      }
      var node = { tag: tag, ltag: ltag, attrs: attrs, kids: [] };
      // light implicit-close rules (same-type siblings that HTML closes automatically)
      var tp = top();
      if ((ltag === 'li' && tp.ltag === 'li') || (ltag === 'option' && tp.ltag === 'option') ||
        ((ltag === 'td' || ltag === 'th') && (tp.ltag === 'td' || tp.ltag === 'th')) || (ltag === 'tr' && tp.ltag === 'tr') ||
        ((ltag === 'dt' || ltag === 'dd') && (tp.ltag === 'dt' || tp.ltag === 'dd'))) {
        issues.push('implicitly closed <' + tp.tag + '> by <' + tag + '>'); stack.pop();
      }
      top().kids.push(node);
      i = p;
      if (RAW[ltag] && !selfClose) {
        var endIdx = src.toLowerCase().indexOf('</' + ltag, p);
        if (endIdx < 0) endIdx = n;
        var content = src.slice(p, endIdx);
        if (content) node.kids.push({ rawText: content, rawEl: ltag });
        var gt = src.indexOf('>', endIdx);
        i = gt < 0 ? n : gt + 1;
      } else if (!selfClose && !VOID[ltag]) {
        stack.push(node);
      }
      textStart = i;
    }
    flush(n);
    if (stack.length > 1) issues.push('unclosed: ' + stack.slice(1).map(function (x) { return x.tag; }).join(' > '));
    finalize(root);
    root.issues = issues;
    return root;
  }

  // compile attributes and texts once
  function finalize(node) {
    var kids = node.kids;
    for (var k = 0; k < kids.length; k++) {
      var kd = kids[k];
      if (kd.rawText !== undefined) {
        kd.text = parts(kd.rawText, !(kd.rawEl === 'script' || kd.rawEl === 'style'));
        kd.whole = kd.text.length === 1 && isHole(kd.text[0]) ? kd.text[0] : null;
        kd.isStatic = !kd.text.some(isHole);
        if (kd.isStatic) kd.str = kd.text.join('');
        continue;
      }
      if (kd.ltag === 'sc-if' || kd.ltag === 'sc-for') {
        kd.kind = kd.ltag === 'sc-if' ? 'if' : 'for';
        kd.attrs.forEach(function (a) {
          var pp = a.raw == null ? [] : parts(a.raw, true);
          var v = pp.length === 1 && isHole(pp[0]) ? pp[0] : compilePath(JSON.stringify(pp.join('')));
          if (a.name === 'value') kd.value = v;
          else if (a.name === 'list') kd.list = v;
          else if (a.name === 'as') kd.as = a.raw;
        });
        if (kd.kind === 'for' && !kd.as) kd.as = 'item';
      } else {
        kd.cattrs = kd.attrs.filter(function (a) { return a.name.slice(0, 5) !== 'hint-'; }).map(function (a) {
          var name = a.name, lname = name.toLowerCase();
          if (a.raw == null) return { name: name, lname: lname, lit: BOOL[lname] ? true : '' };
          var pp = parts(a.raw, true);
          if (!pp.some(isHole)) {
            var s = pp.join('');
            return { name: name, lname: lname, lit: BOOL[lname] ? true : s };
          }
          if (pp.length === 1) return { name: name, lname: lname, whole: pp[0] };
          return { name: name, lname: lname, interp: pp };
        });
      }
      finalize(kd);
    }
  }

  // ---------- evaluation ----------
  function lookup(cp, sc) {
    if (cp.lit) return cp.v;
    var segs = cp.segs, head = segs[0], v, found = false;
    for (var f = sc.frames; f; f = f.up) {
      if (f.name === head) { v = f.val; found = true; break; }
      if (head === '$index' && f.idx !== undefined) { v = f.idx; found = true; break; }
    }
    if (!found) { var vals = sc.vals; v = vals == null ? undefined : vals[head]; }
    for (var k = 1; k < segs.length; k++) { if (v == null) return undefined; v = v[segs[k]]; }
    return v;
  }
  function str(v) {
    if (v == null || v === false || v === true) return '';
    if (Array.isArray(v)) return v.map(str).join('');
    return String(v);
  }
  function interp(pp, sc) {
    var out = '';
    for (var k = 0; k < pp.length; k++) { var x = pp[k]; out += typeof x === 'string' ? x : str(lookup(x, sc)); }
    return out;
  }

  var cfg = { base: '', top: false, indexStem: 'W00-Website-Preview', stems: null };
  var DC_LINK = /^(\/)?((?:[^\/?#:]+\/)*)([^\/?#:]+)\.dc\.html(\?[^#]*)?(#.*)?$/;
  function mapHref(v) {
    var m = DC_LINK.exec(v);
    if (!m) return null;
    var stem = m[3];
    return cfg.base + (stem === cfg.indexStem ? 'index.html' : stem + '.html') + (m[5] || '');
  }

  function renderKids(kids, sc, h) {
    var out = [];
    for (var k = 0; k < kids.length; k++) {
      var kd = kids[k];
      if (kd.text) { out.push(kd.isStatic ? kd.str : interp(kd.text, sc)); continue; }
      if (kd.kind === 'if') { out.push(kd.value && lookup(kd.value, sc) ? renderKids(kd.kids, sc, h) : null); continue; }
      if (kd.kind === 'for') {
        var list = kd.list ? lookup(kd.list, sc) : null, arr = [];
        if (list && !Array.isArray(list)) list = typeof list.length === 'number' ? Array.prototype.slice.call(list) : [];
        if (list) for (var q = 0; q < list.length; q++) arr.push(renderKids(kd.kids, { vals: sc.vals, frames: { name: kd.as, val: list[q], idx: q, up: sc.frames } }, h));
        out.push(arr);
        continue;
      }
      out.push(renderEl(kd, sc, h));
    }
    return out;
  }

  function renderEl(node, sc, h) {
    var props = {}, ca = node.cattrs, isA = node.ltag === 'a';
    for (var k = 0; k < ca.length; k++) {
      var a = ca[k], name = a.name, v;
      if (a.whole) v = lookup(a.whole, sc);
      else if (a.interp) v = interp(a.interp, sc);
      else v = a.lit;
      if (name.charCodeAt(0) === 111 && name.charCodeAt(1) === 110 && name.length > 2) { // on*
        if (typeof v === 'function') {
          // camelCase events pass through (preact/compat maps onChange->input, onFocus->focusin, ...);
          // lower-case spellings are camel-cased generically.
          if (name[2] !== name[2].toUpperCase()) name = 'on' + name[2].toUpperCase() + name.slice(3);
          props[name] = v;
        }
        continue;
      }
      if (BOOL[a.lname]) { name = BOOL[a.lname]; }
      else if (a.lname === 'value' && !a.whole && !a.interp && (node.ltag === 'input' || node.ltag === 'textarea')) name = 'defaultValue'; // literal value = HTML default
      else if (a.lname === 'class') name = 'class';
      else if (a.lname === 'for') name = 'htmlFor';
      if (isA && a.lname === 'href' && typeof v === 'string') {
        var mapped = mapHref(v);
        if (mapped !== null) { v = mapped; if (cfg.top) props.target = '_top'; }
        else if (/^https?:\/\//i.test(v) && !hasAttr(ca, 'target')) { props.target = '_blank'; props.rel = 'noopener noreferrer'; }
      }
      if (name === 'ref') { if (v && (typeof v === 'function' || typeof v === 'object')) props.ref = v; continue; }
      if (name === 'key') { props.key = v; continue; }
      props[name] = v;
    }
    var kids = node.kids.length ? renderKids(node.kids, sc, h) : null;
    if (node.ltag === 'textarea' && kids) { if (!('value' in props)) props.defaultValue = str(kids); kids = null; }
    return kids ? h(node.tag, props, kids) : h(node.tag, props);
  }
  function hasAttr(ca, n) { for (var k = 0; k < ca.length; k++) if (ca[k].lname === n) return true; return false; }

  // ---------- DCLogic ----------
  // The board's `class Component extends DCLogic` is NOT itself the Preact component (its method names could
  // collide with Preact instance fields such as `base`). A small Preact host owns the state and lifecycle and
  // forwards them; DCLogic exposes props / state / setState / forceUpdate backed by that host.
  function DCLogic(props) { this.__dcProps = props || {}; }
  Object.defineProperty(DCLogic.prototype, 'state', {
    configurable: true,
    get: function () { return this.__dcHost ? this.__dcHost.state : (this.__dcInit || (this.__dcInit = {})); },
    set: function (v) { if (this.__dcHost) this.__dcHost.state = v; else this.__dcInit = v; }
  });
  Object.defineProperty(DCLogic.prototype, 'props', {
    configurable: true,
    get: function () { return this.__dcHost ? this.__dcHost.props : this.__dcProps; },
    set: function (v) { this.__dcProps = v; }
  });
  DCLogic.prototype.setState = function (update, cb) {
    var self = this, host = this.__dcHost;
    if (!host) { var s = this.state; Object.assign(s, typeof update === 'function' ? update(Object.assign({}, s), this.props) : update); return; }
    host.setState(update, cb ? function () { cb.call(self); } : undefined);
  };
  DCLogic.prototype.forceUpdate = function (cb) {
    var self = this;
    if (this.__dcHost) this.__dcHost.forceUpdate(cb ? function () { cb.call(self); } : undefined);
  };

  function makeHost(P, ast, Logic, label) {
    var h = P.h;
    function Host(props, context) {
      P.Component.call(this, props, context);
      var logic = new Logic(props);
      this.state = logic.__dcInit || {};
      logic.__dcHost = this;
      this.__dcLogic = logic;
    }
    Host.prototype = Object.create(P.Component.prototype);
    Host.prototype.constructor = Host;
    Host.prototype.render = function () {
      var logic = this.__dcLogic, vals;
      try { vals = typeof logic.renderVals === 'function' ? logic.renderVals() : {}; }
      catch (e) { console.error('[dc] renderVals failed in ' + label, e); throw e; }
      return h(P.Fragment, null, renderKids(ast.kids, { vals: vals || {}, frames: null }, h));
    };
    Host.prototype.componentDidMount = function () { var l = this.__dcLogic; if (typeof l.componentDidMount === 'function') l.componentDidMount(); };
    Host.prototype.componentDidUpdate = function (pp, ps, snap) { var l = this.__dcLogic; if (typeof l.componentDidUpdate === 'function') l.componentDidUpdate(pp, ps, snap); };
    Host.prototype.componentWillUnmount = function () { var l = this.__dcLogic; if (typeof l.componentWillUnmount === 'function') l.componentWillUnmount(); };
    Host.prototype.shouldComponentUpdate = function (np, ns) { var l = this.__dcLogic; return typeof l.shouldComponentUpdate === 'function' ? l.shouldComponentUpdate(np, ns) : true; };
    Host.prototype.getSnapshotBeforeUpdate = function (pp, ps) { var l = this.__dcLogic; return typeof l.getSnapshotBeforeUpdate === 'function' ? l.getSnapshotBeforeUpdate(pp, ps) : undefined; };
    return Host;
  }

  // ---------- links: '#', '#id', in-page scrolling ----------
  function installLinkHandler() {
    document.addEventListener('click', function (e) {
      if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      var a = e.target && e.target.closest ? e.target.closest('a[href]') : null;
      if (!a) return;
      var href = a.getAttribute('href');
      if (href === '#' || href === '') { e.preventDefault(); return; }
      if (href.charAt(0) === '#') {
        e.preventDefault();
        var id = decodeURIComponent(href.slice(1)), el = document.getElementById(id) || document.getElementsByName(id)[0];
        if (el && el.scrollIntoView) el.scrollIntoView({ block: 'start' });
        // no such element: the hash is a route the board reads (e.g. #legal/<id>, #cookie-settings) — set it so
        // 'hashchange' fires, as a real address-bar hash would
        else if (location.hash !== href) location.hash = href;
      }
    });
  }

  // ---------- location seen by board scripts ----------
  // Boards navigate with location.assign / replace / href = 'X25-Prototype-AdminPlans.dc.html#sec/tab'.
  // Location methods cannot be patched, so each board script gets this stand-in as its `location`:
  // reads go to the real location; .dc.html targets are mapped to the generated pages (top window when framed).
  function makeLocation() {
    var L = global.location;
    function go(u, rep) {
      var s = String(u), win = global, m = mapHref(s);
      if (m !== null) {
        s = new URL(m, L.href).href;
        if (cfg.top) { try { if (global.top && global.top.location.href) win = global.top; } catch (e) { win = global; } }
      }
      if (rep) win.location.replace(s); else win.location.assign(s);
    }
    var o = {
      assign: function (u) { go(u, false); },
      replace: function (u) { go(u, true); },
      reload: function () { L.reload(); },
      toString: function () { return L.href; }
    };
    ['hash', 'host', 'hostname', 'origin', 'pathname', 'port', 'protocol', 'search', 'ancestorOrigins'].forEach(function (k) {
      Object.defineProperty(o, k, { enumerable: true, get: function () { return L[k]; }, set: function (v) { if (k === 'hash' || k === 'search') L[k] = v; } });
    });
    Object.defineProperty(o, 'href', { enumerable: true, get: function () { return L.href; }, set: function (v) { go(v, false); } });
    return o;
  }

  function mount(opts, factory) {
    var P = global.preact;
    var ast = parse(opts.tpl);
    if (ast.issues.length) console.warn('[dc] template notes for ' + opts.stem + ': ' + ast.issues.slice(0, 5).join('; '));
    // fresh DCLogic subclass per board so boards never share prototype state
    function BoardLogic(props) { DCLogic.call(this, props); }
    BoardLogic.prototype = Object.create(DCLogic.prototype);
    BoardLogic.prototype.constructor = BoardLogic;
    var Logic = factory(BoardLogic, typeof location !== 'undefined' ? makeLocation() : undefined);
    var Host = makeHost(P, ast, Logic, opts.stem);
    var el = document.getElementById('dc-root');
    P.render(P.h(Host, Object.assign({}, opts.props || {})), el);
    global.__dcMounted = true;
  }

  var api = {
    parse: parse, mapHref: mapHref, config: cfg,
    mount: function (opts, factory) {
      cfg.base = opts.base || '';
      cfg.top = !!opts.framed;
      if (typeof document !== 'undefined') installLinkHandler();
      mount(opts, factory);
    }
  };
  global.DCRuntime = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof window !== 'undefined' ? window : globalThis);

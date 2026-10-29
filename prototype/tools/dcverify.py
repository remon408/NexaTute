#!/usr/bin/env python3
"""Verify a .dc.html: every template hole resolves in every language; key parity vs bn.
usage: dcverify.py FILE [extra_node_test.js] [--state JSON ...]
Extra states: each --state JSON is merged into the component state before rendering (for all langs)."""
import re, sys, json, subprocess, os, tempfile

f = sys.argv[1]
extra = None
states = [{}]
args = sys.argv[2:]
i = 0
while i < len(args):
    if args[i] == '--state':
        states.append(json.loads(args[i + 1])); i += 2
    else:
        extra = args[i]; i += 1
src = open(f, encoding='utf-8').read()
script = re.search(r'<script type="text/x-dc"[^>]*>(.*?)</script>', src, re.S).group(1)
tpl = re.search(r'<x-dc>(.*?)</x-dc>', src, re.S).group(1)
tpl = re.sub(r'<helmet>.*?</helmet>', '', tpl, flags=re.S)
tpl = re.sub(r'<!--.*?-->', '', tpl, flags=re.S)

# walk tags, keep a stack of sc-for / sc-if frames
holes = []
stack = []
pos = 0
tag_re = re.compile(r'<(/?)([a-zA-Z][\w-]*)([^>]*)>|\{\{\s*([^}]+?)\s*\}\}', re.S)
for m in tag_re.finditer(tpl):
    if m.group(4) is not None:
        holes.append({'path': m.group(4), 'chain': [dict(x) for x in stack]})
        continue
    close, name, attrs = m.group(1), m.group(2), m.group(3)
    if name in ('sc-for', 'sc-if'):
        if close:
            stack.pop()
        else:
            fr = {'type': name}
            if name == 'sc-for':
                fr['list'] = re.search(r'list="\{\{\s*([^}]+?)\s*\}\}"', attrs).group(1)
                fr['as'] = re.search(r'\bas="([^"]+)"', attrs).group(1)
            else:
                fr['value'] = re.search(r'value="\{\{\s*([^}]+?)\s*\}\}"', attrs).group(1)
            stack.append(fr)
    # holes inside attributes of this tag (except hint-*, sc-for list / sc-if value handled as frames)
    if not close:
        for am in re.finditer(r'([\w-]+)="\{\{\s*([^}]+?)\s*\}\}"', attrs):
            an, ap = am.group(1), am.group(2)
            if an.startswith('hint-'):
                continue
            if name == 'sc-for' and an == 'list':
                holes.append({'path': ap, 'chain': [dict(x) for x in stack[:-1]]}); continue
            if name == 'sc-if' and an == 'value':
                holes.append({'path': ap, 'chain': [dict(x) for x in stack[:-1]]}); continue
            holes.append({'path': ap, 'chain': [dict(x) for x in stack]})
assert not stack, 'unbalanced sc-for/sc-if'
# attribute holes were also matched by the generic {{ }} branch? no: finditer consumes whole tag first.

node = r'''
class DCLogic{constructor(){this.state={};this.props=JSON.parse(process.env.DCPROPS||"{}");} setState(p){Object.assign(this.state,p);}}
global.setInterval=function(){return 0;}; global.clearInterval=function(){};
''' + script + r'''
const holes = JSON.parse(require('fs').readFileSync(process.argv[2],'utf8')); const states = JSON.parse(require('fs').readFileSync(process.argv[3],'utf8'));
function get(scope, path){ if(/^(true|false|null|\d+)$/.test(path)) return JSON.parse(path);
  const parts = path.split('.'); let v = (parts[0] in scope.vars) ? scope.vars[parts[0]] : scope.root[parts[0]];
  for (let i=1;i<parts.length;i++){ if(v===undefined||v===null) return undefined; v=v[parts[i]]; } return v; }
let problems = [], count = 0;
function walk(h, scope, ci){
  if (ci === h.chain.length){ count++; const v = get(scope, h.path); if (v === undefined) problems.push(h.path + ' [' + Object.keys(scope.vars).join(',') + ']'); return; }
  const fr = h.chain[ci];
  if (fr.type === 'sc-if'){ if (get(scope, fr.value)) walk(h, scope, ci+1); return; }
  const list = get(scope, fr.list); if (!Array.isArray(list)) { problems.push('not a list: ' + fr.list); return; }
  list.forEach(it => { const vars = Object.assign({}, scope.vars); vars[fr.as] = it; walk(h, {root: scope.root, vars}, ci+1); });
}
const C = Component; const probe = new C(); const UI = probe.uiText ? probe.uiText() : null;
const langs = UI ? Object.keys(UI) : ['bn'];
const out = {};
for (const st of states) for (const lang of langs){
  const c = new C(); c.state = Object.assign({lang}, st); let root;
  try { root = c.renderVals(); } catch(e){ problems.push('renderVals threw for '+lang+' '+JSON.stringify(st)+': '+e.stack.split('\n').slice(0,3).join(' | ')); continue; }
  for (const h of holes) walk(h, {root, vars:{}}, 0);
}
// key parity vs bn (deep)
function keys(o, p, acc){ if (o && typeof o === 'object' && !Array.isArray(o)) { Object.keys(o).forEach(k => keys(o[k], p ? p+'.'+k : k, acc)); } else if (Array.isArray(o)) { acc.add(p + '[' + o.length + ']'); o.forEach((x,i)=>{ if (x && typeof x==='object') keys(x, p+'['+i+']', acc); }); } else acc.add(p + ':' + typeof o); return acc; }
let parity = [];
if (UI && UI.bn){ const base = keys(UI.bn, '', new Set());
  for (const l of langs){ if (l==='bn') continue; const k = keys(UI[l], '', new Set());
    for (const x of base) if (!k.has(x)) parity.push(l + ' missing ' + x);
    for (const x of k) if (!base.has(x)) parity.push(l + ' extra ' + x); } }
const uniq = [...new Set(problems)];
console.log(JSON.stringify({langs, holes: holes.length, checks: count, problems: uniq.slice(0,40), nproblems: uniq.length, parity: parity.slice(0,40), nparity: parity.length}, null, 1));
'''
if extra:
    node += '\n' + open(extra, encoding='utf-8').read()
tmp = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_dcv_run_%d.js' % os.getpid())
open(tmp, 'w', encoding='utf-8').write(node)
hf = tmp + '.holes.json'; sf = tmp + '.states.json'
open(hf, 'w').write(json.dumps(holes)); open(sf, 'w').write(json.dumps(states))
r = subprocess.run(['node', tmp, hf, sf], capture_output=True, text=True)
print(r.stdout[-20000:]); print(r.stderr[-4000:])
for _f in (tmp, hf, sf):
    try: os.remove(_f)
    except OSError: pass

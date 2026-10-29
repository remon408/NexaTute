// Minimal static renderer for .dc.html snapshots (visual QA only).
// usage: node dcrender.js FILE OUT.html '{"lang":"bn",...}'
const fs = require('fs');
const [file, out, stJson] = process.argv.slice(2);
const src = fs.readFileSync(file, 'utf8');
const script = src.match(/<script type="text\/x-dc"[^>]*>([\s\S]*?)<\/script>/)[1];
let tpl = src.match(/<x-dc>([\s\S]*?)<\/x-dc>/)[1];
const helmet = (tpl.match(/<helmet>([\s\S]*?)<\/helmet>/) || ['', ''])[1];
tpl = tpl.replace(/<helmet>[\s\S]*?<\/helmet>/, '').replace(/<!--[\s\S]*?-->/g, '');
global.setInterval = () => 0; global.clearInterval = () => {};
const DCLogic = class { constructor() { this.state = {}; } setState(p) { Object.assign(this.state, p); } };
const Component = new Function('DCLogic', script + '\nreturn Component;')(DCLogic);
const c = new Component(); c.state = JSON.parse(stJson || '{}');
const root = c.renderVals();
// attribute pre-pass: drop events, make boolean attrs conditional
tpl = tpl.replace(/<([a-zA-Z][\w-]*)([^>]*)>/g, (m, name, attrs) => {
  if (name === 'sc-for' || name === 'sc-if') return m;
  attrs = attrs.replace(/\s+on[A-Z]\w*="\{\{[^}]*\}\}"/g, '');
  attrs = attrs.replace(/\s+(disabled|checked|selected)="\{\{\s*([^}]+?)\s*\}\}"/g, (mm, a, p) => ' {{?' + a + ' ' + p + '}}');
  return '<' + name + attrs + '>';
});
// tokenize into tree
const re = /<sc-for\s+list="\{\{\s*([^}]+?)\s*\}\}"\s+as="([^"]+)"[^>]*>|<sc-if\s+value="\{\{\s*([^}]+?)\s*\}\}"[^>]*>|<\/sc-for>|<\/sc-if>|\{\{(\?\w+ )?\s*([^}]+?)\s*\}\}/g;
const rootNode = { kids: [] }; const stack = [rootNode]; let last = 0, m;
while ((m = re.exec(tpl))) {
  const top = stack[stack.length - 1];
  if (m.index > last) top.kids.push({ text: tpl.slice(last, m.index) });
  last = re.lastIndex;
  if (m[1]) { const n = { type: 'for', list: m[1], as: m[2], kids: [] }; top.kids.push(n); stack.push(n); }
  else if (m[3]) { const n = { type: 'if', value: m[3], kids: [] }; top.kids.push(n); stack.push(n); }
  else if (m[0] === '</sc-for>' || m[0] === '</sc-if>') stack.pop();
  else top.kids.push({ hole: m[5], bool: m[4] ? m[4].slice(1).trim() : null });
}
if (last < tpl.length) rootNode.kids.push({ text: tpl.slice(last) });
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
function get(vars, p) { if (/^(true|false|null|\d+)$/.test(p)) return JSON.parse(p); const parts = p.split('.'); let v = parts[0] in vars ? vars[parts[0]] : root[parts[0]]; for (let i = 1; i < parts.length; i++) { if (v == null) return undefined; v = v[parts[i]]; } return v; }
const missing = new Set();
function render(node, vars) {
  return node.kids.map(k => {
    if (k.text !== undefined) return k.text;
    if (k.hole !== undefined) { const v = get(vars, k.hole); if (k.bool) return v ? k.bool : ''; if (v === undefined) { missing.add(k.hole); return ''; } return esc(v); }
    if (k.type === 'if') return get(vars, k.value) ? render(k, vars) : '';
    const list = get(vars, k.list) || []; return list.map(it => render(k, Object.assign({}, vars, { [k.as]: it }))).join('');
  }).join('');
}
const body = render(rootNode, {});
fs.writeFileSync(out, '<!doctype html><html><head><meta charset="utf-8">' + helmet + '</head><body style="margin:0">' + body + '</body></html>');
if (missing.size) console.log('missing', [...missing]);

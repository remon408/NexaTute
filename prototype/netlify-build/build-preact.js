const esbuild = require('/opt/npm-tools/node_modules/esbuild');
const path = require('path'); const fs = require('fs');
const P = path.join(__dirname, 'preact-src');
const map = { 'preact': 'src/index.js', 'preact/hooks': 'hooks/src/index.js', 'preact/compat': 'compat/src/index.js' };
const mc = JSON.parse(fs.readFileSync(path.join(__dirname, 'mangle-cache.json'), 'utf8'));
esbuild.build({
  entryPoints: [path.join(__dirname, 'vendor-entry.js')], bundle: true, minify: true, format: 'iife', target: 'es2017',
  legalComments: 'none', outfile: path.join(__dirname, 'preact-bundle.js'),
  mangleProps: /^_[^_]/, reserveProps: /^(_renderers|__source|__self)$/, mangleCache: mc,
  define: { 'process.env.NODE_ENV': '"production"' },
  plugins: [{ name: 'p', setup(b) { b.onResolve({ filter: /^preact(\/(hooks|compat))?$/ }, a => ({ path: path.join(P, map[a.path]) })); } }]
}).then(r => { console.log('ok', JSON.stringify(r.warnings).slice(0, 500)); }).catch(e => { console.error(e.message); process.exit(1); });

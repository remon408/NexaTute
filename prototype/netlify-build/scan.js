const fs=require('fs'), path=require('path');
const R=require(path.join(__dirname,'src/dc-runtime.js'));
const dir=process.argv[2];
const BLOCK=new Set('address article aside blockquote details dialog div dl fieldset figcaption figure footer form h1 h2 h3 h4 h5 h6 header hgroup hr main menu nav ol p pre section table ul'.split(' '));
for (const f of fs.readdirSync(dir).filter(f=>f.endsWith('.dc.html')).sort()){
  const src=fs.readFileSync(path.join(dir,f),'utf8');
  let tpl=src.match(/<x-dc>([\s\S]*?)<\/x-dc>/)[1];
  const helmet=(tpl.match(/<helmet>([\s\S]*?)<\/helmet>/)||['',''])[1];
  tpl=tpl.replace(/<helmet>[\s\S]*?<\/helmet>/,'');
  const ast=R.parse(tpl);
  const out=[]; const tags={};
  (function walk(n, anc){ for(const k of n.kids||[]){ if(k.tag){ tags[k.ltag]=(tags[k.ltag]||0)+1; if(BLOCK.has(k.ltag)){ const pi=anc.lastIndexOf('p'); const bi=Math.max(anc.lastIndexOf('button'),anc.lastIndexOf('table'),anc.lastIndexOf('td'),anc.lastIndexOf('th')); if(pi>=0&&pi>bi) out.push('p>'+k.ltag);} if((k.ltag==='tr'||k.ltag==='td')&&anc[anc.length-1]==='sc-for') out.push('sc-for>'+k.ltag); if(k.ltag==='option'&&anc.includes('select')&&anc[anc.length-1].startsWith('sc-')) out.push('select>sc>option'); walk(k, anc.concat(k.ltag)); } } })(ast,[]);
  const interesting=['table','select','textarea','svg','details','dialog','form','iframe','video','audio','canvas','label'].filter(t=>tags[t]).map(t=>t+':'+tags[t]).join(' ');
  console.log(f, 'issues', ast.issues.length, ast.issues.slice(0,3).join(' | '), 'pblock', out.length, [...new Set(out)].join(','), '|', interesting, '| helmetHoles', /\{\{/.test(helmet));
}

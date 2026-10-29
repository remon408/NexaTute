import json, os, re, subprocess, sys
from io import BytesIO
from PIL import Image
from playwright.sync_api import sync_playwright
SP=sys.argv[1]; ONLY=set(sys.argv[2].split(',')) if len(sys.argv)>2 else None
PROJ=os.path.join(SP,'ntd','project'); OUT=os.path.join(SP,'s2','fix14','thumbs','shots'); REND=os.path.join(SP,'s2','fix14','thumbs','render')
os.makedirs(OUT,exist_ok=True); os.makedirs(REND,exist_ok=True)
RJ=os.path.join(SP,'s2','site','tools','dcrender_props.js')
canvas=json.load(open(os.path.join(PROJ,'canvas.json')))['boards']
w00=open(os.path.join(PROJ,'W00-Website-Preview.dc.html'),encoding='utf-8').read()
rows=re.findall(r"B\('([^']+)', '([^']+)', '(\w)', '(\w+)', '(\w+)', (\d+), (\d+), '(\w+)'\)",w00)
fit={r[0]:r[7] for r in rows}
rep={}
with sync_playwright() as p:
    br=p.chromium.launch()
    for stem,f in fit.items():
        if ONLY and stem not in ONLY: continue
        b=canvas[stem+'.dc.html']; out_html=os.path.join(REND,stem+'.html')
        r=subprocess.run(['node',RJ,os.path.join(PROJ,stem+'.dc.html'),out_html,'{}'],capture_output=True,text=True)
        if r.returncode: rep[stem]='FAIL '+r.stderr[-200:]; continue
        if f=='phone': vw,vh=390,844
        else: vw,vh=b['w'],b['h']
        pg=br.new_page(viewport={'width':vw,'height':vh}); pg.route('**/fonts.g*/**',lambda rt: rt.abort())
        pg.goto('file://'+out_html); pg.wait_for_timeout(int(os.environ.get("WAIT","200")))
        png=pg.screenshot(clip={'x':0,'y':0,'width':vw,'height':vh}); pg.close()
        im=Image.open(BytesIO(png)).convert('RGB')
        tw=360 if f=='phone' else 720; th=round(vh*tw/vw)
        im=im.resize((tw,th),Image.LANCZOS); im.save(os.path.join(OUT,stem+'.webp'),'WEBP',quality=70,method=6)
        rep[stem]=(tw,th)
    br.close()
json.dump(rep,open(os.path.join(SP,'s2','fix14','thumbs','rep.json'),'w'),indent=0)
print(rep)

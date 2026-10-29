# find page of each heading in the PDF (search after Contents pages)
import json, subprocess, sys, re
M=sys.argv[1]; pdf=sys.argv[2]
heads=json.load(open(M+'/heads.json'))
n=int(re.search(r'Pages:\s+(\d+)',subprocess.run(['pdfinfo',pdf],capture_output=True,text=True).stdout).group(1))
txt=[subprocess.run(['pdftotext','-f',str(i),'-l',str(i),'-layout',pdf,'-'],capture_output=True,text=True).stdout for i in range(1,n+1)]
norm=lambda s: re.sub(r'\s+',' ',s).strip().lower()
ntxt=[norm(t) for t in txt]
# skip front + contents pages: start after last page containing 'contents' heading list
start=0
for i,t in enumerate(ntxt):
    if t.startswith('remonlogic / remon motion studio blueprint contents') or ' contents ' in t[:120]: start=i+1
res={}; cur=start; miss=[]
for k,(lvl,h) in enumerate(heads):
    key=norm(h)[:60]
    found=None
    for i in range(cur,n):
        if key in ntxt[i]: found=i; break
    if found is None: miss.append(h); continue
    res[k]=found+1; cur=found
json.dump(res,open(M+'/toc_pages.json','w'))
print('pages',n,'found',len(res),'of',len(heads),'missing',miss[:5])

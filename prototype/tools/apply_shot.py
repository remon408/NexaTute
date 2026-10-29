import json, re, sys
SP = sys.argv[1]
W = SP + '/ntd/project/W00-Website-Preview.dc.html'
rep = json.load(open(SP + '/s2/fix14/thumbs/rep.json'))
urls = json.load(open(SP + '/s2/fix14/thumbs/urls.json'))  # stem -> url
s = open(W, encoding='utf-8').read()
n_shot = n_size = 0
for stem, url in urls.items():
    s, k = re.subn(r"('" + re.escape(stem) + r"': )'[^']*'", lambda m: m.group(1) + "'" + url + "'", s)
    n_shot += k
for stem, v in rep.items():
    if isinstance(v, str):
        continue
    tw, th = v
    s, k = re.subn(r"(B\('" + re.escape(stem) + r"', '[^']+', '\w', '\w+', '\w+', )\d+, \d+",
                   lambda m: m.group(1) + f"{tw}, {th}", s)
    n_size += k
open(W, 'w', encoding='utf-8').write(s)
print('shot', n_shot, 'size', n_size)

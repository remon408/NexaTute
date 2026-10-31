# INTEGRATION.md: 8 board splits integrated (31 Oct 2026)

Work folder: `integrate/` (nothing in `/home/claude/nexatute` was edited, committed or pushed). Result boards: `integrate/project/` (72 boards + canvas.json). Copies of the inputs before any edit: `integrate/before/` (project/, urls.json, manifest.json, xlinks.py). Scripts used: `integrate/tools/` (`oracle.js` route oracle, `repoint.js`, `sync_a.py`, `sync_b.py`, `registry.py`, checkers, `mkmd.py` + `INTEGRATION.tpl.md` build this file). Raw verifier outputs: `integrate/verify_final/`.

Method note: a "route oracle" (`tools/oracle.js`) loads a board's own script in node with a stubbed `location`, sets `location.hash`, runs the board's `st()` and `componentDidMount()` and records where the board redirects. So every link/route result below comes from the boards' own code, not only from the split notes.

## 0. One bug found and fixed (please read)

`X12-Prototype-Institute.dc.html` and `X12b-Prototype-Institute-Ops.dc.html`, as delivered by the X12 split, had an EMPTY method `secGo(h) {  }` (the split's dead-code pass removed the body; `split/X12/finA.html` and `midA.html` already show it, `cutA.html` still has it). Effect: every cross-board jump of X12 did nothing (redirect of an old hash such as `#staff`, the `go2()` buttons, KPI tiles, bell). I restored the line from `cutA.html` in both boards: `secGo(h) { try { if (typeof location !== 'undefined' && location) location.href = h; } catch (e) {} }`. This is the only code change outside the task list. The files in `split/X12/` still contain the bug; if the split is rebuilt (`run.sh`), `s2.js` must keep `secGo`. Checked after the fix with the oracle: X12 `#staff` -> X12b, X12b `#people` -> X12. A grep of all 72 boards for methods with an empty body finds nothing else.

## 1. Route map (moved routes -> new board)

Generated with the oracle (the old board loads the hash and redirects; chains followed to the board that finally holds it). The fragment never changes. A bare board link (no fragment) keeps pointing at the old board = its first/default section.

| From -> to | Fragments |
|---|---|
| `X07#...` -> `X07b` | `#rec` `#flag` `#cat` `#spk` `#code` `#cert` `#minor` `#emp` |
| `X07#...` -> `X07c` | `#merit` `#battle` `#papers` `#allx` `#eday` `#hub` |
| `X10#...` -> `X10b` | `#acct` `#acct/pl` `#acct/jr` `#acct/led` `#acct/tb` `#acct/vat` `#acct/appr` `#acct/recv` `#acct/pay` `#acct/hr` `#acct/vend` `#acct/loan` `#acct/inv` `#acct/log` `#acct/exp` `#roles` `#roles/people` `#roles/perms` `#roles/rules` `#roles/review` `#roles/log` `#roles/pk` `#roles/acc` |
| `X12#...` -> `X12b` | `#staff` `#bill` `#special` `#org` `#mentor` `#reports` `#msg` `#notif` `#atlas` `#classreports` |
| `X14#...` -> `X14b` | `#gpu` `#maint` `#gpu/cap` `#gpu/lk` `#gpu/ing` `#gpu/beta` `#gpu/bdash` `#gpu/wn` `#gpu/video` `#gpu/vid` `#gpu/edge` `#gpu/own` `#gpu/syn` `#gpu/poll` `#gpu/adm` `#maint/sw` `#maint/thr` `#maint/swset` `#maint/lt` `#maint/wnn` |
| `X16#...` -> `X16b` | `#mf` `#disc` `#seats` `#gift` `#ref` `#pay` `#vat` `#kpi` `#sch` `#qt` `#rck` `#aiq` `#fil` `#enb` |
| `X16#...` -> `X16c` | `#rec` `#anti` `#cat` `#nte` `#spk` `#cod` `#crt` `#prc` `#emp` `#api` |
| `X20#...` -> `X20b` | `#plans` `#proof` `#safety` `#playboom` `#mindforge` `#hall` `#institutions` |
| `X20#...` -> `X20c` | `#notes` `#roadmap` `#faq` `#start` `#beta-list` |
| `X25#...` -> `X25b` | `#plans/plat` `#plans/adm` `#plans/adm21` `#plans/wl21` `#plans/cg21` `#plans/voice` `#plans/live` `#plans/mf` `#plans/legal` `#plans/otp` `#plans/pro` `#plans/eng` `#plans/signup` `#plans/lgx` `#plans/otp17` |
| `X25#...` -> `X25c` | `#plans/pp` `#plans/prices` `#plans/storage` `#plans/disc` `#plans/refund` `#plans/addon` `#plans/dpass` `#plans/rate` `#plans/usd` `#plans/trial` `#plans/bill` `#plans/gw` `#plans/stg` `#plans/stadd` `#plans/strl` |
| `X25#...` -> `X26` | `#plans/rules` `#plans/beta` `#plans/cls` `#plans/net` `#plans/login` `#plans/well` `#plans/streak` `#plans/gsms` `#plans/calm` `#plans/cflow` `#plans/bteach` `#plans/sh` `#plans/shx` `#plans/free` `#plans/mfl` `#plans/pbl` `#plans/pbf` `#plans/minu` `#plans/pap` `#plans/hot` `#plans/fbtn` `#plans/fbcat` `#plans/fbsla` `#plans/aierr` `#plans/offm` `#plans/bcomm` `#plans/xlink` `#plans/weak` `#plans/recmis` `#plans/imgc` `#plans/pref` `#plans/tq` |
| `X25#...` -> `X26b` | `#plans/engage` `#plans/egsh` `#plans/egdb` `#plans/egfq` `#plans/eggs` `#plans/egbt` `#plans/egar` `#plans/egtt` `#plans/egnr` `#plans/egmm` `#plans/eggm` `#plans/egci` `#plans/egle` `#plans/egbp` `#plans/more` `#plans/ksht` `#plans/khlp` `#plans/kptm` `#plans/kjob` `#plans/kpapi` `#plans/kswap` `#plans/kroad` `#plans/strategic` `#plans/lea` `#plans/lvm` `#plans/ley` `#plans/lsrc` `#plans/lbot` `#plans/trust` `#plans/bots` `#plans/mss` `#plans/msb` `#plans/mwl` `#plans/mcom` `#plans/mspon` `#plans/mwif` `#plans/more2027` `#plans/vac` `#plans/vc` |
| `X26#...` -> `X25` | `#plans/mx` `#plans/loop` `#plans/hub` `#plans/crash` `#plans/cap` `#plans/price` `#plans/sales` `#plans/tier` `#plans/tier2` `#plans/placement` `#plans/limits` `#plans/a11yrep` `#plans/adapt` `#plans/advice` `#plans/allex` `#plans/anon` `#plans/atlas` `#plans/avatar` `#plans/badges` `#plans/batch` `#plans/bdsl` `#plans/bdslcap` `#plans/bdslrec` `#plans/calc` `#plans/cert` `#plans/certx` `#plans/chat` `#plans/code` `#plans/creport` `#plans/crp1` ... (151 ids in all; full list: tools/routemap.md) |
| `X26#...` -> `X25b` | `#plans/plat` `#plans/adm` `#plans/adm21` `#plans/wl21` `#plans/cg21` `#plans/voice` `#plans/live` `#plans/mf` `#plans/legal` `#plans/otp` `#plans/pro` `#plans/eng` `#plans/signup` `#plans/lgx` `#plans/otp17` |
| `X26#...` -> `X25c` | `#plans/pp` `#plans/prices` `#plans/storage` `#plans/disc` `#plans/refund` `#plans/addon` `#plans/dpass` `#plans/rate` `#plans/usd` `#plans/trial` `#plans/bill` `#plans/gw` `#plans/stg` `#plans/stadd` `#plans/strl` |
| `X26#...` -> `X26b` | `#plans/engage` `#plans/egsh` `#plans/egdb` `#plans/egfq` `#plans/eggs` `#plans/egbt` `#plans/egar` `#plans/egtt` `#plans/egnr` `#plans/egmm` `#plans/eggm` `#plans/egci` `#plans/egle` `#plans/egbp` `#plans/more` `#plans/ksht` `#plans/khlp` `#plans/kptm` `#plans/kjob` `#plans/kpapi` `#plans/kswap` `#plans/kroad` `#plans/strategic` `#plans/lea` `#plans/lvm` `#plans/ley` `#plans/lsrc` `#plans/lbot` `#plans/trust` `#plans/bots` `#plans/mss` `#plans/msb` `#plans/mwl` `#plans/mcom` `#plans/mspon` `#plans/mwif` `#plans/more2027` `#plans/vac` `#plans/vc` |
| `X07b#...` -> `X07` | `#mcq` `#omr` `#short` `#mixed` |
| `X07b#...` -> `X07c` | `#merit` `#battle` `#papers` `#allx` `#eday` `#hub` |
| `X07c#...` -> `X07` | `#mcq` `#omr` `#short` `#mixed` |
| `X07c#...` -> `X07b` | `#rec` `#flag` `#cat` `#spk` `#code` `#cert` `#minor` `#emp` |
| `X10b#...` -> `X10` | `#over` `#usage` `#inst` `#prog` `#guard` `#sched` `#help` |
| `X12b#...` -> `X12` | `#over` `#people` `#classes` `#study` `#assess` `#notice` |
| `X14b#...` -> `X14` | `#models` `#spend` `#esc` `#cost` `#flags` `#backup` `#appr` `#inc` `#log` |
| `X16b#...` -> `X16` | `#cache` `#wrong` `#circ` `#tr` `#gloss` `#gate` `#tch` `#qa` `#weak` `#bdsl` `#kpid` `#anyc` `#ap` `#log` |
| `X16b#...` -> `X16c` | `#rec` `#anti` `#cat` `#nte` `#spk` `#cod` `#crt` `#prc` `#emp` `#api` |
| `X16c#...` -> `X16` | `#cache` `#wrong` `#circ` |
| `X16c#...` -> `X16b` | `#pay` `#disc` `#mf` `#kpi` |
| `X20b#...` -> `X20` | `#hero` `#paths` `#how` `#fit` `#courses` `#crash` `#hub` |
| `X20b#...` -> `X20c` | `#notes` `#roadmap` `#faq` `#start` |
| `X20c#...` -> `X20` | `#hero` `#paths` `#how` `#fit` `#courses` `#crash` `#hub` |
| `X20c#...` -> `X20b` | `#plans` `#proof` `#safety` `#playboom` `#mindforge` `#hall` `#institutions` |
| `X20d#...` -> `X20` | `#hero` `#how` |
| `X20d#...` -> `X20b` | `#plans` |
| `X20d#...` -> `X20c` | `#roadmap` |

Notes: X20 `#notes` = Notes teaser on X20c; `#notes/<slug>` = a blog post on X20d (X20, X20b and X20c redirect old post hashes to X20d). X20 itself keeps hero, paths, how, fit, courses, English, SSC/HSC, crash, hub, demo, cookie-settings. X07 keeps pick, mcq, omr, result, review, eve, tf, fill, match, short, wr, mixed. X25 keeps `#plans/mx` and every matrix-row id (the default). X26 keeps `#plans/rules`, `cls`, `net`, `login`, `well`, `streak`, `gsms`, `calm`, `cflow`, `bteach`, `sh`, `shx`, `free`, `mfl`, `pbl`, `pbf`, `minu`, `pap`, `hot`, `weak`, `recmis`, `imgc`, `pref`, `tq`, `beta` and the Free Beta cards.

### Link changes per file (task 1): 58 hrefs in 19 files

Rule applied: every `<board>.dc.html#frag` in a non-comment line whose old board redirects that fragment to another board is repointed to that board, fragment unchanged. Bare links untouched. canvas.json has no link with a fragment (0 changes). Seven comment lines that show an old URL as an example (X07, X07b, X07c, X12, X12b, X14, X14b) are left as they are.

| File | Changed | Details |
|---|---:|---|
| D01-Learner-Desktop | 2 | `X07#hub` -> `X07c` (line 153); `X07#hub/plan` -> `X07c` (line 154) |
| X01-Prototype-Flow1 | 6 | `X07#hub` -> `X07c` (lines 791,968); `X07#battle` -> `X07c` (lines 969,1796); `X07#papers` -> `X07c` (lines 970,1796) |
| X03-Prototype-Flow3 | 1 | `X07#hub` -> `X07c` (line 408) |
| X08-Prototype-Guardian | 1 | `X20#roadmap` -> `X20c` (line 1310) |
| X11-Prototype-Tools | 2 | `X07#allx` -> `X07c` (line 275); `X07#hub/olvl/bokul` -> `X07c` (line 296) |
| X12-Prototype-Institute | 1 | `X20#roadmap` -> `X20c` (line 335) |
| X13-Prototype-LandingAI | 2 | `X20#beta-list` -> `X20c` (line 458); `X25#plans/prices` -> `X25c` (line 639) |
| X14-Prototype-Ops | 2 | `X26#plans/bots` -> `X26b` (line 656); `X26#plans/vac` -> `X26b` (line 663) |
| X14b-Prototype-Ops-Infra | 3 | `X26#plans/egbp` -> `X26b` (line 502); `X25#plans/storage` -> `X25c` (line 514); `X25#plans/adm` -> `X25b` (line 654) |
| X15-Prototype-Accounts | 1 | `X26#plans/bots` -> `X26b` (line 752) |
| X16b-Prototype-Quality-Money | 7 | `X25#plans/disc` -> `X25c` (line 739); `X14#gpu/cap` -> `X14b` (line 783); `X25#plans/refund` -> `X25c` (line 830); `X10#acct` -> `X10b` (lines 849,877); `X10#acct/pay` -> `X10b` (line 865); `X10#acct/vat` -> `X10b` (line 914) |
| X17-Prototype-Growth | 3 | `X25#plans/prices` -> `X25c` (line 501); `X16#pay` -> `X16b` (line 688); `X26#plans/mspon` -> `X26b` (line 758) |
| X18-Prototype-MindForge | 4 | `X07#hub` -> `X07c` (line 578); `X07#allx` -> `X07c` (line 637); `X07#hub/plan` -> `X07c` (line 731); `X20#roadmap` -> `X20c` (line 1397) |
| X21-Prototype-Comms | 12 | `X14#gpu/edge` -> `X14b` (lines 1139,1140,1141,1142,1143,1144); `X14#gpu/syn` -> `X14b` (lines 1139,1140,1141,1142,1143,1144) |
| X25-Prototype-AdminPlans | 1 | `X14#gpu/cap` -> `X14b` (line 647) |
| X25b-Prototype-AdminPlans-Platform | 3 | `X14#maint/lt` -> `X14b` (lines 487,551); `X14#gpu/adm` -> `X14b` (line 487) |
| X26-Prototype-AdminRules | 1 | `X14#gpu/beta` -> `X14b` (line 849) |
| X26b-Prototype-AdminRules-More | 1 | `X14#maint/lt` -> `X14b` (line 974) |
| X27-Prototype-CoAdmin | 5 | `X10#roles` -> `X10b` (line 3879); `X14#gpu/beta` -> `X14b` (line 3888); `X10#acct` -> `X10b` (lines 3901,3982,3983) |

Total 58 in 19 files. Not changed on purpose: `X20c ... 'X20d...#notes/' + BPK[k].slug` (dynamic, already the right board).

## 2. Admin sidebar, group A (`x10-menu`): X10, X10b, X25, X25b, X25c, X26, X26b, X27

Done on all eight boards (`tools/sync_a.py`, based on X10's `sidebar_sync_apply.js`):
- `<aside>` replaced by the X10/X10b one (two-shape entries: own board = button, other board = link); 5 CSS lines for link-looking entries added to the helmet; `menuVals` `sec` / `tabbed` return `href/isLink/isBtn`; bell `read` passes `aTab || roTab` too.
- ONE routing block, textually identical on all eight (only the one-line `self20()` differs): `self20, f20, sub26, subTab, own20, secHref, go20` (the X25 boards also keep `tabHref`, now `b === this.self20()`).
  - `own20(sec, tab, sub)`: acct/roles -> X10b; other sections -> X10; plans: `beta` -> X26; `mx` -> X25; `plat` -> X25b; `pp` -> X25c; `rules` -> X26b for the moved `#plans/<sub>` blocks, X26 for the others. With a `sub` (only given when a board redirects on load) `subTab(sub)` first maps the sub to its tab (lists copied from X25's `st()`: 15 platform, 15 price, 8 beta subs; the 62 rules subs are in `sub26`).
  - `go20` opens `f20()[own20(...)]` directly (`location.assign`; `replace` on load). `secHref` gives the same target as a plain link ('' for this board and for the Plans parent entry; Plans sub-entries are now links to the sister boards, as X25's own tab bar already was).
- X27: the `F` map of the "open the page of this section" code is now `this.f20()`; the `#from=` regex is `^X(1[0-9]|2[0-6])[b-d]?-[A-Za-z-]+$` (accepts X10b, X14b, X16b, X16c, X25b, X25c, X26b, X12b, X20d ...; X07b, X07c and X12 stems are not in X27's board-name table, so they show no back link, as before).
- The Co-Admin button of the new boards now sends `#from=<own stem>` (X10b, X14b, X16b, X16c, X25b, X25c, X26b) instead of the parent stem, so the assistant's back link returns to the board the person came from.

Hashes (SHA-256 of the `<aside>` template; the current-page marker is data, `mn.*.cls` / `cur`, so it is not in the template; routing block = the methods listed above with `self20` and `tabHref` normalised), from `verify_final/hashes.out`:

```
GROUP A  (x10-menu): <aside> template, SHA-256 (the current-page marker is data driven: mn.*.cls / cur, so the template itself carries no marker)
 X10-Prototype-Admin                  aside 16264 B d81ff87bf266ca4d2e4bf831e3fc29393721b9ccb21a9ef86416417b6a98593f | routing block (own20/subTab/sub26/f20/secHref/go20, self20+tabHref normalised) b5870313404707123b05fbff2c2c15bb7e74c972bbe25b990d7b0107269be20e
 X10b-Prototype-Admin-Accounts        aside 16264 B d81ff87bf266ca4d2e4bf831e3fc29393721b9ccb21a9ef86416417b6a98593f | routing block (own20/subTab/sub26/f20/secHref/go20, self20+tabHref normalised) b5870313404707123b05fbff2c2c15bb7e74c972bbe25b990d7b0107269be20e
 X25-Prototype-AdminPlans             aside 16264 B d81ff87bf266ca4d2e4bf831e3fc29393721b9ccb21a9ef86416417b6a98593f | routing block (own20/subTab/sub26/f20/secHref/go20, self20+tabHref normalised) b5870313404707123b05fbff2c2c15bb7e74c972bbe25b990d7b0107269be20e
 X25b-Prototype-AdminPlans-Platform   aside 16264 B d81ff87bf266ca4d2e4bf831e3fc29393721b9ccb21a9ef86416417b6a98593f | routing block (own20/subTab/sub26/f20/secHref/go20, self20+tabHref normalised) b5870313404707123b05fbff2c2c15bb7e74c972bbe25b990d7b0107269be20e
 X25c-Prototype-AdminPlans-Pp         aside 16264 B d81ff87bf266ca4d2e4bf831e3fc29393721b9ccb21a9ef86416417b6a98593f | routing block (own20/subTab/sub26/f20/secHref/go20, self20+tabHref normalised) b5870313404707123b05fbff2c2c15bb7e74c972bbe25b990d7b0107269be20e
 X26-Prototype-AdminRules             aside 16264 B d81ff87bf266ca4d2e4bf831e3fc29393721b9ccb21a9ef86416417b6a98593f | routing block (own20/subTab/sub26/f20/secHref/go20, self20+tabHref normalised) b5870313404707123b05fbff2c2c15bb7e74c972bbe25b990d7b0107269be20e
 X26b-Prototype-AdminRules-More       aside 16264 B d81ff87bf266ca4d2e4bf831e3fc29393721b9ccb21a9ef86416417b6a98593f | routing block (own20/subTab/sub26/f20/secHref/go20, self20+tabHref normalised) b5870313404707123b05fbff2c2c15bb7e74c972bbe25b990d7b0107269be20e
 X27-Prototype-CoAdmin                aside 16264 B d81ff87bf266ca4d2e4bf831e3fc29393721b9ccb21a9ef86416417b6a98593f | routing block (own20/subTab/sub26/f20/secHref/go20, self20+tabHref normalised) b5870313404707123b05fbff2c2c15bb7e74c972bbe25b990d7b0107269be20e
```

Click test (`tools/sbtest.js`; every sidebar entry and sub-entry of every board, rendered in en, the button's handler or the link's href captured, then the target board loads that hash): `entries tested 188 bad 1`. The one flagged entry is X26b > "Plans & modules > Rules": it is the current-page entry on X26b and stays on X26b by design (as before the split; its bare `#plans/rules` hash means the first Rules block, which lives on X26). The other 187 entries open the board that holds the section/tab in ONE navigation, with no redirect on arrival.

Redirect-chain test (`tools/hops.js`; every section, acct/roles tab, plans tab and sub id, every X07/X12/X14/X16/X20 route, on every board of its family): `(board,hash) pairs 1594 resolved in 0 hops 344 1 hop 1250 >=2 hops/missing 0`

Rendered label text of the aside (en, ar, bn): X10 = X10b character for character. X25 ... X27 differ from X10 only by the 14 labels of the Accounts sub-list (Profit & loss ... Backup & export). That sub-list is hidden (`.ns-sub.shut{display:none}`) and exists with content only on X10/X10b, because X25/X26/X27 never carried the Accounts tab names (same before the splits; adding them needs new text in 5 boards).

dcverify with 11 extra `--state` runs (sections, plans tabs, acct/roles tabs, phone drawer, tablet, rail), `--langs bn,en,hi,ur,ar,fr`: all 0 problems, 0 parity. Checks: X10 29766, X10b 43272, X25 130314, X25b 125394, X25c 111624, X26 168492, X26b 174120, X27 23880.

## 3. Admin sidebar, group B (`sbm-nav` / `ng-*`): X13, X14, X14b, X15, X16, X16b, X16c, X17, X19, X21, X22

- Label keys: X15, X16, X16b, X16c, X17, X19, X21 already used `t.nav.x10 ... x22`. X14, X14b and X22 used `t.nav.admin, ops, acc, qual, grow, mh`; X13 used `t.navx.x10 ... x22`. The aside of X14, X14b, X22 now uses `t.nav.x10 / x14 / x15 / x16 / x17 / x19`, the aside of X13 uses `t.nav.x10 ... x22`.
- Keys added in all 6 languages by copying the exact X15 literals. The existing strings were already identical to X15's in every language (0 differences), so nothing changes on screen. X14, X14b, X22: `x10, x14, x15, x16, x17, x19` added inside their `nav` object (x21 and x22 existed; the old keys `admin ... mh` are kept, each is used once outside the aside). X13: a new top-level `nav: { x10, x14, x15, x16, x17, x19, x21, x22 }` object per language (X13's `navx` stays, it is used by the rail tooltips and `navx.live`). No other aside text was touched; the own two-shape sub-lists of X14, X14b, X16, X16b, X16c are as the splits made them.
- Rendered check (en, ar, bn, fr): the nine main entries (href + label) are identical on all 11 boards (11 of 11 equal to X15 in each language).
- SHA-256 of the `<aside>` with the active marker normalised (`class="ng-it on" aria-current="page"` -> `class="ng-it"`) and the own entry's sub-list wrapper (`ng-row` + `ng-sub`, which differs per board by design) collapsed to its plain link: ONE value for all 11 (below, "(1)"). "(2)" is the hash with only the marker normalised: it differs only where the own sub-list differs (X14 = X14b, X16 = X16b = X16c).

```
GROUP B  (sbm-nav / ng-*): <aside> SHA-256 with (1) the active marker normalised AND the own entry collapsed to its plain link, i.e. own two-shape sub-list removed; (2) only the active marker normalised
 X13-Prototype-LandingAI              (1) cb411307c39c8fb7b78a5d2f9b02dfbef3825e8bb887d874c39a0707beec805d  (2) ffce0ab9158a204b
 X14-Prototype-Ops                    (1) cb411307c39c8fb7b78a5d2f9b02dfbef3825e8bb887d874c39a0707beec805d  (2) 3e90c90f260471db
 X14b-Prototype-Ops-Infra             (1) cb411307c39c8fb7b78a5d2f9b02dfbef3825e8bb887d874c39a0707beec805d  (2) 3e90c90f260471db
 X15-Prototype-Accounts               (1) cb411307c39c8fb7b78a5d2f9b02dfbef3825e8bb887d874c39a0707beec805d  (2) 3389e6f518577a71
 X16-Prototype-Quality                (1) cb411307c39c8fb7b78a5d2f9b02dfbef3825e8bb887d874c39a0707beec805d  (2) e78191763a46ff3e
 X16b-Prototype-Quality-Money         (1) cb411307c39c8fb7b78a5d2f9b02dfbef3825e8bb887d874c39a0707beec805d  (2) e78191763a46ff3e
 X16c-Prototype-Quality-ExamAid       (1) cb411307c39c8fb7b78a5d2f9b02dfbef3825e8bb887d874c39a0707beec805d  (2) e78191763a46ff3e
 X17-Prototype-Growth                 (1) cb411307c39c8fb7b78a5d2f9b02dfbef3825e8bb887d874c39a0707beec805d  (2) f3c307392ea2e938
 X19-Prototype-MarketingHub           (1) cb411307c39c8fb7b78a5d2f9b02dfbef3825e8bb887d874c39a0707beec805d  (2) c2d5b22ce32dc0f6
 X21-Prototype-Comms                  (1) cb411307c39c8fb7b78a5d2f9b02dfbef3825e8bb887d874c39a0707beec805d  (2) e9004af28bd8fe35
 X22-Prototype-AvatarVoice            (1) cb411307c39c8fb7b78a5d2f9b02dfbef3825e8bb887d874c39a0707beec805d  (2) 00a7d685994fb795
distinct (1) hashes: 1

```

## 4. Registries

- `canvas.json`: 13 entries added after their parent (page learner, w 1440, h 1000, `expand` fill, `is_interactive` true, all copied from the parent; every other top-level key untouched; file format kept: indent 1, round-trips exactly). Titles: `Xnn · Prototype: <English section list from the board's own <title>> (Play)`. Row layout: every X row is a strip at x = 0, 1520, 3040 ...; the new frames take the next slots and the following frames of the same row move right by 1,520 per inserted board (11 existing entries changed, x only). Parent titles were NOT shortened (see doubts).

```
canvas.json valid JSON; round-trips with indent=1: True
board files on disk: 72 | boards entries: 72 | order entries: 72
boards keys == files: True | order is a permutation of files (each once): True
listed files that do not exist: []
overlapping frames: 0 []
new boards present, right after parent in order:
   X07b-Prototype-Test-ExamAid.dc.html index 24 prev in order: X07-Prototype- | x,y 1520 10740 page learner
   X07c-Prototype-Test-Hub.dc.html index 25 prev in order: X07b-Prototype | x,y 3040 10740 page learner
   X10b-Prototype-Admin-Accounts.dc.html index 29 prev in order: X10-Prototype- | x,y 9120 10740 page learner
   X12b-Prototype-Institute-Ops.dc.html index 38 prev in order: X12-Prototype- | x,y 3040 11860 page learner
   X14b-Prototype-Ops-Infra.dc.html index 41 prev in order: X14-Prototype- | x,y 7600 11860 page learner
   X16b-Prototype-Quality-Money.dc.html index 44 prev in order: X16-Prototype- | x,y 3040 12980 page learner
   X16c-Prototype-Quality-ExamAid.dc.html index 45 prev in order: X16b-Prototype | x,y 4560 12980 page learner
   X20b-Prototype-Landing-Plans.dc.html index 50 prev in order: X20-Prototype- | x,y 3040 14100 page learner
   X20c-Prototype-Landing-More.dc.html index 51 prev in order: X20b-Prototype | x,y 4560 14100 page learner
   X20d-Prototype-Landing-Blog.dc.html index 52 prev in order: X20c-Prototype | x,y 6080 14100 page learner
   X25b-Prototype-AdminPlans-Platform.dc.html index 31 prev in order: X25-Prototype- | x,y 4560 15220 page learner
   X25c-Prototype-AdminPlans-Pp.dc.html index 32 prev in order: X25b-Prototype | x,y 6080 15220 page learner
   X26b-Prototype-AdminRules-More.dc.html index 34 prev in order: X26-Prototype- | x,y 9120 15220 page learner
top-level keys other than boards/order identical to before: True
existing boards whose entry changed (x shift only): 11 ; non-x changes: []
```

- `W00-Website-Preview.dc.html`: for each of the 8 parents, in all 6 language maps the new boards get an entry right after the parent (48 text lines): `t` = parent title + ` · ` + English short name, `d` = English description. Also `B(...)` board rows (same kind / device / audience / size as the parent, id `X7b` ...), `SHOT` thumbnail = the parent's, journeys: X07b and X07c after X07 in "new", X12b after X12 in "teach", X10b / X14b / X16b / X16c after their parents in "admin", X20b / X20c / X20d after X20 in "web". Script parses (`node --check`), dcverify 0/0.
- `Main.dc.html`: `STEMS` 27 -> 40 with the 13 new stems after their parents; 13 matching labels inserted in all 6 `links` arrays (parent label + ` · ` + English short name); the tile id is now taken from the stem (`X07b` -> `X7b`; existing ids unchanged, `X0n` -> `Xn`); `hint-placeholder-count` 23 -> 40. dcverify 0/0.
- `urls.json` (thumbnail URLs): 13 stems added after their parent, same URL as the parent. `manifest.json`: 13 page entries (same fields as the parent, title = canvas title), sorted by stem as the build writes it. `xlinks.py`: Co-Admin board list +7 boards (check now says "18 admin boards"), back-link test +X10b, X25c, X26b, `X25#acct` now expects X10b, plus 19 new hash-navigation checks for the moved routes. It compiles (`py_compile`) but was NOT run (needs playwright and the built site).

### New labels that need review (English added, per your rule)

Short names (appended after the parent label in W00 `t` x 6 languages and Main `links` x 6 languages): X07b "Exam-aid pages", X07c "Exam & Admission Hub", X10b "Accounts & Roles", X12b "Operations", X14b "Infrastructure", X16b "Money & tests", X16c "Exam rules & integrity", X20b "Plans & more", X20c "Notes, roadmap, FAQ", X20d "Nexa Notes blog", X25b "Platform switches", X25c "Plans & prices", X26b "Rules (part 2)".

Descriptions (W00 `d`, English in all 6 languages; same text in canvas/manifest titles): X07b "Exam-aid pages: recovery, appeal, adaptive, speaking, coding, certificate, employer"; X07c "Exam & Admission Hub, merit list, Quiz Battle, past questions, All Exams, exam day"; X10b "Accounts and finance, roles and access"; X12b "Operations: staff, billing, reports, messages"; X14b "Infrastructure: GPU, servers, maintenance"; X16b "Money, MindForge items, tests and marking"; X16c "Exam rules and integrity"; X20b "Plans, safety, PlayBoom, MindForge, institutions"; X20c "Notes teaser, roadmap, FAQ, sign-up"; X20d "The Nexa Notes blog: list, posts, videos, newsletter"; X25b "Plans and modules: platform switches"; X25c "Plans and prices (price table)"; X26b "Rules and settings, part 2: engagement, learning, trust". They come from each board's own `<title>`; Bengali, Hindi, Urdu, Arabic and French versions are still to be written.

## 5. Verifier output

### dcverify `--langs bn,en,hi,ur,ar,fr` on every changed board (27 boards; `verify_final/*.out`)

```
D01-Learner-Desktop holes:190,checks:1290,problems:[],nproblems:0,parity:[],nparity:0
Main holes:66,checks:1686,problems:[],nproblems:0,parity:[],nparity:0
W00-Website-Preview holes:121,checks:9348,problems:[],nproblems:0,parity:[],nparity:0
X01-Prototype-Flow1 holes:1107,checks:726,problems:[],nproblems:0,parity:[],nparity:0
X03-Prototype-Flow3 holes:887,checks:1392,problems:[],nproblems:0,parity:[],nparity:0
X08-Prototype-Guardian holes:1701,checks:1488,problems:[],nproblems:0,parity:[],nparity:0
X10-Prototype-Admin holes:1684,checks:2736,problems:[],nproblems:0,parity:[],nparity:0
X10b-Prototype-Admin-Accounts holes:1932,checks:3834,problems:[],nproblems:0,parity:[],nparity:0
X11-Prototype-Tools holes:657,checks:1212,problems:[],nproblems:0,parity:[],nparity:0
X12-Prototype-Institute holes:1591,checks:2856,problems:[],nproblems:0,parity:[],nparity:0
X12b-Prototype-Institute-Ops holes:1926,checks:3738,problems:[],nproblems:0,parity:[],nparity:0
X13-Prototype-LandingAI holes:967,checks:6548,problems:[],nproblems:0,parity:[],nparity:0
X14-Prototype-Ops holes:1288,checks:3624,problems:[],nproblems:0,parity:[],nparity:0
X14b-Prototype-Ops-Infra holes:2052,checks:17676,problems:[],nproblems:0,parity:[],nparity:0
X15-Prototype-Accounts holes:1483,checks:3534,problems:[],nproblems:0,parity:[],nparity:0
X16b-Prototype-Quality-Money holes:1332,checks:3276,problems:[],nproblems:0,parity:[],nparity:0
X16c-Prototype-Quality-ExamAid holes:1097,checks:1974,problems:[],nproblems:0,parity:[],nparity:0
X17-Prototype-Growth holes:1145,checks:4148,problems:[],nproblems:0,parity:[],nparity:0
X18-Prototype-MindForge holes:1590,checks:4314,problems:[],nproblems:0,parity:[],nparity:0
X21-Prototype-Comms holes:1227,checks:2988,problems:[],nproblems:0,parity:[],nparity:0
X22-Prototype-AvatarVoice holes:919,checks:1746,problems:[],nproblems:0,parity:[],nparity:0
X25-Prototype-AdminPlans holes:1241,checks:23472,problems:[],nproblems:0,parity:[],nparity:0
X25b-Prototype-AdminPlans-Platform holes:1840,checks:22488,problems:[],nproblems:0,parity:[],nparity:0
X25c-Prototype-AdminPlans-Pp holes:1828,checks:19734,problems:[],nproblems:0,parity:[],nparity:0
X26-Prototype-AdminRules holes:3860,checks:29316,problems:[],nproblems:0,parity:[],nparity:0
X26b-Prototype-AdminRules-More holes:4114,checks:32262,problems:[],nproblems:0,parity:[],nparity:0
X27-Prototype-CoAdmin holes:801,checks:2430,problems:[],nproblems:0,parity:[],nparity:0
```

27 of 27: problems [], nproblems 0, parity [], nparity 0. The 45 boards that did not change were also run (`verify_unchanged/`, run before the last X16c edit; X16c is in the list above): 0 / 0 on all. Default state, plus the state runs of section 2.

### Sizes (`wc -c`)

```
1029453 project/X25-Prototype-AdminPlans.dc.html
 1091850 project/X20c-Prototype-Landing-More.dc.html
 1105885 project/X19-Prototype-MarketingHub.dc.html
 1129881 project/X10b-Prototype-Admin-Accounts.dc.html
 1137848 project/X12b-Prototype-Institute-Ops.dc.html
 1143125 project/X24-Prototype-Legal.dc.html
 1146215 project/X20d-Prototype-Landing-Blog.dc.html
33481150 total
>1,150,000:
>1,800,000:
board count
72
```

Largest 1,146,215 (X20d); no board over 1,150,000; none over 1,800,000.

### Global link check (`tools/linkcheck.js`, all 72 boards, non-comment lines), sidebar click test, redirect chains, rendered links

```
{"boards":72,"hrefOccurrences":395,"distinct":151,"skipped_empty_or_from":27,"bad":0}

X26b | plans/rules | stay | X26b | #plans/rules | BAD X26-Prototype-AdminRules.dc.html#plans/rules
entries tested 188 bad 1

(board,hash) pairs 1594 resolved in 0 hops 344 1 hop 1250 >=2 hops/missing 0

rendered hrefs 498 distinct 181 bad 0
```

Line 1: 395 href occurrences `<board>.dc.html#frag` (27 with empty fragment or `#from=` skipped): every target board exists, every fragment is handled by that board without a redirect hop, and every fragment token is a literal or id in that board's source (this last test is lenient: the token only has to appear in the source). Run against `before/project`, the same checker reports 58 bad = the 58 repointed links. Last line: 498 hrefs found in the rendered pages of 38 boards (default state, en; X02 and X04 cannot be rendered by the static renderer, they need props, as before): 0 hop. Sidebar targets produced by code are covered by the click test.

### canvas.json

See the block in section 4: valid JSON, 72 files = 72 entries = 72 order entries, 0 missing, 0 overlapping frames.

### lostcheck (`lostcheck.py ORIGINAL NEW`, ORIGINAL = `before/project/<board>`, NEW = the edited board; 27 boards)

```
D01-Learner-Desktop missing strings: 2 english text-like: 0
Main missing strings: 0 english text-like: 0
W00-Website-Preview missing strings: 0 english text-like: 0
X01-Prototype-Flow1 missing strings: 3 english text-like: 0
X03-Prototype-Flow3 missing strings: 1 english text-like: 0
X08-Prototype-Guardian missing strings: 1 english text-like: 0
X10-Prototype-Admin missing strings: 4 english text-like: 0
X10b-Prototype-Admin-Accounts missing strings: 5 english text-like: 0
X11-Prototype-Tools missing strings: 2 english text-like: 0
X12-Prototype-Institute missing strings: 1 english text-like: 0
X12b-Prototype-Institute-Ops missing strings: 0 english text-like: 0
X13-Prototype-LandingAI missing strings: 2 english text-like: 0
X14-Prototype-Ops missing strings: 3 english text-like: 0
X14b-Prototype-Ops-Infra missing strings: 5 english text-like: 0
X15-Prototype-Accounts missing strings: 1 english text-like: 0
X16b-Prototype-Quality-Money missing strings: 7 english text-like: 0
X16c-Prototype-Quality-ExamAid missing strings: 1 english text-like: 0
X17-Prototype-Growth missing strings: 3 english text-like: 0
X18-Prototype-MindForge missing strings: 4 english text-like: 0
X21-Prototype-Comms missing strings: 2 english text-like: 0
X22-Prototype-AvatarVoice missing strings: 0 english text-like: 0
X25-Prototype-AdminPlans missing strings: 6 english text-like: 0
X25b-Prototype-AdminPlans-Platform missing strings: 8 english text-like: 0
X25c-Prototype-AdminPlans-Pp missing strings: 6 english text-like: 0
X26-Prototype-AdminRules missing strings: 5 english text-like: 0
X26b-Prototype-AdminRules-More missing strings: 6 english text-like: 0
X27-Prototype-CoAdmin missing strings: 7 english text-like: 0
```

"english text-like: 0" on all 27 = no English text lost. The "missing strings" are code or href strings that the edits replaced on purpose (old `own20` fragments, repointed hrefs, old sidebar markup); X25b, X27, X16b and D01 were checked by hand. W00 and Main only gained text.

## 6. Doubts / for a human

1. Nothing was seen in a real browser. Link and route results come from node with a stubbed `location` (the boards' own code) and from rendering with `dcrender.js`; clicks were simulated by calling the entries' own `go` / `pick` handlers. Please click through once: X10 > Accounts, X25 > Platform / Prices, X26b > Platform, X12 > Staff (the `secGo` fix).
2. Parent titles and descriptions are stale: the canvas titles (and W00 / Main labels) of X07, X10, X12, X14, X16, X20, X25, X26 still list the sections that moved out (e.g. X10 "accounts, roles", X25 "plans & prices"). I did not shorten them ("keep every other key untouched"); the new boards' English `<title>` lines can be used.
3. Thumbnails of the 13 new boards are the parent's thumbnail (no new screenshots): the W00 cards of X10b, X25c ... show the parent's first screen.
4. Canvas rows are now wide: row y=15220 has 8 frames (x up to 9,120 + 1,440), row y=10740 has 7. The alternative is extra rows.
5. The Accounts sub-list labels are absent on X25/X26/X27 (hidden group, as before the splits; see section 2).
6. State is still per board (approvals, drafts, read marks do not cross X10/X10b, X25/b/c, X26/b, X12/b ...), as the splits' notes say.
7. Static copies of tab maps: `sub26` (X26 / X26b blocks) and `subTab` (X25 tab of each sub id) are copied into 8 boards. If a block moves again, update all 8 (`tools/sync_a.py` holds the block text; it ran on `before/` and was then patched in place once, so it cannot be re-run on `project/`).
8. Three bare links to `X16-Prototype-Quality.dc.html` (X14 `es_open`, X19 `subj_link`, X21 `toX16`) open Answer cache; the X16 split notes ask the owner whether they should open `X16b` (`#ref`, `#pay`) instead. Not changed.
9. Outside this folder and not touched: `prototype/shared/numbers.md` line 209 (`X25...#plans/adm` -> X25b), `docs/briefs/fix21b_coadmin.txt`, `netlify-build/links.py` and `tabperf.py` (board lists; they only name X10, X20, X26 and stay valid).
10. The old keys kept in X14, X14b, X22 (`nav.admin ...`) are now used once outside the aside; they can go at the next text clean-up.
11. X27's `#from=` table (`FROMN`) has no entry for X12, X07, X20, so those boards cannot use the Co-Admin back link (they have no Co-Admin button anyway).
12. The sidebar click test flags 1 entry (X26b "Rules", explained in section 2); the link check's fragment-token test is lenient.

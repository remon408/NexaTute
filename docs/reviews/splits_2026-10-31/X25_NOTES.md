# X25 split notes (31 Oct 2026)

Source: `X25-Prototype-AdminPlans.dc.html`, 1,775,578 B, 6 languages. Split by top tab. Rebuild: `bash run.sh` (scripts in this folder).

| Board | Tab | Bytes (wc -c) |
|---|---|---|
| X25-Prototype-AdminPlans.dc.html | Matrix (`mx`) | 1,021,285 |
| X25b-Prototype-AdminPlans-Platform.dc.html | Platform switches (`plat`) | 749,938 |
| X25c-Prototype-AdminPlans-Pp.dc.html | Plans & prices (`pp`) | 502,045 |

All three are <= 1,150,000 B. Rough 10-language estimate (ui* text x 4/6): A ~1.53 MB, B ~1.07 MB, C ~0.67 MB (original ~2.63 MB). A is the largest and is under 1.8 MB, but has the least headroom.

## Method (X14 pilot, extended)
1. Stage 1 (`stage1.js`): whole template blocks of the other tabs removed; tab bar made of button (own tab) or link (other boards, same route and order); `own20/go20` extended to X25/X25b/X25c/X26 with `f20()` and `tabHref()`; default tab per board; titles and `$preview` labels; `.seg a` CSS so links look like the buttons. Two in-block links to `#plans/signup` and `#plans/otp17` on B now point at X25b.
2. Dead-code elimination (`dce.js`): scope-aware removal of vals, renderVals0 statements and kit cards nothing in the kept board reads (A 113 units, B 234, C 256).
3. Text pruning (`stage3.js`): literal values captured at runtime, mapped to merged leaves, deleted only if unused; identical across the 6 languages. Removed en leaves: A 903, B 1,257, C 1,743 (of 2,483). Self-check: every kept leaf byte-identical, no removed leaf was used (`bad: []`). Methods removed whole: A uiF20, uiAdd6; B same; C uiAddMF, uiAdd11sn, uiF20, uiAdd6.
Nothing reworded. Helmet, header, language switcher and approvals engine are the same code on all three. Mixed blocks (k17run engine, shared constants) were kept whole.

## Where USD figures live (BDT x 0.015)
Text: `uiAdd15` (p15), `uiAdd16` (f16.sales), `uiAdd17` (k17.u.usd, k17.c.usd/addon/dpass/gw, pp17 and f17 notes), `uiAdd18f` (stadd), `uiEa` (ea.mx.rtadd), `uiAdd11`/`uiAddFix` (tt.mx.rtadd).
Code: `usd`/`usd2` in renderVals0; `usdR`, `p15`, `e15v`, `c15tab` price-change logic; `usdOf`/`usdCell` in `pp17`; constants `PP17` (`.usd` keys), `PRICE`, `LKP`.

## Verification (exact)
- `dcverify.py --langs bn,en,hi,ur,ar,fr`, default run: A holes 1160, checks 23,256; B holes 1759, checks 22,272; C holes 1747, checks 19,518; all 0 problems, 0 parity. (Original untouched: holes 4147, checks 23,232, 0/0.)
- Named states (--state per tab/role/bell/asOpen/phone/tablet/editors): A 21 states, 530,706 checks; B 17 states, 338,256; C 11 states, 178,938; all 0/0.
- Generated states (every handler called once on default and on results): A 120 states, 2,470,134 checks, 0/0; B 120 states, 2,138,096, 0/0; C 117 states, 1,241,064, 0/0. Two C states (`pp17Sel:{"c":"x"}` and its follow-up) are excluded: the dummy value 'x' selects a non-existent course, and the original board reports the same `pp17.kSel []`.
- dcverify checks parity only of `uiText()`; parity of the other methods is by construction (byte copy).
- `dcrender.js` smoke render: A mx, B plat, C pp, in en and ar: all exit 0, empty log, no missing, no 'undefined'/'NaN'/'[object'.
- Render text comparison, original vs new: 88 pairs (3 boards x en/ar/bn/fr x roles p1/p3 x editor states), 0 different.
- Link check (`linkcheck.js`, 3 boards plus all rendered pages): 194 distinct links, 203 occurrences, 0 bad.
- Hash redirect/click simulation: 47 of 47 OK (old moved-tab hashes, #acct/#over to X10, rules/beta/offm/cls to X26, tab-bar links, sidebar sub-entries).
- Sidebar `<aside>` hash identical to original (`b7655db1dced`, 10,962 B) on all three.
- Text partition (`lost.js`): 2,483 leaves in the original; 1,831 used there; 652 unused already in the original (`unused_in_original.txt`); lost used leaves 0, value mismatches 0. Kept: A 1,580, B 1,226, C 740.
- Missing-key Proxy sweep: see SWEEP section below.

## Doubts
- Each board has its own approvals, log and state; edits in one tab do not carry to another board.
- No real browser test: redirects use `location.assign/replace`, only tested with a simulated node `location`.
- X10/X26/X27 still hold the old `own20` (see SIDEBAR_SYNC.md); X27 `#from=` regex knows only the X25 stem.
- Sweep coverage is limited to the start states in `sweep2.js`.
- Some mixed blocks could still be hand-cut further.

## SWEEP (sweep2.js, missing-key Proxy vs the original; depth-2 limit 1)
Every start state x 6 languages: render both, compare vals; handlers called on both and states compared; text Proxy logs any key the original has and the new board lacks.
| Board | start states | nodes | renders | handler calls | errors | missing keys | diffs |
|---|---|---|---|---|---|---|---|
| A (mx) | 309 | 90 | 9,182 | 11,233 | 0 | 0 | 4 |
| B (plat) | 186 | 386 | 23,222 | 37,977 | 0 | 0 | 15 |
| C (pp) | 14 | 42 | 2,017 | 3,360 | 0 | 0 | 19 |
The diffs are the expected pruning, none read by the kept board: (a) TEXT leaves whose key still exists but is undefined (text removed as unused, e.g. `lg.season`, `eid_none`, `cl_ret`, `qa.n_sh`; all in the unused/removed lists; the `eid_none` reader `eidPreview` is in the Platform tab); (b) VALS `k17`/`k18f` where unused kit cards were dropped (e.g. `stg` on A, `pro` on C). The sweep does not tell "unused" from "lost" by itself; `lost.js` does (0 lost used leaves). The earlier depth-3 sweeps were killed by the 600 s limit (exit 144) and are not claimed.

# X14 split (pilot) — method, result, doubts

Date 31 Oct 2026. Nothing in `/home/claude/nexatute` was edited. All work is in this folder.

## Result

| file | bytes (`wc -c`) |
|---|---:|
| original `orig.html` (= prototype/project/X14-Prototype-Ops.dc.html) | 1,360,158 |
| `X14-Prototype-Ops.dc.html` (Models, Spend, Escalation, Cost, Flags, Backup, Approvals, Incidents, Activity log) | 840,695 |
| `X14b-Prototype-Ops-Infra.dc.html` (GPU fleet & load incl. `#gpu/*`, Maintenance & busy page incl. `#maint/*`) | 915,602 |

X14 saves 519,463 B (38%) against the original; X14b is a new file. Both share the helmet CSS, header and logic, so the two together are 1,756,297 B (396 KB more than the original, the cost of duplicating the shared parts). Rough 10-language estimate (text methods `ui*` grow by 4/6, Bengali/Hindi/Urdu/Arabic bytes counted as UTF-8): original about 1.99 MB (over the limit), X14 about 1.23 MB, X14b about 1.32 MB.

Deliverables in this folder:
- `X14-Prototype-Ops.dc.html`, `X14b-Prototype-Ops-Infra.dc.html` — the two result boards.
- `EXTERNAL_LINKS_TO_UPDATE.md` — links in other files to repoint (nothing else was edited).
- `NOTES.md` — this file.
- Pipeline scripts (re-runnable: `bash run.sh`): `stage1.js`, `stage2.js`, `stage25.js`, `stage3.js`, helpers `undef.js`, `usage.js`, `sweep.js`; intermediate outputs `removed_vals_{A,B}.txt` (return-object keys removed), `removed_text_{A,B}.txt` (text leaves removed), `stage3_{A,B}.json` (per-method statistics + verification). `A` = X14, `B` = X14b. `node_modules` is a symlink to `/opt/npm-tools/node_modules` (acorn 8).

## How X14 is built (what I found)

- One state key `sec` (models, spend, esc, cost, gpu, flags, maint, backup, inc, appr, log) selects the visible `<sc-if value="{{ sModels }}">` block. The location hash `#<sec>[/<sub>]` is read once in `st()` (default section) and in `componentDidMount` (scroll to an anchor id `x14-…`).
- The sidebar `<aside>` is generated: the list of sections is `mn.subs` (from `renderVals0().secs` via `menuCfg`/`menuVals`) and drawn as `<button>`s that call `setState({sec})`. The KPI tiles (`kpis`, `go('gpu')` …) and bell notifications (`go: { sec: … }`) switch sections the same way.
- The text is in ~15 methods (`uiText`, `uiFix8`, `uiSw17`, `uiLk16`, …). Each builds one literal per language (`F.bn = {…}` / `L.bn = {…}` / `bn: {…}` inside `var F = {…}`) and merges it into one tree `t` (e.g. `uiSw17` fills `t.k17`, `t.sw17`, `t.x17` and `t.lg`; `uiBeta18` adds `t.k17.c.bdash`; the log lines of several methods go to `t.lg`).
- Sections are NOT independent: one state, one `commit()` (state + activity log + toast), one approvals engine (maint/scale/edge requests are signed in the Approvals section), shared sample data (INC-0142 is a GPU incident, the GPU KPI tile sits in the page header).

## The method, step by step (repeat on X07, X10, X12, X16, X20, X25, X26)

Everything is scripted so that markup and text are copied byte-for-byte and only whole units are removed.

1. **Read first.** Find (a) the section blocks in the template (`<!-- n. Name -->` + `<sc-if value="{{ sXxx }}">`; get the line ranges with `grep -nE "^<!--|^<sc-if|^</sc-if"`), (b) how sections are switched (state key, hash, nav list), (c) the markers `// ---------- … ----------` that cut `renderVals0` into per-section code regions, (d) the text methods and how they merge into `t`.
2. **Stage 1 (`stage1.js`) — structural cut.** Delete by line range (asserted: each range must start at the expected marker): the template blocks of the other board and the matching `renderVals0` code regions (a region is a marker comment up to the next marker). Then, identical in both boards: add the class helpers `secOwn()`, `secOther()`, `secHref(k)`, `secGo(h)`; sections of the other board become links (`href` from `secHref`) in the sidebar list (template: `<sc-if isBtn><button>…</button></sc-if><sc-if isLink><a href>…</a></sc-if>` around the same inner markup), in the KPI tiles, and in the bell (`read` calls `secGo`); set the default section and the hash whitelist (`st()`); in `componentDidMount` an old hash of a moved section redirects to the other board (`hash` is kept); the scroll-anchor map keeps only own anchors; fix links inside moved blocks that pointed at the old board's moved routes; title/preview of the new board.
3. **Stage 2 (`stage2.js A|B`) — prune the returned vals object.** With acorn: a property of the big `return { … }` in `renderVals0` is removed when it references an identifier that no longer exists, or when its name is used only by the removed template blocks (and not by the kept template). Output list: `removed_vals_*.txt`. After this, `undef.js` (free-variable check on every method) reports `{}` for both boards — no identifier is left undefined.
4. **Stage 2.5 (`stage25.js`) — settings-kit cards.** The `k17run(…, [SPEC…])` array holds cards of several sections (here `route` for Models, `thr`/`swset` for Maintenance). Whole array elements of the other board are cut out as text (no JSON re-serialising).
5. **Stage 3 (`stage3.js`) — prune the text, per key.**
   - `usage.js` (acorn, scope-aware) computes which text paths the kept code and template read: aliases like `var K = t.k17`, `var SW = t.sw17`, `T = r.t.mn`, `Object.assign({}, UI.en, UI[l])`, `||` / `?:` flows, member chains; a computed key (`t.lg[e.k]`) keeps the whole subtree; the generic kit `K.c[c.id]` keeps only the card ids that still exist in the code; a read on a leaf (`t.stages.map`) keeps the leaf.
   - Every merged text leaf that nothing reads is "deletable". Each text method has a mount table (e.g. `uiBeta18: c → k17.c, b18 → b18`; `uiSw17: sw17.lg → lg`); a source property is deleted only if ALL merged paths it feeds are deletable (so shared feeds like `lg` are never lost), in all 6 languages at once; whole objects go as one range, a method whose literals are all deleted is removed together with its `this.uiXxx(L)` call.
   - **Self-check inside the script:** the merged text tree is rebuilt from the new file and compared with the old one: every remaining leaf must be byte-identical, every removed leaf must have been "deletable", the removed set must be identical in all 6 languages (`bad: []`). Anything the tool could not map is simply kept.
6. **Verify.** `dcverify.py` with `--langs bn,en,hi,ur,ar,fr` and one `--state` per section/tab (it renders every `{{ hole }}` in every language for each state); `dcrender.js` smoke render per section in en and ar; a link check over all `href`s to X14/X14b; `sweep.js` (renders every own section × 6 languages × 6 roles × tabs, then calls every handler found in the vals, with a Proxy that logs any text key that exists in the ORIGINAL board but is missing in the new one; the original board is run with the same sweep to separate old errors from new ones).
7. **Write the list of external links** (`grep -o "X14-Prototype-Ops\.dc\.html#[^\"']*"` over `prototype/project/*.dc.html` and `canvas.json`).

## What moved

- X14b: template blocks `5. GPU fleet & load` (orig lines 692–1053, 74 KB) and `7. Maintenance & busy page` (1103–1308, 49 KB); code regions 5 GPU fleet (rows), 5c recording pipeline, 5b marking queue, 7 maintenance (`mw*`, `busy*`, `bp*` previews), 5a capacity plan, 5d LiveKit panel + area notice (`wn18v`), `SWINV` + 7b software updates, the Beta dashboard (`b18v`), video delivery (`vd18v`), admissions guard (`f21v`); kit cards `thr`, `swset`.
- X14 keeps everything else. It keeps the GPU KPI tiles (values computed from the shared GPU constants) but as links to X14b.
- Both boards keep: helmet CSS (+ one line `a.kc{text-decoration:none}`), header, language switcher, notification bell, approvals engine (`commit`, `request`, `approve`, `descOf`, OTP), `k17run` kit and the mixed blocks that serve both (see doubts).
- Sidebar `<aside>`: byte-identical in X14 and X14b (SHA-256 12 hex `f6a9d104e002`), 7,080 B. It differs from the old X14 aside only by the sub-list: the section entry is now `<button>` for own sections and `<a href>` for the other board's. The Ops entry stays `class="ng-it on" aria-current="page"` with `href="X14-Prototype-Ops.dc.html"` in BOTH boards (it is the same sidebar entry "Platform operations"; X14b is a second page of that entry), so the "active-page marker" does not differ and the rule "same links, labels, order" holds between X14 and X14b. Within the X13–X22 group the X14 aside differs from the others, as before, by label keys.
- Route names are unchanged. Old hashes: `X14-Prototype-Ops.dc.html#gpu/cap` and `X14b-…#models` both redirect to the board that holds the section (`componentDidMount`).

## Keys removed

Full lists: `removed_vals_A.txt` / `removed_vals_B.txt` (return-object keys, with reason), `removed_text_A.txt` / `removed_text_B.txt` (text leaves, one path per line; same set removed in all 6 languages).
- X14 (A): 52 vals keys (all `g*`, `mw*`, `busy*`, `bp*`, `rpv`, `mkv`, `srvRows`, `sw17`, `lk16`, `cap14`, `f21`, `vd18`, `wn18`, `b18`, `k18`, `sGpu`, `sMaint`), 686 text leaves: whole `cap14` (except `ad.scale`, still read by Approvals), `rp`, `mk` (except their `lg` lines, shared with the activity log), `vd18`, `wn18`, `c21`, `b18`, most of `lk16` and `sw17` (the launch-checklist keys `lk16.lc*` stay for Incidents), 276 keys of `uiText` (`g_*`, `mw_*`, `busy*`, `t_scale`, …), parts of `k17.c`, `f18f`, `f20`, `f8`, `tl`. Methods `uiVd18`, `uiF21`, `uiWn18` removed entirely with their calls.
- X14b (B): 100 vals keys (every other section's vals), 630 text leaves: 172 in `f8` (security tab), `lg` log lines (activity log is not on X14b), incident timeline `tl` (26), `inc_ti`, `svc`, `lf`, models/spend/escalation/cost/flags/backup texts, parts of `f18f`, `f20`, `k17.c`, `sw17`, `lk16` (launch checklist), `rp`/`mk` tooltips.

## Doubts / things I was unsure about (kept rather than cut)

1. **Mixed blocks kept whole in both boards:** `k18` (cards `bdash`, `vid`; `vid.live.bgt` feeds the budget table of Cost), `k18f`/`f18fv` (edge and synthetic checks are GPU, cost guards are Cost, status page is Incidents), `k20`/`f20v` (load test and What's-new are Maintenance, audio-cache is Cost, pen test is Incidents), the k17 engine. So texts such as `f18f`, `f20`, `k17.c.edge` are still in X14 even though their cards are drawn on X14b, and vice versa. Cutting inside these blocks needs a hand edit of ~150 lines each; it would save roughly 60–100 KB per board at 6 languages. I did not do it (rule: when unsure, keep).
2. **State is per board.** Approvals, the activity log, the clock and every setting live in each page's own state. A maintenance window requested on X14b is not in X14's Approvals list or activity log (the prototype never shared state between boards; links lose state too, e.g. the bell item "new incident INC-0142" opens X14 `#inc` with the default incident selected). Sample data (initial approvals/log rows of kind maint/gpu) is identical in both boards.
3. **`#from=X14-Prototype-Ops`** (header link to X27 Co-Admin) is unchanged in X14b because X27 only accepts `X1x/X2x-Name`; see EXTERNAL_LINKS_TO_UPDATE.md.
4. **Sidebar sub-list now has two shapes** (`<button>` for own sections, `<a>` for the other board). This is a markup change inside the `<aside>` of X14 compared with X15–X22 (their sub-lists are not touched). If the group rule must stay byte-exact, the same two-shape list has to be adopted by every board of the group that gets split later.
5. **Redirect on load** (`secGo`) assigns `location.href`; I could only test it in node (no browser), where `location` does not exist and the guard skips it. The links themselves are plain `<a href>`.
6. **Static analysis limits.** `usage.js` follows aliases and member chains; a text object passed whole to a function would be treated as root use (the script prints `bare t passed` warnings; the only one left is the tooltip helper and the `t: t` in the vals). The dynamic sweep is the second safety net, but it only covers the states listed in `sweep.js`.
7. `dcverify.py` only checks parity of `uiText()` (as the audit already noted), not the side text methods; parity of the other methods is guaranteed by construction (the same keys are removed in all 6 languages — checked in `stage3.js`).
8. The 10-language estimate below is a rough linear one; real CJK text is shorter per language than Bengali/Hindi/Urdu, so it is probably high.

## Verifier output (exact, run on the two result files in this folder)

`python3 /home/claude/nexatute/prototype/tools/dcverify.py <file> --langs bn,en,hi,ur,ar,fr` (default state):
- X14: `holes 1288, checks 3624, problems [], nproblems 0, parity [], nparity 0`
- X14b: `holes 2052, checks 17676, problems [], nproblems 0, parity [], nparity 0`

Same tool with one `--state` per section / tab / role (X14: models, spend, esc, cost, flags, backup, inc, appr, log, models ver+hist tabs, flags A/B tab, inc security tab with the launch checklist open, cost "actual" view, esc week, spend cap form open; X14b: gpu, maint, gpu scale start, LiveKit ingress live, maint sw17Sel=os, busy page on):
- X14: `checks 56778, nproblems 0, nparity 0`
- X14b: `checks 106686, nproblems 0, nparity 0`
(6-language check only; the 4 new languages are not in the boards yet, so the 10-language parity of the tool was not run.)

`stage3.js` self-check: `bad: []`, `langsEqual: true` for both boards (A: 687 leaves removed, B: 631 removed; the "kept although deletable" leaves are `lg` log lines fed by shared sources, 24 in A, 1 in B).

`undef.js` (free variables per method): `{}` for both result boards.

`dcrender.js` (smoke render, en and ar, every own section): works; no `missing` output for any of the 22 renders (9 sections × 2 languages for X14, 2 × 2 for X14b). Link check over all rendered pages and both sources: 157 hrefs to X14/X14b, every fragment names a section that exists on the target board, 0 bad.

`sweep.js` (6 languages × all roles × tabs/sub-states per own section, then every handler found in the vals called in en, with a Proxy that logs a text key that exists in the original board but not in the new one):
- X14: 534 renders, 10,535 handler calls, 0 exceptions, 0 missing keys
- X14b: 222 renders, 6,696 handler calls, 0 exceptions, 0 missing keys
(I did not wait for the sweep of the original board; it was only meant to separate old from new errors and there were none.)

Not tested: a real browser (Design canvas / Netlify build). The Design viewer's handling of `href` from one `.dc.html` to another is as in the existing sidebar links; the load-time redirect uses `location.href`.

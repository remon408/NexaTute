# X07 split — NOTES

Nothing inside the repo was edited. Result files (this folder):
- `X07-Prototype-Test.dc.html` (A) — 582,466 B: pick, mcq, omr, result, review, eve, tf, fill, match, short, wr, mixed.
- `X07b-Prototype-Test-ExamAid.dc.html` (B) — 436,865 B: rec, ap, cat, spk, code, cert, emp + the exam-aid text (`exText` part).
- `X07c-Prototype-Test-Hub.dc.html` (C) — 1,005,867 B: merit, battle, papers, allx, axd, eday, hub + `hubText`.
Original: 1,667,860 B. All three <= 1,150,000 B. (C is the largest because `hubText` is ~465 KB; a further cut would be by hub tab, not done: not needed for the limit.)

## Method (X14 pilot method)
stage1 (template cuts + links + redirect), stage2 (AST removal of vals props / locals / methods nothing reads), stage3 (static text-usage prune, hubText/f11Text prune on A and B). Re-run: `bash run.sh`. Whole template units only; markup and text copied byte-for-byte; no wording changed.

## What changed in behaviour
- Pages of another board are plain `<a href>` with the same route (list below). Same helmet CSS, header, language switcher, `<script src="./support.js">`.
- Old hash of a moved page redirects on load (`componentDidMount` -> `scrOtherHash()`), whole hash kept (e.g. `#hub/olvl/bokul`).
- B opens on `rec` (also `#rec|#flag|#cat|#spk|#code|#cert|#minor|#emp`); C opens on `merit` (also `#merit|#battle|#papers|#allx|#eday|#hub[/sec[/who]]`); A also accepts `#mcq|#omr|#short|#mixed`.
- New titles/`$preview` on B and C (see `<title>`).
- Routes: A -> C (`#hub`, `#allx`, `#eday`, `#merit`, `#battle`, `#papers`), A -> B (`#rec`, `#flag`, ...), B -> A, C -> A (`#mcq/#omr/#short/#mixed`).
- "On this page" rail (`dvSub`): items on other boards are links.

## Keys removed (details in removed_*.txt)
- Vals props / locals / methods: `removed_code_A.txt` (VALS 347), `removed_code_B.txt` (393), `removed_code_C.txt` (458) + lists of removed locals and methods.
- Text keys (6 languages, per key): `removed_text_A.txt` (396 lines), `removed_text_B.txt` (526), `removed_text_C.txt` (804); per-method counts in `stage3_?.json`. hubText/f11Text pruned on A and B to the keys the kept template/code read (A keeps `hb.chips`, `hb.name`, `u.entry_s`, `u.pq_*`, `xa.ax_s/ax_t/ed_s/ed_t`).
- Orphan comments removed: `orphan_comments_?.txt`.
- Text already unused in the original: `fb_q` (uiText) — see `unused_in_original.txt`.

## Verification (final files, run after last build; outputs real)
- `dcverify.py <file> --langs bn,en,hi,ur,ar,fr`, default state: A holes 1160 checks 2052; A, B, C: problems [] / nproblems 0 / nparity 0.
- dcverify with one `--state` per page/tab (A 40, B 29, C 34 states from `vstates.py`; outputs `vfinal_A/B/C.out`): all three nproblems 0, nparity 0.
  Dropped from the state list: states with array-valued `fillIn`/`shIn` (dcverify gives `x.val [x]` — same on the ORIGINAL).
- `undef.js` (undefined identifiers): B `{}`, C `{}`, A only `isFinite, URL, Image` (browser globals, same in the original).
- `smoke.sh` (dcrender.js, every page x en, ar): `smoke renders: 52, with output (missing holes / errors): 0`.
- `rcmp.js` (rendered text of original vs new board, 202 states x 6 langs): `renders compared 1212 diffs 0`. (`missing (new boards): A:x.val, A:wTq1,wTq2` = dcverify-level notes, also in the original.)
- `leafcheck.js`: `leaves checked 8982, present in >=1 board 8976, unused in the original 1, LOST 0`.
- `linkcheck.js`: all hrefs between the three boards point to a base + route that exist. Two "BAD" lines for `X07-Prototype-Test.dc.html#allx` in B/C are in the SOURCE only: they are inside a code comment (line ~997 / ~1019), not an href; rendered links are all valid.
- `sweep2.js` (every state x 6 languages, all handlers in en, text methods wrapped in a missing-key Proxy against the original's trees):
  A: states 74, renders 444, calls 11173, errors 0, missing keys 0.
  B: states 71, renders 426, calls 3080, errors 0, missing keys 0.
  C: states 75, renders 450, calls 4184, errors 0, missing keys 0.
  (Handler calls were limited to the first 4 states per screen to keep run time down.)

## Doubts / to check by a human
1. Not seen in a real browser (no browser here): only dcrender/jsdom-style renders and the sweeps. Please click through once, esp. the redirect of old hashes and the exam-aid cards on the test list.
2. `canvas.json`, W00 and Main.dc.html must list X07b and X07c (not done — outside my folder); other boards' links: EXTERNAL_LINKS_TO_UPDATE.md (14 hrefs, 5 files).
3. Static text prune is conservative (kept when unsure); computed keys (`t['pl_'+k]`) are handled by prefix. Leaf check shows 0 lost, so a missing key would only come from a computed key path the sweep did not hit.
4. Sweep handler calls limited to first 4 states per screen.
5. 10-language growth (owner order 30 Oct) is not in this file (still 6 languages); with 10 languages C would be ~1.6 MB: tight against 1.8 MB, so split hubText by hub tab at that time.

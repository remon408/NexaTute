# X12 split — method, result, doubts

Date 31 Oct 2026. Nothing in `/home/claude/nexatute` was edited; all work is in this folder. Same method as the X14 pilot (`../X14/NOTES.md`).

## Result

| file | bytes (`wc -c`) |
|---|---:|
| original `orig.html` (= prototype/project/X12-Prototype-Institute.dc.html) | 1,767,889 |
| `X12-Prototype-Institute.dc.html` (Overview, People, Classes, Study incl. Assess/Paper/Integrity/Proctoring/Review/Certificates/CPP, Notices) | 972,529 |
| `X12b-Prototype-Institute-Ops.dc.html` (Staff, Billing, Special, Org, Mentor, Reports incl. manifest/atlas/class reports, Notifications, Messages) | 1,137,760 |

Both are below the 1,150,000 B target (X12b has 12 KB of room). Rough 10-language growth is about 4/6 of the text part, so X12b will need another cut when the 4 new languages arrive (candidate: Reports manifest and Notifications into a third board).

## How it is built

`bash run.sh`: `s1.js` (structural cut by asserted line ranges: template blocks 323–1054 or 1055–2014, helpers, nav, routing) -> `s2.js A|B` (acorn: prune the returned vals and dead code, scope aware) -> `s3.js A|B` (prune text leaves nothing reads, same keys in all 6 languages, self-check `bad: []`). `undef.js` reports `{}` (no undefined identifier) on both. `states.py A|B` prints one `--state` per section/tab. `routing_test.js` tests hash/redirect logic. `origunused.js` lists leaves already unused in the original.

## Routing

- Sidebar entries of the other board are `<a href>`, own entries `<button>`; same labels and order; the `<aside>` is byte-identical in both boards (3,521 B), header and helmet identical.
- Other board's href: `X12b-…#<sec>?type=..&wn20=1&ntSel=..` (a small whitelisted `?query` carries the school type, the open notification, and tab selections, because state is not shared between pages). `st()` reads it; `hashCarry` validates every value.
- Old hash of a moved section redirects on load (`componentDidMount`, `secGo`): X12 -> X12b for staff, bill, special, org, mentor, reports, msg, notif, atlas, classreports; X12b -> X12 for over, people, classes, study, assess, notice; unknown hash -> default section (X12 Overview, X12b Staff). Only the logic was tested (node, no `location`); a real browser was not available.
- Buttons that switch section (KPI tiles, bell "see all", open item, Welcome flip, Wallet flips, school-type tab) go through `go2()`: same board -> setState, other board -> link.

## Known open bug (not touched)

HANDOVER: "X12 Open approval on an already-open approval does nothing." The button exists in both boards and was left exactly as it was: `ex.open_ap` (Paper maker request, Study/Paper) stays in X12; `ex.open_ap` (Special request), `nt.open_ap` x2 (Notifications) and `sp_open` live in X12b. I did not find out which one the HANDOVER means, so the bug is in whichever of them it was, now in X12 or X12b.

## Verification (run on the final files)

- `dcverify.py <board> --langs bn,en,hi,ur,ar,fr`, default state: X12 `holes 1591, checks 2856, nproblems 0, nparity 0`; X12b `holes 1926, checks 3738, nproblems 0, nparity 0`.
- Same, with 23 `--state` (A) / 31 `--state` (B) covering every section, tab, school type, bell, mobile/tablet nav, wn20: X12 `checks 73266, nproblems 0, nparity 0`; X12b `checks 90858, nproblems 0, nparity 0`.
- `cmp_render.js`: rendered text of the same state and language equals the original: A 138 renders, B 186 renders, 0 diffs, 0 missing holes.
- `dcrender.js` smoke render, every own section in en and ar: 28/28 ok (12 on X12, 16 on X12b).
- `<script src="./support.js"></script>` present once in each board.
- Link check: the only hrefs in the boards are to each other (no fragments other than `#` + section), X20 `#roadmap`, X24 `#legal/...` (copied unchanged).
- Text: `removed_text_A.txt` 1,189 leaves, `removed_text_B.txt` 873 leaves (same set in all 6 languages). 38 of them are removed from BOTH boards because they were already unused in the original (listed by `origunused.js`; the original has 163 unused leaves of 2,556; the rest of those stay because s3 keeps leaves when unsure). All other removed leaves are read only by a section of the other board.
- Sweep (`sweep12r.js`, a reduced version of `sweep12.js`: every own section x school types x tabs x 6 languages rendered; handlers called only in en, school type, first 60 per state; missing-key Proxy compared with the original; the full sweep was too slow, 4 runs did not finish in 40 minutes). Results: X12 `renders 330, calls 900, nerrors 6, nmissing 0`; original run on the same X12 states: identical (`renders 330, calls 900, nerrors 6, nmissing 0`); the 6 errors are one test state (`ppCfg` I invented for the sweep) that also fails in the original, in every language. X12b `renders 786, calls 1920, nerrors 0, nmissing 0`; original on the X12b states: the same. Not run: handler calls in ar and in college/coaching/uni/org types, and mobile/tablet/bell states (excluded for time).

## Doubts

1. State is per board (approvals, read notifications, drafts, clock). A link keeps only the whitelisted carry parameters; the bell item opens the other board with the item selected, but "read" marks made on one board do not appear on the other.
2. Redirect-on-load and `?query` carry-over were tested in node only.
3. Sidebar sub-list has two shapes (button / link), as in X14.
4. X12b is the larger board (1.14 MB); with 10 languages it will pass 1.5 MB.
5. canvas.json / W00 / Main / urls.json / manifest need the new board added (see `EXTERNAL_LINKS_TO_UPDATE.md`).

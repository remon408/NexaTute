# X26 split — method, result, doubts

Date 31 Oct 2026. Nothing in `/home/claude/nexatute` was edited. All work is in this folder. Method = the approved X14 pilot (`../X14/NOTES.md`), adapted (see "What differs from the pilot").

## Result

| file | bytes (`wc -c`) |
|---|---:|
| original `orig.html` (= prototype/project/X26-Prototype-AdminRules.dc.html) | 1,699,549 |
| `X26-Prototype-AdminRules.dc.html` (fix17 rules, fix18g Study Hall quest, fix18b weak network, fix18f image compression, fix18 Free Beta safety) | 966,516 |
| `X26b-Prototype-AdminRules-More.dc.html` (fix18h engagement, fix18i more ways to learn, fix18k strategic items, fix18l trust and access, fix18m smart suggestion, fix20 load test / voice cache) | 950,379 |

Both are under 1,150,000 B. Rough 10-language estimate (text methods `ui*` grow by 4/6, UTF-8 bytes): original about 2.43 MB, X26 about 1.36 MB, X26b about 1.32 MB.

Deliverables: the two boards; `EXTERNAL_LINKS_TO_UPDATE.md`; `SIDEBAR_SYNC.md`; this file; scripts (re-runnable with `bash run.sh`, then `bash verify_all.sh X26-Prototype-AdminRules.dc.html X26b-Prototype-AdminRules-More.dc.html`): `stage1.js` (structure), `stage2.js` (vals), `stage25.js` (kit cards), `stage3.js` + `textmap.js` (text), helpers `undef.js`, `usage.js`, `sweep.js`, `cmp_render.js`, `textloss.js`, `redirect_test.js`, `linkcheck.py`; lists `removed_vals_{A,B}.txt`, `removed_text_{A,B}.txt` (leaf paths removed, same in all 6 languages), `unused_in_original.txt`, `kept_but_deletable_{A,B}.txt`, `stage3_{A,B}.json`. `A` = X26, `B` = X26b. `node_modules` is a symlink to `/opt/npm-tools/node_modules` (acorn 8).

## How X26 is built (what I found)

- X26 is itself a split of X10 (fix20, 29 Oct): the page is only "Plans & modules" (`sec: 'plans'`), with five tabs in `p2Tab` (mx, plat, pp = on X25; rules, beta = X26). Template: one `isPlans` block; inside it `tRules` (lines 485–1353) and `tBeta` (1356–1466). The Rules tab is one long list of blocks marked with `fix*` comments, in this order: fix17 rules (cards cls … shx), fix18g Study Hall quest, fix18b weak network | fix18h, 18i, 18k, 18l, 18m | fix18f | fix20 — so the moved blocks are two runs (808–1292 and 1327–1352), cut as whole units; the fix18f block (imgc, pref) stays between them.
- Settings cards come from one kit (`k17run`) with four calls: `k17` (SPEC17), `k18` (Free Beta + weak network), `k18f` (34 cards: imgc, pref, tq stay; 31 move), `k20` (pk20 + vac20). Every card has its texts in `t.k17.c.<id>`. `k20` and `f20v` (voice-cache purge) are used only by the fix20 block.
- Navigation to a block is a hash only (`#plans/<sub>`; the sidebar and the tab chips switch tabs only). `st()` maps a sub to a tab; `componentDidMount` first forwards a hash that belongs to another board (`go20`: X10 / X25 / X26) and then scrolls to the anchor id (`x10-…`).
- Text: ~28 methods `ui*` (6 languages each) that merge into one tree `t` (`Object.assign(L[c], A[c])`, `x.k17.c = Object.assign(…)`, `x.f18 = f.f18`, …).
- The whole script is 1.23 MB of 1.70 MB; the vals part (`renderVals0`) is already small (the earlier fix20 split removed most of the X10 sections); `added3` holds the plans vals (`isPlans`, `p2Tabs`, `tRules`, `tBeta`, `k17`, `k18`, `k18f`, `k20`, `f20`, …).

## What moved, what changed (both boards share the helmet CSS, header, language switcher, notification bell, approvals engine `AC`, `k17run` kit)

Template (orig line numbers): X26 loses 808–1292 and 1327–1352 and gets one link row where fix20 was (end of the Rules tab); X26b loses 486–807, 1293–1326 and 1354–1466 (so no Free Beta tab body) and gets one link row at the top. Everything else is a byte-for-byte copy (checked with a line diff against the original: the only differences are those two rows, and the title of X26b).
- Link rows: X26 end of Rules tab: 6 links with the existing heading texts (`t.f18f.eg_h`, `mw_h`, `ks_h`, `ls_h`, `ms_h`, `t.f20.vc_h`) + "↗" to `X26b…#plans/engage|more|strategic|trust|more2027|vac`. X26b top: 2 links (`t.f17.rules_h`, `t.f18f.in_h`) to `X26…#plans/rules|imgc`. No new text. They are the only way to get from one page to the other in the UI apart from the tab chip "Free Beta" (see below), because the sidebar is fixed and its sub-entries are tabs.
- `own20(sec, tab, sub)` / `go20`: three arguments now. X26: sub in the 39 moved subs (`engage`, `egsh` … `mwif`, `more2027`, `vac`, `vc`) -> X26b; X26b: sub in the 24 subs that stayed -> X26; `beta` tab -> X26 (also from X26b), `mx/plat/pp` -> X25; `rules` without a sub stays on the current board. Old hash `X26…#plans/engage` and `X26b…#plans/cls` redirect on load (`location.replace`, hash kept). X26b opens on its first block (Engagement) and the sidebar keeps "Rules" active.
- Scroll-anchor map in `componentDidMount`: own anchors only (X26: the K17 cards, beta cards, storage/imgc/pref/tq …; X26b: eg*, ks*, ls*, ms*, `bots`, vc20).
- Code: X26 loses `SPEC20`, `k20`, `f20v` (vals `k20`, `f20` removed by stage 2) and 31 cards of the `k18f` array; X26b loses `SPEC17`, `k17`, `k18` (vals `k17`, `k18`, `tBeta` removed) and the cards imgc, pref, tq. X26b keeps SPEC20 whole (pk20 is read by `f20v.pk`, kept: unsure).
- Title/preview: X26 unchanged; X26b `<title>Prototype: admin panel — rules & settings (part 2: engagement, learning, trust)</title>` and `$preview` label `X26b · Rules & settings — part 2`. `<script src="./support.js"></script>` unchanged in both.
- Sidebar: see `SIDEBAR_SYNC.md` — byte-identical `<aside>` (SHA-256 `b7655db1dced`, 10,962 B) in X10, X25, X26, X26b, X27.

## Text pruning (new tool: token map instead of the pilot's mount table)

The pilot needed a hand-written mount table per text method. X26 has ~28 methods with different merge code, so `textmap.js` finds the source of every merged leaf automatically: it replaces every string literal and function leaf inside a language literal by a unique token, runs `uiText()` on that copy and reads the tokens back from the merged tree (verified: 12,528 leaves, detokenised = real tree, 0 differences; 96 leaves without tokens = numbers). `stage3.js` then deletes a source property only if every merged leaf it feeds is unused (usage analysis `usage.js` on the new file), in all 6 languages at once, and rebuilds the tree to verify: every remaining leaf identical, every removed leaf was "deletable", removed set equal in all languages. Two safety nets were needed and fired: methods whose merge code reads literal keys (`uiQadm`, `uiAdd11`) are left unpruned; two leaves (`legend`, `qa.imp_w_note`) that would have let an older shadowed definition show through are kept. Methods removed whole with their call: `uiAdd16`, `uiAdd6` (all leaves unused). `stage3` self-check `bad: []` for both boards.
- Leaf statistics (en leaves; each has the same 6-language set): original 2,088; read by the original code/template 1,515; unused already in the original 573 (list: `unused_in_original.txt`, 448 removed from both boards, 125 kept: they sit in unpruned/shared structures); X26 keeps 1,227, X26b 1,135; of the 1,515 read leaves 505 are only on X26, 413 only on X26b, 597 on both, 0 on neither; `textloss.js`: 0 lost, 0 changed values; every leaf that a board's own code/template reads is present on that board.
- Removed leaves of X26: 860 (`removed_text_A.txt`), of X26b: 952 (`removed_text_B.txt`).

## Verification (exact outputs, run on the two result files in this folder)

`python3 /home/claude/nexatute/prototype/tools/dcverify.py <file> --langs bn,en,hi,ur,ar,fr` (default state, then one `--state` per tab (rules, beta, mx, plat, pp), per person/role `asP` p1–p6, panels (bell, assistant, one-time code, device m/t, menu rail), other `sec` values, kit cards edited (`k17D`), pending approvals of cards of both boards (`k17S`), voice-cache purge requested/done, passkey recovery; `verify_all.sh`):
- original: default `holes 7551, checks 59424, nproblems 0, nparity 0`; all states `checks 1093944, nproblems 0, nparity 0`
- X26: default `holes 3779, checks 29100, nproblems 0, nparity 0`; all states `checks 547476, nproblems 0, nparity 0`
- X26b: default `holes 4033, checks 32046, nproblems 0, nparity 0`; all states `checks 591636, nproblems 0, nparity 0`
(6-language check only; the 4 new languages are not in the boards yet.)

`undef.js` (free variables per method): `{"mx0":["Component"]}` for the original and for both results (the same known reference to the class name in `mx0`, not an error).

`dcrender.js` smoke render, en and ar: X26 rules / beta / mx, X26b rules / beta / pp, original rules / beta: all rendered, no `missing` output (16 renders). X26 beta tab = 82,171 B in en and 90,228 B in ar = identical size to the original's beta tab.

`cmp_render.js` (visible text, multiset of text nodes + aria/tooltip/placeholder attributes; original rules/beta tab vs X26 + X26b minus the shared chrome; 6 languages × 10 states: both tabs, roles p2/p4/p6, pending approvals of cards on both boards, purge pending/done, bell, assistant): `only in orig 0`; `only in new 288` = exactly the link-row texts (heading + " ↗") — nothing else added, nothing lost.

Redirects (`redirect_test.js`, node with a fake `location`, `componentDidMount` run for every `#plans/<sub>` of the Rules tab, the Beta cards and a sample of the other tabs, on both boards): 188 checks, 0 fails (target board correct, `location.replace`, hash kept; `#plans/calm` is expected on X25 because the matrix row `calm` wins — same as the original). Tab clicks (`go20`, no hash): rules stays, beta -> X26 (from X26b), mx/plat/pp -> X25. Default state on both: `sec plans`, `p2Tab rules`.

Link check (`linkcheck.py`): 42 distinct hrefs/targets in the two boards; every target file exists in prototype/project (or is X26/X26b), every `#plans/<sub>` that points to X26/X26b names the board that holds the block; `bad 0`. Template balance (`bal.js`): `<div>`, `<sc-if>`, `<sc-for>`, `<a>`, `<button>`, `<span>`, `<p>`, … balanced in both cut files.

`sweep.js` (renders every state × 6 languages — 5 tabs × (default + 6 roles), card edits `k17D`, pending approvals `k17S` for roles p1–p3, purge/passkey states, 9 other `sec` values, bell/assistant/one-time code/device/menu panels = 72 states; then, in en, calls every handler function found in the vals for 21 of those states (both tabs, several roles, pending cards, purge pending/done, panels), re-rendering after each call; a Proxy over the text tree logs any key that exists in the ORIGINAL board's text but is missing in the new one):
- X26: 432 renders, 3,861 handler calls, 0 exceptions, 0 missing keys
- X26b: 432 renders, 3,960 handler calls, 0 exceptions, 0 missing keys
(The original board was not swept; it is only the reference for the key list.)

Reproducibility: `bash run.sh` in a fresh folder from `orig.html` gave byte-identical results (same SHA-256 for both boards).

File sizes: `wc -c` X26 966,516, X26b 950,379.

## Doubts / things I was unsure about

1. **Link rows are new markup** (no new text). The sidebar must stay unchanged and its sub-entries are tabs, so without a visible link the second page could only be reached by a hash. If the owner does not want the rows, X26b is still reachable by hash and by `canvas.json`/W00; delete the two `<div class="row">` lines.
2. **State is per board.** The approvals engine and the settings-kit state (`k17S` pending changes, `k17H` history, activity log, toast, clock) live in each page's own state. A change proposed on X26b is not in X26's bell or card history and vice versa (the prototype never shared state between boards; the same doubt as in the X14 pilot). The sample "pending" seed is identical in both.
3. **Free Beta tab chip on X26b** is a plain page link to X26 (`go20` -> `location.assign`), and the three X25 chips too; X26b has no Beta body, so `#plans/beta` in X26b's own state (before the redirect) is an empty tab.
4. **Pre-existing dead code and text** (X10 residue in `renderVals0`: access-control engine, People, Roles … ) is untouched; only text with no reader was pruned. `uiQadm` (31 KB) and `uiAdd11` (33 KB) are not pruned at all (merge code depends on literal keys); a hand edit could save about 30–40 KB per board.
5. `usage.js` is static (aliases and member chains; a computed key keeps its whole subtree). The dynamic nets are `cmp_render.js`, `dcverify.py`, the sweep below; `dcverify.py` checks parity only of `uiText()` — parity of the other methods holds by construction (the same keys removed in all 6 languages; `stage3` checks it).
6. **Redirect on load** uses `location.replace`; tested only with a fake `location` in node, not in a real browser (Design canvas / Netlify build). `netlify-build/xlinks.py` (browser based) should get the new X26b cases listed in EXTERNAL_LINKS_TO_UPDATE.md.
7. `ca27` header link (`#from=X26-Prototype-AdminRules`) is unchanged on X26b (X27 only knows `X1x/X2x-Name`).
8. X26 and X26b links to X14 (`#gpu/beta` on X26, `#maint/lt` on X26b) point at routes the X14 pilot moves to X14b; left as in the original (they redirect). Repoint with the X14 list.
9. The 10-language estimate is rough and probably high (CJK text is shorter than Bengali/Hindi/Urdu).
10. Not tested: a real browser; `dcverify.py` for the 10 languages (the boards still have 6).

# X20 split into four boards (builder notes, revision 2)

Source: prototype/project/X20-Prototype-Landing.dc.html (1.80 MB, 6 languages). Method: the X14 pilot (structural cut, vals tree-shake, text pruning) plus provenance tagging. Nothing in the repo was edited.

## Result
| Board | Keeps | Bytes |
|---|---|---|
| X20-Prototype-Landing.dc.html | hero, paths, how, fit, courses, English, SSC/HSC, crash, hub | 958,281 |
| X20b-Prototype-Landing-Plans.dc.html | plans (finder, add-ons, refund), proof, safety, PlayBoom, MindForge, Hall, Institutions | 990,205 |
| X20c-Prototype-Landing-More.dc.html | Nexa Notes teaser section (#notes), roadmap, FAQ, start, sign-up | 1,091,850 |
| X20d-Prototype-Landing-Blog.dc.html | the Nexa Notes blog: list, posts, videos, newsletter | 1,146,215 |

Header (top menu) and footer are the same template on all four boards (same items, labels, order; checked on rendered pages in en and ar, plain and admin). X20d is the original "blog open" view of the page: the sticky section nav is hidden there and the More button is marked current, exactly as in the original when the blog was open.

## How the blog works across boards
- On X20c the teaser cards, category chips, "see all", the video chip and the Nexa Notes menu item go to X20d and carry the state (language, era, admin preview, country, course, currency, cookie choice, blog list/post/category/video filter) through sessionStorage key `nx20carry`.
- X20d: `#notes` = list, `#notes/<slug>` = a post (the slug table is in the board). Default state is the list; the blog is never "closed". "Back to home" goes to X20c#notes; "see the plan" goes to X20b#plans/#other with the course carried.
- X20 and X20b: the Nexa Notes menu items link to X20d#notes. An old `#notes/<slug>` hash on X20, X20b or X20c redirects to X20d.

## Text pruning rule (lead order, 31 Oct 2026)
1. A text leaf is removed from a board only when nothing in that board reads it. "Read" = the analysis of the kept code and template (alias-aware), not only literal `t.a.b`.
2. Union rule: a leaf that the analysis proves unread on ALL four boards is the only kind that could be lost silently. For those, the key-name rule decides per board: it stays on a board if its key name appears in that board's kept template or code outside `uiText()` (member access, `['key']`, string key, `{{ x.key }}`). With this rule every leaf survives on at least one board unless its key name is used nowhere.
3. The text-merge code inside `uiText()` is part of the definitions: its own member reads do not count. A leaf that merge code reads to build another leaf stays (keep.txt: ver_draft/adm_draft, upd2/upd3, tc_note, tip_more, plans.incl, foot.legal, blog.v.c2pa, inst.form.org keys, plans.other_p.uni).
4. s3.js now exits with an error if the pruned text no longer builds or any leaf changed, so a broken merge can no longer pass quietly.
5. The chat widget reads `faq.items[+chQ]`, only for CHQ = [1, 3, 5]; on boards without the FAQ list only those items are read.

## Leaves removed from all four boards (dead in the original)
9 leaf paths, 54 leaves (6 languages): the key occurs in the original only as its own definition (6 hits = 6 languages), never read.
sy.a_cur, blog.v.own, live.lg.adm.st_new, f16.lg.draft_badge, f16.lg.foot_more, f16.lg.foot_less, f16.lg.foot_n, f16.lg.nav_main, f16.lg.nav_new.
(The legal-page footer lines, the "drafts marked" lines and the "NexaTute video" label are among them: the legal footer moved to X24 earlier, and `t.blog.v.ai` is the only video label the page reads.)
Every other leaf of the original exists on at least one board with the identical value (10,074 leaves compared, 0 different).

## Checks (see the report for exact numbers)
dcverify default and 70 states per board; dcrender en/ar; link and anchor check on rendered pages; header/footer equality; navigation test between boards (secBoard on 19 ids x 4 boards, C -> D with carried state, D load with hash and carry, old hashes); lost-text render comparison (original vs union of the four boards, 3 languages x 72 states); leaf comparison of uiText (original vs union); sweep with the missing-key Proxy, calls to the handlers of 14 states.

## Known leftovers
- Old texts (dates "20 November - 9 December 2026", "Nexa Teacher", wallet wording) are unchanged by order.
- The new boards are not registered in canvas.json, Main or W00 (see EXTERNAL_LINKS_TO_UPDATE.md).
- BL.tTog errors for an unknown post ("Cannot read properties of null (reading 'k')") also occur in the original sweep; unchanged.
- Arrays are text leaves as a whole (e.g. faq.items), so they cannot be pruned item by item.

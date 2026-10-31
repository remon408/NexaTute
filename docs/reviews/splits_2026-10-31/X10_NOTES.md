# X10 split: X10 + X10b (NOTES)

## Result (bytes, `wc -c`; limit 1,150,000 each)
- X10-Prototype-Admin.dc.html: 726,730 (Overview, Guardians, Schedule, Helpline, Institutions, Progress, Usage)
- X10b-Prototype-Admin-Accounts.dc.html: 1,127,833 (Accounts incl. HR/Loan/Invoice tabs, Roles). Close to the target: with 10 languages the text methods (748,771 B at 6 langs) will grow; a further cut may be needed (candidates: uiAdd4 ~299 KB; Plans text kept only for the audit-log renderer FTX.plan_send).
- Original: 1,764,276 (orig.html). Repo untouched.

## Method (`./run.sh` rebuilds both boards byte-for-byte)
stage1.js (template cut, dead Plans compute region cut, sidebar two-shape markup, own20/secHref/go20/hash/bell changes, title/preview, CSS) -> stage15.js (engine stub in X10, SPEC17 card cuts) -> shake.js (unread vals / dead declarations; removed_vals_{A,B}.txt) -> stage3.js (text keys never read, all 6 languages; removed_text_{A,B}.txt; self-check bad: [] on both).
Rules kept: whole units, byte copy of kept code, no rewording, `<script src="./support.js"></script>` unchanged, same helmet/header/language switcher, X10b opens on Accounts, old hashes redirect (X10: #acct*, #roles* -> X10b; X10b: #over, #sched, #usage... -> X10; #plans -> X25/X26).

## Sidebar
X10 and X10b share the identical new `<aside>` (16,264 B, sha256 d81ff87bf266); see SIDEBAR_SYNC.md for X25/X26/X27 (not changed here). External links: EXTERNAL_LINKS_TO_UPDATE.md.

## Verification (exact, all `--langs bn,en,hi,ur,ar,fr`)
dcverify: X10 default 1684 holes/2736 checks, 0 problems, 0 parity; X10b default 1932/3834, 0/0; X10 +16 --state: 69084 checks 0/0; X10b +25 --state: 131886 checks 0/0.
dcrender smoke: 18 renders (X10 7 sections + X10b acct/roles, en+ar), no "missing".
Visible text compare vs original (cmp_render.sh): 78 cases, 0 different.
Link check: 63 hrefs, 0 broken. Redirect test (node, stubbed location): as listed above, pass. Not tested in a real browser.
Text leaves: original 2670 en; X10 1098; X10b 1699; missing from both 456 (same set in 6 langs), of which 412 unused in the original and 44 read only by code dead since fix20 (Plans region). Lists: leaves_missing_unused_in_original.txt, leaves_missing_read_only_by_dead_code.txt. Changed values 0, extra leaves 0.
Proxy sweep: see the end of this file.

## Doubts
- Strict sidebar identity holds X10<->X10b now; X25-X27 need the sync.
- X27 `#from=` regex does not accept X10b.
- State is per board: approvals and audit log do not cross between X10 and X10b.
- Shared engine/text methods stay duplicated in both boards.
- 10-language size not computed. dcverify checks parity only for uiText(). Static analysis limits as in the X14 pilot.

## Proxy sweep (missing-key Proxy vs original)
- X10 (sections over,guard,sched,help,inst,prog,usage): completed. renders 1020, calls 20108, errors 0, missing keys 0.
- X10b (acct,roles): DID NOT COMPLETE. The run was stopped by the 30-minute background limit with empty output (sweepB.out is empty). No sweep result is claimed for X10b. Its coverage comes from the other checks only (78-case rendered-text compare, 25-state dcverify, leaf check, stage3 self-check bad: []). Re-run: `node sweep10.js finB.html orig.html acct,roles` with a longer timeout, or split by tab.

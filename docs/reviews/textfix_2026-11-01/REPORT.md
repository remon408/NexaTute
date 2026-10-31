# Text-fixes pass — REPORT (builder, second continuation: every item applied)

S = /tmp/claude-0/-home-claude/9c0c5ff5-dbc3-5918-808a-b72f22b21703/scratchpad/textfix
Output: S/work/project (72 boards + canvas.json), S/work/prototype/shared, S/diff/*.diff (82 files, regenerated with `diff -u` against the repo), S/report/*, S/build/* (reproducible: `python3 S/build/finish.py` restores S/work_snapshot_earlier and re-applies S/build/mods.txt, then shared_md.py; 998 log rows, 0 "!!" problems; it takes about 2 minutes, run it in the background).
/home/claude/nexatute untouched (read only), nothing committed.

## 1. Checks actually run on the final state (after the last finish.py)
- dcverify, 6 languages (`--langs bn,en,hi,ur,ar,fr`, from the repo root), all 72 boards: **72/72 nproblems=0 nparity=0** (S/report/dcverify_all.txt; table in section 7). ja/de/zh/ko not checked (not in the boards yet).
- Size: largest board X20d 1,146,694 B <= 1,148,000 (S/report/sizes.md; the margin is 1,306 B, X24 1,145,364, X12b 1,138,291).
- Weekday audit (audit_wd.py): 0 mismatches. Invalid-date audit (audit_valid.py, e.g. "29 February 2027"): 0 (was 15). Range audit (audit_rng.py): 12 flags, all the valid calendar-year "1 January – 31 December" lines (D04 k50, X12b su_year), no reversed ranges (was 6 real ones, fixed).
- Protect checks (S/report/protect_checks.txt, same 22 phrases as before): 0 differences.
- Cross-language date audit (audit_lang.py, set based, S/report/audit_lang_final.txt): 16 boards where a date exists only in English (code comments or English-only strings, same signature in all 5 other languages), and 3 boards (X08, X19, X21) with residual signature differences, explained in section 6. No other board differs from English.

## 2. All phases (module -> applied -> counts; S/report/phase_counts.tsv)
| phase (module) | applied | log rows | replacements |
|---|---|---:|---:|
| GPU #2 (ph2_gpu) | yes | 211 | 300 |
| Dates: puzzle, 21-day counts, pen-test, hub clock, GST restore, aligner (ph2_dates) | yes | 141 | 402 |
| USD rule and "to the cent" text (ph2_usd) | yes | 102 | 102 |
| Refund and wallet (ph2_refund) | yes | 26 | 26 |
| Item 1: "day 1 of 21" state wording (ph3_state) | yes | 79 | 79 |
| Item 1: code constants and Christmas (ph3_const) | yes | 18 | 18 |
| Item 2: gift vouchers in minutes (ph3_gift) | yes | 65 | 272 |
| Item 2: Helper free minutes, 30% cap, affiliate 12 months, packs (ph3_disc) | yes | 140 | 170 |
| Item 3: bug bounty M2 (ph3_m2) | yes | 72 | 72 |
| Item 5: comments and X20b prepay code (ph3_cmt) | yes | 29 | 29 |
| Item 6: date groups by hand (ph3_datefix) | yes | 105 | 263 |
| Item 7: money labels and X16b comment (ph3_money) | yes (9 headings, 4 boards; see limits) | 10 | 55 |
| Item 4: shared/*.md (shared_md.py, S/report/shared_md_log.tsv) | yes | 81 | see log |
| Earlier builder phases R, D, W, U, G, M, F (changes.tsv, 986 rows) | yes (earlier) | 986 | see changes.tsv |

The phase letter inside changes2.tsv is approximate (modules share one global label); phase_counts.tsv counts per module function and is the reliable table.

## 3. What was applied in this second continuation (items 1–7 of the coordinator list)
1. "Day 1 of 21" state wording and code constants: done (ph3_state, ph3_const). Free Beta days 25 Dec 2026 – 14 Jan 2027, today = day 1 of 21.
2. Gift vouchers in minutes and Helper free minutes (ph3_gift, ph3_disc.helper/packs); 30% total cap (ph3_disc.disc_cap): X25c default 40 -> 30, no choice above 30, locked "never above 30%" row, derived prices recomputed by code (৳360 -> ৳420, ৳420 -> ৳490, institution invoices in X16/X16b/X17/X19 pipeline values 172,800 -> 201,600, 64,800 -> 75,600, 115,200 -> 134,400, 43,200 -> 50,400); affiliate 12 months (X12b, X16b, X17, 6 languages); extra-minute packs 30/60/120 at ৳1/min (X25c rows pk1–pk3, L04 chips, X20b `mins.d` were already right; the stale Urdu `rate.note` rewritten). Sample invoice amounts (84,000 etc.) and totals are kept by the owner money rule a0c67a8 (S/report/discount_totals.tsv).
3. Bug bounty M2 (ph3_m2): X24 disclosure page (rewards critical $500 / high $200 / medium $50, hall of fame, no cash under 18, triage within 7 days (default)), X15 `bounty`, `sr_s`, `sr_st.fixed`, W00 3 clauses, all 6 languages.
4. shared/*.md (shared_md.py): guarantee.md v3.2 (82 hits in 69 pairs, title, v3.2 change note, lines 37, 99, 128, §10 heading), dated 31 Oct lines in numbers.md and kpi.md (kpi v1.23 stays, "no version bump"), "AI Teacher" -> "AI Tutor" on non-history lines, x20_live.md line 343. History lines (kpi 9 and 11, numbers 1) intentionally kept.
5. Code comments (ph3_cmt): old 0.015 / ".5 rounds down" statements rewritten in X10, X10b, X25*, X26*, X27, X22, X23, X24. **X20b prepay code now computes to the cent**: `usdNum(tb * (period==='m3' ? 3*0.9 : 5))` (old code: `Math.floor(Math.round(tot*100)/100)` = whole dollar, rounded down). Node check: 600/m3 -> $17.93, 1000/m6 -> $55.33. X14b's `0.015` is the R2 storage price per GB and is correct.
6. Date groups (ph3_datefix + aligner); before/after in S/report/date_fixes.tsv (349 date tokens that differ from the earlier snapshot, per line, with context) and S/report/date_fixes_hand.tsv (the 106 hand fixes, before/after strings). Summary in section 4.
7. Money labels: S/report/money_labels.tsv (346 headings scanned on 29 admin boards + 29 board summary rows), S/report/discounts.tsv (172 = every 40%/45% hit of the original boards: 97 kept with reason, 75 changed), S/report/discount_totals.tsv (62 lines, all "sample, not recomputed"). Details in sections 5 and 6.

## 4. Item 6 — date fixes (root causes and lists)
Three engine defects found and fixed (all dates in bn, hi, ur, ar had been affected):
- The date finder refused a month name followed by the danda "।", the Urdu full stop "۔", the Arabic comma "،" / semicolon "؛" or a Bengali case suffix (জানুয়ারির, মার্চে), and did not know the abbreviated bn/hi months (জানু., ফেব্রু., जन., फ़र.). Those dates were never moved in the first pass. S/tools/datemap.py was patched (backup datemap.py.bak31). With the fixed finder the aligner (align_to_en) now runs on every board except X06, X07c, X14b (explicit edits instead) and moves each non-English date to the English one when both sides have the same shape (154 token edits, S/report/align_edits.tsv). The aligner also fixes the Bengali suffix when the month changes (ফেব্রুয়ারির -> মার্চের, never "মার্চর").
- Month-crossing ranges had the month words swapped by the old handler ("29 February – 4 January" = invalid, 15 places in G01, X08, X18; "15 February – 14 January" in X16b; "15 April – 8 March" for the SSC window in D09; comments in X08, X17, X18). All fixed; the SSC window in D09 k46 is EXTERNAL and is back to "1–25 March" (6 languages, original escapes).
- X07c: the hub is EXTERNAL (SPEC 97: no date change) but the earlier snapshot had moved 159 hub JSON leaves by +14 days (events iso/end, bokul `nd`, an English `li` and `voice` text, a comment, a timestamp). Restored from the approved prototype; the "Exam-calendar sample date: Mon 1 Feb 2027" label and Co-Tutor names are kept. English "Fri 5 Mar / Sun 21 Mar" in `voice.bokul` now says "Fri 19 Feb / Sun 7 Mar" again (it matches "in 18 / 34 days" from the hub clock 1 Feb).
Other hand fixes (all in date_fixes_hand.tsv): G01/X08 pre-test week "Sun 21 – Thu 25 Feb" (was Sun 7) and "next check Mon 22 Mar" (bn, hi, ur were 8 March); X18 week labels (bn and hi were still on the November calendar; last week "29 Jan – 4 Feb" in six languages, `tl_m` bn/hi), X18 `time_h`, `wi_r1` (first date 15 Feb in en/ar/fr), X18 bn result day, ur/ar past estimates (25 Jan, 11 Jan); X20c/X20d Crash Pack worked example (opens 13 Feb, first paper 1 March, answer 16 days; the old text had "30 and 14 February: 2 days … = 30" and a first paper on 15 March) and the ur/ar PlayBoom Free Beta period; X14 retest 22 Feb and 14 Mar projection (bn/hi/ur); X16b `p_per` period "15 January – 14 February" (en, hi, ur were reversed, bn had "1–31 January"); ur/ar dates in X04, D01, X12, X12b, X18 (23 Jan -> 6 Feb), X12/X12b (26 Jan -> 9 Feb, paper-setter dates 27 Feb / 6 Mar), D09 (6 Feb -> 20 Feb), G01/X08 (5 Feb -> 19 Feb), X14 (29 Jan -> 12 Feb), G02 ar, X08 wl_sms/rc_prev, X09 bn, L07 bn/hi, X17 ar, X21 bn, X27/X10b bn bill_sal, X06 bn/hi/ur monthly mock test (11 Feb). X06's real calendar (SSC 1–25 March, Eid about 10 March, General Maths 16 March) is unchanged.

## 5. Item 7 — money labels (honest coverage)
- Headings that now end with " · " + the board's existing label (the same six strings as the `samp` key of X15/X27: নমুনা (প্রোটোটাইপ) / Sample (prototype) / नमूना (प्रोटोटाइप) / نمونہ (پروٹوٹائپ) / عيّنة (نموذج أولي) / Exemple (prototype)): X10 `tot_h` (Platform totals), `l_h` (Billing ledger); X10b `cf_h` (Cash flow), `led_h` (Ledger), `pay_h` (Bills to pay), `a_h` (Accounts & finance); X27 `tot_h`; X16b `p_h` (payout batch), `r_h` (Refund requests). No new keys were needed.
- The scan finds en strings with money words by key, it is not a render check. Most other rows are row/column labels inside those pages, navigation or role labels, or settings rows; they are listed with status "not labelled" or "n/a". **Not labelled and still open**: X22 "Revenue (BDT)/(USD)" column headers, X16/X16c tab labels (Refunds, Payouts & tax), X21 Payables/Refunds chat rows, X25*/X26*/X27 money nav labels, D06–D10 money text (D05 already carries "sample (prototype)"), X17/X19 sections that mention revenue. Whether each page shows one label above these rows can only be confirmed by opening the boards.

## 6. Limits, findings and decisions for the main session
- Pen-test window "11–14 Jan 2027" stays as a "(to confirm)" default (the boards call it "sample"; please log it as "(to confirm)" in docs/decisions.md; I cannot write to the repo).
- Crash Pack opening date is mixed by the spec's own date table: G01, X08, X14b, X17, X20c, X20d show 13 Feb (+14 days, M5) while X03, X10, X10b, X16b keep 30 Jan; SPEC line 402 calls it EXTERNAL. Left as the spec table has it; needs an owner decision (one date everywhere).
- Residual English-only date tokens (code comments such as "// fix9 …", X10/X25*/X26/X27 invoice comments, X13/X15 comments) differ from the other five languages by design. X08, X19, X21 still show signature differences caused by English-only comments and by original source strings that already disagreed (X21 "Cloudflare R2, 3 नवंबर" vs English 3 Feb, fixed to 17 Feb in all languages).
- Discount scan: 3 remaining "40%" hits are a code comment and two history notes in X16b/X17 stating the old rule (kept on purpose) plus the X19 sample where a guardian asks for 40% and the reply says only 30% is possible. D06 "18+ learning credits ৳5 each up to ৳200 a month", X26b `cr`, X18 `hr_18` and W00 "learning credits" still give Helper credits a Taka value or credit wording; this conflicts with the "never a Taka value" rule and the new `hfm` default of 10 free minutes. Not changed (outside the list).
- X24 test rules already cover test accounts, no real data and no DDoS. No new X15 admin row exists for the 7-day triage. No affiliate 3-month code constant exists. The L04 chips have no USD view.
- Size margin is thin: X20d 1,146,694 B (limit 1,148,000), X24 1,145,364.
- Cosmetic: the phase label in changes2.tsv is shared between modules (use phase_counts.tsv).

## 7. dcverify per board (6 languages) and size
- D01-Learner-Desktop.dc.html nproblems=0 nparity=0 98571
- D02-Classroom-Desktop.dc.html nproblems=0 nparity=0 46588
- D03-Content-Studio.dc.html nproblems=0 nparity=0 44183
- D04-Institution.dc.html nproblems=0 nparity=0 138303
- D05-Admin-Overview.dc.html nproblems=0 nparity=0 80106
- D06-Admin-Plans.dc.html nproblems=0 nparity=0 70975
- D07-Admin-Safety.dc.html nproblems=0 nparity=0 76403
- D08-Admin-Quality.dc.html nproblems=0 nparity=0 56471
- D09-Admin-Schedule.dc.html nproblems=0 nparity=0 44353
- D10-Admin-Helpline-Sponsor.dc.html nproblems=0 nparity=0 47044
- G01-Guardian-1.dc.html nproblems=0 nparity=0 293894
- G02-Guardian-2.dc.html nproblems=0 nparity=0 42431
- L01-Onboarding-1.dc.html nproblems=0 nparity=0 41038
- L02-Onboarding-2.dc.html nproblems=0 nparity=0 47460
- L03-Home-Plans.dc.html nproblems=0 nparity=0 62658
- L04-Account.dc.html nproblems=0 nparity=0 78138
- L05-AI-Teacher.dc.html nproblems=0 nparity=0 81114
- L06-Batch-Class.dc.html nproblems=0 nparity=0 62042
- L07-Co-teacher.dc.html nproblems=0 nparity=0 73031
- L08-Tests.dc.html nproblems=0 nparity=0 54775
- L09-Progress.dc.html nproblems=0 nparity=0 69174
- L10-StudyHall-Lab.dc.html nproblems=0 nparity=0 40506
- L11-Moderator.dc.html nproblems=0 nparity=0 35495
- L12-More-Learning.dc.html nproblems=0 nparity=0 41535
- L13-Beyond-Syllabus.dc.html nproblems=0 nparity=0 36875
- L14-Safety-Links-Global.dc.html nproblems=0 nparity=0 46167
- L15-Free-Growth.dc.html nproblems=0 nparity=0 41628
- Main.dc.html nproblems=0 nparity=0 71158
- P01-PlayBoom-1.dc.html nproblems=0 nparity=0 26242
- P02-PlayBoom-2.dc.html nproblems=0 nparity=0 18976
- T01-Teacher-Mobile.dc.html nproblems=0 nparity=0 44798
- W00-Website-Preview.dc.html nproblems=0 nparity=0 646604
- X01-Prototype-Flow1.dc.html nproblems=0 nparity=0 548179
- X02-Prototype-Flow2.dc.html nproblems=0 nparity=0 659735
- X03-Prototype-Flow3.dc.html nproblems=0 nparity=0 371836
- X04-Prototype-Flow4.dc.html nproblems=0 nparity=0 454313
- X05-Prototype-Flow5.dc.html nproblems=0 nparity=0 500811
- X06-Prototype-Batch.dc.html nproblems=0 nparity=0 411899
- X07-Prototype-Test.dc.html nproblems=0 nparity=0 582431
- X07b-Prototype-Test-ExamAid.dc.html nproblems=0 nparity=0 436849
- X07c-Prototype-Test-Hub.dc.html nproblems=0 nparity=0 1006123
- X08-Prototype-Guardian.dc.html nproblems=0 nparity=0 1005232
- X09-Prototype-Teacher.dc.html nproblems=0 nparity=0 265865
- X10-Prototype-Admin.dc.html nproblems=0 nparity=0 729252
- X10b-Prototype-Admin-Accounts.dc.html nproblems=0 nparity=0 1131750
- X11-Prototype-Tools.dc.html nproblems=0 nparity=0 351326
- X12-Prototype-Institute.dc.html nproblems=0 nparity=0 972749
- X12b-Prototype-Institute-Ops.dc.html nproblems=0 nparity=0 1138291
- X13-Prototype-LandingAI.dc.html nproblems=0 nparity=0 480416
- X14-Prototype-Ops.dc.html nproblems=0 nparity=0 848015
- X14b-Prototype-Ops-Infra.dc.html nproblems=0 nparity=0 923050
- X15-Prototype-Accounts.dc.html nproblems=0 nparity=0 789476
- X16-Prototype-Quality.dc.html nproblems=0 nparity=0 869478
- X16b-Prototype-Quality-Money.dc.html nproblems=0 nparity=0 819161
- X16c-Prototype-Quality-ExamAid.dc.html nproblems=0 nparity=0 561125
- X17-Prototype-Growth.dc.html nproblems=0 nparity=0 871831
- X18-Prototype-MindForge.dc.html nproblems=0 nparity=0 829349
- X19-Prototype-MarketingHub.dc.html nproblems=0 nparity=0 1105601
- X20-Prototype-Landing.dc.html nproblems=0 nparity=0 958936
- X20b-Prototype-Landing-Plans.dc.html nproblems=0 nparity=0 992064
- X20c-Prototype-Landing-More.dc.html nproblems=0 nparity=0 1092592
- X20d-Prototype-Landing-Blog.dc.html nproblems=0 nparity=0 1146694
- X21-Prototype-Comms.dc.html nproblems=0 nparity=0 824702
- X22-Prototype-AvatarVoice.dc.html nproblems=0 nparity=0 498219
- X23-Prototype-AvatarVoice-User.dc.html nproblems=0 nparity=0 359793
- X24-Prototype-Legal.dc.html nproblems=0 nparity=0 1145364
- X25-Prototype-AdminPlans.dc.html nproblems=0 nparity=0 1029970
- X25b-Prototype-AdminPlans-Platform.dc.html nproblems=0 nparity=0 758993
- X25c-Prototype-AdminPlans-Pp.dc.html nproblems=0 nparity=0 516141
- X26-Prototype-AdminRules.dc.html nproblems=0 nparity=0 974183
- X26b-Prototype-AdminRules-More.dc.html nproblems=0 nparity=0 958445
- X27-Prototype-CoAdmin.dc.html nproblems=0 nparity=0 938819

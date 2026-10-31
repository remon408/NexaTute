# FIXES — review_A + review_B of the text-fixes pass (fixer, 31 Oct / 1 Nov 2026)

All edits are in `build/ph4_review.py` (registered last in `build/mods.txt`: `restores, countdowns, admin_clock, review_b, review_a, systemic, x20b_tiers, x16b_days`). The helpers are in `build/ph4_restore.py`. Shared .md fixes are a block appended to `build/shared_md.py`. Every edit is logged with phase `P4` in `report/changes2.tsv`, also extracted to `report/ph4_changes.tsv` (2,078 rows: about 600 restored real-world date hunks, about 615 date shifts, the rest text and code edits). The final `finish.py` run reported **3011 log rows; 0 problems**. Nothing in the repo was touched.

Two helpers do the date work:
- **`restore`** diffs each repo board against the current text. Where a hunk contains only date tokens and the rule selects it, the original date goes back. Rules select hunks by key, original text and context.
- **`shift`** reuses `tools/datemap.py`. It recomputes weekdays and keeps the ur/ar `M()`/`I()` glue intact. Since the last run, tokens like "X10" and "TD-0007" are no longer read as dates.

Every restored date comes from the original repo board. The "real-world" sources are `prototype/shared/hub.md` §8/§9 and numbers.md F1:
- SSC theory papers Mon 1 – Thu 25 Mar 2027; General Maths Tue 16 Mar.
- Admit cards Sun 14 Feb, changed from Thu 11 Feb by an official notice.
- HSC Head Start Sun 28 Mar 2027 – June. hub.md l.445 and numbers.md l.104 tie it to "after the SSC", so it is **real-world/exam-tied** and was restored.
- SSC Crash Pack opens Sat 30 Jan (30 days before the first paper); season 30 Jan – 28 Feb.
- Model test 4 on Sat 30 Jan, and the national model tests on 12 and 26 Feb, on the hub sample clock Mon 1 Feb.
- Holiday tables, board, Cambridge and admission circulars.

## Review A

| # | board / key | what I did | status |
|---|---|---|---|
| A1 | X08 hub `ALL`, `LV`/`df` stamps, FCW `ex`, crash program, consent, centre, admit card, Crash Pack, Model test 4 | Restored from the repo: the hub code region (`NOW`…`EV = ALL.filter`) plus the hub-quoted guardian copy (`cp_*`, `ms_rows`, `ms_report`, `rc_prev`, `id_given`, `id_when`, `plan_rd_s`, `wl_rows`, the Model-test-4 tip, comments): 151 hunks. `NOW = Date.UTC(2027,1,1)` now matches the label "Exam-calendar sample date: Mon 1 Feb 2027". Non-hub guardian items (guarantee windows, waitlist, PlayBoom renewal) stay at the guardian sample date Mon 15 Feb. "Why: … 29 days to the Maths paper" recomputed for 15 Feb. | fixed |
| A2 | X12 institution calendar | Restored `addEv` SSC/Eid/national days/Ramadan, `HOL`, circulars c15/c16/c20/c21/c24, the pre-test, b26/b28/b29 (26 hunks). Institution-own exams, `TODAY` and assignments stay on M5. | fixed |
| A3 | X20, X20b ar `v39` | PlayBoom paid from 15 Jan 2027, Beta 25 Dec 2026 – 14 Jan. | fixed |
| A4 | X02 `oos_dp_t` | $0.55 in 6 languages; wallet clause → "paid at checkout" (bn/hi/ur/ar/fr). | fixed |
| A5 | L14 template, `k073`, `k076` | $6.64 / $8.85 / $11.07; single subject $5.53; Combo $8.85 (all 6 languages). | fixed |
| A6 | X05 `plan_rows` ur/ar/fr | $6.63 / $63.63. **Also found:** PlayBoom institution discount "35% (100+)" breaks the 30% cap → 30% (6 languages, 2 strings each). | fixed |
| A7 | X07/X07b `empAddonUsd` | 4.42, printed with `toFixed(2)` in X07b (X07 has no print call). | fixed |
| A8 | X24 guarantee terms + guarantee.md | "The minutes stay valid for 6 months. This is not a cash refund…" in en/hi/ur/ar/fr (+ the `li` form). Same in guarantee.md §9 (10 lines) and in the admin `val` label row; v3.2 addendum note. | fixed |
| A9 | X20 ur/ar `×1.35 ÷ 122` | LRI opener added. | fixed |
| A10 | X20c `later[2]` ur/ar | `⁦25⁩ دسمبر ⁦2026⁩ – ⁦14⁩ جنوری ⁦2027⁩` (also ar). | fixed |
| A11 | X23 code clock | `t.fd(15,1,2027)`, `fdt(18…)`, `fdt(16…)`, age cut-off `d > 15` → matches the label "Sample date (prototype): Mon 15 Feb 2027". | fixed |
| A12 | X23 "rounded" | bn/hi/ur/ar "to the cent" + code comment. | fixed |
| A13 | X20c/X20d Crash Pack post | `d 2027-01-30`, `chk 2027-01-28` restored. | fixed |
| A14 | X20c/X20d launch post | `d: '2027-01-14'`. | fixed |
| A15 | X20, X20b, X20c, X20d, Main (+X01) ar | "مدرّس خصوصي بالذكاء الاصطناعي" glossary term: h1, titles, "ابدأ مع …", "مدرّسنا الخصوصي الذكي/بالذكاء الاصطناعي". Human-teacher "مساعد المعلّم الذكي" untouched (protect count 11 = 11). | fixed |
| A16 | shared/x20_live.md headline | bn/hi/ur/ar/fr tutor wording. | fixed |
| A17 | shared/kpi.md `ln_hr_cr` fr | "Minutes gratuites : …" (also the fr `hr_18` cell, with the NBSP kept). | fixed |
| A18 | shared/numbers.md Redis | Valkey on l.147 and in the l.202 load-test result. | fixed |
| A19 | L04 hard-coded "min" | New key `min_u` in 6 languages (মিনিট / min / मिनट / منٹ / دقيقة / min); template uses `{{ t.min_u }}`. | fixed |
| A20 | X24 ur refund `secs[0].p[1]` | "…اور مفت درجہ مفت ہیں — ان پر کوئی خرچ نہیں، اس لیے واپس کرنے کو کچھ نہیں۔" | fixed |
| A21 | X24 ur `secs[11].p[3]` | "منٹ کتنی مدت (6 ماہ) کارآمد رہتے ہیں". The §12 history line of 28 Oct (with "کریڈٹ") is left as written, because history lines stay (R3). | fixed |
| A22 | X08 date picker | min 2026-12-01 / max 2027-12-31 (input + `exOk`); en hint "November" → "December 2026" like the other 5 languages. | fixed |
| A23 | X08 ar claim strings | `صالحةً`, "اطلبوا إعادة ⁦1,260⁩ دقيقة…", single isolates. | fixed |
| A24 | X24 fr | "peuvent être offerts". | fixed |
| A25 | W00 ur/ar bug bounty | `⁦18⁩` in both. | fixed |
| A26 | X03 `gu_amt` | "Minutes back:" (6 languages). | fixed |
| A27 | L04 comment | `<!-- 4.1 Extra minutes & Daily Pass -->`. | fixed |
| A28 | comments X20b/X24/X20c/X20d | $4.43; $9.96 / $13.28 / $16.60, single $4.43 / $7.75; ($1.11); $15.49 / $8.85; Motion Studio "beta from 20 Dec 2026" restored (X20c and X20d). | fixed |
| A29 | shared/kpi.md §7.2 | "co-tutor answer". | fixed |
| A30 | X20c `later[2]` | "Free Beta on the same dates, 25 December 2026 – 14 January 2027" (6 languages). | fixed |
| A-chk1 | X20b `exRows` | With the 30% cap both tiers are equal → one tier "20 or more students", one price column (6 languages; template column and placeholder count). | fixed |
| A-chk2 | W00 / X14 / X14b / X15 pen test "done 11–14 Jan 2027" | → "scheduled 11–14 Jan 2027, before the paid launch". The findings tracker label → "test before the Free Beta" (its findings are dated Dec 2026). | fixed |
| A-chk3 | X20c `later[0]` | "Paid plans — from 15 January 2027; Crash Packs — 30 days before each exam (SSC: from 30 January 2027)" (6 languages). | fixed |
| A-chk4 | numbers.md engagement/strategic "from 1 Jan 2027" | Not changed: they sit below the dated D1 line, which declares the older lines history. | not a defect (history) |
| A-chk5 | X24 fr "marchand officiel" | Not changed; needs native or legal review. Paddle's French documents use "revendeur officiel". | open (native/legal) |
| A-chk6 | kpi.md v1.18 note "(since 31 Oct 2026; were learning credits)" | Kept. The phase-1 snapshot already had it. It records the change instead of rewriting history, and avoids a "credits" claim that is no longer true. | not a defect |
| A-chk7 | A6000 #2 date | No board says "#2 from 1 Jan"; D05 `k21` now says "#2 live since 20 Dec 2026" (decisions.md). | fixed |

## Review B

| # | board / key | what I did | status |
|---|---|---|---|
| B1 | X16 `q3.dt` HSC 2027 | Restored "Thu 24 Jun – Thu 12 Aug 2027 (expected)" (6 languages; the whole circular queue is real-world; 82 hunks with B2). | fixed |
| B2 | X16 `q4.dt` Cambridge | "Entry Fri 19 Feb … exams Mon 26 Apr – Wed 9 Jun" restored; also `old.q2` and the circular deadlines `CI` (BPSC, bank, DU). **Also found:** the BCS answer "4 November 1972" had become "9 December" (engine moved a 1972 date) → restored in 6 languages. | fixed |
| B3 | X13 HSC Head Start banner | "Shows from 28 March, ends 30 June". | fixed |
| B4 | X13 model-test campaign | "until 28 February 2027" (6 languages, `ann`). | fixed |
| B5 | X17 `count_hsh`, `hsh` | "28 March to June". | fixed |
| B6 | X17 `poly27` | "from Sun 28 Mar (after SSC)". | fixed |
| B7 | X17 `count_mt`, `mt`, `h14` | "Ends 28 February" / "Until 28 February". | fixed |
| B8 | X19 bn ad copy | "28 মার্চ". Kept out of the X19 M7 shift with an exam-word exclusion. | fixed |
| B9 | D09 `k43` | "30 Jan – 28 Feb". | fixed |
| B10 | D09 `k48` | "28 March – June". | fixed |
| B11 | X18 `wi_r0/1/2`, D01 `wi_r0`, X07/X07b `wi_x7r` | "16 March" restored; the "last topic mastered" forecasts keep +14. | fixed |
| B12 | X18 term line | **Different from B's fix:** "26 December 2026 – 16 March 2027 · day 42 of 81". B's start date (6 Dec) would contradict `tl_all` "first class Sat 26 Dec 2026". Python: 81 days; Fri 5 Feb = day 42. | fixed (own values) |
| B13 | X18 `oth[].ex` | "Exam 22 March", "Exam 4 March". | fixed |
| B14 | D05 `k33` | "18+: Mistral Large 3 → Claude Opus → a person (Luna 6 only on overload) · Under 18: our own servers → a person" (6 languages). | fixed |
| B15 | D05 `k30` | "Nexa Co-Tutor fallback (18+ only)". | fixed |
| B16 | D05 `k21`, `k27` | A6000 #1 and #2 (8 cards each, LeaderGPU Netherlands; #2 live since 20 Dec 2026) · one GPU cluster · load balancer + Valkey; priority NexaTute → NexaLogicDev → Remon Motion Studio. | fixed |
| B17 | X21 clock + `now_txt` | `BASE 2026-12-25 16:20`. `now_txt(wd,d,tm,y)` takes the year from the clock (no hard-coded 2027) and reads "app servers USA · GPU Netherlands". X21 message, alert and approval stamps in Jan–Apr 2027 moved by M7 (−52 days; exam words excluded). The comment "X10 January run" that the engine had turned into "X24 January" is repaired. The moderation-queue sample (Sun 27 Dec, in the future) → today. | fixed |
| B18 | X19 clock | `NOW0 2026-12-25 16:20`. Inbox, posts, bookings, connectors and CRM stamps ≤ Apr 2027 moved by M7 (−52 days; invoice/money and exam contexts excluded). AI Tutor Live moved −56 days to keep Fridays: last stream Fri 18 Dec, next = today Fri 25 Dec 8:00 pm. | fixed |
| B19 | D05/D07/D09 ur weekday | جمعہ. A global ur/ar rule also fixed X15 ur/ar `M()` forms ("پیر/الاثنين" → "جمعہ/الجمعة"). **Also found:** L05/X02 ur/ar "Wed 14 Jan" → Thu (جمعرات / الخميس). | fixed |
| B20 | AC module `TD` (X10, X10b, X25, X25b, X25c, X26, X26b, X27) | `TD 2026-12-25`; people, approvals and auditor-expiry stamps −52 days. **X17's `TD` is not in an AC module**: it drives the affiliate ledger (money, owner rule a0c67a8), so it is unchanged. **X15's `TD`** → 25 Dec, with request/log/takedown stamps moved (see B24). | fixed (X17 TD: not a defect) |
| B21 | X14/X14b load tests | LT-03 → Mon 21 Dec 2026 (also in the "done … (LT-03)" lines); "now" → Fri 25 Dec 2026. | fixed |
| B22 | X14b `ver_last` | "Last check Wed 25 Nov 2026" (6 languages). | fixed |
| B23 | settings kit (15 boards) | "In 7 days (Fri 1 Jan 2027)"; "From the next billing month (15 Jan 2027)" (6 languages). | fixed |
| B24 | X15 subject requests, `sync` | `sr_rcv/rep/due` −52 days with weekdays recomputed (Mon 30 Nov / Fri 11 Dec / Fri 25 Dec received; due Sat 26 Dec, Mon 28 Dec, Fri 1 Jan). Sync 25 Dec 15:40. | fixed |
| B25 | X10b/X26b security events | `ev`, `ev_ok`, `samp`, passkey "last used" −52 days (sample = Fri 25 Dec 2026). | fixed |
| B26 | X10 `k_beta` ur/ar | "· day 1 of 21" + isolated 2026. | fixed |
| B27 | X10 `k_beta_s` | "signed up · open (day 1 of 21)" (6 languages). | fixed |
| B28 | X17 `out` | "After month 12 — no commission" (6 languages). The code window `c[4] > 12`: all sample conversions are month 1, so the ledger sums are unchanged. | fixed |
| B29 | X18 fr `hr_18`, `ln_hr_cr` | Free minutes wording (NBSP kept). | fixed |
| B30 | X26b `khlp cash` | "Free minutes are not cash … own learning" (6 languages). | fixed |
| B31 | X25/X25b `val` | "Minutes validity" (6 languages). | fixed |
| B32 | D06 `g17c` | $0.55 (fr "0,55 $"). | fixed |
| B33 | D06 fr storage | (0,89 $) / (1,99 $) / (3,32 $). | fixed |
| B34 | D06 `k9` | bn/hi/ur/ar translated "to the cent (owner, 31 Oct 2026)". | fixed |
| B35 | X14b `lead` ur/ar | Emergency cloud GPU (hourly) wording. | fixed |
| B36 | X14/X14b capacity tokens | "GPU groups (2× A6000)" in 6 languages. **Also found:** fr `k_gpu`, `scale`, "serveur IA GPU" leftovers (with a narrow NBSP) → groupes GPU / GPU cloud d'urgence. | fixed |
| B37 | X18 `rv_hist` | "16, 19, 23, 30 January and 3 February" (6 languages, ur/ar `M()` kept). | fixed |
| B38 | X13 ar | Glossary term in `head`, `ssc_s` ×2, FAQ, "مدرّسنا الخصوصي الذكي". | fixed |
| B39 | X17 ar FAQ | "هل المدرّس الخصوصي ذكاء اصطناعي حقًا؟" | fixed |
| B40 | X25 E15 USD | `Number(e15v(k,'usd')).toFixed(2)` in the USD cells ($16.60). | fixed |
| B41 | X16b `se_h` | "(Mon 15 Feb 2027)" = the board's money "as of" date (6 languages). | fixed |
| B42 | D09 `k42` | **Different from B's fix:** "Ended · 31 January" would still be wrong on today Fri 25 Dec. → "Scheduled · 1–31 January". Also `k45` "Running" → "Scheduled" for the Crash Pack (6 languages). | fixed (own wording) |
| B43 | X16/X16b/X16c refund type | "Shikkha Salami voucher" (6 languages). | fixed |
| B44 | X16 ar toast | "قسيمة هدايا: …" | fixed |
| B45 | X25c ar `gv` | "صلاحية قسائم الهدايا". | fixed |
| B46 | X10 ar `eid` | "العيد — قسائم شيكشا سلامي (دقائق مجانية)". | fixed |
| B47 | X27 `eid` | "Eid — Shikkha Salami vouchers (free minutes)" (6 languages). | fixed |
| B48 | X25b `gift` | "(Shikkha Salami, free minutes)" (6 languages; same string in X16b too). | fixed |
| B49 | X16b retailer note | "…of the vouchers they sell" (6 languages). | fixed |
| B50 | X16b fr | "jamais remboursés". | fixed |
| B51 | X14 fr alert | "file du GPU 3–4". | fixed |
| B52 | X14/X14b fr | "Le GPU cloud est prêt…", "le GPU cloud sera prêt". The X21 string is not present, so nothing to change there. | fixed |
| B53 | X22 hi + en comment | "सेंट तक" / "to the cent". | fixed |
| B54 | X25c fr `rate` | "× 1,35 ÷". | fixed |
| B55 | X15 v2.3 note | "(25 Dec 2026 – 14 Jan 2027)". | fixed |
| B56 | X10b/X27 bill schedule | "auto-pay on the 15th" (6 languages; gpu + infra), matching the due date 15 Feb (M5 money period). | fixed |
| B57 | D04 takedown log | "Mon 15 Feb 2027, 11:34 · TD-0007" (6 languages). | fixed |
| B58 | D04 "6 June" | "Sun 6 Jun". The hi/fr forms were already consistent. | fixed |
| B59 | X14 `ch.luna` | "(overload only, 18+)" (6 languages). | fixed |
| B60 | X14b sample notification | "Lesson 03 — 25 Dec 2026" (6 languages). | fixed |
| B61 | ur/ar inserted year | Applied to **all** boards: `⁦2026⁩` in plain strings and in `' دسمبر 2026 – '` concatenations (28+ places, incl. W00, X13, X20*, X24, X26*). | fixed |
| B-chk1 | systemic past/present after 25 Dec | X14/X14b remediation dues, status samples, break-glass, cache sample, maintenance, node test: −52 days. Incidents i124 → Fri 18 Dec, i139 → Tue 22 Dec (pilot). HSC Physics revision → Sat 2 Jan 2027. Pen test → scheduled. X10 "Crash Pack opened … 12 sold" → "opens Sat 30 January (30 days before the first paper)". Money "as of 15 Feb" samples (X14 spend so far, X16b Crash Pack sales, X10b loans, X10b/X16b money TODAY) kept, labelled sample (owner a0c67a8). Post-launch "What's new" update samples (Wed 3 Feb, "(sample)") kept as labelled post-launch samples. | fixed / default |
| B-chk2 | X10b `money()` vs kept income | X10b's `money()` is not rendered (no `led.*` in its template). **Found instead:** the rendered X10 billing card still used `seats >= 100 ? 40 : 30` → 30% flat (cap). The card sits under "Billing ledger · Sample (prototype)"; the totals keep their sample numbers. | fixed |
| B-chk3 | X10 "AI server load / Request a new server" | Not changed this round (wording outside the 10.8 token list). | open |
| B-chk4 | money labels X21/X25*/X26*/D06–D10 | D10 `k39` sponsor-fund total labelled (6 languages). X25*/X26*/D06 show list prices and rule values (product values, not sample money). D07–D09 show no money figures. X21 money figures are inside chat/notification samples under X21's own "Sample (prototype) — Fri 25 Dec 2026" label. | fixed / not a defect |
| B-chk5 | two clocks on X16b | By design: day 1 of 21 + money "as of" Mon 15 Feb, labelled sample (owner rule). | not a defect |
| B-chk6 | ur/ar words inside an LTR isolate | Fixed where seen (X20c `later[2]`, X25c `⁦⁦1⁩:⁦1⁩⁩`). Not swept across all boards. | partly open |

## Further fixes I found (not in either review)
- **Holiday tables** X10/X10b `HOL0` (Shab-e-Qadr, Janmashtami, Saudi Founding Day, Gandhi Jayanti, Pakistan Day, …) had been moved +14 → restored.
- **X14b capacity weeks** tied to the exam season (HSC Head Start week 29 Mar, admission 26 Apr, HSC Crash Pack 31 May) → restored.
- **Countdowns recomputed on the M5 learner boards** (the exam dates are real again):
  - D01 (Thu 4 Feb): 25 / 40 days.
  - L06: 25 days, all 6 languages.
  - X18 (Fri 5 Feb): 24 / 39 days; `EXAM` 53 → 39.
  - X16b Crash Pack note on its money "as of" date Mon 15 Feb: 38 days to the last paper (was 52, which counted from 1 Feb).
- **Restores on G01, X03, X07, D04 and D05:**
  - G01 hub copy (k14, k81, k104, k152–k180).
  - X03 Crash Pack reminder (30 Jan).
  - X07 national model test Fri 12 Feb (= X07c).
  - D04 school pre-test / Class XI admission window.
  - D05 `k36` "On sale since 30 January".
- **Language and encoding fixes:**
  - Bangla genitive after a shifted month.
  - X25c ar `⁦⁦1⁩:⁦1⁩⁩` → `⁦1:1⁩`.
  - X08 en exam-hint month.

## Default choices for the owner (Claude, editable)
1. **Admin operational history after Fri 25 Dec 2026 uses the M7 rule.** New date = d − 52 days (old "now" 15 Feb 2027 → 25 Dec 2026), with weekdays recomputed. Incidents go into the pilot window. Inherently post-launch events are written as scheduled (pen test 11–14 Jan 2027; Crash Pack opens Sat 30 Jan).
2. **Two sample clocks stay where the spec has them.** The hub blocks (X07c, X08 hub, G01 G2c, L08, X16 circular queue, X20* hub teaser) keep "Exam-calendar sample date: Mon 1 Feb 2027". Learner and guardian screens keep their labelled M5 date, and their code now matches the label (X23 15 Feb; D01 4 Feb; X18 5 Feb). The school pre-test therefore reads 7–11 Feb in the hub copy and 21–25 Feb in the guarantee example on the same guardian boards.
3. **Things kept as samples or kept unchanged:**
  - Money "as of" samples stay at 15 Feb with their labels: X16b Crash Pack sales (12 sold), X14 spend so far, X17 affiliate ledger `TD`, X10b loans.
  - The post-launch "What's new" sample (Wed 3 Feb 2027, "(sample)") is kept.
  - The X17 "Head Start — from 1 December" campaign (next year's chapters) follows M1 (5 Jan); it is not exam-tied.
4. **Wordings I chose myself (both differ from the reviewers' suggested fix):**
  - X18 term = 26 Dec 2026 – 16 Mar 2027 · day 42 of 81.
  - D09 January season / Crash Pack = "Scheduled".
5. **Schedules and discounts:**
  - Bills auto-pay "on the 15th" (billing months run from the 15th, like the settings kit).
  - PlayBoom institution 100+ discount capped at 30%.
  - X20b shows one institution tier.
6. **Copy changes:**
  - X02 fr "payé au moment de l'achat".
  - X03 "Minutes back:".
  - X20c `later[0]` new sentence.

## Check results (actual output, `report/ph4_checks.txt`)
```
finish.py: 3011 log rows; 0 problems   (shared_md: guarantee pair hits 82 in 69 pairs; kpi.md ph4 edits 3; shared md ph4 done)
dcverify (verify_all.sh, --langs bn,en,hi,ur,ar,fr): boards with nproblems=0 nparity=0: 72 of 72
boards > 1,148,000 B: 0   largest: X12b 1,138,291 · X24 1,145,461 · X20d 1,146,808
node --check: scripts checked 72 failures 0
audit_wd ../work/project: 0          audit_valid: invalid 0
audit_rng: 12  (all the calendar-year "2027 · 1 January – 31 December" NOYEAR rows in D04 k50 / X12b su_year, as before)
protect phrases vs repo: differences 0  (22 phrases, e.g. Be the Teacher 240/240, مساعد المعلّم الذكي 11/11)
spot checks (one or more per review row, fx/spot.py): FAILS 0 of 104
revA iso.py X08 X12: 34 remaining changed ISO literals (was 183) — all M5 learner/institution product dates (FCW forecasts, maintenance notice, institution exams/TODAY/assignments) and the picker min
revA wdchk.py (all boards): 1 line left: X08 comment "(Mon 22 Mar, Thu 4 Mar)" = false positive; X07c/X12/X16/X17 rows are year-guess false positives (2027 dates without a year), also present in the repo
revB wd.py (30 boards): 0 hard mismatches; 24 "WD?" year-guess rows (X16 q6, X17 15 Aug 2027 — correct for 2027)
stale terms, work counts: credit validity 0 · Credits are not cash 0 · crédits d'apprentissage 0 · learning credits 0 · Redis 0 · Co-Teacher 0 · AI Teacher 0 · Nexa Teacher 0 · RTX Pro 0 · AI-1..5 0 · AI GPU server 0 · معلّم AI 0 · auto-pay on the 1st 0 · $1 (computed) 0 · after month 3 0 · first 3 months 0 · 40% off 0 · Prototype clock 0 · 20 November – 9 December 0 · since 1 January 2027 0 · servers in the USA 0 · 35% (100+) 0
  left on purpose: "wallet" = document/admit-card wallet and "mobile-wallet password" (ur count matches کوالٹی); 0.015 = Cloudflare R2 $0.015/GB; "Mon 1 Feb 2027" only in hub blocks (X07c, X08 hub, G01, L08, X20 hub teaser, D08, X16 queue); ⁦⁦ only in D04/G01 = repo originals
diffs regenerated: diff/ (72 boards + canvas.json + changed shared .md)
```

## Still open
- **The 4 new languages (ja, de, zh, ko) are not added.** The 6-language checks pass; 10-language parity is not attempted.
- **Native-speaker review is needed** for all new bn/hi/ur/ar/fr strings in this pass, X24 fr "marchand officiel" in particular.
- **Remaining review items:**
  - B-chk3: X10 GPU load card wording.
  - B-chk6: a full sweep for ur/ar words inside LTR isolates.
- **Systemic M7 coverage is partial.** It covers the rows the reviewers named plus X14/X14b/X15/X19/X21 and the AC modules. Other admin boards may still hold non-money post-25-Dec past-tense items that nobody flagged.
- **Not changed:** hub.md §7/l.382 still quotes the old USD rule ($21 / $12 …) inside the hub spec text.

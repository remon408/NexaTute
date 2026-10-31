# Review B — text-fixes pass (independent Opus review)

Scope: X10, X10b, X13, X14, X14b, X15, X16, X16b, X16c, X17, X18, X19, X21, X22, X25, X25b, X25c, X26, X26b, X27, D01–D10, canvas.json.
Changed copies: `textfix/work/project/`; originals: `/home/claude/nexatute/prototype/project/`.

How I checked (all run, not assumed):
- String-level diff of every board (line diff → JS-literal token diff → word diff), script in `scratchpad/revB/sd2.py`; date-only and pure-rename hunks were filtered by pattern and the rest read by hand.
- Weekday check (Python `datetime`) of every "weekday + day + month" in en/fr/bn/hi/ur/ar in my boards (`revB/wd.py`).
- USD recomputed with `Decimal` (×1.35÷122, half-up): X25c PP17 (59 values, 0 wrong), X27 PU (18, 0 wrong), X25 E15 (7, 0 wrong); literal "৳… ($…)" scan of all my boards.
- Settings rows read directly in X25c (rate, gl, c2, t1, t2, p3, cap, afm, pk1–3, hfm, gmin, rf, gv, gr).
- `node --check` on every inline script of my 30 boards: 0 failures. canvas.json parses. dcverify (6 langs) on X21: 0/0; builder's 72/72 table present.
- Sidebar: literal-diff across Group A and Group B (a literal removed in one board but kept in another of the same group) — no sidebar label diverged.
- Greps for the old rules (wallet, credit, 0.015, Redis, 40/45/50 %, 3 months, 20 Nov, 9 Dec, 5 Feb, 1 Feb 2027).

## Findings

| board | key / location | language | current text | problem | exact fix | sev |
|---|---|---|---|---|---|---|
| X16 | hub queue `v.q3.dt` | all 6 | "Thu 8 Jul – Thu 26 Aug 2027 (expected)" (HSC 2027 · all 11 boards) | Real-world exam date moved +14 days (EXTERNAL, must never move) | restore original: "Thu 24 Jun – Thu 12 Aug 2027 (expected)" (and the 5 translations from the original file) | H |
| X16 | hub queue `v.q4.dt` | all 6 | "Entry Fri 5 Mar 2027 · late entry Fri 26 Mar 2027 (extra fee) · exams Mon 10 May – Wed 23 Jun" (Cambridge O Level May/June 2027) | Real-world exam-series dates moved +14 | restore: "Entry Fri 19 Feb 2027 · late entry Fri 12 Mar 2027 (extra fee) · exams Mon 26 Apr – Wed 9 Jun" | H |
| X13 | HSC Head Start proposal banner | all 6 | "+ Shows from 11 April, ends 14 July — then removes itself" | HSC Head Start is EXTERNAL (starts 28 March after SSC); the same proposal text in X13 still says "from 28 March" | "+ Shows from 28 March, ends 30 June — then removes itself" (restore originals) | H |
| X13 | model-test campaign note | en (+ check others) | "The February model-test campaign runs until 14 March 2027." | Exam-tied campaign moved into the SSC exam window (1–25 Mar) | "…runs until 28 February 2027." | H |
| X17 | `count_hsh`, HSC Head Start body text | all 6 | "Starts after the SSC exam · 11 April to June"; "After the SSC exam, from 11 April to June: the first HSC chapters…" | EXTERNAL date moved; X10/X19 say 28 March | "· 28 March to June"; "from 28 March to June" | H |
| X17 | `poly27` | all 6 | "Polytechnic admission prep batch from Sun 11 Apr (after SSC)" | exam-tied batch moved | "from Sun 28 Mar (after SSC)" | H |
| X17 | `count_mt`, model-test strings | all 6 | "Ends 14 March"; "SSC and HSC model tests with OMR. Until 14 March."; "February model tests — until 14 March" | "February" model tests now run into the SSC exams | "Ends 28 February"; "Until 28 February."; "— until 28 February" | H |
| X19 | `ads[0].copy` (bn ad text) | bn | "SSC পরীক্ষার পর 11 এপ্রিল থেকে HSC-র প্রথম অধ্যায় …" | EXTERNAL date moved; X19's own HSC Head Start rows say 28 মার্চ | "SSC পরীক্ষার পর 28 মার্চ থেকে HSC-র প্রথম অধ্যায় …" | H |
| D09 | `k43` (SSC Crash Pack window) | all 6 | "13 Feb – 14 Mar" | Crash Pack opens Sat 30 Jan 2027 and closes before the exam; now it runs into the SSC exams | "30 Jan – 28 Feb" (restore originals) | H |
| D09 | `k48` (HSC Head Start) | all 6 | "11 April – June" | EXTERNAL | "28 March – June" | H |
| X18 + D01 | `wi_r0/1/2` (X18), same string in D01 | all 6 | "Readiness on 30 March: 70 (65–75) …" | 16 March = General Maths exam (EXTERNAL); readiness after the SSC has ended is meaningless | "Readiness on 16 March: …" (keep the +14 "last topic mastered" ranges) | H |
| X18 | SSC term line | all 6 | "SSC preparation term · 26 December 2026 – 30 March 2027 · day 62 of 116" | end date is the exam (EXTERNAL); 26 Dec–30 Mar is 95 days, not 116; day 62 from 26 Dec ≠ the board date Fri 5 Feb | "SSC preparation term · 6 December 2026 – 16 March 2027 · day 62 of 101" (6 Dec + 61 days = 5 Feb; 6 Dec–16 Mar = 101 days, Python-checked) | H |
| X18 | `oth[].ex` | all 6 | "Science — Exam 5 April", "English — Exam 18 March" | SSC subject exams moved; 5 April is after the SSC ends | restore "Exam 22 March", "Exam 4 March" | H |
| D05 | `k33` (fallback chain) | all 6 | "Mistral Large 3 → Claude Opus → a person (Luna 6 only on overload)" | Child safety: no under-18 exclusion — spec 10.9 / owner D.207 | "18+: Mistral Large 3 → Claude Opus → a person (Luna 6 only on overload) · Under 18: our own servers → a person" (translate) | H |
| D05 | `k30` | all 6 | "Nexa Co-Tutor fallback" | missing 18+ restriction (spec 10.9) | "Nexa Co-Tutor fallback (18+ only)" | H |
| D05 | `k21`, `k27` | all 6 | "· 8 NexaTute servers · GPU pool shared with…"; "…Remon Motion Studio and NexaLogicDev (NexaTute first)" | GPU fleet / priority not updated (spec 10.8, D.199/D.201) | k21 "A6000 #1 and #2 (8 cards each, LeaderGPU Netherlands) · one GPU cluster with Remon Motion Studio and NexaLogicDev"; k27 "…· priority NexaTute → NexaLogicDev → Remon Motion Studio" | M |
| X21 | `var BASE = mOf('2027-02-15 16:20')` + `now_txt` | code + all 6 | header renders "Dhaka · Mon 15 Feb 2027, 16:20 · servers in the USA"; all X21 message stamps were moved to 21–25 Dec 2026, so relative times are ~52 days off | demo clock must be Fri 25 Dec 2026 16:20; server text not updated | `BASE = mOf('2026-12-25 16:20')`; in `now_txt` replace the hard-coded `2027` with `2026` and " · servers in the USA" with " · app servers USA · GPU Netherlands" (and the 5 translations as in X14) | H |
| X19 | `var NOW0 = TS('2027-02-15 16:20')` | code | comment says Fri 25 Dec 2026, value is 15 Feb 2027; X19 rows mix 20–22 Dec stamps and 15 Feb "pending today" replies | admin demo clock wrong | `NOW0 = TS('2026-12-25 16:20')` and move the 2027-02-15 reply stamps (inbox rows) to 2026-12-25 | H |
| D05 / D07 / D09 | `k10` / `k9` / `k9` (header) | ur | "… پیر، ⁦25⁩ دسمبر ⁦2026⁩ …" | weekday not recomputed: 25 Dec 2026 is Friday (Python) | "جمعہ، ⁦25⁩ دسمبر ⁦2026⁩" | H |
| X10, X10b, X15, X17, X25, X25b, X25c, X26, X26b, X27 | Access-control module `var TD = '2027-02-15'` (people `last: TD`, approvals 11–15 Feb) | code | last sign-in / approvals show 15 Feb 2027 while the same page header says Fri 25 Dec 2026 | demo "today" mismatch (M7 not applied to the AC module) | `TD = '2026-12-25'` and shift the AC log/approval dates 2027-02-11…15 → 2026-12-21…25 | M |
| X14, X14b | load-test history `dt` | all 6 | d1 "Sat 12 Dec 2026", d2 "Sat 19 Dec 2026", d3 "Thu 17 Dec 2026", now "Mon 15 Feb 2027" | d3 ("before the paid launch") now earlier than d2 ("before the Free Beta"); "now" ≠ demo today | d3 → "Mon 21 Dec 2026"; now → "Fri 25 Dec 2026" (weekdays Python-checked) | M |
| X14b | `ver_last` | all 6 | "Last check Mon 18 Jan 2027 · this month’s check is due today" | last check is after "today" (25 Dec) | "Last check Wed 25 Nov 2026 · this month’s check is due today" | M |
| 15 admin boards (X10, X10b, X13, X14, X14b, X15, X16, X16b, X19, X21, X25, X25b, X25c, X26, X26b) | settings kit `d7`, `next` | all 6 | "In 7 days (Mon 22 Feb 2027)"; "From the next billing month (15 Mar 2027)" | relative to today Fri 25 Dec 2026 these are wrong | "In 7 days (Fri 1 Jan 2027)"; "From the next billing month (15 Jan 2027)" | M |
| X15 | `sr_rcv`, `sr_rep`, `sr_due`, `sync` | all 6 / code | "Mon 15 Feb 2027 … Replied today"; sync '2027-02-15 15:40' | "today" = 25 Dec on X15 (its `samp` says so) | received → Thu 24 Dec / Mon 21 Dec / Fri 25 Dec 2026 pattern; sync '2026-12-25 15:40' | M |
| X10b, X26b | security events `ev`, `ev_ok`, `samp` | all 6 | "Mon 18 Jan 2027 …", "Mon 15 Feb 2027 · … YubiKey removed", "Sample (prototype) · Mon 15 Feb 2027" | events after today | ev_ok/samp → "Fri 25 Dec 2026"; 18 Jan event → "Thu 24 Dec 2026" | M |
| X10 | `k_beta` | ur, ar | "Free Beta (25 دسمبر 2026 – 14 جنوری 2027)" without the day count | en/bn/hi/fr have "· day 1 of 21" | append " · ' + M('21') + ' میں سے پہلا دن" / " · اليوم الأول من ' + M('21')" | M |
| X10 | `k_beta_s` | all 6 | "joined · closed" (জন যোগ দিয়েছিল · শেষ …) | Beta is open, day 1 | "signed up · open (day 1 of 21)" + translations | M |
| X17 | affiliate status `out` | all 6 | "After month 3 — no commission" | affiliate period is 12 months (owner 31 Oct) | "After month 12 — no commission" | M |
| X18 | `hr_18`, `ln_hr_cr` | fr | "aussi des crédits d’apprentissage …"; "Crédits d’apprentissage : …" | other 5 languages say free minutes; old credit rule | "18 ans et plus : des minutes gratuites aussi — pas d’argent, non transférables, seulement pour ton apprentissage, dans une limite mensuelle (par défaut, réglée dans l’admin ; aucun crédit stocké)"; "Minutes gratuites : 18 ans et plus avec une formule payante, jusqu’au plafond mensuel (par défaut)" | M |
| X26b | `khlp.o.cash.true` | all 6 | "Credits are not cash, not transferable, only for the learner’s own subscription; …" | Helper rewards are free minutes; rows above already say "free minutes" | "Free minutes are not cash, not transferable, only for the learner’s own learning; no learner-to-learner selling (locked)" + translations | M |
| X25, X25b | guarantee settings `lab.val` | all 6 | "Credit validity" (ক্রেডিটের মেয়াদ, क्रेडिट की वैधता, کریڈٹ کی مدت, صلاحية الرصيد, Validité du crédit) | guarantee gives minutes back, not credit | "Minutes validity" / "মিনিটের মেয়াদ" / "मिनट की वैधता" / "منٹ کی مدت" / "صلاحية الدقائق" / "Validité des minutes" | M |
| D06 | `g17c` Doubt Pass | all 6 | "৳50 … $1 (computed)" | USD rule: ৳50 = $0.55 | "$0.55 (computed)" (fr "0,55 $ (calculé)") | M |
| D06 | storage add-ons | fr | "+20 Go ৳80 (1 $) · +50 Go ৳180 (3 $) · +100 Go ৳300 (4 $)" | other languages already $0.89/$1.99/$3.32 | "(0,89 $) … (1,99 $) … (3,32 $)" | M |
| D06 | `k9` | bn, hi, ur, ar | "… USD = BDT × 1.35 ÷ 122, to the cent (owner, 31 Oct 2026)" | English words left untranslated | bn "সেন্ট পর্যন্ত (মালিক, 31 অক্টোবর 2026)", hi "सेंट तक (मालिक, 31 अक्टूबर 2026)", ur "سینٹ تک (مالک، 31 اکتوبر 2026)", ar "لأقرب سنت (المالك، 31 أكتوبر 2026)" | M |
| X14b | `lead` | ur, ar | "… “1 GPU سرور شامل کریں” …", "«أضف 1 خادم GPU»" | en/bn/hi/fr say "emergency cloud GPU (hourly)"; button text no longer matches | ur "“' + M('1') + ' ہنگامی کلاؤڈ GPU (فی گھنٹہ) شامل کریں”"; ar "«أضف GPU سحابيًا طارئًا (بالساعة)»" | M |
| X14, X14b | capacity `k.fleet`, `alert`, `ad` | all 6 | "AI GPU servers now", "add n AI GPU server", "Capacity plan: add n AI GPU server before …" | spec 10.8 token "AI GPU server(s)" → GPU groups; inconsistent with the fleet card | "GPU groups (2× A6000) now", "add n GPU group(s) (2× A6000)" + translations | M |
| X18 | `rv_hist` | all 6 | "5 reviews — 2, 5, 9, 16 and 3 February" | only the last date moved; list no longer in order | "5 reviews — 16, 19, 23, 30 January and 3 February" (+14 each) | M |
| X13 | `head`, `ssc_s`, FAQ question | ar | "معلّم AI، وتعلّم حقيقي"; "…ومعلّم AI فردي"; "هل المعلّم فعلًا AI؟" | rule Teacher = human, Tutor = AI (other 5 languages changed) | "مدرّس خصوصي AI، وتعلّم حقيقي"; "…ومدرّس خصوصي AI فردي"; "هل المدرّس الخصوصي فعلًا AI؟" | M |
| X17 | `th.signup[2]` | ar | "هل المعلم حقًا ذكاء اصطناعي؟" | not renamed (en: "Is the tutor really an AI?") | "هل المدرّس الخصوصي ذكاء اصطناعي حقًا؟" | M |
| X25 | E15 USD row `it(C.usd, '$' + e15v(...)…)` | code | renders "$16.6" for ৳1,500 | USD must show to the cent ($16.60) | wrap each `e15v(k,'usd')` in `Number(…).toFixed(2)` | M |
| X16b | Crash Pack sales heading | all 6 | "Crash Pack sales — season to date (Mon 1 Feb 2027) · Sample (prototype)" | old demo date left | "(Mon 15 Feb 2027)" (the board's money "as of" date, TODAY constant) | M |
| D09 | `k42` (January season) | all 6 | "Ended · 14 February" | calendar-month season; "January" ending 14 February | "Ended · 31 January" (restore) | M |
| X16, X16b, X16c | refund-type `gift` | all 6 | "Shikkha Salami card" (… কার্ড, … कार्ड, … کارڈ, Carte Shikkha Salami) | gift cards are vouchers (free minutes) | "Shikkha Salami voucher" + translations | L |
| X16 | gift transfer toast | ar | "بطاقة هدايا: عُرض النقل على …" | not converted (others "Gift voucher: …") | "قسيمة هدايا: عُرض النقل على …" | L |
| X25c | `gv` | ar | "صلاحية بطاقة الهدايا" | not converted | "صلاحية قسائم الهدايا" | L |
| X10 | `eid` | ar | "العيد — قسائم هدايا شيكشا سلامي" | missing "(free minutes)" (others have it) | "… (دقائق مجانية)" | L |
| X27 | `eid` | all 6 | "Eid — Shikkha Salami gift vouchers" | spec 10.5: "(free minutes)" | "Eid — Shikkha Salami vouchers (free minutes)" + translations | L |
| X25b | `gift` | all 6 | "Gift vouchers (Shikkha Salami) — sales and redemption" | spec 10.5 wording lacks "free minutes" | "Gift vouchers (Shikkha Salami, free minutes) — sales and redemption" | L |
| X16b | retailer note | all 6 | "Gift-voucher retailers keep about 5% of the cards they sell" | "cards" left | "…of the vouchers they sell" | L |
| X16b | no-cash rule | fr | "Les bons cadeaux ne sont jamais remboursées en espèces" | agreement | "…jamais remboursés en espèces" | L |
| X14 | GPU alert | fr | "Alerte : file d’GPU 3–4 au-dessus de 10 pendant 5 minutes." | elision error | "Alerte : file du GPU 3–4 …" | L |
| X14, X14b, X21 | `scaleok`, `t_scale`, `t_ready` | fr | "GPU cloud est prêt …" | missing article | "Le GPU cloud est prêt …" | L |
| X22 | USD rule line | hi | "USD = BDT × 1.35 ÷ 122, राउंड करके।" | old "rounded" | "…, सेंट तक।" (also en code comment "rounded" → "to the cent") | L |
| X25c | `r.rate` | fr | "Prix USD = prix en taka × 1.35 ÷" | French decimal comma used everywhere else | "× 1,35 ÷" | L |
| X15 | privacy version note | en (+5) | "v2.3 was the Free Beta version (25 Dec 2026 – 15 Jan 2027)" | Beta ends Thu 14 Jan | "(25 Dec 2026 – 14 Jan 2027)" | L |
| X10b, X27 | bills `gpu` schedule | all 6 | "Monthly · auto-pay on the 1st" while the GPU bill is due '2027-02-15' | mismatch after +14 | "Monthly · auto-pay on the 15th" (or due '2027-02-01') | L |
| D04 | takedown log | en (+5) | "When: Mon 1 Feb 2027, 11:34 · TD-0007" | X12/X12b now "Mon 15 Feb 2027, 11:34 · TD-0007" | "Mon 15 Feb 2027" | L |
| D04 | class booking | en, hi, fr | "Sun 6 June – Sun 20 Jun 2027" | mixed month forms | "Sun 6 Jun – Sun 20 Jun 2027" | L |
| X14 | `ch.luna` label | all 6 | "Luna 6 API (overload only)" | outside AI, but unlike Mistral/Claude labels no "(18+ only)" (the tip says 18+) | "Luna 6 API (overload only, 18+)" | L |
| X14b | sample notification | en (+5) | "…Lesson 03 — 1 Feb 2027” is ready" | old demo date | "— 25 Dec 2026" | L |
| X10, X14, X14b, X27, D05 | inserted year in RTL ranges | ur, ar | "⁦25⁩ دسمبر 2026 – …" | new "2026" not isolated like the surrounding digits | wrap as `M('2026')` / ⁦2026⁩ | L |

## To check (not confirmed as defects)
1. Systemic, admin boards with today = Fri 25 Dec 2026: many non-money items mapped by M2/M5 now lie in the future but are written as past/current — e.g. X14 incident "Thu 7 Jan 2027, slow class joining", "Update · Wed 3 Feb 2027", "Sample · last 30 days to Mon 15 Feb 2027", a pen-test finding "open" although the pen test is 11–14 Jan; X10/X16b "The SSC Crash Pack opened on Sat 30 January — 12 sold"; X14 "Spent so far = 15 Feb 2027 up to 16:20"; X10b loans "Pick a date from 15 February 2027 up to today". The owner's money rule covers money screens only; the rest needs one rule (M7 extension or a "sample after launch" label).
2. X10b `money()` now applies a flat 30% to `r.seats × r.base`, so the institution card bill (computed) will differ from the kept sample income (e.g. Model 320 seats: sample ৳1,15,200). Check the rendered card and add a "sample" note if needed.
3. X10 GPU load card still says "AI server load / Request a new server" (outside spec 10.8's token list).
4. Money-section labels still missing per the builder's own TSV: X21 refund/payables approval rows, X25*/X26* money navigation targets, D06–D10 money text. Needs a render check per page.
5. X16b `beta_h`/X14 "today" items use day 1 of 21, while X16b money "as of" = 15 Feb 2027 — two clocks on one board (allowed by owner money rule, but worth one note on the page).
6. ar/ur strings where an Urdu/Arabic word sits inside an LTR isolate, e.g. X16 `ad.gift` → `M(q + ' × ' + v)` with v = "800 منٹ".

## Verdict
**Not ready to merge.** 18 H, 25 M, 19 L confirmed (table rows; most rows cover all 6 languages). The blocking groups are: (a) real-world exam/season dates that moved (X16 hub, X13, X17, X18, D01, D09, X19 — HSC Head Start, Crash Pack window, SSC subject exams, HSC/Cambridge series); (b) D05 still shows the outside-AI fallback with no under-18 exclusion; (c) the demo clock is still 15 Feb 2027 in X21 and X19 (and in the Access-control module of 10 admin boards); (d) wrong Urdu weekday in three D-board headers. Money maths (USD tables, discount rows, 30% cap prices, GPU bill 3,237.84) checked correct; JS parses; no sidebar divergence found.

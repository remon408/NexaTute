# Review A — text-fixes pass (independent Opus review)

Scope: W00, Main, X01–X09 (incl. X07b, X07c), X11, X12, X12b, X20, X20b, X20c, X20d, X23, X24, all L*, G*, P*, T* boards, and shared/*.md.
Method: I diffed every quoted literal and every non-literal segment in each board (Python difflib on the string sequence, after first applying the mechanical rename substitutions to the original). That left 2,499 unique changed hunks, and I read all of them. On top of that:
- An independent weekday checker over the new boards: 0 new mismatches. The only flags are 12 X12 hub lines, which were already there before and are unchanged.
- A date-mapping check of 1,040 date-only hunks against rules M0–M5. The exceptions are listed below.
- All 18 priceTable rows ×5 boards recomputed by code (Decimal, half-up): 0 errors.
- A full read of the X24 refund page in all 6 languages.
- Greps for the stale terms in all 6 languages.

Tools and outputs are in `.../scratchpad/revA/` (ldiffw.py, w/*.ld, dedup.txt, iso.txt, wdchk.py, datebad.txt).

## Confirmed defects

| # | board | key / location | lang | current text | problem | exact fix | sev |
|---|---|---|---|---|---|---|---|
| 1 | X08 | guardian hub `ALL` event array (hub ev1–ev30) + `df('2027-02-15')` LV / `df('2027-02-13')` | code (all langs) | `[8, "2027-03-15", "2027-04-08", "exam"…]`, `[10, "2027-03-30"…]`, `[11, "2027-04-08"…]`, results `2027-05-27`, deadlines `2027-05-28…06-03`, `06-06…06-20`, `06-24…07-14`, `08-30`, bokul `03-05`, `03-26`, `03-21…03-25`, `05-10…06-23`, `08-26`, etc. | The real-world exam calendar was shifted +14 days. The SSC theory papers (1–25 Mar 2027) now show 15 Mar – 8 Apr. This breaks "real-world dates never move". It also contradicts X07c, which still has 2027-03-01…03-25, and hub.md. `NOW` is still `Date.UTC(2027,1,1)`, so the "past" flags and countdowns are wrong as well. | Restore every ISO date in the X08 hub `ALL` array (and the hub `df(...)` stamps) to the original values. Treat the whole X08 hub block as EXTERNAL, the same as X07c. | H |
| 2 | X12 | institution calendar `addEv(...)`, `HOL`, `C.school/college/coaching` circulars, `emItems` (b26/b28/b29) | code (all langs) | `addEv('2027-03-15','exam',f10_ssc)`, `('2027-03-30',…ssc_m)`, `('2027-04-08',…ssc_end)`, `('2027-03-24','gov',f10_eid)`, `('2027-03-07','gov',victory)`, `('2027-04-09','gov',indep)`; `HOL=[[0,'2027-03-11'],[1,'2027-04-11','2027-04-14']]`; c20 `2027-11-21…12-12`, c21 `2028-01-08`, c24 `2028-01-28`; b29 `2027-05-10…06-23` | SSC dates, Eid, national days (21 Feb → 7 Mar, 26 Mar → 9 Apr), holidays, admission-test circulars and the Cambridge series all moved +14 days. c21 now shows Sat 8 Jan 2028 while `ev21_note` still says "Sat 18 Dec → Sat 25 Dec". | Restore the originals: `03-01`, `03-16`, `03-25`, `03-10`, `02-21`, `03-26`, `02-08` (ram); `HOL [[0,'2027-02-25'],[1,'2027-03-28','2027-03-31']]`; c20 `2027-11-07/11-28`, c21 `2027-12-25`, c24 `2028-01-14`; c15/c16 `2027-05-23/06-06`, `06-10/06-30`; b26 `02-19`, b28 `03-07/03-11`, b29 `04-26/06-09`. Only institution-own samples (TODAY, exams, assignments) follow M5. | H |
| 3 | X20, X20b | `v39` (changelog) | ar | `'قسم PlayBoom: مدفوع منذ 4 فبراير 2027 (جرت Free Beta الخاصة به من 15 يناير إلى 3 فبراير)'` | The PlayBoom dates are wrong: the generic +14 rule was applied, not the PB rule. X20c/X20d and the other 5 languages are correct. | `… مدفوع منذ 15 يناير 2027 (جرت ' + I('Free Beta') + ' الخاصة به من 25 ديسمبر 2026 إلى 14 يناير)` (same as X20c) | H |
| 4 | X02 | `oos_dp_t` (Doubt Pass line) | all 6 | en `… ($1 computed for USD users) — paid at checkout …`; bn `… $1, হিসাব করা) — ওয়ালেট থেকে কাটা হয়`; hi `… $1 … — वॉलेट से कटता है`; ur `⁦$1⁩ … — والٹ سے کٹتا ہے`; ar `⁦$1⁩ … — يُدفع من المحفظة`; fr `1 $ calculé … — payé depuis le porte-monnaie` | The USD price is still the old whole dollar in all 6 languages. The wallet wording is still there in 5 languages (no-stored-money rule). | ৳50 → **$0.55** in all 6. Wallet clause → bn `চেকআউটে পরিশোধ`, hi `चेकआउट पर भुगतान`, ur `چیک آؤٹ پر ادائیگی`, ar `يُدفع عند الشراء`, fr `payé au paiement`. Keep the ur/ar `⁦$0.55⁩` isolates. | H |
| 5 | L14 | template `$9` `$12` `$15`; `k073`; `k076` | all 6 | `$9`/`$12`/`$15`; `… single subject $7`; `Continue with Combo · $12` (and the bn/hi/ur/ar/fr equivalents) | The U3 USD change was not applied. Shown prices are wrong. | Template `$6.64` `$8.85` `$11.07`; k073 `$5.53`; k076 `$8.85`, in all 6 languages (ur/ar keep `⁦…⁩`). | H |
| 6 | X05 | `plan_rows` | ur, ar, fr | ur/ar `M('$9')` … `M('$86')`; fr `… à l’étranger $9 / mois` | Only bn/en/hi (and fr annual) were updated. | ur/ar `M('$6.63')`, `M('$63.63')`; fr `$6.63 / mois`. | H |
| 7 | X07b (and X07 data) | `eaRules().empAddonUsd: 6`, rendered by `t.ea_emp_addon(…, M('$' + R.empAddonUsd) …)` | all 6 (rendered) | `$6` for the ৳399 recruitment add-on | The visible USD price is stale. The comment beside it already says $4.42. | `empAddonUsd: 4.42` in X07 and X07b. Print with `Number(R.empAddonUsd).toFixed(2)`. | H |
| 8 | X24 (+ shared/guarantee.md §9) | guarantee-terms page `p` "The credit is valid for 6 months. It is not a cash refund…" and `li` "The credit is valid for 6 months." | en, hi, ur, ar, fr (bn is fixed) | en `The credit is valid for 6 months.`; hi `क्रेडिट 6 महीने तक मान्य है।`; ur `کریڈٹ ⁦6⁩ ماہ تک کارآمد رہتا ہے۔`; ar `يبقى الرصيد صالحًا 6 أشهر.`; fr `Le crédit est valable 6 mois.` | Stale "credit"/"balance" wording on a legal page, and the languages now disagree with bn. | en `The minutes stay valid for 6 months.`; hi `मिनट 6 महीने तक मान्य रहते हैं।`; ur `منٹ 6 ماہ تک کارآمد رہتے ہیں۔`; ar `تبقى الدقائق صالحة 6 أشهر.`; fr `Les minutes restent valables 6 mois.` Make the same change in guarantee.md lines 206/276/466/536/596/666/726/796/856/926. | M |
| 9 | X20 | `cur`/IGCSE price note | ur, ar | `(×1.35 ÷ 122⁩ سے حساب)` / `(محسوبة ×1.35 ÷ 122⁩)` | The LRI `⁦` opener was dropped, leaving an orphan PDI. In RTL the × and ÷ signs reorder. | `(⁦×1.35 ÷ 122⁩ سے حساب)` / `(محسوبة ⁦×1.35 ÷ 122⁩)` | M |
| 10 | X20c | `later[2]` PlayBoom line | ur, ar | `⁦25 دسمبر 2026 – 14⁩ جنوری ⁦2027⁩` / `⁦25 ديسمبر 2026 – 14⁩ يناير ⁦2027⁩` | The month name sits inside an LTR isolate, so the range renders garbled in RTL. | `⁦25⁩ دسمبر ⁦2026⁩ – ⁦14⁩ جنوری ⁦2027⁩` / `⁦25⁩ ديسمبر ⁦2026⁩ – ⁦14⁩ يناير ⁦2027⁩` | M |
| 11 | X23 | `today = t.fd(1, 1, 2027)`, `delBy = t.fdt(4,1,2027…)`, `takeBy = t.fdt(2,1,2027…)`, `ageOf` (`d > 1`) | code | still 1 Feb 2027 | The header now says "Sample date (prototype): Mon 15 Feb 2027" and the comment says the board day is 15 Feb, but the board's own "today", deadlines and age maths still use 1 Feb. | `t.fd(15,1,2027)`, `fdt(18,1,2027,…)`, `fdt(16,1,2027,…)`, `(mo === 2 && d > 15)` (or keep the label at 1 Feb). | M |
| 12 | X23 | USD rule note | bn, hi, ur, ar | `… × 1.35 ÷ 122, রাউন্ড করা।` / `राउंड किया हुआ` / `راؤنڈ کیا ہوا` / `مقرّبًا` | en/fr say "to the cent"; these four still say "rounded". Code comment line 2374 also says "rounded". | bn `সেন্ট পর্যন্ত`, hi `सेंट तक`, ur `سینٹ تک`, ar `لأقرب سنت`; comment → `to the cent`. | M |
| 13 | X20c, X20d | blog post `{k:'crash', slug:'ssc-2027-crash-pack-opens-30-january', d:'2027-02-13', src.chk:'2027-02-11'}` | data | post dated 13 Feb | The Crash Pack opening (Sat 30 Jan 2027) is external, but the post announcing it is now dated two weeks after the opening. | `d:'2027-01-30'`, `chk:'2027-01-28'` (restore). | M |
| 14 | X20c, X20d | blog post `{k:'launch', slug:'paid-plans-and-the-7-day-free-trial', d:'2026-12-24'}` | data | 24 Dec 2026 | The paid-launch post now comes before the Free Beta starts (25 Dec). It was the day before the paid launch. | `d:'2027-01-14'` | M |
| 15 | X20, X20b, X20c, X20d, Main | hero `h1`, page `title()`, X20c `fin.h`, hero `sub` | ar | `معلّم AI، وتعلّم حقيقي`; `— معلّم AI | NexaTute`; `ابدأ مع معلّم AI…`; `معلّمنا الذكي Nexa Tutor`; X20c `معلّمنا بالذكاء الاصطناعي` | The rule "Teacher = human, Tutor = AI" was not applied to the `معلّم AI` form. en says "AI tutor". | `مدرّس خصوصي بالذكاء الاصطناعي، وتعلّم حقيقي`; title `— مدرّس خصوصي بالذكاء الاصطناعي | NexaTute`; `ابدأ مع مدرّس خصوصي بالذكاء الاصطناعي…`; `مدرّسنا الخصوصي الذكي Nexa Tutor` | M |
| 16 | shared/x20_live.md | headline row | bn, hi, ur, ar, fr | `AI শিক্ষক…`, `AI शिक्षक…`, `AI استاد…`, `معلّم AI…`, `Un prof IA…` | Only en became "AI tutor", so the source no longer matches the boards. | bn `AI টিউটর, সত্যিকারের শেখা`; hi `AI ट्यूटर, सच्ची पढ़ाई`; ur `AI ٹیوٹر، حقیقی سیکھنا`; ar as #15; fr `Un tuteur IA, un vrai apprentissage` | M |
| 17 | shared/kpi.md | `ln_hr_cr` | fr | `Crédits d’apprentissage : 18 ans et plus …` | The Helper reward is still "credits" in fr; the other 5 languages are free minutes. | `Minutes gratuites : 18 ans et plus avec une formule payante, jusqu’au plafond mensuel (par défaut)` | M |
| 18 | shared/numbers.md | LiveKit line (l.147) | en | `… + Redis;` | The Valkey rule is not applied in the shared source the boards quote. | `+ Valkey;` | M |
| 19 | L04 | template: big number `45 min`, chips `30 min · ৳30` …, rows `− 12 min`, `+ 60 min` | bn, hi, ur, ar | English "min" hard-coded in the template | Untranslated text in 4 languages (6-language rule). | Render from an i18n key (`t.min_u`: মিনিট / मिनट / منٹ / دقيقة / min), e.g. `45 {{ t.min_u }}`. | M |
| 20 | X24 | refund `secs[0].p[1]` | ur | `… اور مفت درجہ کچھ خرچ نہیں کرتے` | This means "do not spend anything", not "cost nothing". Legal meaning is lost. | `Free Beta، 7 دن کا Free Trial اور مفت درجہ مفت ہیں — ان پر کوئی خرچ نہیں، اس لیے واپس کرنے کو کچھ نہیں۔ …` | M |
| 21 | X24 | refund `secs[11].p[3]` and §12 history | ur | `منٹ کتنے دن (6 ماہ) درست رہتے ہیں` | "درست" means "correct"; the glossary term for validity is "کارآمد". | `منٹ کتنی مدت (6 ماہ) کارآمد رہتے ہیں` | L |
| 22 | X08 | date input min/max + label | code + all 6 | `'2026-12-06'`…`'2028-01-14'` vs label "between December 2026 and December 2027" | The max was shifted to 14 Jan 2028, so it no longer matches the label. 31 Dec 2027 is a plain calendar bound, not a launch date. | max back to `'2027-12-31'` | M |
| 23 | X08 | `gc` claim strings | ar | `تعود الدقائق … إلى الدورة — لا نقدًا — صالحًا ⁦6⁩ أشهر`; `اطلبوا ⁦⁦1,260⁩⁩ دقيقة إلى الدورة`; `⁦⁦1,260⁩⁩ دقيقة أُضيفت…` | Gender agreement is wrong (الدقائق → صالحةً), there are nested double isolates, and the request phrasing is awkward. | `… — لا نقدًا — صالحةً ⁦6⁩ أشهر`; `اطلبوا إعادة ⁦1,260⁩ دقيقة إلى الدورة`; single `⁦1,260⁩` | L |
| 24 | X24 | terms gift `li` | fr | `Les bons cadeaux sont valables 12 mois, peuvent être offertes …` | Gender agreement: bons is masculine. | `… peuvent être offerts …` | L |
| 25 | W00 | bug-bounty clause (new text) | ur, ar | `18 سے کم کو نقد نہیں` / `لمن هم دون 18` | "18" is not isolated, unlike the amounts in the same string. | `⁦18⁩` | L |
| 26 | X03 | `gu_amt` | en (+ peers) | `Credit: the 1:1 minutes used in these 4 weeks — 612 min (sample)` | The leftover word "Credit" contradicts the no-stored-money wording. | `Minutes back: the 1:1 minutes used in these 4 weeks — 612 min (sample)` | L |
| 27 | L04 | HTML comment | — | `<!-- 4.1 Wallet -->` | Spec rule 3 includes comments. | `<!-- 4.1 Extra minutes & Daily Pass -->` | L |
| 28 | X20b, X24, X20c | code comments | — | X20b `// … USD single batch where approved ($6)`; X24 `// … USD $13 / $18 / $22, single $6 / $10`, `৳100 a month per course ($1)`, `// USD $21 / $12`; X20c `// video post (Motion Studio, beta from 17 Dec 2026)` | Old USD rule left in comments, and a Motion Studio date was moved by the NexaTute engine (Motion Studio dates must not move). | `$4.43`; `$9.96 / $13.28 / $16.60, single $4.43 / $7.75`; `($1.11)`; `$15.49 / $8.85`; restore `20 Dec 2026` | L |
| 29 | shared/kpi.md | §7.2 heading | en | `… under every AI tutor / co-teacher answer` | Lower-case co-teacher was not renamed. | `… / co-tutor answer` | L |
| 30 | X20c | `later[2]` | all 6 | `PlayBoom … — its own Free Beta, 25 December 2026 – 14 January 2027` | "its own" is misleading now that PlayBoom has the same dates as NexaTute. | `PlayBoom (Play class–Class III) — Free Beta on the same dates, 25 December 2026 – 14 January 2027` (6 langs) | L |

What I checked and found clean:
- The X24 en refund page equals `x24_refund_en.json`, except the expected rename (Co-Tutor Pass).
- The bn, hi, ar and fr refund pages match the English meaning and the 30 Oct rule: request within 30 days; refund only if approved; AI checks and a person decides; two-person approval above the admin amount; used part at list price; money back to the original method with no balance kept; automatic refunds for our faults; EU/UK 14 days; under-18 refunds to the guardian's method; app-store process. The ur refund page has the same meaning except #20 and #21.
- The 13-section structure is identical in all 6 languages, and every language is at or below its byte budget.
- Bug bounty ($500 / $200 / $50, no cash under 18, 7-day triage).
- The privacy page: app and database servers in the USA, GPU servers with LeaderGPU in the Netherlands, and under-18 requests never sent to an outside AI.
- The 30% institution cap (X12b, X24, X20b); affiliate 12 months (X12b); Helper free minutes; gift vouchers as minutes; extra-minute packs.
- The 21-day puzzle and the "21 days" changes.
- Storage add-on prices ($0.89 / $1.99 / $3.32), PlayBoom $6.63 / $63.63 (bn/en/hi), all priceTable values, and the X20b prepay maths (600 m3 → $17.93).
- No `Nexa Teacher`, `Co-Teacher`, `AI Teacher`, `Redis`, `0.015`, `20 Nov`, `9 Dec` (outside history), or `RTX Pro` left in my boards. The protected texts are unchanged.

## To check (not confirmed as defects)
- **X20b `exRows`**: the third column (`c`) is now 420/560, the same as column b, because 40% became 30%. If that column's header still reads "100+ seats", either remove the column or relabel it.
- **W00 (mirrors X14/X15)**: "External penetration test — done 11–14 Jan 2027". This is written in the past tense, but the demo "today" is 25 Dec 2026. These are reviewer B's boards; the W00 text should follow whatever they decide.
- **X20c**: `later[0]` says "Paid plans and Crash Packs — from 15 January 2027", but the Crash Pack opens on Sat 30 Jan 2027. The older text had the same simplification.
- **shared/numbers.md**: the "Engagement features … from 1 Jan 2027" and "Strategic items … on from 1 Jan 2027" lines. The new top line declares the lines below it history, but the boards now say 15 Jan 2027.
- **X24 fr**: "marchand officiel" for merchant of record. Paddle's French documents use "revendeur officiel" / "marchand attitré". A native or legal reviewer should check this.
- **shared/kpi.md**: the v1.18 change note (history) was edited in place with "(since 31 Oct 2026; were learning credits)". Spec R3 says history lines stay as they are.
- **Not in the pass's scope**: the rules list says A6000 #2 is live on 25 Dec, but SPEC §10.8 still says "#2 from 1 Jan 2027". None of my boards state the A6000 #2 date, so this needs checking in reviewer B's boards (D05, X14b).

## Counts
H 7 · M 14 · L 9 (30 confirmed) · to check 7.

## Verdict
**Not ready to merge.** The H items must be fixed first:
- the X08 and X12 external exam/holiday calendars moved;
- wrong PlayBoom dates in X20/X20b ar;
- stale USD prices in L14, X05, X07b and X02;
- wallet wording left in X02.

M #8 (credit wording in the X24 legal page) and M #9–#10 (bidi) should be fixed in the same round. After the fixes, re-run dcverify (6 languages), the size check, and my `iso.py` / `wdchk.py` scripts on X08 and X12.

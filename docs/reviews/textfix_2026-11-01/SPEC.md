# SPEC — NexaTute prototype pass "TEXT FIXES" (rename · dates · no stored money · refund · USD · GPU/Valkey · discounts/bug bounty)

Planner: Opus, 31 Oct 2026. Builder: Sonnet. Checks: Haiku. Final line-by-line review: Opus.
Scope: only text that newer owner decisions in `docs/decisions.md` already settled. Nothing new is designed here except where a decided rule needs wording (marked "(default, editable)"). Everything not decided is in §12 (needs owner decision) and §14 (questions) — **do not change those places**.

Data files that belong to this spec (same folder, `.../scratchpad/textfix/data/`):

| file | what |
|---|---|
| `dates_actions.tsv` | every string literal (all 6 languages) holding an old launch/Beta date: `action ⇥ board ⇥ key ⇥ reason ⇥ old string`. 1,729 rows: CHANGE 1,206 · CHANGE-SPECIAL 21 · KEEP 502 |
| `counts_rename.tsv` | per-board counts of every rename pattern (before) |
| `usd_tables.txt` | computed replacement values for every hard-coded USD table/literal (Python, half-up to the cent) |
| `x24_refund_en.json` | the new English refund page object for X24 (Opus-written, 6,316 B ≤ old 6,376 B) |
| `w_bn.txt w_hi.txt w_ur.txt w_ar.txt w_fr.txt wallet_keys.tsv` | every wallet/top-up string per language (count ⇥ boards ⇥ string); `w_ar.txt` also catches accounting "رصيد" (= balance in books, trial balance) and `w_fr.txt` "recharge" — those are not stored money, ignore them |
| `gpu_keys.tsv`, `refund_keys.tsv` | GPU/location and refund string inventories (English rows used below) |

---

## 0. Ground rules for the builder

1. **Never edit the repo.** Copy `/home/claude/nexatute/prototype/project/` (72 boards + `canvas.json`) and `/home/claude/nexatute/prototype/shared/` to a work folder `W/` in your scratchpad (`W/before/` untouched copy, `W/project/`, `W/shared/`). Copy `prototype/tools/dcverify.py` to `W/tools/` and run it from there (it writes a temp `.js` next to itself).
2. **Each board is loaded once, all phases run in memory in the order R → D → W → F → U → G → M, then saved once** (§9). Write the pipeline as one script `W/tools/textfix.py` with one function per phase; each phase logs every change as `board ⇥ phase ⇥ key ⇥ old ⇥ new` into `W/report/changes.tsv`.
3. Replace only inside **text**: JS string literals, JSON values, template text nodes, `<title>`, `aria-label`/`title`/`alt`/`data-tip` attribute values, and `//` / `<!-- -->` comments. **Never** change: i18n key names, JS identifiers, file names, hrefs, `id`/`class` values, `canvas.json` file keys, object keys used in code (exception: the X26 option value in D-S4).
4. Digit-tolerant matching for ur/ar: digits and Latin words may be wrapped in U+2066…U+2069 / U+200E / U+200F, or written as concatenation `I('20') + ' نومبر'` / `M('…')`. Every pattern below for ur/ar must allow these wrappers between tokens and keep them in the output.
5. Copy month/weekday spellings **from the boards**, not from a keyboard: Bangla জানুয়ারি / ফেব্রুয়ারি use য + nukta (U+09AF U+09BC), Hindi फ़रवरी uses फ + nukta (U+092B U+093C). Latin digits everywhere (PlayBoom child screens excepted — they are not touched).
6. A pattern count that differs from the expected count in this spec = stop and report; do not "fix" by widening the pattern.
7. Every changed board must pass `dcverify --langs bn,en,hi,ur,ar,fr` with 0 problems / 0 parity, and must stay **≤ 1,150,000 bytes** (§10).

## 1. Boards (72) and where each phase touches

Current largest: X20d 1,146,215 (3,785 B spare) · X24 1,143,125 (6,875 B spare) · X12b 1,137,848 · X10b 1,129,881 · X19 1,105,885 · X20c 1,091,850. All others < 1,030,000.

| phase | boards touched |
|---|---|
| R rename | 63 boards (every board in `counts_rename.tsv`) + `canvas.json` + `shared/*.md` |
| D dates | 26 boards: D05 D08 G01 L02 L15 W00 X01 X02 X08 X09 X12 X12b X13 X14 X14b X15 X18 X20 X20b X20c X20d X24 X25 X26 X26b X27 |
| W stored money | L03 L04 L09 Main W00 X02 X03 X08 X10b X13 X16b X17 X19 X20 X20b X20c X20d X24 X25 X25c + `canvas.json` + `shared/guarantee.md` |
| F refund | X24 (refund page), X16b, X25c, X20b (one tooltip) |
| U USD | D04 D06 G01 L14 X02 X03 X05 X07 X07b X08 X10 X10b X12 X12b X16c X20 X20b X20c X20d X22 X23 X24 X25 X25b X25c X26 X26b X27 |
| G GPU/Valkey | D05 W00 X10b X14 X14b X15 X16 X22 X24 X25 X25b |
| M misc | X25c (guardian discount), X15 X24 W00 (bug bounty) |

---

## 2. Phase R — Nexa Teacher → Nexa Tutor, Co-Teacher → Co-Tutor (D.150, `docs/tasks/rename-nexa-tutor.md`)

Counts now (all boards): "Nexa Teacher" 2,756 · "Nexa Co-Teacher" (not Pass) 648 · bare "Co-Teacher" (not Pass) 475 · "Co-Teacher Pass" 121 · "nexa teacher"/"AI co-teacher" 13 · Bangla/Hindi/Urdu/Arabic-script name forms 8.
How the boards write the name: **every language uses the Latin brand** ("Nexa Teacher-এর", "Nexa Teacher के", "Nexa Teacher کی", "مع Nexa Teacher", "le Co-Teacher"). Only the avatar/voice names in X22/X23 use native script. New names follow the same rule: **Latin "Nexa Tutor" / "Nexa Co-Tutor" in all languages**; native script only where the board already uses it.

### R1 — brand names (apply in this order, case-sensitive, all text incl. comments)
| # | find | replace |
|---|---|---|
| R1.1 | `Nexa Co-Teacher` **not followed by** ` Pass` | `Nexa Co-Tutor` |
| R1.2 | `Nexa Teacher` | `Nexa Tutor` (so `Nexa Teacher’s`→`Nexa Tutor’s`, `Nexa Teacher-এর`→`Nexa Tutor-এর`) |
| R1.3 | `Co-Teacher` not followed by ` Pass` (incl. `⁦Co-Teacher⁩`, `وCo-Teacher`, `lite`, `’s`) | `Co-Tutor` |
| R1.4 | `nexa teacher` (X20c/X20d SEO `kw` strings) | `nexa tutor` |
| R1.5 | `AI co-teacher` (X19, 1) | `AI co-tutor` |
| R1.6 | native-script avatar name a1 (X22 `nm(...)`, X23 `av.a1`): bn `নেক্সা টিচার` → `নেক্সা টিউটর`; hi `नेक्सा टीचर` → `नेक्सा ट्यूटर`; ur `نیکসا ٹیچر` → `نیکسا ٹیوٹر`; ar `معلّم نيكسا` → `⁦Nexa Tutor⁩` (ar keeps the Latin brand like everywhere else on the boards); en/fr `Nexa Teacher — Classic/Classique` handled by R1.2 | |

Gate **R1-PASS (default OFF, owner Q2):** "Co-Teacher Pass" / "Nexa Co-Teacher Pass" (121 in 13 boards: D06 G01 L15 X08 X14 X18 X20 X20b X20c X20d X24 X25c X27) stays unchanged. If the owner says yes, run R1.1/R1.3 without the "not followed by Pass" guard → "Co-Tutor Pass" / "Nexa Co-Tutor Pass".

**Protect (must be byte-identical after R):** file ids and hrefs `L05-AI-Teacher`, `L07-Co-teacher` (W00 keys `'L07-Co-teacher'`, `B('L07-Co-teacher', …)`, blob map), `X09-Prototype-Teacher`, `T01-Teacher-Mobile`, the HTML comment `<!-- 7.1 Co-teacher -->` in L07 (lower-case, leave), identifiers (`rTeacher`, `isTeacher`, `pickTeacher`, `handTeacher`, `roleTeacher`), and every **human** teacher text: `Be the Teacher` (240), `Teacher Reviewer(s)`, `Teacher’s AI assistant`, `Teacher & institution view`, `Teacher app`, `Teacher content studio`, `Teacher marketplace`, `Teacher workshop`, `Teacher voice`, `class teacher`, `institution teacher`, X09/T01/D03 boards' own teacher texts, "it explains like a real teacher" (testimonial).

### R2 — generic "AI teacher" wording (rule "Teacher = human, Tutor = AI", D.150)
| lang | find | replace | count now |
|---|---|---|---|
| en | `AI teachers` / `AI teacher` (word) | `AI tutors` / `AI tutor` | 41 |
| en | `ai teacher` (SEO kw only) | `ai tutor` | 2 |
| en | `Is the teacher really AI?` / `Is the teacher really an AI?` | `Is the tutor really AI?` / `Is the tutor really an AI?` | FAQ X13 X17 X20 X20b X20c X20d |
| bn | `AI শিক্ষক` (keeps suffixes: শিক্ষকের→টিউটরের) | `AI টিউটর` | 43 |
| bn | `শিক্ষক কি সত্যিই AI?` | `টিউটর কি সত্যিই AI?` | FAQ |
| hi | `AI शिक्षक` | `AI ट्यूटर` | 36 |
| hi | `क्या शिक्षक सच में AI है?` | `क्या ट्यूटर सच में AI है?` | FAQ |
| ur | `AI استاد` | `AI ٹیوٹر` | 24 |
| ur | `کیا استاد واقعی AI ہے؟` (also `M('AI')` form) | `کیا ٹیوٹر واقعی AI ہے؟` | FAQ |
| fr | `professeurs IA` / `professeur IA` / `enseignants IA` / `enseignant IA` / `prof IA` | `tuteurs IA` / `tuteur IA` / `tuteurs IA` / `tuteur IA` / `tuteur IA` | 32 |
| fr | `Le professeur est-il vraiment une IA ?` | `Le tuteur est-il vraiment une IA ?` | FAQ |
| ar | first `هل المعلّم ذكاء اصطناعي حقًا؟` → `هل المدرّس الخصوصي ذكاء اصطناعي حقًا؟`; then `معلّم ذكاء اصطناعي` → `مدرّس خصوصي بالذكاء الاصطناعي`; `معلم ذكاء اصطناعي` (kw) → `مدرس خصوصي ذكاء اصطناعي`; `المعلم الذكي` / `المعلّم الذكي` → `المدرّس الخصوصي الذكي` **except when preceded by `مساعد `** (= "Teacher’s AI assistant", human teacher — keep) | | ≈15 |

Exclusions in R2: fr `parents–professeur IA` (monthly parent–teacher summary — human; keep). "AI Teacher Live" (143, D09 W00 X17 X19) is **not** changed (owner Q9). All R2 replacements in bn/hi/ur/ar/fr are marked "native review pending" in the report.

### R3 — non-board files in the same pass
- `canvas.json` labels: "D2 · Nexa Teacher classroom (desktop)", "L5 · Nexa Teacher 1:1 class", "L7 · Nexa Co-Teacher, recordings, error notebook", X2 label → R1 rules. File-name keys untouched.
- `shared/kpi.md, numbers.md, recording.md, x20_live.md, hub.md, guarantee.md, sensory.md, bdsl.md`: R1 + R2 on all lines **except** lines that start with `> **Change note` / `## vNN note` / `Earlier —` history (they record what was true then).

---

## 3. Phase D — dates (D.188, D.186; owner 31 Oct)

New NexaTute dates: **pilot ≈ 1–14 Jan 2027, Free Beta Fri 15 Jan – Thu 4 Feb 2027 (21 days), paid launch Fri 5 Feb 2027.** (15 Jan and 5 Feb are Fridays, like the old 20 Nov / 1 Jan, so "Fri" labels stay; 4 Feb is a Thursday, old end 9 Dec was a Wednesday.) The end date 4 Feb is derived (owner Q3).

### Why not every old date changes
All admin boards and the learner sample timelines run on the **demo clock Mon 1 Feb 2027 16:20** (`numbers.md` D1) with a finished Free Beta (1,764 joined), January paid revenue, payroll, P&L, version histories "in force since 1 Jan 2027", Tanvir enrolled 20 Nov, recordings "today = Sun 6 Dec 2026". With the new dates 1 Feb 2027 falls **inside** the Free Beta, so those samples cannot be fixed by text replacement — it needs a demo-clock decision (owner Q1). This pass changes only **date statements that do not depend on the demo clock** (public site, legal pages, onboarding, teasers, feature-switch rules, launch-milestone labels) and leaves the clock-bound samples exactly as they are (action KEEP in `dates_actions.tsv`, listed in the report).

### D-S1 — which strings
- Use `dates_actions.tsv`. Row action CHANGE / CHANGE-SPECIAL = change; KEEP = must stay byte-identical.
- Boards with **no** date change (all rows KEEP): L05 L09 X07c X10 X10b X16 X16b X16c X17 X19 X21 X22 X25b X25c.
- The TSV holds whole literals. **ur/ar concatenation forms** (`I('20') + ' نومبر – ' + I('9') + ' دسمبر 2026'`) appear as fragments and are not in the TSV: in boards L02 X01 X12b X13 X18 X20 X20b X20c X20d X27 (and X02/X10/X16b/X07c/L05/X11, where they are KEEP), find them with a wrapper-tolerant raw-source regex, determine the owning key (nearest preceding `key:` on the same line), and apply the action of the **English row with the same board + key**. Log each as `concat`.

### D-S2 — replacement rules (inside CHANGE strings only)
**D1 Free Beta range** — inside a span that matches "20 ‹Nov› … 9 ‹Dec› [2026]" (any separator: ` – `, `-`, `to`, `থেকে`, `से`, `سے`, `إلى`/`من`, `au`/`du`), map tokens:

| token | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| start day | 20 → 15 | 20 → 15 | 20 → 15 | 20 → 15 | 20 → 15 | 20 → 15 |
| Nov | November→January · Nov→Jan | নভেম্বর→জানুয়ারি | नवंबर→जनवरी | نومبر→جنوری | نوفمبر→يناير | novembre→janvier · nov.→janv. |
| end day | 9 → 4 | 9 → 4 | 9 → 4 | 9 → 4 | 9 → 4 | 9 → 4 |
| Dec | December→February · Dec→Feb | ডিসেম্বর→ফেব্রুয়ারি | दिसंबर→फ़रवरी | دسمبر→فروری | ديسمبر→فبراير | décembre→février · déc.→févr. |
| year after end | 2026 → 2027 | same | same | same | same | same |
| end weekday | Wed→Thu · Wednesday→Thursday | বুধ→বৃহস্পতি | बुध→गुरु | بدھ→جمعرات | الأربعاء→الخميس | mer.→jeu. |

Start weekday (Fri / শুক্র / शुक्र / جمعہ / الجمعة / ven.) stays.

**D2 Free Beta start only** (CHANGE rows only): "20 November 2026"/"20 Nov 2026" and each language's form → "15 January 2027"/"15 Jan 2027" (same token table); e.g. X20b `s` "We open on 20 November 2026", X20 "On 20 November you can start your first lesson", X27 `beta_tot`/`wa_beta` "Fri 20 Nov 2026" → "Fri 15 Jan 2027", X14/X14b `n2`/`beta` "(starts Fri 20 Nov 2026)" → "(starts Fri 15 Jan 2027)".

**D3 day count** (CHANGE rows only): `20 days` / `(20 days)` / `these 20 days` → 21; bn `20 দিন`→`21 দিন`; hi `20 दिन`/`20 दिनों`→`21 …`; ur `20 دن`/`20 دنوں`→`21 …`; ar `(20 يومًا)`→`(21 يومًا)` and `هذه الأيام العشرين`→`هذه الأيام الواحدة والعشرين`; fr `20 jours`→`21 jours`. Expected: X20c 12 + X20d 12 literal hits (see `sum`, `p`, the "Dates" table row) plus ur/ar concat hits — list each in the report.

**D4 paid launch** (CHANGE rows only): "1 ‹Jan› 2027" → "5 ‹Feb› 2027": en `1 January 2027`→`5 February 2027`, `1 Jan 2027`→`5 Feb 2027`; bn `1 জানুয়ারি 2027`→`5 ফেব্রুয়ারি 2027`; hi `1 जनवरी 2027`→`5 फ़रवरी 2027`; ur `1 جنوری 2027`→`5 فروری 2027`; ar `1 يناير 2027`→`5 فبراير 2027`; fr `1er janvier 2027`→`5 février 2027`, `1er janv. 2027`→`5 févr. 2027`. The "1" must stand alone (not `1–20`, not `21`, not `1 to 20`). Year-less "1 January" only in X20c/X20d `posts.launch` heading `h` ("What starts on 1 January" → "5 February", 6 languages).

**D5 legal versions** "in force from/since 1 January 2027" (X01, X13, X20–X20d, X24) are covered by D4 (legal pages take effect at the paid launch, contradictions.md #20). Admin `v_seed` / `ver0` / KPI-dictionary lines are KEEP.

### D-S3 — CHANGE-SPECIAL (21 rows)
1. **X20c + X20d `posts.launch`… `try` day-count puzzle** (q, steps, ans; 6 languages each). New content, mirroring each language's existing structure and wrappers:
   - en: q `The Free Beta runs from 15 January to 4 February. How many days is that?` · steps `January has 31 days: 15 to 31 January is 31 − 15 + 1 = 17 days.` / `Then 1 to 4 February is 4 days, and 17 + 4 = 21.` · ans `21 days`
   - bn: `Free Beta চলবে 15 জানুয়ারি থেকে 4 ফেব্রুয়ারি। মোট কত দিন?` · `জানুয়ারি 31 দিনের: 15 থেকে 31 জানুয়ারি = 31 − 15 + 1 = 17 দিন।` / `তারপর 1 থেকে 4 ফেব্রুয়ারি 4 দিন, আর 17 + 4 = 21।` · `21 দিন`
   - hi: `Free Beta 15 जनवरी से 4 फ़रवरी तक चलता है। यह कितने दिन हैं?` · `जनवरी 31 दिन का है: 15 से 31 जनवरी = 31 − 15 + 1 = 17 दिन।` / `फिर 1 से 4 फ़रवरी 4 दिन, और 17 + 4 = 21।` · `21 दिन`
   - fr: `La Free Beta dure du 15 janvier au 4 février. Combien de jours cela fait-il ?` · `Janvier a 31 jours : du 15 au 31 janvier, 31 − 15 + 1 = 17 jours.` / `Puis du 1er au 4 février, 4 jours, et 17 + 4 = 21.` · `21 jours`
   - ur / ar (concat form): keep the `I('…')` structure; map 20→15, نومبر/نوفمبر→جنوری/يناير, 9→4, دسمبر/ديسمبر→فروری/فبراير, month length 30→31, `I('30 − 20 + 1 = 11')`→`I('31 − 15 + 1 = 17')`, "1 to 9 … 9 days"→"1 to 4 … 4 days", `11 + 9 = 20`→`17 + 4 = 21`, answer 20→21.
2. **X20b `st_beta`** (6 langs): "Arriving in January 2027, after the Free Beta (20 November – 9 December 2026)…" → month "January 2027" → "February 2027" (first month token only, each language), then D1 on the range.
3. **X26 Beta-room close option** (`close` map, 6 langs, and the SPEC row `"v": ["2026-12-09", "2027-01-31", "none"]`): replace the value `'2026-12-09'` → `'2027-02-04'` everywhere in X26 (7 places: 6 map keys + 1 list item) and the labels by D1 rules ("The Free Beta ends (9 Dec 2026)" → "The Free Beta ends (4 Feb 2027)"). Leave `2027-01-31` (owner may drop it later). After the change, check in node that the card renders all three options in all 6 languages.

### D-S4 — must NOT be touched (expected KEEP counts are in the TSV)
PlayBoom dates "1–20 January 2027 / paid from 21 January 2027" (owner Q4) · every ISO date in code/data · all KEEP rows (demo-clock samples: Free Beta dashboards/weeks 20–26 Nov…, enrolment 20 Nov, consent logs, incidents, pen/load-test done-dates, books/P&L, payroll, legal-register `from/to`, version seeds, KPI-dictionary v1, MindForge Free Beta sample, Tanvir's timeline, X02/L05 "Wed 9 Dec" review dates) · changelog lines that record history ("26 October 2026: …", "v39: …") unless the line states a current NexaTute date · `numbers.md`/`kpi.md`/`recording.md` (clock sources).

---

## 4. Phase W — no stored money (D.111, D.114, D.132; legal Draft 2 Terms 1.7 / Refund 4.4, 4.6.6)

Decided replacements only: **(a) learning-guarantee, outage, wrong-answer and reward minutes are added back to the course as minutes, never money (legal 1.7.5, 4.4.1, 4.6.6); (b) everything is paid per order/plan at checkout for the exact amount; refunds go to the original payment method (D.111, D.114); (c) no balance, no top-up.**
Not stored money (do **not** touch): "Admit-card & document wallet", "Documents wallet", "wallet copy/copies" (X07c X03 X08 X10 X10b X25 X26 X26b X27 hub rows and X25 `wal`), "Mobile wallet" / `m_wallet` (bKash/Nagad payment method), "mobile-wallet PIN/password", "wallet provider" (chargeback text), "bKash merchant wallet" (X27), "Petty cash top-up" (accounting), X05 PlayBoom coin game (`wallet` variable / "Your money"), "Mobile-recharge shops" (X16* gift channel, see §12), fr "se recharge(nt)" (minutes refill daily / page reload).

### W1 — phrase pairs (substring, all boards; counts = occurrences now)
| id | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| W1.1 guarantee line (16 each) | `we give the minutes back as wallet credit` → `we add the minutes back to your course` | `সেই মিনিটগুলো ওয়ালেট ক্রেডিট হিসেবে ফেরত দিই` → `সেই মিনিটগুলো তোমার কোর্সে আবার যোগ করে দিই` (12); formal `সেই মিনিটগুলো আমরা ওয়ালেট ক্রেডিট হিসেবে ফেরত দিই` → `সেই মিনিটগুলো আমরা আপনার কোর্সে আবার যোগ করে দিই` (6) | `तो हम वे मिनट वॉलेट क्रेडिट के रूप में लौटा देते हैं` → `तो हम वे मिनट आपके कोर्स में वापस जोड़ देते हैं` | `تو ہم وہ منٹ والیٹ کریڈٹ کے طور پر واپس کر دیتے ہیں` → `تو ہم وہ منٹ آپ کے کورس میں واپس شامل کر دیتے ہیں` | `نعيد إليك الدقائق رصيدًا في المحفظة` → `نعيد إضافة الدقائق إلى دورتك` | `nous te rendons les minutes en crédit sur ton portefeuille` → `nous rajoutons les minutes à ton cours` (12); `nous vous rendons les minutes en crédit sur votre portefeuille` → `nous rajoutons les minutes à votre cours` (6) |
| W1.2 terms line (16 each; ur/ar 12 + digit-isolate variants) | `the credit lasts 6 months` → `the minutes stay valid for 6 months` | `ক্রেডিট থাকে 6 মাস` → `মিনিটগুলো 6 মাস বৈধ থাকে` | `क्रेडिट 6 महीने चलता है` → `मिनट 6 महीने मान्य रहते हैं` | `کریڈٹ 6 ماہ تک رہتا ہے` → `منٹ 6 ماہ تک کارآمد رہتے ہیں` | `ويبقى الرصيد صالحًا 6 أشهر` → `وتبقى الدقائق صالحة 6 أشهر` | `le crédit est valable 6 mois` → `les minutes restent valables 6 mois` |
| W1.3 "is wallet credit, not a cash refund" (X19, X24) | `It is wallet credit, not a cash refund` → `The minutes go back into your course; it is not a cash refund` | `এটি ওয়ালেট ক্রেডিট, নগদ রিফান্ড নয়` → `মিনিটগুলো আপনার কোর্সে ফেরত যায়; এটি নগদ রিফান্ড নয়` | `यह वॉलेट क्रेडिट है, नक़द रिफ़ंड नहीं` → `मिनट आपके कोर्स में वापस जुड़ते हैं; यह नक़द रिफ़ंड नहीं है` | `یہ والیٹ کریڈٹ ہے، نقد ریفنڈ نہیں` → `منٹ آپ کے کورس میں واپس شامل ہوتے ہیں؛ یہ نقد ریفنڈ نہیں` | `وهو رصيد في المحفظة، لا استرداد نقدي` → `وتعود الدقائق إلى دورتك؛ وليس استردادًا نقديًا` | `Il s’agit d’un crédit, pas d’un remboursement en espèces` → `Les minutes reviennent dans votre cours ; ce n’est pas un remboursement en espèces` |
| W1.4 "how long the credit lasts (6 months)" | `how long the credit lasts (6 months)` → `how long the minutes stay valid (6 months)` | `আর ক্রেডিট কতদিন থাকে (6 মাস)` → `আর মিনিটগুলো কতদিন বৈধ থাকে (6 মাস)` | `और क्रेडिट कितने समय तक चलता है (6 महीने)` → `और मिनट कितने समय तक मान्य रहते हैं (6 महीने)` | `اور کریڈٹ کتنی مدت تک رہتا ہے (6 ماہ)` → `اور منٹ کتنی مدت تک کارآمد رہتے ہیں (6 ماہ)` | `وكم يدوم الرصيد (6 أشهر)` → `وكم تبقى الدقائق صالحة (6 أشهر)` | `et combien de temps dure le crédit (6 mois)` → `et combien de temps les minutes restent valables (6 mois)` |
| W1.5 claim flow "come back as wallet credit" | `come back as wallet credit` → `are added back to the course` | `ওয়ালেট ক্রেডিট হিসেবে ফেরত আসবে` → `কোর্সে আবার যোগ হবে`; `… ফেরত আসে` → `কোর্সে আবার যোগ হয়` | `वॉलेट क्रेडिट के रूप में लौटेंगे` → `कोर्स में वापस जुड़ेंगे`; `… लौटते हैं` → `कोर्स में वापस जुड़ते हैं` | `والیٹ کریڈٹ کے طور پر واپس آئیں گے` → `کورس میں واپس شامل ہوں گے`; `… واپس آتے ہیں` → `کورس میں واپس شامل ہوتے ہیں` | (after W1.1) `رصيدًا في المحفظة` → `إلى الدورة` | `en crédit sur le portefeuille` → `dans le cours`; `en crédit de portefeuille` → `dans le cours` |
| W1.6 claim done | `Claimed — the credit is in your wallet.` → `Claimed — the minutes are back in your course.` | `দাবি সম্পন্ন — ক্রেডিট তোমার/আপনার ওয়ালেটে।` → `দাবি সম্পন্ন — মিনিটগুলো তোমার/আপনার কোর্সে যোগ হয়েছে।` | `दावा हो गया — क्रेडिट आपके वॉलेट में है।` → `दावा हो गया — मिनट आपके कोर्स में जुड़ गए।` | `دعویٰ ہو گیا — کریڈٹ آپ کے والیٹ میں ہے۔` → `دعویٰ ہو گیا — منٹ آپ کے کورس میں شامل ہو گئے۔` | `تمّت المطالبة — الرصيد في محفظتك.` → `تمّت المطالبة — أُضيفت الدقائق إلى دورتك.` | `Demande faite — le crédit est sur ton/votre portefeuille.` → `Demande faite — les minutes sont dans ton/votre cours.` |
| W1.7 credit validity | `Credit valid for 6 months` → `Minutes valid for 6 months` | `ক্রেডিট 6 মাস বৈধ` → `মিনিট 6 মাস বৈধ` | `क्रेडिट 6 महीने मान्य` → `मिनट 6 महीने मान्य` | `کریڈٹ 6 ماہ کارآمد` → `منٹ 6 ماہ کارآمد` | `الرصيد صالح 6 أشهر` → `الدقائق صالحة 6 أشهر` | `Crédit valable 6 mois` → `Minutes valables 6 mois` |
| W1.8 card note (X08) | `Wallet credit for lessons —` → `Minutes back for lessons —` | `পাঠের জন্য ওয়ালেট ক্রেডিট —` → `পাঠের জন্য মিনিট ফেরত —` | `पढ़ाई के लिए वॉलेट क्रेडिट —` → `पढ़ाई के लिए मिनट वापस —` | `اسباق کے لیے والیٹ کریڈٹ —` → `اسباق کے لیے منٹ واپس —` | `رصيد في المحفظة للدروس —` → `دقائق تُعاد للدروس —` | `Crédit de cours dans le portefeuille —` → `Minutes de cours rendues —` |
| W1.9 lost minutes (X20 FAQ ×4, X20 tip, X24) | `come back to your wallet` → `are added back to your course` | builder translates the 6 strings from en with the glossary below | | | | |

### W2 — whole-string replacements (en given; bn/hi/ur/ar/fr: Sonnet translates with the glossary, keeps the register of the old string, Opus reviews)
| board · key | old (en) | new (en) |
|---|---|---|
| X08 `gt_claim` | Claim 1,260 minutes as wallet credit | Claim 1,260 minutes back to the course |
| X08 `gt_claimed` | 1,260 minutes of wallet credit, valid until Sun 1 Aug 2027 | 1,260 minutes added to the course, valid until Sun 1 Aug 2027 |
| X08 `t_claim` | Claim received — the credit is in the wallet (sample) | Claim received — the minutes are added to the course (sample) |
| X24 terms/fair-use `li` + `p` (2) | …lost 1:1 minutes are credited to your wallet within 24 hours, at the course’s per-minute rate. | …lost 1:1 minutes are added back to your course within 24 hours. |
| X24 guarantee-terms `sum` | …we give back the minutes used in those 4 weeks as wallet credit [to confirm with our lawyer]. | …we add the minutes used in those 4 weeks back to the course [to confirm with our lawyer]. |
| X24 guarantee-terms `p` | …It is wallet credit, not a cash refund, and it does not change your rights under the Refund policy. | …The minutes go back into the course — not cash — and this does not change your rights under the Refund policy. |
| X24 guarantee-terms `li` | The minutes used in those 4 weeks, as wallet credit — never cash. | The minutes used in those 4 weeks, added back to the course — never cash. |
| X24 guarantee-terms `contact` | …or Settings → Wallet → Learning guarantee in the app [menu names to confirm]. | …or Settings → Plan → Learning guarantee in the app [menu names to confirm]. |
| X25 `og` note | …the minutes go back as wallet credit. The public text carries “[to confirm with our lawyer]”. | …the minutes are added back to the course. The public text carries “[to confirm with our lawyer]”. |
| X25 `og_on` | On — shown on the website, plans, wallet and progress | On — shown on the website, plans, account and progress |
| X20b `mins.d` | Used up today’s minutes? Top up from your wallet, per minute, at your course’s rate. | Used up today’s minutes? Buy extra 1:1 minutes at your course’s per-minute rate — paid at checkout, no balance kept. |
| X20b `mins.np` | The per-minute rate for this course is shown in your wallet before you top up. | The per-minute rate for this course is shown at checkout before you pay. |
| X16b `night` | Extra 1:1 minutes bought from the wallet cost 20% less between 1 and 7 am (not for school or children) | Extra 1:1 minutes bought between 1 and 7 am cost 20% less (not for school or children) |
| X16b (2nd night string) | …(e.g. ৳1.00 → ৳0.80 a minute) — a wallet rate, given separately from the plan discount. | …(e.g. ৳1.00 → ৳0.80 a minute) — a per-minute rate, given separately from the plan discount. |
| X25c `note` (rate card) | Extra 1:1 minutes from the wallet. | Extra 1:1 minutes, paid at checkout per order. |
| X25c `dpass.h` | Doubt Pass — separate top-up | Doubt Pass — separate purchase |
| X25c `dpass.note` | …USD $1 (computed); paid from the wallet. | …USD $0.55 (computed); paid at checkout. (USD per §7, U3) |
| X25c `price` / `q` / `true` | Price per top-up · Out-of-syllabus questions per top-up · Guardian approves each top-up — locked | Price per pass · Out-of-syllabus questions per pass · Guardian approves each purchase — locked |
| X02 `tip_oos`, `after` | …use a Doubt Pass top-up or add the subject. / For a full lesson take a Doubt Pass top-up or add the subject… | …use a Doubt Pass or add the subject. / For a full lesson take a Doubt Pass or add the subject… |
| X02 (Doubt Pass line) | …valid 30 days (default; $1 computed for USD users) — paid from the wallet; under 18 needs the guardian’s approval. | …valid 30 days (default; $0.55 computed for USD users) — paid at checkout; under 18 needs the guardian’s approval. |
| X10b, X16b `pass` / `inc_pass` | Daily Pass & top-ups | Daily Pass & extra minutes |
| X03 `inc` item | 1:1 call top-up (per minute) | Extra 1:1 minutes (per minute, at checkout) |
| Main `v`, W00 `d`, canvas label "L4 · Wallet & Daily Pass, …" | Wallet (and Daily Pass), notifications, profile, settings | Extra minutes & Daily Pass, notifications, profile, settings |

### W3 — L04 screen 4.1 "Wallet" → "Extra minutes & Daily Pass" (decided rule: pay per order, no balance; values = (default, editable), ৳1/min = the school per-minute rate already in X25c `rate.sch`)
| key / template | old (en) | new (en) |
|---|---|---|
| `k001` | Wallet and Daily Pass, notifications, profile and plan, settings | Extra minutes and Daily Pass, notifications, profile and plan, settings |
| `k002` | Wallet and Daily Pass | Extra minutes and Daily Pass |
| `k004` | Wallet | Extra minutes |
| `k005` | Balance | Extra 1:1 minutes left (Maths) |
| template `৳145` (big number) | ৳145 | 45 min |
| `k007` | Top up | Buy extra minutes — paid now, no balance kept |
| template chips `৳100` `৳200` `৳500` | | `30 min · ৳30` `60 min · ৳60` `120 min · ৳120` (selected = 60) |
| `k013` row value `− ৳12` | | `− 12 min` |
| `k016` + value `+ ৳100` | Top-up · Nagad | Extra 60 min bought · Nagad ; value `+ 60 min` |
| `k018` | (guarantee line) | W1.1 |
| `k019` | (terms line) | W1.2 |
k006 (per-minute rate line), k008–k011 (Daily Pass, spending limit) stay. Translate the new keys into bn/hi/ur/ar/fr (glossary). Template literal edits are allowed here only.

### W glossary (use exactly; register as in the old string)
| term | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|
| added back to your course (as minutes) | তোমার/আপনার কোর্সে আবার যোগ হয় | आपके कोर्स में वापस जोड़े जाते हैं | آپ کے کورس میں واپس شامل کیے جاتے ہیں | تُضاف إلى دورتك من جديد | rajoutées à ton/votre cours |
| paid at checkout | চেকআউটে পরিশোধ | चेकआउट पर भुगतान | چیک آؤٹ پر ادائیگی | يُدفع عند الشراء | payé au paiement |
| no balance kept | কোনো ব্যালান্স রাখা হয় না | कोई बैलेंस नहीं रखा जाता | کوئی بیلنس نہیں رکھا جاتا | لا يُحتفظ بأي رصيد | aucun solde conservé |
| extra 1:1 minutes | বাড়তি 1:1 মিনিট | अतिरिक्त 1:1 मिनट | اضافی 1:1 منٹ | دقائق 1:1 إضافية | minutes 1:1 en plus |
| original payment method | যে মাধ্যমে টাকা দিয়েছেন সেখানেই | जिस तरीके से भुगतान किया, उसी पर | جس طریقے سے ادائیگی کی، اسی پر | إلى وسيلة الدفع نفسها | le moyen de paiement utilisé |

### W4 — shared source
`shared/guarantee.md`: apply W1.1–W1.8 to §4, §4b, §5, §5b, §9 (6 legal-page blocks), §10; update its one-line summary (line 37: "back as wallet credit (not cash), valid 6 months" → "added back to the course as minutes (not cash), valid 6 months"); add a change note "v3.2 — 31 Oct 2026: wallet credit → minutes added back to the course (no stored money, D.111/D.114); terms line 'the credit lasts' → 'the minutes stay valid'". Keep the retired-v2 lines as history.

---

## 5. Phase F — refund rule (D.184, 30 Oct; all products)

Rule to state: request within 30 days of payment; refund only if approved (AI checks, a person decides; two-person approval above an admin amount); unused part, used usage deducted at list price; money to the original payment method, never a balance; automatic refunds for our faults unchanged and need no request; EU/UK 14-day right and stronger laws apply; under-18 refunds to the guardian's method; store purchases follow the store's process.

- **F1 X24 refund page** (`L.<lang>.lg.pages.refund = {…};`, 6 objects): replace the **en** object with `data/x24_refund_en.json` verbatim (compact JSON, same structure: `sum`, `secs[{h,p,li,after}]`, `contact`; 13 sections). bn/hi/ur/ar/fr: Sonnet translates the new en object section by section, formal register (bn আপনি, fr vous), ur/ar isolates as the old objects do, keeping `[to confirm …]` tags in each language's existing tag form. **Byte budget per language: new object ≤ old object** (bn 14,136 · en 6,376 · hi 14,355 · ur 9,955 · ar 9,429 · fr 7,800 B); if over, shorten wording, never drop a rule sentence. Opus reviews every line (legal text).
- **F2 X24 other refund lines**: page-summary/link texts that say "100% of the part you haven’t used" (e.g. sum line in the page index, X20b tooltip `refund` "Opens the refund policy: 30-day rule, technical problems, Paddle purchases.") → "Opens the refund policy: ask within 30 days, refund if approved, our faults fixed automatically." (X20b + X24, 6 langs).
- **F3 X16b admin rule texts**: `pass` "Year Pass, Head Start & Olympiad: the unused part is refunded within the first 30 days" → "Every purchase: refund if asked within 30 days and approved — unused part, used part at list price, to the original payment method"; `r_none` stays; `gift` lines → §12 (leave).
- **F4 X25c** `rf` "Refund window (Crash Pack, Co-Teacher Pass, MindForge Pro)" → "Refund request window (all purchases)"; the value row stays 30 days.
- Not touched: marketplace 7-day rule, affiliate "after the 30-day refund window", VAT credit notes, Paddle text (still true).

---

## 7. Phase U — USD = BDT × 1.35 ÷ 122, to the cent (D.203(1), D.213(b))

**Formula (integer-exact, use everywhere):**
```js
// USD cents from a Taka amount: half-up to the cent. paisa = Taka × 100 (Taka may be 0.80, 1.50 …)
function usdCents(bdt) { var p = Math.round(Number(bdt) * 100); return Math.floor((270 * p + 12200) / 24400); }
function usdNum(bdt) { return usdCents(bdt) / 100; }             // 7.73
function usdTxt(bdt) { return '$' + (usdCents(bdt) / 100).toFixed(2); } // "$7.73"  (same in all 6 languages; owner Q7)
```
Proof values (Python `Decimal`, `data/usd_tables.txt` §F): ৳50 $0.55 · ৳80 $0.89 · ৳100 $1.11 · ৳180 $1.99 · ৳199 $2.20 · ৳300 $3.32 · ৳399 $4.42 · ৳500 $5.53 · ৳600 $6.64 · ৳699 $7.73 · ৳799 $8.84 · ৳800 $8.85 · ৳1,000 $11.07 · ৳1,500 $16.60 · ৳3,999 $44.25 · ৳5,750 $63.63. Ties (exact half cent) only at odd multiples of ৳61; no board price is one. A USD **total** (prepay, annual) = `usdCents(total Taka)`, never a sum of rounded monthly USD. Numbers formatted as data: drop trailing zeros in JS literals (`16.6`), but **display always `toFixed(2)`** ("$16.60").

**U1 — helpers to replace (code):**
| board | current | change to |
|---|---|---|
| X20 | `USD = function (tk) { return Math.floor((tk * 15 + 499) / 1000); }`; `CUR = … ISO('$' + u)` | `USD = usdNum`; every `'$' + u` / `'$' + x` that prints a price → `'$' + Number(u).toFixed(2)` |
| X20b | `cpUsd = function (tk) { return Math.floor((tk * 15 + 499) / 1000); }` + `'$' +` print | `cpUsd = usdNum`; print `toFixed(2)` |
| X20c, X20d | `'$' +` price print (1 each) | `toFixed(2)` |
| X22, X23 | `usdOf = function (…) { return Math.max(1, Math.floor((Math.round(…) * 15 + 499) / 1000)); }` + `'$' +` prints | `usdOf = usdNum` (no `Math.max(1, …)` minimum); prints `toFixed(2)` |
| X25, X26, X26b, X27 | `usd = function (v) { return '$' + Math.round(v * 0.015); }` | `usd = usdTxt` |
| X25 | `usdR = function (b) { var x = Math.round(b) * 15 …}` | `usdR = usdNum` |
| X25c | `usdOf = function (b) { var x = Math.round(b) * 15 …}` | `usdOf = usdNum`; `usdCell` prints `toFixed(2)` |
| X27 | `usdOf = function (n) { var x = n * 0.015 …}`; `usd = function (n) { return iso('$' + n); }` | `usdOf = usdNum`; `usd = function (n) { return iso('$' + Number(n).toFixed(2)); }` |
| X10, X10b, X25, X26 (shared text method, 6 languages each) | inline `'$' + (function (b) { var x = Math.round(b) * 15, q = … })(n) + ' (computed)'` | `usdTxt(n) + ' (computed)'` (same per language: `(হিসাব করা)`, `(गणना की …)`, …) |
| X10b `FX = 122` (Paddle accounting), X14b `usd` (cost formatting), X10b `usdF` | — | **unchanged** (not price conversion) |
Define `usdCents/usdNum/usdTxt` once per board at the top of the script (inside the class file, before first use).

**U2 — hard-coded USD tables:** replace with the exact values in `data/usd_tables.txt`: A (`priceTable()` in X20, X20b, X20c, X20d — identical blocks — and the X24 copy: 18 `usd: [...]` arrays, `usdBatchOne`, `crashUsd`, `pass.usd` 2→1.11, `rec.usd` 6→4.42), B (X25c `PP17` — 60 `"*.usd"` entries), C (X27 `PU`), D (X25 `E15`). Keep the X24 comment "the same price table as X20 (keep the two in step)" true.

**U3 — literal USD strings (all 6 languages, keep wrappers):** storage add-ons "+20 GB · ৳80/month ($1)" → `($0.89)`, "+50 GB ৳180 ($3)" → `($1.99)`, "+100 GB ৳300 ($4)" → `($3.32)` (D04 k164–k166, D06 g19c, G01 k373, X03 sg_a20/50/100 + note, X08 sg_a20, X12/X12b sg_a20/50/100); Doubt Pass ৳50 "$1 (computed)" → `$0.55` (D06 g17c, X02, X25c); ৳399 add-on "(USD $6)"/"($6)" → `$4.42` (X07, X07b, X16c em_ls + `s:` arg `'$6'`, X24 `rec` text); PlayBoom X05 "abroad $9 / month" → `$6.63`, "$86 / year" → `$63.63`; L14 template `$9` `$12` `$15` → `$6.64` `$8.85` `$11.07`, `k073` "single subject $7" → `$5.53`, `k076` "Continue with Combo · $12" → `$8.85`; X24 "৳100 a month per course ($1)" → `($1.11)`.
**U4 — rule statements (6 languages):** "USD = BDT × 0.015 (Paddle)" (D06 k9), "(× 0.015, computed)" (D06 g17b), X22 `usd` "USD = BDT × 0.015, rounded to a whole dollar (at least $1)" and its marketplace note, X25c `addon.note`, `stadd.note`, `prices.foot`, `usd.r.rate`, `usd.o.rnd`, X25 `usd_note`, `ver0_c` ("USD = ৳ × 0.015 (owner, 28 Oct 2026)") → new text: **"USD = BDT × 1.35 ÷ 122, to the cent (owner, 31 Oct 2026)"**; X25c rounding lock `rnd` → "To the cent (half-up); USD totals computed from the Taka total". X25/X10/X26/X27 visible note "$ prices after Paddle’s fee (5% + $0.50), at ৳1 = $0.015" → "…, at $1 = ৳122 (sample rate)". X25c settings row `{"k": "rate", "t": "ch", "d": 0.015, "v": [0.014, 0.015, 0.016], "u": "dec"}` → `{"k": "rate", "t": "ch", "d": 122, "v": [118, 122, 126], "u": "dec"}` with label `r.rate` "USD price = Taka price × 1.35 ÷" (6 languages); check in node that the card renders and the "computed" cells use the formula (the 1.35 markup is fixed text here; making it editable is a new control — not in this pass).
Code comments with the old rule (`// BDT × 0.015 rule (৳399 → $6)`, `J1 … × 0.015`, X24 `// … 600→$9 …`) → rewrite to the new rule (`// USD = BDT × 1.35 ÷ 122, cents half-up (৳399 → $4.42)`).
**Do not touch:** "$0.015 per GB" (Cloudflare R2 price, X14b, 6 langs), Paddle "5% + $0.50", "$0 to $5", AI API budgets "$120/$95/$97", "R2 $100", bill amounts `usd: 4800/1100/80/60/35` (X10 X10b X25 X25b X25c X26 X26b X27), "$11.50 average order", X10b "$32" (books sample), bug-bounty USD amounts (§8), anything in NexaLogicDev/Motion Studio text.

---

## 8. Phase G — GPU fleet, servers, Valkey (D.199, D.201) and Phase M — misc

**G1 Valkey:** whole word `Redis` → `Valkey` in all text, all languages (112 word hits: D05 6, W00 6, X10b 6, X14 34, X14b 56, X16 6 — re-count). Keys `redis:` / `rd:` unchanged.
**G2 hardware/location strings (en; translate the 5 others with the same facts):**
| board · key | old | new |
|---|---|---|
| X14, X14b, X22 `now` (also the function form `return 'Dhaka · ' + wd + … + ' · servers in the USA'`) | … · servers in the USA | … · GPU servers in the Netherlands |
| X14b `g_loc` | All servers are in the USA. The GPU pool is shared with Remon Motion Studio and NexaLogicDev — NexaTute comes first; spare GPU time is lent to the other products (as on D05). Each new 1:1 request … | GPU servers: LeaderGPU, Netherlands (EU) — one cluster for all three products. Priority: NexaTute live classes and Nexa Speak first, then NexaLogicDev, then Remon Motion Studio; spare night-time GPU goes to video. Each new 1:1 request … (rest unchanged) |
| X14b `chk[0]` | Reserve the monthly GPU server (RTX Pro 6000, US data centre) | Rent the monthly GPU server (LeaderGPU 8× RTX A6000, Netherlands) |
| X14b server rows `hw: 'RTX Pro 6000 · 96 GB'` (AI-1…AI-5, rec; 9) | RTX Pro 6000 · 96 GB | 8× RTX A6000 · 48 GB each |
| X14b `edge_note` | …measured the delay from Bangladesh to the US nodes. … | …measured the delay from Bangladesh to the Netherlands GPU nodes. … (date part KEEP) |
| D05 `k21` | · 8 NexaTute servers · GPU pool shared with Remon Motion Studio and NexaLogicDev | · LeaderGPU Netherlands · one GPU cluster with Remon Motion Studio and NexaLogicDev |
| D05 `k27` | Spare GPU time lent — outside the 17% · Remon Motion Studio and NexaLogicDev (NexaTute first) | Spare GPU time lent — outside the 17% · priority NexaTute → NexaLogicDev → Remon Motion Studio |
| X10b `bills.gpu` | GPU servers (USA) — 5 servers | GPU servers (LeaderGPU, Netherlands) |
| X15 `host` | Hosting — US data centre (16 servers) | Hosting — GPU servers LeaderGPU, Netherlands; other servers [location to confirm] |
| X25, X25b `reg` (2 strings each) | Servers in the USA for now; … / USA (for now) | GPU servers in the Netherlands (EU); other servers [location to confirm]; … / Netherlands (GPU) · others to confirm |
| X24 privacy `p` "Our AI runs on our own servers in the USA. …" | | "Our AI runs on our own GPU servers in the Netherlands (LeaderGPU, EU). …" (rest unchanged) |
| X24 privacy `p` "Our servers are in the USA for now, and our files are stored with Cloudflare. …" | | "Our AI servers are in the Netherlands (EU) and our files are stored with Cloudflare; other servers [location to confirm]. …" |
| X24 privacy `li` "…our servers and storage in the USA, Cloudflare…" | | "…our GPU servers in the Netherlands (LeaderGPU), other servers and storage [location to confirm], Cloudflare…" |
Leave unchanged (numbers/clock pass, owner Q11): server counts and capacity samples ("AI GPU servers (4)", AI-1…AI-5 rows, "Add 1 GPU server", bill amount $4,800), the city tables `us: 'USA (server)'` (non-GPU server location undecided, Q10), fallback-API order (out of scope, see §13).

**M1 guardian learning discount (D.203(2)):** X25c SPEC17 `disc` row `{"k": "gl", "t": "ch", "d": 50, "v": [30, 50], "u": "pct"}` → `{"k": "gl", "t": "ch", "d": 30, "v": [20, 30], "u": "pct"}`. No other board holds it (grep `"gl"`).
**M2 bug bounty (five-gaps-solutions §2, approved 30 Oct, D.156):** critical $500 · high $200 · medium $50 + hall of fame; no cash for under-18; acknowledge 3 business days (already "3 working days"), triage 7 days; test accounts only, no real users'/children's data, no DDoS, no social engineering. Amounts are fixed USD (not converted).
| board · key | new (en; translate) |
|---|---|
| X24 security `sum` "There is no paid bug bounty at launch. …" | We pay a bug bounty for valid reports — critical $500, high $200, medium $50 — and list you on our public hall of fame if you wish. No cash rewards for anyone under 18. |
| X24 `h` "Thank-you list instead of a paid bug bounty" | Bug bounty and hall of fame |
| X24 `p` "At launch we do not pay rewards for reports. …" | Valid reports are rewarded: critical $500, high $200, medium $50 [amounts set in admin]. Reporters are named on our public hall of fame, by name or nickname, only if they agree. No cash for anyone under 18; test accounts only — never real users’ or children’s data, no DDoS, no social engineering. |
| X24 two `li` with "thank-you list" | "…on the hall of fame." / "…add your name or nickname to the public hall of fame and pay the bounty for its severity." |
| X15 `bounty.true` | Bug bounty: critical $500 · high $200 · medium $50 + hall of fame (with consent); no cash under 18 — locked |
| X15 note "…no paid bug bounty at launch — a public thank-you list instead (only with the reporter’s consent)." | "…bug bounty critical $500 / high $200 / medium $50 and a public hall of fame (only with the reporter’s consent); no cash under 18." |
| X15 `sr_st.fixed` | Fixed — bounty paid, on the hall of fame (with consent) |
| W00 `d` (3 descriptions) | "no paid bug bounty — a public thank-you list, with the reporter’s consent" → "bug bounty $500 / $200 / $50 + hall of fame, with the reporter’s consent"; "public thank-you list" → "bug bounty + hall of fame" |
**M3 institution discounts vs caps:** not decided (D.177 "to confirm") → no change (Q8).

---

## 9. Order of work (each board touched once)

1. Copy repo → `W/before/`, `W/project/`, `W/shared/`; record `wc -c` and the pattern counts (`counts_rename.tsv` regenerated) → `W/report/before.tsv`.
2. Build `textfix.py`: phases R → D → W → F → U → G → M as functions on the file text; D uses `dates_actions.tsv` (+ concat rule); W/F/G/M use the pairs above; U uses `usd_tables.txt`. Dry-run on all 72 boards → `changes.tsv` + per-pattern counts. **Stop if any expected count differs.**
3. Translations (Sonnet) for: W1.9, W2, W3 (5 languages), F1 refund page (5 languages), G2 rows, M2 rows, R2 ar. Put them in `W/report/translations.tsv` (board, key, lang, old, new) and feed them to the pipeline as exact pairs.
4. Real run, one save per board, in this order (largest/risky first so problems show early): X20d, X24, X20c, X20b, X20, X25c, X25, X26, X26b, X27, X10, X10b, X13, X14, X14b, X15, X16b, X22, X23, then all other boards, then `canvas.json`, then `shared/*.md`.
5. After each save: `node --check` on the extracted script, dcverify, size check; failing board → restore from `W/before/` and report.
6. Haiku: run §10 checks on all 72 boards; Opus: line-by-line review of `changes.tsv` (all money, legal, refund, USD, dates rows; samples of the rename rows ≥ 10% per board) before anything reaches the repo.

## 10. Verification (all must pass; paste outputs in `W/report/VERIFY.md`)

1. **dcverify** `python3 W/tools/dcverify.py W/project/<board> --langs bn,en,hi,ur,ar,fr` → `nproblems 0, nparity 0` on all 72. Plus a side-method parity check (node: call every method that returns a `{bn,en,hi,ur,ar,fr}` object, compare key paths/array lengths/types across the 6 languages) — 0 differences on changed boards.
2. **Sizes:** `wc -c W/project/*.dc.html` — every board ≤ 1,150,000. Report before/after per changed board.
3. **Greps (after):**
   - `Nexa Teacher` 0 · `Nexa Co-Teacher` only `Nexa Co-Teacher Pass` (6) · `Co-Teacher` = 121, all followed by ` Pass` (0 if R1-PASS approved) · `Nexa Tutor` = 2,756 · `Co-Tutor` = 1,123 · `নেক্সা টিচার|नेक्सा टीचर|نیکسا ٹیچر|معلّم نيكسا` 0.
   - Protected unchanged: `Be the Teacher` 240 · `L05-AI-Teacher` 8 · `L07-Co-teacher` 8 · `X09-Prototype-Teacher` / `T01-Teacher-Mobile` hrefs same · `Teacher’s AI assistant` same · `مساعد المعلّم الذكي` same · `AI Teacher Live` 143 (unless Q9 yes).
   - `\bAI teachers?\b` 0 · `AI শিক্ষক|AI शिक्षक|AI استاد` 0 · `professeurs? IA|enseignants? IA|prof IA` 1 (the parents–professeur IA line).
   - Dates: in CHANGE boards no `20 Nov(ember)?|9 Dec(ember)?|1 Jan(uary)? 2027` (and 5 other languages) outside KEEP rows — script compares every remaining hit against the KEEP list (expected remaining = KEEP rows: 502 literals + KEEP concat hits). `15 January – 4 February 2027` / `5 February 2027` present in X20–X20d, X24, X01, L02.
   - Wallet: `\b[Ww]allet\b` (en) only in the allowed list of §4 (document/admit-card/mobile/merchant/copies/X05 code/petty cash) — script prints every remaining hit with its key; bn/hi/ur/ar/fr wallet words likewise; `top-up|Top-up|Top up|top up` only "Petty cash top-up"; `wallet credit|crédit sur (ton|votre|le) portefeuille|ওয়ালেট ক্রেডিট|वॉलेट क्रेडिट|والیٹ کریڈٹ|رصيدًا في المحفظة` 0. `shared/guarantee.md` the same except retired-v2/history lines.
   - Refund: `100% of the part you haven’t used|unused wallet balance` 0; X24 refund objects parse as JSON in all 6 languages; each ≤ its old byte size.
   - USD: `0\.015` only the R2 "$0.015 per GB" (6) and inside the X25c "rate" history if any (list); `\* ?15 ?\+ ?499|Math\.round\(v \* 0\.015\)|Math\.round\(b\) \* 15` 0; every `usd: [` array in priceTable has the values of `usd_tables.txt`; node test: `usdCents(699)=773, (799)=884, (50)=55, (61)=68, (5750)=6363`; render X20 USD view and X25c price editor — all prices show 2 decimals.
   - GPU: `\bRedis\b` 0 · `Valkey` = old Redis count · `RTX Pro 6000|US data centre|servers in the USA` 0 · `LeaderGPU` present in X14b, X10b, X15, X24, D05.
   - Misc: X25c `"k": "gl"` row d 30; `no paid bug bounty|thank-you list|Pas de bug bounty payant` 0 (all 6 langs).
4. **Diff summary instead of lostcheck:** `W/report/DIFF.md` — per board: bytes before/after, number of changed literals per phase, number of KEEP date rows confirmed untouched, and `changes.tsv` (every old → new). Opus reviews this file.
5. Links/sidebars: no href, id, sidebar `<aside>` text keys changed — compare `<aside>…</aside>` hashes before/after for the two admin groups (labels in asides contain no renamed word except D01/D03 "Teacher", which are human → unchanged).

## 11. Size impact (estimates; the pipeline must measure)

| board | spare now | R | D | W/F | U | estimate |
|---|---:|---:|---:|---:|---:|---|
| X20d | 3,785 | −540 | +300…600 (bn +15 B per range) | ≈ −50 | +200 | fits (≈ +0.3 KB net) — measure after each phase |
| X24 | 6,875 | −252 | +250 | refund objects ≤ old; W ≈ 0; bug bounty +1.0…1.5 KB (6 langs) | +40 | fits (≈ +1.2 KB) |
| X20c | 58,150 | −468 | +700 | ≈0 | +200 | fits |
| X12b, X10b, X19 | ≥ 12 KB | small | 0 | 0 | +100 | fits |
Rule: if any board passes 1,148,000 B after a phase, stop and report (do not trim other text).

---

## 12. Needs owner decision — not changed in this pass

1. **Demo clock** vs new dates (all KEEP rows in `dates_actions.tsv`: admin samples, books, versions, Free Beta dashboards, learner timelines; `numbers.md`, `kpi.md`, `recording.md`).
2. **Shikkha Salami gift cards** (Taka face values ৳800/৳20, sales via bKash agents and recharge shops, 12-month validity, "can be given to someone else"): X10 `eid`, X16/X16b/X16c gift tables and `t5`/`gift` rule lines, X25b gift sales, X25c `gv`/`h`, X27, D06 g17d, D09 k51, L15 k060, W00, X24 terms/gift page text. D.114 says named-plan vouchers; launch status, transferability and the agent channel are open (legal hold).
3. **"Helper learning credits (18+)"** (X08, X20b, X25 `p_hcr`/`hcr`): stored value or minutes/plan days?
4. Server counts, capacity samples and GPU bill amounts in admin (5 GPU servers / $4,800, 4 AI servers + AI-5, on-demand "Add 1 GPU server") vs the final rented fleet.
5. Location of non-GPU servers (database, LiveKit, app) — boards' city tables say "USA (server)".
6. Institution 30%/40% as base price under the caps.
7. "Co-Teacher Pass" product name; "AI Teacher Live" feature name; L05/L07 file names.

## 13. Out of scope but found (report to the owner, no change now)
- X14/D05 AI fallback order (own model → Mistral → Claude Opus; Luna 6 "overload fallback for Nexa Co-Teacher text answers") conflicts with D.207 (under-18 requests never go to outside AI) — needs its own fix.
- Affiliate "10% commission for the first 3 months" (X12b `aff_s`, X17) vs "10% for 12 months with cap" (D.140 / unified-credit-governance) — confirm if the 12-month rule covers NexaTute.
- PlayBoom's own Free Beta 1–20 Jan 2027 now starts before the NexaTute Free Beta.

## 14. Questions for the owner (short)
1. Demo clock: (a) keep sample dates as they are for now (Claude recommends), (b) move the demo date to after the paid launch (e.g. Mon 15 Mar 2027) in a separate numbers pass, or (c) make Mon 1 Feb 2027 a Free Beta day and rewrite the samples? — pick one.
2. Rename the paid "Nexa Co-Teacher Pass" to "Nexa Co-Tutor Pass"? yes / no
3. Show the Free Beta as "15 January – 4 February 2027 (21 days)", paid from 5 February? yes / no
4. PlayBoom dates (Free Beta 1–20 Jan, paid 21 Jan 2027): keep, or new dates? keep / new (give dates)
5. Shikkha Salami gift vouchers: off until the lawyer confirms (yes), or on at launch as named-plan vouchers? off / on
6. "Helper learning credits (18+)": turn into free minutes/plan days (yes) or remove? minutes / remove
7. USD shown as "$7.73" with a dot in all languages and exact half-cents rounded up? yes / no
8. Institution prices 30%/40% are base prices, so the 45%/30% caps apply on top? yes / no
9. Rename "AI Teacher Live" to "AI Tutor Live"? yes / no
10. Database/app/LiveKit servers: Netherlands too, or USA? NL / USA / later
11. Recompute admin GPU samples to the real fleet (2 × 8×A6000 at Feb 2027, €2,998/month) in the numbers pass? yes / no
12. Extra 1:1 minutes on the Account screen sold per order as 30/60/120 minutes at the course's per-minute rate (৳1/min school)? yes / no

---

## 10. Owner answers 31 Oct — addendum

Sources: `docs/decisions.md` lines added in commits c0b4fa8, 4ef211e, a0c67a8 (31 Oct 2026). **This section wins over every earlier section of this spec where they differ.** Superseded in full: §3 (Phase D), §12, §13 (except the "out of scope" note on Nexa Verify), §14. Superseded in part: §2 gate R1-PASS (now ON), §2 R2 "AI Teacher Live" exclusion (now renamed), §4 W3 (packs), §8 G2 (server locations), §8 M3 (discounts), §11 (sizes, see 10.12). The builder can now run the whole pass in one go; there are **no open owner questions** that block it.

### 10.1 Final dates — parameter table (all date work is driven by this table)

| parameter | value | source |
|---|---|---|
| `BETA_START` | Fri 25 Dec 2026 | decisions 4ef211e |
| `BETA_END` | Thu 14 Jan 2027 (21 days) | 〃 |
| `PAID_START` | Fri 15 Jan 2027 | 〃 |
| `PILOT` | Fri 11 – Thu 24 Dec 2026 (default, editable) | 〃 |
| `DEMO_NOW` | Fri 25 Dec 2026, **16:20** (kept: the boards use 16:20) — day 1 of 21 of the Free Beta | 〃 |
| `PB_BETA`, `PB_PAID` | PlayBoom = same as NexaTute (25 Dec 2026 – 14 Jan 2027; paid 15 Jan 2027) | c0b4fa8 item 4 + 4ef211e |
| `HISTORY_END` | 31 Oct 2026 — anything dated on/before stays (company history, decision/"owner, 28 Oct" stamps, legal drafting) | coordinator |
| old anchors | Free Beta 20 Nov – 9 Dec 2026; paid 1 Jan 2027; demo now Mon 1 Feb 2027 16:20; PlayBoom Beta 1–20 Jan, paid 21 Jan 2027 | boards / numbers.md |
| Nexa Speak store release | 15 Jan 2027 (to confirm) — no board shows it yet; nothing to change | 4ef211e |

The table lives at the top of `tools/datemap.py` (`P = dict(…)`). Change a value, re-run, and every date row in `data/dates_map.tsv` is recomputed; nothing else in this spec depends on the literal dates except the hand-written strings in 10.3 (they use the same values and are listed so they can be regenerated).

### 10.2 Date engine (replaces §3 entirely)

`tools/datemap.py PROJECT OUT.tsv [--apply DST]` scans the raw source of all 72 boards (all 6 languages, ISO dates in data, `Date.UTC` constants), and writes one row per date with `board, start, end, lang, class, rule, old, new, old_text, new_text, key, flags`. Output for the final table: **`data/dates_map.tsv` (13,482 rows; 7,670 changed)** and **`data/dates_summary.tsv`** (per-board counts and byte delta).

Mapping (old date → new date). **Weekday names are always recomputed with Python from the new date**, in the same language and form (short/long), and month names are copied from the boards' own spellings (Bangla য+়, Hindi फ़):

| rule | old dates | new dates | meaning |
|---|---|---|---|
| M0 | ≤ 31 Oct 2026 | unchanged | history / stamps |
| M1 | 1 – 19 Nov 2026 | + (BETA_START − old Beta start) = +35 days → 6 – 24 Dec 2026 | pre-Beta preparation (lands in the pilot window) |
| M2 | 20 Nov – 8 Dec 2026 | +35 days → 25 Dec 2026 – 12 Jan 2027 (capped one day before BETA_END) | Free Beta day n stays day n |
| M3 | 9 Dec 2026 | BETA_END 14 Jan 2027 | Beta end |
| M4 | 10 – 31 Dec 2026 | linear into the pilot window 11 – 24 Dec 2026 | prep "before the paid launch" (load test LT-03, legal gate, R2 restore test…) |
| M5 | ≥ 1 Jan 2027 | + (PAID_START − old paid) = +14 days | everything after the paid launch: weekdays unchanged, intervals unchanged (1 Jan → 15 Jan, 1 Feb → 15 Feb) |
| M7 clock | on admin boards (D05–D10, X10, X10b, X13–X17, X19, X21, X22, X25*, X26*, X27): the demo "today" and the last 7 days before it, when the date carries a time, "Today/Live ·", "Dhaka ·", or a log key (`at/ts/when/last/seen/time/login/since`) | DEMO_NOW − (old now − d) → 18 – 25 Dec 2026 | headers "Dhaka · Fri 25 Dec 2026, 16:20", "Today · Friday, 25 December 2026", audit/notification/sign-in stamps |
| PB | PlayBoom dates (literal mentions PlayBoom): "1–20 January", "from 1 to 20 January", "21 January 2027" | PB_BETA / PB_PAID | answer 4 |
| month labels | "<Month> <Year>" without a day | month of f(14th of that month): Nov 2026 → Dec 2026; Dec, Jan, Feb … unchanged | money screens keep calendar months (VAT/Mushak and payroll are calendar months by law) |
| EXTERNAL | Ramadan/Eid/holidays/national days (21 Feb, 26 Mar, 16 Dec, 14 Apr, 25 Dec…), SSC/HSC routines, admit cards, board notices & circulars, exam series, admission/scholarship calendars, Crash Pack opening and HSC Head Start (tied to exam dates), the Exam & Admission Hub (X07c and hub keys `ev*`, `corr*`, `pub_d*`, `lv*`, `cal_s`, `hub*`, `kh*`, `notice`, `se_h`, `f16*`) | unchanged | real-world calendar — never moves |

Ranges are handled as one unit (`20 Nov – 9 Dec 2026` → `25 Dec 2026 – 14 Jan 2027`, year inserted when the two ends fall in different years; `D1–D2 Month` that crosses a month becomes `D1 Month – D2 Month`; word ranges "du 1er au 31 janvier", "from 1 to 20 January", "من 1 إلى 20 يناير", "1 থেকে 9 ডিসেম্বর" included). ur/ar concatenations (`I('20') + ' نومبر – ' + I('9') + …`) are edited token by token, wrappers kept. Year-less dates get their year from a following year, then from the weekday, then by default (Jul–Dec → 2026, Jan–Jun → 2027; flag YEARGUESS). The decision for one key is copied to the same key in all 6 languages (English decides; if any language is EXTERNAL the group is EXTERNAL).

**Checked (by me, on a scratch copy, not the repo):** applying `dates_map.tsv` to all 72 boards → `node --check` 0 failures and `dcverify --langs bn,en,hi,ur,ar,fr` **0 problems / 0 parity on all 72**. Total growth from dates alone +9,049 B; largest X20c +919, X13 +768, X20b +744, X20d +728.

**Review artifacts (Opus reviews before merge):** `data/dates_lang_mismatch.tsv` lists 196 board×language groups where a language changes a different set of dates than English (mostly English-only code comments, a few different phrasings, e.g. "8–22 Feb" written as one range in bn). The builder resolves each by hand to match English, or marks it "comment only". Rows with flags `YEARGUESS`, `CROSSRANGE`, `WORDRANGE`, `REVIEW-CODE` are in the review list too.

**Builder steps for dates:** (1) run `datemap.py` on the pristine copy with `--apply` FIRST (offsets refer to the untouched file), (2) apply the 10.3 specials, (3) then phases R, W, F, U, G, M of the spec on the result. Rows with class SPECIAL (the puzzle) are not applied by the engine.

### 10.3 Date specials (hand-written; regenerate from 10.1 if the dates change)

1. **Free Beta length** — in strings about the Free Beta, `20 days`/`(20 days)`/`these 20 days`/`in 20 days` → **21** (bn `20 দিন`, hi `20 दिन/दिनों`, ur `20 دن/دنوں`, ar `(20 يومًا)` and `هذه الأيام العشرين` → `هذه الأيام الواحدة والعشرين`, fr `20 jours`): X20c/X20d `sum`, `p`, the "Dates" table row; X02/X18 "You’ve come a long way in 20 days!", "before → after the Free Beta (20 days)" (all languages).
2. **Day-count puzzle** (X20c, X20d, `posts.beta…try`; 6 languages, keep ur/ar `I('…')` structure):
   - en: q `The Free Beta runs from 25 December to 14 January. How many days is that?` · steps `December has 31 days: 25 to 31 December is 31 − 25 + 1 = 7 days.` / `Then 1 to 14 January is 14 days, and 7 + 14 = 21.` · ans `21 days`
   - bn: `Free Beta চলবে 25 ডিসেম্বর থেকে 14 জানুয়ারি। মোট কত দিন?` · `ডিসেম্বর 31 দিনের: 25 থেকে 31 ডিসেম্বর = 31 − 25 + 1 = 7 দিন।` / `তারপর 1 থেকে 14 জানুয়ারি 14 দিন, আর 7 + 14 = 21।` · `21 দিন`
   - hi: `Free Beta 25 दिसंबर से 14 जनवरी तक चलता है। यह कितने दिन हैं?` · `दिसंबर 31 दिन का है: 25 से 31 दिसंबर = 31 − 25 + 1 = 7 दिन।` / `फिर 1 से 14 जनवरी 14 दिन, और 7 + 14 = 21।` · `21 दिन`
   - fr: `La Free Beta dure du 25 décembre au 14 janvier. Combien de jours cela fait-il ?` · `Décembre a 31 jours : du 25 au 31 décembre, 31 − 25 + 1 = 7 jours.` / `Puis du 1er au 14 janvier, 14 jours, et 7 + 14 = 21.` · `21 jours`
   - ur/ar: same numbers; months نومبر/نوفمبر → دسمبر/ديسمبر and دسمبر/ديسمبر → جنوری/يناير; `I('30 − 20 + 1 = 11')` → `I('31 − 25 + 1 = 7')`; `11 + 9 = 20` → `7 + 14 = 21`.
3. **Free Beta state words on admin/learner Beta screens** (today is day 1): en text below; translate to the 5 other languages keeping each board's register.
   | board · key | new (en) |
   |---|---|
   | D05 `k19` | Individual 508 (459 NexaTute + 49 PlayBoom) · institution seats 720 · Free Beta 25 Dec 2026 – 14 Jan 2027: day 1 of 21 — 1,764 signed up (cap ≈2,000) · sample (prototype) |
   | X10 `beta`, X27 `beta` | The Free Beta runs 25 December 2026 – 14 January 2027 with about 2,000 seats; today is day 1 of 21 and 1,764 have signed up (sample, prototype). |
   | X10 `k_beta` | Free Beta (25 Dec 2026 – 14 Jan 2027) · day 1 of 21 |
   | X16b `beta_h` | Free Beta measures · 25 Dec 2026 – 14 Jan 2027 · day 1 of 21 (sample) |
   | X16b `sample`, `mk_sample` | "…the Free Beta (25 Dec 2026 – 14 Jan 2027) pilots the items…" / "MindForge starts with the Free Beta (…); these are sample values (prototype)." |
   | X14b `edge_note` | No edge server at launch. The Free Beta (25 Dec 2026 – 14 Jan 2027) measures the delay from Bangladesh to our servers (app servers in the USA, GPU servers in the Netherlands). … (rest unchanged) |
   | X14b `sub`, `bp_s`, X14 `all`; D05 `g18d` | keep the (mapped) dates and add " · day 1 of 21" after the range |
   | X15 `samp` | Sample (prototype) — the queue on Fri 25 Dec 2026 at 11:20 (Free Beta day 1) |
   | X27 `beta_today` | Today ({0}) is day 1 of the Free Beta — it runs Fri 25 Dec 2026 – Thu 14 Jan 2027. Sample for the opening day: |
   | X03 `tip_beta` "Your Free Beta has ended…" (paid-era learner view) | unchanged (it is the after-Beta view) |
   The public site keeps its two era views (beta view / paid view); past tense in the paid view is correct ("The Free Beta (25 December 2026 – 14 January 2027) is over; paid plans started on 15 January 2027").
4. **Hub sample clock** — the Exam & Admission Hub screens are an external exam-calendar sample whose countdowns depend on "Mon 1 Feb 2027"; they keep that date but stop calling it the prototype clock: `Prototype clock: Mon 1 Feb 2027, 16:20` → `Exam-calendar sample date: Mon 1 Feb 2027, 16:20 (prototype)` in X07c, L08 and the hub blocks of G01/X08 (6 languages; key `clock`/`hub_clock`). On learner/guardian/teacher boards that are not hub screens (X05, X09, X12, X12b, X23, X08 `clock`), the clock date follows M5 (→ Mon 15 Feb 2027) and the label becomes `Sample date (prototype): Mon 15 Feb 2027, 16:20` — these screens show the paid product after launch.
5. **Code constants** (`Date.UTC`, 15 places; class REVIEW-CODE): X22 `stamp` base `Date.UTC(2027, 1, 1, 0, NOWM + k)` → `Date.UTC(2026, 11, 25, 0, NOWM + k)` (admin clock); X16 `cBars` `Date.UTC(2027, 0, 26 + i)` → `Date.UTC(2026, 11, 19 + i)` (last 7 days before today); X16b `TODAY = Date.UTC(2027, 1, 1)` → `Date.UTC(2027, 1, 15)` with comment `// money sample "as of" date (M5 +14); the demo today is Fri 25 Dec 2026` (refund-window maths must stay consistent with the +14 money data); X12/X12b `dayLbl` `Date.UTC(2027, 1, 1 + dd)` → `Date.UTC(2027, 1, 15 + dd)`, X12b `mfDays` base → `Date.UTC(2027, 1, 15)`, X18 `dt` base `Date.UTC(2027, 0, 22)` → `Date.UTC(2027, 1, 5)` (all M5); unchanged: X08 `NOW = Date.UTC(2027, 1, 1)` (hub calendar), X10/X10b `Date.UTC(2027, 0, 1)` (month label "January"), X12/X12b `tm`/`tmA` (time formatting only), X12 calendar `sat0` (month view of Feb 2027). After the change run the board in node and check the rendered labels.
6. **Christmas** — 25 Dec is a public holiday in Bangladesh, and D01 `k030` says "No batch classes on public holidays and Eid (1:1 and Co-Teacher keep running)". The admin "now" samples show live batch classes at 16:20. Least change, honest: keep the sample numbers and add to each admin live-now caption (X14 live classes card, D05 `k16`/`k17`, X14b fleet card) the note "sample (prototype) — on 25 Dec (public holiday) only 1:1 and Co-Tutor classes run". Ramadan text ("Ramadan is coming — from about 8 February") stays true for 25 Dec; no change.
7. **Money screens** (owner a0c67a8): revenue, payroll, refunds, payouts, VAT, P&L, cash and totals keep their numbers; dates follow M5 (+14) so the first paid period starts 15 Jan 2027; calendar-month labels (January 2027 = first month with sales, from 15 Jan) stay. Each money section must show a "sample (prototype)" label — use the existing one where the board has it; otherwise append ` · sample (prototype)` (6 languages) to the section heading. Builder: list every money section heading in X10, X10b, X15, X16b, X17 (affiliate ledger), X21 (refund approvals), X25*, X26*, X27, D05, D06 with "has label: yes/no" in `W/report/money_labels.tsv` and add the label where it is missing.

### 10.4 Answers 2 & 3 — rename additions
- R1 gate **ON**: `Nexa Co-Teacher Pass` → `Nexa Co-Tutor Pass`, `Co-Teacher Pass` → `Co-Tutor Pass` (121 hits, 13 boards). Expected after: `Co-Teacher` 0; `Co-Tutor` 1,244; `Nexa Co-Tutor Pass` 6.
- `AI Teacher Live` → `AI Tutor Live` (143) and the remaining `AI Teacher` (13, the same weekly livestream) → `AI Tutor`, all 6 languages (the boards write it in Latin everywhere); regex `(?<![-\w])AI Teacher\b` so `L05-AI-Teacher` stays. Also the code comment "AI Teacher Live" in numbers.md v14 note stays (history).

### 10.5 Answers 5 & 6 — gift vouchers and Helper minutes (free minutes, never a Taka value, admin-controlled)
| board · key / code | change |
|---|---|
| X16b gift table (`GB0`, `gVals`, `g_l.val`, rows `val: tk(g.val)`, approval text `t.ad.gift(…, tk(g.val), …)`) | the voucher value is minutes: `val: tk(g.val)` → `val: nf(g.val) + ' ' + t.min_u` (add `min_u`: en "min", bn "মিনিট", hi "मिनट", ur "منٹ", ar "دقيقة", fr "min"); `gVals` button text `tk(v) + ' · ' + …` → `nf(v) + ' ' + t.min_u + ' · ' + …`; label `g_l.val` "Card value" → "Free minutes per voucher"; numbers stay (20 / 800 / 2,400 → minutes). Sales totals (`soldV`) stay money (voucher price = minutes × the course per-minute rate, ৳1 default) — add to `g_pol_h` rules list: "A voucher gives free learning minutes, never a Taka value; its price is the minutes × the course’s per-minute rate (default)". `g_out` keeps "owed as learning time". |
| X16, X16c gift rows (same pattern) | same rendering and labels |
| text (6 langs) | "Gift cards" → "Gift vouchers (free minutes)"; "Shikkha Salami card(s)" → "Shikkha Salami voucher(s) (free minutes)"; "Gift cards cannot/are never refunded as cash" → "Gift vouchers give free minutes and are never refunded as cash"; X10/X27 `eid` "Eid — Shikkha Salami gift cards" → "Eid — Shikkha Salami vouchers (free minutes)"; X10 "Gift-card campaign · retailer stock" → "Gift-voucher campaign · retailer stock"; X10b `inc_gift`/`gift` "Gift cards & Year Pass" → "Gift vouchers & Year Pass"; X16b `ret` "Gift-card retailer" → "Gift-voucher retailer"; X25b `gift` → "Gift vouchers (Shikkha Salami, free minutes) — sales and redemption"; X25c `refund.h`, `pp_note` "gift cards" → "gift vouchers"; `gv` "Gift card validity" → "Gift voucher validity"; `gr` "Retailer commission on gift cards" → "Retailer commission on gift vouchers"; D06 `g17d`, W00 `d` "gift cards" → "gift vouchers"; D09 `k51` "Education Salami gift card" → "Education Salami voucher (free minutes)"; X24 terms gift page `h` "Gift cards" → "Gift vouchers", `p` → "Shikkha Salami gift vouchers give free learning minutes (never a money value), are valid for 12 months (default), can be given to someone else and are not refunded in cash."; X24 refund page — already in `data/x24_refund_en.json` (updated: 6,285 B) |
| X25c SPEC17 `refund` card — new row after `gv` | `{"k": "gmin", "t": "lk", "d": true, "u": "lk"}` label `r.gmin` "Gift vouchers give free minutes only — never a Taka value (owner, 31 Oct 2026)" |
| Helper (answer 6) | label "Helper learning credits (18+)" → "Helper free minutes (18+)" (X25 `p_hcr`, `hcr`; X08 and X20b plan lists; 6 langs). X25c SPEC17 `disc` card — new row `{"k": "hfm", "t": "ch", "d": 10, "v": [5, 10, 15], "u": "min"}` label `r.hfm` "Helper free minutes (18+), per accepted answer (default)" — 10 = the existing best-question reward (`bq`), Claude default, editable |
The settings kit already renders `ch`/`lk` rows with "(default)", two-person approval and the log; verify the two new rows render in all 6 languages (node).

### 10.6 Answer 7 — total discount never above 30% (institution included)
| place | change |
|---|---|
| X25c SPEC17 `disc` rows | `c2` v [20, 30, 40] → [20, 25, 30]; `t1` d 30 v [20, 30, 40] → [20, 25, 30]; `t2` d 40 v [30, 40, 50] → **d 30**, v [20, 25, 30]; `gl` (guardian, M1) d 30 v [20, 25, 30]; `p3` stays (10%); new row `{"k": "cap", "t": "lk", "d": true, "u": "lk"}` label "Total discount never above 30% — institution prices included (owner, 31 Oct 2026)" |
| strings with 40% institution discount (6 langs) | D04 `k16` "320 seats bought · 100+ seats → 40% off" → "320 seats bought · institution price 30% off (the most any discount can give)"; D04 `k37`, X12b `b_tier_note`, X12b `disc`, X24 institution `li`: "30% off for 20–99 seats, 40% off for 100+" → "30% off for 20 or more seats (no discount goes above 30% in total)"; X20b `v` "40% off" / "−40 %" → check context: if it is the institution tier chip, → "30% off" |
| code | X12b `discFor(n)` — the 100+ tier returns 40 → return 30 (both tiers 30); render the institution order card and check the unit price |
| prices derived from 40% (recompute by code: unit = round(list × 0.7)) | D04 `k32` "৳360" (SSC Batch 600) → "৳420"; X17 pipeline `val` 64,800 (180 × 360) → 75,600, 1,15,200 (320 × 360) → 1,34,400 (and the matching text "Rajshahi Medha 180 → ৳64,800, Chattogram Ideal 320 → ৳1,15,200"), Rangpur and any other "× ৳360" line; Alokito College HSC Batch "৳420 a seat" (700 × 0.6) → "৳490", "200 seats → ৳84,000" → "৳98,000" wherever the string shows the multiplication |
| money totals that contain these invoices (January institution seats ৳2,83,200, P&L, cash) | **unchanged** (owner a0c67a8: money screens keep their sample numbers) — list each one in `W/report/discount_totals.tsv` as "sample, not recomputed" |
| 45% cap | no NexaTute board shows a 45% discount cap (grep "45%" hits only CSS widths); nothing to remove. Motion Studio's 45% per-minute cap is outside this pass |
Builder: grep all boards for `40 ?%|40 %|−40|45 ?%` in discount/price contexts (exclude CSS, storage "40%", talk-time "40%", search-trend "+40%", "(40%)" quiz scores) and write every hit with its decision to `W/report/discounts.tsv`.

### 10.7 Answers 8 & 9 & 10
- **Servers (answer 8):** database, app and LiveKit servers stay in the USA for now; the GPU fleet is LeaderGPU, Netherlands. Replace §8 G2 location rows with:
  | board · key | new (en) |
  |---|---|
  | X14, X14b, X22 `now` (and function form) | Dhaka · Fri 25 Dec 2026, 16:20 · app servers USA · GPU Netherlands |
  | X14b `g_loc` | App, database and LiveKit servers: USA. GPU servers: LeaderGPU, Netherlands (EU) — one cluster for all three products; priority NexaTute live classes and Nexa Speak first, then NexaLogicDev, then Remon Motion Studio. Each new 1:1 request goes to the least-loaded GPU group that hosts that subject’s model. |
  | X15 `host` | Hosting — app, database & LiveKit servers: USA; GPU servers: LeaderGPU, Netherlands |
  | X25, X25b `reg` | App, database and LiveKit servers in the USA for now and GPU servers in the Netherlands (EU); Personal Data Protection Act 2026 s.29 cross-border rules — a DPA with every provider (Accounts, support & legal › DPA register). / short form: "USA (app) · Netherlands (GPU)" |
  | X24 privacy | "Our AI runs on our own GPU servers in the Netherlands (LeaderGPU, EU) …"; "Our app and database servers are in the USA for now, our AI servers are in the Netherlands (EU), and our files are stored with Cloudflare. …"; providers list "…our servers in the USA (app, database) and the Netherlands (GPU, LeaderGPU), Cloudflare…" |
  | city tables `us: 'USA (server)'` | unchanged (correct) |
- **Extra-minute packs (answer 9):** L04 W3 chips are now the decided packs `30 min · ৳30`, `60 min · ৳60`, `120 min · ৳120` (৳1/min default; USD by the §7 formula: $0.33 / $0.66 / $1.33 where a USD view exists). Admin control: X25c SPEC17 `rate` card — add rows `{"k": "pk1", "t": "ch", "d": 30, "v": [15, 30, 45], "u": "min"}`, `{"k": "pk2", "t": "ch", "d": 60, "v": [45, 60, 90], "u": "min"}`, `{"k": "pk3", "t": "ch", "d": 120, "v": [90, 120, 180], "u": "min"}` with labels "Extra-minute pack 1 / 2 / 3 (per order, at the course’s per-minute rate)"; `rate.note` → "Extra 1:1 minutes are sold per order in packs (30 / 60 / 120 min, default) at the course’s per-minute rate — no balance kept." X20b `mins.d` → "Used up today’s minutes? Buy an extra-minute pack (30, 60 or 120 min) at your course’s per-minute rate — paid at checkout, no balance kept."
- **Affiliate 12 months (answer 10):** X25c SPEC17 `refund` card `afm` d 3 v [1, 3, 6] → **d 12, v [6, 12, 24]**; strings (6 langs): X12b `aff_s` "…for the first 3 months…" → "first 12 months", X12b `aff`, X16b `p_rules`, X17 `nc_note_aff`, `af_rules` ("first 3 months" → "first 12 months"). Code: in X17 and X16b search for a 3-month commission window constant (e.g. `3` months / `90` days in the affiliate ledger) and set it to 12 months / 365 days; ledger sample amounts stay (money rule).

### 10.8 GPU samples recomputed to the real fleet (D.199, D.201; coordinator: this pass)
Fleet on the demo date Fri 25 Dec 2026 (D.199 ramp): **A6000 #1 only** (8 × RTX A6000 48 GB, rented early Dec 2026 for the 1-week test, €1,499/month); A6000 #2 (Nexa Speak) from 1 Jan 2027; A6000 #4 (Motion Studio) from 15 Jan 2027; A6000 #3 + 8×A100 (NexaLogicDev) from 15 Mar 2027; full fleet €10,986/month. Least-change rule: the old "AI servers" become **GPU groups of 2 cards** (2 × 48 GB = 96 GB, the same capacity number the samples use), so loads/capacity samples stay valid.
| place | change |
|---|---|
| X14b fleet code (`srvRows`) | `n: 'AI-' + (i + 1)` → `n: GN[i]` with `var GN = ['A6000 #1 · GPU 1–2', 'A6000 #1 · GPU 3–4', 'A6000 #1 · GPU 5–6', 'A6000 #1 · GPU 7–8', 'Cloud GPU (emergency, hourly)']`; `hw: 'RTX Pro 6000 · 96 GB'` → `hw: i < 4 ? '2× RTX A6000 · 96 GB' : 'cloud GPU · hourly'`; the scale-out row `AI-5` → `n: GN[4], hw: 'cloud GPU · hourly'`; `rec` row hw → `'CPU (FFmpeg) · no GPU (default)'`; comment "520 learners per AI server" → "per GPU group (2 cards)" |
| tokens in strings (X14, X14b, X21; 6 langs) | `AI-1`…`AI-4` → `GPU 1–2`…`GPU 7–8`; `AI-5` → `cloud GPU`; "AI GPU server(s)" → "GPU group(s) (2× A6000)"; "AI GPU servers (4)" → "GPU groups on A6000 #1 (4)"; "add a GPU server" / "Add 1 GPU server" / "no extra GPU server needed" → "add an emergency cloud GPU (hourly)" / "Add 1 emergency cloud GPU (hourly)" / "no extra GPU needed"; `g_add` tip → "Starts one emergency cloud GPU (hourly, our own models; charged to NexaTute). It is logged and stops by itself after the peak."; `k_gpu` → "Average load of the GPU groups. At 60% we start an emergency cloud GPU (hourly)."; `chk[0]` → "Rent the next A6000 server (LeaderGPU, Netherlands) — A6000 #2 is planned from 1 Jan 2027" |
| D05 `k20`/`k21` | "Shared GPU system" · "A6000 #1 (8 cards, LeaderGPU Netherlands) · #2 from 1 Jan 2027 · one GPU cluster with Remon Motion Studio and NexaLogicDev" |
| open bills (X10, X10b, X25, X25b, X25c, X26, X26b, X27 `{ id: 3, k: 'gpu', usd: 4800, due: … }`) | the February rent of NexaTute's two A6000 servers (#1 + #2) = €2,998 → **`usd: 3237.84`** at **€1 = $1.08 (sample rate, to confirm — no EUR rate in decisions)**; label `bills.gpu` → "GPU servers — LeaderGPU Netherlands, 2 × 8×A6000 (€1,499 each; $ at €1 = $1.08, sample rate)" |
| closed-month cost maps (X10b `['2026-12', { … gpu: 4800 …}]`, `'2027-01'`, P&L, cash, runway) | **unchanged** (owner money rule a0c67a8); note in the report |
| Motion Studio / NexaLogicDev shares | not shown on NexaTute money screens; nothing to add |
Finding for the owner (not blocking, no change): with the Free Beta now starting 25 Dec, A6000 #2 (Nexa Speak voice) only arrives 1 Jan 2027 — the first week of the Beta runs on one server.

### 10.9 X14 — under-18 requests never go to outside AI (D.207; owner c0b4fa8)
The boards only display the fallback; there is no routing code. Strings (6 languages):
| board · key | new (en) |
|---|---|
| X14 `c8` | AI fallback order (18+): own model → Mistral Large 3 → Claude Opus → human · Under 18: own model → human only; when our GPUs are busy the request waits in the queue (locked) |
| X14 `ch.mis` / `ch.cla` | Mistral Large 3 API (18+ only) / Claude Opus API (18+ only) |
| X14 `tip.ch.mis` / `tip.ch.cla` | Gets the questions our own model could not settle — adults (18+) only; under-18 questions never leave our servers. / Gets the hardest questions Mistral could not settle — adults (18+) only. |
| X14 `luna` (long form) | Overload fallback for Nexa Co-Tutor text answers when the GPUs are full — adults (18+) only; under-18 requests wait in the queue |
| X14 `c142` | Busy page on for GPU 3–4; adult Co-Tutor requests on the Mistral fallback, under-18 requests queued on our own servers; 14 learners kept their place and got their minutes back. |
| X14b `net` | Safety net stays: our own servers + the Valkey queue; for adults (18+) also the Luna 6, Mistral Large 3 and Claude Opus APIs. Under-18 requests never go to an outside AI — they wait in the queue, and lost minutes are added back. |
| D05 `k33` | 18+: Mistral Large 3 → Claude Opus → a person (Luna 6 only on overload) · Under 18: our own servers → a person |
| D05 `k30` | Nexa Co-Tutor fallback (18+ only) |
| X24 privacy `p` "…some questions go to a cloud AI provider under a data processing agreement." | append: "This happens only for users aged 18 or over; questions from learners under 18 always stay on our own servers." |
Code (X14): the chain array keeps its sample counts; add after the chain list (template) one line `<p class="xs">{{ t.ch_u18 }}</p>` with `ch_u18` = "Under 18: own model → human only — never an outside AI (locked, owner 31 Oct 2026)" in all 6 languages; check parity.

### 10.10 Earlier sections — what changes
- §3 Phase D → replaced by 10.1–10.3. `data/dates_actions.tsv` is superseded by `data/dates_map.tsv`.
- §2 R1-PASS → ON (10.4); R2 → "AI Teacher Live" renamed (10.4).
- §4 W2/W3 → packs per 10.7; gift/Helper per 10.5.
- §5 F1 → use the updated `data/x24_refund_en.json` (6,285 B).
- §8 G2 → 10.7 server table + 10.8 fleet; M3 → 10.6.
- §9 order → (0) copy, (1) **dates engine on the pristine copy**, (2) 10.3 specials, (3) R incl. 10.4, (4) W incl. 10.5, (5) F, (6) U, (7) G incl. 10.7–10.9, (8) M incl. 10.6; one save per board after all phases.
- §10 verification — add: (a) `datemap.py` re-run on the result finds no old-anchor dates in DATE class (only EXTERNAL/history rows remain); (b) "Free Beta … day 1 of 21" present on D05, X10, X27, X16b; (c) `Co-Teacher` 0, `AI Teacher` 0 except `L05-AI-Teacher`; (d) `"t2"` row d 30 and no discount choice above 30 in X25c; `afm` d 12; `gmin`, `hfm`, `cap`, `pk1–pk3` rows render; (e) no `AI-[1-5]\b` and no `RTX Pro 6000` left; `usd: 3237.84` in the 8 bill tables; (f) every money section has a sample label (`money_labels.tsv` all "yes").
- Shared sources: `numbers.md` D1 "Demo clock" and `kpi.md` change notes get one new dated line each ("31 Oct 2026: demo today Fri 25 Dec 2026 16:20 = Free Beta day 1 of 21; Free Beta 25 Dec 2026 – 14 Jan 2027; paid 15 Jan 2027; sample dates mapped by tools/datemap.py; money samples keep their numbers (owner)"); their older history lines stay.

### 10.11 New owner question
None blocking. (Two findings only: A6000 #2 arrives 1 Jan, a week after the Beta starts — 10.8; and the EUR→USD sample rate €1 = $1.08 needs a real rate from the accountant.)

### 10.12 Expected size deltas (bytes; dates measured, the rest estimated)
| board | now | dates (measured) | rename | W/F/U/G/M (est.) | expected | ≤ 1,148,000? |
|---|---:|---:|---:|---:|---:|---|
| X20d | 1,146,215 | +728 | −540 | +150 | ≈1,146,550 | yes (≈1.4 KB spare) — measure after every phase |
| X24 | 1,143,125 | +135 | −252 | +1,500 (bug bounty, privacy, guarantee, refund ≤ old) | ≈1,144,500 | yes |
| X12b | 1,137,848 | +38 | −24 | +600 (discount, affiliate strings) | ≈1,138,500 | yes |
| X10b | 1,129,881 | +140 | −54 | +300 | ≈1,130,300 | yes |
| X19 | 1,105,885 | +64 | −70 | +50 | ≈1,106,000 | yes |
| X20c | 1,091,850 | +919 | −468 | +150 | ≈1,092,500 | yes |
| X13 | 479,936 | +768 | small | small | — | yes |
| all others | < 1,030,000 | ≤ +744 | | | | yes |
Rule unchanged: stop if any board passes **1,148,000 B** after any phase; report, do not trim other text.

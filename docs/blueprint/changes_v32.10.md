# Blueprint v32.9 → v32.10 — change report

## সংক্ষেপে (বাংলা)

- নতুন সংস্করণ: Corporate Edition v32.10, তারিখ 29 অক্টোবর 2026। আপনার সিদ্ধান্ত (29 অক্টোবর, বিকেল 3:53): ৳500 = $7 — USD নিয়ম (টাকা × 0.015, নিকটতম ডলার, ঠিক .5 হলে নিচে) কোনো ব্যতিক্রম ছাড়া সব USD দামে প্রযোজ্য। 11.2-এর "(to confirm)" নোট সরানো হয়েছে, নিয়মটি চূড়ান্ত হিসেবে লেখা।
- বদলানো দাম: Class 6–8 Batch $8 → $7; Personal single $8 → $7 — Class 4–5, Class 6–8, Class 9–10/SSC ও SSC Vocational, HSC, HSC Vocational ও Admission, BCS + Job (11.2); Nexa Co-Teacher Pass $2 → $1, কারণ ৳100 × 0.015 = $1.50 (3.22, 11.14); prepay উদাহরণ: Class 6–8 Batch 3 মাস $18, 6 মাস $35।
- বাকি সব USD দাম নিয়মের সাথে মিলিয়ে দেখা হয়েছে (27টি ৳/$ জোড়া ও 11.2-এর পুরো টেবিল) — আর কোনো অমিল নেই। মিনিটভিত্তিক আন্তর্জাতিক wallet রেট ($0.03/$0.05/$0.08) ও wallet top-up আলাদাভাবে অনুমোদিত, রূপান্তর নয়; Motion Studio ও NexaLogicDev-এর USD তাদের +35% নিয়মে।
- লক্ষ্য করুন: memory-র পুরোনো লাইনে Co-Teacher Pass "$2" লেখা ছিল; নতুন "কোনো ব্যতিক্রম নেই" নিয়মে এটি $1 হয়েছে — অন্যরকম চাইলে জানাবেন।

## Summary

- Register rows: **244 → 244** (added 0, updated 0, rows removed by merging 0; 0 merges in all).
- Product codes, whole register: B 96 → 96, N 69 → 69, M 21 → 21, E 33 → 33, L 25 → 25.
- Body units (paragraphs, headings and table rows) added 2, changed 9, removed 0.
- Repeated paragraphs inside one section in v32.10: 0.

## 1. Software register (18.1)

### 1.1 Added rows

| Software | Licence | Product | Runs on | Status |
|---|---|---|---|---|

### 1.2 Merged duplicates


Rows removed by these merges: .

### 1.3 Updated rows (field-level)

| v32.9 row | Fields changed | Product |
|---|---|---|

Every added or changed row has a licence, a status, a product code and a placement (checked by the script: all present).

## 2. Edit log by section (from the build script)

- **11.2** (updated): USD for ৳500 prices $8 → $7: Class 6–8 Batch; Personal single of Class 4–5, Class 6–8, Class 9–10/SSC (and SSC Vocational), HSC/HSC Vocational/Admission and BCS + Job
- **11.2** (updated): Rounding rule stated as final (exact .5 down, no exception; ৳500 = $7); the “(to confirm)” note removed; prepay example Class 6–8 Batch 3 months $18, 6 months $35
- **3.22, 11.14** (updated): Nexa Co-Teacher Pass USD $2 → $1 (৳100 × 0.015 = $1.50, exact .5 rounds down)

## 3. Hardware and placement

- No hardware or register change.

## 4. Body changes by section (script diff)

### 3.22

- changed para: “Nexa Co-Teacher Pass: ৳100 a month per course ($2) for the full Nexa Co-Teacher — text lessons, step-by-step answers and topic summaries — for 25 topics a day,…” → “Nexa Co-Teacher Pass: ৳100 a month per course ($1) for the full Nexa Co-Teacher — text lessons, step-by-step answers and topic summaries — for 25 topics a day, the same limit as the plans; during overload Pass users get cached answers first and then wait in t…”

### 11.2

- changed para: “International prices (USD): learners whose billing country is outside Bangladesh (for example India, Pakistan, the Middle East and the diaspora, 2.5) pay the m…” → “International prices (USD): learners whose billing country is outside Bangladesh (for example India, Pakistan, the Middle East and the diaspora, 2.5) pay the monthly plan prices below — the BDT price × 0.015, rounded to the nearest dollar (an exact 0.50 round…”
- changed row: “Class 4–5 | — | — | $15 | $8” → “Class 4–5 | — | — | $15 | $7”
- changed row: “Class 6–8 | $8 | $11 | $15 | $8” → “Class 6–8 | $7 | $11 | $15 | $7”
- changed row: “Class 9–10 / SSC, SSC Vocational | $9 | $12 | $15 | $8” → “Class 9–10 / SSC, SSC Vocational | $9 | $12 | $15 | $7”
- changed row: “HSC, HSC Vocational, Admission Test Preparation | $10 | $13 | $15 | $8” → “HSC, HSC Vocational, Admission Test Preparation | $10 | $13 | $15 | $7”
- changed row: “BCS + Job Test Preparation | $11 | $13 | $15 | $8” → “BCS + Job Test Preparation | $11 | $13 | $15 | $7”

### 11.14

- changed row: “Nexa Co-Teacher Pass (3.22) | ৳100 a month per course ($2); 25 topics a day; cached answers and the queue during overload” → “Nexa Co-Teacher Pass (3.22) | ৳100 a month per course ($1); 25 topics a day; cached answers and the queue during overload”

### Appendix D

- added row: “v32.10 | 29 October 2026 | Owner decision of 29 October 2026 (15:53): ৳500 = $7 — the USD rule (Taka × 0.015, nearest dollar, an exact .5 rounds down) applies to every USD price with no exception; the “(to confirm)” note of v32.9 is removed and the rule is st…”

### Cover

- changed row: “Edition | Corporate Edition v32.9 | 29 October 2026” → “Edition | Corporate Edition v32.10 | 29 October 2026”

### Edition history

- added row: “v32.10 | 29 October 2026 | USD rounding final: an exact .5 rounds down with no exception (৳500 = $7); USD figures corrected (11.2, 3.22, 11.14)”

## 5. Checks

See checks.txt (register duplicate check, repeated paragraphs, phase wording, validation, render and TOC).

## 6. Items marked “(to confirm)” or “(default, editable)” in this edition

- Nexa Co-Teacher Pass $1 follows the no-exception rule; an older memory line says $2 — owner may confirm. No other new “(to confirm)” items; the USD-rounding item is closed.

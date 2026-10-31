# NexaTute boards: health check, ja/de/zh/ko size estimate, split plan

Date 31 Oct 2026. Repo `/home/claude/nexatute` was only read. Nothing in it was edited, committed or pushed. All work files are in `/tmp/claude-0/-home-claude/9c0c5ff5-dbc3-5918-808a-b72f22b21703/scratchpad/boards/`. Note: dcverify.py normally writes a temp `_dcv_run_*.js` next to itself in `prototype/tools/`; to keep the repo untouched I ran a byte-identical copy (`.../boards/tools/dcverify.py`), which removes its own temp files.

## Summary

- Files: 59 `.dc.html` boards + `canvas.json` (25,960 B) = the 60 files. Boards total 28,568,503 B.
- dcverify, run on all 59 boards (`xargs -P 4`, 1500 s timeout; each finished in 0-3 s, exit code 0): **59 of 59 gave nproblems 0 and nparity 0. No failures.** Raw output per board: `.../boards/v/<board>.out`. Caveat from reading the script: it checks key parity of `uiText()` only, not the side text methods (`f18Text`, `hubText`, `exText`, ...).
- Languages: every board has exactly bn, en, hi, ur, ar, fr (X15/X16/X17/X19 list en first). None has ja/de/zh/ko yet.
- Current sizes: all 59 are <= 1,800,000 B. Closest: X20 1,795,876 (4,124 B spare), X25 1,775,578, X12 1,767,889, X10 1,764,276, X16 1,707,709, X26 1,699,549.
- At 10 languages (my estimate, method below): **8 boards exceed 1,800,000 B in the middle estimate, and also in the low estimate: X07, X10, X12, X14, X16, X20, X25, X26.** X24-Legal is the only board close but under (est. 1.64-1.79 MB). Everything else fits. All boards together would grow from 28.6 MB to about 39.8 MB.
- Sidebar rule: X10, X25, X26, X27 are byte-identical (same SHA-256). X13-X22 are NOT byte-identical: 8 boards, 8 different hashes, see section 4.
- Fonts: no font is embedded in any board. All 59 use a Google Fonts `<link>` in `<helmet>`; the Netlify build script swaps these for self-hosted files. No CJK font is referenced anywhere yet.
- Broken paths: build.py, checks.py, apply_shot.py, shoot14.py, dbg.py, dbg3.py, shots.py, smoke.py, build-preact.js and others point at a workspace or files that do not exist (section 6).

## How the boards store text (found by reading, not assumed)

- A board = `<x-dc>` template (with `<helmet>` for CSS and font links) + one `<script type="text/x-dc">` with a `Component` class. All text sits in the script: `uiText()` (in X01 it calls `i18n()`) builds `L.bn = {...}; L.en = ...; L.hi; L.ur; L.ar; L.fr`, one object per language, or one JSON object `{"bn":{...},"en":{...}}`. Bigger boards add more methods with the same shape: X07 has 17, X05 has 9, X14/X16 have dozens of `ui*` methods.
- dcverify.py gets the languages by calling `new Component().uiText()` and reading `Object.keys()`. It renders every `{{ hole }}` in every language and compares each language against `bn` (key path, array length, value type). Boards fall back to English per key: `t = Object.assign({}, L.en, L[lang])`, so a missing key shows English silently (parity check is the only guard).
- The language list is also hard-coded as `LANGS = ['bn','en','hi','ur','ar','fr']` in 19 boards (X08-X17 and X19-X27) and in `langNames()`. Adding four languages needs code edits there, not only text. `<html lang="bn">` in X01.
- "keys" below = number of text leaves per language. Where two numbers are shown, the first is `uiText()` only, the second all language-keyed methods in the board. I counted leaves by loading each board in node, calling every method and walking objects that have bn/en/fr keys. Leaf counts are equal across the six languages in every board.

## 1. Table: all boards

Columns: bytes = `wc -c`. problems/parity = dcverify nproblems / nparity. 6-lang text = estimated bytes the six language blocks occupy in the file. est. 10 langs = bytes + estimated de+zh+ja+ko text (middle value; low-high in brackets, thousands of bytes). over = middle estimate above 1,800,000. "close" = high estimate above 1,750,000 but middle below limit.

| board | bytes | problems | parity | languages | keys (uiText / all) | 6-lang text B | est. B at 10 langs (low-high) | over? | proposed split |
|---|---:|---:|---:|---|---:|---:|---:|---|---|
| D01-Learner-Desktop | 98,518 | 0 | 0 | bn,en,hi,ur,ar,fr | 114 / 114 | 69,151 | 137,368 (133k-142k) | no | none |
| D02-Classroom-Desktop | 46,686 | 0 | 0 | bn,en,hi,ur,ar,fr | 41 / 41 | 35,001 | 66,950 (65k-69k) | no | none |
| D03-Content-Studio | 44,195 | 0 | 0 | bn,en,hi,ur,ar,fr | 81 / 81 | 28,609 | 60,853 (59k-63k) | no | none |
| D04-Institution | 137,604 | 0 | 0 | bn,en,hi,ur,ar,fr | 193 / 193 | 103,114 | 193,047 (187k-201k) | no | none |
| D05-Admin-Overview | 78,621 | 0 | 0 | bn,en,hi,ur,ar,fr | 80 / 80 | 64,284 | 114,303 (110k-119k) | no | none |
| D06-Admin-Plans | 70,731 | 0 | 0 | bn,en,hi,ur,ar,fr | 73 / 73 | 54,724 | 100,825 (97k-105k) | no | none |
| D07-Admin-Safety | 76,418 | 0 | 0 | bn,en,hi,ur,ar,fr | 91 / 91 | 62,205 | 109,713 (106k-114k) | no | none |
| D08-Admin-Quality | 56,485 | 0 | 0 | bn,en,hi,ur,ar,fr | 77 / 77 | 41,916 | 79,122 (76k-82k) | no | none |
| D09-Admin-Schedule | 44,257 | 0 | 0 | bn,en,hi,ur,ar,fr | 78 / 78 | 31,168 | 61,257 (59k-63k) | no | none |
| D10-Admin-Helpline-Sponsor | 47,044 | 0 | 0 | bn,en,hi,ur,ar,fr | 91 / 91 | 32,371 | 64,735 (62k-67k) | no | none |
| G01-Guardian-1 | 293,263 | 0 | 0 | bn,en,hi,ur,ar,fr | 424 / 424 | 203,634 | 402,531 (391k-418k) | no | none |
| G02-Guardian-2 | 42,464 | 0 | 0 | bn,en,hi,ur,ar,fr | 68 / 68 | 24,649 | 56,022 (54k-57k) | no | none |
| L01-Onboarding-1 | 41,083 | 0 | 0 | bn,en,hi,ur,ar,fr | 56 / 56 | 21,198 | 53,182 (51k-54k) | no | none |
| L02-Onboarding-2 | 47,462 | 0 | 0 | bn,en,hi,ur,ar,fr | 82 / 82 | 26,440 | 61,845 (60k-63k) | no | none |
| L03-Home-Plans | 62,686 | 0 | 0 | bn,en,hi,ur,ar,fr | 101 / 101 | 34,371 | 81,954 (80k-84k) | no | none |
| L04-Account | 77,083 | 0 | 0 | bn,en,hi,ur,ar,fr | 110 / 110 | 47,984 | 103,333 (100k-106k) | no | none |
| L05-AI-Teacher | 81,147 | 0 | 0 | bn,en,hi,ur,ar,fr | 105 / 105 | 49,447 | 108,857 (106k-112k) | no | none |
| L06-Batch-Class | 62,089 | 0 | 0 | bn,en,hi,ur,ar,fr | 97 / 97 | 37,189 | 82,921 (80k-85k) | no | none |
| L07-Co-teacher | 73,119 | 0 | 0 | bn,en,hi,ur,ar,fr | 125 / 125 | 41,105 | 96,323 (94k-99k) | no | none |
| L08-Tests | 54,458 | 0 | 0 | bn,en,hi,ur,ar,fr | 95 / 95 | 31,249 | 71,360 (69k-73k) | no | none |
| L09-Progress | 69,264 | 0 | 0 | bn,en,hi,ur,ar,fr | 97 / 97 | 44,387 | 94,164 (91k-97k) | no | none |
| L10-StudyHall-Lab | 40,506 | 0 | 0 | bn,en,hi,ur,ar,fr | 87 / 87 | 21,174 | 52,912 (51k-54k) | no | none |
| L11-Moderator | 35,543 | 0 | 0 | bn,en,hi,ur,ar,fr | 57 / 57 | 20,319 | 47,517 (46k-49k) | no | none |
| L12-More-Learning | 41,547 | 0 | 0 | bn,en,hi,ur,ar,fr | 66 / 66 | 23,538 | 55,038 (53k-56k) | no | none |
| L13-Beyond-Syllabus | 36,887 | 0 | 0 | bn,en,hi,ur,ar,fr | 58 / 58 | 22,408 | 49,723 (48k-51k) | no | none |
| L14-Safety-Links-Global | 46,191 | 0 | 0 | bn,en,hi,ur,ar,fr | 77 / 77 | 31,333 | 64,234 (62k-66k) | no | none |
| L15-Free-Growth | 41,696 | 0 | 0 | bn,en,hi,ur,ar,fr | 68 / 68 | 27,043 | 57,568 (55k-59k) | no | none |
| Main | 65,491 | 0 | 0 | bn,en,hi,ur,ar,fr | 117 / 112 | 38,831 | 87,079 (84k-89k) | no | none |
| P01-PlayBoom-1 | 26,242 | 0 | 0 | bn,en,hi,ur,ar,fr | 36 / 36 | 7,400 | 30,556 (30k-31k) | no | none |
| P02-PlayBoom-2 | 18,976 | 0 | 0 | bn,en,hi,ur,ar,fr | 22 / 22 | 6,103 | 22,607 (22k-23k) | no | none |
| T01-Teacher-Mobile | 44,797 | 0 | 0 | bn,en,hi,ur,ar,fr | 67 / 67 | 26,955 | 59,503 (57k-61k) | no | none |
| W00-Website-Preview | 630,312 | 0 | 0 | bn,en,hi,ur,ar,fr | 207 / 207 | 565,239 | 936,388 (899k-987k) | no | none |
| X01-Prototype-Flow1 | 548,296 | 0 | 0 | bn,en,hi,ur,ar,fr | 507 / 686 | 376,054 | 751,217 (730k-779k) | no | none |
| X02-Prototype-Flow2 | 660,647 | 0 | 0 | bn,en,hi,ur,ar,fr | 509 / 849 | 438,606 | 903,395 (879k-936k) | no | none |
| X03-Prototype-Flow3 | 371,835 | 0 | 0 | bn,en,hi,ur,ar,fr | 231 / 426 | 241,567 | 501,697 (488k-519k) | no | none |
| X04-Prototype-Flow4 | 454,421 | 0 | 0 | bn,en,hi,ur,ar,fr | 413 / 545 | 286,951 | 613,657 (597k-635k) | no | none |
| X05-Prototype-Flow5 | 500,675 | 0 | 0 | bn,en,hi,ur,ar,fr | 739 / 1,486 | 292,116 | 667,085 (651k-689k) | no | none |
| X06-Prototype-Batch | 412,289 | 0 | 0 | bn,en,hi,ur,ar,fr | 164 / 537 | 290,183 | 569,774 (553k-591k) | no | none |
| X07-Prototype-Test | 1,667,860 | 0 | 0 | bn,en,hi,ur,ar,fr | 916 / 4,009 | 1,291,518 | 2,396,136 (2327k-2490k) | **YES** | 3 boards: X07, X07b-...-ExamAid, X07c-...-Hub |
| X08-Prototype-Guardian | 1,005,124 | 0 | 0 | bn,en,hi,ur,ar,fr | 1,201 / 1,419 | 759,051 | 1,420,803 (1378k-1478k) | no | none |
| X09-Prototype-Teacher | 265,806 | 0 | 0 | bn,en,hi,ur,ar,fr | 340 / 400 | 188,609 | 371,931 (361k-386k) | no | none |
| X10-Prototype-Admin | 1,764,276 | 0 | 0 | bn,en,hi,ur,ar,fr | 2,783 / 2,759 | 1,249,699 | 2,471,381 (2398k-2571k) | **YES** | 2 boards: X10, X10b-Prototype-Admin-Accounts |
| X11-Prototype-Tools | 351,462 | 0 | 0 | bn,en,hi,ur,ar,fr | 398 / 497 | 230,194 | 477,012 (464k-493k) | no | none |
| X12-Prototype-Institute | 1,767,889 | 0 | 0 | bn,en,hi,ur,ar,fr | 2,612 / 2,793 | 1,334,238 | 2,507,245 (2432k-2609k) | **YES** | 2 boards: X12, X12b-Prototype-Institute-Ops |
| X13-Prototype-LandingAI | 477,839 | 0 | 0 | bn,en,hi,ur,ar,fr | 661 / 636 | 332,136 | 666,338 (646k-693k) | no | none |
| X14-Prototype-Ops | 1,360,158 | 0 | 0 | bn,en,hi,ur,ar,fr | 2,156 / 2,092 | 930,326 | 1,878,857 (1825k-1951k) | **YES** | 2 boards: X14, X14b-Prototype-Ops-Infra |
| X15-Prototype-Accounts | 788,266 | 0 | 0 | en,bn,hi,fr,ur,ar | 1,195 / 1,227 | 530,373 | 1,082,963 (1053k-1123k) | no | none |
| X16-Prototype-Quality | 1,707,709 | 0 | 0 | en,bn,hi,ur,ar,fr | 2,537 / 2,543 | 1,177,518 | 2,372,358 (2303k-2466k) | **YES** | 3 boards: X16, X16b-...-Money, X16c-...-ExamAid |
| X17-Prototype-Growth | 871,579 | 0 | 0 | en,bn,hi,ur,ar,fr | 1,422 / 1,480 | 642,818 | 1,230,670 (1195k-1279k) | no | none |
| X18-Prototype-MindForge | 829,220 | 0 | 0 | bn,en,hi,ur,ar,fr | 499 / 1,125 | 583,785 | 1,145,280 (1113k-1189k) | no | none |
| X19-Prototype-MarketingHub | 1,105,885 | 0 | 0 | en,bn,hi,ur,ar,fr | 1,726 / 1,676 | 707,467 | 1,505,497 (1465k-1559k) | no | none |
| X20-Prototype-Landing | 1,795,876 | 0 | 0 | bn,en,hi,ur,ar,fr | 2,631 / 2,318 | 1,383,897 | 2,550,489 (2468k-2662k) | **YES** | 3 boards: X20, X20b-...-Plans, X20c-...-More |
| X21-Prototype-Comms | 824,678 | 0 | 0 | bn,en,hi,ur,ar,fr | 1,294 / 1,275 | 567,667 | 1,145,484 (1113k-1189k) | no | none |
| X22-Prototype-AvatarVoice | 496,438 | 0 | 0 | bn,en,hi,ur,ar,fr | 719 / 723 | 310,904 | 672,184 (654k-696k) | no | none |
| X23-Prototype-AvatarVoice-User | 359,450 | 0 | 0 | bn,en,hi,ur,ar,fr | 536 / 575 | 242,384 | 492,903 (479k-510k) | no | none |
| X24-Prototype-Legal | 1,143,125 | 0 | 0 | bn,en,hi,ur,ar,fr | 1,572 / 981 | 1,071,299 | 1,703,794 (1639k-1791k) | close | optional pre-emptive 2-way split (X24 + X24b) |
| X25-Prototype-AdminPlans | 1,775,578 | 0 | 0 | bn,en,hi,ur,ar,fr | 2,528 / 2,518 | 1,267,668 | 2,486,399 (2410k-2589k) | **YES** | 3 boards: X25, X25b-...-Platform, X25c-...-Pp |
| X26-Prototype-AdminRules | 1,699,549 | 0 | 0 | bn,en,hi,ur,ar,fr | 2,135 / 2,126 | 1,052,950 | 2,281,638 (2219k-2366k) | **YES** | 2 boards: X26, X26b-Prototype-AdminRules-More |
| X27-Prototype-CoAdmin | 929,708 | 0 | 0 | bn,en,hi,ur,ar,fr | 1,403 / 1,810 | 676,716 | 1,300,184 (1261k-1352k) | no | none |
| canvas.json | 25,960 | n/a | n/a | n/a (layout data: board titles, x/y/w/h) | n/a | n/a | unchanged | no | add one entry per new board |

Notes on the keys column: the second number counts each distinct (path, value) once, so it can differ from the first number (array nodes are counted in the first only, and strings identical in several languages are merged in the second); it is not a parity failure. X05 shows 673 / 1,486 because most of its text sits in `kidText`, `guardText`, `guardText0` etc. D, G, L, P, T boards and Main are small (< 0.3 MB) and stay far under the limit.

## 2. Size estimate for ja, de, zh, ko

### Measured (all 59 boards, six current languages)

| language | chars / en chars | string bytes / en string bytes | bytes per char |
|---|---:|---:|---:|
| bn | 0.965 | 2.38 | 2.51 |
| hi | 0.979 | 2.36 | 2.46 |
| ur | 0.968 | 1.67 | 1.75 |
| ar | 0.924 | 1.62 | 1.78 |
| fr | 1.190 | 1.23 | 1.05 |
| en | 1.000 | 1.00 | 1.02 |

Sum over all boards: en strings 1,309,966 B (1,670,711 B including keys and quotes); the six language blocks together about 20.3 MB (about 71% of all board bytes). The rest is template, CSS and logic.

### Method

1. For each board I loaded the script in node, called `uiText()` and every other method that returns language-keyed objects, and measured per language: string bytes (UTF-8), characters, and bytes including the key name and JSON punctuation. O = overhead per entry (key + quotes + comma) = en bytes incl. keys minus en string bytes; S = en string bytes.
2. Coverage correction: some text is in the file once but rendered many times, and some boards keep part of the script text in the template or generate it in code. I compared the count of Bengali/Devanagari/Arabic characters found in the file with the count found in the measured blocks and divided by that coverage (0.34-1.86; most boards 0.9-1.07). Small static boards (D, L) have low coverage; the rule does not matter for the limit.
3. Added bytes per new language = (O + f x S) / coverage, with f = (new-language string bytes) / (en string bytes):
   - de: f = 1.05 x fr ratio (1.23) = 1.29 (low 1.14, high 1.46). German UI text is a little longer than French; this is the assumption with least evidence.
   - zh: chars about 0.38 x en (low 0.33, high 0.45); 2.76 bytes per char (CJK = 3 B, digits/punctuation/placeholders = 1 B; Bengali measured 2.51 on the same material); f = 1.05.
   - ja: chars about 0.52 x en (0.45-0.60); 2.72 B per char; f = 1.41. ja mixes kana and kanji and keeps more Latin loan words.
   - ko: chars about 0.62 x en (0.55-0.72); 2.56 B per char (Hangul has spaces between words); f = 1.59.
   Sum of the four: mid = 4 x O + 5.34 x S. In total this adds about 11.3 MB to the 20.3 MB the six blocks occupy now (+55%), range +10.3 to +12.4 MB.
4. The CJK char ratios are typical published ratios for UI text (zh about one third of English, ja and ko somewhat more), not measured on this content, because no CJK text exists in the repo. Re-measure once the first draft of any CJK language exists; a 15% error in f moves the biggest boards by about 0.1 MB, which does not change which boards are over.
5. Result per board is in the table. The 8 over-limit boards are over in the low estimate too (X14 low = 1,825,695).

### Fonts

- CLAUDE.md: CJK fonts Noto Sans/Serif CJK (OFL) as subsets.
- Current boards: nothing embedded. `grep` finds no `@font-face` and no `data:font` in any of the 59 boards. All 59 have `<link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri...&family=Hind...&family=Noto+Naskh+Arabic...&family=Noto+Nastaliq+Urdu...">` in `<helmet>` (6 boards use weights 400/600/700 only for the Arabic and Urdu fonts); a few add Baloo Da 2 / Baloo 2 / Baloo Bhaijaan 2 (PlayBoom). Latin text uses Hind. No CJK font is referenced.
- The Netlify build (`netlify-build/build.py`) strips the Google links and copies self-hosted Fontsource files (`FONTSRC` map, `fonts/fonts.css`). So fonts are outside the board files and add 0 bytes to the 1.8 MB limit; CJK fonts must be added the same way (per-language `@font-face` with `unicode-range`) and need entries in `FONTSRC` plus a font folder `netlify-build/ff/` (which is missing in this repo).
- Google Fonts serves Noto Sans SC/JP/KR as many unicode-range slices, so the existing `<link>` approach would work for the live viewer by adding `family=Noto+Sans+SC:wght@400;600;700` etc.; for self-hosting the slices are needed.
- Subset cost, measured here: I subset the system Noto Sans CJK (2023, OTF/CFF) with fontTools (hinting dropped, Basic Latin included) and compressed with brotli q11, which approximates WOFF2 for CFF fonts (no brotli module for a real WOFF2 write was available offline, so this is an approximation, within a few percent):

| language | characters in subset | Regular | Bold |
|---|---|---:|---:|
| zh (SC) | 800 most basic GB2312 | 264 KB | 267 KB |
| zh (SC) | 1,500 | 447 KB | 456 KB |
| zh (SC) | 3,755 (all GB2312 level 1) | 1,040 KB | 1,066 KB |
| ja | 800 (JIS kanji start + kana) | 310 KB | 315 KB |
| ja | 1,500 | 544 KB | 555 KB |
| ja | 4,565 (JIS level 1+2 start + kana) | 1,536 KB | 1,575 KB |
| ko | 800 Hangul syllables | 77 KB | 78 KB |
| ko | 1,500 | 117 KB | 119 KB |
| ko | 2,350 (KS X 1001) | 167 KB | 173 KB |

  The 800/1,500 sets are the first characters in code-point order of each standard, not a frequency list, so real sets chosen from the actual text will compress differently. Rough planning number: one weight, text-derived subset of about 1,200 distinct characters per language: zh 0.4 MB, ja 0.5 MB, ko 0.1 MB (Regular); with a Bold weight about double. UI text of this size normally uses 1,200-2,000 distinct hanzi/kanji, so budget **about 1.0-1.4 MB of font files per CJK site for Regular+Bold of zh+ja+ko together if generated from the real text**, versus 4.2 MB for full common-character sets. German needs only Latin glyphs Hind already has. Embedding as base64 would add about 33% and push every board over the limit: do not embed, use files with `unicode-range`.

## 3. Split plan (boards over 1,800,000 B at 10 languages)

Splitting rule used: each split board keeps the shared parts (CSS in `<helmet>`, sidebar, header, language/state logic = the script that is not text) and the text of only its own sections; sections are cut at the existing `sc-if` page/tab blocks and `fix*` HTML comment markers. Sizes are estimates (mid-high) assuming the shared part is duplicated: shared template + CSS counted fully, shared script logic about 10% of the non-text script, text of a section follows the section. Section sizes are template bytes measured from the files.

| board | est. 10-lang bytes | new boards (est. bytes mid-high) | what moves where |
|---|---:|---|---|
| X07-Prototype-Test | 2,396,136 | 549-597 k; 688-718 k; 1,427-1,461 k | 1. X07 stays: pick, MCQ, OMR, result, review, event, T/F, fill, match, short, written, mixed pages (549-597 k). 2. X07b-Prototype-Test-ExamAid: all `eaIs*` pages (record, apply, category, speaking, code, cert, employer) plus `exText` 211 KB (688-718 k). 3. X07c-Prototype-Test-Hub: merit, battle, papers, all-exams, axd, exam-day, hub pages plus `hubText` 662 KB (1,427-1,461 k). X07c is the biggest; if it grows beyond 1.6 MB split `hubText` by hub tab. |
| X10-Prototype-Admin | 2,471,381 | 1,272-1,323 k; 1,478-1,537 k | 1. X10 stays: Overview, Guardians, Schedule, Helpline, Institutions, Progress, Usage (1,272-1,323 k). 2. X10b-Prototype-Admin-Accounts: Accounts (incl. HR/Loan/Invoice tabs, 69 KB) and Roles (1,478-1,537 k). Both keep the same admin sidebar (hash below) with the nav link to X10b added in every board of that group. |
| X12-Prototype-Institute | 2,507,245 | 1,212-1,261 k; 1,561-1,624 k | 1. X12 stays: Overview, People, Classes, Study, Assess, Paper, Integrity, Proctoring, Review, Certificates, CPP, Notices (1,212-1,261 k). 2. X12b-Prototype-Institute-Ops: Staff, Billing, Special, Org, Mentor, Reports (incl. manifest), Notifications, Messages (1,561-1,624 k). |
| X14-Prototype-Ops | 1,878,857 | 842-874 k; 1,254-1,303 k | 1. X14 stays: Models, Spend, Escalation, Cost, Flags, Backup, Approvals, Incidents (842-874 k). 2. X14b-Prototype-Ops-Infra: GPU/servers (74 KB template) and Maintenance (49 KB) (1,254-1,303 k). Text methods `uiText` 256 KB, `uiFix8`, `uiSw17`, etc. must be divided along the same sections. |
| X16-Prototype-Quality | 2,372,358 | 759-797 k; 974-1,014 k; 1,081-1,116 k | 1. X16 stays: cache, wrong-answer, gate, teacher QA, circles, translations, glossary, F11 weak/BDSL/KPI-detail, any-check, approvals (759-797 k). 2. X16b-Prototype-Quality-Money: Mf, discounts, gifts, referrals, pay, VAT, KPI, teacher-management `tm.*` with `uiTm` 114 KB (974-1,014 k). 3. X16c-Prototype-Quality-ExamAid: `xa.*` sections with `uiXa` 251 KB (1,081-1,116 k). A 2-board split (X16 + X16b incl. xa) would be about 1.2-1.3 MB each and is also acceptable. |
| X20-Prototype-Landing | 2,550,489 | 1,023-1,064 k; 1,002-1,042 k; 1,320-1,374 k | 1. X20 stays: Home hero, paths, how, fit, courses, English, SSC/HSC, crash, hub (1,023-1,064 k). 2. X20b-Prototype-Landing-Plans: plans (14 KB), proof, safety, PlayBoom, MindForge, Hall, Institutions (1,002-1,042 k). 3. X20c-Prototype-Landing-More: notes, roadmap, FAQ, start, sub pages and blog (40 KB), join, fix18/21 blocks (1,320-1,374 k). X20 has 146 KB CSS in `<helmet>` that is duplicated in each, which is why a 2-way split is not enough (home board would be about 1.80-1.88 MB). Landing is a public page: keep page URLs/anchors working through links between the three boards. |
| X25-Prototype-AdminPlans | 2,486,399 | 830-864 k; 1,133-1,179 k; 1,076-1,120 k | 1. X25 stays: Matrix tab `tMx` (830-864 k). 2. X25b-Prototype-AdminPlans-Platform: `tPlat` tab (90 KB template) (1,133-1,179 k). 3. X25c-Prototype-AdminPlans-Pp: `tPp` tab (84 KB) (1,076-1,120 k). Alternative 2-way split: tMx+tPp together about 1.4-1.5 MB, tPlat alone about 1.15 MB. |
| X26-Prototype-AdminRules | 2,281,638 | 1,238-1,284 k; 1,272-1,319 k | 1. X26 stays: fix17 rules (72 KB), fix18g Study Hall quest, fix18b weak network, fix18f image compression, fix18 Free Beta safety (1,238-1,284 k). 2. X26b-Prototype-AdminRules-More: fix18h engagement, fix18i more ways to learn, fix18k strategic items, fix18l trust and access, fix18m smart suggestion, fix20 load test / voice cache (1,272-1,319 k). `tRules` and `tBeta` tabs live inside one `isPlans` block; split at the comment markers. |

Other boards: X24-Legal (est. 1.64-1.79 MB) is under the limit but has no margin; 86% of the file is the 19 legal pages x 6 languages (987 KB of 1,143 KB; the whole script is 95%) (privacy 202 KB, terms 128 KB, refund 62 KB ... in bn/en/hi/ur/ar/fr combined). Suggest pre-emptive split X24 (privacy, terms, refund, deletion, cookies, access) + X24b (13 other pages) of about 0.9 MB each. X19 (est. 1.47-1.56 MB) and X27 (1.26-1.35 MB), X15 (1.05-1.12 MB) fit. W00 (0.90-0.99 MB) fits.

Consequences of splitting: new entries in `canvas.json` and W00 index/preview; sidebar and cross-board links in X13-X22 and X10 groups; the two sidebar groups below have to stay in sync; dcverify must be run on each new board. Each over-limit board also needs the `LANGS` constant and `langNames()` extended.

## 4. Sidebar identity

The admin sidebar is the `<aside>...</aside>` element. I extracted it from each board with a regex and hashed (SHA-256, first 12 hex shown).

| group | boards | aside bytes | SHA-256 (12) | result |
|---|---|---:|---|---|
| X10 group | X10, X25, X26, X27 | 10,962 each | b7655db1dced (all four) | **byte-identical** |
| X13-X22 group | X13 | 6,964 | fe0cbee5a6c7 | differs |
| | X14 | 6,682 | c29bb0326a08 | differs |
| | X15 | 6,679 | 3236a452dc3e | differs |
| | X16 | 6,678 | 1590a7e23872 | differs |
| | X17 | 6,678 | 20acf9601ada | differs |
| | X19 | 6,679 | 2f58e6097954 | differs |
| | X21 | 6,678 | 94bf4ea13fee | differs |
| | X22 | 6,681 | 7c4113e80d72 | differs |

Boards in the X13-X22 range with no admin sidebar of this kind: X18 (MindForge), X20 (Landing: two other asides, 442 and 5,706 B, not admin), X23, X24, X11 (no `<aside>`); X12 has a different small aside (2,569 B, no admin brand block). Also: X10 group uses the `x10-menu` id; X13-X22 use `sbm-nav` and the `ng-*` classes.

Why the X13-X22 hashes differ (diffed line by line):
- X15, X16, X17, X19, X21: the same markup; the only difference is which link carries the active-page marker (`class="ng-it on" aria-current="page"` plus the `ng-row` wrapper and the submenu toggle button), i.e. the sidebar differs by 2 lines per board. This is by design and cannot be byte-identical while the current page is marked inside the aside.
- X14 and X22 also use different i18n keys in the labels (`t.nav.admin`, `t.nav.ops`, `t.nav.acc`, `t.nav.qual`, `t.nav.grow`, `t.nav.mh` instead of `t.nav.x10`, `t.nav.x14`, ...): 6-7 lines differ from the X15-X21 version beyond the active marker.
- X13 uses a third key set (`t.navx.*`), a literal label "Landing Page AI" and a different grouping of the submenu: 9 lines differ.
So the rule "X13-X22 share byte-identical sidebar" is not true today in the strict sense: two real variants of label keys (`nav.xNN`, `nav.name`, `navx.xNN`) plus the active marker. If the owner means "same links in the same order", all 8 have the same 8 links (X10, X14, X15, X16, X17, X19, X21, X22; X13 adds itself) and that part is consistent. Decision needed before adding boards: either accept "identical except active marker" and unify the label keys, or move the sidebar out of each board. Moving it out is the only way to keep it identical when X10b/X12b/X14b etc. are added.

## 5. Fonts: see section 2 (sub-section Fonts)

## 6. Old paths in `prototype/tools/` and `prototype/netlify-build/`

No path of the form `SP/...` appears as code; the old workspace is referenced as a literal absolute scratchpad path, as a command-line argument expected to be the old `SP` folder, or in comments. Found and checked for existence:

| file:line | reference | exists here? |
|---|---|---|
| netlify-build/build.py:3 | docstring "Reads SP/ntd/project ... writes SP/s2/netlify/nexatute-mockups" | comment only, but describes the old layout |
| netlify-build/build.py:6 | `SP = '/tmp/claude-0/-home-claude/9878cfdb-4647-5257-a0fe-47a0a28067df/scratchpad'` (old session scratchpad) | NO (folder missing) |
| netlify-build/build.py:7 | `PROJ = SP/ntd/project` (should be `prototype/project`) | NO |
| netlify-build/build.py:11 | `SHOTS = SP/s2/fix14/thumbs/shots` (thumbnails; repo has `prototype/thumbs`) | NO |
| netlify-build/build.py:12 | `FF = HERE/ff/fonts/google` (Fontsource files) | NO (`netlify-build/ff` missing) |
| netlify-build/build.py:142-146 | `HERE/preact-src/package.json`, `preact-src/LICENSE` | NO (`netlify-build/preact-src` missing) |
| netlify-build/build.py:10,188 | OUT/NET: `NET = dirname(HERE)` = `prototype/` (output folder `nexatute-mockups` would be created inside the repo) | path logic changed vs. original (`SP/s2/netlify`) |
| netlify-build/checks.py:7-14 | `SP` as above; `NET = SP/s2/netlify`, `PROJ = SP/ntd/project`, `MAN = NET/build/manifest.json` | NO |
| netlify-build/checks.py:82 | `SP/dcrender.js` | NO (repo has `prototype/tools/dcrender.js`) |
| netlify-build/dbg.py:2 | `sys.path.insert(0, ".../scratchpad/s2/netlify/build")` | NO |
| netlify-build/dbg3.py:3 | `O = ".../scratchpad/s2/netlify/checks/"` | NO |
| netlify-build/shots.py:4 | `OUT = ".../scratchpad/s2/netlify/checks/page_"` | NO |
| netlify-build/smoke.py:21 | screenshot path `.../scratchpad/s2/netlify/checks/smoke_` | NO |
| netlify-build/build-preact.js:1 | `require("/opt/npm-tools/node_modules/esbuild")` | yes on this machine (`/opt/npm-tools/node_modules/esbuild` exists) but machine-specific; also reads `mangle-cache.json` and `preact-src/` | NO for the two files (not in repo) |
| tools/apply_shot.py:3-5 | `SP = sys.argv[1]`; `SP/ntd/project/W00-Website-Preview.dc.html`, `SP/s2/fix14/thumbs/rep.json`, `.../urls.json` (repo has `tools/urls.json`) | depends on argument; layout `ntd/`, `s2/` does not exist |
| tools/shoot14.py:5-9 | `SP = sys.argv[1]`; `PROJ = SP/ntd/project`, `OUT = SP/s2/fix14/thumbs/shots`, `REND = .../render`, `RJ = SP/s2/site/tools/dcrender_props.js` | layout does not exist (repo: `prototype/project`, `prototype/tools/dcrender_props.js`, `prototype/thumbs`) |
| netlify-build/*.py (checks, links, tabchk, hdrchk, sweep, shots, smoke, fontchk) | `http://127.0.0.1:8765/nexatute-mockups/...` | expects a local server rooted at the built site; not a file path, but needs the build output first |

Also found: `project/support.js`, which every board loads (`<script src="./support.js">`), is not in `prototype/project/` (MISSING; probably provided by the Design viewer). `netlify-build/src/*` exists. `tools/dcverify.py` has no old paths (uses its own folder and the board path).

## Findings that matter for the next step

1. Eight boards must be split before the four languages are added. Headroom today: X20 4,124 B, X25 24,422 B, X12 32,111 B, X10 35,724 B: none of them can take even one new language (one language adds about 2.3-3.3 MB across all boards, 50-130 KB to each of these).
2. Estimated growth across the 59 boards (mid): de +2.7 MB, zh +2.3 MB, ja +3.0 MB, ko +3.3 MB = +11.3 MB (range +10.1 to +12.9 MB), from 28.6 MB to about 39.8 MB. The six language blocks are about 71% of all bytes, so splitting only keeps each file under the limit (the shared CSS/sidebar are duplicated, adding roughly 1.5-2 MB in total); with the splits proposed here the board count goes from 59 to 59 + 12 = 71 (X07 +2, X10 +1, X12 +1, X14 +1, X16 +2, X20 +2, X25 +2, X26 +1).
3. dcverify checks parity only for `uiText()`; side methods (`hubText`, `exText`, `uiXa`, ...) are about half the text in X07, X14, X16 and are not checked, so 4 new languages could be missing keys there without a failure. Extending the verifier to check them is advisable.
4. The English fallback hides missing keys; ja/de/zh/ko should be added with the parity check as a gate.
5. Sidebar rule for X13-X22 is not literally satisfied today (see section 4).

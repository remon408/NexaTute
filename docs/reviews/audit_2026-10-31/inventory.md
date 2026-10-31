# NexaTute prototype: inventory of pending work (audit 31 Oct 2026, read-only)

Repo: `/home/claude/nexatute`. Boards: **59** `prototype/project/*.dc.html` files (not 60). Evidence comes from case-insensitive fixed-string `grep -o` counts per board, shown as `BOARD:count`. Text is English unless the note says otherwise. "no hit" means 0 matches in all 59 boards.

**Rule used:** an item is DONE only when a grep hit shows it. PARTIAL means some part exists, and the row says what is missing. MISSING means nothing relevant was found, or only an outdated or contradicting version exists.

### Board size headroom (limit 1,800,000 bytes, `wc -c`)
| Board | Bytes | Free | Note |
|---|---|---|---|
| X20 Landing | 1,795,876 | **~4 KB** | Full. Split first (HANDOVER: move Nexa Notes to a new board) before any landing highlight |
| X25 AdminPlans | 1,775,578 | ~24 KB | Nearly full. New price rows need a new admin board |
| X12 Institute | 1,767,889 | ~32 KB | Nearly full. Competition hosting, homework and extra-time views need a new board |
| X10 Admin | 1,764,276 | ~35 KB | Nearly full |
| X16 Quality | 1,707,709 | ~92 KB | |
| X26 AdminRules | 1,699,549 | ~100 KB | |
| X07 Test | 1,667,860 | ~132 KB | |
| X14 Ops | 1,360,158 | ~439 KB | |
| X24 Legal | 1,143,125 | ~656 KB | |
| X19 MarketingHub | 1,105,885 | ~694 KB | |
| X08 Guardian | 1,005,124 | ~794 KB | |
| Others (X01, X02, X06, X18, X27, X17, X13, X15, X22, X23, X03, G01, W00, D01, L*, Main) | < 0.95 MB | > 850 KB | |

**Cross-cutting warning:** the boards still hold **6 languages only**. In X20 `"bn":`/`"en":`/`"hi":`/`"ur":`/`"ar":`/`"fr":` each occur 12 times and `"ja":`, `"de":`, `"zh":`, `"ko":` occur 0 times. No board loads a Noto CJK font. Adding 4 languages roughly grows every board by 60%+, so the near-full boards (X20, X25, X12, X10, X16, X26, X07) must be split **before** any other addition.

---

## A. Learning (core NexaTute)

| # | Item | Source (file + date) | Status | Evidence | Boards to touch | Notes / open questions |
|---|---|---|---|---|---|---|
| A1 | Project & Competition Studio: learner area (Virtual Lab → report, slides, poster, video → AI judge → final video ≤5 min → competition + QR certificate) | decisions.md L118, L120 (30 Oct); tasks/project-studio-package.md §1, §4; HANDOVER step 6 | MISSING | no hit for "Project Studio", "Project & Competition", "AI judge", "lab report". Virtual Lab exists (L10:4, X07:24, X20:12, X25:6) | New learner board (X07 has 132 KB, not enough); Main; D01 | Reuse the X07 Virtual Lab. Counter "N of M works left this month" |
| A2 | Project Studio Pro ৳799 ($12) and Team ৳3,999 ($60, 15 members, 21 works pool) packages | decisions.md L121–122 (30 Oct); task §2, §5 | MISSING | no hit for "৳799", "৳3,999" | Plan cards (X03, X20), admin price table (X25 full, so a new board), numbers.md | Margin re-check after the GPU benchmark |
| A3 | Per-plan Project Studio limits (Batch 1/1 min, Combo 2/2, Personal 3/3, Pro 7/5 min; free tier, Daily Pass, PlayBoom: lab + basic report only) | decisions.md L120; task §3 | MISSING | no hit for "Project Studio" | Admin plan table (X25 or a new board), X03 | "highest limit counts, Pro adds 7" rule |
| A4 | "My Projects" storage folder + meter (Pro +5 GB, Team 30 GB, drafts deleted after 30 days) | decisions.md L123; task §6 | MISSING | no hit for "My Projects" | Learner Project Studio board; storage admin (X14/X10) | |
| A5 | Project Room, Team Lobby, task board, voice huddle, AI "Nexa Project Coordinator" | decisions.md L124; task §7 | MISSING | no hit for "Project Room", "Project Coordinator" | New learner board; Nexa Guard admin | Under-18: no private messages, mentor sees all |
| A6 | Project Studio personal KPIs + AI advice; "Projects" section on the Main Student Dashboard; guardian weekly summary | decisions.md L125–126; task §8 | MISSING | "Projects" appears only incidentally (Main:1, X18:4, X08:4); no Project Studio KPI | Main, D01, X18, X08, G01 | No ranking; "needs more practice", never "weak" |
| A7 | Shared learner record sync (Tutor, Co-Tutor, Coordinator) | decisions.md L125; school-homework.md "Sync" | PARTIAL | X18:1 "One shared learner record — every teacher adds to it" | X18, X02, L07 | Coordinator and Homework inputs are missing |
| A8 | Class extra-time rule (≤10 min, taken back from the next 2 classes at ≤5 min each, 1:1 borrows next-day minutes, never after 9 pm for under-18, Bujhlam/Bujhini meter decides) + pop-up to students, guardians and teachers | decisions.md L128 (30 Oct); HANDOVER step 8 | MISSING | the "extra time" hits are only exam-accommodation text (X07:3, X08:1, X16:1, X24:2, X25:1); no hit for "becomes shorter". The Bujhini meter exists (X02:13, X04:7, X07:7) | X02 (1:1), X06 (batch), X08 guardian, X12 Institute (full), admin settings (X10/X26), D02 frame | X12 and X10 are near full |
| A9 | Content quality flow: "Report a mistake" for students, parents and teachers → AI re-check → human if unsure → fixed everywhere → reporter told; plus a 2–5% random human sample | decisions.md L187, L189 (31 Oct) | PARTIAL | "Report a wrong answer" (X02, L07, X11), and X02 says "A subject expert checks it…fixed for everyone". X16 has "AI verifier" (13) and "human sample" (7), but only for MindForge and speaking scoring. No hit for "Report a mistake" in learner boards (only X19:1, a marketing label) or for "2–5%" | X02, L07, X11, X08 (parent), X09/X12 (teacher), X16 (admin queue + sample % setting) | The AI-first re-check, the reporter notice, parent/teacher entry points and a global 2–5% default are all missing |
| A10 | Trust page per course/content (sources and licences, AI models and verification level, consent and recording, wrong-answer reports and fixes) | decisions.md L89–90 (30 Oct); memory nexatute-admin.md L72–73 | MISSING | no hit for "trust page", "Sources and licences", "verification level" | Learner course page (X01/X07), X20, admin (X16) | |
| A11 | HSK Chinese course Batch ৳2,100 / Combo ৳2,800 / Personal ৳3,500 ($31/$42/$52) | decisions.md L165 (30 Oct) | MISSING | no hit for "HSK" or "৳2,800". "Chinese" appears only in the X20 language list ("Japanese · Korean · German · Arabic · Chinese · French") | X20 courses (full), X25/numbers.md, X03 | |
| A12 | Exam & Admission Hub: Chinese scholarship (CSC) and university admission guide | decisions.md L165 | MISSING | the only "CSC" hit (W00) is inside SVG path data | X07 hub / X20 hub section; hub.md | Verified facts only |
| A13 | Free 45-min Motion Studio course inside NexaTute + cross-course suggestions + 50% off the first course for Motion Studio clients | decisions.md L98–101, L178 (30 Oct) | MISSING | no hit for "Free course", "Making videos with AI", "50% off" | X01/X05 course catalogue, X20, X25 (discount exception) | The 50% is the owner's explicit exception to the 30% fee cap |
| A14 | "Try it in Motion Studio / NexaLogicDev" buttons in NexaTute skill courses; "Coming soon — notify me"; free 45-min NexaLogicDev class | tasks/free-class-links.md (30 Oct) | MISSING | no hit for "Try it in Motion Studio", "Learn to do this", "Free class" | Skill course boards (X05/X01), admin mapping table | The NexaTute side of a cross-product link |
| A15 | AI Tutor Creator (adults create their own AI tutor under twin/clone rules); central logout/device/session dashboard | tasks/ecosystem-architecture-review.md (30 Oct) | PARTIAL | no hit for "AI Tutor Creator". "Sign out of all devices" exists (D01, X08:4, X18:2, X15:1) | X23 (Avatar & Voice user), X22, account boards | |
| A16 | Minimum age for under-18 profiles outside the USA follows the learner's enrolled class/grade | decisions.md L182 (30 Oct) | MISSING | no hit for "class/grade", "enrolled class", "minimum age" | Onboarding (L01/X01), X24 legal, admin age rules (X26) | |

## B. Nexa Speak / Nexa Scripts

| # | Item | Source | Status | Evidence | Boards to touch | Notes |
|---|---|---|---|---|---|---|
| B1 | "Nexa Speak" menu item in NexaTute | decisions.md L162 (30 Oct); HANDOVER step 15 | MISSING | no hit for "Nexa Speak" or "নেক্সা স্পিক" | All learner boards with a menu (X01, X02, X18, D01, Main) | |
| B2 | Nexa Speak learner module: modes (Daily Conversation, Job Interview, IELTS Speaking, Business, Travel, Free, Pronunciation, Grammar, Shadowing), role-plays, CEFR placement, end-of-session report (fluency, pronunciation, grammar, vocabulary, "speaking flow"), open mic + push-to-talk, low-internet mode | decisions.md L161–163 | MISSING | no Speak module. Related pieces exist: an "IELTS Speaking" debate practice (X11:6), a speaking appeals queue (X16 "IELTS Speaking practice · Part 2") and CEFR on certificates (L09:10) | New learner board(s) | Never reads emotion or confidence (EU AI Act) |
| B3 | Nexa Speak Pass ৳699/month ($10), 45 min/day shared across 10 languages; what counts and what doesn't; phone practice 60 min/month; no rollover | decisions.md L162, L185 (31 Oct, replaces 30 min) | MISSING | no hit for "৳699" | Plan cards (X03, X20), price admin (X25 full), numbers.md | |
| B4 | Language-specific modes: IELTS/TOEFL/PTE, DELF/TCF, MSA + Gulf/Egyptian, JLPT, Goethe/TestDaF, HSK/HSKK, TOPIK/EPS-TOPIK | decisions.md L163–165 | MISSING | no hit for "Goethe", "TestDaF", "HSK". JLPT/TOPIK/EPS-TOPIK exist only as courses (X20, X25), not as Speak modes | Speak board | Each language goes live only after native review |
| B5 | International-standard Speak additions: phoneme/IPA feedback, A1→C1 path, listening, full exam mocks, job-specific language, validated level test, Nexa Speak Certificate (QR, Open Badges, LinkedIn), 18+ peer practice, stammering-friendly mode, offline practice, corporate packages, quarterly learning-gain results | decisions.md L169 (30 Oct) | MISSING | no hit for "phrasebook", "stammer", "peer practice", "Nexa Speak Certificate". "Open Badges" exists in admin (X10, X15, X18…) for other certificates | Speak board(s), X12 (corporate), X20 | |
| B6 | Weekly human re-rating of a random sample of AI speaking scores | decisions.md L169, L194(6) | PARTIAL | X16 "Weekly human sample" (sp_sm) for speaking scores | X16 | Needs extending to Nexa Speak |
| B7 | 18+ opt-in saving of own speaking recordings, auto-deleted after 30 days (under-18 never stored) | decisions.md L170 (30 Oct) | MISSING | no hit for "save my recording" or "auto-deleted after 30" | Speak board, X24 privacy text | Exception to the "learner voice never stored" rule |
| B8 | Human Conversation Club add-on ৳199/month (Saturday 8 pm, 45 min, 25 per group, teen groups) | decisions.md L170–171 (৳199 replaces ৳99) | MISSING | no hit for "Conversation Club". The "৳199" hits are MindForge Pro | Speak board, plan cards, X25 | |
| B9 | Admin "Teachers" page for club teachers (hiring/verification, Saturday slots, attendance, ratings, pay ৳600/session, standby pool, supervisor 1:20) with every value editable | decisions.md L172, L174 | MISSING | no hit for "Teachers page" or "Conversation Club" | New admin board (shared sidebar; X10/X25 full) | The admin sidebar must stay byte-identical |
| B10 | Ten 31 Oct additions: visa/embassy and job interview simulations, CV/job-ad interviews (STAR), "say it in Bangla" coaching, workplace culture (keigo, honorifics, Gulf), offline emergency phrasebook, WhatsApp voice-note practice, IVR phone-call practice, Kids Nexa Speak (6–12), Family Plan ৳1,999 (4 members), monthly then-vs-now video + Speaking Challenge | decisions.md L185 (31 Oct) | MISSING | no hit for "Family Plan", "Kids Nexa", "phrasebook", "then vs now", "Speaking Challenge", "৳1,999". The IVR phone tutor exists for other learning (G01, X01, X08…) | Speak boards, X08 guardian (Kids), plan cards | No visa promise; no cash for children |
| B11 | 3 stages × 120 days (A1→A2, B1, B2→C1), "day X of 120", stage level tests, continue 30/60 days, placement may start higher, no level guarantee | decisions.md L193 (31 Oct) | MISSING | no hit for "Nexa Speak" | Speak board, app board | |
| B12 | Student "My roadmap" dashboard (stage path, minutes left of 45, streak, skill KPIs with then-vs-now graphs, top 3 mistakes, CEFR "I can now", Scripts progress, mocks, certificates) | decisions.md L194(1) | MISSING | no hit | Main/D01/X18 + Speak app | Uses the kpi.md engine |
| B13 | Parent Nexa Speak dashboard (Bangla, weekly report, WhatsApp/SMS optional, consent by age) | decisions.md L194(2) | MISSING | no hit | X08, G01 | |
| B14 | Teacher Nexa Speak dashboard (club, institution and recruiting-agency trainers: at-risk, test-ready, common mistakes) | decisions.md L194(3) | MISSING | no hit | X09/X12/T01 | Masked IDs |
| B15 | Admin controls for Speak KPIs, alert rules and report frequency | decisions.md L194(5) | MISSING | no hit | New admin board | |
| B16 | Nexa Scripts (formerly Script Starter): ৳199/month, 30-day course per script (Hangul, Hiragana/Katakana + 50 Kanji, Pinyin + 50 characters, Arabic, Devanagari, Nastaliq, phonics, Bangla), tracing with AI stroke check, FSRS, voice-first mode, auto-start from the placement test, "Script Ready" certificate | decisions.md L166, L192–193 (31 Oct) | MISSING | no hit for "Nexa Scripts", "Script Starter", "Script Ready", "Hangul", "Hiragana", "Pinyin" | New learner board(s) + app board | Included free in language-course plans and the Speak Pass |
| B17 | Standalone "Nexa Speak" mobile app (phone + tablet; Nexa Speak Pass + Nexa Scripts), store prices +30%, parental gate, listings in 10 languages; admin settings/versions/store prices in the NexaTute admin | tasks/nexa-speak-app.md; decisions.md L191–192 (31 Oct) | MISSING | no hit for "Nexa Speak" | New mobile/tablet board(s) (390/834/1024 only); admin board | The +30% store pattern already exists (see G9) |
| B18 | Share for everything in Speak/Scripts (then-vs-now video, stage certificates, Script Ready, Speak certificate, badges, streaks, challenge results, mock results by choice) | decisions.md L195 (31 Oct) | MISSING | no Speak items exist | Speak boards | Under-18: certificate only |

## C. Institutions / School Homework

| # | Item | Source | Status | Evidence | Boards to touch | Notes |
|---|---|---|---|---|---|---|
| C1 | "School Homework" section on the student dashboard (photo/typed input, Qwen3-VL fills subject/topic/due date, hints only, AI checks, Error Notebook, "Beyond NexaTute syllabus" tag + AI lesson, KPIs + AI advice) | decisions.md L127 (30 Oct); tasks/school-homework.md; HANDOVER step 7 | MISSING | no hit for "School Homework", "Beyond NexaTute syllabus", "Homework help". The existing "Homework" hits are teacher-assigned work (X12:18, X06:14) and the guardian "homework list" upload (X08:8) | X18/D01 (Main dashboard), Main | Reuse the X08 upload flow and X02 Error Notebook |
| C2 | Daily homework-help limits Free 1 / Daily Pass 3 / Batch 5 / Combo 10 / Personal unlimited | school-homework.md | MISSING | no hit | Admin plan table (new board) | No extra charge |
| C3 | Guardian homework weekly summary + topic list + KPIs | school-homework.md | PARTIAL | X08 has "School diary or homework list — Adds the homework to Tanvir's plan" (upload only) | X08, G01 | Summary/KPIs missing |
| C4 | School teacher class summary (individual only with guardian consent); partner-school teacher assigns homework from X12 into the section | school-homework.md | PARTIAL | X12 "Give homework or a test" (as_h, kinds hw/ct/mt) | X12 (full → new board) | Link to the student's section and the consent gate are missing |
| C5 | Institution counts-only homework view (hidden under 5) | school-homework.md | MISSING | no hit | X12 / new board | |
| C6 | Competition hosting for institutions (topic, rules, deadlines, rubric, online judging, results, QR certificates, pooled storage) | decisions.md L118; project-studio-package.md §4 | MISSING | "competition" hits only in X04:2 and X18:1 ("no competition"); X12 has a "Science fair 2027" group seed only | X12 is full, so a new institute board | |
| C7 | Project Studio Team join by invitation within the same institution/class; adult mentor required | task §5 | MISSING | no hit | X12/new board, Project Studio board | |
| C8 | Extra-time view on the institute side | decisions.md L128 | MISSING | see A8 | X12 / new board | |
| C9 | Recruiting-agency worker-readiness view (worker consent; counts only, cells < 20 hidden) | decisions.md L194(4); cross-product-audit 31 Oct | MISSING | "recruiting agenc" appears only in disclaimers (X10:1, X12:2) | X12 / new B2B board | |
| C10 | Corporate language packages (BPO, call centres, exporters, agencies) at institution discounts | decisions.md L169; language-marketing.md | MISSING | "BPO" hits are existing course text (X20:25, X04:15), not language packages | X12, X20 | |
| C11 | Institute may use a teacher's face/voice only with that teacher's live consent + OTP; withdrawn automatically when the teacher leaves | ecosystem-architecture-review.md correction 3 | MISSING | no hit for "teacher leaves", "left the institution" | X22/X23, X12 | Check the X22 consent flows in detail |

## D. Admin (platform)

| # | Item | Source | Status | Evidence | Boards to touch | Notes |
|---|---|---|---|---|---|---|
| D1 | Futuristic admin: Co-Admin command bar (Ctrl+K, text/voice), daily morning briefing, anomaly alerts with reasons, "what-if" price simulator with uncertainty, one-click fixes, dark mode default with glass panels | decisions.md L97 (30 Oct); memory nexatute-admin.md L74 | PARTIAL | Co-Admin exists (X27:142 + 14 on every admin board). No hit for "Ctrl+K", "briefing", "anomaly", "price simulator", "dark mode". The "what-if" hits are the learner exam-readiness simulator | X27 + admin header on all admin boards | Header changes must keep the sidebar byte-identical |
| D2 | "Why?" on any number; forecasts | decisions.md L97 | PARTIAL | "Why:" lines widespread (X16:277, X25:121…); "forecast" in X14:25 | Admin boards | Needs a generic "why?" affordance |
| D3 | Protected-settings rule: 3 approvals (founder + security/compliance owner + 1), law reference, 24-h delay with cancel, urgent option, separate log, rollback; Co-Admin proposes only | decisions.md L107–108 (30 Oct) | MISSING | no hit for "protected setting", "compliance owner", "24-hour delay" | X26 AdminRules, X27 | |
| D4 | "People, teams & job assignment" page (queues, approvals, disputes, legal requests, shifts) | decisions.md L115 (30 Oct); reviews/gap_solutions | MISSING | no hit for "People, teams", "job assignment" | New admin board | Design is in gap_solutions_2026-10-30.md |
| D5 | Per-purpose customer email addresses set in admin, routed to teams | decisions.md L116–117, L175 | PARTIAL | hard-coded addresses in boards: security@nexatute.com ×61, privacy@ ×30, copyright@ ×12, accessibility@ ×6; generic "Enter an email address" fields in X10/X15/X26 | New admin page; X24 must read the addresses from admin | Support phone/email: set in admin (owner, 30 Oct) |
| D6 | Discount stacking: rule discounts always; one promo (largest); caps 45% per-minute / 30% fee; 30% margin floor; caps apply on top of institution 30/40% contract prices (to confirm); 50% first-course exception | decisions.md L113, L177–178 | MISSING | no hit for "one promotional" or "discount cap"; the "45%" hits are CSS widths | X25 (full) or a new pricing-rules board | |
| D7 | Exchange-rate policy: Taka × 0.015 compared with the market every 3 months, changed with two-person approval, books at the actual daily rate | decisions.md L90 | PARTIAL | X25 has an editable USD row (`"k": "rate" … 0.015`, a lock on rounding) | X25 | The 3-month market check and actual-rate booking are missing |
| D8 | Accounting: product tag + funding tag, OpenCost allocation, common-platform pool, margin alerts | decisions.md L39–44 (29 Oct) | PARTIAL | "Funding A" X10:19, X25:6. No hit for "OpenCost", "common platform", "product tag" | X10 accounting / X25 | |
| D9 | GPU fleet panel: LeaderGPU Netherlands, 4 × 8×A6000 + 1 × 8×A100, priority NexaTute → NexaLogicDev → Motion Studio, lend rules, admission caps, upgrade rule | decisions.md L199, L201 (31 Oct) | MISSING (outdated) | no hit for "LeaderGPU", "A6000", "Netherlands". X14 shows "RTX Pro 6000 · 96 GB … US data centre" | X14 (439 KB free), X10 | Contradicts the newest decision |
| D10 | Valkey instead of Redis | decisions.md L201 (31 Oct) | MISSING (outdated) | "Redis" X14:107, D05:6, X10:6, X16:6, W00:6; no hit for "Valkey" | X14, D05, X10, X16, W00, X07, X13 | Licence rule |
| D11 | Cloudflare: cache purge + WAF status visible; security-rule changes need two-person approval | decisions.md L200 (31 Oct) | PARTIAL | "Cloudflare" X14:123; "WAF" X14:2, X26:13; no hit for "cache purge" | X14 | |
| D12 | Internal Video Service controls (on/off, quota, internal price, GPU share, alerts) | decisions.md L132; tasks/internal-video-service.md | MISSING | no hit for "Internal Video" | X14 or a new admin board | Must exist in all 3 admin panels |
| D13 | Landing Page AI suggestion card with full "why": evidence + data window + sample size, expected range + confidence, risks, test plan + stop rule, priority/approver/rollback, sources | decisions.md L158; tasks/landing-page-ai-all.md | PARTIAL | X13 card has Source / Why / Expected effect / risk level ("trig_lbl", "why_lbl", "exp_lbl", "risk") | X13 | Missing: confidence range, data window, sample size, test plan, stop rule, rollback, sources |
| D14 | Share admin controls (item types, templates, brand mark, age rules); share KPIs (counts only) | tasks/sharing-and-connectors.md | MISSING | no hit for "Share template", "shareable" | X19/X17 | |
| D15 | Language-prompt admin (on/off, country→language map, prompt text in 10 languages, counts report) | tasks/language-prompt.md; decisions.md L197–198 | MISSING | no hit for "language prompt", "or in English" | X26 or X13 | |
| D16 | Project Studio, Homework, extra-time, Speak, Club and Scripts numbers editable ("(default)", two-person, logged) | all task files | MISSING | see A2–A8, B3–B16, C2 | New admin board(s) | X10 and X25 are full |
| D17 | Self-service data export + "Delete my account" with a 30-day cancel window, admin deletion queue, DPO oversight | decisions.md L156; tasks/five-gaps-solutions.md §1 | PARTIAL | "Download all my data" (L04:2, X01:2, X08:1, X10…); X24 "Choose 'Delete my account'…". No hit for "cancel window" | L04/X01/X08, X15 | |
| D18 | Status page status.remonlogic.com with per-product components; post-incident report within 5 business days | five-gaps-solutions.md §5 | PARTIAL | X14 has status.nexatute.com (fix18f); "lost minutes" are added back (X02:3, X14:4…). No hit for "status.remonlogic", "post-incident" | X14, X20 footer | |
| D19 | EU data residency at launch (R2 EU, EU DB copy) | decisions.md L156; five-gaps §3 | MISSING | no hit for "data residency", "EU data" | X14, X24 privacy | |
| D20 | "Remon Growth Logic AI" name for the shared growth platform / Marketing Hub | decisions.md L176 (30 Oct) | MISSING | no hit for "Growth Logic" | X19, X17 | |

## E. Landing / marketing (X20, W00, X13, X17, X19)

| # | Item | Source | Status | Evidence | Boards to touch | Notes |
|---|---|---|---|---|---|---|
| E1 | Landing highlight for the Project & Competition Studio (5-step flow, free vs paid, "sample (prototype)") | decisions.md L119 (30 Oct); task §4 | MISSING | no hit for "Project Studio" | X20 (4 KB free, split first), W00 | |
| E2 | Landing highlight for Nexa Speak | decisions.md L161–162; landing-page-ai-all.md | MISSING | no hit for "Nexa Speak" | X20, W00 | |
| E3 | Landing hero for Nexa Scripts: "Learn any language even if you can't read the letters — from ৳199" | decisions.md L166; tasks/language-marketing.md | MISSING | no hit for "can't read the letters" (both apostrophe types) | X20 | |
| E4 | "Why learn with NexaTute" section on the pricing page (9 points) | decisions.md L149 (30 Oct); tasks/why-us-nexatute-motionstudio.md | MISSING | no hit for "Why learn with", "Why choose", "Why NexaTute" | X20 pricing | The draft text uses "Nexa Teacher" and "app in 6 languages", so update it to Nexa Tutor and 10 languages before building |
| E5 | Recruitment-test offer highlight | landing-page-ai-all.md | DONE | X20 "Employee skill tests and recruitment tests…", "Monthly price of the Recruitment tests add-on…" (recruitment X20:15) | — | |
| E6 | One SEO landing page per language/goal (Korea EPS, Japan, Gulf, CSC, Germany, diaspora) via Landing Page AI | language-marketing.md | MISSING | no hit (no Speak/Scripts pages) | X13 (page list), X17 | |
| E7 | Landing pages link the Trust Center and status page | landing-page-ai-all.md | PARTIAL | "status page" X20:3; no hit for "Trust Center/Trust centre" | X20 footer | |
| E8 | Landing in 10 languages with hreflang | decisions.md L164, L202 | MISSING | hreflang exists for 6 languages (X20:17, X17:19); no ja/de/zh/ko keys | X20 (split first), all | |
| E9 | Dates on landing/boards: Free Beta 15 Jan 2027, paid 5 Feb 2027, pilot ~1–14 Jan 2027; Motion Studio Free Beta 30 Jan 2027 | decisions.md L186, L188 (31 Oct) | MISSING (outdated) | boards still show "20 November – 9 December 2026" ("20 Nov" X20:38, X14:16, X01:11, W00:10…; "9 Dec" X20:19…) and paid "1 Jan 2027" (X26:48, X25:12…); X20 shows Motion Studio "beta from 20 Dec 2026" | X20, W00, X01, X13, X14, X25, X26, X27, D05, L02, X16, X18, X08… | A broad date sweep; numbers.md v13 holds the old dates |
| E10 | Motion Studio / NexaLogicDev blogs (Motion Notes, Build Notes) in the shared Marketing Hub | decisions.md L135 | MISSING | no hit for "Motion Notes", "Build Notes" | X19 (NexaTute side only); mainly the MS/NLD prototypes | |

## F. Sharing / language prompt / connectors / cross-product

| # | Item | Source | Status | Evidence | Boards to touch | Notes |
|---|---|---|---|---|---|---|
| F1 | One-tap Share sheet (Facebook, WhatsApp, LinkedIn, Instagram, TikTok, YouTube, X, copy link, download) on EVERY shareable result: certificates, badges, streaks, Most Improved, milestone cards, portfolio, results | CLAUDE.md standing order (31 Oct); decisions.md L131, L196; sharing-and-connectors.md | PARTIAL | L09 certificate: "Add to LinkedIn Profile", "Download PDF", "Share link"; X07 LinkedIn button (18+); X08 "Share on WhatsApp" (weekly report). No Facebook/X/TikTok share in learner boards (L09, X07, X18, X01: Facebook 0). No hit for "Share button" | L09, X07, X18, X01, X02, X08, G01, D01, Main | Badges, streaks, Most Improved, portfolio and results have no share |
| F2 | Verify link (nexatute.com/v/XXXX) + QR + public verify page with a "Start free" button; Open Graph card | sharing-and-connectors.md B | PARTIAL | QR verify on certificates (L09 "QR verify", X07 "QR-verify link"). No hit for "nexatute.com/v/" or "Open Graph" | L09, X07, X20 (verify page) | |
| F3 | Under-18 share rules: guardian approval, first name only, no location, face optional, guardian can switch the link off; no tracking | sharing-and-connectors.md | PARTIAL | L09 "under 18 only PDF and link sharing". No hit for "first name only"; no guardian share approval | L09, X08, G01 | |
| F4 | Report button + 24 h takedown on public share pages | sharing-and-connectors.md | PARTIAL | general takedown flows exist (X15:9, X24:6, X22:10) | Verify page | |
| F5 | Co-branded institution result posts | sharing-and-connectors.md | MISSING | no hit | X12 | |
| F6 | Sign-up/login with Google / Facebook / Apple (OAuth, basic profile) | decisions.md L130–131 | MISSING | X01 has "Continue with email", "Continue with mobile number", "Log in with your Nexa ID". No hit for "Sign up with", "Continue with Google" in learner boards ("Sign in with Google" occurs only in X19 admin channels) | L01, X01, L14 | |
| F7 | "Connected accounts" for 18+ learners (YouTube, FB, IG, TikTok): permissions shown, Disconnect, no auto-post for under-18 | decisions.md L131; sharing-and-connectors.md A | MISSING | no hit for "Connected accounts" in learner boards; admin company channels exist (X19 "Disconnect":15, OAuth:22) | L04/X01 settings | Admin side DONE (X19) |
| F8 | First-visit language prompt "View in <language> or in English?" (small non-blocking banner, browser beats IP, saved in Settings + browser, never asked again, English fallback) on landing, app, admin | CLAUDE.md standing order; tasks/language-prompt.md; decisions.md L197–198 (31 Oct) | MISSING | no hit for "or in English", "browser language", "CF-IPCountry" | X20, W00, X01/L01, all admin boards, Speak app | |
| F9 | Header language switcher always present | language-prompt.md | DONE | "Language" in every board (e.g. X20:78, X01:36, L01:7); X08 "Choose your language…" | — | Must grow to 10 languages (F10) |
| F10 | 10 languages in every board (ja, de, zh-Simplified, ko), CJK subset fonts, native review gate | decisions.md L164, L202; CLAUDE.md | MISSING | 0 ja/de/zh/ko keys; no Noto CJK font; "6 languages" text in 52 boards | All 59 boards | Split boards first; biggest single job |
| F11 | Internal Video Service in NexaTute: "Make video" with "powered by Remon Motion Studio", child-safe profile, ETA, failed jobs never counted, "Open in Motion Studio" for 18+ | tasks/internal-video-service.md (30 Oct) | MISSING | no hit for "Make video" or "Internal Video". "powered by" exists only for the white-label portal ("powered by NexaTute") | Project Studio board, X09 teacher, X17 marketing | |
| F12 | Nexa ID single sign-on | ecosystem-architecture-review.md | DONE | "Log in with your Nexa ID" (X01); "Nexa ID" L01:18, X15:43 | — | |
| F13 | One shared marketplace for 3 products; under-18s see NexaTute items only with guardian approval | decisions.md L111, L114 | PARTIAL | marketplace exists (X10:22, X23:21, X16:18); X23 "under-18s buy only through the guardian" | X23, X10 | Products other than NexaTute are absent |

## G. Safety / legal shown in the UI

| # | Item | Source | Status | Evidence | Boards to touch | Notes |
|---|---|---|---|---|---|---|
| G1 | No stored money: remove "wallet", "top up from your wallet", "wallet credit", gift-card balances; refunds to the original payment method | decisions.md L111, L114 (30 Oct); HANDOVER | MISSING (contradiction) | "Wallet" L04:7 ("Wallet and Daily Pass"), X20 "Top up from your wallet, per minute", "minutes you lost come back to your wallet"; L03/L04/L09/X03/X08/X10/X13 "minutes back as wallet credit" (guarantee); X08 "1,260 minutes of wallet credit, valid until Sun 1 Aug 2027"; Shikkha Salami gift cards (X25:7, X16:8, X24:6); no hit for "original payment method" | L03, L04, L09, X02, X03, X08, X10, X13, X16, X20, X24, X25, guarantee.md | Open question: are the Doubt Pass "top-up" (X02:25, X25:18) and "Helper learning credits (18+)" (X20, X25, X08) stored value? Lawyer/owner to confirm. The "Admit-card & document wallet" is a document wallet, not money |
| G2 | Refund rule (all products): requested within 30 days, given only if approved (AI checks, a person decides), unused part with used usage deducted at list price, to the original method, EU/UK 14-day right, under-18 to the guardian, store purchases per store | decisions.md L184 (30 Oct) | PARTIAL (contradiction) | X24: "Within 30 days of a new purchase, we refund 100% of the part you haven't used" (automatic); X20 "30-day rule". No hit for "14-day right", "original payment method" | X24, X20, X15 (refund queue), X25 | |
| G3 | Terms versioning + re-consent; auto-renew consent; EU/UK 14-day withdrawal right (NT Terms 1.6.5, 1.20; NT Refund 4.7.6) | reviews/review3 C10–C12; decisions.md L112 | PARTIAL | auto-renew "chosen at purchase" (L04:2, D01, L03, X03). No hit for "re-consent", "14-day right", "Terms version" | X24, X01 checkout, L04 | |
| G4 | Brand-impersonation protection (NT Terms 1.3.6: official numbers page, we never ask for PIN/OTP) | review3 C16; decisions.md L112 | PARTIAL | X24 "We will never ask for your password or one-time code"; L01 "We never ask for your password by SMS" | X24, X20 footer | No official-numbers page or look-alike report found |
| G5 | Bug bounty: critical $500 / high $200 / medium $50 + hall of fame, no cash for under-18; ack 3 business days, triage 7 | five-gaps-solutions.md §2 (approved 30 Oct) | MISSING (contradiction) | boards say "no paid bug bounty at launch — a public thank-you list" (X15, X24, W00); "security.txt" exists (W00:6, X15:6, X24:12) | X15, X24, W00 | Newest decision wins |
| G6 | Under-18 never clones own face/voice; photo avatars not for under-18 | ecosystem-architecture-review.md corr. 1–2 | DONE | X22 "Only choose from the library. No clone and no photo avatar under 18."; X23 "no voice copies and no photo avatars under 18" | — | |
| G7 | AI label + C2PA on shared AI items | sharing-and-connectors.md | PARTIAL | C2PA X20:34, X22:25, X17:12; "AI label" X19:3 | Share/verify pages, Project Studio videos | |
| G8 | Live transcript shown but the learner's own speech never stored | ecosystem-architecture-review.md corr. 6 | PARTIAL | X24 "Your voice in live classes is processed while yo[u…]"; no transcript-specific rule found | X02/X06, X24 | Check wording by hand |
| G9 | App-store purchases +30% with a breakdown | decisions.md L156; fix17_pending 28 Oct 19:31 | DONE | "App-store charge" X03:6, X08:12, X20:5, X24:11, X25:12, D06:4, G01:4 | Speak app (B17) must reuse it | |

## H. Rename (Nexa Teacher → Nexa Tutor, Co-Teacher → Co-Tutor)

| # | Item | Source | Status | Evidence | Boards to touch | Notes |
|---|---|---|---|---|---|---|
| H1 | Rename "Nexa Teacher" → "Nexa Tutor" (bn নেক্সা টিউটর) in all boards and all languages | decisions.md L150 (30 Oct); tasks/rename-nexa-tutor.md; HANDOVER step 13 | MISSING | "Nexa Teacher" **2,342** hits in **48** boards (X20:402, X02:279, X06:212, X01:150, X08:96, X18:96, X14:85, X24:84, X26:84…); "Nexa Tutor" 0 hits; "নেক্সা টিচার" 2 hits (most bn text uses the Latin brand) | 48 boards | Do not touch human-teacher text (X09, institution teachers, revision-class teacher). Growing by 2 characters ×2,342 needs ~5 KB, which pushes X20 over the limit, so split X20 first |
| H2 | Rename "Co-Teacher" → "Co-Tutor", incl. "Co-Teacher Pass" ৳100 | same | MISSING | "Co-Teacher" **1,124** hits in **38** boards (X02:126, X20:102, X25:93, X11:65…); "Co-Tutor" 0 hits | 38 boards | The product name in the price table changes too |
| H3 | Rename in prototype/shared/*.md | rename-nexa-tutor.md | MISSING | "Nexa Teacher" in kpi.md:24, numbers.md:5, recording.md:3, x20_live.md:2 lines | shared/*.md | |
| H4 | Board/file names L05-AI-Teacher, L07-Co-teacher (and the W00 index labels) | inference from rename task | MISSING | file names unchanged | L05, L07, W00, Main | Owner to confirm whether file names change |
| H5 | "AI Tutor Creator" naming | ecosystem-architecture-review.md corr. 8 | MISSING | no hit | X22/X23 | See A15 |

## I. Small fixes / known items / hygiene

| # | Item | Source | Status | Evidence | Boards to touch | Notes |
|---|---|---|---|---|---|---|
| I1 | X12 "Open approval" on an already-open approval does nothing | HANDOVER "Known small items" | MISSING (fix not confirmed) | the button exists ("Open approval" X12:2, `srPlan.open` → `openIt(n)`); the behaviour cannot be proved by grep | X12 | Needs a runtime click test |
| I2 | Static frame: D05/D07 load test | HANDOVER known items (optional) | MISSING | "load test" D05:0, D07:0 (exists in X14:9, X10:4) | D05, D07 | |
| I3 | Static frame: G01/D04 What's new | HANDOVER known items (optional) | MISSING | "What's new" G01:0, D04:0 (exists in X08, X12, X14, X18) | G01, D04 | |
| I4 | Split X20 (Nexa Notes → new board) | HANDOVER known items | MISSING | X20 = 1,795,876 bytes | X20 + new board | Blocks E1–E4, E8, E9, H1 |
| I5 | Split/relieve X25, X12, X10 before additions | CLAUDE.md size rule | MISSING | 1,775,578 / 1,767,889 / 1,764,276 bytes | X25, X12, X10 | |
| I6 | numbers.md (v16) / kpi.md / hub.md must carry the new prices and limits (Project Studio, Speak, Club, Scripts, Family, HSK, homework limits, extra-time defaults) | project-studio-package.md §4 | MISSING | numbers.md has 0 hits for Project Studio / Nexa Speak / Homework; it still carries the 20 Nov Free Beta dates (v13 note) | prototype/shared | |
| I7 | "6 languages" wording in boards → 10 | decisions.md L164 | MISSING | "6 languages" in 52 boards (X01:16, X14:13, X17:13…) | 52 boards | Part of F10 |
| I8 | fix17_pending (28–29 Oct) owner lines: spot-check | briefs/fix17_pending.txt | DONE (spot-check) | "1:50" (X06:20…), "Raise hand" (X02:5, X06:3), "mic paused" (X02, X06, X12), "Sign out of all devices" (X08:4), "streak freeze" (X18:4), "Software updates" (X14:10), "App-store charge", "Crash Pack" (X20:138), "English Medium" (X20:14), "Autism-friendly" (X20:8), "Choose your path" (X20:1), "Doubt Pass" (X02:25, X25:18), "licensed SMS provider" (X08:4), "View pre-launch checklist" (X14, X15, X25, X26), Co-Admin X27, waiting list (X20:15), "$7" (L14:6) | — | Spot-check only, not line by line |
| I9 | dcverify.py paths ("SP/...") must point at this repo | CLAUDE.md | Not checked | not a board item | prototype/tools | Check before the first board change |
| I10 | Satisfaction loop "you said, we fixed" in What's new | decisions.md L53 (29 Oct) | MISSING (unconfirmed) | no hit for "we fixed"; "You said" hits are L14:1 and X18:1 only (context not confirmed) | X14/X18 What's new | May exist under other wording; check by hand |

---

## J. Pending work that is NOT prototype work (keep track)

| # | Item | Source | Owner / who |
|---|---|---|---|
| J1 | **Mon 2 Nov 2026, 12:00 noon Dhaka**: logos (with the owner) + live sites nexatute.com and remonlogicstudio.com via Landing Page AI with the Draft 2 legal pages; trademark-filing reminder at the same meeting | decisions.md L168, L186; HANDOVER step 1 | Owner + Claude (the new account must start it itself; the old reminder lived in another session) |
| J2 | RJSC filing Sun 1 Nov 2026 with the MoA draft | decisions.md L66; HANDOVER step 2 | Owner |
| J3 | Company prerequisites: TIN, VAT BIN, trade licence, bank account, payment accounts moved to RemonLogic (aamarPay is in Vitlous's name), D-U-N-S, Apple/Google/Microsoft developer accounts | decisions.md L186; nexa-speak-app.md | Owner |
| J4 | Lawyer: memo review (wallet, Vitlous aamarPay, children's data); trademarks (NexaTute, Motion Studio, NexaLogicDev, Nexa Speak, Nexa Tutor/Co-Tutor, Remon Growth Logic AI); whether the Doubt Pass, Helper learning credits and Boost packs are prepaid instruments; EU residency without the Data Localization Suite; bug-bounty safe harbour; legal drafts updated to the 30 Oct refund rule and no-wallet | decisions.md L150, L162, L184, L200; HANDOVER | Lawyer / owner |
| J5 | Cross-product audit report `docs/reviews/cross_product_audit_<date>.md` + the requested fresh review (not present in docs/reviews/) | tasks/cross-product-audit.md; decisions.md L133, L202 | Claude (Opus), before the prototype additions |
| J6 | Master Blueprint v32.11 build with everything in decisions.md (+ Security Control Centre §34 items from memory) | decisions.md L183; HANDOVER step 5; memory security-control-centre.md | Next account |
| J7 | Remon Motion Studio prototype (phases, boards ≤1.8 MB) and NexaLogicDev prototype + full admin panel; Free class / Learn-to-do-this, Motion Notes / Build Notes, Internal Video Service, Share and language prompt in those products | HANDOVER steps 3, 4, 10–12, 14 | Claude |
| J8 | NexaTute MVP list + week-by-week plan → GitHub Issues (only after all prototypes) | HANDOVER step 4; decisions.md L129 | Claude (lead) |
| J9 | GPU 1-week test (A6000 #1, early Dec 2026), latency BD↔NL < 1 s, 200-task benchmark; margin re-checks (Project Studio, Speak Pass ≥60%, NexaLogicDev credits) | decisions.md L122, L161, L199 | Owner + Claude |
| J10 | People plan (content team, native reviewers for ja/de/zh/ko, club teachers, 24/7 support, DPO/child-safety lead): owner says later | decisions.md L186 | Owner |
| J11 | Open owner decisions still marked "to confirm": discount caps on top of institution prices; Motion Studio public launch date; Nexa Speak store title; NexaLogicDev engine details; whether the L05/L07 file names change in the rename | decisions.md L177, L186; nexa-speak-app.md | Owner |
| J12 | Stale docs: STATUS.md (last entry 29 Oct); HANDOVER (30 Oct; old Free Beta context); CLAUDE.md "What this repo is" still says "text (6 languages)"; board count is 59, not 60 | repo | Claude (lead), when allowed to edit |

---

## Counts (rows A1–I10 only; J is excluded)
- DONE: 6 (E5, F9, F12, G6, G9, I8)
- PARTIAL: 26
- MISSING (incl. outdated/contradiction/unconfirmed): 79
- Not checked: 1 (I9)
- Total prototype rows: 112

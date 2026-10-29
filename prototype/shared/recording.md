# Recording + class-report texts — fix11/fix12 (learn1) — v1.6 (29 Oct 2026, fix18m)

> **Change note v1.6 — 29 Oct 2026 (fix18 addendum M, owner 02:46):** the NexaTute Free Beta is now **Fri 20 Nov – Wed 9 Dec 2026** (paid launch still 1 Jan 2027). Every sample date here moves −14 days (weekdays unchanged): X02 "today" = **Sun 6 Dec 2026**; recordings 30 Nov – 6 Dec 2026; auto-delete 6 Dec / 4 Dec 2027; review Wed 9 Dec. Boards use `t.day(d − 14)` for the error-notebook day numbers. Nothing else changed. Earlier: v1.5 below.

> **Change note v1.5 — 28 Oct 2026 (fix18 addendum D, learner; owner approved 23:53):** new **§9** `sec_link` / `sec_link_g` (6 languages) — the protected-link note (signed link, only the learner and the guardian can open it, expires after 15 minutes (default), a new link each time Watch is pressed) under the X02 player and in the X01 recordings-library help; X08 uses `sec_link_g`. Nothing else changed. Earlier: v1.4 below.

> **Change note v1.4 — 28 Oct 2026 (fix18 addendum C, learner; owner approved 23:31):** new **§8** sample data for the mistake timeline, red player markers, per-class improvement and library chips (labels = kpi.md v1.12 §9): §8.1 chips + one-line summaries for the 6 sample entries (e.g. entry 1 "1 mistake · 0 corrected", Quadratic Equations 42 % → 61 % (+19); entry 6 "Not enough data"); §8.2 the X02 1:1 class steps (08:20 calculation · 14:05 concept · 17:40 careless) with the correct rule, 2 practice items, whiteboard line and Nexa Teacher’s words (no-recording fallback); §8.3 X06 own poll mistakes (14:20, 22:45); §8.4 guardian "top 3 mistakes" week sample. Batch classes list only the learner’s own mistakes. §1–§7 unchanged. Earlier: v1.3 below.

> **Change note v1.3 — 27 Oct 2026 (fix12, learn1; R11-learner-12/-13, coordinator decisions G3, G7):**
> - **§2 Stop recording (R11-learner-13):** the 1:1 class shows `one_stop` next to the indicator while recording; new row `stop_toast`. The part
>   recorded so far goes through the §3 pipeline as usual; the learner can start again with `one_mid`.
> - **§6 batch code (R11-learner-12, G7):** the kind chip of the batch entries (3 and 4) follows the teaching language exactly as X06 / kpi.md §4:
>   **B-07** when Tanvir is taught in Bangla, **EN-03** when he is taught in English (en/hi/ur/ar/fr app users in Bangladesh courses fall back to
>   English, E6). New chip row `kind_en`.
> - **§7 guardian access (G3):** guardian access to an under-18 learner’s recordings and class reports is ON and LOCKED wherever recordings or
>   reports exist; X10 shows the cells locked with the tooltip "Required by policy" (sensory.md `sn_adm_req` wording).
> - Nothing else changed. Earlier: Recording + class-report texts — fix11 (learn1, 26 Oct 2026) — v1.2 (22:40: English apostrophes are typographic ’ as on every board — Don’t record, I don’t need the recording, guardian’s; earlier 22:15: fr library title “Cours enregistrés” = the fr home quick-action label, R10-learner-6; entry 2 duration 22:10 = the X02 player)

Single source for X01, X02, X06, X08, X12, X14, X15, X10, X18, D01, L-/G-/D- statics. Copy the strings EXACTLY.
Source: memory /areas/nexatute-learning.md "## Recording, class reports, dashboard & All Exams" (all [stated] 26 Oct 2026).
Register: learner boards use bn তুমি, hi/ur tum, ar أنت, fr tu (same as X01/X02). Guardian/admin boards keep the
labels (§1–§4) exactly and may change only the surrounding sentence register (আপনি, आप, آپ, vous).
Latin digits everywhere. In ur/ar wrap dates, durations and "1:1" in LTR isolation (M()/⁦…⁩) — the visible text stays identical.

RULE (replaces the old "Every class is recorded"): recording NEVER starts automatically. Retire every
"every class is recorded" / "প্রতিটি ক্লাস রেকর্ড হয়" / "auto-recording" line on learner, guardian, site and admin boards.

## 1. Recording choice labels (buttons)

| key | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| one_yes (1:1) | Record this class | এই ক্লাস রেকর্ড করো | यह क्लास रिकॉर्ड करो | یہ کلاس ریکارڈ کرو | سجِّل هذه الحصة | Enregistrer ce cours |
| one_no (1:1) | Don’t record | রেকর্ড কোরো না | रिकॉर्ड मत करो | ریکارڈ نہ کرو | لا تسجِّل | Ne pas enregistrer |
| one_mid (1:1, during class) | Start recording now | এখন রেকর্ড শুরু করো | अभी रिकॉर्डिंग शुरू करो | ابھی ریکارڈنگ شروع کرو | ابدأ التسجيل الآن | Lancer l’enregistrement |
| one_stop (1:1, during class) | Stop recording | রেকর্ড বন্ধ করো | रिकॉर्डिंग रोको | ریکارڈنگ روکو | أوقف التسجيل | Arrêter l’enregistrement |
| bat_yes (batch) | I want the recording | আমি রেকর্ডিং চাই | मुझे रिकॉर्डिंग चाहिए | مجھے ریکارڈنگ چاہیے | أريد التسجيل | Je veux l’enregistrement |
| bat_no (batch) | I don’t need the recording | আমার রেকর্ডিং লাগবে না | मुझे रिकॉर्डिंग नहीं चाहिए | مجھے ریکارڈنگ نہیں چاہیے | لا أحتاج إلى التسجيل | Je n’ai pas besoin de l’enregistrement |

Choice question (1:1 start sheet): en "Record this class?" · bn "এই ক্লাসটা রেকর্ড করবে?" · hi "यह क्लास रिकॉर्ड करें?" · ur "یہ کلاس ریکارڈ کریں؟" · ar "هل تريد تسجيل هذه الحصة؟" · fr "Enregistrer ce cours ?"

Choice note (1:1): en "Only you (and your guardian, if you are under 18) can watch it. You can also start recording later in the class." ·
bn "শুধু তুমি (আর 18-এর কম হলে তোমার অভিভাবক) দেখতে পারবে। ক্লাসের মাঝেও রেকর্ড শুরু করতে পারবে।" ·
hi "सिर्फ़ तुम (और 18 से कम हो तो तुम्हारे अभिभावक) देख सकते हो। क्लास के बीच में भी रिकॉर्डिंग शुरू कर सकते हो।" ·
ur "صرف تم (اور 18 سے کم ہو تو تمہارے سرپرست) دیکھ سکتے ہو۔ کلاس کے دوران بھی ریکارڈنگ شروع کر سکتے ہو۔" ·
ar "لا يشاهده إلا أنت (وولي أمرك إن كان عمرك أقل من 18). يمكنك أيضًا بدء التسجيل لاحقًا أثناء الحصة." ·
fr "Toi seul (et ton parent si tu as moins de 18 ans) peux le regarder. Tu peux aussi lancer l’enregistrement plus tard pendant le cours."

Choice note (batch): en "One shared recording is made only if at least one learner asks for it. Only the voices of learners who agreed are kept; others appear by nickname. Under 18: your guardian’s consent is needed." ·
bn "অন্তত একজন চাইলে তবেই পুরো ক্লাসের একটি যৌথ রেকর্ডিং হয়। শুধু রাজি শিক্ষার্থীদের কণ্ঠ রাখা হয়; বাকিরা ডাকনামে থাকে। 18-এর কম হলে অভিভাবকের সম্মতি লাগবে।" ·
hi "कम से कम एक शिक्षार्थी चाहे तभी पूरी क्लास की एक साझा रिकॉर्डिंग बनती है। सिर्फ़ सहमत शिक्षार्थियों की आवाज़ रखी जाती है; बाकी उपनाम से दिखते हैं। 18 से कम: अभिभावक की सहमति ज़रूरी है।" ·
ur "کم از کم ایک طالب علم چاہے تبھی پوری کلاس کی ایک مشترکہ ریکارڈنگ بنتی ہے۔ صرف رضامند طلبہ کی آواز رکھی جاتی ہے؛ باقی عرفی نام سے دکھتے ہیں۔ 18 سے کم: سرپرست کی رضامندی ضروری ہے۔" ·
ar "يُصنع تسجيل مشترك واحد للحصة فقط إذا طلبه متعلّم واحد على الأقل. تُحفظ أصوات من وافقوا فقط؛ ويظهر الباقون بأسماء مستعارة. أقل من 18: يلزم موافقة ولي الأمر." ·
fr "Un seul enregistrement partagé est fait seulement si au moins un élève le demande. Seules les voix des élèves d’accord sont gardées ; les autres apparaissent par pseudo. Moins de 18 ans : l’accord de ton parent est nécessaire."

## 2. Recording indicator (always visible while recording)

| key | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| ind_one | ● Recording · only in your account | ● রেকর্ড হচ্ছে · শুধু তোমার অ্যাকাউন্টে | ● रिकॉर्ड हो रहा है · सिर्फ़ तुम्हारे अकाउंट में | ● ریکارڈ ہو رہا ہے · صرف تمہارے اکاؤنٹ میں | ● جارٍ التسجيل · في حسابك فقط | ● Enregistrement · seulement dans ton compte |
| ind_bat | ● Shared recording · only voices of learners who agreed | ● যৌথ রেকর্ডিং · শুধু রাজি শিক্ষার্থীদের কণ্ঠ | ● साझा रिकॉर्डिंग · सिर्फ़ सहमत शिक्षार्थियों की आवाज़ | ● مشترکہ ریکارڈنگ · صرف رضامند طلبہ کی آواز | ● تسجيل مشترك · أصوات الموافقين فقط | ● Enregistrement partagé · seules les voix des élèves d’accord |
| ind_off | Not recording | রেকর্ড হচ্ছে না | रिकॉर्ड नहीं हो रहा | ریکارڈ نہیں ہو رہا | لا يوجد تسجيل | Pas d’enregistrement |
| mid_toast | Recording started — the part before now is not recorded. | রেকর্ড শুরু হলো — এর আগের অংশ রেকর্ড হয়নি। | रिकॉर्डिंग शुरू हुई — इससे पहले का हिस्सा रिकॉर्ड नहीं हुआ। | ریکارڈنگ شروع ہوئی — اس سے پہلے کا حصہ ریکارڈ نہیں ہوا۔ | بدأ التسجيل — الجزء السابق لم يُسجَّل. | Enregistrement lancé — la partie d’avant n’est pas enregistrée. |
| stop_toast (v1.3, after one_stop) | Recording stopped — the part recorded so far stays in your Recordings. | রেকর্ড বন্ধ হলো — এ পর্যন্ত যতটুকু রেকর্ড হয়েছে, তা তোমার রেকর্ডিং-এ থাকবে। | रिकॉर्डिंग रुकी — अब तक रिकॉर्ड हुआ हिस्सा तुम्हारी रिकॉर्डिंग में रहेगा। | ریکارڈنگ رک گئی — اب تک ریکارڈ ہونے والا حصہ تمہاری ریکارڈنگ میں رہے گا۔ | توقّف التسجيل — يبقى الجزء المسجَّل حتى الآن في تسجيلاتك. | Enregistrement arrêté — la partie déjà enregistrée reste dans tes Cours enregistrés. |

## 3. Recording status labels (one set, this order)

| key | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| none | Not requested | চাওয়া হয়নি | माँगी नहीं गई | مانگی نہیں گئی | لم يُطلب | Non demandé |
| consent | Consent pending | সম্মতির অপেক্ষায় | सहमति बाकी | رضامندی باقی | بانتظار الموافقة | Accord en attente |
| queued | Queued | সারিতে আছে | कतार में | قطار میں | في قائمة الانتظار | En file d’attente |
| proc | Processing | প্রসেস হচ্ছে | प्रोसेस हो रही है | پروسیس ہو رہی ہے | قيد المعالجة | En traitement |
| up | Uploading | আপলোড হচ্ছে | अपलोड हो रही है | اپ لوڈ ہو رہی ہے | جارٍ الرفع | Envoi en cours |
| verify | Verifying | যাচাই হচ্ছে | जाँच हो रही है | جانچ ہو رہی ہے | جارٍ التحقق | Vérification |
| ready | Ready | তৈরি | तैयार | تیار | جاهز | Prêt |
| failed | Failed | ব্যর্থ | विफल | ناکام | فشل | Échec |
| retry (button) | Retry | আবার চেষ্টা করো | फिर कोशिश करो | دوبارہ کوشش کرو | أعد المحاولة | Réessayer |
| watch (button, Ready only) | Watch | দেখো | देखो | دیکھو | شاهد | Regarder |

Status help (tooltip, 6 langs): en "The recording is made in your browser, uploaded to our storage, then checked (SHA-256). “Watch” appears only after the check." ·
bn "রেকর্ডিং তোমার ব্রাউজারেই তৈরি হয়, আমাদের স্টোরেজে আপলোড হয়, তারপর যাচাই হয় (SHA-256)। যাচাইয়ের পরই “দেখো” আসে।" ·
hi "रिकॉर्डिंग तुम्हारे ब्राउज़र में ही बनती है, हमारे स्टोरेज पर अपलोड होती है, फिर जाँची जाती है (SHA-256)। जाँच के बाद ही “देखो” आता है।" ·
ur "ریکارڈنگ تمہارے براؤزر میں ہی بنتی ہے، ہمارے اسٹوریج پر اپ لوڈ ہوتی ہے، پھر جانچی جاتی ہے (SHA-256)۔ جانچ کے بعد ہی “دیکھو” آتا ہے۔" ·
ar "يُصنع التسجيل في متصفحك، ثم يُرفع إلى تخزيننا، ثم يُتحقق منه (SHA-256). لا يظهر زر “شاهد” إلا بعد التحقق." ·
fr "L’enregistrement est fait dans ton navigateur, envoyé sur notre stockage, puis vérifié (SHA-256). « Regarder » n’apparaît qu’après la vérification."

Failed reason (sample): en "Upload stopped — the connection dropped" · bn "আপলোড থেমে গেছে — সংযোগ কেটে গিয়েছিল" · hi "अपलोड रुक गया — कनेक्शन टूट गया था" · ur "اپ لوڈ رک گیا — کنکشن ٹوٹ گیا تھا" · ar "توقف الرفع — انقطع الاتصال" · fr "Envoi interrompu — la connexion a coupé"
Consent pending reason (sample, under-18 batch): en "Waiting for your guardian’s consent" · bn "তোমার অভিভাবকের সম্মতির অপেক্ষায়" · hi "तुम्हारे अभिभावक की सहमति का इंतज़ार" · ur "تمہارے سرپرست کی رضامندی کا انتظار" · ar "بانتظار موافقة ولي أمرك" · fr "En attente de l’accord de ton parent"

## 4. Class-report status labels (separate from the recording status)

| key | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| r_gen | Generating | তৈরি হচ্ছে | बन रही है | بن رہی ہے | قيد الإنشاء | En préparation |
| r_ready | Ready | তৈরি | तैयार | تیار | جاهز | Prêt |
| r_upd | Updated | হালনাগাদ | अपडेट हुई | اپ ڈیٹ ہوئی | محدَّث | Mis à jour |
| r_nodata | Not enough data | যথেষ্ট তথ্য নেই | पर्याप्त डेटा नहीं | کافی ڈیٹا نہیں | لا توجد بيانات كافية | Pas assez de données |
| r_na | Unavailable | পাওয়া যাচ্ছে না | उपलब्ध नहीं | دستیاب نہیں | غير متاح | Indisponible |

Prefix for the report chip: en "Report:" · bn "রিপোর্ট:" · hi "रिपोर्ट:" · ur "رپورٹ:" · ar "التقرير:" · fr "Rapport :"
A class report exists even when the class was not recorded (it is built from the Nexa Teacher’s own text and the quiz results);
"Updated" = a later review or practice changed the report (review history is append-only).

## 5. Library naming format (memory, exact)

"Subject — Topic — Lesson/Unit — Class date", e.g. memory’s own example "Mathematics — Linear Equations — Lesson 03 — 26 Oct 2026".
Hierarchy: Subject → Unit → Topic → Class; filter (subject, status) + search. Repeat classes of a topic are separate entries linked to the review history.
Card fields: subject, topic, lesson, date, duration, AI tutor, status, Watch (Watch only when Ready).
Retention: deleted automatically 12 months after the class; switch "Keep until my course ends".

| key | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| lib_h (library title = the home quick-action label) | Recordings | রেকর্ডিং | रिकॉर्डिंग | ریکارڈنگ | التسجيلات | Cours enregistrés |
| lib_search (placeholder) | Search subject, topic or lesson | বিষয়, টপিক বা পাঠ খোঁজো | विषय, टॉपिक या पाठ खोजो | مضمون، ٹاپک یا سبق تلاش کرو | ابحث عن مادة أو موضوع أو درس | Chercher une matière, un thème ou une leçon |
| lib_keep_rule | Deleted automatically 12 months after the class | ক্লাসের 12 মাস পরে নিজে থেকে মুছে যায় | क्लास के 12 महीने बाद अपने आप मिट जाती है | کلاس کے 12 مہینے بعد خود بخود مٹ جاتی ہے | تُحذف تلقائيًا بعد 12 شهرًا من الحصة | Supprimé automatiquement 12 mois après le cours |
| lib_keep_sw | Keep until my course ends | কোর্স শেষ হওয়া পর্যন্ত রাখো | कोर्स ख़त्म होने तक रखो | کورس ختم ہونے تک رکھو | احتفظ بها حتى نهاية دورتي | Garder jusqu’à la fin de mon cours |
| lib_rep | 2nd class on this topic · linked to your review history | এই টপিকের 2য় ক্লাস · তোমার রিভিউ ইতিহাসের সঙ্গে যুক্ত | इस टॉपिक की 2री क्लास · तुम्हारे रिव्यू इतिहास से जुड़ी | اس ٹاپک کی دوسری کلاس · تمہاری ریویو ہسٹری سے جڑی | الحصة الثانية في هذا الموضوع · مرتبطة بسجل مراجعتك | 2e cours sur ce thème · lié à ton historique de révision |
| lib_tutor | Nexa Teacher (AI) | Nexa Teacher (AI) | Nexa Teacher (AI) | Nexa Teacher (AI) | Nexa Teacher (AI) | Nexa Teacher (AI) |

Learner = Tanvir (SSC 2027, batch B-07). X02 is set on Sun 6 Dec 2026 (Free Beta 20 Nov – 9 Dec 2026; the code keeps "today = 20" and shows day numbers 14 days earlier), so every sample class is on or before 6 Dec 2026.
Months: bn ডিসেম্বর / নভেম্বর · hi दिसंबर / नवंबर · ur دسمبر / نومبر · ar ديسمبر / نوفمبر · fr déc. / nov. (short) / décembre / novembre. "1:1" and "B-07" stay Latin.

## 6. The 6 sample library entries (same on every board that lists them)

| # | Subject | Unit | Topic | Lesson | Date | Kind | Duration | Status | Report |
|---|---|---|---|---|---|---|---|---|---|
| 1 | General Mathematics | Algebra | Quadratic Equations | Lesson 03 | Sun 6 Dec 2026 | 1:1 | 22:10 | Ready (today’s class; X02 shows Queued → Processing → Uploading → Verifying → Ready after the class) | Ready |
| 2 | General Mathematics | Algebra | Quadratic Equations | Lesson 02 | Fri 4 Dec 2026 | 1:1 | 22:10 | Ready · "2nd class on this topic" | Updated |
| 3 | General Mathematics | Algebra | Factorisation | Lesson 01 | Wed 2 Dec 2026 | Batch B-07 (shared) | 40:00 | Ready | Ready |
| 4 | Physics | Mechanics | Motion | Lesson 02 | Sat 5 Dec 2026 | Batch B-07 (shared) | 40:00 | Consent pending (guardian) | Ready |
| 5 | Physics | Mechanics | Motion | Lesson 01 | Thu 3 Dec 2026 | 1:1 | 18:45 | Failed + Retry ("Upload stopped — the connection dropped") | Ready |
| 6 | General Mathematics | Sets & Functions | Sets | Lesson 01 | Mon 30 Nov 2026 | 1:1 | 20:05 | Not requested ("Don’t record" chosen) | Not enough data |

Entry titles (format "Subject — Topic — Lesson — Class date"):

en
1. General Mathematics — Quadratic Equations — Lesson 03 — 6 Dec 2026
2. General Mathematics — Quadratic Equations — Lesson 02 — 4 Dec 2026
3. General Mathematics — Factorisation — Lesson 01 — 2 Dec 2026
4. Physics — Motion — Lesson 02 — 5 Dec 2026
5. Physics — Motion — Lesson 01 — 3 Dec 2026
6. General Mathematics — Sets — Lesson 01 — 30 Nov 2026

bn
1. সাধারণ গণিত — দ্বিঘাত সমীকরণ — পাঠ 03 — 6 ডিসেম্বর 2026
2. সাধারণ গণিত — দ্বিঘাত সমীকরণ — পাঠ 02 — 4 ডিসেম্বর 2026
3. সাধারণ গণিত — উৎপাদকে বিশ্লেষণ — পাঠ 01 — 2 ডিসেম্বর 2026
4. পদার্থবিজ্ঞান — গতি — পাঠ 02 — 5 ডিসেম্বর 2026
5. পদার্থবিজ্ঞান — গতি — পাঠ 01 — 3 ডিসেম্বর 2026
6. সাধারণ গণিত — সেট — পাঠ 01 — 30 নভেম্বর 2026

hi
1. सामान्य गणित — द्विघात समीकरण — पाठ 03 — 6 दिसंबर 2026
2. सामान्य गणित — द्विघात समीकरण — पाठ 02 — 4 दिसंबर 2026
3. सामान्य गणित — गुणनखंड — पाठ 01 — 2 दिसंबर 2026
4. भौतिकी — गति — पाठ 02 — 5 दिसंबर 2026
5. भौतिकी — गति — पाठ 01 — 3 दिसंबर 2026
6. सामान्य गणित — समुच्चय — पाठ 01 — 30 नवंबर 2026

ur
1. عام ریاضی — دو درجی مساوات — سبق 03 — 6 دسمبر 2026
2. عام ریاضی — دو درجی مساوات — سبق 02 — 4 دسمبر 2026
3. عام ریاضی — تجزی — سبق 01 — 2 دسمبر 2026
4. طبیعیات — حرکت — سبق 02 — 5 دسمبر 2026
5. طبیعیات — حرکت — سبق 01 — 3 دسمبر 2026
6. عام ریاضی — سیٹ — سبق 01 — 30 نومبر 2026

ar
1. الرياضيات العامة — المعادلات التربيعية — الدرس 03 — 6 ديسمبر 2026
2. الرياضيات العامة — المعادلات التربيعية — الدرس 02 — 4 ديسمبر 2026
3. الرياضيات العامة — التحليل إلى عوامل — الدرس 01 — 2 ديسمبر 2026
4. الفيزياء — الحركة — الدرس 02 — 5 ديسمبر 2026
5. الفيزياء — الحركة — الدرس 01 — 3 ديسمبر 2026
6. الرياضيات العامة — المجموعات — الدرس 01 — 30 نوفمبر 2026

fr
1. Mathématiques générales — Équations du second degré — Leçon 03 — 6 déc. 2026
2. Mathématiques générales — Équations du second degré — Leçon 02 — 4 déc. 2026
3. Mathématiques générales — Factorisation — Leçon 01 — 2 déc. 2026
4. Physique — Mouvement — Leçon 02 — 5 déc. 2026
5. Physique — Mouvement — Leçon 01 — 3 déc. 2026
6. Mathématiques générales — Ensembles — Leçon 01 — 30 nov. 2026

Unit names (order en · bn · hi · ur · ar · fr): Algebra · বীজগণিত · बीजगणित · الجبرا · الجبر · Algèbre; Sets & Functions · সেট ও ফাংশন · समुच्चय और फलन · سیٹ اور فنکشن · المجموعات والدوال · Ensembles et fonctions; Mechanics · বলবিদ্যা · यांत्रिकी · میکانیات · الميكانيكا · Mécanique.
Kind chips: "1:1" · "Batch B-07 · shared" = bn "ব্যাচ B-07 · যৌথ" · hi "बैच B-07 · साझा" · ur "بیچ B-07 · مشترکہ" · ar "الدفعة B-07 · مشترك" · fr "Groupe B-07 · partagé".
Batch code (v1.3, R11-learner-12 / G7): the chip uses the learner’s batch for the CURRENT teaching language, exactly as X06 / kpi.md §4 — B-07 when
taught in Bangla, EN-03 when taught in English (en/hi/ur/ar/fr app users in Bangladesh courses fall back to English, E6). kind_en = en "Batch EN-03 · shared" ·
bn "ব্যাচ EN-03 · যৌথ" · hi "बैच EN-03 · साझा" · ur "بیچ EN-03 · مشترکہ" · ar "الدفعة EN-03 · مشترك" · fr "Groupe EN-03 · partagé" (ur/ar wrap the code in M()).
Retention date on entry 1: "Auto-delete on 6 Dec 2027" (bn "6 ডিসেম্বর 2027-এ নিজে থেকে মুছে যাবে").

Guardian view (X08/G01): the guardian of an under-18 learner sees the same entries and the class reports (summary). Entry 4's
"Consent pending" is the guardian’s own action there ("Give consent" / "Not now"). No other learner’s voice, video, KPI or mistakes are shown.
Admin view (X14/X15): counts by status use the same §3 labels; consent records + access log per recording (PDPO 2025).

## 7. Guardian access and admin lock (v1.3, G3)

Guardian access to an under-18 learner’s recordings and class reports is ON and LOCKED wherever recordings or reports exist (X01 library, X02 report,
X06, X08, G01). It is not a per-plan option: X10 Plans & modules shows the cells ON with a lock and the tooltip "Required by policy"
(bn "নীতিমালা অনুযায়ী বাধ্যতামূলক", hi "नीति के अनुसार ज़रूरी", ur "پالیسی کے تحت لازمی", ar "مطلوب بموجب السياسة", fr "Requis par la politique" —
the sensory.md `sn_adm_req` wording). Adults (18+) decide themselves; no other learner ever sees a recording or report.

## 8. Mistake timeline, player markers, per-class improvement & library chips — sample data (v1.4, fix18 addendum C, owner 28 Oct 2026 23:31)

Labels come from **kpi.md v1.12 §9**. Learner boards use the plain key; guardian / institution boards use the `_g` row where one exists (third person about the child). (`mt9_*`, `pl9_*`, `im9_*`, `lb9_*`, `g9_*`). Admin defaults (X10 "Class report & mistake timeline", two-person approval, logged): feature on, **10 s** before the mistake, **2** practice items per mistake, kinds shown, guardian top-3 on, improvement minimum **5** answers.
Privacy: batch classes (entries 3, 4 and the X06 class) list only Tanvir’s OWN mistakes; only Tanvir and his guardian (under 18) see them — no other learner’s mistakes, voice, video or scores.

### 8.1 Library chips for the 6 sample entries (§6) — same on X01 library, X18 entry card, D01, X08 / G01
| # | Mistakes · corrected | Topic mastery before → after (change) | One-line summary key |
|---|---|---|---|
| 1 | 1 · 0 (14:05 sign rule, concept) | Quadratic Equations 42 % → 61 % (+19) | rs8_1 |
| 2 | 1 · 1 (09:30 a × c, calculation) | Quadratic Equations 30 % → 42 % (+12) | rs8_2 |
| 3 | 2 · 1 (own mistakes only) | Factorisation 47 % → 55 % (+8) | rs8_3 |
| 4 | 0 (own mistakes only) | Motion 51 % → 57 % (+6) | rs8_4 |
| 5 | 2 · 2 (upload failed → text rows, no video) | Motion 41 % → 51 % (+10) | rs8_5 |
| 6 | 1 · 1 (not recorded → text row, no video) | Sets — Not enough data (4 answers) | rs8_6 |
Percentages: Latin digits; ur/ar wrap "42 % → 61 %" and "+19 %" in an LTR isolate.


| key | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| rs8_1 | Solved x² − 5x + 6 = 0 by splitting the middle term. | মধ্যপদ বিভাজন করে x² − 5x + 6 = 0 সমাধান করেছ। | मध्य पद तोड़कर x² − 5x + 6 = 0 हल किया। | درمیانی رکن توڑ کر ⁦x² − 5x + 6 = 0⁩ حل کیا۔ | حللت ⁦x² − 5x + 6 = 0⁩ بتجزئة الحد الأوسط. | Tu as résolu x² − 5x + 6 = 0 en décomposant le terme du milieu. |
| rs8_1_g | Solved x² − 5x + 6 = 0 by splitting the middle term. | মধ্যপদ বিভাজন করে x² − 5x + 6 = 0 সমাধান করেছে। | मध्य पद तोड़कर x² − 5x + 6 = 0 हल किया। | درمیانی رکن توڑ کر ⁦x² − 5x + 6 = 0⁩ حل کیا۔ | حلّ ⁦x² − 5x + 6 = 0⁩ بتجزئة الحد الأوسط. | A résolu x² − 5x + 6 = 0 en décomposant le terme du milieu. |
| rs8_2 | Standard form of a quadratic equation and what its roots are. | দ্বিঘাত সমীকরণের আদর্শ রূপ আর মূল কী। | द्विघात समीकरण का मानक रूप और उसके मूल क्या हैं। | دو درجی مساوات کی معیاری شکل اور اس کے جذر کیا ہیں۔ | الصورة القياسية للمعادلة التربيعية وما هي جذورها. | La forme standard d’une équation du second degré et ce que sont ses racines. |
| rs8_3 | Taking out common factors and grouping terms. | সাধারণ উৎপাদক বের করা আর পদ জোড়া করা। | उभयनिष्ठ गुणनखंड निकालना और पदों का समूह बनाना। | مشترک جزوِ ضربی نکالنا اور ارکان کو گروپ کرنا۔ | إخراج العامل المشترك وتجميع الحدود. | Mettre en facteur commun et regrouper les termes. |
| rs8_4 | Speed, velocity and acceleration on a straight road. | সোজা রাস্তায় দ্রুতি, বেগ আর ত্বরণ। | सीधी सड़क पर चाल, वेग और त्वरण। | سیدھی سڑک پر رفتار، سمتی رفتار اور اسراع۔ | السرعة القياسية والمتجهة والتسارع على طريق مستقيم. | Vitesse, vecteur vitesse et accélération sur une route droite. |
| rs8_5 | Distance–time graphs and average speed. | দূরত্ব–সময় লেখচিত্র আর গড় দ্রুতি। | दूरी–समय ग्राफ़ और औसत चाल। | فاصلہ–وقت گراف اور اوسط رفتار۔ | منحنيات المسافة–الزمن والسرعة المتوسطة. | Graphiques distance–temps et vitesse moyenne. |
| rs8_6 | Sets: listing the elements and the empty set. | সেট: উপাদান তালিকা করা আর ফাঁকা সেট। | समुच्चय: अवयवों की सूची और रिक्त समुच्चय। | سیٹ: ارکان کی فہرست اور خالی سیٹ۔ | المجموعات: سرد العناصر والمجموعة الخالية. | Ensembles : lister les éléments et l’ensemble vide. |

### 8.2 X02 1:1 class (entry 1, today) — the three whiteboard steps where a mistake can happen (the live prototype lists only the steps Tanvir actually got wrong; the saved sample class has the 14:05 one)
Minutes: step 3 → **08:20** (kind calculation) · step 4 → **14:05** (kind concept) · step 5 → **17:40** (kind careless). "What went wrong" = the X02 step-mistake name (`e_split` / `e_sign`); Watch opens the player at minute − 10 s (08:10 / 13:55 / 17:30). Practice items (default 2, maths only): step 3 `x² − 7x + 12 = 0` · `x² − 6x + 8 = 0`; step 4 `−4x + 8 = ?` · `−5x + 15 = ?`; step 5 `x(x − 4) − 3(x − 4) = ?` · `x(x + 1) − 2(x + 1) = ?`. Whiteboard at that moment (no-recording fallback): step 3 `x² − 2x + 3x + 6 = 0` · step 4 `x(x − 2) − 3(x + 2) = 0` · step 5 `(x − 2)(x + 3) = 0`.

| key | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| r8_s3 | Pick two terms that multiply to 6x² and add to −5x: −2x and −3x. | এমন দুটি পদ নাও যাদের গুণফল 6x² আর যোগফল −5x: −2x ও −3x। | ऐसे दो पद लो जिनका गुणनफल 6x² और योग −5x हो: −2x और −3x। | ایسے دو رکن لو جن کا حاصلِ ضرب ⁦6x²⁩ اور مجموعہ ⁦−5x⁩ ہو: ⁦−2x⁩ اور ⁦−3x⁩۔ | اختر حدّين حاصل ضربهما ⁦6x²⁩ ومجموعهما ⁦−5x⁩: ⁦−2x⁩ و⁦−3x⁩. | Choisis deux termes de produit 6x² et de somme −5x : −2x et −3x. |
| r8_s4 | Taking out −3 changes every sign inside: −3x + 6 = −3(x − 2). | −3 বাইরে নিলে ভেতরের সব চিহ্ন বদলায়: −3x + 6 = −3(x − 2)। | −3 बाहर निकालने पर अंदर के सारे चिह्न बदलते हैं: −3x + 6 = −3(x − 2)। | ⁦−3⁩ باہر نکالنے پر اندر کی سب علامتیں بدلتی ہیں: ⁦−3x + 6 = −3(x − 2)⁩۔ | إخراج ⁦−3⁩ يغيّر كل الإشارات في الداخل: ⁦−3x + 6 = −3(x − 2)⁩. | Sortir −3 change tous les signes à l’intérieur : −3x + 6 = −3(x − 2). |
| r8_s5 | Copy the common bracket and its sign together: (x − 2)(x − 3) = 0. | সাধারণ বন্ধনী আর তার চিহ্ন একসাথে লেখো: (x − 2)(x − 3) = 0। | उभयनिष्ठ कोष्ठक और उसका चिह्न साथ लिखो: (x − 2)(x − 3) = 0। | مشترک قوسین اور اس کی علامت ساتھ لکھو: ⁦(x − 2)(x − 3) = 0⁩۔ | انسخ القوس المشترك مع إشارته معًا: ⁦(x − 2)(x − 3) = 0⁩. | Recopie la parenthèse commune avec son signe : (x − 2)(x − 3) = 0. |
| n8_s3 | Check: −2x + 3x = +x, not −5x. Both parts must be negative here. | মিলিয়ে দেখো: −2x + 3x = +x, −5x নয়। এখানে দুটো অংশই ঋণাত্মক হবে। | जाँचो: −2x + 3x = +x, −5x नहीं। यहाँ दोनों हिस्से ऋणात्मक होंगे। | جانچو: ⁦−2x + 3x = +x⁩، ⁦−5x⁩ نہیں۔ یہاں دونوں حصے منفی ہوں گے۔ | تحقّق: ⁦−2x + 3x = +x⁩ وليس ⁦−5x⁩. يجب أن يكون الجزآن سالبين هنا. | Vérifie : −2x + 3x = +x, pas −5x. Ici, les deux parties doivent être négatives. |
| n8_s4 | Multiply back: −3 × (+2) = −6, but we need +6 — so it’s −3(x − 2). | গুণ করে মিলাও: −3 × (+2) = −6, কিন্তু দরকার +6 — তাই −3(x − 2)। | गुणा करके जाँचो: −3 × (+2) = −6, पर चाहिए +6 — इसलिए −3(x − 2)। | ضرب کر کے جانچو: ⁦−3 × (+2) = −6⁩، مگر چاہیے ⁦+6⁩ — اس لیے ⁦−3(x − 2)⁩۔ | اضرب للتحقّق: ⁦−3 × (+2) = −6⁩، لكننا نحتاج ⁦+6⁩ — إذن ⁦−3(x − 2)⁩. | Redéveloppe : −3 × (+2) = −6, mais il faut +6 — donc −3(x − 2). |
| n8_s5 | Look at the line above: it was − 3, so the factor is (x − 3). | ওপরের লাইনটা দেখো: সেখানে − 3 ছিল, তাই উৎপাদক (x − 3)। | ऊपर की लाइन देखो: वहाँ − 3 था, इसलिए गुणनखंड (x − 3) है। | اوپر کی لائن دیکھو: وہاں ⁦− 3⁩ تھا، اس لیے جزوِ ضربی ⁦(x − 3)⁩ ہے۔ | انظر إلى السطر السابق: كان ⁦− 3⁩، لذا العامل هو ⁦(x − 3)⁩. | Regarde la ligne du dessus : c’était − 3, donc le facteur est (x − 3). |

### 8.3 X06 1:50 AI class (today, 40:00) — Tanvir’s OWN poll mistakes only
Rows: poll 2 at **14:20** (calculation; practice `x² − 7x + 12 = 0` · `x² + 2x − 3 = 0`) · poll 3 at **22:45** (concept; practice `x² + 4 = 0` · `x² − 4 = 0`). Watch opens the shared class recording 10 s before (14:10 / 22:35) when the batch recording is Ready; otherwise the text fallback. Improvement: Quadratic Equations 61 % → 66 % (+5).

| key | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| w8_p2 | Chose 11 for b² − 4ac in x² − 5x + 6 = 0 | x² − 5x + 6 = 0-এ b² − 4ac-এর উত্তর 11 দিয়েছ | x² − 5x + 6 = 0 में b² − 4ac के लिए 11 चुना | ⁦x² − 5x + 6 = 0⁩ میں ⁦b² − 4ac⁩ کے لیے ⁦11⁩ چنا | اخترت ⁦11⁩ لقيمة ⁦b² − 4ac⁩ في ⁦x² − 5x + 6 = 0⁩ | Tu as choisi 11 pour b² − 4ac dans x² − 5x + 6 = 0 |
| w8_p2_g | Chose 11 for b² − 4ac in x² − 5x + 6 = 0 | x² − 5x + 6 = 0-এ b² − 4ac-এর উত্তর 11 দিয়েছে | x² − 5x + 6 = 0 में b² − 4ac के लिए 11 चुना | ⁦x² − 5x + 6 = 0⁩ میں ⁦b² − 4ac⁩ کے لیے ⁦11⁩ چنا | اختار ⁦11⁩ لقيمة ⁦b² − 4ac⁩ في ⁦x² − 5x + 6 = 0⁩ | A choisi 11 pour b² − 4ac dans x² − 5x + 6 = 0 |
| r8_p2 | 4ac = 4 × 1 × 6 = 24, so b² − 4ac = 25 − 24 = 1. | 4ac = 4 × 1 × 6 = 24, তাই b² − 4ac = 25 − 24 = 1। | 4ac = 4 × 1 × 6 = 24, इसलिए b² − 4ac = 25 − 24 = 1। | ⁦4ac = 4 × 1 × 6 = 24⁩، اس لیے ⁦b² − 4ac = 25 − 24 = 1⁩۔ | ⁦4ac = 4 × 1 × 6 = 24⁩، إذن ⁦b² − 4ac = 25 − 24 = 1⁩. | 4ac = 4 × 1 × 6 = 24, donc b² − 4ac = 25 − 24 = 1. |
| w8_p3 | Said 2 real roots when b² − 4ac < 0 | b² − 4ac < 0 হলে 2টি বাস্তব মূল বলেছ | b² − 4ac < 0 होने पर 2 वास्तविक मूल बताए | ⁦b² − 4ac < 0⁩ پر ⁦2⁩ حقیقی جذر بتائے | قلت جذرين حقيقيين عندما ⁦b² − 4ac < 0⁩ | Tu as dit 2 racines réelles quand b² − 4ac < 0 |
| w8_p3_g | Said 2 real roots when b² − 4ac < 0 | b² − 4ac < 0 হলে 2টি বাস্তব মূল বলেছে | b² − 4ac < 0 होने पर 2 वास्तविक मूल बताए | ⁦b² − 4ac < 0⁩ پر ⁦2⁩ حقیقی جذر بتائے | قال جذرين حقيقيين عندما ⁦b² − 4ac < 0⁩ | A dit 2 racines réelles quand b² − 4ac < 0 |
| r8_p3 | D < 0 → no real roots; D = 0 → one; D > 0 → two. | D < 0 → কোনো বাস্তব মূল নেই; D = 0 → একটি; D > 0 → দুটি। | D < 0 → कोई वास्तविक मूल नहीं; D = 0 → एक; D > 0 → दो। | ⁦D < 0⁩ ← کوئی حقیقی جذر نہیں؛ ⁦D = 0⁩ ← ایک؛ ⁦D > 0⁩ ← دو۔ | ⁦D < 0⁩ ← لا جذور حقيقية؛ ⁦D = 0⁩ ← جذر واحد؛ ⁦D > 0⁩ ← جذران. | D < 0 → aucune racine réelle ; D = 0 → une ; D > 0 → deux. |

### 8.4 Guardian weekly report (X08, G01) — "This week’s top 3 mistakes" (adult tone, `g9_*`)
Week 30 Nov – 6 Dec 2026: (1) entry 1 · 14:05 sign rule (concept) · not corrected yet; (2) entry 5 · 06:15 distance–time slope (concept) · corrected; (3) entry 3 · 18:40 common factor sign (calculation) · corrected. Each opens the child’s report / recording at that minute (10 s before). Improvement chips as §8.1.

## 9. Protected recording links (v1.5, fix18 addendum D — owner approved 28 Oct 2026 23:53; Cloudflare R2 signed links, validity 15 minutes (default), set in admin X14 → Video & recording delivery)
Small note under the X02 player and in the recordings-library help (X01); the guardian view (X08) uses `sec_link_g`. Latin digits; ur/ar wrap 15 in an LTR isolate.

| key | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| sec_link | Protected link — only you (and your guardian) can open it; it expires after 15 minutes and a new one is made each time you press Watch. | সুরক্ষিত লিংক — শুধু তুমি (আর তোমার অভিভাবক) খুলতে পারো; 15 মিনিট পরে এর মেয়াদ শেষ হয়, আর প্রতিবার “দেখো” চাপলে নতুন লিংক তৈরি হয়। | सुरक्षित लिंक — सिर्फ़ तुम (और तुम्हारे अभिभावक) इसे खोल सकते हो; 15 मिनट बाद इसकी अवधि ख़त्म हो जाती है, और हर बार “देखो” दबाने पर नया लिंक बनता है। | محفوظ لنک — صرف تم (اور تمہارے سرپرست) اسے کھول سکتے ہو؛ ⁦15⁩ منٹ بعد اس کی میعاد ختم ہو جاتی ہے، اور ہر بار “دیکھو” دبانے پر نیا لنک بنتا ہے۔ | رابط محميّ — لا يفتحه إلا أنت (ووليّ أمرك)؛ تنتهي صلاحيته بعد ⁦15⁩ دقيقة، ويُنشأ رابط جديد في كل مرة تضغط فيها «شاهد». | Lien protégé — seul toi (et ton parent) peux l’ouvrir ; il expire après 15 minutes et un nouveau est créé chaque fois que tu appuies sur Regarder. |
| sec_link_g | Protected link — only you and your child can open it; it expires after 15 minutes and a new one is made each time you press Watch. | সুরক্ষিত লিংক — শুধু আপনি আর আপনার সন্তান খুলতে পারেন; 15 মিনিট পরে এর মেয়াদ শেষ হয়, আর প্রতিবার “দেখুন” চাপলে নতুন লিংক তৈরি হয়। | सुरक्षित लिंक — सिर्फ़ आप और आपका बच्चा इसे खोल सकते हैं; 15 मिनट बाद इसकी अवधि ख़त्म हो जाती है, और हर बार “देखें” दबाने पर नया लिंक बनता है। | محفوظ لنک — صرف آپ اور آپ کا بچہ اسے کھول سکتے ہیں؛ ⁦15⁩ منٹ بعد اس کی میعاد ختم ہو جاتی ہے، اور ہر بار “دیکھیں” دبانے پر نیا لنک بنتا ہے۔ | رابط محميّ — لا يفتحه إلا أنتم وطفلكم؛ تنتهي صلاحيته بعد ⁦15⁩ دقيقة، ويُنشأ رابط جديد في كل مرة تضغطون فيها «مشاهدة». | Lien protégé — seuls vous et votre enfant pouvez l’ouvrir ; il expire après 15 minutes et un nouveau est créé chaque fois que vous appuyez sur Regarder. |

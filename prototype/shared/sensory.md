# Sensory-friendly mode texts — v4 (fix15, family, 28 Oct 2026)

> **CHANGE NOTE — v2, 27 Oct 2026 (fix pass 12, coordinator decisions G1 + G3; family area):**
> - **G1 naming.** PlayBoom's mode uses the shared name. No localized "calm" word (শান্ত মোড / शांत मोड / پرسکون موڈ / الوضع الهادئ / mode calme) may name
>   EITHER mode anywhere. `sn_pb` is rewritten (it said "PlayBoom's calm mode is this same mode"); `sn_teacher` no longer says শান্ত স্ক্রিন /
>   शांत स्क्रीन / پرسکون اسکرین / شاشة أهدأ / écran plus calme. X05 shows `sn_name` as the mode label (not a "calm" label).
>   The rank-hiding mode is "Calm mode" in Latin in every language (kpi.md, learn2), optionally followed by a short descriptor
>   (bn "Calm mode · র‍্যাঙ্ক লুকানো", en "Calm mode · ranks hidden", hi "Calm mode · रैंक छिपी", ur "Calm mode · رینک پوشیدہ",
>   ar "Calm mode · إخفاء الترتيب", fr "Calm mode · classements masqués"). `sn_not_calm` already uses the Latin name — unchanged.
> - **G3 locks.** §5 rewritten: Sensory-friendly mode is ON and LOCKED in every plan; only the platform-wide switch and the default settings are
>   editable. New 6-language keys `sn_adm_val`, `sn_adm_req`, `sn_adm_lock` (§5).
> - **G2 / G6.** §2 note says "extra-time settings" (not "slow-learner settings"). New §3 rule + key `sn_setlog`: turning the mode on or off is
>   written to the settings log, never to the consent record.
> - Unchanged keys: sn_name, sn_short, sn_desc, sn_free, sn_not_calm, all §2 setting labels, sn_who_*, sn_note, sn_teacher_n.
> - Everyone re-copies `sn_pb` and `sn_teacher` (X05, X08, X09, X10, X12, X20, T01, W00 — wherever they were copied) and the §5 keys (X10).

> **CHANGE NOTE — v3, 28 Oct 2026 (build pass 14, Exam & Admission Hub; family area):** new §6 — how hub reminders look when the mode is on
> (advance-notice style, brief: "advance-notice style when Sensory-friendly mode is on"). New 6-language keys `sn_hub` (rule line) and
> `sn_hub_ex` (sample reminder, Tanvir's General Maths paper Tue 16 Mar 2027, 10:00 am = sample time). Nothing else changed; the v2 note above still applies.
> Copied by X08 (guardian hub copy, Reminders tab) and G01 (static frame; v4: `sn_hub` only); learner boards with hub reminders (X07/X01) may copy the same two keys.

> **CHANGE NOTE — v4, 28 Oct 2026 (fix pass 15, R14-family-8 + decision J4; family area):**
> - **R14-family-8.** `sn_hub_ex` now starts with an example label in every language (en "Example: in 3 days …", bn "উদাহরণ: …", hi "उदाहरण: …",
>   ur "مثال: …", ar "مثال: …", fr "Exemple : dans 3 jours …") so the sample is not read as a real reminder on a screen dated Mon 1 Feb 2027.
>   X08 re-copies it. G01 (static frame G2c) copies `sn_hub` only (under the 9 pm line); `sn_hub_ex` is shown on X08 only.
> - **J4.** The mode's name is ONLY `sn_name` in every language (ur «حسّی دوستانہ موڈ», ar «الوضع الملائم للحواس», fr «Mode sensoriel adapté»;
>   chip = `sn_short`). Any other spelling (e.g. ur «حسی دوست موڈ», ar «الوضع الملائم حسيًا») is wrong wherever it appears — hub.md f24_d, X07, X10 and
>   every copy use these strings. No other key changed.

(v1 was written by family in fix11, 27 Oct 2026 00:50.)

Single source for every board (X01–X23, L/D/G/P statics, X10 admin row, X20 landing). Copy the strings EXACTLY.
Source: owner 27 Oct 2026 ("Eta shobar jonnoi hobe") via SP/s2/fix11/shared/sensory_brief.md; memory /areas/nexatute-playboom.md
("calm mode for autism/speech delay — soft colours, no sudden sounds, picture routine; guardian turns on") + /areas/nexatute-learning.md 27 Oct:
the mode is now for everyone — all ages, classes and courses.
Name: en "Sensory-friendly mode". It is NOT the rank-hiding "Calm mode" (X08/X02: hides batch rank, merit lists and leaderboards before exams) —
the two names must never be swapped. PlayBoom's mode for autism/speech delay (X05) IS this mode and uses this name (sn_name) — never a localized "calm" word; PlayBoom shows the sn_pb line.
Register: neutral (no তুমি/আপনি, tum/aap, tu/vous) so learner, guardian, teacher and admin boards can all copy it. sn_teacher / sn_teacher_n speak to the
teacher (bn আপনি-free wording, hi/ur polite imperative, ar أنت, fr vous).
Latin digits; in ur/ar the Latin words and digits ("18", "5", "Calm mode", "PlayBoom") are wrapped in LTR isolation (M() or ⁦…⁩) — the visible text
stays identical; ur/ar arrows point right-to-left (←). No medical or cure claims anywhere; no diagnosis is asked or stored; never shown to other
learners, guardians or teachers (a teacher only sees that the class uses the quieter screen, never who).

## 1. Name, chip and one-line description

| key | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| sn_name | Sensory-friendly mode | সংবেদন-বান্ধব মোড | संवेदी-अनुकूल मोड | حسّی دوستانہ موڈ | الوضع الملائم للحواس | Mode sensoriel adapté |
| sn_short (chip) | Sensory-friendly | সংবেদন-বান্ধব | संवेदी-अनुकूल | حسّی دوستانہ | ملائم للحواس | Sensoriel adapté |
| sn_desc | Soft colours, no sudden sounds, a picture routine and notice before changes — for every age, class and course | নরম রং, হঠাৎ কোনো শব্দ নেই, ছবিতে রুটিন আর কিছু বদলানোর আগে জানানো — সব বয়স, সব ক্লাস আর সব কোর্সের জন্য | हल्के रंग, अचानक कोई आवाज़ नहीं, तस्वीरों में दिनचर्या और बदलाव से पहले सूचना — हर उम्र, हर क्लास और हर कोर्स के लिए | ہلکے رنگ، اچانک کوئی آواز نہیں، تصویروں میں روزمرہ اور تبدیلی سے پہلے اطلاع — ہر عمر، ہر کلاس اور ہر کورس کے لیے | ألوان هادئة، بلا أصوات مفاجئة، روتين بالصور وتنبيه قبل أي تغيير — لكل الأعمار والصفوف والدورات | Couleurs douces, aucun son soudain, une routine en images et un préavis avant chaque changement — pour tous les âges, toutes les classes et tous les cours |
| sn_free | No extra price — included in every plan | বাড়তি দাম নেই — প্রতিটি প্ল্যানে আছে | कोई अतिरिक्त कीमत नहीं — हर प्लान में शामिल | کوئی اضافی قیمت نہیں — ہر پلان میں شامل | بلا سعر إضافي — مُتاح في كل خطة | Sans supplément — inclus dans chaque formule |
| sn_not_calm | Not the same as Calm mode, which hides ranks before exams | Calm mode থেকে আলাদা — Calm mode পরীক্ষার আগে র‍্যাঙ্ক লুকায় | Calm mode से अलग — Calm mode परीक्षा से पहले रैंक छिपाता है | ⁦Calm mode⁩ سے مختلف — ⁦Calm mode⁩ امتحان سے پہلے رینک چھپاتا ہے | يختلف عن ⁦Calm mode⁩ الذي يخفي الترتيب قبل الامتحانات | À ne pas confondre avec le Calm mode, qui masque les classements avant les examens |
| sn_pb (PlayBoom only) | In PlayBoom it is the same Sensory-friendly mode | PlayBoom-এও এটি একই সংবেদন-বান্ধব মোড | PlayBoom में भी यही संवेदी-अनुकूल मोड है | ⁦PlayBoom⁩ میں بھی یہی حسّی دوستانہ موڈ ہے | في ⁦PlayBoom⁩ هو الوضع الملائم للحواس نفسه | Dans PlayBoom, c’est le même Mode sensoriel adapté |

## 2. Setting labels (switches or a checklist under the mode; all on by default when the mode is on, each can be turned off)

| key | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| sn_soft | Soft colours | নরম রং | हल्के रंग | ہلکے رنگ | ألوان هادئة | Couleurs douces |
| sn_quiet | No sudden sounds | হঠাৎ কোনো শব্দ নেই | अचानक कोई आवाज़ नहीं | اچانک کوئی آواز نہیں | بلا أصوات مفاجئة | Aucun son soudain |
| sn_still | No automatic animations | নিজে থেকে কোনো অ্যানিমেশন নেই | अपने-आप चलने वाले एनिमेशन नहीं | خودکار اینیمیشن نہیں | بلا رسوم متحركة تلقائية | Pas d’animation automatique |
| sn_routine | Visual routine board | ছবিতে রুটিন বোর্ড | तस्वीरों वाला रूटीन बोर्ड | تصویری روٹین بورڈ | لوحة روتين مصوّرة | Tableau de routine en images |
| sn_notice | Advance notice before changes | কিছু বদলানোর আগে জানানো | बदलाव से पहले सूचना | تبدیلی سے پہلے اطلاع | تنبيه مسبق قبل التغيير | Préavis avant un changement |
| sn_one | One instruction at a time | একবারে একটি নির্দেশ | एक बार में एक निर्देश | ایک وقت میں ایک ہدایت | تعليمة واحدة في كل مرة | Une consigne à la fois |
| sn_time | Longer answer time | উত্তর দিতে বেশি সময় | जवाब के लिए ज़्यादा समय | جواب کے لیے زیادہ وقت | وقت أطول للإجابة | Plus de temps pour répondre |
| sn_fewer | Fewer items on each screen | প্রতি স্ক্রিনে কম জিনিস | हर स्क्रीन पर कम चीज़ें | ہر اسکرین پر کم چیزیں | عناصر أقل في كل شاشة | Moins d’éléments par écran |
| sn_audio | Class audio without chimes | ক্লাসের অডিওতে কোনো ঘণ্টাধ্বনি নেই | क्लास ऑडियो में घंटी की आवाज़ नहीं | کلاس آڈیو میں گھنٹی کی آواز نہیں | صوت الحصة بلا رنين | Audio du cours sans carillon |
| sn_routine_ex (routine board sample) | Today: class → break → practice | আজ: ক্লাস → বিরতি → অনুশীলন | आज: क्लास → ब्रेक → अभ्यास | آج: کلاس ← وقفہ ← مشق | اليوم: حصة ← استراحة ← تدريب | Aujourd’hui : cours → pause → exercices |
| sn_notice_ex (advance-notice sample) | Class ends in 5 minutes | ক্লাস 5 মিনিটে শেষ হবে | क्लास 5 मिनट में ख़त्म होगी | کلاس ⁦5⁩ منٹ میں ختم ہوگی | تنتهي الحصة بعد ⁦5⁩ دقائق | Le cours se termine dans 5 minutes |

Older learners get the same switches; the routine board becomes the day's schedule, and the quiet UI keeps fewer items per screen.
The mode respects the browser's prefers-reduced-motion and works together with the dyslexia / ADHD / extra-time settings (G2: public name, never "slow-learner") and the BdSL avatar.
Text contrast stays at least 4.5:1 with the soft colours.

## 3. Who turns it on, and the privacy note

| key | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| sn_who_u18 | Under 18: a guardian turns it on — the learner can ask for it | 18 বছরের কম হলে অভিভাবক চালু করেন — শিক্ষার্থী চাইতে পারে | 18 साल से कम: अभिभावक चालू करते हैं — विद्यार्थी माँग सकता है | ⁦18⁩ سال سے کم: سرپرست آن کرتے ہیں — طالب علم درخواست کر سکتا ہے | دون ⁦18⁩ سنة: وليّ الأمر يفعّله — ويمكن للمتعلّم أن يطلبه | Moins de 18 ans : un parent l’active — l’élève peut le demander |
| sn_who_adult | Adults turn it on themselves | প্রাপ্তবয়স্করা নিজেই চালু করেন | वयस्क ख़ुद चालू करते हैं | بالغ خود آن کرتے ہیں | البالغون يفعّلونه بأنفسهم | Les adultes l’activent eux-mêmes |
| sn_who_inst | An institution can turn it on for a class — each learner’s guardian consents first | প্রতিষ্ঠান একটি ক্লাসের জন্য চালু করতে পারে — আগে প্রত্যেক শিক্ষার্থীর অভিভাবকের সম্মতি লাগে | संस्थान किसी क्लास के लिए चालू कर सकता है — पहले हर विद्यार्थी के अभिभावक की सहमति | ادارہ کسی کلاس کے لیے آن کر سکتا ہے — پہلے ہر طالب علم کے سرپرست کی رضامندی | يمكن للمؤسسة تفعيله لصف كامل — بعد موافقة وليّ أمر كل متعلّم | Un établissement peut l’activer pour une classe — avec d’abord l’accord du parent de chaque élève |
| sn_note | A preference, not a label — no diagnosis is asked for or stored, and no one else sees it. | এটি একটি পছন্দ, কোনো তকমা নয় — কোনো রোগনির্ণয় চাওয়া বা রাখা হয় না, আর অন্য কেউ দেখতে পায় না। | यह एक पसंद है, कोई ठप्पा नहीं — कोई निदान न पूछा जाता है न रखा जाता है, और कोई और इसे नहीं देखता। | یہ ایک پسند ہے، کوئی لیبل نہیں — نہ کوئی تشخیص پوچھی جاتی ہے نہ محفوظ کی جاتی ہے، اور کوئی اور اسے نہیں دیکھتا۔ | إنه تفضيل لا تصنيف — لا يُطلب أي تشخيص ولا يُحفَظ، ولا يظهر لأحد آخر. | Une préférence, pas une étiquette — aucun diagnostic n’est demandé ni conservé, et personne d’autre ne le voit. |
| sn_setlog (note under the switch / settings-log entry; never the consent record) | Saved in the settings log — not a consent | সেটিং লগে রাখা হয় — এটি সম্মতি নয় | सेटिंग लॉग में दर्ज — यह सहमति नहीं है | سیٹنگ لاگ میں درج — یہ رضامندی نہیں | يُحفَظ في سجل الإعدادات — وليس موافقة | Enregistré dans le journal des réglages — pas un consentement |

Rule (v2, G6): the mode is a preference. Turning it on or off goes to the settings log (sn_setlog), never to the consent record, and is not
counted as a consent anywhere (X08, X15, G01).

## 4. Teacher view (X09 / T01): only that the class uses it — never who (v2: no "quieter/calm screen" wording)

| key | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| sn_teacher | This class uses Sensory-friendly mode — keep to the routine board and give notice before changes | এই ক্লাসে সংবেদন-বান্ধব মোড চালু — রুটিন বোর্ড মেনে চলা আর কিছু বদলানোর আগে জানানো | इस क्लास में संवेदी-अनुकूल मोड चालू है — रूटीन बोर्ड के अनुसार चलें और बदलाव से पहले बताएँ | اس کلاس میں حسّی دوستانہ موڈ آن ہے — روٹین بورڈ پر چلیں اور تبدیلی سے پہلے بتائیں | هذا الصف يستخدم الوضع الملائم للحواس — التزم بلوحة الروتين ونبّه قبل أي تغيير | Cette classe utilise le Mode sensoriel adapté — suivez le tableau de routine et prévenez avant tout changement |
| sn_teacher_n | No names — you only see that the class uses it | কোনো নাম নেই — শুধু দেখা যায় ক্লাসটি এটি ব্যবহার করে | कोई नाम नहीं — आपको सिर्फ़ यह दिखता है कि क्लास इसे इस्तेमाल करती है | کوئی نام نہیں — آپ کو صرف یہ دکھتا ہے کہ کلاس اسے استعمال کرتی ہے | بلا أسماء — ترى فقط أن الصف يستخدمه | Aucun nom — vous voyez seulement que la classe l’utilise |

## 5. Admin (X10 Plans & modules) — for admin agents (v2, G3: ON and LOCKED in every plan)

Control row: name = sn_name, value = sn_adm_val. The per-plan cells are ON and LOCKED (lock icon, not clickable) with the chip sn_adm_req and the
tooltip sn_adm_lock. Editable: ONLY the platform-wide switch and the default settings (which §2 settings start on, how much longer the answer time
is — no number is set here; an admin board that shows one marks it "(default)"). No price line, no per-plan switch to remove it.

| key | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| sn_adm_val | On and locked in every plan · no extra price | প্রতিটি প্ল্যানে চালু ও লক করা · বাড়তি দাম নেই | हर प्लान में चालू और लॉक · कोई अतिरिक्त कीमत नहीं | ہر پلان میں آن اور لاک · کوئی اضافی قیمت نہیں | مفعّل ومقفل في كل خطة · بلا سعر إضافي | Activé et verrouillé dans chaque formule · sans supplément |
| sn_adm_req | Required by policy | নীতিমালা অনুযায়ী বাধ্যতামূলক | नीति के अनुसार ज़रूरी | پالیسی کے تحت لازمی | مطلوب بموجب السياسة | Requis par la politique |
| sn_adm_lock | Required by policy — Sensory-friendly mode stays on in every plan. Only the platform-wide switch and the default settings can be changed. | নীতিমালা অনুযায়ী বাধ্যতামূলক — সংবেদন-বান্ধব মোড প্রতিটি প্ল্যানে চালু থাকে। শুধু প্ল্যাটফর্ম-জুড়ে সুইচ আর ডিফল্ট সেটিং বদলানো যায়। | नीति के अनुसार ज़रूरी — संवेदी-अनुकूल मोड हर प्लान में चालू रहता है। सिर्फ़ पूरे प्लेटफ़ॉर्म का स्विच और डिफ़ॉल्ट सेटिंग बदली जा सकती हैं। | پالیسی کے تحت لازمی — حسّی دوستانہ موڈ ہر پلان میں آن رہتا ہے۔ صرف پورے پلیٹ فارم کا سوئچ اور ڈیفالٹ سیٹنگز بدلی جا سکتی ہیں۔ | مطلوب بموجب السياسة — يبقى الوضع الملائم للحواس مفعّلًا في كل خطة. يمكن تغيير المفتاح العام للمنصة والإعدادات الافتراضية فقط. | Requis par la politique — le Mode sensoriel adapté reste activé dans chaque formule. Seuls l’interrupteur global de la plateforme et les réglages par défaut peuvent être modifiés. |

## 6. Exam & Admission Hub reminders (v3, fix14) — advance-notice style when the mode is on

With the mode on, hub reminders (deadlines, exam days, date changes) arrive early and always in the same order — what, when, what stays the
same — with no sudden alarm sound; "date changed" alerts still show old → new. Quiet hours and the under-18 "nothing after 9 pm" rule are unchanged.

| key | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| sn_hub | With Sensory-friendly mode on, exam and deadline reminders come early and always in the same order: what will happen, when, and what stays the same — no sudden alarms | সংবেদন-বান্ধব মোড চালু থাকলে পরীক্ষা ও শেষ তারিখের রিমাইন্ডার আগেভাগে আর সবসময় একই ক্রমে আসে: কী হবে, কখন, আর কী একই থাকছে — হঠাৎ কোনো অ্যালার্ম নয় | संवेदी-अनुकूल मोड चालू होने पर परीक्षा और आख़िरी तारीख़ के रिमाइंडर पहले से और हमेशा एक ही क्रम में आते हैं: क्या होगा, कब, और क्या वैसा ही रहेगा — कोई अचानक अलार्म नहीं | حسّی دوستانہ موڈ آن ہو تو امتحان اور آخری تاریخ کی یاددہانیاں پہلے سے اور ہمیشہ ایک ہی ترتیب میں آتی ہیں: کیا ہوگا، کب، اور کیا ویسا ہی رہے گا — کوئی اچانک الارم نہیں | عند تشغيل الوضع الملائم للحواس تصل تذكيرات الامتحانات والمواعيد النهائية مبكرًا وبالترتيب نفسه دائمًا: ماذا سيحدث، ومتى، وما الذي سيبقى كما هو — بلا تنبيهات مفاجئة | Avec le Mode sensoriel adapté, les rappels d’examen et d’échéance arrivent tôt et toujours dans le même ordre : ce qui va se passer, quand, et ce qui ne change pas — aucune alarme soudaine |
| sn_hub_ex (sample — always shown with its example label) | Example: in 3 days (Tue 16 Mar): General Maths paper, 10:00 am, same centre — nothing else changes | উদাহরণ: 3 দিন পরে (মঙ্গলবার, 16 মার্চ): সাধারণ গণিত পরীক্ষা, সকাল 10:00, একই কেন্দ্র — আর কিছু বদলাচ্ছে না | उदाहरण: 3 दिन बाद (मंगलवार, 16 मार्च): सामान्य गणित का पेपर, सुबह 10:00, वही केंद्र — और कुछ नहीं बदल रहा | مثال: ⁦3⁩ دن بعد (منگل، ⁦16⁩ مارچ): جنرل میتھس کا پرچہ، صبح ⁦10:00⁩، وہی سینٹر — اور کچھ نہیں بدل رہا | مثال: بعد ⁦3⁩ أيام (الثلاثاء ⁦16⁩ مارس): ورقة الرياضيات العامة، الساعة ⁦10:00⁩ صباحًا، المركز نفسه — لا شيء آخر يتغيّر | Exemple : dans 3 jours (mardi 16 mars) : épreuve de mathématiques générales, 10 h 00, même centre — rien d’autre ne change |

## Changelog
- v1 (27 Oct 00:50, family): first version from sensory_brief.md.
- v2 (27 Oct 2026, fix12, family): G1 — sn_pb and sn_teacher rewritten without any localized "calm" word, X05 uses sn_name; G3 — §5 ON and locked in every plan (sn_adm_val, sn_adm_req, sn_adm_lock); G2 — "extra-time settings"; G6 — sn_setlog, settings log not consent record.
- v3 (28 Oct 2026, fix14, family): §6 hub reminders in advance-notice style (sn_hub, sn_hub_ex).
- v4 (28 Oct 2026, fix15, family): R14-family-8 — sn_hub_ex carries an example label in 6 languages; G01 copies sn_hub only; J4 — sn_name is the only name of the mode in every language.

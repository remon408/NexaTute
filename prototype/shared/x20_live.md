# E2 — X20 live site facts (fix9, site agent, 26 Oct 2026; fix16 update 28 Oct 2026 — v45, see §9; fix17 update 28 Oct 2026 — redesign, still v45, see §10; fix18 update 28 Oct 2026 — Free-Beta safety items, still v45, see §11; fix18f–l update 29 Oct 2026 — storage, status page, Team Quest, 2027 features, free vs paid, roadmap, WhatsApp/Messenger FAQ, still v45, see §12; F19 final check 29 Oct 2026 — Game Show day, still v45, see §13; fix20 update 29 Oct 2026 — legal pages moved to the new board X24 + page “Report a security problem”, still v45, see §14; fix21 update 29 Oct 2026 — waiting list + admissions closed (prototype switches), still v45, see §15)

X20 now opens in the POST-LAUNCH state by default: the demo date is Mon 1 Feb 2027 (D1).
X13 (live-page preview + version list) and X17 (page builder / AI CMS home entry) mirror these
facts EXACTLY. The values below were taken from X13's current preview (`lp.*`) so X13 should
already match for the hero; the version list and the v39 text change (see §2).

Prototype states kept in X20 (admin preview → "Prototype state"): 
- `live` (default) — 1 Feb 2027, v45 live (fix16: v45 published Mon 1 Feb 2027 after v44 the same day; v43 was live 31 Jan – 1 Feb)
- `beta` — the pre-launch snapshot of 26 Oct 2026 (Free Beta 20 Nov – 9 Dec 2026 sign-up, October banner),
  with its own version numbers v27–v31 (v31 published 24 Oct 2026), so v39–v43 always mean January 2027
- `beta` + "Beta full" switch — the Free Beta waiting room (number 214 in line)

All 6 site languages (bn, en, hi, ur, ar, fr) went live at launch — no version entry publishes a language.

## 1. Live version

- Live version: **v45**, published **1 February 2027** (fix16, build pass 16), approved by the marketing admin on 1 February 2027
  (proposal drafted by the AI, `by: 'ai'`). Before it: v44, published the same day (fix14); v43, published 31 January 2027.
- Status line (admin): en "Status: live — the site runs version v45, published 1 February 2027." (6 languages in §9)
- After-publish watch: the 24–48 h auto-rollback check now runs for v45 (published 1 Feb 2027) — it was v44's in fix14/fix15.

## 2. Version list (newest last) — X13 `versions` and X17 `vers` use exactly these dates

| v | date | by | en text |
|---|---|---|---|
| v39 | 2027-01-09 | ai | PlayBoom section: paid from 21 January 2027 (its Free Beta ran 1–20 January) |
| v40 | 2027-01-16 | admin | 4 new questions in the FAQ |
| v41 | 2027-01-23 | ai | February: model-test campaign banner |
| v42 | 2027-01-26 | ai | New layout for the plans section |
| v43 | 2027-01-31 | ai | Positioning line under the headline; Learning guarantee in the plans, FAQ and refund policy; autism-support section with Sensory-friendly mode (also in “Every plan includes”); “Every class in Bangla Sign Language”; class-recording choice in the FAQ; Learning Atlas teaser |
| v44 | 2027-02-01 | ai | Exam & Admission Hub teaser (calendar, eligibility checker, deadline alerts — free for everyone) and a new FAQ entry |
| v45 | 2027-02-01 | ai | Fuller sections: weak-internet card, Free Beta results card, guardian reminders, help card beside the FAQ; 2 new FAQ entries (weak internet, old phones and accessibility); 12 new legal pages as drafts for lawyer/DPO approval; Learning guarantee terms; five date statuses and the “not an official service” note in the hub teaser |

v39 REPLACES the old "Hindi, Urdu, Arabic and French pages live" (E2: no later language publish dates).
v43 REPLACES the old "Country & syllabus picker; currency follows where you live; legal pages linked":
the picker and the legal-page links were approved on 24 Oct 2026 and were already on the site before
launch (R9-admin-13), so they are no longer a January 2027 version. v40, v41, v42 keep X13's texts.
X13's `vc.v43` (long change description) should say the same as the v43 text below.
fix14 (28 Oct 2026, site): the v43 line now names the four additions that were live in v43 (fix11–fix13: autism-support section with
Sensory-friendly mode, "Every class in Bangla Sign Language", class-recording choice in the FAQ, Learning Atlas teaser) — the exact X13 `vt.v43` /
X17 `vt.h15` text in 6 languages, so X20's admin preview, X13 and X17 say the same.

v39 in the other languages:
- bn: PlayBoom সেকশন: পেইড 21 জানুয়ারি 2027 থেকে (এর Free Beta চলেছিল 1–20 জানুয়ারি)
- hi: PlayBoom सेक्शन: पेड 21 जनवरी 2027 से (इसका Free Beta 1–20 जनवरी चला)
- ur: PlayBoom سیکشن: پیڈ 21 جنوری 2027 سے (اس کا Free Beta 1–20 جنوری چلا)
- ar: قسم PlayBoom: مدفوع منذ 21 يناير 2027 (جرت Free Beta الخاصة به من 1 إلى 20 يناير)
- fr: Section PlayBoom : payante depuis le 21 janvier 2027 (sa Free Beta a eu lieu du 1er au 20 janvier)

v43 in the other languages:
- bn: হেডলাইনের নিচে পজিশনিং লাইন; প্ল্যান, FAQ আর রিফান্ড নীতিতে শেখার নিশ্চয়তা; সংবেদন-বান্ধব মোডসহ অটিজম সহায়তার সেকশন (“প্রতিটি প্ল্যানে থাকছে”-তেও); “প্রতিটি ক্লাস বাংলা সাংকেতিক ভাষায়”; FAQ-তে ক্লাস রেকর্ডিং বেছে নেওয়ার নিয়ম; Learning Atlas-এর ঝলক
- hi: हेडलाइन के नीचे पोज़िशनिंग लाइन; प्लान, FAQ और रिफ़ंड नीति में सीखने की गारंटी; संवेदी-अनुकूल मोड के साथ ऑटिज़्म सहायता सेक्शन (“हर प्लान में शामिल” में भी); “हर क्लास बांग्ला सांकेतिक भाषा में”; FAQ में क्लास रिकॉर्डिंग का विकल्प; Learning Atlas की झलक
- ur: سرخی کے نیچے پوزیشننگ لائن؛ پلانز، FAQ اور ریفنڈ پالیسی میں سیکھنے کی ضمانت؛ حسّی دوستانہ موڈ کے ساتھ آٹزم معاونت کا سیکشن (“ہر پلان میں شامل” میں بھی)؛ “ہر کلاس بنگلہ اشاروں کی زبان میں”؛ FAQ میں کلاس ریکارڈنگ کا انتخاب؛ ⁦Learning Atlas⁩ کی جھلک
- ar: سطر التموضع تحت العنوان؛ ضمان التعلّم في الخطط والأسئلة الشائعة وسياسة الاسترداد؛ قسم دعم التوحد مع الوضع الملائم للحواس (وفي «تتضمن كل خطة» أيضًا)؛ «كل حصة بلغة الإشارة البنغالية»؛ خيار تسجيل الحصص في الأسئلة الشائعة؛ لمحة عن ⁦Learning Atlas⁩
- fr: Ligne de positionnement sous le titre ; Garantie d’apprentissage dans les formules, la FAQ et la politique de remboursement ; section Autisme avec le Mode sensoriel adapté (aussi dans « Chaque formule comprend ») ; « Chaque cours en langue des signes bangladaise » ; choix d’enregistrer les cours dans la FAQ ; aperçu du Learning Atlas

X20 admin chips (live state) per section: hero "Last change v43", announcement bar "Last change v41 · Ends 28 February 2027",
plans "Last change v43" (guarantee line; v42 = layout), FAQ "Last change v44" (fix14: hub question; v43 = guarantee entry; v40 = 4 questions),
hub teaser (new section between the courses and the plans) "Last change v44" + note "Sample dates only — the hub in the app reads reviewer-approved circulars (X16)",
PlayBoom "Last change v39", footer: no change since launch.

## 3. Hero, CTA, banner, pill (6 languages, identical to X13 `lp.*`)

| key | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| headline (h1) | AI tutor, real learning | AI টিউটর, সত্যিকারের শেখা | AI ट्यूटर, सच्ची पढ़ाई | AI ٹیوٹر، حقیقی سیکھنا | مدرّس خصوصي بالذكاء الاصطناعي، وتعلّم حقيقي | Un tuteur IA, un vrai apprentissage |
| main CTA | Start the 7-day Free Trial | 7 দিনের Free Trial শুরু করো | 7 दिन का Free Trial शुरू करें | 7 دن کا Free Trial شروع کریں | ابدأ Free Trial لمدة 7 أيام | Commencer le Free Trial de 7 jours |
| 2nd CTA | Try the live demo | লাইভ ডেমো চেষ্টা করো | लाइव डेमो आज़माएँ | لائیو ڈیمو آزمائیں | جرّب العرض المباشر | Essayer la démo |
| pill | Paid plans since 1 January 2027 · 7-day Free Trial | পেইড প্ল্যান 1 জানুয়ারি 2027 থেকে · 7 দিনের Free Trial | पेड प्लान 1 जनवरी 2027 से · 7 दिन का Free Trial | پیڈ پلان 1 جنوری 2027 سے · 7 دن کا Free Trial | الخطط المدفوعة منذ 1 يناير 2027 · Free Trial لمدة 7 أيام | Offres payantes depuis le 1er janvier 2027 · Free Trial de 7 jours |
| banner (announcement bar) | The February model-test campaign runs until 28 February 2027. | ফেব্রুয়ারির মডেল টেস্ট ক্যাম্পেইন চলছে 28 ফেব্রুয়ারি 2027 পর্যন্ত। | फ़रवरी का मॉडल टेस्ट कैंपेन 28 फ़रवरी 2027 तक चल रहा है। | فروری کی ماڈل ٹیسٹ مہم 28 فروری 2027 تک جاری ہے۔ | حملة الاختبارات النموذجية لشهر فبراير مستمرة حتى 28 فبراير 2027. | La campagne de tests blancs de février se poursuit jusqu’au 28 février 2027. |
| banner link | See the campaign | ক্যাম্পেইন দেখো | कैंपेन देखें | مہم دیکھیں | شاهد الحملة | Voir la campagne |

The banner ends on 28 Feb 2027 and then removes itself (admin chip "Ends 28 February 2027").
(ur/ar: the digits are wrapped in LTR isolation, e.g. M('1') — visible text identical.)

## 4. Positioning line (hero sub-line under the h1, footer; institutions variant)

| lang | hero / footer | institutions |
|---|---|---|
| en | An AI-Powered Learning Operating System | One AI-Powered Learning Operating System for your whole institution |
| bn | একটি AI-চালিত লার্নিং অপারেটিং সিস্টেম | আপনার পুরো প্রতিষ্ঠানের জন্য একটি AI-চালিত লার্নিং অপারেটিং সিস্টেম |
| hi | एक AI-संचालित लर्निंग ऑपरेटिंग सिस्टम | आपके पूरे संस्थान के लिए एक AI-संचालित लर्निंग ऑपरेटिंग सिस्टम |
| ur | ایک AI سے چلنے والا لرننگ آپریٹنگ سسٹم | آپ کے پورے ادارے کے لیے ایک AI سے چلنے والا لرننگ آپریٹنگ سسٹم |
| ar | نظام تشغيل للتعلّم مدعوم بالذكاء الاصطناعي | نظام تشغيل واحد للتعلّم مدعوم بالذكاء الاصطناعي لمؤسستك كلّها |
| fr | Un système d’exploitation de l’apprentissage propulsé par l’IA | Un seul système d’exploitation de l’apprentissage, propulsé par l’IA, pour tout votre établissement |

## 5. Guarantee line

Plans section, FAQ and refund page show the E1 Learning guarantee exactly as in
SP/s2/fix9/shared/guarantee.md §4 + the terms line §5. Live in v43 with the lawyer tag; the full
terms are still with the lawyer (admin chip: "Live · full terms waiting for the lawyer").

## 6. Other live-state facts on X20 (for consistency, not for X13/X17 to copy)

- Free Beta (20 Nov – 9 Dec 2026) is over and shown as past; no live seat counter; no "Join the Free Beta" button anywhere
  (and no A/B test on it — E4).
- Sign-up = 7-day Free Trial, 15 min a day of 1:1 (memory); Daily Pass, plans and prices unchanged.
- PlayBoom: Free Beta 1–20 Jan 2027 (past), paid since 21 Jan 2027.
- Pending proposals shown in the admin preview: #1 "HSC Head Start — banner and headline", #2 "New FAQ: does it work on slow internet?" (same as X13).
- Nexa Notes video post "SSC maths: factorisation in 6 minutes" (made with Remon Motion Studio) is dated 1 February 2027,
  the same as X17 `vd1.pub`; it does not exist in the 26 Oct 2026 `beta` snapshot.
- Footer: "© 2027 RemonLogic Private Limited".

## 7. v44 — Exam & Admission Hub teaser (fix14, site, 28 Oct 2026)

X13 (version list + live-page preview) and X17 (page builder `vers`) add this line exactly; the X20 admin preview shows it.
v44 | 2027-02-01 | by ai | approved by the marketing admin 1 Feb 2027. Content: a compact free "Exam & Admission Hub" section on the live home page
between the courses and the plans (hub name, hub_tag and the free / paid chips from SP/s2/fix14/shared/hub.md; Calendar & alert sync, Eligibility checker,
"Date changed" alerts; also-free and paid-plan lists; a calendar preview of 5 SSC 2027 sample events with status badges, sample marker, source and
last verified; privacy note: masked IDs, NexaTute never takes the fee, no reminders to under-18 after 9 pm, Calm mode; CTA "Use the hub free"),
a footer link, and FAQ entry 15 "What is the Exam & Admission Hub, and is it free?" (last in the FAQ). Not in the 26 Oct 2026 `beta` snapshot.
On the X20 page the live English-medium Class 4–5 / 6–8 courses and the crash-program line in the Add-ons box are price-table changes (no version text).

| lang | v44 (version list text) | status line |
|---|---|---|
| bn | পরীক্ষা ও ভর্তি হাবের ঝলক (ক্যালেন্ডার, যোগ্যতা যাচাই, শেষ তারিখের সতর্কবার্তা — সবার জন্য ফ্রি) আর FAQ-তে নতুন প্রশ্ন | অবস্থা: লাইভ — সাইটে চলছে ভার্সন v44, প্রকাশিত 1 ফেব্রুয়ারি 2027। |
| en | Exam & Admission Hub teaser (calendar, eligibility checker, deadline alerts — free for everyone) and a new FAQ entry | Status: live — the site runs version v44, published 1 February 2027. |
| hi | परीक्षा और प्रवेश हब की झलक (कैलेंडर, पात्रता जाँच, आख़िरी तारीख़ के अलर्ट — सबके लिए मुफ़्त) और FAQ में नया सवाल | स्थिति: लाइव — साइट पर संस्करण v44 चल रहा है, 1 फ़रवरी 2027 को प्रकाशित। |
| ur | امتحان اور داخلہ ہب کی جھلک (کیلنڈر، اہلیت چیکر، آخری تاریخ کے الرٹ — سب کے لیے مفت) اور FAQ میں نیا سوال | حیثیت: لائیو — سائٹ پر ورژن v44 چل رہا ہے، 1 فروری 2027 کو شائع ہوا۔ |
| ar | لمحة عن مركز الامتحانات والقبول (التقويم، فاحص الأهلية، تنبيهات المواعيد النهائية — مجاني للجميع) وسؤال جديد في الأسئلة الشائعة | الحالة: مباشر — يعمل الموقع بالإصدار v44، المنشور في 1 فبراير 2027. |
| fr | Aperçu du Hub examens & admissions (calendrier, vérificateur d’éligibilité, alertes d’échéance — gratuit pour tous) et nouvelle entrée de FAQ | Statut : en ligne — le site tourne sur la version v44, publiée le 1er février 2027. |

## 8. fix15 (site, 28 Oct 2026) — page fixes, no new version

**v44 stays the live version** (published 1 February 2027); X13 `versions` / X17 `vers` and the status line do not change. The fix15 changes on X20 are
layout / behaviour fixes and price-table values, so they carry no version text (same rule as the §7 last line):
- Header: below a 1060 px page width the sign-up button shows the short label (`cta_s`: en "Sign up", fr "S’inscrire" …) and never wraps (decision J7).
- "More ▾" and the language menu close on a click outside them and when keyboard focus leaves them.
- Hub teaser: only the SSC admit-card event (Thu 11 Feb → Sun 14 Feb) is styled as a "Date changed" alert; on phones the teaser shows 3 dates and a
  "Show 2 more dates" button, hides the "Also free" chips and puts the paid-plan list on one line. Texts stay verbatim hub.md.
- Add-ons, Exam Crash Pack tile: "(computed)" follows each computed crash-program price; abroad (USD) the 1/3/6-month prices are shown too, computed as
  the Taka price × 0.015, nearest dollar with .5 rounding down (decision J1, owner 28 Oct 2026, option ক): e.g. O-Level $18 / $32 (computed) / $58 (computed),
  Checkpoint $13 / $24 / $43. By the same rule the ৳900 Crash Pack (Checkpoint, University, Polytechnic) is $13 abroad (was $14).
- English-medium Class 6–8 abroad: Batch card shows "or one subject $6" (memory single $6 / $10).
- Touch targets ≥ 44 px on phones/tablets (Change-syllabus link, footer links, tooltip triggers).

## 9. fix16 (site, 28 Oct 2026) — v45, legal drafts, fuller sections

**v45** | 2027-02-01 | by ai | approved by the marketing admin 1 Feb 2027 (after v44 the same day). **X13** (`versions` + live-page preview + status line) and **X17** (page builder `vers`)
add v45 exactly (text + status line below) and drop pending proposal **#2 "New FAQ: does it work on slow internet?"** — it is published in v45 (live state: only #1
"HSC Head Start — banner and headline" stays pending). The 26 Oct 2026 `beta` snapshot is unchanged (v27–v31, its own proposals).
Admin chips on X20 (live): hero, plans, PlayBoom, MindForge, safety, proof, institutions, FAQ, hub and footer → "Last change v45".

| lang | v45 (version list text) | status line |
|---|---|---|
| bn | আরও ভরা সেকশন: দুর্বল ইন্টারনেটের কার্ড, Free Beta-র ফলের কার্ড, অভিভাবকের রিমাইন্ডার, FAQ-এর পাশে সাহায্যের কার্ড; FAQ-তে 2টি নতুন প্রশ্ন (দুর্বল ইন্টারনেট, পুরোনো ফোন ও প্রবেশযোগ্যতা); আইনজীবী/DPO-র অনুমোদনের জন্য 12টি নতুন আইনি পেজের খসড়া; শেখার নিশ্চয়তার শর্তাবলি; হাবের ঝলকে তারিখের পাঁচটি অবস্থা আর “অফিসিয়াল সেবা নয়” নোট | অবস্থা: লাইভ — সাইটে চলছে ভার্সন v45, প্রকাশিত 1 ফেব্রুয়ারি 2027। |
| en | Fuller sections: weak-internet card, Free Beta results card, guardian reminders, help card beside the FAQ; 2 new FAQ entries (weak internet, old phones and accessibility); 12 new legal pages as drafts for lawyer/DPO approval; Learning guarantee terms; five date statuses and the “not an official service” note in the hub teaser | Status: live — the site runs version v45, published 1 February 2027. |
| hi | भरे-पूरे सेक्शन: कमज़ोर इंटरनेट कार्ड, Free Beta नतीजों का कार्ड, अभिभावक रिमाइंडर, FAQ के पास सहायता कार्ड; FAQ में 2 नए सवाल (कमज़ोर इंटरनेट, पुराने फ़ोन और सुलभता); वकील/DPO की मंज़ूरी के लिए 12 नए क़ानूनी पेजों के मसौदे; सीखने की गारंटी की शर्तें; हब की झलक में तारीख़ की पाँच स्थितियाँ और “आधिकारिक सेवा नहीं” नोट | स्थिति: लाइव — साइट पर संस्करण v45 चल रहा है, 1 फ़रवरी 2027 को प्रकाशित। |
| ur | بھرے پُرے سیکشن: کمزور انٹرنیٹ کارڈ، ⁦Free Beta⁩ نتائج کا کارڈ، سرپرست کی یاد دہانیاں، ⁦FAQ⁩ کے ساتھ مدد کا کارڈ؛ ⁦FAQ⁩ میں ⁦2⁩ نئے سوال (کمزور انٹرنیٹ، پرانے فون اور رسائی)؛ وکیل/⁦DPO⁩ کی منظوری کے لیے ⁦12⁩ نئے قانونی صفحات کے مسودے؛ سیکھنے کی ضمانت کی شرائط؛ ہب کی جھلک میں تاریخ کی پانچ حیثیتیں اور “سرکاری سروس نہیں” نوٹ | حیثیت: لائیو — سائٹ پر ورژن ⁦v45⁩ چل رہا ہے، ⁦1⁩ فروری ⁦2027⁩ کو شائع ہوا۔ |
| ar | أقسام أكمل: بطاقة الإنترنت الضعيف، وبطاقة نتائج ⁦Free Beta⁩، وتذكيرات أولياء الأمور، وبطاقة مساعدة بجانب الأسئلة الشائعة؛ سؤالان جديدان في الأسئلة الشائعة (الإنترنت الضعيف، والهواتف القديمة وإمكانية الوصول)؛ ⁦12⁩ صفحة قانونية جديدة كمسودات بانتظار موافقة المحامي/⁦DPO⁩؛ شروط ضمان التعلّم؛ خمس حالات للتواريخ وملاحظة «ليست خدمة رسمية» في لمحة المركز | الحالة: مباشر — يعمل الموقع بالإصدار ⁦v45⁩، المنشور في ⁦1⁩ فبراير ⁦2027⁩. |
| fr | Sections plus complètes : carte internet faible, carte des résultats de la Free Beta, rappels aux parents, carte d’aide à côté de la FAQ ; 2 nouvelles questions dans la FAQ (internet faible, vieux téléphones et accessibilité) ; 12 nouvelles pages juridiques en projet pour approbation de l’avocat/du DPO ; Conditions de la garantie d’apprentissage; cinq statuts de date et la mention « pas un service officiel » dans l’aperçu du hub | Statut : en ligne — le site tourne sur la version v45, publiée le 1er février 2027. |

What v45 contains on X20 (owner 28 Oct 2026 12:00 "fill the empty spaces" — real approved content only, no invented numbers or reviews):
- Hero: the live demo now starts at the top of its column, with a "Works on weak internet" card under it (audio-only fallback on 2G/3G, lost minutes back,
  device/network check before class) and the chips "In every paid plan: Bangla Sign Language in every class · Sensory-friendly mode · Learning guarantee".
- Section headers (≥ 1181 px): heading left, lede right — no empty right half.
- Plans: "Every plan includes" + "Clear voice on weak internet"; a card under Free for life / Free Trial: in-app purchases on Google Play, Apple App Store and
  Microsoft Store show the plan price, a separate "App-store charge (30%)" line and the total (website prices have none); links to the Learning guarantee
  terms and Subscription terms next to the refund link; the guarantee terms line is guarantee.md v3 §5.
- Hub teaser (hub.md v1.4): five statuses (User-entered · Pending verification · Verified from official source · Updated by official notice · Unable to verify),
  the SSC admit-card event = Updated by official notice with its corrections line, "Published" dates, and the `not_off` note + link to the hub disclaimer.
  The teaser's 5 sample dates are now: SSC admit cards (upd) · SSC theory papers (ver) · General Maths (ver) · College (Class XI) admission (pend) ·
  SSC-based education board scholarship results, Mon 16 Aug 2027 (unab, note `ev17_note`) — HSC Head Start is no longer in the teaser; the old "Official · verified" label is retired.
- MindForge card button opens `X18-Prototype-MindForge.dc.html#mindforge` (X18 now opens on its dashboard).
- Proof: the dashed "no reviews yet" placeholder is replaced by a "Free Beta results: what we measure" card (live: being checked; beta: arriving January 2027),
  a 4th item "Connection-quality report", and a 6th standard "Personal data: built to Bangladesh’s Personal Data Protection Act 2026 …" (3 × 2 grid).
- Built for guardians: "Reminders that reach every guardian" card under the phone (in-app call / WhatsApp voice / push, SMS, licensed voice-call provider,
  phone-tutor hotline on a licensed IPTSP number — no "waiting for lawyer" label); "Your data, your rights" names the Personal Data Protection Act 2026.
- PlayBoom: 6th feature (NCTB books Class I–II); MindForge: solid puzzle card + "For families and schools" rows (guardian decides sharing, class summaries
  only with 5+ consenting learners, institution seats).
- Institutions: "For Cambridge and Pearson centres" band (private past-paper area, free, own students only) → Institution agreement & DPA.
- FAQ: 2 new questions on the live site — fq-15 "Does it work on weak internet?" and fq-16 "What if I have an old phone, little data or a disability?"
  (accessibility / low-internet; families without a smartphone get SMS or voice reminders and can call the phone-tutor hotline); live side cards
  "Policies at a glance" (6 legal links) and "What we build to".
- Footer: Legal spans two columns with all 18 pages (new drafts marked "draft"); App + Language stacked; App text names the three stores and the separate
  app-store charge line.

### 9a. Legal pages (18; 19 since fix20) — deep links for other boards

**fix20: the legal pages are on the board `X24-Prototype-Legal.dc.html`** (X20 had grown past the Design viewer's 2 MiB limit). Every page opens directly with `X24-Prototype-Legal.dc.html#legal/<id>` (also on `hashchange`); an old `X20-Prototype-Landing.dc.html#legal/<id>` link is forwarded to X24. Public URL pattern `nexatute.com/{lang}/legal/<id>`.
New pages are **v1.0 drafts for lawyer/DPO approval in both states** (badge "Draft — for lawyer/DPO approval", "not yet in force"); they are never shown as in force.
X13/X15 legal registers list the 12 new pages as drafts and the refund / data retention & deletion / accessibility pages as v1.1 drafts (live).

| key | en name | deep link | public URL | version |
|---|---|---|---|---|
| privacy | Privacy policy | `X24-Prototype-Legal.dc.html#legal/privacy` | nexatute.com/{lang}/legal/privacy | v2.5 draft (v2.4 in force) |
| terms | Terms of use | `X24-Prototype-Legal.dc.html#legal/terms` | nexatute.com/{lang}/legal/terms | v3.2 draft (v3.1 in force) |
| refund | Refund policy | `X24-Prototype-Legal.dc.html#legal/refund` | nexatute.com/{lang}/legal/refund | v1.1 draft (v1.0 in force since 1 Jan 2027) |
| deletion | Data retention & deletion | `X24-Prototype-Legal.dc.html#legal/data-deletion` | nexatute.com/{lang}/legal/data-deletion | v1.1 draft (v1.0 in force since 1 Jan 2027) |
| cookies | Cookie policy | `X24-Prototype-Legal.dc.html#legal/cookies` | nexatute.com/{lang}/legal/cookies | v1.0 in force since 1 Jan 2027 |
| access | Accessibility statement | `X24-Prototype-Legal.dc.html#legal/accessibility` | nexatute.com/{lang}/legal/accessibility | v1.1 draft (v1.0 in force since 1 Jan 2027) |
| consent | Child & guardian consent policy | `X24-Prototype-Legal.dc.html#legal/child-guardian-consent` | nexatute.com/{lang}/legal/child-guardian-consent | v1.0 draft for lawyer/DPO approval (new, 28 Oct 2026; never "in force" on the live site) |
| recording | Recording & class-report policy | `X24-Prototype-Legal.dc.html#legal/recording-class-reports` | nexatute.com/{lang}/legal/recording-class-reports | v1.0 draft for lawyer/DPO approval (new, 28 Oct 2026; never "in force" on the live site) |
| ai | AI transparency notice | `X24-Prototype-Legal.dc.html#legal/ai-transparency` | nexatute.com/{lang}/legal/ai-transparency | v1.0 draft for lawyer/DPO approval (new, 28 Oct 2026; never "in force" on the live site) |
| community | Community rules | `X24-Prototype-Legal.dc.html#legal/community-rules` | nexatute.com/{lang}/legal/community-rules | v1.0 draft for lawyer/DPO approval (new, 28 Oct 2026; never "in force" on the live site) |
| guarantee | Learning guarantee terms | `X24-Prototype-Legal.dc.html#legal/learning-guarantee` | nexatute.com/{lang}/legal/learning-guarantee | v1.0 draft for lawyer/DPO approval (new, 28 Oct 2026; never "in force" on the live site) |
| subscription | Subscription terms | `X24-Prototype-Legal.dc.html#legal/subscription-terms` | nexatute.com/{lang}/legal/subscription-terms | v1.0 draft for lawyer/DPO approval (new, 28 Oct 2026; never "in force" on the live site) |
| hubd | Exam & Admission Hub disclaimer | `X24-Prototype-Legal.dc.html#legal/exam-hub-disclaimer` | nexatute.com/{lang}/legal/exam-hub-disclaimer | v1.0 draft for lawyer/DPO approval (new, 28 Oct 2026; never "in force" on the live site) |
| institution | Institution agreement & DPA | `X24-Prototype-Legal.dc.html#legal/institution-agreement` | nexatute.com/{lang}/legal/institution-agreement | v1.0 draft for lawyer/DPO approval (new, 28 Oct 2026; never "in force" on the live site) |
| copyright | Copyright & takedown policy | `X24-Prototype-Legal.dc.html#legal/copyright-takedown` | nexatute.com/{lang}/legal/copyright-takedown | v1.0 draft for lawyer/DPO approval (new, 28 Oct 2026; never "in force" on the live site) |
| incident | Security incident response policy | `X24-Prototype-Legal.dc.html#legal/security-incidents` | nexatute.com/{lang}/legal/security-incidents | v1.0 draft for lawyer/DPO approval (new, 28 Oct 2026; never "in force" on the live site) |
| notify | Notification & communication policy | `X24-Prototype-Legal.dc.html#legal/notifications` | nexatute.com/{lang}/legal/notifications | v1.0 draft for lawyer/DPO approval (new, 28 Oct 2026; never "in force" on the live site) |
| complaints | Complaints & data-rights procedure | `X24-Prototype-Legal.dc.html#legal/complaints-data-rights` | nexatute.com/{lang}/legal/complaints-data-rights | v1.0 draft for lawyer/DPO approval (new, 28 Oct 2026; never "in force" on the live site) |
| disclosure | Report a security problem | `X24-Prototype-Legal.dc.html#legal/security-disclosure` | nexatute.com/{lang}/legal/security-disclosure | v1.0 draft for lawyer/DPO approval (new, fix20, 29 Oct 2026; never "in force" on the live site) — see §14 |

Names in 6 languages (the merged data page is renamed "Data retention & deletion"):

| key | bn | en | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| deletion | ডেটা সংরক্ষণ ও মুছে ফেলা | Data retention & deletion | डेटा रखना और मिटाना | ڈیٹا رکھنا اور مٹانا | الاحتفاظ بالبيانات وحذفها | Conservation et suppression des données |
| consent | শিশু ও অভিভাবকের সম্মতি নীতি | Child & guardian consent policy | बच्चे और अभिभावक की सहमति नीति | بچے اور سرپرست کی رضامندی کی پالیسی | سياسة موافقة الطفل ووليّ الأمر | Politique de consentement enfant et parent |
| recording | রেকর্ডিং ও ক্লাস রিপোর্ট নীতি | Recording & class-report policy | रिकॉर्डिंग और क्लास रिपोर्ट नीति | ریکارڈنگ اور کلاس رپورٹ کی پالیسی | سياسة التسجيل وتقارير الحصص | Politique d’enregistrement et de rapports de cours |
| ai | AI স্বচ্ছতা বিজ্ঞপ্তি | AI transparency notice | AI पारदर्शिता सूचना | AI شفافیت کا نوٹس | إشعار الشفافية في الذكاء الاصطناعي | Avis de transparence sur l’IA |
| community | কমিউনিটির নিয়ম | Community rules | समुदाय के नियम | کمیونٹی کے قواعد | قواعد المجتمع | Règles de la communauté |
| guarantee | শেখার নিশ্চয়তার শর্তাবলি | Learning guarantee terms | सीखने की गारंटी की शर्तें | سیکھنے کی ضمانت کی شرائط | شروط ضمان التعلّم | Conditions de la garantie d’apprentissage |
| subscription | সাবস্ক্রিপশনের শর্তাবলি | Subscription terms | सब्सक्रिप्शन की शर्तें | سبسکرپشن کی شرائط | شروط الاشتراك | Conditions d’abonnement |
| hubd | পরীক্ষা ও ভর্তি হাবের দায়মুক্তি | Exam & Admission Hub disclaimer | परीक्षा और प्रवेश हब अस्वीकरण | امتحان اور داخلہ ہب کا دستبرداری نوٹس | إخلاء مسؤولية مركز الامتحانات والقبول | Avertissement du Hub examens et admissions |
| institution | প্রতিষ্ঠান চুক্তি ও DPA | Institution agreement & DPA | संस्थान अनुबंध और DPA | ادارے کا معاہدہ اور DPA | اتفاقية المؤسسة وDPA | Contrat établissement et DPA |
| copyright | কপিরাইট ও অপসারণ নীতি | Copyright & takedown policy | कॉपीराइट और हटाने की नीति | کاپی رائٹ اور ہٹانے کی پالیسی | سياسة حقوق النشر والإزالة | Politique droit d’auteur et retrait |
| incident | নিরাপত্তা ঘটনা মোকাবিলা নীতি | Security incident response policy | सुरक्षा घटना प्रतिक्रिया नीति | سیکیورٹی واقعے پر ردعمل کی پالیسی | سياسة الاستجابة للحوادث الأمنية | Politique de réponse aux incidents de sécurité |
| notify | নোটিফিকেশন ও যোগাযোগ নীতি | Notification & communication policy | सूचना और संचार नीति | اطلاعات اور رابطے کی پالیسی | سياسة الإشعارات والتواصل | Politique de notifications et de communication |
| complaints | অভিযোগ ও ডেটা-অধিকারের প্রক্রিয়া | Complaints & data-rights procedure | शिकायत और डेटा-अधिकार प्रक्रिया | شکایات اور ڈیٹا حقوق کا طریقہ | إجراء الشكاوى وحقوق البيانات | Procédure de réclamation et droits sur les données |
| disclosure | নিরাপত্তা সমস্যা জানান | Report a security problem | सुरक्षा समस्या की रिपोर्ट करें | سیکیورٹی مسئلے کی اطلاع دیں | الإبلاغ عن مشكلة أمنية | Signaler un problème de sécurité |

Content rules applied (memory /areas/nexatute.md last lines + SP/s2/briefs/legal_opinion_draft.txt): law names "Personal Data Protection Act 2026" (Act 63; s.29
cross-border), Cyber Security Act 2026 (Act 81), National Data Management Act 2026 (Act 80), Children Act 2013, Copyright Act 2023, Trademark Act 2009 — no
"Ordinance 2025" left on X20; NexaTute = data fiduciary, providers = data processors with a DPA each (hosting, email, SMS, voice/IVR, IPTSP, analytics, AI APIs,
Paddle, aamarPay, app stores); privacy, AI transparency, community rules, institution agreement (+ consent, recording) state "NexaTute does not interfere with the
privacy of students, parents, teachers or schools; we only filter bad language, pornography and similar harmful content (Nexa Guard)" + the liability lines
(centre-uploaded Cambridge/Pearson papers = the school’s decision and responsibility; approved/uploaded content = responsibility of the approver/uploader;
NexaTute processes data only as stated) with "[lawyer to finalise the wording]"; subscription terms list the three stores, the separate "App-store charge (30%)"
line with the example Combo ৳800 + ৳240 = ৳1,040, the % editable in admin, and **each app-store charge rounded to the nearest taka (30% of ৳199 = ৳60 → total ৳259)**;
the Learning guarantee terms page = guarantee.md v3 §9; data retention merged into the data-deletion page (backup deletion text source = privacy page);
the institution agreement carries the centre-uploaded exam materials clauses (6 confirmations + NexaTute storage-only/log/takedown) and the provider DPA template.

## 10. fix17 (site, 28 Oct 2026) — page redesign + wording fixes, no new version

**v45 stays the live version** (published 1 February 2027): X13 `versions` / X17 `vers` and the status line do not change (same rule as §8 — layout and
behaviour changes carry no version text). If the owner wants the redesign announced as its own version, the coordinator adds a v46 row here first and X13/X17 copy it.

Owner 28 Oct 2026 18:11 ("more beautiful and more standard, no empty space") — what changed on X20 (live and the 26 Oct beta snapshot; ids, links and test hooks kept):
- Section rhythm: eyebrow + title + one-line subtitle (centred), 88 px section padding (56 px on phones), 1280 px container, alternating bands. Eyebrow texts (6 languages) are site copy (`f17.eb`).
- Hero: headline, sub-line, the two CTAs, trust facts; the class window (demo) gets a bar "1:1 class · Nexa Tutor" + "Mic off — raise your hand to speak" (owner 16:46–16:55 mic rule);
  the syllabus picker is one row under the hero; the "Works on weak internet" card moved into "How it works".
- Sticky section nav (desktop ≥ 1024 px): appears in the header once the hero has scrolled away (How it works · Autism support · Courses · Exam hub · Plans · Guardians ·
  PlayBoom & MindForge · For institutions · FAQ), marks the section being read.
- Folded, never deleted: "See all N courses" (first 6 shown), course tabs (Courses for this syllabus · University & technical · Exams & skills), "Find your plan" (3-question finder),
  "Compare all plans, add-ons and rules" (rules box, Also in NexaTute, other courses, add-ons), "Standards we build to" + Learning Atlas, FAQ "Show all 17 questions"
  (first 8 shown; a jump to a later question opens all), hub: dates 4–5 behind "Show 2 more dates", privacy box behind "More"; phones: status legend behind
  "What the 5 statuses mean", the hub cards as a chip row, 4 more autism-friendly settings, guardian items 4–6; phone carousels for how-it-works, plans, study together, notes.
- Cookie choice: one slim bar at the bottom (≤ 64 px on desktop/tablet: title + one short line + policy links | Accept / Reject / Settings; phones: 2 text lines + one
  row of buttons, links in Settings); the full text and the under-18 line show in Settings; the page gets matching bottom padding so the hero buttons are never covered.
- App-store example (owner 28 Oct 2026 19:31), plans app-store card and Subscription terms §5, 6 languages, amounts from the price table (Combo SSC):
  "Plan price (incl. VAT) — if you buy on the website: ৳800" · "App-store charge (30%): ৳240" · "Total — if you buy through the app store (Google Play / App Store /
  Microsoft Store): ৳1,040" (bn «প্ল্যানের দাম (ভ্যাটসহ) — ওয়েবসাইট থেকে কিনলে: ৳800» · «অ্যাপ-স্টোর চার্জ (30%): ৳240» · «মোট — অ্যাপ স্টোর থেকে কিনলে: ৳1,040»).
- Maintenance banner (owner 17:56–18:01, X14 "Software updates" customer notice): a banner above the announcement bar; prototype switch "Maintenance notice" in the top bar.
  Text = kpi.md v1.8 §6.6 verbatim (`mt_h` + ":", `mt_b` with X20's own date, `mt_src`): en "Scheduled maintenance: Wed 3 Feb 2027, 02:00–05:00 (Bangladesh time):
  a planned software update. No live classes run then, so no class is interrupted. You don’t need to do anything. Sample notice · NexaTute admin chooses how notices are
  sent (app, SMS, email, WhatsApp)" (6 languages; beta snapshot date Wed 4 Nov 2026). The 02:00–05:00 window is the X14 example value (editable, never during live classes).
- Past questions (owner 16:38, R16-site-1): "Also in NexaTute" no longer offers "a past-paper bank (licensed papers only)" — en "past questions inside lessons and mock tests
  (Bangladesh board questions with their year and board — never whole papers)", 6 languages. IB is treated like Cambridge/Pearson: no verbatim IB questions; an IB-authorised school
  may upload papers into its own private area for its own students only — institution band "For Cambridge and Pearson centres and IB-authorised schools", hub disclaimer,
  copyright page, institution agreement (confirmation 1: "approved Cambridge/Pearson centre or an IB-authorised school (centre or school number given)"), privacy and terms
  liability lines ("Cambridge, Pearson or IB papers that a school uploads …"). The one-line rule hub.md v1.5 `pq_rule` is shown verbatim in the courses
  "Exams & skills" tab and under the centre band.
- Hub teaser copies hub.md v1.5: sample marker "sample date (prototype) — not a real notice"; corrections line starts "Mon 18 Jan 2027 — notice: admit cards on Thu 11 Feb";
  SSC admit cards stay "Updated by official notice"; the legend lists the five statuses.
- Admin preview (live) "This page" (R16-site-2): **17 legal drafts waiting for lawyer/DPO approval** — next-version drafts Terms v3.2, Privacy v2.5, Refund v1.1,
  Data retention & deletion v1.1, Accessibility v1.1 (v3.1 / v2.4 / v1.0 stay in force) + the 12 new v1.0 pages; the cookie policy v1.0 is in force. (R16 proposed 14; 17 matches
  the page's own legal list and §9a.) **X13** `cr.block` copies the count and text (admin area).
- guarantee.md v3.1 never-use phrases removed from X20 copy (community rules bn, the 30-day-plan post bn/hi/ur, an older fr FAQ answer).
- Owner 28 Oct 2026 20:03 — AUTISM, SSC, HSC, ENGLISH MEDIUM highlighted: hero path chips "SSC · HSC · English Medium · Autism-friendly" under the headline
  (below 1181 px they replace the longer autism chip so the hero buttons stay in the first screen); a "Choose your path" band right after the hero (4 cards; beta: 3 —
  no autism section in the snapshot) with 3 approved points each, "from" = the Batch price of SSC ৳600 / HSC ৳700 / English-medium Class 6–8 ৳900 (abroad $9 / $10 / $13),
  autism card = sensory.md name + "No extra price — included in every plan"; an **English Medium** section (id `english`, between courses and the hub): Class 4–5
  (Personal ৳1,400 ($21), one subject ৳800 ($12)), Class 6–8 (Batch ৳900 ($13) · Combo ৳1,200 ($18) · Personal ৳1,500 ($22); one subject Batch ৳400 ($6) · Personal ৳700 ($10)),
  Cambridge Checkpoint Crash Pack ৳900/৳1,600/৳2,900 ($13/$24/$43), O-Level / IGCSE and A-Level (plans + crash programs, 3/6 months "(computed)"), hub.md `pq_rule`,
  CTA to the English-medium courses; an **SSC & HSC** band (id `sschsc`): next SSC date from the hub teaser (live only), SSC/HSC crash 1/3/6 months ৳600/৳1,067/৳1,933 (computed),
  SSC/HSC plan prices, board-question rule, CTAs to SSC / HSC prices.
- Owner 28 Oct 2026 20:07 — **Crash Pack**: own header menu item (desktop and phone menu right after PlayBoom, so Courses, Plans, Autism support stay first per fix13 H1; sticky nav; MindForge moves into More ▾ at ≤ 1280 px so the
  header never wraps — checked 1000–1440 px × 6 languages) and own section (id `crash`): 1 / 3 / 6-month switch, 16 courses with ৳ + $ from the price table,
  "(computed)" marks as before (Checkpoint unmarked), hub.md `cr_notoffer` when the program is longer than the time left (SSC: live 28 days → 3/6 months not offered;
  beta 126 days → 6 months not offered), weekly milestones = hub.md `cr_steps`, the add-on rule line, "No seat limit" (live only — the beta keeps its 2,000 seats),
  guarantee.md `not_result`, CTAs Free Trial / See all add-ons.
- Footer on phones: Product links in two columns (R16-site-4). Touch targets ≥ 44 px on phones/tablets for the remaining tooltip triggers (R16-site-5).

## 11. fix18 (site, 28 Oct 2026) — Free-Beta safety items, no new version

Owner 28 Oct 2026 21:55 (approved; in-app channel only — **no WhatsApp / Telegram / Facebook Beta group anywhere**). **v45 stays the live version**: X13 `versions` / X17 `vers`
and the status line do not change (same rule as §8/§10). If the owner wants these shown as a version, the coordinator adds a v46 row here first and X13/X17 copy it.

- **Prototype switch "Free Beta view"** in the X20 top prototype bar (next to "Maintenance notice"): the same era switch as the admin preview — pressed = the 26 Oct 2026
  Free Beta snapshot, not pressed = live (1 Feb 2027). On phones the switch is icon-only and the device buttons that are not selected show only their icon (one row in all 6 languages).
- **"In the Free Beta / Coming later" card** (id `beta-list`) in the FAQ side column, **Beta view only** (the Beta is over in the live view). Site copy `f18.bl`, 6 languages; en:
  - In the Free Beta: Nexa Tutor 1:1 by voice on the whiteboard — 30 minutes a day · Lessons, practice and tests for the syllabus you choose · Batch classes — the 1:50 AI class ·
    Class recordings — only if you choose to record · Guardian app — consent, progress and the weekly report · Live Study Hall and the in-app Beta community · MindForge Pro, open to everyone
  - Coming later: Paid plans and Crash Packs — from 1 January 2027 · Learning guarantee — with paid plans (not in the Free Beta) · PlayBoom (Play class–Class III) — its own Free Beta,
    1–20 January 2027 · Links to Remon Motion Studio and NexaLogicDev — after launch
  - Community box = kpi.md v1.10 §7.4 verbatim: `bc_name`, `bc_mod`, `bc_u18`, `bc_only` (learner tone, like the rest of X20); last line "Something looks wrong? Tap “`fb_btn`” on any
    screen of the app — you get a ticket number." (`fb_btn` verbatim).
  - Only approved, dated facts are listed (Free Beta 20 Nov – 9 Dec 2026, paid from 1 Jan 2027, PlayBoom Free Beta 1–20 Jan 2027, guarantee = paid plans only). The Exam & Admission Hub is
    **not** placed in either column (no approved date for the in-app hub; the X20 hub teaser is v44, 1 Feb 2027).
- Admin preview (Beta view) adds a note under the card: en "Admin: which lines show, their order and their texts are set in X13 “Free Beta page content” — marketing proposes,
  a founder approves, every change is logged." (owner 21:56: every fix18 item is controllable from the admin panel; X13 holds the same 7 + 4 default lines.)
- **RemonLogic cross-links** (footer block "Also from RemonLogic": RemonLogic, Remon Motion Studio, NexaLogicDev) follow the admin setting **"Show RemonLogic cross-links"**
  (X10 / X13; default **off during the Free Beta, on after launch**): hidden in the Beta view, shown live. The © line "RemonLogic Private Limited" stays. The admin preview footer shows
  the setting state (en "RemonLogic cross-links: hidden during the Free Beta — admin setting “Show RemonLogic cross-links” (X10/X13; default: off during the Beta, on after launch)").
  X20 state key `ecoLinks` (true/false) mirrors the admin setting when set; unset = the default above.
- **"AI can make mistakes" line** under the hero class-window answer (live and Beta): kpi.md v1.10 §7.2 `ai_err` verbatim (learner key), small muted line with an info icon.
- W00: card texts for every fix18 feature (X01–X04, X06, X07, X11, X18 learner; X08, X12 guardian/institution with the `_g` wording; X10, X13, X14, X15, X21 admin; X20) — names
  quoted from kpi.md §7 (`fb_btn` / `fb_btn_g`, `ai_err` / `ai_err_g` first sentence, `off_ttl`, `bc_name` / `bc_name_g`, `bc_mod`, `fb_tag`). Main: one more sentence in the design
  rules (Report-a-problem on every learner, guardian and institution screen; `ai_err` under every AI answer; a paused feature shows `off_msg`, never an error).
- For X13 (admin): the live-page preview should show the same "Show RemonLogic cross-links" toggle (default off during the Beta) — X20 reads it as above.
- **Deep link `#beta-list`** (coordinator follow-up; X13 "Free Beta page content" links to `X20-Prototype-Landing.dc.html#beta-list`): on load or hash change X20 opens the
  Free Beta view on the home page (closes an open legal page / Nexa Notes view) and scrolls to the card. Any other hash and no hash: unchanged (live by default; `#legal/<id>` as before).
- **Weak network / weak phone addendum (owner 28 Oct 2026 22:55):** the live FAQ answers "Does it work on weak internet?" (#15) and "What if I have an old phone, little data
  or a disability?" (#16) end with kpi.md v1.11 §8 texts verbatim — #15: `ds_name`, `ds_est_h` "Data per hour of class — estimate (prototype)" with `ds_a` ≈ 15 MB/h · `ds_l` ≈ 90 MB/h ·
  `ds_f` ≈ 250 MB/h, options `ds_vid`, `ds_wifi` (default on), `ds_rec`; #16: `lt_name` with `lt_what` (2D avatar, animations off, lower video quality), switchable in Settings.
  en: "On mobile data you can turn on Data saver. Data per hour of class — estimate (prototype): Audio + whiteboard ≈ 15 MB/h · Light video ≈ 90 MB/h · Full video ≈ 250 MB/h. Options:
  Video off (audio + whiteboard only); Downloads on Wi-Fi only (default: on); Recordings stream in low quality." / "On a slow or older phone the app suggests Lite mode: 2D avatar,
  animations off, lower video quality. You can switch it on or off in Settings any time." The 26 Oct 2026 Beta snapshot FAQ is unchanged. W00 cards name the new items per board.
- **Addendum C (owner 23:31):** the live FAQ "Do I get a report after every class?" (#12) ends with kpi.md v1.12 §9 texts verbatim: `mt9_h` (minute · what went wrong · kind
  `mt9_care` / `mt9_concept` / `mt9_calc` · `mt9_rule` · `mt9_prac` with 2), `mt9_watch_tip` (10 s before), `mt9_fixed_tip`, `im9_h` (mastery before → after), `im9_rule`, `mt9_own`.
  W00 cards: mistake timeline / markers / improvement / library card (X02, X06, X01, X18, L05, D01, D02), guardian top 3 (X08, G01), X10 / D05 / D07 settings.
- **Addendum D (owner 23:53):** W00 cards only — X14 "Video & recording delivery" panel (D05 line) and protected 15-minute recording links (X02; X08 adult wording).

## 12. fix18f–n (site, 29 Oct 2026, owner 01:24–02:49) — no new version (still v45)
Texts verbatim from kpi.md v1.13–v1.19 (§10–§17; site uses the `_g` adult rows). The pinned lists (`plans.incl`, `f18.bl.later`, base FAQ) are unchanged; additions render from `t.f18f`. No prices are typed in copy (sizes only; prices come from the price table).
- **Every plan includes** (both views): extra line "Storage — Batch 6 GB · Combo 8 GB · Personal 10 GB (more with add-ons)"; live view also `lim_list_paid` (2027 feature limits per plan).
- **Free for life** (live view): plans `free` text + `lim_list_free`.
- **FAQ**: "What stays free?" (fq-8, both views) gains the storage sentence (`sg_rule` + `sg_crash` + add-ons +20 / +50 / +100 GB + `sg_u18_g` + `sg_keep_g`); live view also `lim_list_free`. Live view gains an 18th question, fq-17 "Can I ask on WhatsApp or Messenger?" (`faq_bot_q`; answer `bot_desc` + `bot_paid` + `bot_u18` + `bot_sms`). Beta view still 10.
- **Subscription terms** (legal page `subscription-terms`): new section "Storage add-ons (per month)" before "Learners under 18" (7 items: allowance, Crash Pack bonus, sizes, the 3 purchase-screen lines for store apps, under-18 approval, full-storage choice, 30-day keep) — no amounts typed.
- **Status page**: footer link "System status" → https://status.nexatute.com (new tab); preview card `#status` in the FAQ help box ("All systems normal", parts, sample (prototype)); last-incident line (`ss_inc1`, Thu 3 Dec 2026) only in the live view.
- **Roadmap** `#roadmap` ("Coming in 2027", before the FAQ; links in the header More menu after Log in and in the footer; HOME list + `roadmap`): groups Learning (Game Show, Debate, Be the Teacher, Shorts question, AR Magic Book, Time-Travel, Nexa Radio, mystery mission, team mind map, Error Autopsy, Voice mode) · Community & rewards (Helper rewards, Nexa Swap, job board, Learn → Earn) · Schools, guardians & partners (teacher's AI assistant, PTM phone call, WhatsApp/Messenger study bots, NexaTute for Partners); status chips: live view "Live now" (Partners "Later in 2027"), Beta view "From 1 Jan 2027" (Partners "Later in 2027"). Editable in X13 (admin agent).
- **Study Hall card**: + `tq_line`; live view also "Live Game Show — Every Saturday 7:00 pm (default) · AI Debate Chamber · Be the Teacher" (F19: was Friday, see §13).
- **Free Beta view, "In the Free Beta / Coming later" card**: 2 extra later lines (§13 and §14 features, "Coming soon — from 1 Jan 2027").
- **fix18m — new Free Beta dates (owner 02:46):** the NexaTute Free Beta is **Fri 20 Nov – Wed 9 Dec 2026** (20 days); paid launch stays 1 Jan 2027. Every "12–31 December" on X20 (hero pill, join, final CTA, tips, FAQ, blog post "Free Beta: what you get", Free Beta table, beta snapshot note, live FAQ/legal "is over" lines) now reads 20 November – 9 December 2026 in 6 languages; "We open on 20 November 2026"; "ended on 9 December 2026"; the day-count exercise is rewritten (11 + 9 = 20). The 31 Dec 2026 news post is now titled "The Free Beta is over: paid plans and the 7-day Free Trial start tomorrow". Motion Studio Free Beta starts 20 Dec 2026 (code comment updated; no Motion Studio date is shown on X20). Status-page incident moved to Thu 3 Dec 2026. The beta snapshot (26 Oct 2026) and maintenance notice (Wed 4 Nov 2026) are unchanged (both before the Free Beta).
- **fix18m — last items (kpi.md v1.20 §18):** roadmap Learning group + Smart Suggestion, Study Buddy, AI comic stories, What-if simulator; Schools/partners group + White-label portal, Yearly sponsorship (all "From 1 Jan 2027" in the Beta view, "Live now" in the live view; Partners API stays "Later in 2027"). Live view: under the Free / Free Trial boxes two plan notes (`plX`): institution plans (`ln_list_b2b`) and the yearly sponsorship line (`ys_line` + `ln_sp`; no ৳ — the price comes from the Academic Year Pass row). Beta view "Coming later": + one line with the six item names.
- **fix18n — free vs paid (kpi.md v1.20 §19):** live view "Free" box and FAQ 8 + `ln_list_free`; "Every plan includes" + `ln_list_paid`; the bot FAQ answer (fq-17) is now four full sentences ending with the SMS line `ln_sms` (paid plans, up to 5 a day).

## 13. F19 final check (site, 29 Oct 2026) — no new version (still v45)
- **Live Game Show day** (coordinator decision "Game Show clash"; kpi.md v1.21 `gs_when`): the live-view Study Hall line now reads "Live Game Show — Every Saturday 7:00 pm (default) · AI Debate Chamber · Be the Teacher" in 6 languages (`t.f18f.eg_live`; ur "ہر ہفتہ (سنیچر) شام 7:00"). Not 8:00 pm: AI Teacher Live stays Friday 8:00 pm and the weekly human revision class stays Saturday 8:00 pm (not shown on X20).
- **Roadmap** `#roadmap` = the X13 "Coming in 2027" list (Landing Page AI): same 15 / 4 / 6 items, same order and the same labels in all 6 languages.
- Nothing else on X20 changed.

## 14. fix20 (site, 29 Oct 2026, owner 08:07 item C2; coordinator size rule) — no new version (still v45)
- **Legal pages → new board `X24-Prototype-Legal.dc.html`.** The Design viewer drops any board over 2 MiB; X20 was 2.84 MB. Boards must stay <= 1,800,000 bytes. X24 holds all **19 legal pages** in 6 languages with the same texts, versions and drafts as before (Free Beta / live views, admin URL list + hreflang, print, page index at `#legal`, RTL, Mobile/Tablet/Desktop). Every legal link — X20 (footer Legal list, plans notes, institutions, FAQ cards, cookie bar, sign-up dialog, newsletter, accessibility chip, hub disclaimer, footer bar) and the other boards (D04, G01, X01, X03, X07, X08, X10, X12, X15) — opens `X24-Prototype-Legal.dc.html#legal/<id>`; X24's header, footer and page links lead back to X20 ("Back to nexatute.com"). X20 forwards an old `#legal/<id>` link to X24; `X20-Prototype-Landing.dc.html#cookie-settings` opens the cookie settings (X24's cookie-policy button). The public URLs are unchanged: `nexatute.com/{lang}/legal/<id>`.
- **New legal page `security-disclosure`** — key `disclosure`, name “Report a security problem” (6 languages, table §9a), `X24-Prototype-Legal.dc.html#legal/security-disclosure`; a **v1.0 draft for lawyer/DPO approval in both views** like the 12 fix16 pages (“New page approved by the owner on 29 October 2026”, last updated 29 October 2026 (sample date)). X20: 19th entry in the footer Legal list (marked “draft”) + a footer-bar link “Report a security problem” next to “Coming in 2027” and “System status”.
- Content (8 sections, same in 6 languages): how to report (security@nexatute.com, any of the 6 languages, tell us privately first, contact also in `nexatute.com/.well-known/security.txt`); what to include (what, where, steps to see it again, screenshots, contact, thank-you-list choice; never other people’s personal data); rules for testing (own or test accounts only — no access to other people’s data, no denial-of-service, no social engineering, no physical attacks, stop once shown, keep no data); good-faith safe harbour ([lawyer to finalise the wording]; not for other people’s data, harm to the service or a demand for money); what happens next (**reply within 3 working days (default)**, severity high / medium / low, updates until fixed, thank-you list if the reporter agrees, Security incident response policy if personal data was at risk); **no paid bug bounty at launch — a public thank-you list instead**; laws (Cyber Security Act 2026 Act 81, Personal Data Protection Act 2026 Act 63 [to confirm]); changes (29 October 2026 first draft).
- The reply time is an admin value: admin X15 “Security reports” queue (sample report, severity, status, reply SLA 3 working days (default)) is fed by this page (admin area).
- **fr wording**: every “magasin d’applications” on X20 / X24 now reads “boutique d’applications” (“Frais de la boutique d’applications (30 %)”, “via la boutique”, “cette boutique”), the same as X03 and kpi.md. **Urdu**: hub.md v1.6 quote order “…” on X20.
- Touch: the tooltip chips “Verified answers / NexaTute verified” are 44 px tall on phones/tablets (was 43.5 px; the pill looks the same).
- X20 size work (no visible change): legal texts out, leading indentation of template/script lines removed, JSON data lines compacted, history comments removed (the history stays in this file and the pass reports), legal-view CSS removed. X20 = 1.77 MB, X24 = 1.14 MB. Next cut if X20 grows: Nexa Notes (≈ 0.5 MB) to its own board.

## 15. fix21 (site, 29 Oct 2026, owner 12:30 item 4 + addition 12:32 + change 12:36) — no new version (still v45)
Texts verbatim from kpi.md v1.23 §21 (learner owns; the site uses the adult `_g` rows where they exist). Admin values live in X25 “Admission limits per class / course” (two-person approval, logged). **No seat counts, no “only N left”, no countdown** — the sample position “#14 (sample)” is the only number, and only after joining.
- **Prototype switch “Simulate: class full”** (`wl_sim_full`, prototype bar; icon only on phones): the plan-card button, the price-finder result button and the higher-education card button read **“Join the waiting list”** (`wl_join_g`); a one-line explanation sits in the plans panel and in the courses panel: **“This class is full right now”** + `wl_full_g` + `wl_pay_g` (“No payment is taken until a place is offered and you accept it.”) + link “What is the waiting list?” (live view). The header / hero sign-up buttons stay as they are. The sign-up dialog shows the same line (+ `wl_u18_g` when a guardian signs up) and its button joins the waiting list: no application, no payment; the result says `wl_on_t_g` / `wl_pos_g` (“You are #14 on the waiting list (sample)”) + `wl_n3_g` (SMS (free), push notification and email) + `wl_pay_g`; no “next step” to payment.
- **Prototype switch “Simulate: admissions closed”** (`ad_sim`; the admin master switch “Close all new admissions” in X25 — the admin writes the message in any one language and AI translates and publishes it in all 6, owner 12:36): a banner at the very top (above the announcement bar) with the label `ad_msg_l` (“Message from NexaTute (written by the admin)”), **`ad_closed_t`** + the admin’s message `ad_closed_msg_g` (sample/default text), `ad_reopen` (“Expected to reopen: Mon 1 Feb 2027 (sample)”, optional) · `ad_existing_g` (“Already a learner? Your classes continue as normal.”) and a “Join the waiting list” button; **every** enrol / price CTA (header, hero, plans, price finder, higher education, fit, hub, final call) reads “Join the waiting list” and the sign-up dialog shows the admin’s message. Admin preview adds the `ad_src` note. Separate from “class full”; both can be on.
- **FAQ**: live question 19 (`fq-18`, last) **“What is the waiting list?”** (`wl_faq_q` / `wl_faq_a`); the Free Beta snapshot keeps its 10 questions.
- Existing sign-up-by-country Open / Waiting list / Closed (syllabus “Coming soon” waiting list, `t.cur.wait_btn`) and the Free Beta “waiting room” (admin preview) are unchanged.
- Size: X20 = 1,794,096 bytes (limit 1,800,000) — Nexa Notes did not need to move (no X27).

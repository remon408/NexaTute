# Bangla Sign Language (BdSL) avatar texts — fix11/fix12 (learn1) — v1.2 (27 Oct 2026, fix12)

> **Change note v1.2 — 27 Oct 2026 (fix12, learn1; coordinator decision G3):** the BdSL avatar and its caption rule are **ON and LOCKED in every
> plan** (same pattern as Sensory-friendly mode, sensory.md v2 §5). In X10 Plans & modules the per-plan cells are ON + locked (lock icon, not
> clickable) with the chip `a_req` and the tooltip `a_lock`; the row value is `a_val`. Editable: ONLY the platform-wide switch and the default
> settings (minute rate 1.5 (default), caption default). No per-plan switch to remove it. The LEARNER still turns the avatar on/off for
> themselves in X01 settings / X02 (that is a personal preference, unchanged). New 6-language keys `a_val`, `a_req`, `a_lock` in §5
> (`a_val` / `a_req` use exactly the wording of sensory.md `sn_adm_val` / `sn_adm_req`). Nothing else changed.
> Earlier: Bangla Sign Language (BdSL) avatar texts — fix11 (learn1, 26 Oct 2026) — v1.1 (22:40: English apostrophes typographic ’)
>
> **§5 note — 27 Oct 2026 (fix12, admin1; coordinator decision G3, R11-admin-3):** §5 now says "ON and LOCKED in every plan" (the v1.1 wording
> "on/off per plan" is withdrawn — memory: the avatar costs nothing extra and covers every class, subject and course). The `a_val` / `a_req` / `a_lock`
> rows are joined to the §5 table (a blank line had split them off). X10 Plans & modules implements it: the BdSL avatar and caption-rule cells are ✓ with
> a lock in all 7 plans (tooltip `a_lock`; the editor shows `a_req` + `a_val`); "all / none" on the group and version restores cannot switch them off;
> the platform-wide switch (logged, with a reason) and the default settings (minute rate 1.5 (default), caption default) stay editable.

Single source for X01, X02, X05, X06, X08, X10, X12, X16, X20, X22, L/D/G/P statics. Copy the strings EXACTLY.
Source: memory /areas/nexatute-learning.md, last [stated] lines of 26 Oct 2026:
- complete feature (not a pilot), everything rendered in the user’s web browser; its package works like the other packages
- for English-medium learners too: the avatar signs in Bangla Sign Language (BdSL) with English captions
- covers every class, every subject and every course
- costs nothing extra — same price in every plan; with the avatar on for the whole 1:1 class, minutes are counted slower
  (1.5 minutes used = 1 minute charged, default, editable in admin)
- a separate Sign Language Fund from Sponsor-a-Learner/CSR, grants and deaf-school/NGO B2B at normal seat prices
- all these features must be controllable from the admin panel
Register: learner boards bn তুমি, hi/ur tum, ar أنت, fr tu; guardian/admin boards keep the labels and change only the sentence register.
Latin digits; in ur/ar wrap "1.5", "1" and "BdSL" in LTR isolation (M()/⁦…⁩) — the visible text stays identical.
"BdSL" stays Latin in every language. PlayBoom child views (X05) may use their own digit rule for the numbers.

## 1. Avatar toggle label (switch, class + recording player + settings)

| key | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| sl_toggle | Sign language avatar (BdSL) | সাংকেতিক ভাষার অ্যাভাটার (BdSL) | सांकेतिक भाषा अवतार (BdSL) | اشاروں کی زبان کا اوتار (BdSL) | أفاتار لغة الإشارة (BdSL) | Avatar en langue des signes (BdSL) |
| sl_short (chip / small button) | BdSL avatar | BdSL অ্যাভাটার | BdSL अवतार | BdSL اوتار | أفاتار BdSL | Avatar BdSL |
| sl_on | Avatar on | অ্যাভাটার চালু | अवतार चालू | اوتار آن | الأفاتار مفعَّل | Avatar activé |
| sl_off | Avatar off | অ্যাভাটার বন্ধ | अवतार बंद | اوتار بند | الأفاتار متوقف | Avatar désactivé |
| sl_sub (one-line description) | Signs every class in Bangla Sign Language — every subject, every course | প্রতিটি ক্লাস বাংলা সাংকেতিক ভাষায় দেখায় — সব বিষয়, সব কোর্স | हर क्लास बांग्ला सांकेतिक भाषा में दिखाता है — हर विषय, हर कोर्स | ہر کلاس بنگلہ اشاروں کی زبان میں دکھاتا ہے — ہر مضمون، ہر کورس | يترجم كل حصة بلغة الإشارة البنغالية — كل مادة وكل دورة | Signe chaque cours en langue des signes bangladaise — toutes les matières, tous les cours |
| sl_browser | Drawn in your browser — no video is sent | তোমার ব্রাউজারেই আঁকা হয় — কোনো ভিডিও পাঠানো হয় না | तुम्हारे ब्राउज़र में ही बनता है — कोई वीडियो नहीं भेजा जाता | تمہارے براؤزر میں ہی بنتا ہے — کوئی ویڈیو نہیں بھیجی جاتی | يُرسم في متصفحك — لا يُرسل أي فيديو | Dessiné dans ton navigateur — aucune vidéo n’est envoyée |

## 2. Caption rule (one sentence + the per-medium chip)

Rule: the avatar always signs in BdSL; captions follow the course’s teaching language — Bangla medium: Bangla captions; English medium: English captions.

| key | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| sl_cap_rule | The avatar always signs in BdSL. Captions follow your teaching language: Bangla medium → Bangla captions, English medium → English captions. | অ্যাভাটার সবসময় BdSL-এ দেখায়। ক্যাপশন তোমার পড়ার ভাষায়: বাংলা মাধ্যম → বাংলা ক্যাপশন, ইংরেজি মাধ্যম → ইংরেজি ক্যাপশন। | अवतार हमेशा BdSL में दिखाता है। कैप्शन तुम्हारी पढ़ाई की भाषा में: बांग्ला माध्यम → बांग्ला कैप्शन, अंग्रेज़ी माध्यम → अंग्रेज़ी कैप्शन। | اوتار ہمیشہ BdSL میں دکھاتا ہے۔ کیپشن تمہاری پڑھائی کی زبان میں: بنگلہ میڈیم → بنگلہ کیپشن، انگلش میڈیم → انگریزی کیپشن۔ | يترجم الأفاتار دائمًا بلغة BdSL. والترجمة النصية بلغة دراستك: التعليم بالبنغالية → نص بنغالي، التعليم بالإنجليزية → نص إنجليزي. | L’avatar signe toujours en BdSL. Les sous-titres suivent ta langue d’enseignement : bengali → sous-titres en bengali, anglais → sous-titres en anglais. |
| sl_cap_bn (chip) | BdSL + Bangla captions | BdSL + বাংলা ক্যাপশন | BdSL + बांग्ला कैप्शन | BdSL + بنگلہ کیپشن | BdSL + نص بنغالي | BdSL + sous-titres bengali |
| sl_cap_en (chip) | BdSL + English captions | BdSL + ইংরেজি ক্যাপশন | BdSL + अंग्रेज़ी कैप्शन | BdSL + انگریزی کیپشن | BdSL + نص إنجليزي | BdSL + sous-titres anglais |

Captions are WebVTT and stay on while the avatar is on (they cannot be switched off while the avatar is on — (default)).

## 3. "Sign check in progress" (lesson whose signs are not yet verified by the X16 queue: BdSL expert + Deaf reviewer)

| key | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| sl_chk | Sign check in progress | সাইন যাচাই চলছে | साइन जाँच जारी है | اشاروں کی جانچ جاری ہے | جارٍ التحقق من الإشارات | Vérification des signes en cours |
| sl_chk_s | A BdSL expert and a Deaf reviewer are checking this lesson’s signs. Until then the avatar shows only checked signs, and the captions show everything. | একজন BdSL বিশেষজ্ঞ ও একজন বধির রিভিউয়ার এই পাঠের সাইন যাচাই করছেন। ততক্ষণ অ্যাভাটার শুধু যাচাই-করা সাইন দেখায়, আর ক্যাপশনে সবকিছু থাকে। | एक BdSL विशेषज्ञ और एक बधिर समीक्षक इस पाठ के साइन जाँच रहे हैं। तब तक अवतार सिर्फ़ जाँचे गए साइन दिखाता है, और कैप्शन में सब कुछ रहता है। | ایک BdSL ماہر اور ایک بہرے جائزہ کار اس سبق کے اشارے جانچ رہے ہیں۔ تب تک اوتار صرف جانچے گئے اشارے دکھاتا ہے، اور کیپشن میں سب کچھ رہتا ہے۔ | يتحقق خبير في BdSL ومراجِع أصمّ من إشارات هذا الدرس. حتى ذلك الحين يعرض الأفاتار الإشارات المعتمدة فقط، وتعرض الترجمة النصية كل شيء. | Un expert BdSL et un relecteur sourd vérifient les signes de cette leçon. En attendant, l’avatar ne montre que les signes vérifiés et les sous-titres montrent tout. |
| sl_chk_ok | Signs checked | সাইন যাচাই হয়েছে | साइन जाँचे गए | اشارے جانچے گئے | تم التحقق من الإشارات | Signes vérifiés |

## 4. Minute-rate line (1:1 class; no extra price)

| key | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| sl_free | No extra price — the same price in every plan | কোনো বাড়তি দাম নেই — সব প্ল্যানে একই দাম | कोई अतिरिक्त कीमत नहीं — हर प्लान में वही कीमत | کوئی اضافی قیمت نہیں — ہر پلان میں وہی قیمت | بلا سعر إضافي — السعر نفسه في كل خطة | Sans supplément — le même prix dans chaque formule |
| sl_rate | With the avatar on for the whole 1:1 class, your minutes count slower: 1.5 minutes of class = 1 minute from your plan. | পুরো 1:1 ক্লাসে অ্যাভাটার চালু থাকলে মিনিট ধীরে গোনা হয়: ক্লাসের 1.5 মিনিট = প্ল্যান থেকে 1 মিনিট। | पूरी 1:1 क्लास में अवतार चालू रहे तो मिनट धीरे गिने जाते हैं: क्लास के 1.5 मिनट = प्लान से 1 मिनट। | پوری 1:1 کلاس میں اوتار آن رہے تو منٹ آہستہ گنے جاتے ہیں: کلاس کے 1.5 منٹ = پلان سے 1 منٹ۔ | عند تفعيل الأفاتار طوال حصة 1:1 تُحسب دقائقك أبطأ: 1.5 دقيقة من الحصة = دقيقة واحدة من خطتك. | Avec l’avatar activé pendant tout le cours 1:1, tes minutes comptent moins vite : 1,5 minute de cours = 1 minute de ta formule. |
| sl_rate_chip (in-class timer chip) | BdSL · 1.5 min = 1 min | BdSL · 1.5 মিনিট = 1 মিনিট | BdSL · 1.5 मिनट = 1 मिनट | BdSL · 1.5 منٹ = 1 منٹ | BdSL · 1.5 دقيقة = 1 دقيقة | BdSL · 1,5 min = 1 min |

fr uses the decimal comma (1,5) — the only language that does; all others write 1.5.
The batch class (1:50) has a shared timetable, so the minute rate applies to the 1:1 class only (memory: "the whole 1:1 class").

## 5. Admin control names (X10 Plans & modules, X16, X22, X17 sponsors; admin boards address the admin team)

| key | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| a_sl | BdSL sign-language avatar — every plan, no extra price | BdSL সাংকেতিক ভাষার অ্যাভাটার — সব প্ল্যানে, বাড়তি দাম নেই | BdSL सांकेतिक भाषा अवतार — हर प्लान में, अतिरिक्त कीमत नहीं | BdSL اشاروں کی زبان کا اوتار — ہر پلان میں، اضافی قیمت نہیں | أفاتار لغة الإشارة BdSL — في كل خطة، بلا سعر إضافي | Avatar en langue des signes BdSL — toutes les formules, sans supplément |
| a_rate | Minute rate with the avatar on (1:1): 1.5 minutes used = 1 minute charged (default) | অ্যাভাটার চালু থাকলে মিনিটের হার (1:1): 1.5 মিনিট ব্যবহার = 1 মিনিট চার্জ (ডিফল্ট) | अवतार चालू होने पर मिनट दर (1:1): 1.5 मिनट उपयोग = 1 मिनट चार्ज (डिफ़ॉल्ट) | اوتار آن ہونے پر منٹ کی شرح (1:1): 1.5 منٹ استعمال = 1 منٹ چارج (ڈیفالٹ) | معدل الدقائق مع تفعيل الأفاتار (1:1): 1.5 دقيقة مستخدمة = دقيقة واحدة محسوبة (افتراضي) | Taux de minutes avec l’avatar (1:1) : 1,5 minute utilisée = 1 minute facturée (par défaut) |
| a_cap | Caption language rule (BdSL + teaching-language captions) | ক্যাপশনের ভাষার নিয়ম (BdSL + পড়ার ভাষায় ক্যাপশন) | कैप्शन भाषा नियम (BdSL + पढ़ाई की भाषा में कैप्शन) | کیپشن کی زبان کا اصول (BdSL + پڑھائی کی زبان میں کیپشن) | قاعدة لغة الترجمة النصية (BdSL + نص بلغة الدراسة) | Règle de langue des sous-titres (BdSL + sous-titres dans la langue d’enseignement) |
| a_verify | Sign verification queue (BdSL expert + Deaf reviewer) | সাইন যাচাইয়ের সারি (BdSL বিশেষজ্ঞ + বধির রিভিউয়ার) | साइन सत्यापन कतार (BdSL विशेषज्ञ + बधिर समीक्षक) | اشاروں کی تصدیق کی قطار (BdSL ماہر + بہرا جائزہ کار) | قائمة التحقق من الإشارات (خبير BdSL + مراجِع أصمّ) | File de vérification des signes (expert BdSL + relecteur sourd) |
| a_cover | Sign coverage per course × subject | কোর্স × বিষয় অনুযায়ী সাইন কভারেজ | कोर्स × विषय के अनुसार साइन कवरेज | کورس × مضمون کے حساب سے اشاروں کی کوریج | تغطية الإشارات لكل دورة × مادة | Couverture des signes par cours × matière |
| a_look | Avatar look (BdSL) | অ্যাভাটারের চেহারা (BdSL) | अवतार का रूप (BdSL) | اوتار کی شکل (BdSL) | مظهر الأفاتار (BdSL) | Apparence de l’avatar (BdSL) |
| a_fund | Sign Language Fund | সাংকেতিক ভাষা তহবিল | सांकेतिक भाषा कोष | اشاروں کی زبان کا فنڈ | صندوق لغة الإشارة | Fonds langue des signes |
| a_fund_s | Separate from Sponsor-a-Learner · CSR, grants, deaf-school/NGO B2B at normal seat prices | Sponsor-a-Learner থেকে আলাদা · CSR, অনুদান, বধির স্কুল/NGO B2B স্বাভাবিক সিট-দামে | Sponsor-a-Learner से अलग · CSR, अनुदान, बधिर स्कूल/NGO B2B सामान्य सीट कीमत पर | Sponsor-a-Learner سے الگ · CSR، گرانٹس، بہرے بچوں کے اسکول/NGO B2B عام سیٹ قیمت پر | منفصل عن Sponsor-a-Learner · مسؤولية اجتماعية ومنح ومدارس الصم/المنظمات B2B بأسعار المقاعد العادية | Séparé de Sponsor-a-Learner · RSE, subventions, écoles pour sourds/ONG en B2B au prix normal du siège |
| a_val (v1.2, G3) | On and locked in every plan · no extra price | প্রতিটি প্ল্যানে চালু ও লক করা · বাড়তি দাম নেই | हर प्लान में चालू और लॉक · कोई अतिरिक्त कीमत नहीं | ہر پلان میں آن اور لاک · کوئی اضافی قیمت نہیں | مفعّل ومقفل في كل خطة · بلا سعر إضافي | Activé et verrouillé dans chaque formule · sans supplément |
| a_req (v1.2, G3; chip on the locked cells) | Required by policy | নীতিমালা অনুযায়ী বাধ্যতামূলক | नीति के अनुसार ज़रूरी | پالیسی کے تحت لازمی | مطلوب بموجب السياسة | Requis par la politique |
| a_lock (v1.2, G3; tooltip on the locked cells) | Required by policy — the BdSL avatar and its caption rule stay on in every plan. Only the platform-wide switch and the default settings (minute rate, caption default) can be changed. | নীতিমালা অনুযায়ী বাধ্যতামূলক — BdSL অ্যাভাটার আর এর ক্যাপশনের নিয়ম প্রতিটি প্ল্যানে চালু থাকে। শুধু প্ল্যাটফর্ম-জুড়ে সুইচ আর ডিফল্ট সেটিং (মিনিটের হার, ক্যাপশনের ডিফল্ট) বদলানো যায়। | नीति के अनुसार ज़रूरी — BdSL अवतार और उसका कैप्शन नियम हर प्लान में चालू रहते हैं। सिर्फ़ पूरे प्लेटफ़ॉर्म का स्विच और डिफ़ॉल्ट सेटिंग (मिनट दर, कैप्शन डिफ़ॉल्ट) बदली जा सकती हैं। | پالیسی کے تحت لازمی — ⁦BdSL⁩ اوتار اور اس کا کیپشن اصول ہر پلان میں آن رہتے ہیں۔ صرف پورے پلیٹ فارم کا سوئچ اور ڈیفالٹ سیٹنگز (منٹ کی شرح، کیپشن ڈیفالٹ) بدلی جا سکتی ہیں۔ | مطلوب بموجب السياسة — يبقى أفاتار ⁦BdSL⁩ وقاعدة الترجمة النصية مفعّلين في كل خطة. لا يمكن تغيير سوى المفتاح العام للمنصة والإعدادات الافتراضية (معدل الدقائق، الترجمة الافتراضية). | Requis par la politique — l’avatar BdSL et sa règle de sous-titres restent activés dans chaque formule. Seuls l’interrupteur global de la plateforme et les réglages par défaut (taux de minutes, sous-titres par défaut) peuvent être modifiés. |

Admin defaults (v1.2, G3): the avatar and its caption rule are ON and LOCKED in every plan — per-plan cells show a lock, `a_req` and the `a_lock`
tooltip, and cannot be switched off. Editable in X10 Plans & modules: ONLY the platform-wide switch and the default settings — minute rate 1.5
(default, editable) and the caption default (§2 rule). The learner still switches the avatar on/off for themselves (X01 settings, X02 class sheet).
Verification queue required before a lesson’s signs show as "Signs checked" (X16). No new menus.

## 6. Settings / sheet wording (X01 settings, X02 class sheet, X05 Kids Mode)

| key | en | bn | hi | ur | ar | fr |
|---|---|---|---|---|---|---|
| sl_set_h | Accessibility | সহজে ব্যবহার | सुगमता | رسائی | سهولة الوصول | Accessibilité |
| sl_who | For deaf and hard-of-hearing learners — Bangla and English medium | বধির ও কম শোনা শিক্ষার্থীদের জন্য — বাংলা ও ইংরেজি মাধ্যম | बधिर और कम सुनने वाले शिक्षार्थियों के लिए — बांग्ला और अंग्रेज़ी माध्यम | بہرے اور کم سننے والے طلبہ کے لیے — بنگلہ اور انگلش میڈیم | للمتعلمين الصم وضعاف السمع — التعليم بالبنغالية وبالإنجليزية | Pour les élèves sourds et malentendants — enseignement en bengali et en anglais |
| sl_kids (X05 child view) | Sign friend (BdSL) | ইশারা-বন্ধু (BdSL) | इशारा-दोस्त (BdSL) | اشارہ دوست (BdSL) | صديق الإشارة (BdSL) | Ami des signes (BdSL) |

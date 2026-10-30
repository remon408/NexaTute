# Remon Motion Studio — independent review: missing items and admin control

Date: 30 October 2026. Reviewer: Claude (independent pass).
Sources read: `src/decisions.md` (all, incl. the 30 Oct additions not yet in chapters), `sec/front.md`, `sec/01–18.md`, `sec/A.md`, `sec/B.md`, the `/areas/motion-studio.md` copy in `src/memory_decisions.txt`, and the NexaTute admin model (`src/38_Platform_Administration_Institute_Adm.txt`, `/areas/nexatute-admin.md` copy in `src/memory_nexatute_etc.txt`).

Skipped on purpose: anything already covered in substance under any name, and everything the owner rejected (fake testimonials, lyric videos of others' songs, single-photo talking heads, real children's voices, cloning without consent, Stripe/PayPal direct accounts, "detect any AI video" claims, "views guaranteed" claims).

---

## GOAL A — Important things still missing (ranked, max 15)

| # | Rank | Missing item | One-line description | Why it matters |
|---|---|---|---|---|
| A1 | High | Account eligibility and minimum age | No minimum age for a Motion Studio account is set anywhere (only clone/twin are 18+); define 18+ (or 13–17 only with guardian, limited features), age check at sign-up, and a guard on the shared Nexa ID wallet. | The free NexaTute course, cross-course offers, shared Nexa ID and shared wallet send NexaTute learners — many under 18 — straight into a deepfake-capable paid tool; child-data law and guardian spending rules would be broken by default. |
| A2 | High | Discount, credit and offer stacking rules with a price floor | One rule for how coupons, promo codes, gift cards, annual discount, Islamic −25%, Slow −10%, reseller 15–22%, festival early-order, minute packs, referral credit, first-course discount and challenge credits combine (order, which stack, maximum total, floor per rate cell). | Ten discount sources were approved separately; without a stacking rule a Slow + Islamic + reseller + coupon order can fall below GPU cost, and the 30% margin alert only reports it after the loss. |
| A3 | High | AI Co-Director and agent safety | Crisis protocol (self-harm/abuse disclosures → helpline and human), prompt-injection protection for "video from a link", Document-to-Video, faceless autopilot sources and catalogue imports, conversation retention and a "never used for training" rule, and logging/appeal for Co-Director answers. | The Co-Director is an "any-subject" chat on an own LLM in 6 languages + Banglish; link and document ingestion feed untrusted web text into the same LLM that writes scripts and can trigger paid renders. |
| A4 | High | Consumer-law checkout and terms lifecycle | Terms/Privacy versioning with acceptance log and re-consent on change (NexaTute has it; Motion Studio does not), clear auto-renew consent, EU/UK 14-day withdrawal-right waiver for digital services, cancellation confirmation, and what happens to a wallet balance when an account is closed or deleted. | EUR/GBP/USD sales and the non-cash-out wallet create consumer-law exposure; aamarPay international card sales are not covered by a merchant of record until Paddle is live. |
| A5 | High | International tax and market-entry readiness before Paddle | While aamarPay takes international cards, RemonLogic itself may owe foreign VAT/GST (EU, UK, India, Gulf) on digital services; add sanctions/restricted-country screening and per-country AI-labelling and content rules for the newly priced INR/PKR/AED/SAR markets and the Middle East pack. | INR/PKR/AED/SAR prices and a Middle East pack were approved, but the only tax position covers Bangladesh VAT and Paddle; selling first and registering later creates back-tax and platform-ban risk. |
| A6 | High | Legal-process and evidence handling | A procedure and admin queue for police/BTRC/court data and takedown requests, preservation holds, deepfake-victim fast-track (person depicted, not only the copyright owner), CSAM evidence preservation without staff viewing, and a request log. | A voice/face-cloning product in Bangladesh under the Cyber Security Act 2026 will receive such requests; none of the chapters says who answers, within what time, or what data may be disclosed. |
| A7 | Medium | Brand-impersonation and payment-scam protection | Verified WhatsApp/Messenger business badge, payment links only on remonlogicstudio.com, "we never ask for your bKash PIN/OTP" notices, a public list of official numbers, look-alike domain monitoring, and trademark registration of "Remon Motion Studio" and the logo. | Ordering and paying inside WhatsApp chats is exactly the pattern scammers copy with fake numbers; one scam wave would damage trust in the brand. |
| A8 | Medium | Bulk-messaging cost and compliance | Who pays Meta's per-message WhatsApp fees and SMS costs for bulk personalised videos and reminders, BTRC-approved SMS sender masking, opt-out handling, per-business send caps and deletion of uploaded recipient lists. | Video minutes are billed, but the delivery messages are not; at thousands of recipients the message cost can exceed the video price, and spam complaints can get the WhatsApp number banned. |
| A9 | Medium | Verification of regulated businesses | Check licence numbers before export (recruiting-agency RL number against the BMET list, clinic licence, real-estate approval), not only "must show the number". | Fake overseas-job ads are a named scam category; a typed-in fake RL number on a Motion Studio video would make the product a tool for the scam it bans. |
| A10 | Medium | Talent release lifecycle | Contracts for stock presenters, voice artists and child-character voice artists: term, territory, permitted uses, royalties, revocation or death, and what happens to pinned projects and published videos when a release ends. | The stock presenter library and paid voice artists were approved, but only the consent record is described; an expired or revoked release without a rule means takedowns of client videos. |
| A11 | Medium | Free Beta end-of-beta transition | What happens to Beta users' projects, storage above the free allowance, watermarked videos, and voice clones and twins made during the Beta; the Beta-to-paid offer; the notice schedule. | "Free Beta includes all features" means many users will hold assets that their next package does not include; without a rule, deletion or lock-out at day 30 becomes a mass complaint. |
| A12 | Medium | Enterprise and agency commercial kit | Quote and order-form flow, post-paid invoice billing with credit limit and PO numbers, security-questionnaire pack (SOC 2-ready evidence), liability cap and IP-indemnity position for AI output, professional and cyber insurance. | Enterprise is "by contract", but the wallet-only prepaid model and the missing indemnity and insurance position block most corporate buyers. |
| A13 | Medium | Creator-side cancellation, disputes and chargebacks | Creator cancels a paid order before or during rendering (refund amount), a "not what the storyboard showed" dispute route, and chargeback handling (wallet hold, negative balance, account review). | Only staff-side cancellation and fraud mitigation are described; these cases cause the most payment complaints. |
| A14 | Medium | Payment-gateway failover | A second Bangladeshi gateway or direct bKash/Nagad merchant API as fallback, plus an outage mode in which wallet spending continues while top-ups pause. | All Bangladesh money runs through one aamarPay account in another company's name; one outage or account freeze stops all sales. |
| A15 | Low | Hosted public pages and embeds | View and bandwidth limits per package for the shoppable page, interactive-player embeds, review links and the verification tool; hotlinking rules; abuse and phishing takedown for pages on our domain. | These pages make Motion Studio a free video host and a phishing surface unless limits and a takedown path exist. |

---

## GOAL B — Admin control gaps

### B.0 How to read this

- Owner rule: every user-visible value and every feature is an admin setting, marked "(default)", changed with two-person approval and logged.
- **N** = the plan does not say the value or feature is admin-controllable.
- **P** = the plan says "(default, editable)" or "admin setting", but no admin page in chapter 13 (or 14) describes where it is controlled.
- Chapter 13 describes the following pages in detail: Dashboard, Packages & features, Prices and rates, Wallet, Orders/render queue, Moderation, Consent registry, Licence library, Models, Support inbox, Roles, Co-Admin and Notifications. "Growth" and "Operations" appear only as rows in the area map, with no detail section. None of the 30 October 2026 additions after the package placement are in the chapters.

### B.1 Packages & features matrix (10)

| # | Item | Status | Note |
|---|---|---|---|
| 1 | A separate **Free Beta** column ("all features within daily limits", owner 30 Oct) | N | 6.4 merges Trial/Beta and shows "—" for many features, which conflicts with the owner decision; O39 is out of date |
| 2 | A **permanent watermarked free tier** column (approved 30 Oct) | N | Not in 6.2 or 6.4 |
| 3 | **Per-feature daily caps** for the Free Beta and the free tier ("limits from admin") | N | The matrix has cells but no daily-cap dimension |
| 4 | Rows for about 45 features approved on 30 Oct: Scene Bible, deeper emotion engine and director controls, version control, visual storyboard editor, live cost estimate, co-editing (Yjs), approval chains, Shopify/WordPress plugins, brand tone of voice, custom style LoRA, carbon estimate, motion brush, webcam acting, Remix-this, Middle East pack, browser RIFE, multi-camera, faceless autopilot, diaspora messages, shoppable player, event-triggered videos, HubSpot/Salesforce, quality score, live 3D avatar streaming, style analysis, stock-clip sales, verification tool, character personality, cultural adaptation, brand price list and claim check, Quality Checked badge, AI Producer, AI Co-Director, Free Course, cross-course offers, media library, 30-day trash, affiliate, reminders, stock presenters, single-shot clips, screen recording, stock media, annual packages, footage clean-up, edit-by-transcript, restyle, virtual try-on, voice design and SFX, stills, workspace controls | N | Package placement for most of these is not decided either |
| 5 | **Team seats per package** and the extra-seat price | N | 5.5.1 says "team size per package is in chapter 6", but chapter 6 has no such row |
| 6 | **Per-account or per-contract overrides** (Enterprise, pilot businesses, agencies) | N | 13.4 names an Enterprise column, but there is no override page like NexaTute's per-institution overrides |
| 7 | **Closed-pilot cohort settings**: feature set, test payments or real payments, end date | N | O31 lists only the names |
| 8 | **Country and age scoping** of features: Middle East pack, clone/twin per country, live avatar | N | NexaTute has product switches by country and age; Motion Studio does not |
| 9 | A **"legal hold" feature state** separate from "coming soon": clone, twin and face acting in the Beta only after the lawyer check | N | It needs the sign-off evidence attached before the feature can go live |
| 10 | Matrix hygiene: drama row (O35), duplicate analytics rows (O36), "To confirm" cells | P | These must be settled before the page is seeded |

### B.2 Prices & billing (14)

| # | Item | Status | Note |
|---|---|---|---|
| 1 | **Conversion and rounding parameters** as editable formula inputs: +35% international, ৳122 = $1, Islamic −25%, ".5 up", Cinematic +35%, the flat +৳10 exception, the 4K ladder ratio | N | 13.5 recalculates values but does not say the parameters themselves are settings |
| 2 | **Exchange-rate policy**: quarterly market check and rate source | N | Approved 30 Oct; not in 13.5 or 14 |
| 3 | **INR / PKR / AED / SAR price lists** | N | Approved 30 Oct |
| 4 | **Annual packages**: discount, refund and renewal rules | N | |
| 5 | **Billing lifecycle**: proration on upgrade, downgrade at the next cycle, one-click cancel, 3-day grace, renewal-reminder schedule, auto-renew methods | N | NexaTute has a billing lifecycle in its Plans & prices editor |
| 6 | **Remake levels R1–R5** (%, limit per video) | N | In 7.9 only |
| 7 | **Free allowances**: number of free storyboard revisions (value not set), 3 free regenerations per scene per day, 1 free region repair per video, +10% length tolerance | P | Marked "editable" in chapters 3, 4 and 7; no page |
| 8 | **Derived-output billing rules**: auto-dubbing 50%, multi-language pack price, extra aspect ratios, multi-camera billed per angle, hook variants, promo cuts at the Quick rate, intro/outro billed once, series-autopilot drafts free until export | N | |
| 9 | Purchased-credit validity (30 days), minute-pack validity and discount, pay-per-video mark-up | P | O3/O4 |
| 10 | **Metering unit** (seconds-to-minutes conversion, minimum billable unit) | N | Referred to as "approved" in 7.1 but not set anywhere |
| 11 | Prices for new items: live 3D avatar streaming per hour, custom style LoRA fee, external stock-clip prices, licensed stock-media pass-through, stock-presenter fee, voice-over-only rate | N | |
| 12 | NexaLogicDev credit conversion (৳5 = 1 credit) | N | |
| 13 | **Enterprise rate cards / contracts** page (custom rates, SLA, credit terms) | N | |
| 14 | Festival early-order discount amount and window | P | 13.7 has the window; the amount is "to confirm" |

### B.3 Wallet & refunds (9)

| # | Item | Status | Note |
|---|---|---|---|
| 1 | **Refund-policy values** as settings: 0–30 day rule, outage restore within 24 h, extension of expiring credits | N | 7.17 only |
| 2 | Late Normal/Slow orders: full or partial refund (to confirm) | P | **Inconsistency:** 10.7 and 15.6 say "credit", 7.6 says "automatic wallet refund" |
| 3 | Express late threshold (20% beyond the ETA) | P | Rate not settable as described |
| 4 | Top-up minimum and maximum, maximum wallet balance, top-up methods | N | Also relevant for the e-money check |
| 5 | **Default spending cap** for new accounts and for API, bulk, catalogue and autopilot orders | N | Only a creator-set cap exists |
| 6 | Refund destination: original payment method or wallet | N | "To confirm" in 7.17 |
| 7 | Wallet balance on account closure or deletion; dormant balances | N | |
| 8 | Promotional credit (gift card, referral, challenge prize) kept separate from paid credit, with expiry | N | |
| 9 | Chargebacks: wallet hold, negative balance, recovery | N | |

### B.4 Limits & quotas (14)

| # | Item | Status |
|---|---|---|
| 1 | Daily reset time (00:00 Bangladesh time, fixed in 8.2) | N |
| 2 | Beta videos per day (4 + 4) and scripts per day (3) | P |
| 3 | Permanent free-tier limits | N |
| 4 | **AI Co-Director daily messages per package** | N |
| 5 | Faceless-autopilot daily cap | N |
| 6 | Bulk personalised videos: recipients per batch and per day | N |
| 7 | Catalogue import: products per batch | N |
| 8 | Multi-language pack: maximum languages per order | N |
| 9 | Number of hook variants (3) and hero candidates (2) | N |
| 10 | Device-tier thresholds (4 GB / 3 GB RAM) and Data Saver default | N |
| 11 | Review-link expiry 30 d, delivery link 72 h, trash 30 d, storage warnings 80/95%, 30-day keep after a package ends | P (chapter 11, no page) |
| 12 | API rate limits and quotas per package | P |
| 13 | AI thumbnail/image daily limit (memory: admin daily AI-image limit) | N |
| 14 | Character and series LoRA trainings per month, night GPU-minute cap | N |

### B.5 Safety & moderation (12)

| # | Item | Status |
|---|---|---|
| 1 | Enforcement ladder: number of warnings, suspension length, when a ban applies | N |
| 2 | **Islamic AI-confidence threshold for auto-approval** (it drives the 25% discount), verified Quran/hadith text editions, reviewer-assignment rule, queue-alert limit (to confirm) | N/P |
| 3 | Sensitivity of the content-plan mismatch guard | N |
| 4 | **Election-period mode**: dates, candidate list, strictness | N |
| 5 | Public-figure list and the permission-proof queue | N |
| 6 | Ad-policy and claim-check rule sets (Meta/Google policy versions; brand price list and offer rules) | N |
| 7 | Known-source copyright blocklist (Chromaprint); logo-detection sensitivity | N |
| 8 | Faceless autopilot: source requirements and copied-text threshold | N |
| 9 | "Quality Checked" badge criteria and pre-publish quality-score thresholds | N |
| 10 | Report-button categories; appeal SLA (3 working days); takedown timer (24 h) as settings | P |
| 11 | AI Co-Director content policy: topic limits, medical/legal/financial disclaimers, crisis routing | N |
| 12 | Legal-request queue (see A6) | N |

### B.6 Consent registry (10)

| # | Item | Status |
|---|---|---|
| 1 | Consent-sentence templates per language | N |
| 2 | OTP validity and resend; speaker-verification match threshold | N |
| 3 | Minimum recordings: 3-minute base reading, 3 required emotions, ~2-minute twin video | N |
| 4 | Stock-presenter and voice-artist releases (term, territory, revocation) | N |
| 5 | Consent records for webcam acting transfer and face acting | N |
| 6 | Proof documents for public figures and heirs of deceased persons | N |
| 7 | **Lawyer-gate switches** with sign-off evidence (clone, twin, face acting; imo; LoRA on non-owned images) | N |
| 8 | Marketing and showcase consents (sample gallery, challenge winners, case studies) | N |
| 9 | Bulk-message recipient-consent declarations and opt-outs | N |
| 10 | Cross-course-offer consent ("personalised offers") and "don't show again" | N |

### B.7 Models & quality (11)

| # | Item | Status |
|---|---|---|
| 1 | Prompt versions with rollback (Langfuse, as in NexaTute) | N |
| 2 | Model fallback order and quality-regression thresholds (approved 30 Oct) | N |
| 3 | AI Co-Director model, persona, memory retention | N |
| 4 | AI Producer agent roles and steps | N |
| 5 | Cloud LLM fallback on/off and cap; cheapest-spot cloud GPU cap | P |
| 6 | Browser/server placement switches (VITS previews, browser RIFE, device routes) | P |
| 7 | Loudness targets and mastering presets | N |
| 8 | Blind viewer panel: members, rounds, pass rule ("not worse") | N |
| 9 | LoRA training queue (character, series, Enterprise custom style) | N |
| 10 | Factors for the energy and carbon estimate | N |
| 11 | Character-consistency KPI threshold | N |

### B.8 Integrations & channels (11) — no admin page at all

| # | Item | Status |
|---|---|---|
| 1 | Direct publishing per platform: on/off, approval status, API quota (YouTube, Facebook, Instagram, TikTok, LinkedIn) | N |
| 2 | WhatsApp/Messenger ordering bot: number, templates, on/off, AI-provider rule | N |
| 3 | **Payment gateways and methods per country and currency** (aamarPay, Paddle; bKash, Nagad, Rocket, cards) | N |
| 4 | SMS, email and WhatsApp notification providers and sender IDs | N |
| 5 | Shopify/WooCommerce/WordPress plugins, Zapier/Make, HubSpot/Salesforce | N |
| 6 | Meta one-click boost (ads permission) | N |
| 7 | YouTube Data API (trends, analytics) and Facebook analytics | N |
| 8 | **Developer platform**: API clients, scopes, keys and rotation, webhook events and signing, sandbox, idempotency | P (5.6.1 says "default, editable") |
| 9 | Paid stock-media API | N |
| 10 | NexaTute links (Nexa ID, shared wallet, SCORM, Free Course menu) and NexaLogicDev credits | N |
| 11 | Status of the C2PA signing certificate and the NCMEC hash list | N |

### B.9 Support & notifications (7)

| # | Item | Status |
|---|---|---|
| 1 | **Customer notification templates and channels**: video ready, renewal, price-change notice, reminders by the chosen channel | N |
| 2 | Support hours, night English shift, channels per package (phone from Premium Starter) | P |
| 3 | "Always to a person" escalation categories | P |
| 4 | AI support assistant: on/off, languages, hand-over rules | N |
| 5 | Satisfaction prompt and the "what went wrong" options | N |
| 6 | Webinar schedule and tutorial library | N |
| 7 | Customer maintenance and incident notices; approval of status-page text | N |

### B.10 Content & texts (8) — no page beyond "Landing page and CMS"

| # | Item | Status |
|---|---|---|
| 1 | UI strings and translation management (bn/en now, 6 languages later; AI translation plus human check) | N |
| 2 | Tooltips | P (9.3 says "text admin-editable") |
| 3 | Labels and warnings: "AI voice", "Made with AI", inauthentic-content warning, ad-policy disclaimer, busy-page message, "Remix this" text | N |
| 4 | **Legal page versions with acceptance log and re-consent** | N |
| 5 | Sample gallery: labels and permissions | N |
| 6 | **Bangladesh days and festival calendar** (Eid dates move each year) for the content calendar and the festival guard | N |
| 7 | Public pages: trust page, model cards, verification tool, shoppable-page templates | N |
| 8 | Text of business packs and templates | N |

### B.11 Accounting (5)

| # | Item | Status |
|---|---|---|
| 1 | Daily actual exchange-rate table with source and timestamp (approved 30 Oct) | N |
| 2 | Revenue-recognition point (at approval or at delivery) as a setting | P |
| 3 | Liability treatment of promo credit, gift cards and referral credit | N |
| 4 | Payout settings (affiliate, marketplace, challenge prizes, resellers), including tax withholding | N |
| 5 | VAT rate page per product tag and country | P |

### B.12 Co-Admin / AI assistants (7)

| # | Item | Status |
|---|---|---|
| 1 | Command bar (Ctrl+K, text/voice): on/off, voice input | N |
| 2 | Morning briefing: time, content, recipients | N |
| 3 | Anomaly alerts: sensitivity and reason text | N |
| 4 | Forecasts and the "what-if" price simulator: who may use them; the simulator can never publish; uncertainty range shown | N |
| 5 | "Why?" explanations and one-click fixes (the approval path they use) | N |
| 6 | Dark/glass theme default, mobile admin, passkey approvals | N |
| 7 | Settings for the customer-side assistants (Co-Director, AI support, AI insights, weekly AI analyst) | N |

### B.13 Security & access (8)

| # | Item | Status |
|---|---|---|
| 1 | **Customer login security**: OTP wait and daily limit, lockout, session length, maximum devices, sign out of all devices | N |
| 2 | Customer 2-step/passkey requirement and the **"large spend" re-check amount** | N |
| 3 | OTP / SMS-pumping protection (Turnstile, per-IP and per-number limits, SMS spend cap) | N |
| 4 | Free-trial abuse rules (device-check sensitivity) | N |
| 5 | Enterprise SSO, per-client data isolation, EU data-residency option | N |
| 6 | **Data-retention schedule page** and legal holds | P (11.10 says the values are settings) |
| 7 | Data-request queue (export, deletion) and the DPA register | N |
| 8 | Security & Control Centre tab with the release-gate evidence (17.4) | P |

### B.14 Growth / marketing (10) — area-map row only, no detail section

| # | Item | Status |
|---|---|---|
| 1 | Landing-page CMS and live prices | P |
| 2 | Motion Studio journeys and marketing message caps and quiet hours | N |
| 3 | Referral and affiliate programme settings | N |
| 4 | Coupons, promo codes, gift cards | N |
| 5 | Creator challenge: theme, prizes, rules, judging | N |
| 6 | **Free Course menu link and cross-course suggestions** (3 suggestions, once, first-course discount) | N |
| 7 | "Remix this" watermark on free videos | N |
| 8 | Middle East pack and diaspora-message switches | N |
| 9 | Reseller and white-label account management (packs, KYC, branding) | P |
| 10 | Public showcase and sample gallery | N |

### B.15 Operations (extra group, 7) — area-map row only

| # | Item | Status |
|---|---|---|
| 1 | Degradation-ladder thresholds (L1 at 80% …) and lend/borrow floors (25% floor, 50% borrow) | N |
| 2 | Maintenance window and software-updates panel | P |
| 3 | Admission cap, waiting room and capacity guard (2,000 CCU, ≤70%) | P |
| 4 | Stuck-job heartbeat threshold | P |
| 5 | Service budgets (SMS, WhatsApp, email, AI APIs, stock API) | P |
| 6 | SLO targets and the DR-drill schedule | N |
| 7 | Status page | P |

**Total: 143 values or features with no clear admin control (B.1–B.15).**

### B.16 The 10 most important uncontrolled items

1. **Free Beta / free-tier columns and per-feature daily caps.** The owner's "Beta = all features within daily limits" has no controls, and the current matrix contradicts it.
2. **Discount and offer engine**: coupons, promo codes, gift cards, referral, affiliate, annual packages, first-course discount and the stacking rule. There is no page at all.
3. **Billing rules**: remake R1–R5, free revisions and regenerations, the 10% length tolerance, derived-output billing, credit validity, metering unit.
4. **Currency and conversion rules**: +35%, ৳122, rounding, the exchange-rate review, and the EUR/GBP/INR/PKR/AED/SAR lists.
5. **AI Co-Director settings**: model, daily message limits per package, memory retention, topic policy, on/off.
6. **Voice and language library**: library, dialect and child voices, emotion sets, the per-language quality-gate switch for new dubbing languages, the global pronunciation dictionary. NexaTute has an Avatar & Voice Studio; Motion Studio has nothing.
7. **Integrations and payment routing**: publishing platforms, the WhatsApp ordering bot, gateways and methods per country, SMS/email senders, plugins, and the developer platform (keys, rate limits, webhooks).
8. **Islamic auto-verification threshold and verified-text sources.** These decide both religious accuracy and the 25% discount.
9. **Customer account security and fraud settings**: OTP limits, lockouts, devices, the 2-step requirement, the large-spend re-check amount, SMS-pumping protection, trial-abuse rules.
10. **Legal pages and customer-facing texts**: Terms/Privacy versions with acceptance log, consent-sentence templates, labels and warnings, tooltips, translations, the festival calendar.

---

## Proposed minimal admin page set (19 pages)

The pages below copy the NexaTute X10/X14–X17/X21/X22/X25/X27 pattern. "Existing" means chapter 13 already describes the page; "Extend" means it exists and needs the gaps above added; "New" means it has to be designed.

| # | Page | One line | Status |
|---|---|---|---|
| 1 | Command Centre & Co-Admin | Live dashboard, Ctrl+K command bar, morning briefing, anomalies, forecasts, what-if simulator, "why?", Co-Admin settings and chat channels | Extend (13.3 + 13.14) |
| 2 | Packages & features | Matrix with Free Beta and free-tier columns, per-feature daily caps, global/legal-hold switches, country/age scope, per-account and per-contract overrides, comparison page | Extend (13.4) |
| 3 | Prices & billing rules | Rate table, formula parameters and rounding, currencies and exchange-rate review, annual and billing lifecycle, remakes and free allowances, derived-output billing, add-ons, Enterprise rate cards | Extend (13.5) |
| 4 | Offers, partners & payouts | Coupons, promo codes, gift cards, referral, affiliate, reseller packs, festival discount, cross-product offers, **stacking rule and price floor**, payouts | New |
| 5 | Wallet, refunds & payments | Wallet rules and limits, refund-policy values, default caps, chargebacks, refund destination, gateways and methods per country | Extend (13.6) |
| 6 | Limits, trials & capacity | Trial, Beta and free-tier limits, daily reset, per-feature caps, AI message limits, device tiers, admission cap and capacity guard, degradation ladder | New (parts in 13.5/13.7) |
| 7 | Orders & render queue | As described | Existing (13.7) |
| 8 | Trust & safety | Policy and term lists, queues, enforcement ladder, election mode, Islamic thresholds and sources, public-figure list, claim and ad-policy rule sets, takedowns, **legal-request queue** | Extend (13.8) |
| 9 | Consent & rights registry | Voice, face, twin and acting consents, talent releases, proof documents, consent templates and thresholds, marketing and messaging consents, **lawyer-gate switches** | Extend (13.9) |
| 10 | Libraries & languages | Voices (dialect, child, emotion sets), languages and their quality gates, pronunciation dictionary, characters, templates and business packs, music/SFX/images/stock with licence log, famous places | Extend (13.10) |
| 11 | AI models, prompts & assistants | Model registry and switch, prompt versions, fallback order, quality thresholds, viewer panel, LoRA queue, Co-Director / AI Producer / AI support settings | Extend (13.11) |
| 12 | Integrations & developer platform | Publishing platforms, WhatsApp/Messenger bot, SMS/email senders, plugins, Zapier/Make, CRM apps, API clients, keys, rate limits, webhooks, sandbox, NexaTute/NexaLogicDev links | New |
| 13 | Customer care & messages | Inbox, SLAs and hours, escalation categories, help centre, customer notification templates and channels, satisfaction loop, webinars | Extend (13.12) |
| 14 | Content, texts & legal pages | UI strings and translations, tooltips, labels and warnings, legal page versions with acceptance log, sample gallery, public pages, festival calendar | New |
| 15 | Growth | Landing CMS, journeys and message caps, challenge, Free Course and cross-course offers, Remix-this, Middle East/diaspora packs, resellers and white-label | New (area-map row only) |
| 16 | Operations | Software updates, load tests, backups and DR drills, incidents and status page, service budgets, cloud-burst caps, SLOs, maintenance window | New (area-map row only) |
| 17 | Accounting & finance | Chapter 14, plus the daily rate table, revenue-recognition setting, promo-credit liability, payouts and tax | Extend (ch. 14) |
| 18 | Security, access & data | Staff roles and audit log, customer login security, OTP protection, fraud rules, SSO and data residency, retention schedule and legal holds, data requests, DPA register, release-gate evidence | Extend (13.13) |
| 19 | Staff notifications & chat | As described | Existing (13.15) |

### Cross-cutting mechanism (recommended)

One **settings registry** behind all pages. Each setting carries:

- default value and "(default)" flag
- scope (global / country / currency / package / account / age group)
- effective date and notice period
- approver tier
- lock level

Lock levels:

- **L0 – Operations**: logged only. Examples: retry a job, move it to another own node.
- **L1 – Standard**: two-person approval.
- **L2 – Money**: two-person approval plus the finance lead or a founder. Examples: rates, formula parameters, refund thresholds, cloud caps.
- **L3 – Legal-gated**: two-person approval plus the lawyer or DPO, with the sign-off document attached.
- **L4 – Locked**: no admin path. Changing it needs a code change approved by the owner and, where legal, the lawyer.
- **Ratchet rule**: one admin may tighten a safety setting at once, with a second confirmation within 60 minutes; loosening a safety setting always needs L3.

---

## Values that must NOT be freely editable

### L4 — locked (no admin switch)

- Child safety: CSAM hash matching always on; zero tolerance (account closed and reported); a real child's voice or face never used, even with guardian consent; kids-safe strict filters switched on automatically for child characters; "Made for kids" set automatically.
- Consent core: live freshly generated consent sentence plus OTP; 18+ for clone and twin; twin from own face only, never one selfie; no cloning from WhatsApp voice notes; speaker verification on; staff can never play or view voice/face samples; voice or likeness not transferable or saleable.
- The "never" list: AI testimonial videos, lyric videos of others' songs, talking photo from one picture, cloning without consent, "detect any AI video" claims, "views guaranteed" claims, fake reviews, partners or numbers, scarcity wording, "copyright-safe" or "most realistic" claims.
- Provenance: C2PA signing, AI-disclosure auto-tick, the AudioSeal watermark on cloned voices — cannot be removed in any package or by any white-label agency.
- Safety features undisableable per package (13.4 list); data download and deletion rights.
- Islamic: uncertain cases never auto-approved on timeout; prayer scenes always human-reviewed; Arabic and all on-screen text always an overlay; unverified quotations never labelled "verified".
- Governance: two-person approval itself, maker ≠ checker, append-only audit log and Co-Admin log, the Co-Admin "never" list of 6, and Co-Admin can never be the second approver.
- Privacy: cells under 20 hidden; free users and personal data or voice samples never sent to cloud or spot GPUs; staff cannot raise a creator's spending cap.
- Wallet non-cash-out and non-transferable (regulatory position).

### L3 — legal-gated (lawyer or DPO sign-off attached)

- Switching on voice clone, digital twin, face/webcam acting and live avatar streaming (in the Beta and per country).
- The Co-Admin WhatsApp/Messenger/imo channels; imo stays locked until API access exists.
- LoRA training on non-owned images; FLUX.1-dev; any licence-to-verify model.
- Content-policy definitions ("anti-state", deepfake, election rules), loosening election-mode or public-figure rules.
- Retention periods: never below the legal minimum (billing 7 years, consent records 3 years, audit 7 years); the 72-hour deletion after withdrawal can only be shortened.
- Terms, Privacy, Refund and Consent page versions; DMCA agent details; country opening or closing (sanctions, tax).
- Minors and age-gate settings (see A1).

### L2 — extra money approval (finance lead + founder)

- Formula parameters (+35%, ৳122, Islamic 25%, Cinematic +35%, 4K ratio), the exchange-rate change (quarterly, as approved), the discount stacking ceiling and price floor, the margin-alert floor, cloud-burst caps, refund thresholds, VAT rates (chartered accountant only).
- Cost-allocation rules: locked for the financial year; changed only at year start with two approvals (already approved).

---

## Inconsistencies noticed while reviewing (for the next edition)

1. 6.4 / O39 treat the Free Beta like the Free Trial (many "—"), but the owner decided on 30 Oct that the Free Beta includes ALL features within daily limits.
2. Late Normal/Slow delivery: "credit" in 10.7 and 15.6, "automatic wallet refund" in 3.2.2, 7.6 and 7.8.
3. 5.5.1 points to chapter 6 for team size per package; chapter 6 has no such row.
4. 13.4 lists an Enterprise column; 6.4 leaves Enterprise out, and there is no override mechanism.
5. "Free Beta 30 days" and "permanent watermarked free tier" (30 Oct) are not reconciled with 8.1 ("after the Free Beta, new users get the 7-day trial").
6. 13.8 queue-alert limit is still "(to confirm)", and 13.1 says admin pages work "in Bangla and English", while the prototype hard rule is 6 languages on every board. The prototype boards will need all 6 even if launch admin is bn/en.

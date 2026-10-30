# Default solutions for the 10 open gaps (review3, section B)

Date: 30 October 2026. Prepared by Claude as proposals for the owner; not legal advice. Every value below is "(default, editable)" unless it repeats an owner decision. Built to fit the owner's decisions of 30 October 2026: P1 (pay per order / per plan, no stored balance), Motion Studio under-18 mode (guardian account, forced kids-safe, no clone/twin/face acting/bulk/API/publishing, US under-13 blocked, cross-offers 18+ only), protected settings (3 approvals + 24-hour delay, rollback, Co-Admin never approves), "a person decides" on every dispute, takedown, appeal and legal request, one marketplace for 3 products (no personal clones or twins listed), company-paid bulk messages with caps through the client's own sender identity, USA LLC via doola.com only after FX approval, and "everything admin-controllable, including which person or team does which job".

Approval levels used below (settings registry): **L1** = two-person approval; **L2** = L1 + finance lead or founder; **L3** = L1 + lawyer or DPO sign-off attached; **P** = protected setting (3 approvals: founder + security/compliance owner + one more; reason with law reference; 24-hour delay with cancel; rollback; a protected value quoted in a legal page changes only after the page is updated and its notice period has run; the urgent path may only tighten).

## Summary

| # | Gap | Default solution in one line | Main admin page |
|---|---|---|---|
| B1 | Age assurance for 18+ features | One-time adult check (ID + selfie match, image deleted in 24 h, or a provider-confirmed adult payment account) before the first clone, twin, face acting, selling, bulk send or API key | Consent & rights registry |
| B2 | Nexa ID cross-product rules | Age band and guardian link follow the person into every product; consent stays per product; only identity, age band, guardian link, language and receipts are shared; per-product and whole-ID deletion | Security, access & data |
| B3 | International merchant-of-record fallback | Apply to Paddle and one second MoR in parallel; per-country checkout router; switch within 1 day if one declines | Payments & refunds |
| B4 | Marketplace operating model | RemonLogic = operator and agent for outside sellers (seller of record for its own items); PSP/escrow settlement; seller KYC and sanctions checks; one refund rule; under-18s see NexaTute items only | Offers, partners & payouts |
| B5 | Business verification (KYB) tiers | Four tiers (individual, business basic, business verified, credit) that unlock bulk sends, API, white-label and post-paid invoices step by step | Trust & safety |
| B6 | App-store billing | Phase 1: free companion apps with no in-app purchase or purchase prompts; Phase 2 (owner choice): packages as store subscriptions at +30%, per-order charges never sold in-app | Prices & billing rules |
| B7 | Approver roster, delegation, break-glass | Named primary + deputy for every approval role; quorum rules; a "tighten-only" emergency route when the founder is unreachable | People, teams & job assignment |
| B8 | Human operations capacity plan | Queue-by-queue owners, severity SLAs, a launch roster, night and on-call cover, pilot measurement before public promises | People, teams & job assignment |
| B9 | Privacy of viewers and end customers | Client = controller, RemonLogic = processor with a standard DPA in every package; cookieless aggregated analytics; pixels only with consent banner; fixed retention | Security, access & data |
| B10 | Wind-down and exit plan | 90 days' notice (30 for free), export window, free one-time re-render on a successor model, pro-rata refunds to the original method; clones and twins never exported | Operations |

---

## B1. Age assurance for 18+ features

- **When:** once per account, before the first use of any 18+ feature: voice clone, digital twin, face or webcam acting, marketplace selling, bulk sends, API keys and the adult ("any subject") Co-Director mode. A typed date of birth alone never unlocks them. Passkey re-check before each clone, twin, publish or large spend stays as approved.
- **Methods (user chooses one):** (a) NID or passport photo plus a live selfie match, run on RemonLogic's own servers (never an outside AI or spot GPU); the document and selfie images are deleted within 24 hours and only the result, method, date and a hash of the document number are kept (default, editable); (b) a payment-account check, counted only where the provider confirms an adult account holder (for example an NID-registered bKash account or a credit card), done as a ৳10 authorisation voided at once (default, editable) [aamarPay to confirm what it can return].
- **Result handling:** pass = 18+ features unlock (still behind the lawyer gate for clone, twin and face acting); "under 18" or name mismatch with the consent speaker = account moves to under-18 mode and the guardian is invited; disputes go by email to the Consent & likeness team, a person decides.
- **Re-check:** when the account's phone, legal name or payment identity changes, or after a risk signal (consent complaint, report of a minor) (default, editable).
- **Data protection:** DPIA covering the selfie match; biometric template not stored; counts-only reporting.
- **Admin:** Consent & rights registry (methods, triggers, retention — L3); the 18+ list and the "typed DOB is never enough" rule are protected settings (P); retention shown in Security, access & data.

## B2. Nexa ID cross-product rules

- **Person-level attributes:** one Nexa ID per person. Date of birth, age band and the guardian link belong to the Nexa ID and apply in every product; the stricter product rule wins. An under-18 NexaTute learner is automatically in Motion Studio's under-18 mode; NexaLogicDev is 18+ only (default, editable; owner to confirm), because it uses outside AI APIs that children's data never reaches.
- **Consent per product:** accepting one product's terms or consent switches never carries over. On first entry to another product the user (or guardian) sees that product's terms and its own switches.
- **What is shared:** login identity, age band, guardian link, preferred language and payment history (for receipts). Never shared: learning records, recordings, Co-Director chats, project content, voice or face data, interest data. The 18+ free-course suggestions use only data the adult consented to (approved).
- **Deletion:** "delete this product" removes that product's data and keeps the Nexa ID; "delete my Nexa ID" removes all products after cancelling active packages with pro-rata refund to the original method. Legal minimums stay (billing 7 years, consent records 3 years) with a legal hold flag.
- **Offers:** cross-product offers and suggestions only to 18+ Nexa IDs (owner decision); the check reads the person-level age band, so a child cannot be reached through another product.
- **Admin:** Security, access & data (sharing matrix and deletion rules; the age, guardian and sharing items are P); Content, texts & legal pages (per-product terms and consent texts, L3).

## B3. International merchant-of-record fallback

- **Apply in parallel:** Paddle and one second merchant of record (FastSpring by default, 2Checkout/Verifone as third choice) in RemonLogic Private Limited's own name, each told in writing about the AI voice, avatar and twin features [acceptance of a Bangladeshi seller and of these features to confirm with each]. A USA LLC via doola.com is used only after the FX opinion and approval.
- **Checkout router:** a per-country table decides Paddle, the second MoR, aamarPay international cards (only where doola has cleared the country) or "available soon". One MoR per customer subscription, so a customer is never split across two.
- **Failover:** if a MoR declines, suspends or holds payouts, new international checkouts switch to the other within 1 working day; existing subscribers move at their next renewal with 30 days' notice and fresh auto-renew consent.
- **Same rules everywhere:** P1 (no stored balance), refunds to the original method, the same USD/EUR/GBP price table (USD = Taka × 0.015 rule; exchange rate reviewed every 3 months with two-person approval), EU/UK 14-day right in every MoR's checkout.
- **Local counterpart:** the owner's second payment gateway is the Bangladesh fallback for aamarPay under the same router.
- **Admin:** Payments & refunds (router and failover — L2; opening a country — L3); Accounting & finance (payout reconciliation, export receipts, Form-C).

## B4. Shared marketplace operating model

- **Role:** RemonLogic is the marketplace operator and the sellers' commercial agent for outside sellers (the seller is the seller of record), and the seller for its own items; commission 20% as approved [lawyer to confirm agent status and VAT on commission vs gross].
- **Money flow (P1):** the buyer pays per item through the licensed PSP checkout; the seller's share is settled through the PSP or an escrow arrangement as the Bangladesh Bank e-commerce circular requires, released after delivery and the 7-day refund window, paid monthly to a verified bank or MFS account in the seller's name; minimum payout ৳500 (default, editable). No buyer balance exists.
- **Seller checks:** NID or trade licence, payout account in the same name, TIN where required, sanctions screening; foreign sellers: passport or company documents, sanctions screening, tax form; withholding at source as the accountant sets.
- **Listing rules:** licence declared per item; hash and audio-fingerprint checks; model releases for any real person; personal voice clones and digital twins never listed; Islamic items go through Islamic review; 24-hour takedown and the repeat-infringer ladder apply to sellers.
- **Buyers:** one refund rule across products (7 days if not downloaded or opened; any time if not as described); under-18 profiles see only NexaTute learning items, each needing guardian approval; no other-product or third-party listings shown to them.
- **Admin:** Offers, partners & payouts (seller programme, commission, payout schedule — L2); Trust & safety (listing review, takedowns); Accounting & finance (VAT, withholding); Packages & features (marketplace switch on legal hold until the lawyer signs off — L3).

## B5. Business verification (KYB) tiers

- **Tier 0 — Individual:** phone OTP + device check. Free account, Free Beta, normal paid orders.
- **Tier 1 — Business basic:** business name, a trade licence or registration number, website or business page check, and one payment in the business's name. Unlocks business packs at scale, hosted shoppable pages, order QR, Zapier/Make, and company-paid bulk sends at a reduced cap (500 recipients a send, 2,000 a month; default, editable).
- **Tier 2 — Business verified:** trade licence document, TIN or BIN, named authorised person passing the B1 check, payout or payment account in the business's name. Unlocks API keys, event-triggered videos, the full bulk-send allowance, white-label and regulated-business sectors (recruiting, health, finance, education — plus the automatic licence check and human review; never labelled "verified").
- **Tier 3 — Credit:** Tier 2 + 6 months' clean history or an Enterprise contract + finance approval + a credit limit. Unlocks the monthly business invoice (post-paid) and per-client data isolation.
- **Ongoing:** yearly re-check; automatic step-down on risk signals (spam-report rate above 0.3% of recipients, a chargeback, a failed licence check; default, editable), which freezes the unlocked features but never deletes data; the client can dispute by email and a person decides.
- **Admin:** Trust & safety (KYB queue, tier rules — L1, loosening L3); Limits, trials & capacity (caps per tier — L1); Integrations & developer platform (API keys only for Tier 2+); Accounting & finance (credit limits — L2).

## B6. App-store billing (Motion Studio and NexaLogicDev apps, Q2 2027)

- **Phase 1 default — companion apps:** the apps are free companions to the web service: sign in, create, preview, approve storyboards already paid on the web, download, notifications. No purchase inside the app and no buttons or wording that push users to buy outside it (Apple's free stand-alone companion-app route; Google Play equivalent) [to confirm against current store rules before submission]. Orders that need payment show "finish this order on the web" only where the store and local law allow such a link.
- **Phase 2 (owner's choice later):** packages sold as auto-renewing store subscriptions at +30% on a separate line (the NexaTute rule), with guardian approval (Ask to Buy / Family Link) for under-18s. Per-order video charges are never sold in-app as stored packs or credits (P1).
- **Refunds:** store purchases are refunded through the store; the terms say so; web purchases keep the RemonLogic refund rules.
- **Feature parity:** clone, twin and face acting capture stays web-only until each store's AI-likeness policy is checked.
- **Admin:** Prices & billing rules (store uplift, store product mapping — L2); Packages & features (per-platform availability — L1); Integrations & developer platform (store accounts and keys).

## B7. Approver roster, delegation and break-glass

- **Named roster:** every approval role has a primary and a deputy: L1 any two trained admins; L2 finance lead + founder (deputy: a named director [to insert]); L3 DPO or lawyer + one admin; P founder + security/compliance owner + a third named person (default: the DPO), each with a named deputy. Co-Admin can propose, never approve; maker ≠ checker; one person never fills two seats.
- **Delegation:** a deputy acts only when the primary is marked away in the leave calendar or has not answered within 12 hours (urgent) or 72 hours (normal) (default, editable); every delegated approval is labelled and shown to the primary on return.
- **Quorum health:** the system warns when any role has no available primary or deputy for more than 48 hours, and holiday cover (Eid, Puja, year-end) is planned 30 days ahead; batched approval sessions twice a week for non-urgent changes.
- **Founder-unavailable emergency route (break-glass):** for a live child-safety case, fraud, security breach or binding legal order, the security/compliance owner and the on-call lead together may only tighten or stop (suspend an account, take down content, pause a feature, freeze payouts, block a country). Never loosen, never move money out, never change prices. Separate sealed log, all admins notified at once, auto-expires after 72 hours unless the founder (or the P quorum) confirms it.
- **Admin:** People, teams & job assignment (roster, deputies, leave); Security, access & data (break-glass passkeys and sealed log); Staff notifications & chat (alerts). Changes to the P-level roster are themselves P; other roster changes L1.

## B8. Human operations capacity plan

- **Every "a person decides" step becomes a named queue** with an owning team, primary, deputy and severity SLA (see the new page below). The AI handles first line everywhere; it never makes the final decision.
- **Launch roster (default, editable; headcount and budget by the owner):** support lead + 2 day agents (Bangla/English) + 1 night English agent (approved); 2 named Islamic reviewers; trust & safety lead + 1 reviewer; part-time DPO; on-call rota of 4 (CTO, lead developer, trust & safety lead, owner); outsourced or part-time trust-and-safety night cover for S1 only [lawyer question 13.5.7].
- **Night and weekend:** human cover only for S1/S2; S3/S4 wait for the day shift and the customer is told the expected time.
- **Measure before promising:** the 2-week pilots record volume per 1,000 active users for each queue; public pages show response times only after 4 weeks of measured data. Until then they say "we aim to …".
- **Overload rule:** when a queue passes 80% of its SLA budget, intake slows (longer ETA shown, Islamic discount routing paused, new-feature switch-ons paused); nothing is ever auto-approved because of a backlog.
- **Admin:** People, teams & job assignment (queues, shifts, SLAs, workload); Customer care & messages (customer-facing times); Operations (on-call incidents).

## B9. Privacy of viewers and end customers

- **Roles:** for hosted pages, review links, shoppable player, embeds, personalised and event-triggered videos and SCORM, the client is the controller and RemonLogic the processor; RemonLogic is controller only for security and abuse prevention. A standard processor agreement (DPA) is part of the Terms for every package, free included; Enterprise gets a negotiated DPA.
- **Cookies and tracking:** hosted pages use only strictly necessary cookies by default; built-in analytics are cookieless and aggregated (views, plays, clicks; no cross-site identifiers, IP truncated). Pixels (Meta, Google) only if the client switches them on, and then a consent banner shows for every viewer; free-account pages are noindex and pixel-free.
- **Retention:** raw view and click logs 90 days, aggregates while the project exists; sales-tracking events with hashed IDs 12 months; personalised-video recipient lists 30 days after the send; event-trigger payloads 30 days.
- **Children:** pages and videos marked kids-safe or made by under-18 profiles carry no pixels and no click tracking; SCORM learner data goes only to the client's LMS.
- **Viewer rights:** every hosted page has a "Privacy" link naming the client and the privacy address; RemonLogic forwards a viewer's request to the client within 72 hours and helps the client answer.
- **Admin:** Security, access & data (retention, DPA register — L3); Integrations & developer platform (pixels, embeds); Content, texts & legal pages (hosted-page privacy notice and DPA text — L3); Trust & safety (report button).

## B10. Wind-down and exit plan for customer assets

- **Notice:** withdrawing a paid feature, model, provider or product = 90 days' notice in the app and by email (30 days for free features); immediate only for a legal order or a safety emergency, with an explanation.
- **Export window:** during the notice period and 30 days after: download videos, project files (JSON and FCPXML), captions, Brand Kit and hosted-page content. Voice clones and digital twins are never exported (consent is bound to the account): the user may delete them or re-create them on a successor model with fresh consent. A client's own style LoRA is exported only for Enterprise under contract.
- **Models:** pinned model versions for Enterprise stay at least 12 months after a deprecation notice; when a model is retired, every active project gets one free re-render on the successor with a side-by-side preview and a "may look different" note.
- **Money (P1):** prepaid annual packages refunded pro rata for the unused part to the original method; paid but undelivered orders refunded 100%.
- **Pages, embeds and API:** 90 days' notice, deprecation headers on the API, redirects; after closure a neutral notice page for 6 months. A whole-product shutdown adds a deletion certificate; consent records kept the legal 3 years.
- **Admin:** Operations (deprecation schedule and notices); Packages & features (retirement switch — L1, or L3 when a legal page changes); AI models, prompts & assistants (pinning and successor mapping); Payments & refunds (pro-rata refunds — L2); Content, texts & legal pages (notice texts).

---

## New admin page: People, teams & job assignment

Shared by both products (filter by product). It answers one question for every piece of work: **who handles it, who covers, how fast, and who is told if it slips.**

### 1. Directory

- Every staff member, contractor and outsourced provider: role, team, products, languages, time zone, working hours, leave calendar.
- Contract coverage flags that decide what a person may be assigned: confidentiality, safeguarding (children), data-access level, religious-review contract, disturbing-content exposure limit.
- Only people whose flags match a queue can be assigned to it; the page blocks the rest.

### 2. Teams (default, editable)

Customer support · Billing & refunds · Disputes · Trust & safety · Child safety · Consent & likeness · Copyright & takedown · Islamic review · Business verification (KYB & licences) · Privacy & data (DPO) · Legal & law-enforcement · Security · Finance · Enterprise sales · Partners & resellers · Operations on-call.

### 3. Assignment matrix

One row per queue or approval type: owning team → primary person → deputy → backup team → severity → SLA → escalation chain. Covers every queue (support, refunds, disputes, appeals, takedowns, consent complaints, licence checks, Islamic review, legal requests, Co-Director crisis escalations, CSAM reports, KYB, marketplace listings) and every approval role (L1, L2, L3, P) from B7.

### 4. Shifts and on-call

- Rota calendar: day shifts, the night English shift, weekends, public holidays; on-call pager for S1 with a primary and a secondary.
- Handover notes required at each shift change; open S1/S2 items cannot be left without an owner.

### 5. SLAs by severity (default, editable)

| Severity | Examples | Acknowledge | Act or decide | Cover |
|---|---|---|---|---|
| S1 Critical | Child safety, CSAM, imminent harm or Co-Director crisis, active fraud, security breach, emergency legal request | 15 min | Contain within 1 h | 24/7 on-call |
| S2 High | Unauthorised clone or face complaint, valid takedown notice, payment outage, account takeover | 2 h | 24 h (renders suspended at once on a valid consent complaint) | Day + night English shift |
| S3 Normal | Disputes, refunds, appeals, licence-check disputes, privacy requests, ordinary legal requests | 72 h first reply | Disputes 10 working days; privacy 30 days; legal after lawyer review | Day shift |
| S4 Low | General questions, feature requests, partnership enquiries | 2 working days | 5 working days | Day shift |

### 6. Workload view

- Live queue size, oldest item, SLA-breach forecast per team and per person; capacity (people on shift) against demand.
- Round-robin with skill matching; reviewers' daily exposure to disturbing content capped; wellbeing break prompts.
- Co-Admin forecasts load for the next 7 days and can propose rota changes; it never approves them.
- Workload figures are used for planning only, never for automated disciplinary decisions.

### 7. Escalation

- Automatic at 50% / 80% / 100% of the SLA: primary → deputy → team lead → founder (or the B7 emergency route for S1 when the founder is unreachable).
- S1 pages the on-call pair at once and posts to Staff notifications & chat.
- The customer route (AI → email → person) feeds the Disputes queue directly; the AI attaches the order record and its summary, never a decision.

### 8. Founder-unavailable emergency route

As in B7: two named people (security/compliance owner + on-call lead) may tighten or stop only; sealed log; all admins notified; expires in 72 hours unless confirmed.

### 9. Contact-address routing

Each customer-facing email address set on Content, texts & legal pages is linked here to its queue and owning team, so mail for one kind of work never lands with another team.

### 10. Controls

- Queue assignments, shifts and SLAs: L1 (two-person approval, logged).
- Approver roster for L2/L3: L2; approver roster for protected settings: P.
- Every change logged with reason; Co-Admin may draft, never approve.

---

## Contact addresses (setting on "Content, texts & legal pages")

Owner decisions (30 October 2026): every customer-facing "email us" address is set in the admin panel, never hard-coded; each type of work has its own address, set per product and per language, and routed to its team on "People, teams & job assignment". Changes need normal two-person approval (L1), not protected-setting approval. Addresses below are placeholders; `[domain]` = nexatute.com or remonlogicstudio.com.

| Purpose | Example address (placeholder) | Owning team | SLA (default, editable) |
|---|---|---|---|
| Support | support@[domain] | Customer support | AI at once; person within 24 h (S4/S3) |
| Billing & refunds | billing@[domain] | Billing & refunds | First reply 24 h; refund to original method within 10 days |
| Disputes | disputes@[domain] | Disputes | First reply 72 h; decision 10 working days |
| Copyright & takedown | copyright@[domain] | Copyright & takedown | Valid notice acted on within 24 h (S2) |
| Privacy & data requests (incl. DPO) | privacy@[domain] | Privacy & data (DPO) | Acknowledge 72 h; complete 30 days |
| Consent & likeness complaints | consent@[domain] | Consent & likeness | Acknowledge 2 h; renders suspended at once on a valid complaint; decision 72 h |
| Business licence verification | licences@[domain] | Business verification (KYB) | Person reviews within 2 working days |
| Legal & law-enforcement requests | legal@[domain] | Legal & law-enforcement | Emergencies at once (S1); others acknowledged in 1 working day, decided after lawyer review |
| Child-safety reports | childsafety@[domain] | Child safety | S1: acknowledge 15 min, act within 1 h, 24/7 |
| Enterprise sales | enterprise@[domain] | Enterprise sales | 1 working day |
| Partnerships & resellers | partners@[domain] | Partners & resellers | 2 working days |
| Security disclosure | security@[domain] | Security | Acknowledge 24 h (1 h if actively exploited); triage 72 h |

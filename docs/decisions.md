# Decisions log

New owner decisions after Blueprint v32.10 (29 Oct 2026). Format: date — decision.

## 29 Oct 2026 — Remon Motion Studio per-minute rates (owner, final; replaces G.8.1/G.8.2/G.9 values)
| Package | 3D 480p / 720p Esc / 720p / 1080p Esc / 1080p | Cinematic 480p / 720p Esc / 720p / 1080p Esc / 1080p |
|---|---|---|
| Mini | ৳30 / ৳55 / ৳72 / — / ৳120 | ৳41 / ৳74 / ৳97 / — / ৳162 |
| Starter, Premium Starter | ৳30 / ৳55 / ৳72 / ৳85 / ৳120 | ৳41 / ৳74 / ৳97 / ৳111 / ৳162 |
| Professional | ৳25 / ৳50 / ৳66 / ৳78 / ৳120 | ৳34 / ৳68 / ৳89 / ৳102 / ৳162 |
| Agency | — / — / ৳62 / ৳74 / ৳120 | — / — / ৳84 / ৳96 / ৳162 |
- Cinematic 720p Native follows the +35% rule; Cinematic 1080p Escalating is a flat +৳10 (exception to the +35% rule).
- Islamic = 25% off each rate (rounded, .5 up); USD = BDT +35% at ৳122 = $1 (to the cent); Express +20% / Slow −10% / auto-dubbing 50% follow the new rates; pre-production fee unchanged.

## 29 Oct 2026 — Remon Motion Studio new features (owner approved)
1. Order a video by WhatsApp/Messenger voice note + photos; preview and payment link in the chat.
2. Bulk personalised videos: one template + CSV of names → each customer gets a video with their name (Quick mode), sent by WhatsApp/SMS link.
3. Pay-per-video without subscription (bKash), a little above package rates; minute packs (30/100 min) at 10–15% off.
4. Monthly content calendar around Bangladesh days; Slow-tier night renders; auto-publish.
5. Business packs: real estate (2.5D walkthrough), restaurant menu, tours, coaching centres, clinics; licensed businesses must show licence number.
6. Kids-safe mode (stricter filters, YouTube "Made for kids"); PlayBoom content can be made here.
7. Trend ideas from the official YouTube API.
Not offered: AI "customer testimonial" videos; lyric videos of other people's songs.

## 29 Oct 2026 — Remon Motion Studio, more approved features (owner)
- Second set: regional-dialect voices (Chittagonian, Sylheti, Noakhali, Barishal, Rangpur); automatic 360p WhatsApp-friendly copy; end-screen order QR (page / WhatsApp link / bKash merchant QR); one free region repair per video; BdSL sign-language avatar corner; invisible re-upload watermark with complaint report; white-label portal for agencies (separate licence fee). Not offered: talking photo from one picture.
- Third set: auto-edit of phone videos (silence/filler cut, noise cleanup, captions, colour) + in-browser teleprompter; product-catalogue import (Shopify/WooCommerce/CSV) → one ad per product on the Slow tier; voice-over-only audio product priced well below video; per-video sales tracking from QR/order-link clicks; one-click Facebook/Instagram boost from the creator's own ad account (Meta approval needed); monthly creator challenge; NexaTute "making videos with AI" course → Motion Studio trial/discount.
- Quality: per-character LoRA; 2 candidates for hero shots with auto pick (default on Premium); face/hand defect detection + regeneration or GFPGAN repair (CodeFormer excluded, non-commercial licence); colour matching, deflicker, stabilisation; on-screen text always an overlay; quarterly open-model benchmark, switchable from admin; Bangla pronunciation dictionary + text normalisation; DeepFilterNet cleanup before cloning; audio mastering presets; beat-synced cuts; better close-up lip-sync + automatic sync check; blind viewer rating panel before big updates.
- Child voices and emotion: child-character voices only from consenting paid adult voice artists or fully synthetic voices (boy/girl, 5–8 and 9–12, 6 languages); an adult's own clone may be made child-like; never a real child's voice, even with guardian consent; child characters get kids-safe strict filters; every library voice in 8 emotions (neutral, happy, sad, tearful, angry, afraid, whisper, excited); per-line emotion + intensity (AI suggests, creator edits); "act it yourself" performance transfer; facial expression matched to the line's emotion; viewer panel rates emotion. Clients must have a clear, easy way to choose and use voices and emotions.
- Voice Clone Studio (guided, ~10–12 min, in app only): mic test with noise meter → live consent sentence + OTP (no cloning from WhatsApp voice notes) → ~3 min natural reading → emotion cards (2–3 lines, professional example, acting tips, instant check with reason); minimum 3 emotions (neutral, happy, sad), others added later with a progress bar → preview each emotion, re-record only the weak one → "use this voice". Bangla text + voice guidance, help page, support chat, weekly webinar in Free Beta. Safety rules unchanged (own voice, 18+, account-only, deleted 72 h after withdrawal, watermark + "AI voice" label).
- Scenery: "Bangladesh scenes" LoRA trained only on own photos; per-scene reference image; famous-places library (Shaheed Minar, Sundarbans, Cox's Bazar, Sajek …) animated from real licensed photos; pre-delivery scene check with auto regeneration.
- Image sources: Wikimedia Commons (CC0/CC BY, attribution kept), Pexels (reference only), own photographer shoots (owned by RemonLogic), creators' own uploads (their videos only); every image logged (source, licence, photographer, date), removable from admin; LoRA training only on own photos until a lawyer confirms (to confirm).
- Payment at storyboard: storyboard shows estimated length + full price; "approve & pay" takes the amount from the wallet (bKash top-up if short), then rendering starts; nothing charged before storyboard approval. After render: shorter → difference back to wallet; up to 10% longer → no extra charge (10% = default, editable); failed or late → automatic wallet refund (Express late rule unchanged). Our defects fixed free; client changes charged only for changed scenes' minutes. Receipts for every charge/refund. Watermarked preview for review only.
- Risk fixes (all approved): ≤5 s shots + motion/physics defect check; Bangladeshi dress/people in the LoRA, skin tone kept from reference; Islamic: Arabic text as overlay, prayer scenes human-reviewed; crowd shots limited; FLUX licence check before launch (dev = paid commercial licence, schnell = Apache 2.0) (to confirm); Content-ID-free music or own AI music; real person's face needs consent + OTP; warn clients about platform "inauthentic content" rules; festival early-order discount + capacity limit; resume failed renders, no charge on failure; storyboard approval + fixed free revisions (default, editable); script fact check + client approval; wallet = non-cash-out prepaid credit (lawyer check) (to confirm); VAT + Mushak invoices; foreign card payments per the blueprint (aamarPay in Bangladesh, Paddle internationally); terms: client gets all rights we hold, responsible for own inputs; logo detection + 24 h takedown; voice samples encrypted separately, staff can't listen; output moderation; one free trial per phone + device check; HarfBuzz Bangla caption shaping; projects pinned to their model version; browser render resume + server fallback; emergency cloud GPU with new ETA; more Islamic reviewers addable + queue alert.
- Motion Studio admin panel must be as rich as NexaTute's.
- Motion Studio admin panel includes accounting.

## 29 Oct 2026 — RemonLogic accounting (owner)
- Each product (NexaTute, Motion Studio, later NexaLogicDev) has its own accounting books; RemonLogic gets one consolidated company report.
- Shared costs are split by each product's measured resource use (e.g. server $1,000 used 60/30/10 → $600 NexaTute / $300 Motion Studio / $100 NexaLogicDev).
- Allocation rules (approved): OpenCost metering per product — GPU seconds (per-request GPU time on shared LLM servers), CPU core-hours/RAM, R2 GB, Cloudflare bandwidth per domain, DB size/use; each bill split by its own meter; idle capacity split in the same ratio (default, editable); shared staff salaries by admin-set fixed % (default, editable); free users' cost stays with their product; month-end allocation auto-computed, posted to each book after two-person approval, logged; consolidated report eliminates internal transfers; reports: profit/loss per product, cost per user/video/class minute, monthly trend.

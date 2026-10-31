# Remon Motion Studio — Feature Catalogue (state 31 Oct 2026)

**Remon Motion Studio is RemonLogic's AI video studio: idea, script, link or voice note in, finished and labelled video out, in Bangla and 9 more languages. This catalogue lists 248 approved features in 12 areas (including the 19 admin pages and the main system rules).**

How to read it:
- Newest owner decision wins (`docs/decisions.md`, last line = newest). Older blueprint text is replaced where it conflicts.
- "Plans" uses the approved package placement (30 Oct 2026): Trial/Beta · Mini · Starter · Premium Starter (PS) · Professional (Pro) · Agency. "Mini+" = Mini and every package above it.
- **Free Beta = ALL features, within daily limits set in admin** (30 Oct). Voice clone, digital twin and face acting switch on only after the lawyer check. So "Plans" shows the paid placement after the Beta.
- Every value is admin-editable, marked "(default)", changed with two-person approval and logged.
- "(default, editable)" = a value Claude chose. "(to confirm)" = still open.

---

## Plans & prices

Source: decisions.md lines 5–13, 73, 84, 86, 113, 177–184, 203–213; memory/areas/motion-studio.md:48; motion-studio/source/06.md, 07.md

USD rule (31 Oct, all products): **USD = Taka × 1.35 ÷ 122, shown to the cent.** Every USD figure below was computed with Python (`round(taka*1.35/122, 2)`).

### Packages and add-ons

| Plan / package | Price ৳ | USD | What's included | Notes |
|---|---|---|---|---|
| Lifetime free account | ৳0 | $0 | Quick mode 3 min/month, ≤30 s each, 480p; Co-Director 10 msgs/day; 1 storyboard/day; standard voices; basic templates, captions, 360p copy; link-to-video + ad check 1/day; Brand Kit 1 logo; 1 GB | "Remix this" watermark; personal use only; no Cinematic/Enhanced, clone, twin or publishing; Upgrade button + Mini benefits page |
| Free Trial | ৳0 | $0 | 7 days, 1 min video/day, ≤15 s/video, 480p + 720p Esc, Quick + Enhanced; 1 GB | One trial per phone + device check; then the lifetime free account |
| Free Beta | ৳0 | $0 | ALL features within daily limits | 30 Jan → 20 Feb 2027; watermarked business-test licence; 21 days (owner, 31 Oct) |
| Freelancer Mini | ৳499/month | $5.52 | 480p, 720p Esc, 720p, 1080p Native; 5–45 s per video; 5 GB; 1 seat | No 4K |
| Freelancer Starter | ৳999/month | $11.05 | All tiers + 4K Esc; up to 2 min; 10 GB; 1 seat | |
| Premium Starter | ৳1,999/month | $22.12 | All tiers + 4K; up to 5 min; 20 GB; 2 seats; 1 digital twin | |
| Premium Professional | ৳3,999/month | $44.25 | All tiers + 4K; up to 10 min; 40 GB; 5 seats; 3 twins | |
| Premium Agency | ৳7,999/month | $88.51 | 720p Native and up + 4K; up to 20 min; 80 GB; 15 seats; 10 twins | White-label at a separate licence fee (amount to confirm) |
| Enterprise | Custom | Custom | By contract (quote, SSO, DPA, SLA) | Post-paid PO + credit limit only with finance approval |
| Extra team seat / month | Mini, Starter ৳199 · PS ৳299 · Pro ৳399 · Agency ৳499 | $2.20 · $3.31 · $4.42 · $5.52 | One more member | (default, editable) |
| Extra digital twin | ৳500 one-time | $5.53 | One more own-face twin | (default, editable; recheck after GPU benchmark) |
| Character or voice clone beyond 2 free | ৳150 one-time each | $1.66 | First 2 of each free for life | Blueprint rule kept |
| Storage add-on / month | +20 GB ৳80 · +50 GB ৳180 · +100 GB ৳300 | $0.89 · $1.99 · $3.32 | Extra storage | Old whole-dollar USD ($1/$2/$3) replaced |
| Annual packages | Fee − discount | — | Same package, yearly | Discount on the package fee only; discount % (to confirm) |
| App-store purchase | Web price + 30% | — | Same item bought in App Store / Google Play / Microsoft Store | (default, editable) |

### Per-minute video rates (per minute of finished output)

3D / Animation (Quick and Enhanced modes):

| Package | 480p Native | 720p Esc | 720p Native | 1080p Esc | 1080p Native | 4K Esc |
|---|---|---|---|---|---|---|
| Mini | ৳30 ($0.33) | ৳55 ($0.61) | ৳72 ($0.80) | — | ৳120 ($1.33) | — |
| Starter, Premium Starter | ৳30 ($0.33) | ৳55 ($0.61) | ৳72 ($0.80) | ৳85 ($0.94) | ৳120 ($1.33) | ৳142 ($1.57) |
| Professional | ৳25 ($0.28) | ৳50 ($0.55) | ৳66 ($0.73) | ৳78 ($0.86) | ৳120 ($1.33) | ৳142 ($1.57) |
| Agency | — | — | ৳62 ($0.69) | ৳74 ($0.82) | ৳120 ($1.33) | ৳142 ($1.57) |

Cinematic (+35%; 1080p Esc is a flat +৳10 exception):

| Package | 480p Native | 720p Esc | 720p Native | 1080p Esc | 1080p Native | 4K Esc |
|---|---|---|---|---|---|---|
| Mini | ৳41 ($0.45) | ৳74 ($0.82) | ৳97 ($1.07) | — | ৳162 ($1.79) | — |
| Starter, Premium Starter | ৳41 ($0.45) | ৳74 ($0.82) | ৳97 ($1.07) | ৳111 ($1.23) | ৳162 ($1.79) | ৳192 ($2.12) |
| Professional | ৳34 ($0.38) | ৳68 ($0.75) | ৳89 ($0.98) | ৳102 ($1.13) | ৳162 ($1.79) | ৳192 ($2.12) |
| Agency | — | — | ৳84 ($0.93) | ৳96 ($1.06) | ৳162 ($1.79) | ৳192 ($2.12) |

Islamic content = 25% off each rate (whole taka, .5 up). 3D Islamic / Cinematic Islamic:

| Package | 480p | 720p Esc | 720p | 1080p Esc | 1080p | 4K Esc |
|---|---|---|---|---|---|---|
| Mini 3D / Cin | ৳23 ($0.25) / ৳31 ($0.34) | ৳41 ($0.45) / ৳56 ($0.62) | ৳54 ($0.60) / ৳73 ($0.81) | — | ৳90 ($1.00) / ৳122 ($1.35) | — |
| Starter, PS 3D / Cin | ৳23 / ৳31 | ৳41 / ৳56 | ৳54 / ৳73 | ৳64 ($0.71) / ৳83 ($0.92) | ৳90 / ৳122 | ৳107 ($1.18) / ৳144 ($1.59) |
| Pro 3D / Cin | ৳19 ($0.21) / ৳26 ($0.29) | ৳38 ($0.42) / ৳51 ($0.56) | ৳50 ($0.55) / ৳67 ($0.74) | ৳59 ($0.65) / ৳77 ($0.85) | ৳90 / ৳122 | ৳107 / ৳144 |
| Agency 3D / Cin | — | — | ৳47 ($0.52) / ৳63 ($0.70) | ৳56 ($0.62) / ৳72 ($0.80) | ৳90 / ৳122 | ৳107 / ৳144 |

Notes: 4K Escalating = Starter+ only, not in Mini, Trial or Beta. Cinematic 1080p Native (and so Cinematic 4K) switches on only after its GPU benchmark. If the video speed-ups have not passed by paid launch, Cinematic 720p Native and higher stay "coming soon".

### Other charges and buying options

| Item | Price ৳ | USD | What's included | Notes |
|---|---|---|---|---|
| Express delivery | Rate + 20% | e.g. ৳72 → ৳86 ($0.95) | High priority, live ETA | 20% refunded if >20% later than the ETA |
| Normal delivery | Rate | — | Within 12 h | Late = full refund of that order to the original method |
| Slow delivery | Rate − 10% | e.g. ৳72 → ৳65 ($0.72) | Within 24 h, night window | Late = full refund to the original method |
| Pre-production fee | ৳20 per started 2 min (Islamic ৳15) | $0.22 ($0.17) | Script, storyboard, scene list, key images, 480p preview | **Paid first**, before pre-production starts; not charged if safety blocks at start; refunded on technical failure |
| Pay-per-video | A little above package rates | — | One video, no subscription (bKash etc.) | Mark-up (to confirm) |
| Minute pack 30 min / 100 min | 10–15% off the rate | — | A package, not a wallet | **Valid 90 days**; no top-up, no cash value; exact prices (to confirm) |
| Multi-language pack | Each extra language at the dubbing rate (50% of the video's per-minute rate); 10% off for 3–5 languages, 15% off for 6+ | e.g. 2-min 1080p Starter: 5 langs ≈ ৳540 ($5.98), 10 langs ≈ ৳1,020 ($11.29) | Dubbing + lip-sync + on-screen text | (default, editable) |
| Auto-dubbing (one language) | 50% of the per-minute rate | — | Translated voice + subtitles | Approved |
| Hook variants, extra aspect ratios, multi-camera angles | Each billed at its own minutes | — | — | Approved |
| Voice-over-only audio | Well below video | — | Radio ads, shop announcements, IVR | Price (to confirm) |
| Emotion controls | Free | — | Inside the package | Billed only by final video minutes |
| One-click boost | Creator pays Meta directly | — | — | RemonLogic never holds ad money |

### Discount rules (approved 30 Oct)

- Rule discounts always apply: Islamic −25%, Slow −10%.
- Only **one promotional discount** per order — the largest of coupon, festival, reseller, referral or minute pack.
- Annual discount applies to the package fee only.
- **Caps: 45% total off per-minute rates; 30% total off package fees.**
- **Price floor: at least 30% margin** after VAT, gateway fees and refunds. The system trims the promo discount (never the rule discounts). Finance-level approval to change; recheck after the GPU benchmark.
- Owner exception: 50% off the first NexaTute course for Motion Studio clients (once per client).

### Refunds (all products, 30 Oct)

- Request within 30 days of payment; refunded only if approved. AI checks first, a person decides (two-person approval above the admin-set amount).
- Only the unused part is refunded; rendered minutes and other used items are deducted at list price.
- Money goes back to the original payment method. There is no stored balance.
- Automatic refunds (failed render, late delivery, our defects) need no request.
- EU/UK 14-day right and stronger local laws apply. Under-18 refunds go to the guardian. Store purchases follow the store's refund process.

---

## Features by area

### 1. Ordering & briefs

Source: decisions.md:16–18, 33, 83, 88, 103, 113, 179; motion-studio/source/03.md, 04.md §4.1, 05.md §5.1

| Feature | What it does (one line) | Plans | Rules/limits |
|---|---|---|---|
| AI script from an idea | Writes a scene-by-scene script from a topic or brief | All | Pre-production fee applies |
| Script Upload (as-is / AI improve) | Uses the creator's own script; AI changes shown for approval | All | Bijoy → Unicode converted automatically |
| Document-to-Video | Writes a new script from PDF, DOCX, PPT or URL | Pro+ | Pre-production fee applies |
| Video from a link | Pulls text, images and price from a product page, blog, Daraz or Shopify link | All | Creator confirms rights; free account 1/day |
| Order by WhatsApp/Messenger voice note | Voice note + photos → brief, storyboard; preview and payment link in the chat | Mini+ | Never clones a voice from a voice note |
| Project brief | Records audience, purpose, tone, format and constraints | All | — |
| Storyboard with live price | Scene list, key images, 480p preview; shows length and full price | All | Video price paid at "approve & pay" checkout (exact amount) |
| Visual storyboard editor | Drag-and-drop scenes with a cost card per scene | All (to confirm) | Approved 30 Oct |
| Live cost estimate | Price updates as options change; re-render cost shown first; itemised invoice | All | — |
| Fixed free storyboard revisions | Revise the storyboard a set number of times free | All | Number (to confirm) |
| Script fact check | AI flags claims; creator approves before final storyboard | All | Remaining errors are the client's responsibility |
| Length tolerance | Shorter video → difference refunded; up to 10% longer → no extra charge | Paid | 10% (default, editable) |
| Pay-per-video | Buy one video with no subscription | Outside packages | Mark-up (to confirm) |
| Minute packs | 30 or 100 minutes at 10–15% off | Outside packages | Valid 90 days; package, not wallet |
| Spending cap | Creator's monthly cap with 50/80/100% alerts | All paid | Staff cannot raise it |
| Upgrade / downgrade / cancel | Upgrade at once with proration; downgrade next cycle; one-click cancel | All paid | Auto-renew needs consent |
| Coupons and promo codes | Discount codes at checkout | All paid | One promo only; caps apply; gift cards as named plan codes (to confirm, lawyer) |
| Automatic reminders | Storyboard waiting, render ready, renewal due — by the channel the client picks | All | No "low wallet" reminder (no wallet) |

### 2. Creation engines & styles

Source: decisions.md:26–28, 31, 73–75, 88, 93, 103; motion-studio/source/03.md §3.3, 04.md §4.7–4.12

| Feature | What it does (one line) | Plans | Rules/limits |
|---|---|---|---|
| Quick mode (2D/3D in browser) | Draws animation, explainers and avatars in the creator's browser | All | No GPU cost; true 1080p |
| Enhanced mode (2.5D) | AI key image + depth, animated with camera moves | Mini+ (Trial yes) | Not in free account |
| Cinematic mode (Wan 2.2) | Full AI video for hero shots only | Mini+ (Beta in daily pool) | 1080p Native after benchmark |
| Resolution ladder 480p → 4K Esc | Six output tiers incl. upscaled 4K | Per package table | 4K Starter+ |
| Frame rates 24/25/30/60 | Base 25 fps; 60 fps on higher plans | 24/25/30 all; 60 PS+ | Admin-controlled |
| Single-shot clip generator | Prompt or image → 5–10 s clip with camera presets, extend, variations | (to confirm) | — |
| Scene Bible | Locks locations, lighting and environment across scenes | (to confirm) | — |
| Character Bible + personality | Saves look, personality and speaking style per character | All | Consistent across episodes |
| Per-character / series LoRA | Small model per series character, reused every episode | PS+ | Night GPU batch |
| Multi-camera scenes | Several angles of one scene, kept consistent | (to confirm) | Each angle billed as its own minutes |
| Motion brush | Draw arrows on a storyboard image to steer movement | (to confirm) | Model licence check |
| 2 hero-shot candidates | Makes two takes of a hero shot and auto-picks the best | Default on PS+; optional below | — |
| Automatic quality fixes | Face/hand repair (GFPGAN), physics check, colour match, deflicker, stabilise | All | CodeFormer excluded (licence) |
| Pre-delivery scene check | Detects bent buildings, odd food, floating objects; regenerates | All | ≤5 s shots stitched |
| Extra QA checks | Black/broken frames, caption and audio clipping; budget check before auto-regeneration | All | — |
| "Quality Checked" badge | Shown only after every automatic check passes | All | Otherwise repair first |
| Pre-publish quality score | Scores hook, thumbnail, captions, audio with tips | (to confirm) | Never promises views |
| Bangladesh scenes LoRA | Villages, rivers, rickshaws, haat, food; Bangladeshi dress; skin tone kept | All | Trained only on own photos |
| Reference image per scene | Steers the look of one scene | All | — |
| Famous-places library | Shaheed Minar, Sundarbans, Cox's Bazar, Sajek … from licensed photos | All | Every image logged |
| Text always as overlay | Titles, prices, Bangla/Arabic text never drawn by the AI model | All | HarfBuzz shaping |
| Templates library | Product ad, Islamic reminder, greeting, news, education | All (basic on free) | No pre-production fee if own text only |
| Series and promo tools | Intro, outro, recap, next-episode preview, teaser, trailer, highlights, thumbnails | Full set PS+; templates below | Promos from own episodes at Quick rate |
| Long video → Shorts | Cuts the creator's own long video into Reels/Shorts | All | Quick rate, no pre-production fee |
| Still images from projects | Posters, carousels, banners from the same project | (to confirm) | — |
| Stock presenter library | Paid, consenting adult actors with signed releases | (to confirm) | No testimonials/politics; AI label + C2PA |
| Licensed stock media library | B-roll from a paid stock API (listed exception) | (to confirm) | Tracked in licence log |
| Virtual try-on | Clothes on synthetic or consenting models, true colours | (to confirm) | — |
| Model version pinning | Each project stays on the model it started with | All | — |
| Model fallback + regression check | Switches model on failure; detects quality drops after updates | All (system) | Quarterly open-model benchmark |
| AI Producer (agent roles) | Scriptwriter, voice director, editor and reviewer steps checked for budget and policy | All (system) | Same models, separate steps |
| Browser RIFE interpolation | Smooth in-between frames on strong devices | All | Device-check based |
| Resume failed renders | Continues from the last chunk; browser → server takeover | All | Never charged for a failure |
| Region repair | Fix one marked area instead of regenerating the scene | 1 free/video Mini+ | — |

### 3. Voices, characters & cloning

Source: decisions.md:26–30, 56, 83–84, 93, 103–104, 112, 181; motion-studio/source/04.md §4.2–4.6, 12.md §12.5–12.8

| Feature | What it does (one line) | Plans | Rules/limits |
|---|---|---|---|
| Voice picker | Filter by language, dialect, gender, age, style; plays the creator's own first line | All | Clear, easy choice required |
| Library voices in 8 emotions | Neutral, happy, sad, tearful, angry, afraid, whisper, excited | All | Free |
| Simple emotion mode | AI suggests one emotion per line; one-tap change | All | Free |
| Advanced emotion mode | Per-line emotion + intensity, preview, matched facial expression | PS+ | Free |
| Deeper emotion engine | More emotions, continuity across scenes, gesture/eye gaze timeline, director controls | (to confirm) | Shown as creative control, never as reading real feelings |
| "Act it yourself" | Creator speaks the line; feeling transferred to the character voice | Starter+ | Not cloning |
| Webcam acting transfer | Creator's facial expression moved onto a character or own twin | (to confirm) | Own face, consent; lawyer gate |
| Regional-dialect voices | Chittagonian, Sylheti, Noakhali, Barishal, Rangpur | Starter+ | — |
| Middle East pack | Gulf and Egyptian Arabic voices + templates | (to confirm) | No "No. 1" claims |
| Child-character voices | Boy/girl, 5–8 and 9–12, from paid adult artists or synthetic | Mini+ | Never a real child's voice; kids-safe forced |
| Voice design + text-to-SFX | New voice from a description; sound effects from text | (to confirm) | No real-person imitation |
| Voice Clone Studio | Guided 10–12 min: mic test → live consent sentence + OTP → 3 min reading → emotion cards → preview | 2 free, then ৳150 each | In app only; 18+; Free Beta only after lawyer check |
| Third-party voice/face cloning | Clone another adult with their direct live consent + OTP on their phone | Same as clone | At launch (31 Oct); politicians/celebrities need written proof |
| Clone safety rules | Account-only, never sold; deleted 72 h after withdrawal; watermark + "AI voice" label | All | Samples encrypted; staff can't listen |
| Digital-twin presenter | Realistic presenter from a ≥ ~2-min video of the creator's own face | 1 PS / 3 Pro / 10 Agency | Never one selfie; 18+, consent + OTP; extra ৳500 |
| Bangla pronunciation dictionary | Normalises numbers, dates, taka; saves brand/name pronunciations | All | — |
| Other speakers in uploads | Get library voices, never cloned without their consent | All | — |
| Lip-sync + sync check | Browser visemes; server close-up lip-sync; auto check before delivery | All | Close-up model after licence check |

### 4. AI Co-Director

Source: decisions.md:106, 112; memory/areas/motion-studio.md:105–106, :108

| Feature | What it does (one line) | Plans | Rules/limits |
|---|---|---|---|
| Brainstorm ideas | Asks audience, feeling, budget; offers 3–5 ideas | All logged-in | Daily message limit per package; free account 10/day |
| Story shaping | Hook, middle, emotional moment, call to action; honest weak points | All | — |
| Decision help | Compares options with pros/cons, cost, time | All | — |
| Any-subject discussion | Business, marketing, festivals, Islamic content | All | General info only on medical/legal/financial |
| One-click storyboard | "Make a storyboard from this" with the price | All | — |
| Text or voice, 10 languages + Banglish | Chat in any UI language | All | Each language after native review |
| Memory | Remembers Brand Kit, Character Bible, past projects | All | Chats kept 180 days; never used for training |
| Safety | Crisis protocol, prompt-injection protection, content policy, AI label | All | Own LLM; under-18 never sent to outside AI |
| "Learn this" suggestion | Suggests the matching NexaTute lesson when stuck | All | Max once per session (default) |

### 5. Editor & timeline

Source: decisions.md:27, 88, 91, 102–103, 180; motion-studio/source/04.md §4.11

| Feature | What it does (one line) | Plans | Rules/limits |
|---|---|---|---|
| Timeline editor (launch list) | Trim/split, reorder, multi-track video/voice/music/caption, ducking, text/logo layers, transitions, speed, colour, keyframes, snapping, real-time preview | All | (default, editable) |
| Undo/redo + shortcuts | Keyboard shortcuts and full undo/redo | All | — |
| Natural-language editing | "Make scene 3 shorter" applied with a preview | Basic Trial/Starter/PS; full Pro+ | — |
| Edit-by-transcript | Edit the video by editing its text | (to confirm) | — |
| Version control | Compare V1/V2/V3, restore, approval history | All | — |
| Real-time co-editing | 2–3 people edit storyboard/timeline with live comments (Yjs) | (to confirm) | — |
| Agency approval chains | Multi-step approval (junior → senior → client) | (to confirm, Agency) | — |
| Phone-video auto-edit | Cuts silences/fillers, cleans noise, adds captions, fixes colour | Mini+ | DeepFilterNet |
| In-browser teleprompter | Script scrolls while recording | Mini+ | — |
| Screen-recording studio | Screen + webcam + mic, auto-zoom, captions, blur personal data | (to confirm) | — |
| AI clean-up of real footage | Background remove/replace, object removal, eye contact, upscale | (to confirm) | Commercial-safe models only |
| Restyle own footage | New visual style on the creator's own video | (to confirm) | Own footage only |
| Style analysis | Palette, pacing, mood from client-owned references | (to confirm) | No copying, no downloading others' videos |
| Automatic B-roll | Inserts matching cutaways into talking-head videos | Starter+ | — |
| Audio: AI music, SFX, ducking | Mood-based music, CC0 effects, music lowers under voice | All | Content-ID-free or own AI music |
| Mastering + loudness | Platform presets; YouTube −14 LUFS, broadcast EBU R128 −23 LUFS | All | — |
| Beat-synced cuts | Scene cuts on the music beat | Starter+ | — |
| Personal media library | Logos, images, music, voices, characters with folders and search | All | Counts toward storage |
| Project safety | Autosave, duplicate, 30-day trash, folders, search | All | — |
| Brand Kit + tone of voice | Logo, fonts, colours, brand voice applied to every script | Templates Trial; limited Mini; full PS+ | Free account 1 logo |
| Brand price list + claim check | Stored prices/offer rules; wrong prices or over-claims blocked | (to confirm) | — |

### 6. Languages, dubbing, captions

Source: decisions.md:77, 83–84, 164, 180; motion-studio/source/04.md §4.2, 05.md §5.7

| Feature | What it does (one line) | Plans | Rules/limits |
|---|---|---|---|
| 10 voice/caption/UI languages | bn, en, hi, ur, ar, fr, ja, de, zh, ko | All | Each live only after native-speaker review |
| Extra dubbing languages | Spanish, Portuguese, Indonesian, Turkish and more | Starter+ | Each after its quality gate |
| Auto-dubbing | Transcribe → translate → voice → fit timing → redo lip-sync → subtitles | All paid | 50% of the per-minute rate |
| One-click multi-language pack | Many languages in one order (dub, lip-sync, on-screen text) | PS+ | Volume discount 10% / 15% |
| Cultural adaptation | Currency, festivals and local examples changed per market | All | — |
| Video translate | Dubs the creator's own uploaded video | All paid | Blueprint's "Q2 2027" removed (no phases) |
| Burned-in captions | Styled, word-by-word, correct Bangla conjuncts; RTL for ar/ur | All | HarfBuzz, Noto fonts |
| SRT/VTT caption files | Separate caption files | Mini+ | — |
| BdSL sign-language corner | Signing avatar translates narration to Bangla Sign Language | All | Browser-drawn; expert + Deaf reviewer check (to confirm) |
| Audio-description track | Describes visual action for blind viewers (WCAG) | Starter+ | Creator approves text |
| Accessible studio | WCAG 2.2 AA, keyboard, screen reader, high contrast | All | Claim only after audit |
| First-visit language prompt | "View in your country's language or in English?" once; saved in Settings | All | IP country only, IP never stored |

### 7. Delivery, formats & sharing

Source: decisions.md:26, 74–75, 83–84, 93–94, 113, 130–131, 196; tasks/sharing-and-connectors.md; motion-studio/source/04.md §4.10, 05.md §5.4

| Feature | What it does (one line) | Plans | Rules/limits |
|---|---|---|---|
| Delivery tiers Express/Normal/Slow | +20% / normal / −10%, live ETA | Mini+ (paid server renders) | Late refunds per price table |
| Final MP4 + 72 h link | Validated H.264 to storage, or a 72-hour link if no storage | All | — |
| Automatic 360p WhatsApp copy | Small, quick-to-send copy of every video | All | Counts toward storage |
| Aspect ratios + auto-reframe | 16:9, 9:16, 1:1, 4:5 in one click | All | Each extra format billed |
| Pro export | ProRes master, FCPXML/EDL timeline (CPU only) | Pro+ | ProRes counts toward storage |
| Share button (standing order) | One tap: Facebook, WhatsApp, LinkedIn, Instagram, TikTok, YouTube, X, copy link, download, QR | All | Preview first; OAuth only; report + 24 h takedown; no rewards for sharing |
| "Made with" / "Remix this" end card | Product mark + verify link on shared videos | Required on free; switchable on paid | (default, editable) |
| Connected accounts | YouTube, Facebook, Instagram, TikTok via official OAuth | All paid | Never passwords; tokens encrypted, revocable |
| Direct publishing + scheduling | Post with title, tags, thumbnail, captions | Mini+ (free: to confirm) | Each platform after its app review; LinkedIn later |
| C2PA Content Credentials | Every export signed as made with AI | All | Cannot be switched off |
| AI-disclosure auto-tick | Platform AI labels ticked for realistic AI, clones, twins | All | Inauthentic-content warning before posting |
| Invisible re-upload watermark | Detects unauthorised re-uploads; complaint report | All | — |
| Verification tool | Public check: "made with Remon Motion Studio?" (own watermark + C2PA) | All | No general AI-detection claim |
| Hosted pages / embeds | Public video pages with view limits per month | Free 1k · Mini 10k · Starter 50k · PS 200k · Pro 1M · Agency 5M | Signed URLs; free pages noindex; report button |
| Shoppable player | Interactive player on our own page, linked from Facebook/WhatsApp | (to confirm) | Not inside the Facebook feed |
| Interactive video + SCORM | Buttons, chapters, quizzes; SCORM for company LMS and NexaTute | Pro+ | — |
| Client review link | Time-coded comments + approve, no account needed | PS+ | Private, revocable, expires |
| Multi-client agency workspace | Client folders, brand kits, review links, reports per client | Agency | — |

### 8. Business & marketing tools

Source: decisions.md:16–27, 83–84, 93–94, 112–114; motion-studio/source/05.md §5.2–5.3

| Feature | What it does (one line) | Plans | Rules/limits |
|---|---|---|---|
| Business packs | Real estate 2.5D walkthrough, restaurant menu, tours, coaching, clinics | Mini+ | Licensed businesses must show licence no.; AI auto-verifies |
| Product ad maker | Product photos → background removed → ad with price and order button | All paid | — |
| Product-catalogue import | Shopify/WooCommerce/CSV → one ad per product, night Slow tier | PS+ | Batch storyboard approval |
| Bulk personalised videos | Template + CSV of names → one video each, name written and spoken | PS+ | Not for under-18; recipient consent declared |
| Bulk sends (WhatsApp/SMS) | Sends personalised videos from the client's own sender ID | PS+ | Message cost paid by company; 3 sends/day; recipient cap per package |
| Voice-over-only audio | Radio ads, announcements, IVR | Mini+ | Price well below video (to confirm) |
| End-screen order QR | QR + "order now" → page, WhatsApp link or bKash merchant QR | Mini+ | We never take the buyer's payment |
| Per-video sales tracking | Clicks/orders per video from its own QR/link | Mini+ | Counts only |
| 3 hook variants | Three first-3-second hooks; tracking shows the winner | Starter+ | Each variant billed |
| One-click boost | Boost on Facebook/Instagram from the creator's own ad account | Starter+ | Needs Meta approval |
| Pre-publish ad-policy check | Checks script/frames against Meta/Google ad rules | All | Advice only; free account 1/day |
| Monthly content calendar | AI plans posts around Bangladesh days; night render; auto-publish | Starter+ | Approval before charge |
| Festival early-order discount | Early-order discount + daily capacity limit | All paid | Amount (to confirm); counts as the one promo |
| Trend ideas | Popular-in-Bangladesh ideas from the official YouTube API | Starter+ | Safety rules unchanged |
| Hooks, titles, hashtags, thumbnails | AI suggestions; Bangla titles overlaid | All | — |
| Platform analytics | YouTube/Facebook stats in the dashboard | Basic Mini; AI insights Starter+ | — |
| Faceless autopilot | Videos from news/RSS with sources, approval before each post | (to confirm) | No copied text; daily cap |
| Diaspora video messages | Messages in one's own voice to family abroad | (to confirm) | No partner named without agreement |
| Event-triggered videos | e.g. "thank you" video after a purchase, via API | (to confirm, Pro+ API) | HubSpot/Salesforce apps later |
| Live 3D AI avatar streaming | 24-h live avatar for Enterprise, priced per hour | Enterprise | Always AI-labelled; price (to confirm) |
| Enterprise custom style LoRA | Style model on the client's own footage | Enterprise | Separate fee; consent/licence checks |
| Stock-clip library sales | Our own clips sold to other platforms | Company | Model releases signed |
| Motion Studio API + webhooks | Create projects, check status, download; signed webhooks | Pro+ | Same safety and approval rules |
| Developer platform | Sandbox, SDK, docs, scoped rotating keys, idempotency, rate limits | Pro+ | — |
| Zapier / Make | No-code links to shops, sheets, CRMs | PS+ | — |
| Shopify + WordPress plugins | Make videos from inside the store/site | (to confirm) | — |
| White-label portal | Agency's own brand, small "powered by" line | Agency | Separate licence fee; safety can't be switched off |
| Workspace controls | Per-member spend caps, locked templates, client-visible log | Agency / Enterprise | — |
| Team seats | Included seats per package, extra seats priced | 1/1/2/5/15 | See price table |
| Creator challenge | Monthly theme; homepage showcase | All | Prize "Motion Studio credits" conflicts with no-wallet; prize form (to confirm) |
| Referral + affiliate | Shared referral/affiliate system | All paid | 10% for 12 months with cap; paid after the 30-day refund window |
| Reseller programme | Resellers sell packages to their clients | Partners | Named plan codes, no wallet; discount = the one promo (to confirm) |
| Shared marketplace | Templates, characters, voices, services (NexaTute + Motion Studio + NexaLogicDev) | All | 20% commission; cloned voices/twins never sold |

### 9. Safety, consent & kids-safe

Source: decisions.md:29–34, 104, 107–108, 112–114, 181–182, 207; memory/areas/motion-studio.md:28–44; motion-studio/source/12.md

| Feature | What it does (one line) | Plans | Rules/limits |
|---|---|---|---|
| Content safety layers | Text, image/video, audio and upload checks; output moderation too | All | Cannot be switched off |
| Child-safety hash matching | Known illegal images/video blocked; account closed and reported | All | Zero tolerance |
| Content policy (4.15) | Blocks deepfakes as news, fake news, scam ads, gambling, drugs, weapons, health misinformation | All | Stricter in election periods |
| Never offered | AI testimonials, lyric videos of others' songs, talking photo from one picture | — | Fixed |
| Kids-safe mode | Stricter filters; YouTube "Made for kids" set automatically | All | Forced for child characters and under-18 |
| Under-18 accounts | Guardian owns the account and pays | All | No clone/twin/face acting/bulk/API/publishing; US under-13 blocked; offers 18+ only |
| Minimum age | Outside the USA: follows the learner's class/grade, guardian consent under 18 | All | Same as NexaTute |
| Under-18 requests stay in-house | Never sent to outside AI; wait in queue when busy | All | 31 Oct |
| Adult check (age assurance) | One-time ID + selfie or adult payment check before clone, twin, bulk, API | 18+ features | Images deleted in 24 h (default, editable) |
| Consent registry | Live consent sentence, OTP, speaker verification, withdrawal timer | All | Records kept 3 years |
| Real-person face consent | Any real face needs that person's consent + OTP | All | Public figures need proof |
| Islamic verification | AI check with confidence; unsure → named human reviewer (3–7 days) | All | No charge before approval; prayer scenes always human-reviewed |
| Plan mismatch guard | Tells the creator if a General project looks Islamic; offers switch | All | Never switched silently |
| Copyright + logo detection | Upload checks, logo warning, 24 h takedown | All | DMCA designated agent |
| Report, enforcement, appeals | Report button; warning → suspension → ban; a person decides | All | Appeals to human queue |
| Brand-impersonation protection | Official numbers list, verified badge, trademarks | Company | — |
| Image sourcing log | Wikimedia, Pexels (reference), own shoots, creator uploads; every image logged | All | LoRA only on own photos until lawyer confirms |
| Customer account security | 2-step/passkeys, login alerts, device list; re-check before clone/twin/publish/large spend | All | — |
| Per-project trust page | Licences, consents, models, AI disclosure, takedowns in one place | All | — |
| Public model cards + energy estimate | Model card per AI model; kWh and carbon per render | All | No "trees planted" claims |
| Protected safety settings | Child safety, consent, never-lists changeable only with 3 approvals | Admin | 24 h delay; Co-Admin never approves |

### 10. Account, plans, refunds

Source: decisions.md:53, 102–104, 111–114, 155–156, 184, 188, 212–213; tasks/five-gaps-solutions.md; motion-studio/source/09.md

| Feature | What it does (one line) | Plans | Rules/limits |
|---|---|---|---|
| One Nexa ID | Same login for NexaTute, Motion Studio, NexaLogicDev | All | Consent per product |
| Sign-up with Google/Facebook/Apple | OAuth sign-up, basic profile only | All | Never passwords |
| Guided first video | Tour that ends with a finished video, in Bangla | All | Skippable |
| Sample gallery + tutorials | Labelled samples, "make one like this", short Bangla tutorials | All | "Sample (prototype)" label; no invented numbers |
| Package comparison page | Top 8 features per package, "see all", 3-question helper | Public | Reads from the admin matrix |
| Lifetime free account | Permanent watermarked free tier after the trial | Free | See price table |
| No stored money | Every purchase is a checkout for the exact amount | All | No wallet, no top-up, no balance |
| Refund request | Within 30 days, approved by a person | All paid | Unused part to the original method |
| Automatic refunds | Failed render, late order, our defects | All paid | No request needed |
| Receipts + VAT (Mushak) invoices | Receipt for every charge/refund; business VAT invoices | All paid | — |
| Local currencies | BDT, USD; EUR, GBP via Paddle; INR, PKR, AED, SAR | All | USD to the cent; exchange-rate policy |
| Payments | aamarPay in Bangladesh (also international for now); Paddle later | All | Second gateway: owner |
| Terms versioning + re-consent | New terms need fresh acceptance; auto-renew consent | All | EU/UK 14-day right |
| Data export + deletion | Download all data; delete account with 30-day cancel | All | Clones deleted within 72 h |
| EU data residency | EU users' files and data in the EU | All | At launch (lawyer to confirm) |
| Storage + 30-day keep | Included storage; add-ons; 80/95% warnings | All | See price table |
| Mobile app | Order, Co-Director, storyboard approval, preview, share, Voice Clone Studio | All | At launch (PWA + Capacitor) |
| Support | 24-h AI support; human support; SLA | AI all · human Starter+ · SLA Agency + Enterprise | 24-h English: AI first, then a person |
| Disputes | AI → email → human decides | All | Written in terms |
| Weekly webinar + satisfaction loop | One-tap rating; top 5 complaints fixed weekly | All | Webinar during Free Beta |
| Status page + incident notices | status.remonlogic.com; new ETA and auto refunds | All | — |

### 11. Admin panel

Source: reviews/motion-studio_gaps_admin_2026-10-30.md (19 pages, settings registry); reviews/gap_solutions_2026-10-30.md; decisions.md:35–36, 85, 96–97, 108, 112, 115–117

| Feature | What it does (one line) | Plans | Rules/limits |
|---|---|---|---|
| 1. Command Centre & Co-Admin | Live dashboard, Ctrl+K command bar, morning briefing, anomalies, forecasts, what-if simulator, "why?" | Admin | Dark glass theme; mobile admin with passkeys |
| 2. Packages & features | Whole matrix; per-cell on/off + limits; global "coming soon"; legal-hold state | Admin | Free Beta and free-tier columns, daily caps |
| 3. Prices & billing rules | Rates, formula parameters, rounding, currencies, annual, add-ons, Enterprise rate cards | Admin | Money changes: finance + founder |
| 4. Offers, partners & payouts | Coupons, referral, affiliate, reseller, stacking rule + price floor, payouts | Admin | — |
| 5. Refunds & payments | Refund rules, gateways per country, chargebacks | Admin | Renamed from "Wallet…"; no wallet rows |
| 6. Limits, trials & capacity | Trial/Beta/free limits, daily reset, AI message limits, admission cap | Admin | — |
| 7. Orders & render queue | All jobs, stuck jobs, retries, emergency GPU move, pauses | Admin | Moves to own nodes logged only |
| 8. Trust & safety | Safety queue, Islamic review, election mode, takedowns, legal-request queue | Admin | A person decides |
| 9. Consent & rights registry | Voice/face/twin consents, talent releases, lawyer-gate switches | Admin | DPO only; staff can't play samples |
| 10. Libraries & languages | Voices, dialects, child voices, language gates, dictionary, templates, licence log | Admin | — |
| 11. AI models, prompts & assistants | Model registry/switch, prompt versions, fallback, viewer panel, Co-Director settings | Admin | Rollback in one click |
| 12. Integrations & developer platform | Publishing platforms, WhatsApp bot, SMS/email senders, plugins, API keys, webhooks | Admin | — |
| 13. Customer care & messages | Inbox, SLAs, help centre, notification templates | Admin | — |
| 14. Content, texts & legal pages | UI strings, translations, labels, legal versions, festival calendar, contact addresses | Admin | One email per type of work |
| 15. Growth | Landing Page AI, Motion Notes, journeys, challenge, Free Course links | Admin | Every suggestion explains why (evidence, risk, rollback) |
| 16. Operations | Updates, backups, DR drills, incidents, status page, service budgets, SLOs | Admin | — |
| 17. Accounting & finance | Own books, allocation by usage, daily rate table, VAT, payouts, margin alert < 30% | Admin | Product tag per entry |
| 18. Security, access & data | Roles, audit log, customer login security, SSO, retention, data requests | Admin | — |
| 19. Staff notifications & chat | Bell, routing, internal chat | Admin | — |
| People, teams & job assignment | Who does which job: queues, deputies, shifts, SLAs | Admin (shared) | Shared with NexaTute; Co-Admin drafts only |
| Central settings registry | Every setting: default, scope, effective date, approver tier, lock level | Admin | Two-person approval, logged |
| Nexa Co-Admin (AI) | Acts only within the admin's own permissions; WhatsApp/Messenger/imo switchable | Admin | Never second approver; log 7 years |
| Protected settings | Legal/safety floors: 3 approvals, reason + law reference, 24 h delay, rollback | Admin | Urgent path only tightens |
| GPU view | Use, priority and limits of the shared GPU cluster | Admin (all 3 panels) | Upgrade proposal if queue > 30 min for 2 weeks |

### 12. Cross-product

Source: tasks/internal-video-service.md, free-class-links.md, marketing-automation.md; decisions.md:98–101, 118–123, 136, 166, 176, 178, 185, 194, 199, 210; reviews/audit_2026-10-31/crossproduct.md rows 5–15

| Feature | What it does (one line) | Plans | Rules/limits |
|---|---|---|---|
| Internal Video Service | NexaTute and NexaLogicDev make videos through Motion Studio; result into their storage | Internal | NexaTute class videos go first on A6000 #4; transfer price (to confirm) |
| NexaTute child-safe jobs | Child-safe profile, library voices, pseudonymous IDs | Internal | Working copy deleted 7 days after delivery |
| Project Studio videos | NexaTute students' 1–5 min project videos rendered behind the scenes | Internal | No Motion Studio account needed |
| Nexa Speak then-vs-now video | Monthly progress video for adult learners | Internal | 18+, opt-in; clips kept while subscribed, deleted 30 days after |
| Nexa Scripts animations | Stroke-order and mnemonic animations for the script course | Internal | Content quality flow |
| NexaLogicDev handover video | Free 1-min handover video for Medium/Complex modules | Internal | Old "৳5 = 1 credit" replaced by per-order price / plan minutes |
| "Free Course" menu | Free 45-min NexaTute class on using Motion Studio | All | No learning minutes used; certificate → trial/discount (amount to confirm) |
| "Learn to do this" buttons | Open the exact NexaTute lesson for a feature; "Back to my project" | All | "Coming soon — notify me" if no lesson |
| Cross-course suggestions | 3 NexaTute courses suggested once at course end | 18+ | Interest data with consent; no project content shared |
| 50% first NexaTute course | Discount on the first course for Motion Studio clients | 18+ clients | Once per client; owner exception to the 30% cap |
| NexaTute "Making videos with AI" | Course with certificate → Motion Studio trial/discount | All | Discount amount (to confirm) |
| Motion Notes blog | Motion Studio's blog with SEO module | Company | Human edit of every article; max 3/week |
| Remon Growth Logic AI | Shared Marketing Hub + CRM: calendar → article → video → approval → publish | Company | Cost to the promoted product's budget; night GPU |
| Landing Page AI | remonlogicstudio.com built and run with Landing Page AI | Company | Highlights: free course, lifetime free account |
| Shared GPU cluster | One cluster; Motion Studio on A6000 #4 from 15 Jan 2027 | System | Priority NexaTute → NexaLogicDev → Motion Studio |
| Separate accounting book | Motion Studio book; shared costs split by measured usage | Company | Consolidated company report |
| PlayBoom content | NexaTute PlayBoom content made in kids-safe mode | Internal | — |
| Teacher lesson → explainer video | Teacher script exported as a Motion Studio video | Internal | Payer and consent link (to confirm) |
| Link character/voice to NexaTute | Reuse a Motion Studio character or voice in NexaTute | 18+ | Price and consent (to confirm) |

---

## Out of date in older documents

Biggest changes vs the Motion Studio Blueprint Edition 1.0 (`docs/motion-studio/source/`):

- **No wallet.** "Approve & pay from the wallet", bKash top-up, wallet refunds, §7.13 Wallet and reseller "usable wallet" packs are gone. Every purchase is a checkout for the exact amount; refunds go to the original payment method.
- **USD rule and rounding.** Package fees are now to the cent ($5.52 / $11.05 / $22.12 / $44.25 / $88.51, not $6 / $11 / $22 / $44 / $89); storage add-ons $0.89 / $1.99 / $3.32. Same rule (×1.35 ÷ 122) for all three products.
- **Dates.** Not "Free Beta 20 Dec 2026, 30 days". Now: in-house/closed pilot 15–29 Jan 2027, Free Beta 30 Jan 2027, paid 20 Feb 2027.
- **GPU.** Not 6 RTX PRO servers in Dallas, floors 60/25/15 or A100 lending. Now: LeaderGPU Netherlands, A6000 #4 for Motion Studio from 15 Jan 2027, priority NexaTute → NexaLogicDev → Motion Studio, A100 never lent.
- **Refunds.** Not "fee back only if no video was made" / "no refund after 31 days". Now: request within 30 days, refunded only if approved, unused part to the original method; late Normal/Slow = full refund of that order.
- **Pre-production fee** is paid first, before pre-production starts (not taken at storyboard approval).
- **Minute packs** are approved packages valid 90 days (not a "balance" liability); "Motion Studio credits" (30-day) and "৳5 = 1 NexaLogicDev credit" are replaced.
- **Scope and languages.** No phases (mobile app, video translate, team workspace no longer "Q2 2027"); Free Beta has all features within daily limits; 10 languages, not 6 with UI staged by year; third-party cloning with consent at launch (not own-voice only).

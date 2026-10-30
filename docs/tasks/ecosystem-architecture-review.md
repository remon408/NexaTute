# Review of "RemonLogic Ecosystem — Unified Nexa ID, NexaTute AI Teacher & Motion Studio Integration" (approved with corrections 30 Oct 2026)

Accepted architecture: one Nexa ID (OAuth 2.0/OIDC, PKCE, short-lived access + rotating refresh tokens, passkeys, MFA, central session revocation, product-specific RBAC) with separate product databases; Motion Studio as invisible backend for NexaTute avatar/voice jobs (private API + signed callback; fields: Nexa ID/tenant, avatar ID, voice model ID, asset ref, animation/lip-sync profile, consent ref, version, job status); browser-side 3D rendering; LiveKit SFU separate from AI compute; raw biometric files in separate encrypted storage; organisation identity.

## 8 mandatory corrections
1. Under-18 learners never clone their own face or voice (even with guardian consent) — library avatars/voices only.
2. Photo → stylised/cartoon avatar only; a real-person likeness needs a ≥2-min video + live consent sentence + OTP (digital-twin rule).
3. Institutes may use a teacher's face/voice only with that teacher's own live consent + OTP; withdrawn automatically if the teacher leaves.
4. Marketplace never sells real-person clones/twins (MoA) — only library/fictional avatars; a real person's avatar is usable only in their own classes.
5. Storage follows the 29 Oct tiered model (not "10 GB per package"); character/voice-clone rule from the blueprint stays (first 2 free per platform, then ৳150 one-time each).
6. Live transcript shown during the session but the learner's own speech is never stored (only the tutor's text).
7. No phases — everything at launch.
8. Name: "AI Tutor Creator" (Nexa Tutor naming).

## Adopted good ideas
Per-product token audience; central logout/device/session dashboard; one identity in several organisations with separate permissions; adults (guardians/teachers) can create their own AI Tutor under the twin/clone rules; English Speaking Lab extras; one shared Digital Human Engine for all products.

## Capacity note
The proposed LiveKit server (48 cores, 256 GB, 10 Gbps) ≈ our Core-1 — no new server. The "2,000–4,000 concurrent sessions" figure is unverified; the real limit is GPU (STT + LLM + TTS per session). Load-test at 500 / 1,000 / 2,000.

## Open question
"GrowthLogicAI" appears as a 4th product with its own CRM DB — confirm whether it is the new name of the RemonLogic Growth Platform / AI Marketing Hub.

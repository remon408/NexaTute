# Handover — state on 29 Oct 2026

## Done
- **NexaTute prototype**: Version 156 of the Design canvas (claude.ai artifact, owner's account) = the 59 boards in `prototype/project/`. Last passes:
  - fix20: staging load test, voice/audio cache, admin passkeys + "Report a security problem" page + pen-test before paid launch, "What's new" sheet; X20 legal pages moved to X24; X10 split into X10 / X25 (plans & prices) / X26 (rules).
  - fix21: admission limits per class/course, waiting list, capacity guard (75 % of load-test capacity, release below 60 %), one master "All new admissions" switch with an admin message written once and AI-translated into 6 languages; Nexa Co-Admin (X27) acting within each admin's own permissions, on WhatsApp / Messenger / imo (all off until lawyer/DPO check; imo needs business API access).
  - fix22: USD rule ".5 rounds down" with no exception (৳500 = $7).
  - X20 header: one compact sticky bar when scrolled (≥ 1024 px).
- **Master Blueprint** Corporate Edition v32.10 (`docs/blueprint/`).
- **Netlify static export** of all prototypes (built from `prototype/netlify-build/`; fonts folder `ff/` and `preact-src/` are not committed — re-fetch from npm/fontsource when rebuilding).

## Key dates
- NexaTute Free Beta 20 Nov – 9 Dec 2026; paid launch 1 Jan 2027.
- Remon Motion Studio Free Beta 20 Dec 2026 (paid start to be set).
- NexaLogicDev development from March 2027, launch September 2027.

## Open owner questions
- Nexa Co-Teacher Pass ৳100 = $1 under the rounding rule (an older note said $2) — confirm.
- Co-Admin activity log kept 7 years (default) — confirm.
- L14 learner abroad: "prices in USD, app language of their choice" (was "English UI and USD") — confirm.
- imo business API access; lawyer/DPO check for Co-Admin on chat apps.

## Next steps (owner's order)
1. This repo is the shared home for all Claude accounts (lead / back-end / front-end).
2. Prototypes still to build: **Remon Motion Studio** (first — Free Beta 20 Dec) and **NexaLogicDev** — separate canvases, same rules.
3. Real NexaTute development: MVP for the Free Beta first (sign-up/OTP/guardian consent, plans & payment, 1:1 and 1:50 AI classes, Co-Teacher, recordings, guardian dashboard, core admin). There is no developer team yet — a human full-stack/DevOps reviewer is strongly recommended before anything goes live (payments, children's data).

## Known small items left
- X12 "Open approval" on an already-open approval does nothing.
- Optional static frames not drawn: D05/D07 load test, G01/D04 What's new.
- X20 (≈1.80 MB) and X12 (≈1.77 MB) have little room left; next X20 split: Nexa Notes → new board.

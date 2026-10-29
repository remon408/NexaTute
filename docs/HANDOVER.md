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
- Answered 29 Oct 2026 (see decisions.md): Co-Teacher Pass $1; Co-Admin log 7 years; L14 USD + own language; imo business API still to apply; Claude drafts legal positions for the lawyer to check.

## Next steps (owner's order, updated 29 Oct 2026 night)
Owner: "start properly — dates may move if needed"; new features paused until Free Beta; people for accounting, legal and developer review are available. All decisions after v32.10 are in `docs/decisions.md` (to go into the next blueprint build).
1. **Live websites** nexatute.com and remonlogicstudio.com (home, features, prices, contact, terms, privacy, refund, children's data) — needed before aamarPay website check, Meta, YouTube API, Paddle. Trade licence not shown; support phone + email to decide (reminder Sat 31 Oct 10:00 Dhaka).
2. NexaTute MVP list + week-by-week plan → GitHub Issues for lead / back-end / front-end. 2-week closed pilot before the public Free Beta; Free Beta pass conditions decide the paid launch.
3. **Remon Motion Studio** prototype, then **NexaLogicDev** prototype — separate canvases, same rules.
4. Payments: aamarPay (already has a merchant account, supports international) until the Paddle API is approved.

## Known small items left
- X12 "Open approval" on an already-open approval does nothing.
- Optional static frames not drawn: D05/D07 load test, G01/D04 What's new.
- X20 (≈1.80 MB) and X12 (≈1.77 MB) have little room left; next X20 split: Nexa Notes → new board.

# For the OLD Claude account — build the Remon Motion Studio prototype (in parallel)

Owner order, 31 Oct 2026: the two Claude accounts work at the same time through this repo.
- **New account:** NexaTute prototype (`prototype/`), the audit fixes, the Netlify zip.
- **Old account (you):** Remon Motion Studio prototype, in its own folder **`prototype-motion-studio/`**. Do not edit `prototype/` — the new account is splitting and changing those boards.

Reply to the owner (Md Raju Ahmed) in Bengali, plain and short. Follow `CLAUDE.md` fully (model split: Opus plans/reviews, Sonnet builds, Haiku checks; never claim a check you did not run).

## Read first, in this order
1. `CLAUDE.md`, `docs/HANDOVER.md`.
2. `docs/decisions.md` — ALL of it; newest lines win. Key 31 Oct answers: one USD rule for all products = BDT +35% at ৳122 = $1, shown to the cent; minute packs (90-day validity) and Boost packs are packages, not wallet; no stored money anywhere; refund rule of 30 Oct (request within 30 days, refund only if approved); third-party cloning at launch with consent rules; under-18 requests never go to outside AI; Motion Studio dates: in-house 15 Jan 2027, Free Beta 30 Jan 2027, paid 20 Feb 2027; GPU: A6000 #4 for Motion Studio from 15 Jan 2027, priority NexaTute → NexaLogicDev → Motion Studio.
3. `docs/memory/areas/motion-studio.md` and `docs/memory/preferences.md`.
4. Motion Studio Blueprint Edition 1.0 sources `docs/motion-studio/source/` — written BEFORE most 30–31 Oct decisions; it still contains wallet, old GPU split, old dates and old refund text. Use it for features and screens, never for those outdated rules.
5. `docs/reviews/motion-studio_gaps_admin_2026-10-30.md` (19 admin pages + central settings registry), `docs/reviews/gap_solutions_2026-10-30.md`, and the 31 Oct audit `docs/reviews/audit_2026-10-31/` (contradictions.md and crossproduct.md list every Motion Studio item that is out of date or missing a cross-product connection).
6. Nexa Verify (RASP, 31 Oct): build the Motion Studio "AI Quality (Nexa Verify)" admin page per `docs/tasks/nexa-verify-admin.md`, and the user-facing statuses.
7. Shared patterns: `docs/tasks/sharing-and-connectors.md`, `language-prompt.md`, `internal-video-service.md`, `free-class-links.md`, `marketing-automation.md`, `rename-nexa-tutor.md`.

## Step 1 — plan (Opus), show the owner before building
- Start from the feature catalogue made on 31 Oct: `docs/features/motion-studio-features_2026-10-31.md` (≈200 features, prices recomputed, newest decisions applied, open items marked "(to confirm)"). Check it, do not rebuild it from scratch.
- List every approved Motion Studio feature and place it on boards by area (customer app, ordering and pricing, editor/timeline, voices/characters/clone studio, AI Co-Director, delivery and sharing, account/plans/refunds, safety and consent, admin pages 1–19 + Co-Admin, landing page, legal pages links, "Free class" / "Learn to do this" links into NexaTute, blog "Motion Notes").
- HANDOVER asked for four phases (launch / first 3 months / 2027 / later) while the owner also wants all features in the Free Beta. Show the owner the list and ask how to handle that before building.
- Board plan with sizes: every board ≤ 1,800,000 bytes **with all 10 languages** (bn, en, hi, ur, ar, fr, ja, de, zh, ko); keep each board well below (≈1.3 MB) so it never needs splitting later.
- Show the owner a short Bengali summary of the plan; save his approvals to `docs/decisions.md`.

## Step 2 — build (Sonnet from your spec), check (Haiku), review (Opus)
- Same board format as NexaTute (`.dc.html`, Design canvas). Look at one NexaTute board for the format and shared look; Motion Studio may have its own brand look if the owner approved one (check decisions/memory).
- Every board: 10 languages with identical keys, RTL for ar/ur, Latin digits, responsive 390/834/1024/1440, touch targets ≥ 44 px, contrast ≥ 4.5:1, Share buttons and the first-visit language prompt where they fit, every value admin-editable "(default)", samples labelled "sample (prototype)", no fake numbers.
- Verify each board: `python3 prototype/tools/dcverify.py prototype-motion-studio/<board>` → 0 problems, 0 parity (the tool now requires all 10 languages). `wc -c` ≤ 1,800,000.
- Prices: compute every Taka→USD figure with code (BDT × 1.35 ÷ 122, to the cent).
- You may publish the boards to a NEW Design canvas in your account named "Remon Motion Studio prototype" for the owner to view.

## How we avoid stepping on each other
- You write only in `prototype-motion-studio/` and `docs/motion-studio/`, plus new lines at the END of `docs/decisions.md` and `docs/STATUS.md`. The new account writes in `prototype/` and the other docs.
- Before every commit: `git pull --rebase origin main`; small commits; push often. If a pull shows a conflict in `decisions.md` or `STATUS.md`, keep both sides' lines.
- A shared rule you think must change (CLAUDE.md, tools, shared task files): write it as a line in `docs/STATUS.md` ("Request to new account: …") instead of editing it; the new account does the same for you.
- If you find something that affects NexaTute (cross-product), add it to `docs/tasks/cross-product-audit.md` at the end and mention it in STATUS.md.
- Your separate job from `docs/tasks/old-account-canvas-update.md` (updating the old NexaTute canvas) still applies when STATUS.md says the NexaTute boards are ready.

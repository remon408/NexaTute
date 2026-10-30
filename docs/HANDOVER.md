# Handover — state on 30 Oct 2026, 12:30 Dhaka (written for the next Claude account)

Read `CLAUDE.md` first, then this file, then `docs/decisions.md` (newest lines at the bottom win). The owner writes Banglish/Bengali — reply in Bengali, plain and short. Build files only when he asks; save every decision.

## Where everything is
| What | Where |
|---|---|
| All owner decisions after Master Blueprint v32.10 (dated; superseded lines are marked) | `docs/decisions.md` |
| Full memory export of the previous account (the owner's durable facts and decisions, by subject) | `docs/memory/` — read `docs/memory/areas/<subject>.md` before answering about that subject. Lines are "[stated]" = the owner said it. Newer lines override older ones in the same file. |
| Master Blueprint v32.10 (whole ecosystem, 382 pp) | `docs/blueprint/` |
| Remon Motion Studio Blueprint, Edition 1.0 (126 pp, Word) + chapter sources | `docs/motion-studio/` (sources in `source/`) — written BEFORE most 30 Oct decisions; `docs/reviews/` lists its contradictions |
| Legal pack (drafts for a Bangladeshi lawyer; Claude is not a lawyer) | `docs/legal/` — memo, Motion Studio pages (Draft 2), NexaTute pages (Draft 2), MoA objects clause, research note `research_2026-10-30.md`, markdown sources in `source/` |
| Reviews | `docs/reviews/` — gaps + admin control (review 2), third review (`review3_2026-10-30.md`) |
| Word/PDF builder used for all documents | `tools/docbuilder/` — `build.js` (docx-js; markdown → corporate Word), `pages.py` (two-pass contents page numbers), `build_doc.sh <dir> <out.docx>` (needs `meta.json`, `order.json`, `sec/front.md`, `sec/*.md`; set paths at the top of the scripts) |
| NexaTute prototype (59 boards, artifact Version 156) | `prototype/` |

## What happened on 29–30 Oct 2026 (summary — details in decisions.md and docs/memory/areas/motion-studio.md)
- Motion Studio: final per-minute rates; 4K Escalating; ~150 approved features incl. emotions, child-character voices, Voice Clone Studio, digital twin, AI Co-Director, international-standard set, package placement matrix; lifetime free account; discount caps (45% per-minute / 30% fee, one promo discount, 30% margin floor); Free Beta = all features within daily limits (clone/twin/face acting only after legal clearance); futuristic admin with Co-Admin; 19 admin pages + central settings registry; protected settings change with 3 approvals + 24 h delay (not hard-locked, laws change).
- Company: RemonLogic Private Limited — RJSC application Sun 1 Nov 2026; MoA objects draft ready; USA LLC via doola.com (lawyer must confirm Bangladesh Bank outward-investment approval first); second payment gateway — owner's initiative.
- **No stored money anywhere** (Bangladesh Bank 2024 prepaid-instrument rules): pay per order / per plan; credits, minute packs, gift cards, reseller packs, NexaLogicDev credits, Shikkha Salami become named plan codes or per-order prices; refunds to the original payment method.
- Accounting: one ledger with product + funding tags; costs split by measured use (OpenCost); everything admin-controlled.
- Every customer-facing email address is set in admin; one separate address per type of work, each routed to a team; which person/team does which job is assigned in admin ("People, teams & job assignment" page).

## In progress when the previous account stopped (check before redoing)
1. **Legal memo update + gap solutions: DONE** (memo Draft 2, 42 pp, wallet options relabelled P1–P4 with P1 decided; gap solutions with admin pages, the "People, teams & job assignment" page design and the per-purpose email table in `docs/reviews/gap_solutions_2026-10-30.md`). Gap solutions are Claude defaults — show them to the owner for approval if not yet approved.
2. The owner asked for **another review after this work finishes** (fresh agent; check the updated legal drafts and decisions for contradictions).
3. Still-open owner decisions (front notes of the legal drafts): pre-production fee timing; annual-plan refund rule; Motion Studio first-30-days refund; minimum age for under-18 profiles outside the USA; whether the 45%/30% discount caps also apply to NexaTute (institution discount is 40%); third-party voice/face cloning at launch (review recommends own voice/face only at launch).

## Next steps (owner's order)

> **Owner decision 30 Oct 2026: finish all three prototypes first — NexaTute (all additions in `docs/tasks/` and decisions.md), Remon Motion Studio, NexaLogicDev. Real code (backend/frontend Issues) starts only after that.** **First do the owner's ordered cross-product audit (`docs/tasks/cross-product-audit.md`) together with the requested review.** Every account works on prototypes until then; split boards by area, each ≤ 1.8 MB; follow the model split in CLAUDE.md.

1. **Sat 31 Oct 10:00 Dhaka** (scheduled reminder in the old session; the new account must start it itself): logos (with the owner) + live websites nexatute.com and remonlogicstudio.com with the legal pages (use Draft 2 pages; contact emails from admin placeholders; trade licence not shown — but the lawyer should check the e-commerce display rule). Support phone/email still to be decided by the owner.
2. Owner: RJSC filing Sun 1 Nov with the MoA draft; lawyer review of the memo (wallet, Vitlous aamarPay account, children's data first).
3. Remon Motion Studio prototype (5–7 days; split boards by area from the start, each ≤ 1.8 MB; Opus coordinates, Sonnet builds, Haiku checks). Put ALL features into four phases first (launch / first 3 months / 2027 / later) — the owner wants all features in the Free Beta, so the Free Beta date will move.
4. NexaTute MVP list + week-by-week plan → GitHub Issues; then NexaLogicDev prototype.
5. Next Master Blueprint build (v32.11) with everything in decisions.md.
6. NexaTute prototype: add the Project & Competition Studio (approved 30 Oct 2026, see decisions.md) and highlight it on the landing page — full instructions incl. the new package and per-plan limits in `docs/tasks/project-studio-package.md`.
7. NexaTute prototype: add the "School Homework" dashboard section — `docs/tasks/school-homework.md`.
8. NexaTute prototype: class extra-time rule + pop-up notice (decisions.md, 30 Oct 2026) in X02/X06 class screens, guardian X08, Institute X12 and admin settings.
9. All three prototypes: Connected accounts + Share options — `docs/tasks/sharing-and-connectors.md`.
10. All three prototypes: Internal Video Service — `docs/tasks/internal-video-service.md`.
11. Motion Studio + NexaLogicDev prototypes: "Free class" menu and "Learn to do this" buttons into NexaTute — `docs/tasks/free-class-links.md`.
12. Motion Studio + NexaLogicDev prototypes: blogs (Motion Notes, Build Notes), SEO and marketing automation — `docs/tasks/marketing-automation.md`.

## Advice from the previous account
- The owner approves many ideas quickly. Before adding, check `docs/decisions.md` and `docs/memory/` for an existing decision under another name; say so when an idea already exists.
- Be honest about limits: no fake numbers, no legal conclusions, "(default, editable)" for Claude-chosen values, "(to confirm)" for open ones. Never claim a check you did not run.
- Keep money/children/legal items conservative: no stored balances; under-18 data rules; consent + OTP for voices/faces; AI labels and C2PA.
- Agents are fine for big drafting/reviews ("use as many agents as needed"); use "light mode" checks (see preferences).
- When a document is rebuilt, verify contents page numbers (pages.py) and render a few pages before sending.
- Keep committing `docs/decisions.md` after every approval; this repo is the shared memory between accounts.

## Known small items left (prototype)
- X12 "Open approval" on an already-open approval does nothing.
- Optional static frames not drawn: D05/D07 load test, G01/D04 What's new.
- X20 (≈1.80 MB) and X12 (≈1.77 MB) have little room left; next X20 split: Nexa Notes → new board.

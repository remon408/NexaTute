# NexaTute — instructions for every Claude session working in this repo

Read this file fully before doing anything. Then read `docs/HANDOVER.md`.

## The owner
- Md Raju Ahmed (RemonLogic). He writes in Banglish or Bengali; **reply in Bengali**, plain words, short.
- Build files only when he asks. Save every finalized decision (see "Decisions" below).
- Never claim something is done that you did not check.

## What this repo is
- `prototype/` — the approved clickable prototype of NexaTute (Design-canvas `.dc.html` boards, 59 boards: W00 index, Main, X01–X27 interactive prototypes, L/G/P/T/D static frames). It is the **spec** for the real product: every screen, text (6 languages), price, rule and admin control the owner approved.
- `prototype/shared/` — shared text/number sources the boards quote verbatim (kpi.md v1.23, numbers.md v16, hub.md v1.6, x20_live.md, guarantee.md v3.1, recording.md, sensory.md, bdsl.md).
- `docs/blueprint/` — Master Blueprint Corporate Edition v32.10 (382 pages): every decision A–Z (business, prices, architecture, software register, servers, legal, admin). **The blueprint is the source of truth for the real build.**
- `docs/briefs/` — the build briefs of every prototype pass; `fix17_pending.txt` is the dated owner-decision log.
- Real application code (front-end, back-end, database) will be added here; it does not exist yet.

## Hard rules (prototype)
- 6 languages everywhere: bn, en, hi, ur, ar, fr — identical keys; RTL for ar/ur; Latin digits (PlayBoom child screens are the only exception).
- Responsive 390 / 834 / 1024 / 1440; touch targets ≥ 44 px; contrast ≥ 4.5:1.
- **Every board file ≤ 1,800,000 bytes** (`wc -c`). The Design viewer silently drops any file over 2 MiB. X20 and X12 are near the limit — move a section to a new board rather than growing them.
- Admin sidebar must stay byte-identical on all admin boards (X10, X25, X26, X27 share one; X13–X22 share the other).
- Every user-visible value is admin-editable, marked "(default)", changed with two-person approval and logged.
- No fake reviews/partners/numbers; samples are labelled "sample (prototype)"; no scarcity wording ("only N seats left").
- USD = Taka × 0.015, nearest dollar, exact .5 rounds DOWN, no exceptions (৳500 = $7).
- Verify a changed board with `python3 prototype/tools/dcverify.py <board>` (0 problems, 0 parity). The tools were written for the original workspace; paths like `SP/...` inside them must point at this repo.

## Hard rules (real code, when it starts)
- Free/open-source licences only (check every dependency; no GPL in shipped server components unless the blueprint says so).
- Stack and components = the blueprint's software register (section 18.1). Do not add a component that is not there without asking.
- Privacy: under-18 data, guardian consent, masked IDs, no live location, counts-only with cells < 20 hidden; secrets never in code or logs.
- Money, people, legal and data-deletion actions need two-person approval and an audit log.

## How three Claude accounts work here
- **Lead** (integration): owns `main`, the DB schema, the API contract (OpenAPI), CI, reviews and merges.
- **Back-end**: takes GitHub Issues labelled `backend`.
- **Front-end**: takes GitHub Issues labelled `frontend`.
- One branch per issue (`backend/<issue>-<slug>`, `frontend/<issue>-<slug>`), Pull Request into `main`, tests must pass, lead reviews and merges. Nobody pushes directly to `main` except the lead for repo setup.
- Write progress to `docs/STATUS.md` (date, what changed, what is next). Do not work on another stream's issues.

## Decisions
- New owner decisions go to `docs/decisions.md` (date, exact decision) and, at the next blueprint build, into the blueprint. Claude-chosen values are marked "(default, editable)"; unsettled ones "(to confirm)".

## Which model does which work (owner order, 30 Oct 2026 — quality must be international standard, no mistakes)
Every account and every agent follows this. When unsure which model fits, use the stronger one.

| Model | Does | Never does |
|---|---|---|
| **Opus** | Planning and task split; architecture, DB schema, API contract (OpenAPI), security, privacy, child-safety, money, pricing maths, legal and data-deletion logic; blueprint and legal writing; hard bugs; final review of every change before it reaches `main`; coordinating the other agents; anything ambiguous | — |
| **Sonnet** | Building from a clear Opus spec: prototype boards, front-end and back-end feature code, tests, document chapters from a brief, first drafts of the 6-language texts, refactors | Final decisions on money, children, legal, security or pricing; merging to `main` without Opus review |
| **Haiku** | Mechanical checks: `dcverify.py`, file sizes (≤ 1.8 MB), 6-language key parity, button/link checks, search and inventories, log summaries, simple find-and-replace | Writing features, deciding anything, final approval |

Quality gates (all work):
1. Opus writes the spec → Sonnet builds → Haiku runs the mechanical checks → Opus reviews line by line → only then commit/merge.
2. Money, children's data, legal, security, auth, deletion and every price/number: Opus writes or Opus reviews every line; numbers re-calculated by code, not by hand.
3. Tests and `dcverify.py` must pass (0 problems, 0 parity); text checked in all 6 languages (RTL for ar/ur); WCAG 2.2 AA.
4. Never claim something is done or checked without actually running the check; report any failure to the owner plainly.
5. If a cheaper model's result looks doubtful, redo it with the stronger model — quality comes before saving usage.

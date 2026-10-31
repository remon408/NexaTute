# Audit 31 Oct 2026 — pending work, cross-product gaps, contradictions, board health

Ordered by the owner (31 Oct 2026: "onek pending kaz ase valo kore check koro") before the NexaTute prototype additions. Opus planned and reviewed; four agents swept the repo (read-only). Key claims were spot-checked by the lead (grep/wc on the boards and decisions.md).

| File | What it holds |
|---|---|
| `inventory.md` | Every pending NexaTute prototype item with grep evidence: 112 items — 6 DONE, 26 PARTIAL, 79 MISSING, 1 unchecked; plus non-prototype items (section J) |
| `crossproduct.md` | 44 cross-product features checked on 9 criteria (13 P0, 25 P1, 4 P2); status of every starting-point bullet of `docs/tasks/cross-product-audit.md`; 28 owner questions |
| `contradictions.md` | 81 places where a document still says what a newer decision changed (45 high, 27 medium, 9 low); Taka→USD recomputation; 16 conflicts inside decisions.md (Q1–Q16) |
| `boards.md` | All 59 boards: dcverify 0 problems / 0 parity each (6 languages); sizes; 10-language estimate; split plan; sidebar check; fonts; broken tool paths |

## Main findings (verified)
1. **Boards are in 6 languages** (bn, en, hi, ur, ar, fr); none has ja/de/zh/ko. At 10 languages ≈ +11.3 MB in total and 8 boards pass 1.8 MB (X07, X10, X12, X14, X16, X20, X25, X26) → split into ≈71 boards. `LANGS` is hard-coded in 19 boards. dcverify checks key parity against the board's own language list, so a 6-language board passes — a 10-language check must be added.
2. **Rename not started:** "Nexa Teacher" 2,342 times in 48 boards, "Nexa Tutor" 0.
3. **Old dates in boards:** Free Beta "20 November – 9 December 2026" (X20 and others); decision 31 Oct: pilot 1–14 Jan, Free Beta 15 Jan, paid 5 Feb 2027.
4. **Wallet / stored-value wording** remains in boards (21 boards mention "wallet" — each to be checked), the Master Blueprint, the Motion Studio blueprint (~60 passages) and the memory export, against the 30 Oct no-stored-money rule.
5. **Two USD rules in decisions.md** (verified): Taka × 0.015 (line 90, CLAUDE.md) vs "BDT +35% at ৳122 = $1" (lines 13, 73) for Motion Studio / NexaLogicDev. Owner must pick one.
6. **Not built at all:** Nexa Speak, Nexa Scripts, Project & Competition Studio, School Homework section, class extra-time pop-up, first-visit language prompt, full Share sheet, Human Conversation Club, discount caps, protected settings, People/teams page.
7. **Legal drafts out of date:** refund rule (30 Oct), third-party cloning at launch, minimum age, GPU location (Netherlands), pre-production fee; HANDOVER still lists these as open.
8. **Admin sidebar rule:** X10/X25/X26/X27 identical; X13–X22 are not identical (8 different hashes).
9. **Tools:** `prototype/project/support.js` (loaded by every board) is missing from the repo; build/check scripts point at the old workspace paths.

## Proposed order (to approve)
1. Owner answers the key decisions (USD rule, discount caps, NexaLogicDev age, under-18 and outside AI, Nexa Scripts in the Pass, minute/Boost packs, adult-only pilot, then-vs-now clips).
2. Fix tools (support.js, paths, 10-language check in dcverify).
3. Split the 8 full boards, then text fixes on all boards (rename, dates, wallet, refund, GPU/Valkey).
4. New NexaTute features on new boards; then the 4 new languages (text by Sonnet, marked "native review pending").
5. Fix contradictions in task docs, memory export, legal drafts (Motion Studio blueprint fixes go with the Motion Studio prototype).

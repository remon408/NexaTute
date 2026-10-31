# Nexa Verify (RASP) — admin controls in all three admin panels

Owner order, 31 Oct 2026: every Nexa Verify control is in the admin panel — NexaTute, Remon Motion Studio and NexaLogicDev, each for its own product, plus a shared view for the company-wide parts. Every value shows "(default)", changes need two-person approval and are logged; legal/safety floors are protected settings (3 approvals + 24 h delay). Spec: `docs/specs/RASP_Master_Specification_2026-10-31.docx`; decisions 31 Oct 2026.

## Page "AI Quality (Nexa Verify)" — sections and controls (Claude defaults, editable)

| Section | Controls |
|---|---|
| Overview | Live status of every check; verified / corrected / caveated / abstained / sent-to-human counts; error rate; human review hours; cost and GPU use per product; alerts |
| Risk tiers | Which task types are T0 / T1 / T2 / T3; rules that raise a tier (uncertainty, audience size, under-18, money, irreversible); per-tier required checks and decision (release, correct, caveat, abstain, review, block) |
| Checks (validators) | Turn each validator on/off per task type and language; thresholds; retry limits (count, time, tokens, cost); fallback order; which models/tools may verify (under-18: own servers only — protected) |
| Human review | When an item goes to a person (AI unsure, T3, appeal, random sample %); random sample 2–5% (default); review queues, owners, SLAs, double review for critical items; reviewer workload limits; calibration checks |
| Sources & knowledge | Approved source registry (board, edition, licence, freshness); correction registry with scope, expiry, rollback; quarantine of new sources; Islamic-content source rules |
| Reports & appeals | "Report a mistake" settings (who can report, AI re-check first, reply to reporter); appeal flow and deadlines |
| User-facing labels | Texts and when to show "Verified against our checks / Being reviewed / Could not verify" in all 10 languages; trust-page and Reliability Passport fields shown to users |
| Models & releases | Model/prompt/validator versions in use; shadow test, canary %, rollback; quality-drop alerts |
| Capacity & cost | GPU cards reserved for Nexa Verify (default: 1–2 cards on A6000 #1/#2); per-product budget ceilings; light-check mode for live voice (<1 s target); overload behaviour |
| Privacy & retention | What the Reliability Passport stores, retention per product, deletion propagation; under-18 data rules (protected) |
| Safety switches | Kill switch / safe mode per product and per check; election-period mode; incident links |
| Audit log | Every change: who, when, old → new value, approvers, reason |

## Where it appears
- NexaTute admin (prototype: new board in the admin group, sidebar entry in both admin groups as decided by the integration rules).
- Remon Motion Studio admin (old account builds it in `prototype-motion-studio/`).
- NexaLogicDev admin (with the NexaLogicDev prototype).
- Shared company view (GPU, source registry, model registry, audit) linked from all three.

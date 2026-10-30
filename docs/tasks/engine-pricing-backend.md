# Task (backend + admin) — engine pricing for Claude / GPT / Grok in NexaLogicDev (owner order 30 Oct 2026)

Owner: "these must be set in the back end". Build this into the NexaLogicDev billing service and admin panel (prototype first, then real code). All values admin-editable, dual approval, append-only audit log.

## Price formula (per task)
- Nexa Engine credits = (input tokens ÷ 5 + output tokens) ÷ 2,500 (Heavy); Fast = ÷ 20,000.
- External engine credits = max( API cost in USD × FX (৳122/$) × markup ÷ credit value , Nexa Engine credits × 1.10 ), rounded up.
  - markup default = 1 ÷ 0.70 ÷ 0.83 (≥30% margin after 15% VAT and ~2% gateway); credit value = ৳4.35 (largest Boost pack).
  - Floor rule: an external engine is never cheaper than Nexa Engine + 10% for the same task.
- Default credits per 1M tokens (input / output): Claude Opus 5.5 193 / 965 · GPT-5.3 Codex 84 / 676 · Grok 4.6 97 / 290 (after benchmark) · Nexa Heavy 80 / 400 · Nexa Fast 10 / 50.

## Example prices (credits, ≈৳ at Boost-pack value)
| Task | Nexa Engine | GPT-5.3 Codex | Grok 4.6 | Claude Opus 5.5 |
|---|---|---|---|---|
| Small (50k in / 10k out) | 8 (৳35) | 11 (৳48) | 9 (৳39) | 20 (৳87) |
| Medium (200k / 40k) | 32 (৳139) | 44 (৳191) | 36 (৳157) | 78 (৳339) |
| Large (1M / 200k) | 160 (৳696) | 220 (৳957) | 176 (৳766) | 387 (৳1,683) |

## Backend pieces
1. Engine price table (per engine: API input/output/cached price, long-context surcharge e.g. Grok ×2 above 200k per call, FX rate, markup, VAT %, gateway %, floor %, on/off, plans allowed) — admin page "AI Engines & Pricing"; price changes by dual approval, apply to new tasks only.
2. Estimator: before a task, predicts tokens per engine from task size + history and shows the side-by-side card (credits, ≈৳, our benchmark pass rate, data location, "recommended").
3. Credit hold: holds the estimate (+20% buffer, default) at start; meters real tokens per API call (provider usage fields); settles actual cost at the end and releases the rest; if actual would exceed the hold, pause and ask the user (never silent overspend).
4. Failure rules: provider error or our failure → no charge; fixing the AI's own bug → free; refunds of paid-per-task money to the original payment method.
5. Plan rules: Free = Nexa Engine only; Student/Hobby = external engines pay-per-task only; Pro/Team = from plan credits; under-18 external engines need guardian consent; "RemonLogic servers only" disables external engines.
6. Bring-your-own key (Pro/Team): key stored encrypted in the secrets vault; tokens billed by the provider to the user; we charge 0 credits (optional small platform fee — to confirm).
7. Caps: per-provider monthly spend cap (company), per-user daily/monthly cap, alert at 75% / 90%.
8. Secret removal (Gitleaks) before every external call; provider name and data location logged per task.
9. Accounting: API invoices paid by the USA LLC in USD; each task's API cost and revenue tagged to NexaLogicDev's book; engine profit report (usage share, pass rate, margin per engine).
10. Price-sync check: monthly reminder to compare vendor price pages with the table; vendor price change → proposal → dual approval.

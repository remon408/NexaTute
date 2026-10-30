# NexaLogicDev — credits without stored money, benchmark plan, unit costs (approved by the owner 30 Oct 2026)

## 1. Credits under the "no stored money" rule (lawyer to confirm)
| Before | Now |
|---|---|
| Monthly plan credits | Same, lapse at month end; no carry-over, no cash value |
| Free 3 credits/day | Same, lapse at day end |
| Top-ups (180-day validity) | "Boost pack" add-on at the same prices, valid until the end of the current plan month |
| Out of credits | Buy a Boost pack, or pay for that one task at its shown price |
| NexaCoins | Removed; only XP and badges (no money value) |
| Remix Gallery NexaCoins | XP + badge; sales paid under the marketplace commission rules |
| Two-sided referral bonus credits | Referred user: first-month discount; referrer: discount on the next bill |
| Lifetime 10% referral | Paid out monthly to bKash/Nagad/bank; no balance held beyond the payout cycle |
| Hackathon credit prizes (500/300/150) | A free Pro/Hobby month |
| "One wallet" | One Nexa ID with XP only |
Same treatment for Motion Studio / NexaTute credits or minute packs (cross-product audit); one referral rule for all three products.

## 2. Benchmark (one week on a rented server, before buying the Heavy server)
- 200 real task types (landing page, Laravel and React apps, WordPress plugin, bug fixes, Auto-Architect Medium module).
- Models: GLM-5.2 (8×A100), DeepSeek-V4-Flash and Qwen3-Coder-Next (8×A6000).
- Measure: build pass rate after the verify loop (target ≥90%), time to first token, tokens/s, concurrent users at target speed, cost per task.
- Rule: if GLM-5.2 serves ≥8 concurrent Heavy jobs at ≥15 tokens/s → all Heavy work on GLM-5.2; otherwise GLM-5.2 for planning and Complex modules, medium tasks on DeepSeek-V4-Flash.

## 3. Unit cost per credit (estimate; assumptions: €1 = ৳140, 8×A6000 ≈ 2× the 4×A6000 rent, 50% utilisation)
| Lane | Throughput | Cost/credit |
|---|---|---|
| Heavy GLM-5.2 | 500 / 1,500 / 3,000 tok/s | ৳1.08 / ৳0.36 / ৳0.18 |
| Fast Qwen3-Coder-Next | 3,000 / 6,000 / 10,000 tok/s | ৳2.01 / ৳1.00 / ৳0.60 |
Net per credit after VAT, gateway and reseller discount: ৳3.57–4.67.
- Credit prices stay. If benchmark cost per credit > ৳1.00 on a lane, reduce tokens per credit for that lane (e.g. Fast 20,000 → 15,000) to keep ≥70% margin — admin-editable, two-person approval, only from a new billing month with advance notice.
- Get the real 8×A6000 rent quote.

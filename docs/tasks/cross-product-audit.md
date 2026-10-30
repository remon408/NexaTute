# ORDER from the owner (30 Oct 2026) — find every missing connection between the three products

The owner said: connections between NexaTute, Remon Motion Studio and NexaLogicDev must be found by Claude, not by him. Do this audit BEFORE finishing the prototypes (together with the review he already asked for). Opus leads; use as many agents as needed.

## How
1. Read docs/decisions.md, docs/memory/, docs/tasks/, the Master Blueprint (docs/blueprint/) and the Motion Studio blueprint (docs/motion-studio/).
2. List every feature that uses another product (video, code, accounts, payments, data, AI, servers, marketing, support, legal). For each, check that ALL of these are defined: user flow, technical connection (API/service account), who pays and which book it goes to, priority/capacity, safety and under-18 rules, privacy/consent for cross-product data, storage/retention, failure handling, and admin controls in EVERY affected product's admin panel.
3. Also find contradictions with newer decisions (e.g. anything still using a stored wallet or credits after the "no stored money" decision of 30 Oct 2026).
4. Write the result to docs/reviews/cross_product_audit_<date>.md: table (feature · products · what is missing · proposed fix · default values), then show the owner a short Bengali summary for approval. Save approvals to docs/decisions.md.

## Starting points already spotted (check and complete them; the list is NOT complete)
- One Nexa ID / single sign-on across the three products and the three admin panels; one consent + one unsubscribe for all three.
- Shared marketplace (NexaTute, Motion Studio, NexaLogicDev, third-party goods): checkout, seller payouts, refunds, tax, with no stored balance.
- NexaLogicDev credits and Motion Studio/NexaTute "credits", gift cards, reseller packs, Shikkha Salami → named plan codes or per-order prices (no wallet).
- Learn → Earn: 18+ learners doing real projects through NexaLogicDev or Motion Studio — how they are paid ("learning credits" vs no-stored-money rule), contracts, tax, child rules.
- NexaTute course "Making videos with AI" → Motion Studio trial/discount; Motion Studio free 45-min training inside NexaTute; cross-course recommendations.
- Shared Co-Admin, command bar, People/teams & job assignment page and per-purpose email routing — one setup or per product?
- Shared Nexa Guard / content-safety service, C2PA signing, AI labels across products.
- Shared GPU pool, priority lanes and cost allocation (NexaLogicDev pools join 2027).
- Shared referral system, Marketing Hub, CRM, share/verify pages (docs/tasks/sharing-and-connectors.md).
- Shared support (AI first → email → human) and the legal pages of each site referencing the others.
- NexaLogicDev building websites/apps for NexaTute institutions, and Motion Studio videos for those sites.
- Internal Video Service (docs/tasks/internal-video-service.md) — check it against all of the above.
- Free class / "Learn to do this" links between Motion Studio, NexaLogicDev and NexaTute (docs/tasks/free-class-links.md).

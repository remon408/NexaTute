# Task — Internal Video Service: NexaTute and NexaLogicDev make videos through Motion Studio (approved by the owner 30 Oct 2026)

Not built yet. Values are Claude defaults (editable in admin, two-person approval, logged).

1. Motion Studio runs an internal video service; NexaTute and NexaLogicDev call it with their own service accounts (OAuth client credentials + mTLS through APISIX; scopes per product). Users need no Motion Studio account; inside NexaTute/NexaLogicDev it is that product's own "Make video" button with a small "powered by Remon Motion Studio".
2. Job: template, script, voice, avatar, language, resolution, max length, safety profile → estimate → live progress (Centrifugo/webhook) → result delivered straight into the calling product's own storage (e.g. the student's "My Projects").
3. Money: NexaTute — taken from the student's plan limits, no extra charge; Motion Studio charges NexaTute's books an internal per-minute price (internal transfer, removed in the consolidated report). NexaLogicDev — the old "৳5 = 1 credit" rule conflicts with "no stored money": replace with per-order payment at the Motion Studio price or minutes included in the plan.
4. Priority: NexaTute live classes always first; student videos in their own queue lane, 720p, Quick/Enhanced mode, non-urgent jobs in the night window; ETA shown.
5. Child safety for every NexaTute job: "child-safe" profile, library voices/avatars (own voice only with guardian approval), Nexa Guard + Motion Studio safety checks, AI label + C2PA, pseudonymous ID instead of names, Motion Studio deletes its working copy 7 days after delivery.
6. Failures auto-retry; a failed job never counts against the student's limit.
7. 18+ users can press "Open in Motion Studio" (same Nexa ID) to edit further in the full editor.
8. Admin: the connection is controlled from ALL THREE admin panels — NexaTute, Motion Studio and NexaLogicDev: on/off per product, monthly quota, internal price, GPU share, alerts.

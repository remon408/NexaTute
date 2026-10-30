# RemonLogic Unified Credit, Billing, AI Benchmark & Governance Policy v3.1 — owner-approved with Claude's corrections (30 Oct 2026)

Owner rules: NO phases — every feature below is in the launch scope of the product it belongs to; Claude's review comments are approved. Applies to NexaTute, Remon Motion Studio and NexaLogicDev. All values admin-editable, dual approval, append-only audit log.

## A. Principles (all three products)
No stored monetary wallet · time-bound entitlements (credits/Boost packs lapse at day/month end, no carry-over, no cash value) · transparent checkout (tax, VAT, expiry, refund policy) · least privilege + dual authorization · append-only audit log (actor, time, reason, before/after) · Break-Glass protocol (section F). Never use the word "prepaid" for packs ("Boost pack" only). Lawyer to confirm the no-stored-money design.

## B. Credits & rewards matrix
Monthly plan credits lapse at month end · Free 3 credits/day reset at 24:00 (timezone shown) · Boost pack valid to end of the current billing month, expiry date/time shown at checkout · out of credits → Boost pack or pay-per-task with estimated charge shown before start · NexaCoins removed → XP + badges, no money value · referral bonus → first-month discount for the new user, next-invoice discount for the referrer.
Referral commission (one rule for all three products): 10% for 12 months (default) with a per-customer cap (admin); Pending → Approved (after the 30-day refund window) → Paid monthly to bKash/Nagad/bank, no balance held; net of VAT, tax and gateway fees; no self-referral, fraud checks, no cash commission for under-18; withholding tax confirmed by the tax adviser.

## C. NexaLogicDev international-standard features (all at launch)
- Security: SOC 2 / ISO 27001 controls from day one (certificates when the audits complete — SOC 2 Type II needs an observation period, so the badge comes after it; never claim before); BYOK; private deployment in the client's own AWS/GCP (VPC); SSO (SAML/OIDC: Okta, Azure AD) for Team/Enterprise; audit-log export to the client's SIEM; microVM sandbox isolation (Kata Containers, already planned).
- AI governance: one ISO/IEC 42001 AI management system for all three products (certification after audit); EU AI Act — NexaLogicDev coding AI is generally not high-risk, Article 50 transparency applies ("you are talking to an AI"); NexaTute assessment = high-risk part; Motion Studio deepfake labels (already). Human-in-the-loop: AI recommends, people decide.
- Multi-file context and whole-repository understanding (architecture, dependencies, DB schema).
- Automated Visual QA: Playwright (Apache-2.0) headless visual regression after UI/landing-page builds, auto-fix of mismatches.
- CI/CD & DevSecOps: GitHub Actions / GitLab CI integration; OWASP Top 10, hard-coded secrets and licence scans on generated code.
- Multi-tenant team workspaces: roles Admin/Developer/Viewer; AI code review on every GitHub pull request (Team plan).
- Global payments: Paddle as Merchant of Record (5% + 50¢) primary; Lemon Squeezy (now owned by Stripe) only as backup after confirming it accepts our USA LLC and payouts; verify Paddle's usage-billing/MCP claims with Paddle. Semantic cache (no vague "edge-cached inference").
- Competitors for positioning: Lovable, Bolt.new, Replit, v0, Cursor (HeyGen/Runway are Motion Studio's competitors).
- Value-based messaging: credits presented as "AI labour / agentic fuel"; prices unchanged; no unproven savings claims.

## D. Benchmark (before buying the Heavy server, 1 week, 200 tasks)
Split: Landing/UI 30 · Laravel 35 · React/Next.js 35 · WordPress plugins 25 · Debug/refactor 25 · Auto-Architect Medium 30 · Integrations/auth 20. Standardised, reproducible suite (SWE-bench Verified subset for comparison with published scores; "VibeCodingBench" name to verify).
Metrics: Pass@1 AND pass after the write → run → fix loop (≥90% target), TTFT, tokens/s, concurrent users at target speed, wall time, cost per successful build. Code Acceptance Rate measured in the pilot with real users. Models: GLM-5.2, DeepSeek-V4-Flash, Qwen3-Coder-Next (self-hosted); Claude Opus 5.5 / other API models only as a reference baseline (model names to verify).

## E. Credit economics
GPU cost per credit (not "all-in"; all-in adds sandbox CPU, storage, bandwidth, support): Heavy ৳0.18–1.08, Fast ৳0.60–2.01 (see docs/tasks/nexalogicdev-credits-benchmark.md); margin table verified by code (one cell fix: Fast ৳2.01 at ৳4.67 net = 57.0%). Review trigger when a lane exceeds ৳1.00/credit → change tokens per credit from a new billing month with notice and dual approval.

## F. Governance roles & Break-Glass
Role matrix (initiator → approver 1 → approver 2 → audit): credit conversion change (Product/Finance → Finance Lead → Authorized Admin, immutable log); plan price change (Product → Finance Lead → Executive = owner); large refund/manual adjust (Support → Finance Lead → Authorized Admin, ticket + reason code); referral rate change (Growth → Finance Lead → owner, legal/tax sign-off); model routing & cost policy (Engineering → Engineering Lead → Finance/owner, benchmark evidence); AI risk / human-in-the-loop trigger (AI Governance Lead → Legal/Compliance → owner, ISO 42001/EU AI Act documents). Shown on the "People, teams & job assignment" admin page; AI Governance Lead combined with the DPO or Security owner at first.
Break-Glass: only for making things safer (switch a feature off, block a user, roll back); never for payments, large refunds, children's data export or loosening legal/safety protections (those keep 3 approvals + 24 h delay); triggered by super admin or security owner, elevated access expires after 2 h, instant alert to the owner, second-person review within 24 h, reason code in the immutable log.

## Reality note for the owner (not a phase, a constraint)
BYOK, private-cloud deployment, SSO and SIEM export at launch need more engineering than the 2 dedicated NexaLogicDev engineers planned — the cross-product audit must re-plan team/funding or the launch date (owner: quality before dates).

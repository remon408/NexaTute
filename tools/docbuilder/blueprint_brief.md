# Brief — Remon Motion Studio Blueprint, Edition 1.0 (30 October 2026)

You are writing part of a standalone, corporate-grade **Remon Motion Studio Blueprint** (Word document) for RemonLogic Private Limited (Dhaka, Bangladesh; RJSC registration being applied for). Readers: the owner, board, investors, the lawyer/accountant and the developers who will build it. It must be complete A–Z for Motion Studio only (NexaTute and NexaLogicDev appear only where they connect to Motion Studio).

Folder: /tmp/claude-0/-home-claude/9878cfdb-4647-5257-a0fe-47a0a28067df/scratchpad/msbp
- `src/` — sources (read-only):
  - `src/decisions.md` — newest owner decisions (29–30 Oct 2026). HIGHEST PRIORITY.
  - `src/memory_decisions.txt` — owner decision memory: section "/areas/motion-studio.md" (newest Motion Studio decisions, 21–30 Oct 2026), "/areas/remonlogic.md" (older decisions incl. a "## Motion Studio" part from 17–22 Oct), "/areas/remonlogic-accounting.md", "/areas/remonlogic-growth-platform.md".
  - `src/memory_nexatute_etc.txt` — other memory (pricing, admin, nexatute infra, nexalogicdev) — only for cross-references.
  - Chapter text of the current Master Blueprint v32.10 (`src/04_Remon_Motion_Studio_Detailed_Feature_.txt`, `src/35_Remon_Motion_Studio_Rights_Safety_and.txt`, `src/Appendix_F_*.txt`, `src/Appendix_G_*.txt` (G.3 storage, G.4 remakes, G.8 packages/rates, G.9 Islamic, G.10, G.11), `src/11_Commercial_*.txt` (11.10–11.11), `src/06_*`, `src/07_*`, `src/08_*`, `src/09_*`, `src/18_*` (software register), `src/19_*`, `src/13_*`, `src/23_*`, `src/38_*` (admin, accounting), `src/33_*` (reseller), `src/28_*`, `src/29_*`, `src/16_*`, `src/17_*`, `src/21_*`, `src/00_*`). Lines starting with # are headings. Tables were flattened: each cell is one line.
- Write your output ONLY to the file(s) named in your task under `sec/`.

## Precedence (very important)
1. `src/decisions.md` and the newest dated lines in "/areas/motion-studio.md" win over everything.
2. Then older memory lines; then Master Blueprint v32.10 text.
Known overrides you MUST apply:
- Per-minute rates: use the final 29 Oct 2026 table in decisions.md (3D 480p/720p Esc/720p/1080p Esc/1080p: Mini ৳30/৳55/৳72/—/৳120; Starter & Premium Starter ৳30/৳55/৳72/৳85/৳120; Professional ৳25/৳50/৳66/৳78/৳120; Agency —/—/৳62/৳74/৳120; Cinematic Mini ৳41/৳74/৳97/—/৳162; Starter & Premium Starter ৳41/৳74/৳97/৳111/৳162; Professional ৳34/৳68/৳89/৳102/৳162; Agency —/—/৳84/৳96/৳162). New 4K Escalating ৳142 (3D) / ৳192 (Cinematic), Islamic ৳107/৳144, USD $1.57/$2.12, Starter and above. Any older G.8 rate numbers are superseded — do not repeat them.
- Islamic = 25% off each rate; USD = BDT +35% at ৳122 = $1 (to the cent); EUR and GBP prices also offered (via Paddle); recompute nothing you are not sure of — say "computed by the same rule" instead of inventing figures.
- Delivery tiers (Express +20% / Normal ≤12 h / Slow ≤24 h −10%) replace time-of-day pricing.
- Free Beta for Motion Studio starts 20 December 2026 (30 days); paid start date to be set; 2-week closed pilot (10–15 businesses) before the public Free Beta; Free Beta pass conditions decide the paid launch; dates may move if quality is not ready.
- Storage: Free/Trial 1 GB, Mini 5 GB, Starter 10 GB, Premium Starter 20 GB, Professional 40 GB, Agency 80 GB; add-ons +20 GB ৳80, +50 GB ৳180, +100 GB ৳300 /month.
- Payments: aamarPay (bKash, Nagad, cards; also international cards) now; Paddle for international when its API is approved. Wallet = non-cash-out prepaid credit; money taken from the wallet at storyboard approval (rules in decisions.md).
- Package names: Freelancer Mini (৳499/mo), Freelancer Starter (৳999), Premium Starter (৳1,999), Premium Professional (৳3,999), Premium Agency (৳7,999), Enterprise (contact sales). Short names Mini/Starter/Premium Starter/Professional/Agency are fine after first use. Check Appendix G for USD fees ($6/$11/$22/$44/$89).
- GPU: plan starts with a 1-week test on one rented 8× RTX A6000 server; the master blueprint's server list is the baseline architecture — describe Motion Studio's use of the shared GPU pool and say final server choice follows the benchmark.

## Style
- Plain, clear British-style business English; short sentences; no hype, no marketing superlatives. Explain "why" briefly where useful.
- Never invent numbers, partners, customers, reviews or legal conclusions. Values Claude chose are marked "(default, editable)"; unsettled ones "(to confirm)". Everything user-visible is admin-editable with two-person approval and logged — say so where relevant, not in every line.
- Legal points are positions for a lawyer to check, not legal advice.
- No duplicate content across chapters: if another chapter owns a topic, write one line "See chapter N" instead.
- Use tables for comparisons, prices, matrices; bullets for lists; paragraphs for reasoning.

## Format (strict — a script converts it to Word)
- `# N. Title` chapter (one per chapter), `## N.M Title`, `### N.M.K Title`.
- Paragraphs: plain lines separated by a blank line. Inline `**bold**` allowed. No italics, no links, no HTML, no images, no code blocks.
- Bullets: `- text`; second level: two spaces then `- text`. Numbered lists: `1. text`.
- Tables: GitHub pipe tables with a header row and `|---|` separator; keep ≤ 7 columns; keep cell text short.
- Callout box: a line starting `> ` (one paragraph) for key rules or notes.
- Do not write a contents list or cover; chapters only.

## Chapter plan (whole document — so you know who owns what)
1. Executive Summary and Product Mandate
2. Market, Customers and Competitive Position
3. Product Overview, Creation Workflow and Render Modes
4. Feature Catalogue — Creation, Voice and Quality
5. Feature Catalogue — Business, Collaboration, Accessibility and International
6. Packages and Feature Access
7. Pricing, Billing and Payments
8. Free Trial, Closed Pilot and Free Beta
9. Client Experience, Onboarding and Support
10. Technology Architecture, AI Models and GPU Capacity
11. Data, Storage and Media Lifecycle
12. Safety, Rights, Legal and Compliance
13. Admin Panel
14. Accounting, Cost Allocation and Unit Economics
15. Operations, Quality Assurance and KPIs
16. Risk Register
17. Roadmap and Release Gates
18. Open Items and Confirmations
Appendix A. Decision Log (dated) · Appendix B. Glossary

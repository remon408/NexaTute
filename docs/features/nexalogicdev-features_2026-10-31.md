# NexaLogicDev — Feature Catalogue (state of 31 Oct 2026)

**NexaLogicDev is RemonLogic's AI app and website builder: a browser IDE, website, WordPress and wireframe builders, and the Auto-Architect app factory, running on our own GPUs. This catalogue lists 180 features in 13 areas, plus the plans and prices table.**

Key facts: pilot ≈ 1–14 Apr 2027 · Free Beta 15 Apr 2027 · paid launch 6 May 2027 (decisions.md:190). Everything is in launch scope ("no phases", unified-credit-governance.md). No stored money anywhere. USD = BDT × 1.35 ÷ 122, shown to the cent (decisions.md:204, :213). Every value is admin-editable, "(default)", changed by two-person approval and logged.

---

## Plans and prices

Source: blueprint §32.9 (plan prices and credits), decisions.md:139, :146, :154, :212–213, nexalogicdev-modules-wordpress.md, nexalogicdev-credits-benchmark.md, engine-pricing-backend.md, unified-credit-governance.md, memory/areas/nexalogicdev.md. USD worked out with Python: round(taka × 1.35 ÷ 122, 2).

| Plan / package | Price ৳ | USD | Credits / limits | Notes |
|---|---|---|---|---|
| Free | 0 | 0 | 3 credits/day (lapse at 24:00) | Nexa Engine only; 1 new static site a day, max 5 live; 1 GB; 200 Tab suggestions/day; 0 Background Agents |
| Student Plan | 299/month | 3.31 | 250 credits/month | Verified NexaTute learner; Explain mode on; 3 GB; 1 Background Agent |
| Hobby | 499/month | 5.52 | 400 credits/month | 5 GB; 2 Background Agents |
| Pro | 2,499/month | 27.65 | 1,500 credits/month | Fast and Heavy lanes; 25 GB; 4 agents; 1 Nexa Cloud Starter app included |
| Team | 9,999/month | 110.64 | 6,000 credits/month, pooled | 5 seats; 100 GB pooled; 8 agents shared; 3 Starter apps; 1 Auto-Architect module a month (lapses if unused) |
| Enterprise | from 49,999/month | 553.27 | By contract | 10 users, SSO, SIEM export, BYOK, SLA (default, final per contract) |
| Private-cloud setup | from 2,00,000 one-time | 2,213.11 | — | In the client's own AWS/GCP (VPC) |
| Boost pack 1 | 199 | 2.20 | 35 credits | All Boost packs: valid to end of the current plan month; no cash value; never called "prepaid" |
| Boost pack 2 | 499 | 5.52 | 100 credits | |
| Boost pack 3 | 999 | 11.05 | 210 credits | |
| Boost pack 4 | 2,499 | 27.65 | 550 credits | |
| Boost pack 5 | 4,999 | 55.32 | 1,150 credits (৳4.35 each) | ৳4.35 = credit value used for external-engine pricing |
| Pay per task | Shown before start | — | One task | When credits run out |
| Auto-Architect Basic | 1,499 | 16.59 | ≤5 screens, ≤5 tables, 1–2 roles, email only | Price locked after AI size check |
| Auto-Architect Medium | 4,999 | 55.32 | ≤15 screens, ≤15 tables, ≤4 roles, 1–2 integrations | Free 1-min handover video |
| Auto-Architect Complex (per module) | 9,999 | 110.64 | ≤30 screens, ≤30 tables, permission matrix | Free handover video. The scope table exists in the task file, but the blueprint §32.2 still has none — add it at v32.11 (to confirm) |
| WordPress Template pack | 499 | 5.52 | Page designs/patterns | Any paid plan; Pro/Team may use credits |
| WordPress Plugin Basic | 999 | 11.05 | 1 function + settings page | |
| WordPress Theme | 1,999 | 22.12 | Block theme, 5 templates | |
| WordPress Plugin Advanced | 2,999 | 33.19 | CPTs, WooCommerce, REST API | |
| WooCommerce theme | 3,999 | 44.25 | Full shop theme | |
| Nexa Engine Fast rate | — | — | 10 / 50 credits per 1M input/output tokens | 1 credit = 20,000 Fast tokens (input counts 1/5) |
| Nexa Engine Heavy rate | — | — | 80 / 400 credits per 1M input/output tokens | 1 credit = 2,500 Heavy tokens (was 1,000) |
| GPT-5.3 Codex | — | — | 93 / 743 credits per 1M | Includes +10% surcharge; never cheaper than Nexa Engine + 10% |
| Claude Opus 5.5 | — | — | 212 / 1,062 credits per 1M | Same rules |
| Grok 4.6 | — | — | 106 / 319 credits per 1M | Only if it passes the benchmark (to confirm) |
| Nexa Cloud Free | 0 | 0 | 1 app, 500 MB DB, sleeps | Per app per month |
| Nexa Cloud Starter | 799/app/month | 8.84 | — | |
| Nexa Cloud Growth | 1,999/app/month | 22.12 | — | |
| Nexa Cloud Business | 4,999/app/month | 55.32 | — | |
| Storage add-ons | 80 / 180 / 300 per month | 0.89 / 1.99 / 3.32 | +20 / +50 / +100 GB | |
| AI Shop Assistant | 299–699/month | 3.31–7.73 | Monthly conversation cap | Exact tiers (to confirm) |
| Pay-Per-Deploy | 199/month | 2.20 | 1 site on nexalogicdev.app or 1 custom domain | Blueprint §32.9 |
| Care Plan | 299 / 499 / 999 per month | 3.31 / 5.52 / 11.05 | Static / WordPress / WooCommerce-dynamic | Uptime, updates, monthly backup |
| Go Live Starter (.xyz) | 499 first year; 3,199 renewal | 5.52; 35.40 | Domain + hosting + SSL + email forwarding + Google | Renewal shown prominently |
| Go Live Shop (.shop) | 799; 8,999 renewal | 8.84; 99.58 | Same | |
| Go Live Business (.com) | 2,199; 3,199 renewal | 24.33; 35.40 | Same | Recommended |
| Play Store publishing | ≈999 one-time | 11.05 | PWA/Android (TWA) build | |
| University / polytechnic lab licence | (to confirm) | — | Classroom mode, teacher dashboard | Linked to NexaTute; no price set |
| SME / B2G bulk licences | (to confirm) | — | Bulk seats | Through the Partnership Manager |
| White-label (agencies) | (to confirm) | — | Own brand | Blueprint §32.9, no price |
| Referral | — | — | 10% for 12 months, cap per customer | Pending → Approved after 30-day refund window → paid monthly to bKash/Nagad/bank; no cash for under-18; new user gets a first-month discount |
| Store purchases | +30% | — | App Store / Google Play / Microsoft Store | Web price unchanged |

---

## Features by area

### 1. AI builder and engines
Source: decisions.md:137–148, :199, :201; engine-pricing-backend.md; nexalogicdev-credits-benchmark.md; unified-credit-governance.md D–E.

| Feature | What it does (one line) | Plans | Rules / limits |
|---|---|---|---|
| Nexa Engine Fast lane | Everyday coding, site building, small fixes | All | Qwen3-Coder-Next on A6000 #3 from 15 Mar 2027 |
| Nexa Engine Heavy lane | Plans, architecture, Complex modules | Pro, Team, Auto-Architect buyers | GLM-5.2 (MIT) on 8×A100; not lent to other products |
| Heavy backup model | Takes Heavy work if needed | — | DeepSeek-V4-Flash on A6000 #3 (final after benchmark) |
| GPT Codex review | Fixes the plan when Heavy is down or fails twice; reviews every Complex module; finishes after a third failure | Pro, Team, Auto-Architect | Replaced Claude Sonnet (30 Oct) |
| Engine choice card | Before each task: Nexa Engine / GPT Codex / Claude (/ Grok) with price, pass rate, data location, "recommended" | All (Free = Nexa only) | Nexa Engine always cheapest |
| External engines pay-per-task | Student/Hobby may pick Claude or GPT for one task | Student, Hobby | From plan credits on Pro/Team |
| Bring your own key (BYOK) | User's own API key, billed by the provider | Pro, Team, Enterprise | Key in secrets vault; 0 credits; no platform fee (default, editable) |
| "RemonLogic servers only" | Turns all outside AI off per project | All | Task waits for our servers |
| Price estimate and credit hold | Shows estimate, holds it +20%, settles real use | All | Pauses and asks before going over; never silent overspend |
| Failure = no charge | Failed builds and fixing the AI's own bugs are free | All | Refund to original payment method |
| Two-failure stop | Users without Heavy access: task stops after 2 fails, credits back, Pro offered | Free, Student, Hobby | — |
| Write → run → fix loop | AI builds, tests and fixes in the sandbox until it passes | All | ≥90% pass target |
| Architect → Builder split | Heavy plans, Fast writes files in parallel | Pro, Team | — |
| Semantic cache and docs retrieval | Faster, cheaper answers from official docs and own templates | All | Tenant- and project-aware |
| Multi-file / whole-repo context | AI understands architecture, dependencies, DB schema | All | — |
| Project Memory | Keeps each project's plan, decisions and files | All | Per tenant and project |
| Project Rules file | User's own rules the AI follows | All | — |
| Tab autocomplete | Inline code suggestions | All | Free 200/day; paid unlimited |
| Background Agents | Parallel AI jobs, start from web, mobile or WhatsApp | Student 1, Hobby 2, Pro 4, Team 8 | ≤2 h each, paid from credits |
| Secret removal | Gitleaks strips secrets before any outside call | All | Provider and data location logged |
| Spend caps and alerts | Company cap per provider; user daily/monthly cap | All | Alerts at 75% / 90% |
| 200-task benchmark | Picks models and lane rules before buying | — | ≥8 Heavy jobs at ≥15 tok/s rule; Grok included |
| Tokens-per-credit review | Lowers tokens per credit if GPU cost > ৳1.00/credit | — | New billing month, notice, dual approval |
| MiniMax M3 API Fast fallback | Paid Fast-lane fallback (blueprint) | Paid | Not mentioned after the 30 Oct engine change (to confirm) |

### 2. IDE and developer tools
Source: blueprint §32.2, §32.14; memory/areas/nexalogicdev.md:65–66; nexalogicdev-intl-features.md; decisions.md:143, :153.

| Feature | What it does (one line) | Plans | Rules / limits |
|---|---|---|---|
| NexaBrain Chat | AI chat that routes work to the right tool | All | 10 languages; code names in English |
| Voice to code | Speak instructions | All | In-browser Whisper first; 10 languages |
| Monaco editor + terminal | Code editor in the browser | All | Terminal hidden in beginner mode |
| Lint and format in browser | ESLint, Prettier (PHP too), Stylelint | All | Web Workers |
| Git in the browser | Clone, commit, branch (isomorphic-git), GitHub sync and PRs | All | GitHub via OAuth |
| Offline mode | PWA, local files, sync later | All | AI tasks queue offline |
| Offline autocomplete | Small local model (WebLLM) | Strong devices | Optional |
| Legacy converter | jQuery/Core PHP → React/Laravel | All | — |
| Auto unit tests | Jest / PHPUnit | All | — |
| Mobile app generator | React Native / Flutter apps | All | — |
| Expo QR mobile preview | Test the app on a phone | All | Expo built ourselves (no EAS) |
| Figma import | Turn designs into code | All | OAuth |
| MCP client + server | Connect tools to the AI | All | — |
| VS Code extension + CLI | Use NexaLogicDev from VS Code / terminal | All | — |
| Slack / Discord / Teams | Notices and commands in team chat | All | — |
| Version history + rollback | Snapshot before every AI change, diff, one-click back | All | — |
| Explain mode | Explains every step | All | On by default for Free and Student |
| Low-bandwidth mode | Light IDE for slow internet | All | — |
| Real-time co-editing | Yjs collaboration | Team, Enterprise | — |

### 3. App and site builder modes
Source: blueprint §32.2, §32.4, §32.7; nexalogicdev-modules-wordpress.md; decisions.md:136, :138; memory/areas/nexalogicdev.md:26–27.

| Feature | What it does (one line) | Plans | Rules / limits |
|---|---|---|---|
| Auto Website Builder | Prompt → 5-page site; drag-and-drop canvas (GrapesJS) | All | Export React/Next.js or WP theme |
| Free static sites | username-site.nexalogicdev.app | Free | 1 new/day, 5 live, offline after 90 days with no visitors |
| Wireframe Generator | Wireframe first, approve, then full build | All | Heavy build on Pro/Team |
| WordPress Builder Mode | Plugin, theme and template generators | Paid | Playground test, compatibility and security scan; PHP is GPL |
| Auto-Architect modules | Business software (Accounting, HR, Inventory…) from a consultant chat | All paid (buy per module) | Size check, price lock, no silent extra charge |
| Scope change rule | Bigger scope → pay difference or trim; smaller → refund difference | Auto-Architect | No wallet |
| 14-day free bug fixes | After delivery | Auto-Architect | Build fails tests → full refund |
| Modules connect | e.g. Inventory ↔ Accounting | Auto-Architect | — |
| Team monthly module | One module included a month | Team | Lapses; reminder day 20 |
| Previews (Sandpack) | Instant front-end preview in browser | All | — |
| PHP / WordPress preview | php-wasm / WordPress Playground in browser | All | GPL notice published |
| Power mode | Full Node.js, backend, DB on our sandbox (gVisor/Kata) | Team, agencies, Auto-Architect buyers | Stops after 30 min idle (default, editable); no StackBlitz |
| Facebook Page → Website | Builds a site from the business's Page | All | Official Meta API, owner consent; WhatsApp order button |
| Bangladeshi templates | Shop, coaching, school, pharmacy, restaurant, real estate | All | Correct Bangla fonts |
| Festival templates | Eid, Pohela Boishakh, Victory Day, Black Friday | All | — |
| Remix Gallery | Remix public sites/templates | All | Creator gets XP + badge (no NexaCoins); sales via marketplace |
| BD payment modules | bKash, Nagad, Rocket, SSLCommerz in one click | All | Signed webhooks |
| Global payment modules | Stripe, PayPal, Paddle for client sites | All | Hosted checkout only (PCI SAQ-A style) |
| Mushak 6.3 VAT invoice | In the Accounting module | Auto-Architect | Lawyer checks format |
| BD SMS / OTP gateway | OTP and notices in generated apps | All | — |
| Headless CMS | Payload / Strapi (MIT) | All | — |
| Multi-language / RTL / currency | In client apps | All | — |
| One-click translation | Bangla ↔ English ↔ Arabic | All | — |
| Privacy toolkit | Cookie consent, policy drafts, data deletion in client apps | All | — |
| AI Shop Assistant | Bangla chatbot on the user's site, orders to WhatsApp | Add-on ৳299–699 | Conversation cap; "you are talking to an AI" |
| F-commerce Order Manager | Orders + Pathao/Steadfast/RedX booking, COD reconciliation | All (to confirm plan) | — |
| Freelancer Toolkit | Proposals, quotes, Fiverr/Upwork portfolio, handover docs | All | — |
| Client preview/approval link | Client reviews and approves the build | All | — |
| Bangla README + handover video | Client handover pack | All | Video via Internal Video Service |
| Play Store publishing | PWA/Android build and publishing help | ≈৳999 one-time | Customer's own developer account |

### 4. Code quality and security
Source: unified-credit-governance.md C; nexalogicdev-intl-features.md; decisions.md:143, :153; blueprint §32.3, §36.5.

| Feature | What it does (one line) | Plans | Rules / limits |
|---|---|---|---|
| microVM sandbox | Kata/gVisor isolation, quotas, network policy | All | Accounting/admin data never reachable |
| Visual QA | Playwright visual regression + auto-fix after UI builds | All | — |
| Cross-browser / mobile screenshots | Checks on many screens | All | — |
| DevSecOps scans | OWASP Top 10, secrets, licence scans on generated code | All | GitHub Actions / GitLab CI |
| AI PR review | AI reviews every GitHub pull request | Team | — |
| WCAG 2.2 AA check + auto-fix | axe-core | All | — |
| Lighthouse / Core Web Vitals gate | Speed and quality gate | All | — |
| Playwright E2E tests + coverage | End-to-end tests | All | — |
| SBOM + OSV alerts + signed builds | CycloneDX, OSV, Sigstore | All | OSV data CC-BY attribution |
| Code provenance check | Compares with public GPL code | All | — |
| Dependency-update PRs | Own tool (not Renovate) | All | — |
| Passkeys / MFA / roles in apps | OWASP ASVS baseline in generated apps | All | — |
| Database safety | Separate test/live DB; AI never touches live DB without approval; daily backups | All | — |
| Abuse prevention | Blocks phishing, fake bank/bKash/government pages, scam shops, malware | All | Pre-deploy scan; human decides |
| Acceptable Use Policy | Rules, 24 h takedown, suspension, 7-day appeal | All | DNS can be disabled on abuse |
| AI transparency | AI-commit marker, "why changed", AI history | All | EU AI Act Art. 50 notice |

### 5. Hosting, domains and deploy
Source: decisions.md:143, :146, :153, :159, :200; blueprint §32.7, §32.10; nexalogicdev-intl-features.md.

| Feature | What it does (one line) | Plans | Rules / limits |
|---|---|---|---|
| Nexa Cloud | Managed hosting: DB, auth, storage per app (self-hosted Supabase) | Free–Business tiers | Own OVH SYS-4 servers, USA + EU; order date (to confirm, was Aug 2027) |
| Data residency choice | USA or EU/Netherlands | All | — |
| Point-in-time recovery | PITR backups to R2 | Nexa Cloud | — |
| DB migrations + preview DB branches | Safe schema changes | All | — |
| dev → staging → live | Environments, PR preview links, feature flags, secrets vault | All | — |
| Custom domains | Cloudflare for SaaS, automatic SSL | All | Separate Cloudflare account for client sites (to confirm) |
| Go Live bundles | Buy domain → DNS, SSL, email forwarding, Google submission in 1–2 min | Paid | International TLDs only (Name.com); no .bd |
| DNS change approval | AI proposes; user previews and approves; rollback | All | Audit log |
| Deploy to Vercel/Netlify / ZIP export | One click, or ZIP with Bangla cPanel guide | All | Passwords never stored |
| Export to Docker/Compose/Helm/OpenTofu | Take the app anywhere; no lock-in | All | — |
| Cloudflare WAF / DDoS / rate limits | Protects client sites | All | — |
| App observability | Logs, uptime, GlitchTip errors, status page, WhatsApp/SMS alerts | All | Sentry not used |
| Umami analytics + lead alerts | Visitors and form leads; alerts by WhatsApp/SMS | All | — |
| Local SEO + Google listing | Search Console, sitemap, Bangla keywords | All | — |
| 99.9% uptime SLA | For paid plans (default); RPO/RTO plan | Paid | Conflicts with lending A6000 #3 at NexaTute peak (to confirm) |

### 6. Nexa AI API and chatbots
Source: decisions.md:153–154.

| Feature | What it does (one line) | Plans | Rules / limits |
|---|---|---|---|
| Nexa AI API | Developers put our AI in their own apps | All (Free tests with daily credits) | Nexa rates; Claude/GPT at marked-up rates; Enterprise invoiced |
| Per-app spend cap | Stops at the cap, never overspends | All | Alerts 75% / 90% |
| Rate limits + server-side keys | No keys in browsers | All | — |
| Per-app cost reports | Usage per app | All | — |
| Lowest GPU priority | API waits behind live classes | — | — |
| Safety + AI notice | Content safety and "you are talking to an AI" | All | Customer pays, never end users |
| Public API + Extension SDK | Build on NexaLogicDev | All | — |
| OpenAPI docs + playground + webhooks | For apps users build | All | — |
| Per-project budgets + forecast | Spend forecast per project | All | — |

### 7. Marketplace
Source: nexalogicdev-modules-wordpress.md §2; blueprint §32.8, §32.11; decisions.md:111, :114; crossproduct.md #24.

| Feature | What it does (one line) | Plans | Rules / limits |
|---|---|---|---|
| Shared marketplace | One store for NexaTute, Motion Studio, NexaLogicDev + third-party goods | All | No stored balance |
| Template / code item sales | Sell templates ৳99–4,999, WP packs | Sellers 18+ | 30% commission; 20% Verified Creator (20+ sales, ≥4.5) |
| Seller checks | KYC, build test, licence + security scan, first 3 items human-reviewed | — | — |
| Seller payouts | Monthly to bKash/Nagad/bank | — | Min ৳500, 14-day hold (blueprint) |
| Expert Help | Hire a verified Certified Builder | All | 15% commission |
| Commission per category | 20% default / 30% code / 15% Expert Help | — | (to confirm, audit Q10) |

### 8. Teams, enterprise and governance
Source: unified-credit-governance.md C, F; decisions.md:140, :146; nexalogicdev-intl-features.md.

| Feature | What it does (one line) | Plans | Rules / limits |
|---|---|---|---|
| Team workspaces | Roles Admin / Developer / Viewer | Team, Enterprise | Pooled credits |
| SSO | SAML/OIDC (Okta, Azure AD) via Keycloak | Team, Enterprise | — |
| SIEM export | Audit log to the client's SIEM | Enterprise | — |
| Private VPC deployment | In the client's AWS/GCP | Enterprise | Setup from ৳2,00,000 |
| SOC 2 / ISO 27001 controls | Controls from day one | — | Badges only after audits |
| ISO/IEC 42001 + EU AI Act | One AI management system for all 3 products | — | Certification after audit |
| AI Governance Lead | Owns AI risk; combined with DPO/Security first | — | — |
| Role matrix | Initiator → 2 approvers → audit for prices, refunds, routing | — | — |
| Break-Glass | Emergency safety actions only | — | 2 h access, owner alerted, review in 24 h |
| Trust Center | Security answers, DPA, sub-processors, pen-test summary, VPAT | All | Shared with all 3 products |
| Support + docs | AI first → person; docs, changelog, roadmap voting, Flarum forum | All | SLA Free 72 h → Team 8 business h (blueprint) |

### 9. Learning links (NexaTute)
Source: free-class-links.md; marketing-automation.md; blueprint §32.5; memory/areas/nexalogicdev.md:27.

| Feature | What it does (one line) | Plans | Rules / limits |
|---|---|---|---|
| "Free class" menu | Free 45-min "Build apps and websites with NexaLogicDev" class in NexaTute | All | Shareable certificate |
| "Learn to do this" buttons | Opens the exact NexaTute lesson for a feature | All | "Coming soon — notify me" if none |
| "Try it in NexaLogicDev" | Two-way buttons in NexaTute courses | All | — |
| AI "learn this" hint | When stuck, max once a session | All | — |
| Learn → Build | NexaTute coding learners continue here | Student Plan | — |
| Certified Builder | Certificate for course + real project; Job Board priority | All | Adult check for real jobs |
| Build Notes blog | Automated SEO blog via Marketing Hub | — | Human edit, max 3/week |
| Weekly Bangla Live Build | Live session on LiveKit | — | After Developer Advocate hire |
| Onboarding tutorial | First landing page in 10 minutes | All | Bonus credits lapse like others |

### 10. Sharing and engagement
Source: sharing-and-connectors.md; CLAUDE.md share rule; nexalogicdev-credits-benchmark.md; blueprint §32.6.

| Feature | What it does (one line) | Plans | Rules / limits |
|---|---|---|---|
| Share button | One tap to Facebook, WhatsApp, LinkedIn, Instagram, TikTok, X, copy link, download | All | Preview first; OAuth only |
| "Built with NexaLogicDev" badge | Badge on sites with a showcase page | Free (paid can remove) | Referral link on badge conflicts with "no rewards for sharing" (to confirm) |
| Verify link / QR | On certificates and badges | All | Scores hidden by default |
| Connected accounts | Google and GitHub via OAuth | All | Never passwords |
| Daily Build Challenge + streaks | Small daily task | All | XP/badges only, no money |
| Unfinished-project reminders | "Your site is 80% ready" | All | — |
| Weekly AI site review | SEO, speed, accessibility tips | All | Leads to Care Plan |
| Hackathons | Monthly cash ৳10k/5k/3k; weekly Prompt Battle | All | Credit prizes → free Pro/Hobby month; cash 18+ or guardian |
| XP and badges | One XP system with Nexa ID | All | NexaCoins removed |

### 11. Under-18 rules
Source: decisions.md:206–207, :213; sharing-and-connectors.md; engine-pricing-backend.md.

| Feature | What it does (one line) | Plans | Rules / limits |
|---|---|---|---|
| Guardian approval | Under-18 can use NexaLogicDev with guardian approval | All | Feature limits (to confirm) |
| No purchases by the minor | Guardian pays | — | — |
| No marketplace selling | Minors cannot sell | — | — |
| Public apps/sites after approval | Guardian approves before going public | — | — |
| No outside AI | Under-18 requests never go to GPT, Claude or others | — | Queue when busy; this also means no GPT Codex review step |
| Sharing limits | Certificate/badge only, first name, no face/voice/video | — | — |
| No cash rewards | No referral cash or prize cash without guardian | — | — |

### 12. Admin panel
Source: nexalogicdev-admin.md.

| Feature | What it does (one line) | Plans | Rules / limits |
|---|---|---|---|
| Overview | Live KPIs, alerts, AI Co-Admin, command bar, one-click fixes | Admin | — |
| Accounting & finance | Own book, cost split, VAT/Mushak, aamarPay/Paddle, payouts, engine profit | Admin | — |
| Plans & pricing | Plans, Boost packs, modules, WP packs, Nexa Cloud, Enterprise, USD rule | Admin | — |
| AI Engines & Pricing | Engine table, routing, benchmarks, caps, BYOK | Admin | Price change for new tasks only |
| Users, teams & Enterprise | Workspaces, roles, SSO, private cloud, SIEM | Admin | — |
| Projects, builds & sandboxes | Queues, agents, failures, auto-refunds, Visual QA | Admin | — |
| Nexa Cloud, hosting & domains | Apps, DBs, backups, Go Live, DNS approvals | Admin | — |
| Marketplace & creators | KYC, review, scans, payouts, Remix Gallery | Admin | — |
| Safety & abuse | Scans, reports, 24 h takedowns, AUP cases | Admin | Links to Security & Control Centre |
| Support | AI → email → human, per-purpose emails, SLAs | Admin | — |
| Marketing | Marketing Hub, Build Notes, referrals, hackathons | Admin | Landing Page AI section too |
| Quality & KPIs | Build success, free → paid, churn, NPS, engine pass rates | Admin | — |
| People & approvals | Job assignment, Break-Glass, audit log, AI Governance Lead | Admin | — |
| Settings registry | Legal pages, languages, notifications | Admin | — |
| Cross-product page | Internal Video Service, free-class links, Nexa ID, consent | Admin | — |

### 13. Cross-product
Source: internal-video-service.md; ecosystem-architecture-review.md; decisions.md:176, :199–201; five-gaps-solutions.md; crossproduct.md #41.

| Feature | What it does (one line) | Plans | Rules / limits |
|---|---|---|---|
| One Nexa ID | One login for all 3 products | All | OIDC, passkeys, MFA |
| Motion Studio videos | Promo and handover videos via Internal Video Service | All | Per-order price or plan minutes (no "৳5 = 1 credit") |
| Sites for NexaTute institutions | NexaLogicDev builds institution sites | Contract | Data only via Partner API; price/book (to confirm) |
| Motion Studio videos for those sites | Same service | Contract | — |
| Lab licence linked to NexaTute | Classroom mode, assignments | Licence | Price (to confirm) |
| Remon Growth Logic AI | Shared Marketing Hub + CRM | — | 4th service or module (to confirm) |
| Shared GPU cluster | Priority NexaTute → NexaLogicDev → Motion Studio | — | Valkey, not Redis |
| Data export + deletion | Download all data; delete account with 30-day cancel | All | Warns live sites go offline; gives domain transfer code |
| Shared status page + bug bounty | status.remonlogic.com; security.txt | All | — |
| First-visit language prompt | Country language or English, asked once | All | 10 languages |

---

## Out of date in older documents
- Blueprint §32.1: MiniMax-M2.7 Heavy, RTX PRO 6000 Fast and Claude Sonnet steps. Now GLM-5.2 on 8×A100, Qwen3-Coder-Next / DeepSeek-V4-Flash on A6000 #3, GPT Codex review.
- Blueprint §32.5, §32.9, §33, §0.1: "one wallet", NexaCoins, top-ups valid 180 days, "৳5 = 1 credit". Now Boost packs to end of plan month, XP only, per-order video prices.
- Blueprint §32.9: 1 credit = 1,000 Heavy tokens and the GPU cost per credit figures. Now 2,500 tokens, and costs must be recomputed on the final fleet.
- Blueprint §32.9 and credits-benchmark.md: "lifetime 10% referral" and two-sided bonus credits. Now 10% for 12 months with a cap; discounts instead of credits.
- Blueprint §0.1, §32, §32.12, memory: development Mar 2027, launch Sep 2027. Now Free Beta 15 Apr 2027, paid 6 May 2027.
- Blueprint §32.6, §32.8, §32.12: "later update" items (WordPress Mode, Complex module, Remix Gallery, Shop Assistant…) and "managed hosting later". Now everything is at launch, including Nexa Cloud.
- Blueprint §32.9 and modules-wordpress.md: USD in whole dollars ($28, $111…). Now to the cent ($27.65, $110.64…).
- why-us.md and admin.md say 6 languages; the blueprint said 18+ only. Now 10 languages, and under-18 users are allowed with guardian approval.

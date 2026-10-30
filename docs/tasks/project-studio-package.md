# Task for the next Claude account — Project & Competition Studio package (owner order, 30 Oct 2026)

Status: NOT built yet. The owner said: "do not build it now, leave the instruction on GitHub so the next account can do it."
Read first: `docs/decisions.md` (30 Oct 2026 lines on the Project & Competition Studio) and `docs/memory/areas/nexatute-learning.md`.

## 1. The flow (owner's order — show it like this on the landing page and in the app)
1. Work in the Virtual Lab (steps, data, graphs recorded automatically; the AI asks questions, never gives answers)
2. Report, slides, poster and video
3. Practice with the AI judge
4. A final presentation video of at most 5 minutes (made with Motion Studio)
5. School competition and QR certificate

## 2. New separate package (owner decision)
- Name: "Project Studio Pro" (default name, editable).
- 7 project works per month; each work may have a video of up to 5 minutes.
- Includes everything in the flow above: lab, full report, slides, poster, the video, AI judge practice, competition entry and QR certificate.
- Price: ৳799/month ($12), approved 30 Oct 2026 (see section 5).
- It can be bought on its own or added on top of any plan.

## 3. Limits in the existing paid packages (owner set the lowest; Claude set the rest — default, editable)
"1 work" = one project with its report/slides/poster/video. Unused works do not carry over.

| Package | Project works / month | Max video length | AI judge practice |
|---|---|---|---|
| Free tier / Free Trial | 0 (Virtual Lab + basic report only) | — | — |
| Daily Pass / Co-Teacher Pass | 0 (Virtual Lab + basic report only) | — | — |
| Batch (lowest paid monthly plan) | 1 (owner's number) | 1 min (owner's number) | 1 session per work |
| Combo | 2 (default) | 2 min (default) | 2 sessions per work |
| Personal | 3 (default) | 3 min (default) | 3 sessions per work |
| Project Studio Pro | 7 (owner's number) | 5 min (owner's number) | unlimited (fair use) |
| Institution packages | per seat same as the seat's Batch/Combo plan; competition hosting included | same | same |
| PlayBoom (Play–Class III) | 0 at launch (default) | — | — |

- When several plans are active, the highest limit counts (they do not add up), except Project Studio Pro which adds its 7 works.
- Videos are 720p by default (default, editable); higher quality may be offered later.
- Under-18 rules still apply: guardian consent for any public showcase, first name only, face optional, own voice only with guardian approval (otherwise library voice).

## 4. Where to put it
- Landing page: its own highlighted section with the 5-step flow above and the package table (free part vs paid part); samples labelled "sample (prototype)"; 6 languages.
- Pricing page/plan cards: the new package + the per-plan limits.
- Learner app: a Project Studio area; a counter "N of M works left this month".
- Admin panel: every number in this file (works per month, video minutes, AI judge sessions, video quality, package price, on/off per plan) is editable, marked "(default)", changed with two-person approval and logged.
- Institution admin (X12): competition hosting (topic, rules, deadlines, rubric, online judging, results, QR certificates).
- Then add it to the Master Blueprint at the next build (v32.11) and to `prototype/shared/numbers.md`.
- Check board sizes (≤ 1.8 MB) — X20/X12 are near the limit; use a new board if needed.

## 5. Team option (owner decision, 30 Oct 2026)
- "Project Studio Team" (default name, editable): up to 15 people work together in one team; different students may be on different projects inside the same team.
- Approved by the owner 30 Oct 2026: shared pool of 21 works a month (3 × the single package), video up to 5 min each; one member can be on several projects; a project can have 1–15 members; roles = team leader, members, teacher/mentor; AI judge practice per member (fair use); one competition entry per project.
- Under-18 members: guardian consent each; the team needs an adult teacher/mentor; team chat moderated by Nexa Guard; members join only by invitation from the teacher/leader of the same institution or class.
- Prices approved by the owner 30 Oct 2026 (re-check the margin after the GPU benchmark; GPU cost per video minute is not measured yet): Project Studio Pro ৳799/month ($12); Project Studio Team ৳3,999/month ($60, ≈ ৳267 per member). Videos made in Quick/Enhanced mode at 720p to keep GPU cost low.

## 6. Storage for project videos (approved by the owner 30 Oct 2026; all values admin-editable)
- Students have no Motion Studio account; Motion Studio is only the engine behind the scenes. Finished files are saved in the student's NexaTute storage, in a "My Projects" folder inside Project Studio, with the storage meter.
- Proposed: Project Studio Pro +5 GB; Project Studio Team 30 GB shared; drafts auto-deleted after 30 days (final kept); competition entries copied to the institution's pooled storage until results; usual 30-day keep after a plan ends; download any time.

## 7. Communication (approved by the owner 30 Oct 2026; all values admin-editable)
- One "Project Room" per project (members see only their projects) + a "Team Lobby" for the whole team.
- Members: text chat (text, images, files, threads per task, @mentions, Nexa Guard on every message); task board (to do / doing / done, owner per task); comments pinned to report lines, slides, poster and video seconds; voice huddle from the room (camera off by default, never recorded, ends after 60 min).
- AI co-ordinator "Nexa Project Coordinator" (default name) in every room: @Coordinator or voice, 6 languages; makes the plan and timeline, proposes task split, deadline reminders, gentle nudges, discussion/meeting summaries (decisions + open tasks), asks guiding questions but never gives answers, contribution log for fair credit, sets out both sides in disagreements (team/teacher decides). Pro (single) works with the coordinator alone and can invite own teacher to review.
- Under-18: no private member-to-member messages; teacher/mentor sees all; voice huddle only with an adult mentor in the call; first names only, no phone numbers/contacts; guardian gets a weekly summary (not the messages); the usual behaviour ladder.
- Chats kept 180 days after the project ends, then deleted. Included in the price; coordinator runs on the Co-Teacher LLM (no new GPU).

## 8. Personal KPI, AI advice and data sync (owner decision 30 Oct 2026; KPI list = Claude proposal awaiting approval)
- Owner decision: Project Studio has a personal KPI and AI advice; Nexa Teacher, Nexa Co-Teacher and Nexa Project Coordinator sync through the one shared learner record, so each knows where a student is weak and what to teach; this appears in all dashboard reports for every student who has any package.
- Approved 30 Oct 2026 (all admin-editable):
  - Personal KPIs (each student sees only their own): science skills from the Virtual Lab log (hypothesis, variable control, data accuracy, graphs, conclusion fits data); presentation (AI judge: time, clarity, accuracy, confidence, improvement per attempt); report quality by rubric; originality and AI-help level; teamwork (own tasks done, on time, help given); competitions (entries, results, certificates); syllabus topics used and mastery change.
  - AI advice after each work and weekly, with reason/evidence and a direct button (Co-Teacher lesson, next Nexa Teacher class, AI judge practice); "needs more practice", never "weak".
  - Sync: Coordinator writes lab mistakes, unclear concepts, presentation gaps and contribution to the shared learner record; Nexa Teacher teaches those concepts first in the next 1:1/batch recap; Co-Teacher gives drills; Coordinator reads mastery to split tasks (within reach + a stretch); linked to MindForge problem-solving/creative skills.
  - Shown in: Main Student Dashboard "Projects" section (KPIs + timeline), class reports, guardian weekly summary, teacher/mentor sees own team, institution counts only with consent (hidden under 5), final work and certificates in the learner passport.
  - No member sees another's personal KPI; no ranking.

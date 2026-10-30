# Task for the next Claude account — "School Homework" section (approved by the owner 30 Oct 2026)

Status: NOT built yet. Add to the NexaTute prototype (Main Student Dashboard X18/D01, guardian X08, Institute admin X12, platform admin) and to the next blueprint (v32.11). All values admin-editable, marked "(default)", two-person approval, logged.

## Purpose
A separate "School Homework" (bn: স্কুলের হোমওয়ার্ক) section on the student dashboard in every student package, so student, guardian, school teacher and institution can see what the student learned outside the NexaTute syllabus and its KPIs.

## How homework comes in
- Student photographs the homework / school diary page, or types it; partner-school teachers can assign it directly from X12.
- AI (Qwen3-VL on our GPU) reads it and fills subject, topic and due date.

## Help
- AI gives step-by-step hints and guiding questions only; the student writes the answer; AI checks it afterwards; mistakes go to the Error Notebook.
- Topics outside the NexaTute syllabus are tagged "Beyond NexaTute syllabus"; AI makes a short lesson for it, labelled "AI-generated" until a teacher/admin verifies it.

## KPIs + AI advice
- Homework done on time %, done alone vs with hints, accuracy after checking, time per homework, repeated mistakes, list of beyond-syllabus topics learned with mastery change; AI advice with reasons/evidence (no "weak" labels).

## Who sees what
| Who | Sees |
|---|---|
| Student | everything |
| Guardian | weekly summary, topic list, KPIs |
| School teacher | own class summary; an individual student's details only with guardian consent |
| Institution | counts only, hidden under 5 |

## Sync
- Where the student gets stuck goes to the shared learner record; Nexa Teacher covers it in the next class, Co-Teacher gives practice, Project Coordinator can use it.

## Daily homework-help limits (default, editable)
| Package | Per day |
|---|---|
| Free | 1 |
| Daily Pass | 3 |
| Batch | 5 |
| Combo | 10 |
| Personal | unlimited (fair use) |

Included in all package prices (no extra charge).

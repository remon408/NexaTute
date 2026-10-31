# For the OLD Claude account — update your NexaTute Design canvas from GitHub

Owner order, 31 Oct 2026: the new Claude account builds the prototype changes and keeps them in this repo. The old account (which owns the NexaTute Design canvas, artifact Version 156) publishes the updated boards to its canvas. The new account cannot publish into the old account's canvas.

## When to do it
Only after `docs/STATUS.md` has a line saying **"Boards ready for the old canvas — <date>, commit <hash>"**. Until then the boards in `prototype/project/` may be half-way through a change. Reply to the owner in Bengali.

## What to do
1. Pull this repo (`remon408/nexatute`, branch `main`) at the commit named in STATUS.md.
2. Read `CLAUDE.md`, `docs/HANDOVER.md` and the newest lines of `docs/decisions.md` first.
3. Read your canvas's `project/canvas.json` and compare it with `prototype/project/canvas.json` in the repo. The repo version is the source of truth for the board list, layout, titles and pages (new split boards such as `X14b-…`, `X20b-…` are added there).
4. Publish to YOUR existing canvas (its `url`, never a new canvas) every changed or new `.dc.html` from `prototype/project/` at `project/<same file name>`, and `project/canvas.json` from the repo. Keep within the type's limits (16 MB per call — send in several calls; `canvas.json` last). Boards that were removed in the repo are removed from the canvas too (the changes list in STATUS.md names them).
5. If the owner edited a board by hand in the canvas after Version 156, the publish is refused for that file: tell the owner which file, and do not overwrite his edit without asking.
6. Do not change board content yourself. Report any problem in this repo (`docs/STATUS.md`) and to the owner.
7. After publishing, tell the owner the new version number and add a line to `docs/STATUS.md`: "Old canvas updated to <commit> — Version <n>, <date>".

## What NOT to do
- Do not create a new canvas.
- Do not publish `prototype/netlify-build/` or tool files — only `prototype/project/*.dc.html` and `canvas.json`.
- `./support.js` in each board is supplied by the canvas itself; there is no such file in the repo.

The Netlify zip (static site) is built and handed to the owner by the new account; the owner can upload it from any account.

# AGENTS.md — Projekt SAMOZAMYKACZ (aplikacja aktywności fizycznej)

## What this project is
University lab project by team **SAMOZAMYKACZ**: a responsive (mobile-first) web app for logging
physical activity and showing charts per exercise type. Current phase: **documentation and planning**
(informal SRS + WBS with Delphi estimates). Implementation has not started.

All project documents are written in **Polish**. Keep writing them in Polish unless asked otherwise.
The user prefers **concise, factual content** ("nie rozwijaj zbytnio, rzeczowo i konkretnie") and
wants template questions answered **directly** (bullet question → direct answer under it).

## Fixed decisions (from the lecturer's requirements, "SIWZ")
- Backend: **PHP 8.2+ / Symfony**, ORM **Doctrine** (mandatory; the lab is about a PHP backend).
- Frontend: **Next.js (SPA, TypeScript)** talking to a Symfony **REST API** (API Platform). Decided.
- Mobile-first responsive UI; public part + closed (logged-in) part.
- RODO/GDPR: privacy policy page, cookie consent, data stored in the EU.
- Data model minimum: *zmienna* (exercise type) → *obserwacje* (date + value at minimum).
- Charts must support zoom and pan left/right.
- Theme: sport (agreed for the whole lab group). Tech outside the list → ask the lecturer on Teams.

- Database: **SQLite** via Doctrine ORM + Doctrine Migrations (per SRS 2.3).

## User classes (final)
- **UŻ-1** Użytkownik niezalogowany — public pages only (home, privacy policy, register, log in).
- **UŻ-2** Użytkownik zarejestrowany — logs activities, charts, history (filter/sort), summaries,
  training goals, own exercise types, account settings. Sees only own data.
- **No administrator and no trainer/coach role** — both removed by the user. Do not reintroduce them.
- No password-reset e-mails (SRS IK-5); only activation e-mails via SMTP.
- Data is entered **manually** (no automatic sensor/device sync — it's a web app).

## UI (as described by the user)
Bottom ribbon with 3 buttons: **Menu główne (Home)**, **Mierzenie aktywności (Record)**, **O mnie**.
- Home: chart of the user's favourite activity for the day (scrollable); swipeable cards
  (other charts / stats, configurable order); below: activity history with short summary.
- Record: form to enter exercise data.
- O mnie: summary for a period (default: month), training goals with progress, user panel (incl. logout).
- Also a "Szczegóły aktywności" (activity details) screen: view / edit / delete.
- History list sortable by **date, steps, burned calories**; activity has optional `kroki`, `spalone kalorie`.

## Repo docs
- The user's master copies live **outside the repo**, one level up:
  `../SRS-SAMOZAMYKACZ_2026.docx` and `../WBS_SAMOZAMYKACZ_2026.xlsx`. They win over repo copies.
  When the user says they were updated, re-read them and sync the files below.
- `docs/SRS.md` — Markdown mirror of the SRS .docx (sections 1–8, UI-x, IP/IS/IK, WN, WIL, glossary proposal).
- `docs/WBS.md` — WBS layout, per-person totals, version history.
- `docs/estimates/WBS_SAMOZAMYKACZ_2026.xlsx` — repo copy of the WBS, **same name as the master file**.
  Replace it in place on every update; git keeps history. Never add version suffixes (`_2`, `_3`…).
- `docs/OPEN_ISSUES.md` — unresolved questions and known inconsistencies. Check before editing docs.
- Reading the files: no pandoc/python-docx/openpyxl system-wide — parse .docx XML with `zipfile`,
  and use openpyxl from a throwaway venv.

## Working with the WBS spreadsheet
- Sheet `WBS`: tree levels in columns **B–E** (B = top level), A = milestones, H = assignee (empty),
  J = template labels, **K = Patryk Woźnicki (PW), L = Gracjan Grzeszczak, M = Paweł Ewald,
  N = Michał Marcinkowski**, O = group discussion (not filled).
- Row 3 "Makiety (4h)" covers all mockups. Hours only on leaf tasks. Sum row **258** (`=SUM(K3:K257)`).
- **Estimation is closed** — lecturer's note in O3 says not to fill it any more. Don't add hours.
- The user restructures the sheet between versions: always re-read it and never touch cells
  the user said to leave. Use openpyxl; keep the user's layout.

## Git conventions
- Remote: `origin` → `https://github.com/PeWuPL/AI-Fitness-Tracker.git`.
- Branch name: `<INITIALS>_<TYPE>_<description>`, e.g. `PW_FT_activity-form`, `PW_BF_chart-zoom`,
  `PW_DOC_srs-wbs-planning`. TYPE: `FT` feature, `BF` bugfix, `DOC` docs, `REF` refactor,
  `CH` chore/config, `TST` tests. Description in kebab-case. Initials of the author (e.g. PW).
- Commit messages: **Conventional Commits** (`feat:`, `fix:`, `docs:`, `refactor:`, `chore:`,
  `test:`, optional scope, e.g. `docs(srs): add sorting requirements`).
- Don't commit directly to `main`; push the branch and merge via PR.

## Status / where we left off
- SRS .docx has sections 1–7 filled (functional reqs 3.1–3.12, UI-1…UI-13, interfaces, quality, i18n);
  still empty: 1.4, 4.1 data model, 8, glossary (Suplement A), Suplement B.
- WBS: estimates from all four members — PW 74 h, GG 53 h, PE 126.5 h, MM 158 h. Closed.
- Repo WBS has extra sheets: `WBS (czysty)` (no red/struck rows), `Backend` and `Frontend`
  (work packages `B-x.y`/`F-x.y` under shared milestones M1–M7; column H free for assignees).
  See `docs/WBS.md`. The original `WBS` sheet stays untouched.
- Don't edit the .docx/.xlsx master copies unless asked; the user fixes typos in the .docx themselves.
- Next likely steps: resolve `docs/OPEN_ISSUES.md`, assign tasks (column H), milestone dates,
  data model (ERD), mockups, then scaffold the Symfony + Next.js repos.

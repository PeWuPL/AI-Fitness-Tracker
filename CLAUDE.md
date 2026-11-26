# CLAUDE.md — Projekt SAMOZAMYKACZ (aplikacja aktywności fizycznej)

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

## User classes (final)
- **UŻ-1** Użytkownik główny — logs activities, views charts/history/summaries.
- **UŻ-2** Gość — unauthenticated, public pages only.
- **UŻ-3** Administrator — account management, default exercise types.
- **No trainer/coach role** — explicitly removed by the user. Do not reintroduce it.
- Data is entered **manually** (no automatic sensor/device sync — it's a web app).

## UI (as described by the user)
Bottom ribbon with 3 buttons: **Menu główne (Home)**, **Mierzenie aktywności (Record)**, **O mnie**.
- Home: chart of the user's favourite activity for the day (scrollable); swipeable cards
  (other charts / stats, configurable order); below: activity history with short summary.
- Record: form to enter exercise data.
- O mnie: summary for a period (default: month) + user panel (incl. logout).
- Also a "Szczegóły aktywności" (activity details) screen: view / edit / delete.
- History list sortable by **date, steps, burned calories**; activity has optional `kroki`, `spalone kalorie`.

## Repo docs
- `docs/SRS.md` — consolidated informal SRS (sections 2.2–2.5, 3.1–3.12, glossary). Source of truth for requirements.
- `docs/WBS.md` — WBS structure summary, Delphi estimation method and current numbers.
- `docs/estimates/WBS_SAMOZAMYKACZ_2026_2.xlsx` — latest WBS spreadsheet (the user edits it in Excel).
- `docs/OPEN_ISSUES.md` — unresolved questions and known inconsistencies. Check before editing docs.

## Working with the WBS spreadsheet
- Sheet `WBS`: tree levels in columns **B–E** (B = top level), A = milestones, H = assignee,
  J–N = Delphi individual estimates per person, O = hours after group discussion.
- Column **J = person "PW"** (header cell still says "Imię i Nazwisko"; user fills names).
- Hours go **only on leaf tasks** (no children) to avoid double counting. Sum row at **287**
  (`=SUM(J3:J255)` etc.). Note in row 289 explains the AI-assisted reduction factors.
- The user restructures the sheet between versions: always re-read it, map hours by task
  name + section context (e.g. "Makiety" vs "Frontend" duplicates), and never touch cells
  the user said to leave. Don't overwrite the user's template labels (J1:O9 area) without asking.
- Use openpyxl; keep the user's layout; verify with a formula recalculation after edits.

## Git conventions
- Remote: `origin` → `https://github.com/PeWuPL/AI-Fitness-Tracker.git`.
- Branch name: `<INITIALS>_<TYPE>_<description>`, e.g. `PW_FT_activity-form`, `PW_BF_chart-zoom`,
  `PW_DOC_srs-wbs-planning`. TYPE: `FT` feature, `BF` bugfix, `DOC` docs, `REF` refactor,
  `CH` chore/config, `TST` tests. Description in kebab-case. Initials of the author (e.g. PW).
- Commit messages: **Conventional Commits** (`feat:`, `fix:`, `docs:`, `refactor:`, `chore:`,
  `test:`, optional scope, e.g. `docs(srs): add sorting requirements`).
- Don't commit directly to `main`; push the branch and merge via PR.

## Status / where we left off
- SRS sections 2.2–2.5, 3 (with 3.x.1 Opis + 3.x.2 Wymagania funkcjonalne), accessibility (3.12),
  sorting and glossary are drafted (see `docs/SRS.md`).
- WBS v2026_2 has PW's Delphi hours, reduced for AI-assisted coding: **194.5 h** total
  (was 339.5 h before the reduction).
- Next likely steps: resolve `docs/OPEN_ISSUES.md`, collect other members' estimates (K–N),
  group-discussion column O, milestone dates, then scaffold the Symfony + Next.js repos.

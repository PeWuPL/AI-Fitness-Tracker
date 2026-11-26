# AGENTS.md — Projekt SAMOZAMYKACZ (aplikacja aktywności fizycznej)

## What this project is
University lab project by team **SAMOZAMYKACZ**: a responsive (mobile-first) web app for logging
physical activity and showing charts per exercise type. Current phase: **documentation and planning**
(informal SRS + WBS with Delphi estimates). Implementation has not started.

All project documents are written in **Polish**. Keep writing them in Polish unless asked otherwise.
The user prefers **concise, factual content** ("nie rozwijaj zbytnio, rzeczowo i konkretnie") and
wants template questions answered **directly** (bullet question → direct answer under it).

## Fixed decisions
From the lecturer's requirements ("SIWZ"):
- Backend: **PHP 8.2+ / Symfony**, ORM **Doctrine** (mandatory; the lab is about a PHP backend).
- Frontend: **Next.js (SPA, TypeScript)** talking to a Symfony **REST API** (API Platform).
- Mobile-first responsive UI; public part + closed (logged-in) part.
- RODO/GDPR: privacy policy page, cookie consent. (SRS OG-5 also says "data stored in the EU" —
  unclear for a local project, see `docs/OPEN_ISSUES.md` item 8.)
- Data model minimum: *zmienna* (exercise type) → *obserwacje* (date + value at minimum).
- Charts must support zoom and pan left/right.
- Theme: sport (agreed for the whole lab group). Tech outside the list → ask the lecturer on Teams.

Team decisions:
- Database: **SQLite** via Doctrine ORM + Doctrine Migrations (SRS 2.3).
- **Local project, no deployment** (2026-11-26): no deploy/CI/CD work, no e-mails/SMTP at all.
  Out of scope: activation e-mail (WF-1.2), password change (WF-10.2), account deletion (WF-10.5),
  password reset. The .docx still lists some of these; `docs/SRS.md` shows them struck through.
  HTTPS (IK-1) and the `Secure` cookie flag (IK-3) are open questions for local use (OPEN_ISSUES item 8).
- Data is entered **manually** (no sensor/device sync).

## User classes (final)
- **UŻ-1** Użytkownik niezalogowany — public pages only (home, privacy policy, register, log in).
- **UŻ-2** Użytkownik zarejestrowany — logs activities, charts, history (filter/sort), summaries,
  training goals, own exercise types, profile, logout. Sees only own data.
- **No administrator and no trainer/coach role** — both removed by the user. Do not reintroduce them.

## UI (as described by the user)
Bottom ribbon with 3 buttons: **Menu główne (Home)**, **Mierzenie aktywności (Record)**, **O mnie**.
- Home: chart of the user's favourite activity for the day (scrollable); swipeable cards
  (other charts / stats, configurable order); below: activity history with short summary.
- Record: form to enter exercise data.
- O mnie: summary for a period (default: month), training goals with progress, user panel (incl. logout).
- Also a "Szczegóły aktywności" (activity details) screen: view / edit / delete.
- History list sortable by **date, steps, burned calories**; activity has optional `kroki`, `spalone kalorie`.
- Not every SRS feature has work in the WBS packages yet (e.g. training goals, stats card, card
  configuration, high-contrast mode) — pending team decision, `docs/OPEN_ISSUES.md` item 5.

## Repo docs
- SRS master lives **outside the repo**: `../SRS-SAMOZAMYKACZ_2026.docx` (wins over `docs/SRS.md`).
  Don't edit it unless asked; the user fixes typos in the .docx themselves.
- WBS master is **the repo file** `docs/estimates/WBS_SAMOZAMYKACZ_2026.xlsx` since 2026-11-26 — the team
  edits it directly (assignments, estimate changes). `../WBS_SAMOZAMYKACZ_2026.xlsx` is **outdated**.
- `docs/SRS.md` — Markdown mirror of the SRS .docx (sections 1–8, UI-x, IP/IS/IK, WN, WIL, glossary proposal),
  plus struck-through out-of-scope items. When the .docx changes, re-read it and update the mirror.
- `docs/WBS.md` — sheets, milestones, package table, hour totals, version history.
- `docs/estimates/WBS_SAMOZAMYKACZ_2026.xlsx` — `WBS` sheet + 3 derived sheets with the team's assignments.
  Keep this one file name; git keeps history. No version suffixes (`_2`, `_3`…).
- `docs/OPEN_ISSUES.md` — unresolved questions and known inconsistencies. Check before editing docs.
- `tools/wbs_build.py` — first-time generator of the derived sheets. **Do not run it on the current file** (see below).
- Reading the files: no pandoc/python-docx/openpyxl system-wide — parse .docx XML with `zipfile`,
  and use openpyxl from a throwaway venv (`pip install -r tools/requirements.txt`).

## Working with the WBS spreadsheet
Sheets in the repo file:
| Sheet | What it is |
|---|---|
| `WBS` | The team's sheet: task tree and estimates. |
| `WBS - Czysty` | `WBS` without red and struck-through tasks (and branches left empty). |
| `Backend` / `Frontend` | **Work packages with assignments** (who does what). |

- **Colour code in `WBS`:** red (`FFFF0000`) or struck-through task = **out of scope / dropped**;
  it never goes into the packages, even if it has hours.
- Sheet `WBS` layout: tree levels in columns **B–E** (B = top level), A = milestones,
  J = template labels, **K = Patryk Woźnicki (PW), L = Gracjan Grzeszczak, M = Paweł Ewald,
  N = Michał Marcinkowski**, O = group discussion (not filled; O3 = lecturer's note).
  Row 3 "Makiety (4h)" covers all mockups. Sum row **258** (`=SUM(K3:K257)`).
- `Backend` / `Frontend` layout: A = shared milestone **M1–M7**, B = package `B-x.y` / `F-x.y`,
  C = task (original name), **J = assignee** (PW / GG / PE / MM) per task, K–N = hours,
  G4:H8 = team's `COUNTIF` summary of tasks per person. A package = one side × one feature × one
  milestone; assignment is per task, so a package may have several people (e.g. F-2.1).
  Repo/structure/README live in package `B-1.1 Wspólne`. Frontend styling: **Bootstrap** (not Tailwind).
- Hours only on tasks (leaves); packages and branches have no subtotals.
- **Estimation is closed** — lecturer's note in O3 says not to fill it any more. Don't add hours.
- **Derived sheets copy hours from `WBS`.** If hours in `WBS` change, update K–N in `WBS - Czysty`,
  `Backend` and `Frontend` in place (match rows by task name; disambiguate duplicates such as
  "walidacja danych" by branch). Touch nothing else — J, G4:H8 and labels are the team's.
  Then check Backend + Frontend totals = `WBS - Czysty`, and `WBS - Czysty` = `WBS` minus red rows.
- **Never run `tools/wbs_build.py` on the current file, and never copy `../WBS_SAMOZAMYKACZ_2026.xlsx`
  over it** — both would erase the assignments, the estimate corrections and the sheet rename.
  Back up the file before any scripted edit.

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
  still empty: 1.4, 4.1 data model, 8, glossary (Suplement A), Suplement B. Out-of-scope items still to
  be removed from the .docx (OPEN_ISSUES item 7).
- WBS estimates (closed; PE and MM corrected 2026-11-26): `WBS` PW 74 / GG 53 / PE 93 / MM 86.5 h;
  `WBS - Czysty` 73 / 53 / 92.5 / 86.5 h. Assignments done in column J; a few tasks still unassigned (OPEN_ISSUES).
- Next likely steps: resolve `docs/OPEN_ISSUES.md` (esp. item 5), assign the remaining tasks (column J),
  milestone dates, data model (ERD), mockups, then scaffold the Symfony + Next.js repos.

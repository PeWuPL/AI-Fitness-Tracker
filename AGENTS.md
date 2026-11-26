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
- The user's master copies live **outside the repo**, one level up:
  `../SRS-SAMOZAMYKACZ_2026.docx` and `../WBS_SAMOZAMYKACZ_2026.xlsx`. They win over repo copies.
  Don't edit them unless asked; the user fixes typos in the .docx themselves.
- `docs/SRS.md` — Markdown mirror of the SRS .docx (sections 1–8, UI-x, IP/IS/IK, WN, WIL, glossary proposal),
  plus struck-through out-of-scope items. When the .docx changes, re-read it and update the mirror.
- `docs/WBS.md` — sheets, milestones, package table, hour totals, version history.
- `docs/estimates/WBS_SAMOZAMYKACZ_2026.xlsx` — **not a plain copy**: master `WBS` sheet + 3 generated
  sheets. Same file name as the master; replace in place, git keeps history. No version suffixes (`_2`, `_3`…).
- `docs/OPEN_ISSUES.md` — unresolved questions and known inconsistencies. Check before editing docs.
- `tools/wbs_build.py` — regenerates the derived WBS sheets (see below).
- Reading the files: no pandoc/python-docx/openpyxl system-wide — parse .docx XML with `zipfile`,
  and use openpyxl from a throwaway venv (`pip install -r tools/requirements.txt`).

## Working with the WBS spreadsheet
Sheets in the repo file:
| Sheet | What it is |
|---|---|
| `WBS` | The team's master sheet, copied unchanged. |
| `WBS (czysty)` | `WBS` without red and struck-through tasks (and branches left empty). |
| `Backend` / `Frontend` | **Work packages to assign people from.** |

- **Colour code in `WBS`:** red (`FFFF0000`) or struck-through task = **out of scope / dropped**;
  it never goes into the packages, even if it has hours.
- Sheet `WBS` layout: tree levels in columns **B–E** (B = top level), A = milestones, H = assignee (empty),
  J = template labels, **K = Patryk Woźnicki (PW), L = Gracjan Grzeszczak, M = Paweł Ewald,
  N = Michał Marcinkowski**, O = group discussion (not filled; O3 = lecturer's note).
  Row 3 "Makiety (4h)" covers all mockups. Sum row **258** (`=SUM(K3:K257)`).
- `Backend` / `Frontend` layout: A = shared milestone **M1–M7**, B = package `B-x.y` / `F-x.y`,
  C = task (original name, hours K–N), H = who. A package = one side × one feature × one milestone,
  sized for one person (≈2–7 h average). Repo/structure/README live in package `B-1.1 Wspólne`.
- Hours only on tasks (leaves); packages and branches have no subtotals.
- **Estimation is closed** — lecturer's note in O3 says not to fill it any more. Don't add hours.
- **Updating after the user changes the master file** — never just copy it over the repo file (that
  drops the generated sheets). Instead run:
  `python tools/wbs_build.py ../WBS_SAMOZAMYKACZ_2026.xlsx docs/estimates/WBS_SAMOZAMYKACZ_2026.xlsx`
  If task or branch names changed, the script stops on an assertion — update `MILESTONES` / `PLAN`
  in the script, then re-run. Check that Backend + Frontend totals equal `WBS (czysty)`.

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
- WBS estimates (closed): `WBS` PW 74 / GG 53 / PE 126.5 / MM 158 h; `WBS (czysty)` 73 / 53 / 126 / 158 h.
- Next likely steps: resolve `docs/OPEN_ISSUES.md` (esp. item 5), assign packages (column H),
  milestone dates, data model (ERD), mockups, then scaffold the Symfony + Next.js repos.

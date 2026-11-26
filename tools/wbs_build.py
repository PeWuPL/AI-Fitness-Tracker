"""Generuje arkusze pochodne WBS.

Użycie (z katalogu repo, openpyxl w venv):
    python tools/wbs_build.py ../WBS_SAMOZAMYKACZ_2026.xlsx docs/estimates/WBS_SAMOZAMYKACZ_2026.xlsx

Wejście: plik główny zespołu (arkusz `WBS`). Wyjście: ten sam plik + arkusze
`WBS (czysty)`, `Backend`, `Frontend`. Arkusz `WBS` jest kopiowany bez zmian.

Etap 1 (`build`):
  - `WBS (czysty)`: usuwa zadania czerwone (FFFF0000) oraz przekreślone bez godzin,
    a potem gałęzie, które zostały bez dzieci. Kolumna O (notatka prowadzącego) pomijana.
  - podział na backend / frontend według etykiet gałęzi (SIDE_LABEL, SIDE_TOP, WSPOLNE)
    i kamienie M1–M7 (MILESTONES).
Etap 2 (`reorg`): przebudowuje `Backend` / `Frontend` w pakiety pracy według PLAN.

Jeśli zespół zmieni nazwy zadań lub gałęzi w arkuszu `WBS`, skrypt zatrzyma się na
asercji — wtedy trzeba poprawić MILESTONES / PLAN. Godziny dopisuje się tylko w pliku głównym.
"""
import sys, copy
from collections import Counter
import openpyxl
from openpyxl.styles import Font


def build(SRC, DST):
    wb = openpyxl.load_workbook(SRC)
    ws = wb['WBS']
    LV = 'BCDE'; HC = 'KLMN'; FIRST, LAST = 3, 257

    def task(r):
        for i, c in enumerate(LV):
            if ws[f'{c}{r}'].value not in (None, ''): return i, ws[f'{c}{r}']
        return None, None
    def hours(r): return [ws[f'{c}{r}'].value for c in HC]
    def has_h(r): return any(isinstance(v, (int, float)) for v in hours(r))
    def red(cell): return cell.font.color is not None and cell.font.color.type == 'rgb' and cell.font.color.rgb == 'FFFF0000'

    rows = []
    for r in range(FIRST, LAST + 1):
        lvl, cell = task(r)
        if cell is not None: rows.append((r, lvl, cell))
    # tree
    parent, children = {}, {r: [] for r, _, _ in rows}
    stack = []
    for r, lvl, _ in rows:
        while stack and stack[-1][1] >= lvl: stack.pop()
        parent[r] = stack[-1][0] if stack else None
        if parent[r]: children[parent[r]].append(r)
        stack.append((r, lvl))
    info = {r: (lvl, cell) for r, lvl, cell in rows}

    removed = set()
    for r, lvl, cell in rows:
        if not children[r] and (red(cell) or (cell.font.strike and not has_h(r))): removed.add(r)
    changed = True
    while changed:
        changed = False
        for r, _, _ in rows:
            if r not in removed and children[r] and all(c in removed for c in children[r]):
                removed.add(r); changed = True
    kept = [r for r, _, _ in rows if r not in removed]
    warn_struck_parent = [r for r in kept if children[r] and (info[r][1].font.strike)]
    red_with_hours = [r for r in kept if red(info[r][1]) or info[r][1].font.strike]
    hourless_leaves = [r for r in kept if not children[r] and not has_h(r)]

    # ---------- helpers to write rows ----------
    def copy_cell(src, dst, value=None):
        dst.value = src.value if value is None else value
        if src.has_style:
            f = copy.copy(src.font)
            if red(src): f = Font(name=f.name, size=f.size, bold=f.bold, italic=f.italic, underline=f.underline, strike=f.strike)
            dst.font = f; dst.fill = copy.copy(src.fill); dst.border = copy.copy(src.border)
            dst.alignment = copy.copy(src.alignment); dst.number_format = src.number_format
    def new_sheet(name):
        s = wb.create_sheet(name)
        for k, d in ws.column_dimensions.items(): s.column_dimensions[k].width = d.width
        return s
    COLS = 'ABCDEFGHIJKLMNO'
    def copy_row(s, r_src, r_dst, skip_a=False):
        for c in COLS:
            if skip_a and c == 'A': continue
            if c == 'O' and r_src > 2: continue  # notatka prowadzącego (O3) zostaje tylko w oryginale
            copy_cell(ws[f'{c}{r_src}'], s[f'{c}{r_dst}'])
    def sum_row(s, first, last, at):
        copy_cell(ws['J258'], s[f'J{at}'])
        for c in HC: copy_cell(ws[f'{c}258'], s[f'{c}{at}'], f'=SUM({c}{first}:{c}{last})')

    # ---------- clean sheet ----------
    cs = new_sheet('WBS (czysty)')
    for r in (1, 2): copy_row(cs, r, r)
    out = 3
    for r in range(FIRST, LAST + 1):
        if r in info and r in removed: continue
        if r not in info and not any(ws[f'{c}{r}'].value is not None for c in COLS): continue
        copy_row(cs, r, out); out += 1
    clean_last = out - 1
    sum_row(cs, 3, clean_last, clean_last + 1)

    # ---------- split ----------
    SIDE_LABEL = {  # C-level (or deeper) labels -> side
     'Backend (Symfony)': 'B', 'Model danych': 'B', 'API': 'B', 'Bezpieczeństwo': 'B',
     'Frontend (Next.js)': 'F', 'Frontend': 'F', 'Makiety': 'F', 'Dokumentacja': 'W'}
    SIDE_TOP = {'Makiety (4h)': 'F', 'Strony publiczne': 'F', 'Filtrowanie historii aktywności': 'F',
     'Dostępność': 'F', 'Frontend (Next.js) – warstwa wspólna': 'F', 'Bezpieczeństwo': 'B',
     'Model danych': 'B', 'API REST (Symfony)': 'B'}
    WSPOLNE = {'Utworzenie repozytorium github', 'Przygotowanie struktury projektu (backend + frontend)'}
    def side(r):
        lvl, cell = info[r]; v = str(cell.value).strip()
        if lvl == 0: return SIDE_TOP.get(v)
        if v in WSPOLNE: return 'W'
        if lvl >= 1 and v in SIDE_LABEL and children[r] or (lvl == 1 and v in SIDE_LABEL): return SIDE_LABEL[v]
        return side(parent[r])
    def top(r):
        while parent[r]: r = parent[r]
        return r

    MILESTONES = [
     ('M1 Konfiguracja Projektu', ['Makiety (4h)', 'Inicjalizacja projektu']),
     ('M2 Wdrożenie: logowanie i konto', ['Konto i uwierzytelnianie', 'Model danych', 'API REST (Symfony)', 'Frontend (Next.js) – warstwa wspólna']),
     ('M3 Wdrożenie: strony publiczne', ['Strony publiczne']),
     ('M4 Wdrożenie: formy ćwiczeń i aktywności', ['Formy ćwiczeń', 'Aktywności']),
     ('M5 Wdrożenie: Home i historia', ['Home', 'Filtrowanie historii aktywności']),
     ('M6 Wdrożenie: O mnie', ['O mnie']),
     ('M7 Wdrożenie: dostępność i bezpieczeństwo', ['Dostępność', 'Bezpieczeństwo']),
    ]
    tops = {str(info[r][1].value).strip(): r for r in kept if info[r][0] == 0}
    assert sorted(sum((b for _, b in MILESTONES), [])) == sorted(tops), (sorted(tops))

    def build(name, sides, title):
        s = new_sheet(name)
        for r in (1, 2): copy_row(s, r, r)
        s['B1'].value = f'{ws["B1"].value} – {title}'
        copy_cell(ws['J3'], s['J3'])
        out = 4; first = 4
        for ms, branches in MILESTONES:
            ms_written = False
            for b in branches:
                br = tops[b]
                members = [r for r in kept if top(r) == br and r != br and side(r) in sides]
                if not members and side(br) not in sides: continue
                # include ancestors of members
                need = set(members)
                for m in members:
                    p = parent[m]
                    while p and p != br: need.add(p); p = parent[p]
                if not ms_written:
                    s[f'A{out}'].value = ms; s[f'A{out}'].font = Font(bold=True); ms_written = True
                copy_row(s, br, out, skip_a=True); out += 1
                for r in sorted(need):
                    copy_row(s, r, out, skip_a=True); out += 1
        sum_row(s, first, out - 1, out)
        return s, first, out - 1
    bs = build('Backend', {'B', 'W'}, 'Backend (Symfony) + Wspólne')
    fs = build('Frontend', {'F'}, 'Frontend (Next.js)')
    wb.save(DST)

def reorg(P):
    wb = openpyxl.load_workbook(P)
    HC = 'KLMN'

    PLAN = {
     'Backend': [
      ('M1 Konfiguracja Projektu', [
        ('B-1.1', 'Wspólne: repozytorium, struktura, README', ['Utworzenie repozytorium github', 'Przygotowanie struktury projektu (backend + frontend)', 'README – instrukcja uruchomienia']),
        ('B-1.2', 'Konfiguracja Symfony', ['Konfiguracja Symfony i Doctrine ORM', 'Konfiguracja bazy danych', 'Instalacja API Platform', 'Konfiguracja uwierzytelniania JWT', 'Konfiguracja CORS'])]),
      ('M2 Wdrożenie: logowanie i konto', [
        ('B-2.1', 'Model danych i migracje', ['Użytkownik (e-mail, hash hasła, role, status, data rejestracji)', 'kaskadowe usuwanie aktywności z formą i kontem', 'unikalność e-maila i nazwy formy w obrębie użytkownika', 'walidacja na poziomie encji (Assert)', 'Migracje bazy danych (Doctrine Migrations)']),
        ('B-2.2', 'Bezpieczeństwo konta: hasła, tokeny, autoryzacja', ['hashowanie haseł (Argon2id / bcrypt – PasswordHasher)', 'polityka siły hasła (min. 8 znaków)', 'generowanie kluczy JWT (RS256)', 'przechowywanie tokenu w ciasteczku httpOnly, Secure, SameSite', 'role ROLE_USER', 'Voters – dostęp tylko do własnych zasobów']),
        ('B-2.3', 'Endpointy uwierzytelniania', ['endpoint rejestracji', 'endpoint logowania (wydanie tokenu JWT)', 'endpoint wylogowania']),
        ('B-2.4', 'Warstwa techniczna API', ['DTO i grupy serializacji (ukrycie hasha hasła)', 'walidacja danych wejściowych (Validator)', 'globalna obsługa wyjątków'])]),
      ('M4 Wdrożenie: formy ćwiczeń i aktywności', [
        ('B-4.1', 'Formy ćwiczeń: encja i CRUD', ['Forma ćwiczenia (nazwa, jednostka, typ wykresu, właściciel)', 'Formy ćwiczeń (CRUD)']),
        ('B-4.2', 'Aktywności: encja i CRUD', ['Aktywność (data, wartość, kroki, spalone kalorie, notatka, forma, użytkownik)', 'CRUD']),
        ('B-4.3', 'Aktywności: filtrowanie, sortowanie, statystyki', ['filtrowanie po zakresie dat i formie', 'sortowanie po dacie, krokach i spalonych kaloriach (rosnąco/malejąco)', 'agregacja danych do wykresu (dzień/tydzień/miesiąc)', 'zapytania agregujące (SUM, AVG, MAX, COUNT)'])]),
      ('M6 Wdrożenie: O mnie', [
        ('B-6.1', 'Profil użytkownika (API)', ['Profil użytkownika'])]),
      ('M7 Wdrożenie: dostępność i bezpieczeństwo', [
        ('B-7.1', 'Ochrona aplikacji i RODO', ['ochrona CSRF dla ciasteczek (SameSite + token)', 'brak ujawniania szczegółów błędów na produkcji', 'minimalizacja zbieranych danych'])]),
     ],
     'Frontend': [
      ('M1 Konfiguracja Projektu', [
        ('F-1.1', 'Makiety', ['Makiety (4h)']),
        ('F-1.2', 'Konfiguracja Next.js', ['Utworzenie projektu Next.js (TypeScript)', 'Konfiguracja stylów (np. Tailwind CSS)', 'Instalacja biblioteki wykresów (Chart.js + zoom)', 'Konfiguracja ESLint / Prettier'])]),
      ('M2 Wdrożenie: logowanie i konto', [
        ('F-2.1', 'Klient API, layout i komponenty wspólne', ['klient API (fetch / axios) z bazowym adresem z .env', 'layout aplikacji i wstążka nawigacji', 'komunikaty (toast) i potwierdzenia', 'stany ładowania i puste stany', 'obsługa formatów dat i liczb (locale pl-PL)']),
        ('F-2.2', 'Komponent wykresu', ['komponent wykresu (konfigurowalny typ)']),
        ('F-2.3', 'Sesja i routing', ['ochrona tras (middleware Next.js)', 'przekierowanie po wygaśnięciu sesji', 'kontekst zalogowanego użytkownika']),
        ('F-2.4', 'Rejestracja i logowanie', ['formularz rejestracji', ('walidacja danych', 'Konto i uwierzytelnianie'), 'logowanie', 'wylogowanie', 'blokada po nieudanych próbach'])]),
      ('M3 Wdrożenie: strony publiczne', [
        ('F-3.1', 'Strony publiczne', ['Strona główna', 'Strona polityki prywatności', 'Akceptacja ciasteczek'])]),
      ('M4 Wdrożenie: formy ćwiczeń i aktywności', [
        ('F-4.1', 'Formy ćwiczeń', ['dodawanie formy', 'edycja formy', 'usuwanie formy']),
        ('F-4.2', 'Record (formularz aktywności)', ['formularz aktywności', 'pola kroki i spalone kalorie', ('walidacja danych', 'Aktywności'), 'zapis aktywności']),
        ('F-4.3', 'Szczegóły aktywności', ['podgląd aktywności', 'edycja pomiarów', 'usuwanie aktywności'])]),
      ('M5 Wdrożenie: Home i historia', [
        ('F-5.1', 'Home: wykresy i lista aktywności', ['przewijanie wykresów', 'przybliżanie wykresów', 'lista aktywności', 'sortowanie listy (data, kroki, kalorie)']),
        ('F-5.2', 'Filtry historii', ['Wybór zakresu dat', 'Wybór formy ćwiczenia', 'Jednoczesne zastosowanie filtrów daty i formy ćwiczenia', 'Czyszczenie zastosowanych filtrów', 'Wyświetlenie komunikatu przy braku wyników'])]),
      ('M6 Wdrożenie: O mnie', [
        ('F-6.1', 'O mnie: podsumowanie okresowe', ['podsumowanie okresowe', 'zmiana okresu']),
        ('F-6.2', 'O mnie: profil i ustawienia', ['edycja profilu', 'wybór ulubionej aktywności'])]),
      ('M7 Wdrożenie: dostępność i bezpieczeństwo', [
        ('F-7.1', 'Dostępność: ARIA i obsługa klawiatury', ['Dostępność komponentów (ARIA, semantyczny HTML)', 'obsługa klawiatury i kolejność fokusu', 'link „Przejdź do treści”']),
        ('F-7.2', 'Dostępność: ruch i dotyk', ['ograniczenie animacji (prefers-reduced-motion)', 'duże pola dotykowe (min. 44×44 px)'])]),
     ],
    }

    def collect(s):
        """leaves: (name, top-branch) -> row; top-branch = nearest B-level label above."""
        leaves, top = {}, None
        sr = next(r for r in range(1, s.max_row + 1) if isinstance(s[f'K{r}'].value, str) and s[f'K{r}'].value.startswith('=SUM'))
        for r in range(4, sr):
            lab = next(((i, s.cell(r, 2 + i).value) for i in range(4) if s.cell(r, 2 + i).value), None)
            if not lab: continue
            if lab[0] == 0: top = lab[1]
            if any(isinstance(s[f'{c}{r}'].value, (int, float)) for c in HC):
                key = (lab[1], top)
                assert key not in leaves, key
                leaves[key] = r
        return leaves, sr

    def cp(src, dst, value=None):
        dst.value = src.value if value is None else value
        if src.has_style:
            dst.font = copy.copy(src.font); dst.fill = copy.copy(src.fill); dst.border = copy.copy(src.border)
            dst.alignment = copy.copy(src.alignment); dst.number_format = src.number_format

    for name, plan in PLAN.items():
        old = wb[name]
        leaves, sr = collect(old)
        idx = wb.sheetnames.index(name)
        new = wb.create_sheet(name + '_tmp', idx)
        for k, d in old.column_dimensions.items(): new.column_dimensions[k].width = d.width
        for r in (1, 2, 3):
            for c in 'ABCDEFGHIJKLMNO': cp(old[f'{c}{r}'], new[f'{c}{r}'])
        new['A3'].value = 'kamień milowy'; new['B3'].value = 'pakiet pracy'; new['C3'].value = 'zadanie'; new['H3'].value = 'kto'
        for c in 'ABCH': new[f'{c}3'].font = Font(bold=True)
        out, used = 4, []
        for ms, pkgs in plan:
            first = True
            for code, title, tasks in pkgs:
                if first: new[f'A{out}'].value = ms; new[f'A{out}'].font = Font(bold=True); first = False
                new[f'B{out}'].value = f'{code} {title}'; new[f'B{out}'].font = Font(bold=True); out += 1
                for t in tasks:
                    tname, ttop = (t if isinstance(t, tuple) else (t, None))
                    cands = [k for k in leaves if k[0] == tname and (ttop is None or k[1] == ttop)]
                    assert len(cands) == 1, (name, t, cands)
                    k = cands[0]; used.append(k); r = leaves[k]
                    src_lab = next(old.cell(r, 2 + i) for i in range(4) if old.cell(r, 2 + i).value)
                    cp(src_lab, new[f'C{out}'])
                    for c in 'HIJ' + HC: cp(old[f'{c}{r}'], new[f'{c}{out}'])
                    out += 1
        missing = set(leaves) - set(used); dup = [k for k, v in Counter(used).items() if v > 1]
        assert not missing and not dup, (name, missing, dup)
        cp(old[f'J{sr}'], new[f'J{out}'])
        for c in HC: cp(old[f'{c}{sr}'], new[f'{c}{out}'], f'=SUM({c}4:{c}{out - 1})')
        wb.remove(old); new.title = name
    order = ['WBS', 'WBS (czysty)', 'Backend', 'Frontend']
    wb._sheets.sort(key=lambda ws: order.index(ws.title))
    wb.active = 0
    wb.save(P)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    build(sys.argv[1], sys.argv[2])
    reorg(sys.argv[2])
    print('zapisano', sys.argv[2])

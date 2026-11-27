# WBS i szacowanie (metoda Delphi)

Plik źródłowy: `estimates/WBS_SAMOZAMYKACZ_2026_3.xlsx` (arkusz `WBS`), kopia pliku
`WBS_SAMOZAMYKACZ_2026.xlsx` z 2026-11-26. Ten dokument jest tylko podsumowaniem — wiążący jest arkusz.

> **Szacowanie zamknięte.** Notatka prowadzącego w O3: „proszę już tego nie uzupełniać tylko skupić się
> na dalszych krokach. A.Karczmarczyk”. Kolumny O (godziny po dyskusji) nie wypełniamy.

## Układ arkusza
| Kolumna / wiersz | Zawartość |
|---|---|
| A | kamień milowy: „Konfiguracja Projektu” (wiersz 2), „Wdrożenie Aplikacji” (wiersz 22) |
| B–E | poziomy drzewa WBS (B = poziom 1) |
| H | kto wykonuje zadanie (puste) |
| J | etykiety szablonu Delphi (J2 „Imię i Nazwisko”, J3 „ilość godzin szacowana indywidualnie”, J258 „suma”) |
| K | Patryk Woźnicki (PW) |
| L | Gracjan Grzeszczak |
| M | Paweł Ewald |
| N | Michał Marcinkowski |
| O | godziny po dyskusji — nie wypełniamy (notatka w O3) |
| wiersz 3 | „Makiety (4h)” — wszystkie makiety łącznie, po 4 h na osobę |
| wiersz 258 | suma `=SUM(K3:K257)` dla K–N |

Godziny tylko przy zadaniach najniższego poziomu. Wiersze „Makiety” w gałęziach nie mają godzin
(pokrywa je wiersz 3).

## Godziny według gałęzi
| Gałąź (poziom 1) | PW | GG | PE | MM |
|---|---|---|---|---|
| Makiety (4h) | 4 | 4 | 4 | 4 |
| Inicjalizacja projektu | 9,5 | 6,25 | 11 | 11 |
| Konto i uwierzytelnianie | 15 | 10,75 | 13 | 26 |
| Strony publiczne | 3 | 1,75 | 5 | 10 |
| Nawigacja | 0 | 0 | 0 | 0 |
| Home | 4,5 | 2,75 | 5 | 12 |
| Aktywności | 11,5 | 10,75 | 15,5 | 34,5 |
| Filtrowanie historii aktywności | 3 | 1,5 | 7 | 10 |
| Formy ćwiczeń | 3,5 | 3,5 | 9 | 4,5 |
| O mnie (z Celami treningowymi) | 4 | 2,5 | 14 | 13 |
| Dostępność | 2 | 1,5 | 14,5 | 11 |
| Bezpieczeństwo | 2,5 | 0,75 | 7 | 4 |
| Model danych | 2,5 | 1,25 | 4,5 | 2,5 |
| API REST (Symfony) | 3 | 1,25 | 5,5 | 3 |
| Frontend (Next.js) – warstwa wspólna | 6 | 4,5 | 11,5 | 12,5 |
| **Razem** | **74** | **53** | **126,5** | **158** |

Ok. 90 zadań-liści nie ma godzin u nikogo (np. reset hasła, wstążka, cele treningowe, część dostępności
i bezpieczeństwa), więc sumy nie obejmują całego zakresu.

## Historia wersji arkusza
1. Wersja wygenerowana od zera (kamienie M1–M7, gałęzie testów, wdrożenia, CI/CD, administracji).
2. `WBS_SAMOZAMYKACZ_2026.xlsx` — wersja użytkownika (bez testów/wdrożenia/CI/CD/administracji).
3. Ta sama z dopisanym numerowanym WBS (1.1–13.3.3) od wiersza 221.
4. `WBS_SAMOZAMYKACZ_2026_2.xlsx` — struktura po funkcjonalnościach; godziny PW skrócone za pracę z AI
   (194,5 h, wcześniej 339,5 h). Współczynniki: kod ×0,5, bezpieczeństwo/złożona logika ×0,6,
   makiety ×0,7, dokumentacja ×0,4.
5. `WBS_SAMOZAMYKACZ_2026_3.xlsx` — szacunki czterech osób (K–N), wspólny wiersz makiet, usunięte
   pozostałości (dawne wiersze 256–285), suma w wierszu 258; szacowanie zamknięte przez prowadzącego. **Aktualna.**

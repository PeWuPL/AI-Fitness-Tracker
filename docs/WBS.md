# WBS i szacowanie (metoda Delphi)

Plik: `estimates/WBS_SAMOZAMYKACZ_2026.xlsx` — ta sama nazwa co plik główny zespołu. Przy każdej zmianie
podmieniamy ten plik; poprzednie wersje są w historii gita (bez przyrostków `_2`, `_3`…).
Ten dokument jest tylko podsumowaniem — wiążący jest arkusz.

> **Szacowanie zamknięte.** Notatka prowadzącego (WBS!O3): „proszę już tego nie uzupełniać tylko skupić się
> na dalszych krokach. A.Karczmarczyk”. Nie dopisujemy godzin.

## Arkusze
| Arkusz | Zawartość |
|---|---|
| `WBS` | Oryginał zespołu (stan z 2026-11-26), bez zmian. |
| `WBS (czysty)` | `WBS` bez wierszy czerwonych i przekreślonych (oraz gałęzi, które po tym zostały puste). |
| `Backend` | Pakiety pracy backendu (Symfony) + pakiet wspólny B-1.1. |
| `Frontend` | Pakiety pracy frontendu (Next.js) + makiety. |

## Układ arkusza `WBS`
| Kolumna / wiersz | Zawartość |
|---|---|
| A | kamień milowy: „Konfiguracja Projektu” (2), „Wdrożenie Aplikacji” (22) |
| B–E | poziomy drzewa WBS (B = poziom 1) |
| H | kto wykonuje (puste) |
| J | etykiety szablonu Delphi |
| K / L / M / N | Patryk Woźnicki (PW) / Gracjan Grzeszczak (GG) / Paweł Ewald (PE) / Michał Marcinkowski (MM) |
| O | godziny po dyskusji — nie wypełniamy; w O3 notatka prowadzącego |
| wiersz 3 | „Makiety (4h)” — wszystkie makiety łącznie |
| wiersz 258 | suma `=SUM(K3:K257)` |

## Arkusze `Backend` i `Frontend`
- A: kamień milowy (wspólne dla obu arkuszy), B: pakiet pracy z kodem (`B-x.y` / `F-x.y`),
  C: zadanie z oryginalną nazwą i godzinami K–N, H: kto (do przypisania).
- Pakiet = jedna strona × jedna funkcjonalność × jeden kamień — jednostka pracy dla jednej osoby.
- Godziny tylko przy zadaniach; pakiety bez sum częściowych. Suma na dole arkusza.

| Kamień | Gałęzie WBS |
|---|---|
| M1 Konfiguracja Projektu | Makiety, Inicjalizacja projektu |
| M2 Wdrożenie: logowanie i konto | Konto i uwierzytelnianie, Model danych, API REST, warstwa wspólna Next.js |
| M3 Wdrożenie: strony publiczne | Strony publiczne |
| M4 Wdrożenie: formy ćwiczeń i aktywności | Formy ćwiczeń, Aktywności |
| M5 Wdrożenie: Home i historia | Home, Filtrowanie historii aktywności |
| M6 Wdrożenie: O mnie | O mnie |
| M7 Wdrożenie: dostępność i bezpieczeństwo | Dostępność, Bezpieczeństwo |

| Kamień | Pakiet | śr. h* |
|---|---|---|
| M1 | B-1.1 Wspólne: repozytorium, struktura, README | 2,6 |
| M1 | B-1.2 Konfiguracja Symfony | 3,8 |
| M1 | F-1.1 Makiety | 4,0 |
| M1 | F-1.2 Konfiguracja Next.js | 2,9 |
| M2 | B-2.1 Model danych i migracje | 3,3 |
| M2 | B-2.2 Bezpieczeństwo konta: hasła, tokeny, autoryzacja | 4,6 |
| M2 | B-2.3 Endpointy uwierzytelniania | 2,3 |
| M2 | B-2.4 Warstwa techniczna API | 3,2 |
| M2 | F-2.1 Klient API, layout i komponenty wspólne | 6,0 |
| M2 | F-2.2 Komponent wykresu | 2,6 |
| M2 | F-2.3 Sesja i routing | 2,8 |
| M2 | F-2.4 Rejestracja i logowanie | 5,8 |
| M3 | F-3.1 Strony publiczne | 4,9 |
| M4 | B-4.1 Formy ćwiczeń: encja i CRUD | 1,9 |
| M4 | B-4.2 Aktywności: encja i CRUD | 2,2 |
| M4 | B-4.3 Aktywności: filtrowanie, sortowanie, statystyki | 4,1 |
| M4 | F-4.1 Formy ćwiczeń | 3,2 |
| M4 | F-4.2 Record (formularz aktywności) | 6,8 |
| M4 | F-4.3 Szczegóły aktywności | 5,1 |
| M5 | F-5.1 Home: wykresy i lista aktywności | 6,1 |
| M5 | F-5.2 Filtry historii | 5,4 |
| M6 | B-6.1 Profil użytkownika (API) | 1,3 |
| M6 | F-6.1 O mnie: podsumowanie okresowe | 3,7 |
| M6 | F-6.2 O mnie: profil i ustawienia | 3,4 |
| M7 | B-7.1 Ochrona aplikacji i RODO | 3,6 |
| M7 | F-7.1 Dostępność: ARIA i obsługa klawiatury | 4,5 |
| M7 | F-7.2 Dostępność: ruch i dotyk | 2,8 |

\* średnia z szacunków czterech osób — tylko orientacyjnie, nie ma jej w arkuszu.

## Sumy godzin
| Arkusz | PW | GG | PE | MM |
|---|---|---|---|---|
| `WBS` | 74 | 53 | 126,5 | 158 |
| `WBS (czysty)` | 73 | 53 | 126 | 158 |
| `Backend` | 31 | 22 | 42,5 | 35 |
| `Frontend` | 42 | 31 | 83,5 | 123 |

`WBS (czysty)` jest mniejszy o 3 czerwone zadania, które miały godziny: Swiper (PE 0,5), token resetu/aktywacji
(PW 0,5), refresh token (PW 0,5). Backend + Frontend = `WBS (czysty)`.

## Historia wersji arkusza
1. Wersja wygenerowana od zera (kamienie M1–M7, gałęzie testów, wdrożenia, CI/CD, administracji).
2. Wersja zespołu bez testów/wdrożenia/CI/CD/administracji; potem numerowany WBS od wiersza 221.
3. Struktura po funkcjonalnościach; godziny PW skrócone za pracę z AI (194,5 h, wcześniej 339,5 h).
4. Szacunki czterech osób (K–N), wspólny wiersz makiet; szacowanie zamknięte przez prowadzącego.
5. Dodane arkusze `WBS (czysty)`, `Backend`, `Frontend` (pakiety pracy, kamienie M1–M7). **Aktualna.**

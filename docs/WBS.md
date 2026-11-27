# WBS i szacowanie (metoda Delphi)

Plik: `estimates/WBS_SAMOZAMYKACZ_2026.xlsx`. Od 2026-11-26 zespół edytuje **bezpośrednio ten plik**
(przydział osób, korekty szacunków). Plik `../WBS_SAMOZAMYKACZ_2026.xlsx` poza repo jest nieaktualny.
Ten dokument jest tylko podsumowaniem — wiążący jest arkusz. Poprzednie wersje są w historii gita.

> **Szacowanie zamknięte.** Notatka prowadzącego (WBS!O3): „proszę już tego nie uzupełniać tylko skupić się
> na dalszych krokach. A.Karczmarczyk”.

**Kod kolorów w arkuszu `WBS`:** zadanie czerwone lub przekreślone = poza zakresem, nie trafia do pakietów.

## Arkusze
| Arkusz | Zawartość |
|---|---|
| `WBS` | Arkusz główny zespołu: drzewo zadań i szacunki. |
| `WBS - Czysty` | `WBS` bez wierszy czerwonych i przekreślonych (oraz gałęzi, które po tym zostały puste). |
| `Backend` | Pakiety pracy backendu (Symfony) + pakiet wspólny B-1.1, z przydziałem osób. |
| `Frontend` | Pakiety pracy frontendu (Next.js) + makiety, z przydziałem osób. |

Godziny w `WBS - Czysty`, `Backend` i `Frontend` są kopią godzin z `WBS` (zsynchronizowane 2026-11-26).
Po zmianie godzin w `WBS` trzeba je przepisać także tam.

## Układ arkusza `WBS`
| Kolumna / wiersz | Zawartość |
|---|---|
| A | kamień milowy: „Konfiguracja Projektu” (2), „Wdrożenie Aplikacji” (22) |
| B–E | poziomy drzewa WBS (B = poziom 1) |
| J | etykiety szablonu Delphi |
| K / L / M / N | Patryk Woźnicki (PW) / Gracjan Grzeszczak (GG) / Paweł Ewald (PE) / Michał Marcinkowski (MM) |
| O | godziny po dyskusji — nie wypełniamy; w O3 notatka prowadzącego |
| wiersz 3 | „Makiety (4h)” — wszystkie makiety łącznie |
| wiersz 258 | suma `=SUM(K3:K257)` |

## Arkusze `Backend` i `Frontend`
| Kolumna | Zawartość |
|---|---|
| A | kamień milowy M1–M7 (wspólne dla obu arkuszy) |
| B | pakiet pracy z kodem `B-x.y` / `F-x.y` |
| C | zadanie (oryginalna nazwa) |
| G4:H8 | podsumowanie: liczba zadań na osobę (`COUNTIF` po kolumnie J) |
| **J** | **osoba wykonująca zadanie** (PW / GG / PE / MM) |
| K–N | godziny (szacunki czterech osób) |

- Przydział jest **na poziomie zadania** — pakiet może mieć kilka osób (np. F-2.1: GG i PE).
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

## Pakiety i przydział
| Kamień | Pakiet | Kto | śr. h* |
|---|---|---|---|
| M1 | B-1.1 Wspólne: repozytorium, struktura, README | PW | 2,6 |
| M1 | B-1.2 Konfiguracja Symfony | PW | 3,8 |
| M1 | F-1.1 Makiety | **nieprzypisane** | 4,0 |
| M1 | F-1.2 Konfiguracja Next.js (Bootstrap) | GG | 2,4 |
| M2 | B-2.1 Model danych i migracje | MM | 3,2 |
| M2 | B-2.2 Bezpieczeństwo konta: hasła, tokeny, autoryzacja | MM | 3,8 |
| M2 | B-2.3 Endpointy uwierzytelniania | MM | 2,2 |
| M2 | B-2.4 Warstwa techniczna API | PW | 2,8 |
| M2 | F-2.1 Klient API, layout i komponenty wspólne | GG, PE | 5,0 |
| M2 | F-2.2 Komponent wykresu | PE | 1,6 |
| M2 | F-2.3 Sesja i routing | PE | 2,2 |
| M2 | F-2.4 Rejestracja i logowanie | GG | 4,3 |
| M3 | F-3.1 Strony publiczne | PE | 3,4 |
| M4 | B-4.1 Formy ćwiczeń: encja i CRUD | PW | 1,7 |
| M4 | B-4.2 Aktywności: encja i CRUD | MM | 2,2 |
| M4 | B-4.3 Aktywności: filtrowanie, sortowanie, statystyki | MM | 4,1 |
| M4 | F-4.1 Formy ćwiczeń | PE | 2,4 |
| M4 | F-4.2 Record (formularz aktywności) | PW | 3,8 |
| M4 | F-4.3 Szczegóły aktywności | PW | 2,8 |
| M5 | F-5.1 Home: wykresy i lista aktywności | PW | 4,3 |
| M5 | F-5.2 Filtry historii | PW | 3,4 |
| M6 | B-6.1 Profil użytkownika (API) | MM | 1,0 |
| M6 | F-6.1 O mnie: podsumowanie okresowe | PW | 1,8 |
| M6 | F-6.2 O mnie: profil i ustawienia | PW | 1,6 |
| M7 | B-7.1 Ochrona aplikacji i RODO | **nieprzypisane** | 2,6 |
| M7 | F-7.1 Dostępność: ARIA i obsługa klawiatury | PE | 1,9 |
| M7 | F-7.2 Dostępność: ruch i dotyk | GG (1 z 2 zadań nieprzypisane) | 1,2 |

\* średnia z szacunków czterech osób — tylko orientacyjnie, nie ma jej w arkuszu.

## Obciążenie osób
| Osoba | Zadań | h wg własnego szacunku | h wg średniej |
|---|---|---|---|
| PW | 33 | 28,5 | 28,5 |
| MM | 21 | 17 | 16,6 |
| PE | 16 | 17,5 | 14,1 |
| GG | 12 | 7,5 | 9,9 |
| nieprzypisane | 5 | — | 7,3 |

## Sumy godzin (po korekcie szacunków PE i MM, 2026-11-26)
| Arkusz | PW | GG | PE | MM |
|---|---|---|---|---|
| `WBS` | 74 | 53 | 93 | 86,5 |
| `WBS - Czysty` | 73 | 53 | 92,5 | 86,5 |
| `Backend` | 31 | 22 | 36 | 31 |
| `Frontend` | 42 | 31 | 56,5 | 55,5 |

Przed korektą: PE 126,5 h, MM 158 h. `WBS - Czysty` jest mniejszy od `WBS` o 3 czerwone zadania z godzinami
(Swiper, token resetu/aktywacji, refresh token). Backend + Frontend = `WBS - Czysty`.

## Historia wersji arkusza
1. Wersja wygenerowana od zera (kamienie M1–M7, gałęzie testów, wdrożenia, CI/CD, administracji).
2. Wersja zespołu bez testów/wdrożenia/CI/CD/administracji; potem numerowany WBS od wiersza 221.
3. Struktura po funkcjonalnościach; godziny PW skrócone za pracę z AI (194,5 h, wcześniej 339,5 h).
4. Szacunki czterech osób (K–N), wspólny wiersz makiet; szacowanie zamknięte przez prowadzącego.
5. Arkusze `WBS (czysty)`, `Backend`, `Frontend` (pakiety pracy, kamienie M1–M7), generowane `tools/wbs_build.py`.
6. Edycja zespołu w repo: przydział osób (kolumna J), korekta szacunków PE i MM, Bootstrap zamiast Tailwind,
   arkusz przemianowany na `WBS - Czysty`; godziny arkuszy pochodnych zsynchronizowane z `WBS`. **Aktualna.**

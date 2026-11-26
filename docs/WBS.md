# WBS i szacowanie (metoda Delphi)

Plik źródłowy: `estimates/WBS_SAMOZAMYKACZ_2026_2.xlsx` (arkusz `WBS`). Użytkownik edytuje go w Excelu;
ten dokument jest tylko podsumowaniem — w razie rozbieżności wiążący jest arkusz.

## Układ arkusza
| Kolumna | Zawartość |
|---|---|
| A | kamień milowy (w v2026_2 pusta — kamienie z wcześniejszych wersji usunięte) |
| B–E | poziomy drzewa WBS (B = poziom 1) |
| H | kto wykonuje zadanie (do uzupełnienia) |
| J | szacunek indywidualny **PW** [h] |
| K–N | szacunki indywidualne pozostałych osób (do uzupełnienia) |
| O | liczba godzin po dyskusji w grupie (do uzupełnienia) |
| wiersz 287 | suma `=SUM(x3:x255)` dla J–O |
| wiersz 289 | opis współczynników skrócenia za pracę z AI |

Zasady: godziny tylko przy zadaniach najniższego poziomu (bez podzadań); zadania nadrzędne puste.

## Struktura (v2026_2, wiersze 2–255) i godziny PW po skróceniu
| Gałąź (poziom 1) | Zawartość | h PW |
|---|---|---|
| Inicjalizacja projektu | repo, struktura, backend (Symfony, Doctrine, baza, API Platform, JWT, CORS), frontend (Next.js, Tailwind, Chart.js, Swiper, ESLint), Docker, README | 10,5 |
| Konto i uwierzytelnianie | makiety, encje Użytkownik/tokeny, hasła (hashowanie Argon2id/bcrypt), tokeny JWT/refresh, autoryzacja (Voters), endpointy, frontend sesji/rejestracji/logowania/resetu | 35,5 |
| Strony publiczne | strona główna, polityka prywatności, ciasteczka (makiety + frontend) | 6,5 |
| Nawigacja | wstążka (makieta + frontend) | 1,5 |
| Home | makiety, ustawienia kart (model, API), wykresy, karty, lista, filtrowanie, sortowanie | 19 |
| Aktywności | makiety Record/szczegóły, encja Aktywność + indeksy, API (CRUD, filtr, sortowanie, paginacja, agregacja, statystyki), frontend | 20,5 |
| Filtrowanie historii aktywności | makieta panelu, komponent filtrów (zakres dat, forma, łączenie, czyszczenie, brak wyników) | 4 |
| Formy ćwiczeń | makieta, encja, API CRUD, frontend | 5 |
| O mnie | makiety, API profilu, podsumowanie, profil, hasło, ulubiona aktywność, wylogowanie, usunięcie konta, **Cele treningowe** | 22 |
| Dostępność | makiety (kontrast, fokus, tabela danych), komponenty ARIA, 11 zadań WCAG | 17,5 |
| Bezpieczeństwo | ochrona przed atakami, RODO, logowanie zdarzeń | 17 |
| Model danych | ERD, relacje, UTC, migracje, fixtures | 7,5 |
| API REST (Symfony) | warstwa techniczna (DTO, walidacja, RFC 7807, wyjątki, e-maile, logi, środowiska), OpenAPI | 10 |
| Frontend (Next.js) – warstwa wspólna | klient API, cache (TanStack Query/SWR), komponenty, wydajność | 18 |
| **Razem** | | **194,5** |

Przed skróceniem za pracę z AI suma wynosiła 339,5 h.

## Metoda skrócenia (praca z pomocą AI)
| Rodzaj pracy | Współczynnik |
|---|---|
| Kod (konfiguracja, CRUD, API, frontend) | ×0,5 |
| Bezpieczeństwo i złożona logika (np. obliczanie postępu celu) | ×0,6 |
| Makiety | ×0,7 |
| Dokumentacja | ×0,4 |

Zaokrąglenie w górę do 0,5 h, minimum 0,5 h.

## Historia wersji arkusza
1. Wersja wygenerowana od zera (drzewo B–E, kamienie milowe M1–M7, gałęzie testów, wdrożenia, CI/CD, administracji).
2. `WBS_SAMOZAMYKACZ_2026.xlsx` — wersja użytkownika (bez testów/wdrożenia/CI/CD/administracji), szablon Delphi w J1:O15.
3. Ta sama wersja z dopisanym, numerowanym WBS (1.1–13.3.3) od wiersza 221; godziny PW tylko od 1.1.
4. `WBS_SAMOZAMYKACZ_2026_2.xlsx` — przeorganizowana struktura po funkcjonalnościach (wiersze 2–255), nowe gałęzie
   „Filtrowanie historii aktywności” i „Cele treningowe”; godziny PW skrócone za pracę z AI. **Aktualna.**

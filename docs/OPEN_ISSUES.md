# Otwarte kwestie i niespójności

Stan: SRS z .docx i WBS v2026_3 (2026-11-26).

## SRS — niespójności wewnętrzne
1. **Reset hasła:** IK-5 mówi, że nie ma e-maili resetu hasła, a WBS ma makietę, tokeny, endpointy i frontend
   resetu (wiersze 26, 29, 42, 54, 68). Usunąć z WBS albo dopisać wymaganie w SRS.
2. **Wersja angielska:** 2.3 — „opcjonalne rozszerzenie”; WF-12.16 i WIL-1 — wymóg PL + EN. Ustalić jedno.
   WF-12.16 lepiej pasuje do sekcji 7 niż do dostępności.
3. **WF-12.17 powtarza WF-12.10** (oznaczenia wykresów nie tylko kolorem). Usunąć jedno.
4. **Strefa czasowa:** WIL-2 — polska strefa; WBS — „przechowywanie dat w UTC, konwersja do strefy użytkownika”.
5. **Puste sekcje .docx:** tabela wersji (szablon 0.1.0/2022), 1.4 Odwołania, 4.1 Model danych, 8, Suplement A
   (słownik — propozycja w `SRS.md`), Suplement B (storytelling/makiety).

## WBS v2026_3
6. **Możliwe podwójne liczenie filtrowania:** „Home → filtrowanie listy aktywności” (wiersz 100) oraz gałąź
   „Filtrowanie historii aktywności” (wiersze 132–141).
7. **Brak gałęzi testów, wdrożenia i CI/CD**, choć kamień milowy w A22 to „Wdrożenie Aplikacji”.
8. **Kolumna H (kto wykonuje) pusta** — przypisać zadania.
9. **Ok. 90 zadań-liści bez godzin** u wszystkich osób. Szacowanie zamknięte przez prowadzącego, więc tylko do wiadomości.

## Ogólne
10. **Kalorie:** przyjęto ręczne wpisywanie. Alternatywa: szacowanie z formy, czasu i wagi z profilu (nowe wymaganie).
11. Terminy kamieni milowych od prowadzącego.

## Rozwiązane (2026-11-26)
- Administrator usunięty z SRS (klasy: UŻ-1 niezalogowany, UŻ-2 zarejestrowany) — zgodne z WBS (`ROLE_USER`).
- Cele treningowe opisane w SRS (WF-9.4–9.6, UI-10.2).
- Filtrowanie historii ma osobną sekcję 3.11 (WF-11.1–11.5).
- Pozostałości w arkuszu (dawne wiersze 256–285) usunięte; etykiety szablonu nie kolidują z godzinami.
- Skład zespołu wpisany w K2:N2.

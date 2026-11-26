# Otwarte kwestie i niespójności

Stan: SRS z .docx i `estimates/WBS_SAMOZAMYKACZ_2026.xlsx` z arkuszami `WBS (czysty)`, `Backend`, `Frontend` (2026-11-26).

## SRS — niespójności wewnętrzne
1. **Wersja angielska:** 2.3 — „opcjonalne rozszerzenie”; WF-12.16 i WIL-1 — wymóg PL + EN. Ustalić jedno.
   WF-12.16 lepiej pasuje do sekcji 7 niż do dostępności.
2. **WF-12.17 powtarza WF-12.10** (oznaczenia wykresów nie tylko kolorem). Usunąć jedno.
3. **Strefa czasowa:** WIL-2 — polska strefa; oryginalny WBS miał „daty w UTC, konwersja do strefy użytkownika”
   (czerwone — nie ma go w pakietach). Ustalić podejście.
4. **Puste sekcje .docx:** tabela wersji (szablon 0.1.0/2022), 1.4 Odwołania, 4.1 Model danych, 8, Suplement A
   (słownik — propozycja w `SRS.md`), Suplement B (storytelling/makiety).

## SRS vs pakiety WBS (`Backend` / `Frontend`)
5. **Wymagania SRS bez zadań w pakietach** (zadania były czerwone/przekreślone, więc wypadły):
   - cele treningowe (WF-9.4–9.6),
   - karta statystyk i konfiguracja kart (WF-5.2–5.4), zapamiętanie sortowania (WF-6.6),
   - tryb wysokiego kontrastu (WF-12.8), tabela danych wykresu (WF-12.5), ostrzeżenie przed wygaśnięciem sesji (WF-12.14),
   - przewijanie kart przyciskami (WF-12.6), skalowanie tekstu 200% (WF-12.9).

   Wstążkę (WF-3.x) pokrywa zadanie „layout aplikacji i wstążka nawigacji” (F-2.1).
   Do decyzji: dopisać zadania do pakietów albo wyciąć wymagania z SRS.
6. **Brak zadań testów.** Wdrożenie i CI/CD nie są potrzebne (projekt lokalny).
7. **Usunąć z .docx punkty poza zakresem** (przekreślone w `SRS.md`): WF-1.2, WF-10.2, WF-10.5, UI-2.1.5 (nieaktywne
    konto), UI-3.2, UI-11.2.2–11.2.5, UI-11.3.2–11.3.4, aktywacja w IP-2, IP-7 (SMTP), IK-5, usuwanie konta w 4.3 i 2.2.
8. **Skutki pracy lokalnej do potwierdzenia w SRS:** OG-5 (dane w UE), IK-1 (HTTPS), atrybut `Secure` ciasteczek (IK-3)
    — przy uruchomieniu lokalnym bez HTTPS nie mają zastosowania albo wymagają doprecyzowania.
9. **Kolumna H (kto) pusta** — przypisać pakiety osobom.

## Ogólne
10. **Kalorie:** przyjęto ręczne wpisywanie. Alternatywa: szacowanie z formy, czasu i wagi z profilu (nowe wymaganie).
11. Terminy kamieni milowych M1–M7 od prowadzącego.

## Rozwiązane (2026-11-26)
- **Poza zakresem (decyzja zespołu):** e-mail aktywacyjny, zmiana hasła, usunięcie konta. Projekt działa lokalnie,
  bez wdrożenia — brak SMTP i wysyłki e-maili.
- Administrator usunięty z SRS (klasy: UŻ-1 niezalogowany, UŻ-2 zarejestrowany) — zgodne z WBS (`ROLE_USER`).
- Cele treningowe opisane w SRS (WF-9.4–9.6, UI-10.2) — ale patrz punkt 5.
- Filtrowanie historii ma osobną sekcję 3.11; podwójne „Home → filtrowanie listy aktywności” wypadło z pakietów.
- Reset hasła: wypadł z pakietów (zgodnie z IK-5). Zostaje tylko w oryginalnym arkuszu `WBS`.
- Zadania bez godzin: w pakietach nie ma już żadnego.
- Pozostałości w arkuszu (dawne wiersze 256–285) usunięte; skład zespołu wpisany w K2:N2.

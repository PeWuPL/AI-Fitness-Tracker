# Otwarte kwestie i niespójności

## Arkusz WBS (`estimates/WBS_SAMOZAMYKACZ_2026_2.xlsx`)
1. **Wiersze 3 i 9 nie mają godzin PW.** Etykiety szablonu Delphi zajmują ich komórki:
   J3 „ilość godzin szacowana indywidualnie” (zadanie: repozytorium, 0,5 h przed skróceniem)
   i J9:O9 „suma” (zadanie: konfiguracja JWT, 4 h przed skróceniem). Propozycja: przenieść etykiety
   nad tabelę i dopisać godziny (po skróceniu ×0,5: 0,5 h i 2 h).
2. **Wiersze 256–285 to prawdopodobnie pozostałość** po poprzedniej wersji (powielone tokeny, API,
   logowanie, bez kategorii nadrzędnej). Bez godzin, poza sumą. Do usunięcia.
3. **Możliwe podwójne liczenie filtrowania:** „Home → filtrowanie listy aktywności” oraz osobna gałąź
   „Filtrowanie historii aktywności”. Usunąć jedno z nich.
4. Nagłówek J2 nadal „Imię i Nazwisko” — wpisać „PW”. Kolumny K–N, O, H i kamienie milowe (A) do uzupełnienia.
5. W v2026_2 nie ma gałęzi testów, wdrożenia ani CI/CD (były w pierwszej wersji). Do decyzji, czy wracają.

## SRS vs WBS
6. **Cele treningowe** (WBS: O mnie → Cele treningowe: encja Cel, CRUD, obliczanie postępu, wyświetlanie postępu)
   nie mają jeszcze sekcji w SRS. Dopisać punkt 3.x i pojęcie w słowniku.
7. **Filtrowanie historii** jest w SRS jako WF-6.2; WBS ma je jako osobną gałąź z dodatkowymi wymaganiami
   (łączenie filtrów, czyszczenie, komunikat przy braku wyników) — rozważyć doprecyzowanie WF-6.x.
8. **Administrator:** SRS ma UŻ-3 i sekcję 3.11, ale WBS usunął gałąź administracji, a autoryzacja ma tylko
   `ROLE_USER`. Zdecydować: wyciąć administratora z SRS albo przywrócić w WBS.
9. **Kalorie:** przyjęto ręczne wpisywanie przez użytkownika. Alternatywa: szacowanie z formy ćwiczenia,
   czasu i wagi z profilu (wymagałoby nowego wymagania).

## Ogólne
10. Skład zespołu (osoby do kolumn J–N i H) i terminy etapów/kamieni milowych od prowadzącego.

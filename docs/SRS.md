# Specyfikacja wymagań (SRS) — aplikacja do mierzenia aktywności fizycznej (grupa SAMOZAMYKACZ)

> Kopia robocza dokumentu `SRS-SAMOZAMYKACZ_2026.docx` (stan z 2026-11-26). W razie rozbieżności wiążący
> jest plik .docx. Pominięto opisy szablonu; zostawiono pytania pomocnicze z odpowiedziami.
> Niespójności: `OPEN_ISSUES.md`.

---

## 1. Wprowadzenie

### 1.1 Cel
Celem dokumentu jest określenie wymagań dla aplikacji internetowej służącej do rejestrowania aktywności
fizycznej i przeglądania statystyk. Dokument opisuje funkcjonalności, użytkowników, wymagania i ograniczenia.
Jest przeznaczony dla zespołu projektowego oraz prowadzącego zajęcia i stanowi punkt odniesienia dla
implementacji oraz sprawdzenia poprawności systemu.

### 1.2 Przyjęte konwencje
- Punkty napisane kursywą (w .docx) to opis szablonu — nic się w nich nie wpisuje.
- Od sekcji 2.2 używamy identyfikatorów (np. UŻ-1, WF-1.1, UI-1.1, WN-1).

### 1.3 Zakres projektu
**Dla kogo wytwarzamy produkt?**
Dla osób aktywnych fizycznie, które chcą zapisywać treningi, przeglądać ich historię i obserwować postępy
na wykresach — zarówno regularnie ćwiczących, jak i nowicjuszy.

**Co to jest za produkt?**
Aplikacja internetowa do rejestrowania różnych form aktywności fizycznej i prezentowania danych na wykresach
i w statystykach.

**Jaki jest cel wytworzenia produktu?**
Gromadzenie informacji o ćwiczeniach w jednym miejscu i analiza własnej aktywności.

**Dlaczego użytkownik korzysta z naszego systemu?**
Aby zapisywać ćwiczenia, sprawdzać historię treningów i porównywać wyniki z różnych okresów.

**Cele główne**
- Rejestrowanie aktywności z rodzajem ćwiczenia, datą i uzyskaną wartością.
- Wykresy dopasowane do rodzaju aktywności.
- Przeglądanie, edycja i usuwanie historii treningów.
- Statystyki i podsumowania z wybranego okresu.

**Cele poboczne**
- Dostosowanie kolejności i widoczności kart z wykresami i statystykami.
- Filtrowanie historii według dat i rodzaju ćwiczenia.
- Zarządzanie własnymi formami ćwiczeń.

**Co jest niezbędne do zarabiania na produkcie?** Nie dotyczy.

### 1.4 Odwołania
(do uzupełnienia)

---

## 2. Opis ogólny

### 2.1 Perspektywa produktu
- Nowy produkt: tak, nowa aplikacja internetowa.
- Część większego systemu: nie, samodzielny system.

### 2.2 Klasy i charakterystyki użytkowników

**UŻ-1: Użytkownik niezalogowany**
Korzysta tylko z części publicznej. Może:
- przeglądać stronę główną i informacje o aplikacji,
- zapoznać się z polityką prywatności,
- założyć konto i zalogować się.

Nie ma dostępu do zapisywania aktywności, historii ani wykresów.

**UŻ-2: Użytkownik zarejestrowany**
Osoba aktywna fizycznie (regularnie trenująca lub początkująca). Po zalogowaniu może:
- uzupełniać i edytować profil,
- dodawać, edytować i usuwać własne formy ćwiczeń,
- rejestrować aktywności,
- przeglądać wykresy i statystyki,
- przeglądać, filtrować, edytować i usuwać historię aktywności,
- wyświetlać podsumowania z wybranego okresu oraz ustawiać i śledzić cele treningowe,
- dostosowywać kolejność i widoczność kart,
- zarządzać kontem (zmiana hasła, usunięcie konta) i wylogować się.

Każdy użytkownik ma dostęp wyłącznie do własnych danych.

### 2.3 Środowisko działania

**W jaki sposób użytkownik będzie używać systemu?**
- Aplikacja webowa w przeglądarce, bez aplikacji natywnej.
- Interfejs w pełni responsywny, mobile first (telefon, tablet, komputer).
- Przeglądarki: dwie ostatnie wersje Chrome, Firefox, Edge i Safari, także mobilne (Android, iOS).
- Niezależna od systemu operacyjnego; wymaga przeglądarki z JavaScriptem.
- Użytkownicy głównie w Polsce i UE. Interfejs po polsku, angielski jako opcjonalne rozszerzenie.

**Architektura systemu**
- Backend: PHP 8.x, Symfony.
- Frontend: Next.js (React, TypeScript), komunikacja z backendem przez REST API (API Platform).
- ORM: Doctrine.

**Baza danych**
- Relacyjna baza **SQLite**, obsługiwana przez Doctrine ORM i Doctrine Migrations.
- Główne dane: konta użytkowników, formy ćwiczeń, wpisy aktywności, cele treningowe, ustawienia kart.

### 2.4 Ograniczenia projektowe i wykonawcze

| ID | Ograniczenie | Uzasadnienie |
|---|---|---|
| OG-1 | Backend w PHP z frameworkiem Symfony | Wymóg zamawiającego. Laboratorium dotyczy backendu w PHP. |
| OG-2 | ORM Doctrine | Wymóg zamawiającego; standard w Symfony, niezależność od silnika bazy, migracje. |
| OG-3 | Frontend w Next.js (React, TypeScript) komunikujący się z REST API Symfony | Decyzja zespołu; Next.js to dopuszczony wariant SPA, zgodny z WBS. |
| OG-4 | Responsywny interfejs, mobile first | Wymóg zamawiającego; większość użycia na telefonie. |
| OG-5 | Zgodność z RODO: polityka prywatności, zgoda na ciasteczka, dane w UE | Wymóg prawny; dane o aktywności mogą być danymi o zdrowiu. |
| OG-6 | Model danych: zmienna (forma ćwiczeń) i obserwacje (co najmniej data i wartość) | Wymóg zamawiającego. |
| OG-7 | Wykresy z przybliżaniem i przesuwaniem w lewo i w prawo | Wymóg zamawiającego; ogranicza wybór biblioteki (np. Chart.js + zoom, ApexCharts). |
| OG-8 | Tematyka sportowa, wspólna dla grupy laboratoryjnej | Ustala prowadzący z grupą. |
| OG-9 | Technologie spoza listy wymagają zgody prowadzącego (Teams) | Spójność i ocenialność projektów. |

### 2.5 Założenia i zależności

**Podstawowe działanie użytkownika, jakie to działanie?**
Wprowadzenie danych o ćwiczeniu na ekranie „Mierzenie aktywności” i obejrzenie ich na wykresie w Menu głównym.

**Drugorzędne zadania, jakie to zadania?**
- przewijanie wykresu ulubionej aktywności z danego dnia,
- przesuwanie kart w Menu głównym i konfiguracja ich kolejności,
- przeglądanie historii aktywności z krótkim podsumowaniem, edycja i usuwanie wpisów,
- sortowanie historii po dacie, liczbie kroków lub spalonych kaloriach,
- podsumowanie ćwiczeń i śledzenie celów treningowych na ekranie „O mnie” ze zmianą okresu,
- zarządzanie kontem w panelu użytkownika i wylogowanie,
- rejestracja, logowanie i akceptacja ciasteczek.

**Tylko jedna metoda na osiągnięcie celu czy więcej?**
- Dodanie ćwiczenia: jedna metoda — formularz na ekranie „Mierzenie aktywności”.
- Przeglądanie postępów: kilka metod — karty w Menu głównym, historia aktywności, podsumowanie na ekranie „O mnie”.

**Zależności od czynników zewnętrznych**
- PHP 8.2+ i Composer; Symfony i Doctrine ORM,
- baza SQLite obsługiwana przez Doctrine ORM,
- Nginx lub Apache z PHP-FPM,
- Node.js i npm (budowanie / uruchomienie Next.js),
- Chart.js z obsługą przybliżania i przewijania,
- komponent przesuwanych kart (np. Swiper),
- opcjonalnie Docker i Docker Compose,
- przeglądarka z obsługą JavaScriptu i ciasteczek.

---

## 3. Funkcjonalności systemu

### 3.1 Rejestracja i logowanie
**3.1.1 Opis** — Zakładanie konta, logowanie i wylogowanie. Priorytet: **wysoki**

**3.1.2 Wymagania funkcjonalne**
- WF-1.1: System pozwala na rejestrację konta przy użyciu adresu e-mail i hasła.
- WF-1.2: System musi wysłać e-mail z linkiem aktywacyjnym. Bez aktywacji logowanie nie jest możliwe.
- WF-1.3: System musi odrzucić rejestrację, gdy e-mail jest zajęty albo hasło ma mniej niż 8 znaków, i wyświetlić komunikat.
- WF-1.4: System pozwala na logowanie e-mailem i hasłem. Przy błędnych danych pokazuje ogólny komunikat (bez ujawniania, czy konto istnieje).
- WF-1.5: System musi czasowo zablokować logowanie po 5 nieudanych próbach.

### 3.2 Część publiczna
**3.2.1 Opis** — Strona główna, polityka prywatności i zgoda na ciasteczka. Priorytet: **średni**

**3.2.2 Wymagania funkcjonalne**
- WF-2.1: System musi wyświetlić stronę główną z opisem aplikacji i odnośnikami do logowania i rejestracji.
- WF-2.2: System musi udostępniać stronę polityki prywatności.
- WF-2.3: System musi przy pierwszej wizycie wyświetlić baner zgody na ciasteczka i zapamiętać decyzję.
- WF-2.4: System nie może ustawiać ciasteczek innych niż niezbędne przed wyrażeniem zgody.

### 3.3 Nawigacja (wstążka)
**3.3.1 Opis** — Przełączanie ekranów części zamkniętej. Priorytet: **wysoki**

**3.3.2 Wymagania funkcjonalne**
- WF-3.1: System musi wyświetlać na dole ekranu wstążkę z trzema przyciskami: Menu główne (ikona domku), Mierzenie aktywności, O mnie.
- WF-3.2: System musi wyróżniać przycisk aktywnego ekranu.
- WF-3.3: System musi przekierować niezalogowanego użytkownika z części zamkniętej na stronę logowania.

### 3.4 Wykres ulubionej aktywności
**3.4.1 Opis** — Wykres ulubionej aktywności w ciągu dnia w Menu głównym. Priorytet: **wysoki**

**3.4.2 Wymagania funkcjonalne**
- WF-4.1: System musi wyświetlić w Menu głównym wykres ulubionej aktywności z bieżącego dnia.
- WF-4.2: System daje możliwość przewijania wykresu w lewo i w prawo (poprzednie/następne dni) i jego przybliżania.
- WF-4.3: System musi dobrać typ wykresu do formy ćwiczenia (np. liniowy dla dystansu, słupkowy dla powtórzeń).
- WF-4.4: Przy braku danych system musi wyświetlić komunikat „Brak aktywności” z odnośnikiem do ekranu Mierzenie aktywności.

### 3.5 Karty wykresów i statystyk
**3.5.1 Opis** — Karty z wykresami i statystykami w Menu głównym. Priorytet: **wysoki**

**3.5.2 Wymagania funkcjonalne**
- WF-5.1: System pozwala na przesuwanie kart gestem (swipe) lub strzałkami.
- WF-5.2: System musi udostępniać karty z wykresami pozostałych form ćwiczeń oraz kartę statystyk (suma, średnia, maksimum).
- WF-5.3: System daje możliwość zmiany kolejności kart oraz ich ukrywania i pokazywania.
- WF-5.4: System musi zapamiętać kolejność kart na koncie użytkownika.

### 3.6 Historia aktywności
**3.6.1 Opis** — Lista wykonanych aktywności z krótkim podsumowaniem, filtrowanie i sortowanie. Priorytet: **wysoki**

**3.6.2 Wymagania funkcjonalne**
- WF-6.1: System musi wyświetlić pod kartami listę aktywności; każdy wpis pokazuje formę, datę, wartość, liczbę kroków i spalone kalorie.
- WF-6.2: Historia udostępnia panel filtrowania (wymagania w sekcji 3.11).
- WF-6.3: System daje możliwość sortowania listy po dacie, liczbie kroków i spalonych kaloriach, rosnąco lub malejąco.
- WF-6.4: Domyślnie lista jest posortowana po dacie, od najnowszej.
- WF-6.5: Wpisy bez wartości w polu sortowania trafiają na koniec listy.
- WF-6.6: System musi zapamiętać ostatnio wybrane sortowanie użytkownika.
- WF-6.7: System musi odrzucić sortowanie po polu spoza listy dozwolonych i zastosować sortowanie domyślne.
- WF-6.8: System pozwala na edycję wpisu inline; błędne dane są odrzucane z komunikatem przy polu.
- WF-6.9: System pozwala na usunięcie wpisu po potwierdzeniu.
- WF-6.10: System musi odświeżyć wykresy po edycji lub usunięciu wpisu.

### 3.7 Mierzenie aktywności
**3.7.1 Opis** — Wprowadzanie danych o ćwiczeniu. Priorytet: **wysoki**

**3.7.2 Wymagania funkcjonalne**
- WF-7.1: System musi udostępniać formularz z polami: forma ćwiczenia (lista), data (domyślnie dzisiejsza), wartość; opcjonalnie liczba kroków, spalone kalorie (kcal), notatka.
- WF-7.2: System musi wyświetlić jednostkę wartości zgodną z wybraną formą (km, min, powtórzenia).
- WF-7.3: System musi odrzucić zapis, gdy pole wymagane jest puste, data jest z przyszłości albo wartość, kroki lub kalorie są ujemne lub nie są liczbą (kroki — liczba całkowita), i wskazać błędne pole.
- WF-7.4: System musi potwierdzić zapis komunikatem i wyczyścić formularz.

### 3.8 Zarządzanie formami ćwiczeń
**3.8.1 Opis** — Zmienne (formy ćwiczeń), do których przypisuje się obserwacje. Priorytet: **wysoki**

**3.8.2 Wymagania funkcjonalne**
- WF-8.1: System pozwala na dodanie formy ćwiczenia z nazwą, jednostką i typem wykresu.
- WF-8.2: System pozwala na edycję nazwy, jednostki i typu wykresu.
- WF-8.3: System pozwala na usunięcie formy; musi ostrzec, że zostaną usunięte także jej obserwacje.
- WF-8.4: System musi odrzucić formę o nazwie, która już istnieje na koncie użytkownika.

### 3.9 Podsumowanie okresowe i cele treningowe (O mnie)
**3.9.1 Opis** — Podsumowanie ćwiczeń w wybranym okresie. Priorytet: **średni**

**3.9.2 Wymagania funkcjonalne**
- WF-9.1: System musi wyświetlić podsumowanie bieżącego miesiąca: liczbę treningów i sumę wartości dla każdej formy.
- WF-9.2: System daje możliwość zmiany okresu na tydzień, miesiąc, rok lub zakres własny.
- WF-9.3: System musi odrzucić zakres, w którym data początkowa jest późniejsza niż końcowa.
- WF-9.4: System pozwala na ustawienie celu dla wybranej formy ćwiczenia (wartość docelowa i okres realizacji).
- WF-9.5: System musi wyświetlać postęp realizacji celu na podstawie zapisanych aktywności.
- WF-9.6: System pozwala na edycję i usunięcie celu.

### 3.10 Panel użytkownika
**3.10.1 Opis** — Ustawienia konta i wylogowanie. Priorytet: **średni**

**3.10.2 Wymagania funkcjonalne**
- WF-10.1: System pozwala na edycję danych profilu (imię, wiek, waga, wzrost).
- WF-10.2: System pozwala na zmianę hasła po podaniu obecnego hasła.
- WF-10.3: System pozwala na wybór ulubionej aktywności wyświetlanej na głównym wykresie.
- WF-10.4: System pozwala na wylogowanie.
- WF-10.5: System pozwala na usunięcie konta wraz ze wszystkimi danymi (RODO), po potwierdzeniu hasłem.

### 3.11 Filtrowanie historii aktywności
**3.11.1 Opis** — Wyszukiwanie zapisanych aktywności przez filtrowanie historii. Priorytet: **średni**

**3.11.2 Wymagania funkcjonalne**
- WF-11.1: System pozwala na filtrowanie historii według zakresu dat.
- WF-11.2: System pozwala na filtrowanie historii według formy ćwiczenia.
- WF-11.3: System umożliwia jednoczesne zastosowanie filtrów daty i formy ćwiczenia.
- WF-11.4: System pozwala na wyczyszczenie filtrów i ponowne wyświetlenie pełnej historii.
- WF-11.5: System musi wyświetlić komunikat, jeżeli żadna aktywność nie spełnia kryteriów.

### 3.12 Dostępność
**3.12.1 Opis** — Dostępność dla osób niewidomych, słabowidzących, z ograniczeniami ruchowymi i poznawczymi. Standard: WCAG 2.1, poziom AA. Priorytet: **wysoki**

**3.12.2 Wymagania funkcjonalne**
- WF-12.1: Pełna obsługa z klawiatury, logiczna kolejność fokusu, widoczny wskaźnik fokusu.
- WF-12.2: Link „Przejdź do treści” na początku każdej strony.
- WF-12.3: Semantyczny HTML i etykiety ARIA, poprawnie odczytywane przez czytnik ekranu.
- WF-12.4: Ogłaszanie komunikatów o zapisie, błędach i ładowaniu (aria-live).
- WF-12.5: Dane każdego wykresu dostępne także w formie tabeli.
- WF-12.6: Przełączanie kart przyciskami „poprzednia”/„następna”, nie tylko gestem.
- WF-12.7: Kontrast tekstu do tła co najmniej 4,5:1.
- WF-12.8: Tryb wysokiego kontrastu w panelu użytkownika.
- WF-12.9: Czytelność i funkcjonalność przy powiększeniu tekstu do 200%.
- WF-12.10: Informacja nie tylko kolorem (wzory/znaczniki na wykresach, ikona + tekst przy błędach).
- WF-12.11: Ograniczenie animacji przy ustawieniu prefers-reduced-motion.
- WF-12.12: Pola dotykowe co najmniej 44×44 px.
- WF-12.13: Widoczne etykiety pól; komunikat o błędzie powiązany z polem i mówiący, jak go poprawić.
- WF-12.14: Ostrzeżenie przed wygaśnięciem sesji z możliwością jej przedłużenia.
- WF-12.15: Informowanie czytnika ekranu o aktualnym sortowaniu (aria-sort).
- WF-12.16: Interfejs w języku polskim i angielskim.
- WF-12.17: Wykresy mają oznaczenia inne niż kolory (czytelność dla osób z daltonizmem).

---

## 4. Wymagania dotyczące danych

### 4.1 Logiczny model danych
(do uzupełnienia — diagram encji: Użytkownik, Forma ćwiczenia, Aktywność, Cel, Ustawienia kart)

### 4.2 Raporty
- **Wykresy i statystyki (Menu główne):** ulubiona aktywność z przewijaniem dni oraz karty z wykresami i statystykami.
- **Podsumowanie okresowe (O mnie):** liczba treningów i sumy wartości według form w wybranym okresie; postęp celów.
- **Historia aktywności (Menu główne):** lista aktywności z filtrowaniem po okresie i formie oraz sortowaniem po dacie, krokach i kaloriach.

### 4.3 Pozyskiwanie, integralność, przechowywanie i usuwanie danych
- **Pozyskiwanie:** użytkownik ręcznie wprowadza formę, datę i wartość, opcjonalnie kroki, kalorie i notatkę. Brak automatycznego pobierania z GPS i zegarków.
- **Integralność i przechowywanie:** baza SQLite przez Doctrine. Walidacja pól wymaganych, typów liczbowych, zakresów dat i relacji użytkownik–forma–aktywność.
- **Usuwanie:** użytkownik usuwa własne aktywności i cele oraz trwale usuwa konto z danymi po potwierdzeniu hasłem. Usunięcie formy usuwa jej obserwacje po ostrzeżeniu.

---

## 5. Wymagania dotyczące interfejsu zewnętrznego

### 5.1 Interfejsy użytkownika
Interfejs dostępny przez przeglądarkę, dostosowany do urządzeń mobilnych i komputerów; część publiczna i część dla zalogowanych.

**UI-1: Publiczna strona główna**
- UI-1.1 Nagłówek: nazwa/logo (1.1.1), przycisk „Zaloguj się” (1.1.2), przycisk „Zarejestruj się” (1.1.3).
- UI-1.2 Informacje o aplikacji: nazwa i krótki opis (1.2.1), główne możliwości systemu (1.2.2).
- UI-1.3 Stopka: odnośnik do polityki prywatności (1.3.1).

**UI-2: Ekran logowania**
- UI-2.1 Formularz: pole e-mail (2.1.1), pole hasła (2.1.2), przycisk „Zaloguj się” (2.1.3), komunikat błędnych danych (2.1.4), komunikat o nieaktywnym koncie lub czasowej blokadzie (2.1.5).
- UI-2.2 Nawigacja: odnośnik do rejestracji (2.2.1).

**UI-3: Ekran rejestracji**
- UI-3.1 Formularz: pole e-mail (3.1.1), pole hasła (3.1.2), przycisk „Zarejestruj się” (3.1.3), komunikaty: nieprawidłowy e-mail (3.1.4), hasło krótsze niż 8 znaków (3.1.5), zajęty e-mail (3.1.6).
- UI-3.2 Potwierdzenie: informacja o wysłaniu wiadomości aktywacyjnej (3.2.1), komunikat o poprawnej aktywacji (3.2.2).
- UI-3.3 Nawigacja: odnośnik do logowania (3.3.1).

**UI-4: Nawigacja części zamkniętej**
- UI-4.1 Dolny pasek: „Menu główne” z ikoną domu (4.1.1), „Mierzenie aktywności” (4.1.2), „O mnie” z ikoną użytkownika (4.1.3), wyróżnienie aktywnego ekranu (4.1.4).

**UI-5: Menu główne (Home)**
- UI-5.1 Wykres ulubionej aktywności: nazwa aktywności (5.1.1), wykres wartości (5.1.2), przyciski poprzedni/następny dzień (5.1.3–5.1.4), przybliżanie (5.1.5), komunikat „Brak aktywności” (5.1.6), odnośnik do dodawania aktywności (5.1.7).
- UI-5.2 Karty: wykresy pozostałych form (5.2.1), karta statystyk — suma, średnia, maksimum (5.2.2), przyciski przesuwania (5.2.3), zmiana kolejności (5.2.4), ukrywanie i pokazywanie (5.2.5).
- UI-5.3 Historia: lista aktywności (5.3.1), forma (5.3.2), data (5.3.3), wartość z jednostką (5.3.4), kroki i kalorie, jeśli podane (5.3.5), przejście do szczegółów (5.3.6).

**UI-6: Filtrowanie i sortowanie historii**
- UI-6.1 Panel filtrowania: data początkowa (6.1.1), data końcowa (6.1.2), forma ćwiczenia (6.1.3), „Zastosuj” (6.1.4), „Wyczyść” (6.1.5), komunikat o braku wyników (6.1.6).
- UI-6.2 Sortowanie: kryterium — data, kroki, kalorie (6.2.1), kolejność rosnąca/malejąca (6.2.2).

**UI-7: Szczegóły aktywności**
- UI-7.1 Informacje: forma (7.1.1), data (7.1.2), wartość z jednostką (7.1.3), kroki i kalorie (7.1.4), notatka (7.1.5).
- UI-7.2 Zarządzanie: przycisk edycji (7.2.1), pola edycji (7.2.2), zapis zmian (7.2.3), usunięcie (7.2.4), potwierdzenie usunięcia (7.2.5), komunikaty walidacyjne (7.2.6).

**UI-8: Mierzenie aktywności (Record)**
- UI-8.1 Formularz: forma ćwiczenia (8.1.1), data (8.1.2), wartość (8.1.3), etykieta jednostki (8.1.4), opcjonalnie kroki (8.1.5), kalorie (8.1.6), notatka (8.1.7), „Zapisz” (8.1.8).
- UI-8.2 Komunikaty: błędne lub brakujące dane (8.2.1), potwierdzenie zapisu (8.2.2).

**UI-9: Zarządzanie formami ćwiczeń**
- UI-9.1 Lista form: lista (9.1.1), dodaj (9.1.2), edytuj (9.1.3), usuń (9.1.4).
- UI-9.2 Formularz formy: nazwa (9.2.1), jednostka (9.2.2), typ wykresu (9.2.3), zapis (9.2.4), komunikat o istniejącej nazwie (9.2.5), ostrzeżenie o usunięciu obserwacji (9.2.6).

**UI-10: O mnie**
- UI-10.1 Podsumowanie okresowe: liczba treningów (10.1.1), wartości według form (10.1.2), wybór okresu — tydzień, miesiąc, rok (10.1.3), własny zakres dat (10.1.4), komunikat błędnego zakresu (10.1.5).
- UI-10.2 Cele treningowe: lista celów (10.2.1), dodaj cel (10.2.2), forma ćwiczenia (10.2.3), wartość docelowa (10.2.4), okres realizacji (10.2.5), zapis (10.2.6), wskaźnik postępu (10.2.7), edytuj (10.2.8), usuń (10.2.9).

**UI-11: Panel użytkownika**
- UI-11.1 Profil: imię (11.1.1), wiek (11.1.2), waga (11.1.3), wzrost (11.1.4), zapis (11.1.5).
- UI-11.2 Ustawienia: ulubiona aktywność (11.2.1), zmiana hasła (11.2.2), obecne hasło (11.2.3), nowe hasło (11.2.4), zatwierdzenie (11.2.5).
- UI-11.3 Konto: „Wyloguj się” (11.3.1), „Usuń konto” (11.3.2), potwierdzenie usunięcia (11.3.3), hasło do potwierdzenia (11.3.4).

**UI-12: Elementy wspólne**
- UI-12.1 Komunikaty i formularze: błędy przy polach (12.1.1), potwierdzenia operacji (12.1.2), potwierdzenia usuwania (12.1.3).
- UI-12.2 Dostępność i responsywność: układ dopasowany do ekranu (12.2.1), czytelne etykiety (12.2.2), oznaczenie aktywnych elementów (12.2.3), informacja na wykresach nie tylko kolorem (12.2.4), obsługa klawiaturą (12.2.5), tryb wysokiego kontrastu (12.2.6).

**UI-13: Polityka prywatności i ciasteczka**
- UI-13.1 Polityka prywatności: nagłówek (13.1.1), treść (13.1.2), powrót do części publicznej (13.1.3).
- UI-13.2 Baner ciasteczek: informacja (13.2.1), akceptacja opcjonalnych (13.2.2), odrzucenie opcjonalnych (13.2.3).

### 5.2 Interfejsy programowe
**Czy łączy się z jakimś API?**
- IP-1: Frontend Next.js komunikuje się z backendem Symfony przez REST API (API Platform), dane w JSON.
- IP-2: API obsługuje rejestrację i aktywację konta, logowanie, odświeżanie tokenów JWT, wylogowanie i operacje na profilu.
- IP-3: API udostępnia CRUD aktywności, form ćwiczeń, celów i preferencji kart oraz filtrowanie, sortowanie i statystyki okresowe.
- IP-4: Serwer waliduje dane wejściowe, sprawdza uprawnienia do własnych zasobów i zwraca czytelne odpowiedzi o powodzeniu lub błędzie.
- IP-5: Symfony używa Doctrine ORM do bazy SQLite (konta, aktywności, formy, cele, preferencje).
- IP-6: Chart.js z obsługą zoom prezentuje wykresy, Swiper obsługuje przewijanie kart.
- IP-7: Serwer wysyła e-maile aktywacyjne przez SMTP. Brak integracji z zewnętrznymi API sportowymi i urządzeniami pomiarowymi.
- IP-8: Tokeny JWT; po wygaśnięciu tokenu dostępowego sesja może być odnowiona ważnym tokenem odświeżania.

### 5.3 Interfejsy sprzętowe
**Z jakim sprzętem komunikuje się system?**
- IS-1: Przeglądarki na komputerach, tabletach i smartfonach z dostępem do Internetu.
- IS-2: Brak specjalistycznego sprzętu; brak komunikacji ze smartwatchami, opaskami i odbiornikami GPS.
- IS-3: Aktywność, kroki i kalorie wprowadzane ręcznie; brak odczytu z urządzeń zewnętrznych.

### 5.4 Interfejsy komunikacyjne
- IK-1: Komunikacja frontend–serwer przez HTTP/HTTPS; w środowisku dla użytkowników tylko HTTPS.
- IK-2: Standardowe metody HTTP (GET, POST, PATCH/PUT, DELETE), dane w JSON.
- IK-3: Uwierzytelnianie tokenami JWT; tokeny w ciasteczkach z atrybutami HttpOnly, Secure, SameSite; dostęp do danych prywatnych sprawdzany po stronie serwera.
- IK-4: Po wygaśnięciu tokenu frontend próbuje odświeżyć sesję; jeśli się nie da — przekierowuje do logowania.
- IK-5: Backend wysyła e-maile aktywacyjne przez SMTP. Nie przewiduje się e-maili resetu hasła.
- IK-6: Serwer zwraca komunikaty o wyniku operacji (w tym błędy walidacji i komunikacji); interfejs je wyświetla.
- IK-7: CORS ograniczony do uprawnionych źródeł frontendu.

---

## 6. Cechy jakości

### 6.1 Użyteczność
**Jakie udogodnienia dla osób z niepełnosprawnościami?**
- WN-1: Informacje na wykresach nie są przekazywane wyłącznie kolorem (daltonizm).
- WN-2: Rejestracja i dodanie pierwszego ćwiczenia są szybkie i nie wymagają instrukcji.
- WN-3: Elementy dotykowe w wersji mobilnej mają rozmiar wygodny do obsługi.

### 6.2 Wydajność
- WN-4: Zapis nowego wpisu trwa mniej niż 1 s.
- WN-5: Wykres z 1000 wpisów wyświetla się w mniej niż 2 s.
- WN-6: Strony ładują się w mniej niż 3 s.

### 6.3 Zabezpieczenia
- WN-7: Użytkownik ma dostęp wyłącznie do własnych danych.
- WN-8: Hasła przechowywane wyłącznie jako hashe.
- WN-9: Odporność na SQL injection, XSS i CSRF.

### 6.4 Bezpieczeństwo użytkowania
- WN-10: Aplikacja informuje, że statystyki nie zastępują porady lekarza lub trenera.
- WN-11: System nie sugeruje wartości niebezpiecznych dla zdrowia.

---

## 7. Wymagania internacjonalizacji i lokalizacji
**Czy system będzie obsługiwał inne języki / strefy czasowe / kultury?**
- WIL-1: Interfejs w języku polskim i angielskim.
- WIL-2: System działa w polskiej strefie czasowej.
- WIL-3: Daty w formacie dzień/miesiąc/rok, czas w zapisie 24-godzinnym.
- WIL-4: Jednostki w układzie metrycznym.

---

## 8. Inne wymagania
(brak)

---

## Suplement A: Słownictwo

> Sekcja w .docx jest jeszcze pusta — poniższy słownik jest propozycją do przeniesienia.

| Pojęcie | Definicja |
|---|---|
| Aktywność / obserwacja | Pojedynczy zapis ćwiczenia: data i wartość, opcjonalnie kroki, spalone kalorie, notatka. |
| Forma ćwiczenia / zmienna | Rodzaj aktywności (np. bieganie, rower). Ma nazwę, jednostkę i typ wykresu. |
| Cel treningowy | Wartość docelowa dla formy ćwiczenia w określonym okresie; postęp liczony z zapisanych aktywności. |
| Ulubiona aktywność | Forma ćwiczenia, której wykres wyświetla się jako pierwszy w Menu głównym. |
| Jednostka | Miara wartości obserwacji (km, min, powtórzenia). |
| Kroki | Liczba kroków w czasie aktywności (liczba całkowita, opcjonalna). |
| Spalone kalorie | Szacunkowa energia wydatkowana w czasie aktywności, w kcal (opcjonalna). |
| Filtrowanie | Zawężenie historii do aktywności z wybranego zakresu dat i/lub formy ćwiczenia. |
| Sortowanie | Ustalenie kolejności listy według pola (data, kroki, kalorie), rosnąco lub malejąco. |
| Karta | Przesuwany panel w Menu głównym z wykresem lub statystykami. |
| Wstążka | Stały pasek nawigacji na dole ekranu (Menu główne, Mierzenie aktywności, O mnie). |
| Menu główne (Home) | Ekran startowy części zamkniętej: wykres ulubionej aktywności, karty, historia. |
| Mierzenie aktywności (Record) | Ekran z formularzem wprowadzania obserwacji. |
| O mnie | Ekran z podsumowaniem okresowym, celami treningowymi i panelem użytkownika. |
| Historia aktywności | Lista zapisanych obserwacji z krótkim podsumowaniem. |
| Podsumowanie okresowe | Zestawienie ćwiczeń w wybranym okresie (domyślnie miesiąc). |
| Część publiczna / zamknięta | Strony dostępne bez logowania / tylko po zalogowaniu. |
| Użytkownik niezalogowany / zarejestrowany | Klasy użytkowników UŻ-1 / UŻ-2. |
| Kamień milowy | Punkt kontrolny w harmonogramie oznaczający ukończenie etapu. |
| SRS | Software Requirements Specification — specyfikacja wymagań oprogramowania. |
| SIWZ | Specyfikacja Istotnych Warunków Zamówienia — wymagania prowadzącego. |
| WBS | Work Breakdown Structure — hierarchiczny podział prac. |
| Metoda Delphi | Szacowanie pracochłonności: oceny indywidualne, potem uzgodnienie w grupie. |
| SPA | Aplikacja jednostronicowa (renderowana w przeglądarce). |
| API REST | Interfejs komunikacji frontendu z backendem przez HTTP i JSON. |
| CRUD | Create, Read, Update, Delete. |
| ORM | Mapowanie obiektowo-relacyjne (Doctrine). |
| SQLite | Plikowa relacyjna baza danych używana przez aplikację. |
| JWT | JSON Web Token — token uwierzytelniający żądania do API. |
| CORS | Mechanizm zezwalający frontendowi na żądania do API pod innym adresem. |
| SMTP | Protokół wysyłki e-maili (wiadomości aktywacyjne). |
| Responsywność / mobile first | Dopasowanie interfejsu do ekranu, projektowane najpierw dla telefonu. |
| Edycja inline | Edycja danych bezpośrednio na liście. |
| RODO / GDPR | Rozporządzenie UE o ochronie danych osobowych. |
| WCAG 2.1 AA | Wytyczne dostępności treści internetowych, poziom AA. |
| ARIA | Atrybuty HTML opisujące elementy dla technologii asystujących. |
| Czytnik ekranu | Program odczytujący treść ekranu (NVDA, VoiceOver, TalkBack). |
| Fokus | Wskazanie elementu, który odbiera dane z klawiatury. |

## Suplement B: Modele analityczne
(do uzupełnienia — storytelling / makiety)

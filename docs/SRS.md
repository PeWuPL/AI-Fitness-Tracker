# Nieformalny SRS — aplikacja do mierzenia aktywności fizycznej (grupa SAMOZAMYKACZ)

> Wersja skonsolidowana z sesji roboczej. Obejmuje sekcje 2.2–2.5, 3 oraz słownik.
> Otwarte kwestie: `OPEN_ISSUES.md`.

---

## 2.2 Klasy i charakterystyki użytkowników

**UŻ-1: Użytkownik główny (osoba aktywna fizycznie)**
Osoba mierząca swoją aktywność fizyczną. Może:
- założyć konto i uzupełnić profil (wiek, waga, wzrost, cel),
- ręcznie wprowadzać obserwacje (data, wartość, opcjonalnie kroki, spalone kalorie, notatka),
- tworzyć, edytować i usuwać formy ćwiczeń (bieganie, rower, pływanie, siłownia itd.),
- przeglądać wykresy dla każdej formy ćwiczeń (filtrowanie po datach, przybliżanie, przesuwanie),
- przeglądać, sortować, edytować i usuwać swoje obserwacje.

**UŻ-2: Gość (użytkownik niezalogowany)**
Ma dostęp tylko do części publicznej: strony głównej, logowania i rejestracji oraz polityki prywatności.
Może założyć konto i zaakceptować ciasteczka. Nie może zapisywać danych.

**UŻ-3: Administrator**
Odpowiada za utrzymanie systemu. Nie ma wglądu w szczegółowe dane użytkowników, chyba że wymaga
tego obsługa zgłoszenia. Może:
- zarządzać kontami (blokowanie, usuwanie, reset dostępu),
- zarządzać domyślnym słownikiem form ćwiczeń,
- przeglądać logi i statystyki użycia.

---

## 2.3 Środowisko działania

**Sposób korzystania z systemu**
- Aplikacja webowa w przeglądarce, bez aplikacji natywnej.
- Interfejs w pełni responsywny, projektowany w podejściu mobile first (telefon, tablet, komputer).
- Obsługiwane przeglądarki: dwie ostatnie wersje Chrome, Firefox, Edge i Safari, także mobilne (Android, iOS).
- Niezależna od systemu operacyjnego; wymaga przeglądarki z włączonym JavaScriptem.
- Użytkownicy głównie w Polsce i UE. Interfejs po polsku (angielski opcjonalnie).

**Architektura i technologie**
- Backend: PHP 8.2+, Symfony, API Platform (REST API, JSON).
- Frontend: Next.js (React, TypeScript) jako SPA komunikujące się z API.
- ORM: Doctrine.

**Baza danych**
- PostgreSQL (alternatywnie MySQL/MariaDB), Doctrine ORM + Doctrine Migrations.
- Główne dane: użytkownicy, formy ćwiczeń (zmienne), obserwacje (aktywności).

**Serwer i hosting**
- Serwer linuksowy, Nginx + PHP-FPM dla API, serwer Node.js dla Next.js, opcjonalnie Docker.
- Serwery i baza danych w UE (RODO). Cała komunikacja przez HTTPS.

**Współpracujące składniki**
- Biblioteka wykresów z przybliżaniem i przesuwaniem (Chart.js + wtyczka zoom lub ApexCharts).
- Biblioteka przesuwanych kart (np. Swiper).
- Mechanizm zgody na ciasteczka (RODO).
- Serwer SMTP (potwierdzenie rejestracji, reset hasła).

---

## 2.4 Ograniczenia projektowe i wykonawcze

| ID | Ograniczenie | Uzasadnienie |
|---|---|---|
| OG-1 | Backend w PHP z frameworkiem Symfony | Wymóg zamawiającego (laboratorium dotyczy backendu w PHP). |
| OG-2 | ORM Doctrine | Wymóg zamawiającego; standard w Symfony, niezależność od silnika bazy, migracje. |
| OG-3 | Frontend jako SPA w Next.js (backend w Symfony) | SIWZ dopuszcza SPA; zespół wybrał Next.js. |
| OG-4 | Responsywny interfejs, mobile first | Wymóg zamawiającego; większość użycia na telefonie. |
| OG-5 | Zgodność z RODO: polityka prywatności, zgoda na ciasteczka, dane w UE | Wymóg prawny; dane o aktywności mogą być danymi o zdrowiu. |
| OG-6 | Model danych: zmienna (forma ćwiczenia) i obserwacje (co najmniej data i wartość) | Wymóg zamawiającego. |
| OG-7 | Wykresy z przybliżaniem i przesuwaniem w lewo/prawo | Wymóg zamawiającego; ogranicza wybór biblioteki wykresów. |
| OG-8 | Tematyka sportowa, wspólna dla grupy laboratoryjnej | Ustalone przez prowadzącego z grupą. |
| OG-9 | Technologie spoza listy wymagają zgody prowadzącego (Teams) | Spójność i ocenialność projektów. |

---

## 2.5 Założenia i zależności

**Sprawdzić SIWZ**
System ma część publiczną (strona główna, logowanie i rejestracja, polityka prywatności, zgoda na
ciasteczka) i zamkniętą. Część zamknięta ma trzy ekrany przełączane wstążką na dole ekranu: Menu główne,
Mierzenie aktywności i O mnie. Każda obserwacja zawiera co najmniej datę i wartość; opcjonalnie liczbę
kroków, spalone kalorie i notatkę. Każdy użytkownik widzi i modyfikuje wyłącznie swoje dane.

**Podstawowe działanie użytkownika, jakie to działanie?**
Wprowadzenie danych o ćwiczeniu na ekranie „Mierzenie aktywności” i obejrzenie ich na wykresie w Menu głównym.

**Drugorzędne zadania, jakie to zadania?**
- przewijanie wykresu ulubionej aktywności z danego dnia,
- przesuwanie kart w Menu głównym (inne wykresy, statystyki) i konfiguracja ich kolejności,
- przeglądanie historii aktywności z krótkim podsumowaniem, edycja i usuwanie wpisów,
- sortowanie historii po dacie, liczbie kroków lub spalonych kaloriach,
- podsumowanie ćwiczeń na ekranie „O mnie” ze zmianą okresu (domyślnie miesiąc),
- zarządzanie kontem w panelu użytkownika i wylogowanie,
- rejestracja, logowanie i akceptacja ciasteczek.

**Tylko jedna metoda na osiągnięcie celu czy więcej?**
- Dodanie ćwiczenia: jedna metoda — formularz na ekranie „Mierzenie aktywności”.
- Przeglądanie postępów: kilka metod — karty w Menu głównym, historia aktywności, podsumowanie na ekranie „O mnie”.

**Zależności od czynników zewnętrznych**
- PHP 8.2+ i Composer; Symfony, API Platform, Doctrine ORM,
- serwer bazy danych PostgreSQL (lub MySQL/MariaDB),
- Nginx (lub Apache) z PHP-FPM, certyfikat SSL,
- Node.js i npm (budowanie i uruchomienie Next.js),
- biblioteka wykresów (Chart.js + zoom lub ApexCharts), biblioteka kart (np. Swiper),
- serwer SMTP,
- opcjonalnie Docker i Docker Compose,
- przeglądarka z obsługą JavaScriptu i ciasteczek.

---

## 3. Funkcjonalności systemu

Wymagania pogrupowane według obszarów funkcjonalnych, w kolejności ekranów aplikacji.

### 3.1 Rejestracja i logowanie
**3.1.1 Opis** — Funkcjonalność odpowiada za zakładanie konta, logowanie, wylogowanie i reset hasła. Priorytet: **wysoki**

**3.1.2 Wymagania funkcjonalne**
- WF-1.1: System pozwala na rejestrację konta przy użyciu adresu e-mail i hasła.
- WF-1.2: System musi wysłać e-mail z linkiem aktywacyjnym. Bez aktywacji logowanie nie jest możliwe.
- WF-1.3: System musi odrzucić rejestrację, gdy e-mail jest zajęty albo hasło ma mniej niż 8 znaków, i wyświetlić komunikat.
- WF-1.4: System pozwala na logowanie e-mailem i hasłem. Przy błędnych danych pokazuje ogólny komunikat (bez ujawniania, czy konto istnieje).
- WF-1.5: System daje możliwość resetu hasła przez link wysłany e-mailem, ważny 1 godzinę.
- WF-1.6: System musi czasowo zablokować logowanie po 5 nieudanych próbach.

### 3.2 Część publiczna
**3.2.1 Opis** — Funkcjonalność odpowiada za stronę główną, politykę prywatności i zgodę na ciasteczka. Priorytet: **średni**

**3.2.2 Wymagania funkcjonalne**
- WF-2.1: System musi wyświetlić stronę główną z opisem aplikacji i odnośnikami do logowania i rejestracji.
- WF-2.2: System musi udostępniać stronę polityki prywatności.
- WF-2.3: System musi przy pierwszej wizycie wyświetlić baner zgody na ciasteczka i zapamiętać decyzję.
- WF-2.4: System nie może ustawiać ciasteczek innych niż niezbędne przed wyrażeniem zgody.

### 3.3 Nawigacja (wstążka)
**3.3.1 Opis** — Funkcjonalność odpowiada za przełączanie ekranów części zamkniętej. Priorytet: **wysoki**

**3.3.2 Wymagania funkcjonalne**
- WF-3.1: System musi wyświetlać na dole ekranu wstążkę z przyciskami: Menu główne (ikona domku), Mierzenie aktywności, O mnie.
- WF-3.2: System musi wyróżniać przycisk aktywnego ekranu.
- WF-3.3: System musi przekierować niezalogowanego użytkownika z części zamkniętej na stronę logowania.

### 3.4 Wykres ulubionej aktywności
**3.4.1 Opis** — Funkcjonalność odpowiada za wykres ulubionej aktywności w ciągu dnia w Menu głównym. Priorytet: **wysoki**

**3.4.2 Wymagania funkcjonalne**
- WF-4.1: System musi wyświetlić w Menu głównym wykres ulubionej aktywności z bieżącego dnia.
- WF-4.2: System daje możliwość przewijania wykresu (poprzednie/następne dni) i jego przybliżania.
- WF-4.3: System musi dobrać typ wykresu do formy ćwiczenia (np. liniowy dla dystansu, słupkowy dla powtórzeń).
- WF-4.4: Przy braku danych system musi wyświetlić komunikat „Brak aktywności” z odnośnikiem do ekranu Mierzenie aktywności.

### 3.5 Karty wykresów i statystyk
**3.5.1 Opis** — Funkcjonalność odpowiada za przesuwane karty z wykresami i statystykami w Menu głównym. Priorytet: **średni**

**3.5.2 Wymagania funkcjonalne**
- WF-5.1: System pozwala na przesuwanie kart gestem (swipe) lub strzałkami.
- WF-5.2: System musi udostępniać karty z wykresami pozostałych form ćwiczeń oraz kartę statystyk (suma, średnia, maksimum).
- WF-5.3: System daje możliwość zmiany kolejności kart oraz ich ukrywania i pokazywania.
- WF-5.4: System musi zapamiętać kolejność kart na koncie użytkownika.

### 3.6 Historia aktywności
**3.6.1 Opis** — Funkcjonalność odpowiada za listę wykonanych aktywności z krótkim podsumowaniem, jej filtrowanie i sortowanie. Priorytet: **wysoki**

**3.6.2 Wymagania funkcjonalne**
- WF-6.1: System musi wyświetlić pod kartami listę aktywności; każdy wpis pokazuje formę, datę, wartość, liczbę kroków i spalone kalorie.
- WF-6.2: System daje możliwość filtrowania listy po zakresie dat i formie ćwiczenia.
- WF-6.3: System daje możliwość sortowania listy po dacie, liczbie kroków i spalonych kaloriach, rosnąco lub malejąco.
- WF-6.4: Domyślnie lista jest posortowana po dacie, od najnowszej.
- WF-6.5: Wpisy bez wartości w polu sortowania trafiają na koniec listy.
- WF-6.6: System musi zapamiętać ostatnio wybrane sortowanie użytkownika.
- WF-6.7: System musi odrzucić sortowanie po polu spoza listy dozwolonych i zastosować sortowanie domyślne.
- WF-6.8: System pozwala na edycję wpisu inline; błędne dane są odrzucane z komunikatem przy polu.
- WF-6.9: System pozwala na usunięcie wpisu po potwierdzeniu.
- WF-6.10: System musi odświeżyć wykresy po edycji lub usunięciu wpisu.

### 3.7 Mierzenie aktywności
**3.7.1 Opis** — Funkcjonalność odpowiada za wprowadzanie danych o ćwiczeniu. Priorytet: **wysoki**

**3.7.2 Wymagania funkcjonalne**
- WF-7.1: System musi udostępniać formularz z polami: forma ćwiczenia (lista), data (domyślnie dzisiejsza), wartość; opcjonalnie liczba kroków, spalone kalorie (kcal), notatka.
- WF-7.2: System musi wyświetlić jednostkę wartości zgodną z wybraną formą (km, min, powtórzenia).
- WF-7.3: System musi odrzucić zapis, gdy pole wymagane jest puste, data jest z przyszłości albo wartość, kroki lub kalorie są ujemne lub nie są liczbą (kroki — liczba całkowita), i wskazać błędne pole.
- WF-7.4: System musi potwierdzić zapis komunikatem i wyczyścić formularz.

### 3.8 Zarządzanie formami ćwiczeń
**3.8.1 Opis** — Funkcjonalność odpowiada za zmienne (formy ćwiczeń), do których przypisuje się obserwacje. Priorytet: **wysoki**

**3.8.2 Wymagania funkcjonalne**
- WF-8.1: System pozwala na dodanie formy ćwiczenia z nazwą, jednostką i typem wykresu.
- WF-8.2: System pozwala na edycję nazwy, jednostki i typu wykresu.
- WF-8.3: System pozwala na usunięcie formy; musi ostrzec, że zostaną usunięte także jej obserwacje.
- WF-8.4: System musi odrzucić formę o nazwie, która już istnieje na koncie użytkownika.

### 3.9 Podsumowanie okresowe (O mnie)
**3.9.1 Opis** — Funkcjonalność odpowiada za podsumowanie ćwiczeń w wybranym okresie. Priorytet: **średni**

**3.9.2 Wymagania funkcjonalne**
- WF-9.1: System musi wyświetlić podsumowanie bieżącego miesiąca: liczbę treningów i sumę wartości dla każdej formy.
- WF-9.2: System daje możliwość zmiany okresu na tydzień, miesiąc, rok lub zakres własny.
- WF-9.3: System musi odrzucić zakres, w którym data początkowa jest późniejsza niż końcowa.

### 3.10 Panel użytkownika
**3.10.1 Opis** — Funkcjonalność odpowiada za ustawienia konta i wylogowanie. Priorytet: **średni**

**3.10.2 Wymagania funkcjonalne**
- WF-10.1: System pozwala na edycję danych profilu (imię, wiek, waga, wzrost).
- WF-10.2: System pozwala na zmianę hasła po podaniu obecnego hasła.
- WF-10.3: System pozwala na wybór ulubionej aktywności wyświetlanej na głównym wykresie.
- WF-10.4: System pozwala na wylogowanie.
- WF-10.5: System pozwala na usunięcie konta wraz ze wszystkimi danymi (RODO), po potwierdzeniu hasłem.

### 3.11 Administracja
**3.11.1 Opis** — Funkcjonalność odpowiada za zarządzanie kontami i domyślnym słownikiem form ćwiczeń. Priorytet: **niski**

**3.11.2 Wymagania funkcjonalne**
- WF-11.1: System pozwala administratorowi przeglądać listę kont (e-mail, data rejestracji, status).
- WF-11.2: System pozwala administratorowi blokować, odblokowywać i usuwać konta.
- WF-11.3: System pozwala administratorowi zarządzać domyślnymi formami ćwiczeń dla nowych kont.
- WF-11.4: System nie może dawać administratorowi wglądu w obserwacje użytkowników.

### 3.12 Dostępność
**3.12.1 Opis** — Funkcjonalność odpowiada za dostępność dla osób z niepełnosprawnościami (niewidomych, słabowidzących, z ograniczeniami ruchowymi i poznawczymi). Standard: WCAG 2.1, poziom AA. Priorytet: **wysoki**

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

---

## Słownik pojęć

| Pojęcie | Definicja |
|---|---|
| Aktywność / obserwacja | Pojedynczy zapis ćwiczenia: data i wartość, opcjonalnie kroki, spalone kalorie, notatka. |
| Forma ćwiczenia / zmienna | Rodzaj aktywności (np. bieganie, rower). Ma nazwę, jednostkę i typ wykresu. |
| Ulubiona aktywność | Forma ćwiczenia, której wykres wyświetla się jako pierwszy w Menu głównym. |
| Jednostka | Miara wartości obserwacji (km, min, powtórzenia). |
| Kroki | Liczba kroków w czasie aktywności (liczba całkowita, opcjonalna). |
| Spalone kalorie | Szacunkowa energia wydatkowana w czasie aktywności, w kcal (opcjonalna). |
| Sortowanie | Ustalenie kolejności listy według pola (data, kroki, kalorie), rosnąco lub malejąco. |
| Karta | Przesuwany panel w Menu głównym z wykresem lub statystykami. |
| Wstążka | Stały pasek nawigacji na dole ekranu (Menu główne, Mierzenie aktywności, O mnie). |
| Menu główne (Home) | Ekran startowy części zamkniętej: karty wykresów i historia aktywności. |
| Mierzenie aktywności (Record) | Ekran z formularzem wprowadzania obserwacji. |
| O mnie | Ekran z podsumowaniem okresowym i panelem użytkownika. |
| Historia aktywności | Lista zapisanych obserwacji z krótkim podsumowaniem. |
| Podsumowanie okresowe | Zestawienie ćwiczeń w wybranym okresie (domyślnie miesiąc). |
| Część publiczna / zamknięta | Strony dostępne bez logowania / tylko po zalogowaniu. |
| Gość | Użytkownik niezalogowany. |
| Administrator | Użytkownik zarządzający kontami i domyślnym słownikiem form ćwiczeń. |
| Kamień milowy | Punkt kontrolny w harmonogramie oznaczający ukończenie etapu. |
| SRS | Software Requirements Specification — specyfikacja wymagań oprogramowania. |
| SIWZ | Specyfikacja Istotnych Warunków Zamówienia — wymagania prowadzącego. |
| WBS | Work Breakdown Structure — hierarchiczny podział prac. |
| Metoda Delphi | Szacowanie pracochłonności: oceny indywidualne, potem uzgodnienie w grupie. |
| MVP | Minimum Viable Product — minimalna działająca wersja (Record + Home). |
| SPA / MPA | Aplikacja jednostronicowa (renderowana w przeglądarce) / wielostronicowa (renderowana na serwerze). |
| API REST | Interfejs komunikacji frontendu z backendem przez HTTP i JSON. |
| CRUD | Create, Read, Update, Delete. |
| ORM | Mapowanie obiektowo-relacyjne (Doctrine). |
| JWT | JSON Web Token — token uwierzytelniający żądania do API. |
| CORS | Mechanizm zezwalający frontendowi na żądania do API pod innym adresem. |
| Responsywność / mobile first | Dopasowanie interfejsu do ekranu, projektowane najpierw dla telefonu. |
| Edycja inline | Edycja danych bezpośrednio na liście. |
| RODO / GDPR | Rozporządzenie UE o ochronie danych osobowych. |
| WCAG 2.1 AA | Wytyczne dostępności treści internetowych, poziom AA. |
| ARIA | Atrybuty HTML opisujące elementy dla technologii asystujących. |
| Czytnik ekranu | Program odczytujący treść ekranu (NVDA, VoiceOver, TalkBack). |
| Fokus | Wskazanie elementu, który odbiera dane z klawiatury. |

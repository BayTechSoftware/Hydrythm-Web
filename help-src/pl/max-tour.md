---
title: Ekran główny Cora Max
description: Co oznaczają górny pasek, etykieta stanu, etykiety alertów, menu akwarium i pulpit na Cora Max oraz jak przełączać akwaria i otwierać Gniazda i karmienie.
section: Cora Max
reviewed: 2026-10-13
order: 2
group: Getting started
twin: mobile-tour
---

Ta strona wyjaśnia, co widzisz na Cora Max. Pokazuje on jedno akwarium naraz, a odczyty na żywo wypełniają ekran, więc przeczytasz je z drugiego końca pokoju.

![Ekran główny Cora Max ze wskaźnikami, wartościami, wykresami i kafelkami urządzeń jednego akwarium pod górnym paskiem](img/max-home.webp "Pulpit jednego akwarium wypełnia ekran, a nad nim jest górny pasek.")

## Górny pasek {#the-top-bar}

![Górny pasek Cora Max](img/max-topbar.webp "Górny pasek, ponumerowany od lewej do prawej zgodnie z listą poniżej.")

Od lewej do prawej:

1. **Ikona siatki** otwiera [Reef Room](/help/max-reef-room), przegląd wszystkich akwariów, które pokazuje ten ekran.
2. **Nazwa akwarium** z małą strzałką. Dotknij jej, żeby otworzyć **menu akwarium** ze wszystkimi ekranami dla oglądanego akwarium. Pełna lista jest niżej.
3. **Etykiety alertów** pokazują, co teraz wymaga uwagi: odczyty poza zakresem, usterki urządzeń, pominięte dawki albo kończące się zasoby. Dotknij etykiety, żeby przywrócić ten alert na środek ekranu. Jeśli wszystkie się nie mieszczą, zobaczysz **+2** (albo inną liczbę). Dotknij tego, żeby zobaczyć wszystkie aktywne alarmy.
4. **Zegar**. Możesz go ukryć przełącznikiem **Pokaż zegar** w **Ustawienia → Ustawienia Cora Max**.
5. **Etykieta stanu** pokazuje, co ten ekran teraz robi. Zielona oznacza, że wszystko w porządku, niebieska, że ekran jest zajęty, bursztynowa, że coś warto sprawdzić, a czerwona oznacza usterkę. Wszystkie stany są wymienione niżej.
6. **Bateria i Wi-Fi**.
7. **Ikona urządzeń** otwiera **Urządzenia**, przefiltrowane do tego akwarium. Akwarium bez urządzeń jej nie pokazuje.
8. **Ikona Reef Buddy** otwiera dzisiejsze podsumowanie. Kropka oznacza, że jeszcze go nie przeczytano.
9. **Ikona Cora Assistant** zaczyna rozmowę głosową.
10. **Koło zębate** otwiera ustawienia.

:::warning Cora Assistant od razu zaczyna słuchać
Dotknięcie ikony Cora Assistant zaczyna sesję głosową na żywo. Jeśli chodziło o ustawienia, to koło zębate po prawej stronie.
:::

### Co oznacza etykieta stanu {#what-the-status-pill-means}

| Etykieta | Znaczenie |
|---|---|
| **Online** | Ten ekran zbiera Twoje odczyty i są one aktualne |
| **Chmura** | Odczyty tego akwarium zbiera inne urządzenie Cora, a ten ekran je pokazuje. Są tak samo aktualne jak przy **Online**. Jeśli masz więcej niż jedno urządzenie Cora, ten stan pokazuje to, które nie zbiera |
| **Odpytywanie Apex**, **Głos aktywny** | Ekran właśnie czymś się zajmuje (niebieska) |
| **Odpytywanie wyłączone** | Zbieranie odczytów jest wyłączone dla tego akwarium. Możesz je włączyć z powrotem w Cora Mobile |
| **Aktualizowanie** | Zbieranie jest wstrzymane na czas instalacji aktualizacji |
| **Nieaktualne** | Odczyty przestały napływać. Ekran pokazuje ostatnie, które dostał |
| **Ponowna próba Apex 12 s** | Apex nie odpowiedział. Cora Max spróbuje ponownie, gdy skończy się odliczanie |
| **Synchronizacja z chmurą nie powiodła się** | Apex odpowiedział, ale jego odczytów nie udało się zapisać w Cora Cloud, więc pulpit zostaje w tyle. Cora Max dalej próbuje |
| **Zapis w chmurze odrzucony** | Cora Cloud odmawia zapisania części danych z tego ekranu. Z Twoim akwarium ani z Cora Max nic złego się nie dzieje i nic nie trzeba zmieniać na tym ekranie. Rozwiązaniem jest aktualizacja Cora Cloud. Otwórz **Ustawienia → Ustawienia Cora Max** i przewiń do sekcji **Stan**, gdzie linia **Zapis w chmurze** mówi, których danych to dotyczy. Potem [skontaktuj się z pomocą techniczną](/support.html) |
| **Offline** | Brak połączenia. Ekran pokazuje ostatnie dane, które dostał |
| **Offline, ponowna próba za 45 s** | Sieć działa, ale Cora Cloud jest niedostępna od ponad 30 sekund. Cora Max połączy się ponownie sam, a odliczanie pokazuje, kiedy spróbuje następnym razem |
| **Główne Cora offline** | Ten ekran to drugi Cora Max dla tego akwarium, a **Główne Cora Max** (to przypięte do odczytywania sprzętu tego akwarium) przeszło w tryb offline. Ten ekran pokazuje ostatnie dane, dopóki główne nie wróci albo nie wybierzesz innego Głównego Cora Max. Więcej w [Więcej niż jedno urządzenie Cora](/help/mobile-multi-device) |
| **Hasło Apex** | Twój Apex odrzucił zapisane hasło. Zajrzyj do [Rozwiązywania problemów](/help/troubleshooting) |

:::note Jak działa odliczanie ponownych prób
Cora Max próbuje połączyć się ponownie w stałym rytmie. Czeka około 15 sekund po pierwszym zerwaniu, potem znowu 15 sekund, potem dwa razy 30 sekund, a dalej raz na minutę, aż się uda. Nigdy się nie poddaje. **Offline, ponowna próba za 45 s** to normalny stan.
:::

## Pulpit {#the-dashboard}

Resztę ekranu zajmuje pulpit, stała siatka, w której widać każdy widżet. Nie przewija się.

Widżety działają tak samo jak w telefonie, ale są na tyle duże, że przeczytasz je z kilku kroków. Co pokazuje każdy kształt, opisują [Rodzaje widżetów](/help/mobile-widgets). Żeby zmienić zawartość pulpitu, zobacz [Edytowanie pulpitu Cora Max](/help/max-dashboard-editing).

Każdy widżet z mierzonym parametrem pokazuje **wiek** i **źródło**, tak jak w telefonie. Liczba z `2d` obok ma dwa dni. Kafelki urządzeń i sterowania pokazują zamiast tego swój stan.

### Gdy ekran jest przyciemniony {#when-the-screen-is-dimmed}

Po czasie **Przygaszaj po** bez dotyku ekran się przyciemnia. Pierwsze dotknięcie tylko go wybudza, więc nie naciśnie przypadkiem żadnego elementu sterowania. Dotknij ponownie, żeby korzystać z ekranu.

## Menu akwarium {#the-tank-menu}

![Menu akwarium otwarte nad pulpitem, z pozycjami Zapisz parametry, Dziennik, Reef Buddy i innymi ekranami akwarium](img/max-menu.webp "Menu akwarium, otwarte z nazwy akwarium na górnym pasku.")

Dotknij nazwy akwarium, żeby otworzyć menu akwarium widocznego na ekranie.

| Pozycja | Co otwiera |
|---|---|
| **Zapisz parametry** | Wpisywanie wyników testów kropelkowych na klawiaturze ekranowej |
| **Dziennik** | [Dziennik](/help/max-records) tego akwarium |
| **Reef Buddy** | Najnowsze [podsumowanie](/help/max-intelligence) |
| **Raporty zdrowia** | Oceny zdrowia |
| **Konserwacja** | [Listę zadań](/help/max-records) |
| **Raporty ICP** | Przesłane [wyniki z laboratorium](/help/max-intelligence) |
| **Historia parametrów** | Wybór dowolnego parametru z danymi i jego [wykres](/help/max-intelligence) |
| **Progi alertów** | [Prawidłowy zakres](/help/max-alerts) każdego parametru w tym akwarium |
| **Obsada** | Spis obsady tego akwarium, na tym ekranie tylko do odczytu |
| **Aktywność** | [Każde gniazdo, karmienie i dawkę](/help/max-activity) oraz to, co się stało |
| **Układ panelu** | [Układanie widżetów na tym ekranie](/help/max-dashboard-editing) |
| **Jednostki** | Jednostki wyświetlania odczytów tego akwarium |
| **Ustawienia akwarium** | Pełny ekran ustawień tego akwarium |

## Przełączanie akwariów {#switching-tanks}

Dotknij **ikony siatki** po lewej stronie górnego paska, żeby przejść do [Reef Room](/help/max-reef-room), a potem otwórz wybrane akwarium. Możesz też przesunąć palcem w bok na pulpicie. Każde akwarium ma własny układ pulpitu, więc przy przełączaniu zmienia się cały ekran.

## Szuflada Gniazda i karmienie {#the-outlets-feed-drawer}

Przy akwarium z Neptune Apex na dole pulpitu jest mała etykieta **Gniazda i karmienie**. Dotknij jej albo przesuń palcem w górę w dowolnym miejscu pulpitu, żeby otworzyć **Sterowanie**.

- **KARMIENIE** uruchamia jeden z cykli karmienia Apex przyciskiem **A**, **B**, **C** albo **D**. **Anuluj** kończy go wcześniej.
- **GNIAZDA** możesz przełączać między Auto, Wył. i Wł.

Szuflada wymienia gniazda i cykle karmienia wybrane dla tego pulpitu albo wszystkie, jeśli żadnych nie wybrano. Więcej w [Gniazdach i sterowaniu](/help/max-controls).

:::warning Ta szuflada steruje prawdziwym sprzętem
Polecenie wychodzi w chwili dotknięcia, ale wysłanie nie oznacza wykonania. Wraca jako Potwierdzono, Niepotwierdzone, Odmówiono albo Bez zmian, a który wynik, zobaczysz w [Aktywności](/help/max-activity). Tryb karmienia to bezpieczny sposób na wstrzymanie przepływu na czas karmienia, bo sam wszystko przywraca. Ręczne Wył. zostaje wyłączone, dopóki tego nie zmienisz.
:::

## Gdy coś wygląda nie tak {#if-something-looks-out-of-place}

Jeśli odczyty wyglądają na nieaktualne albo etykieta stanu jest bursztynowa lub czerwona, zacznij od [Rozwiązywania problemów](/help/troubleshooting).

---
title: Konserwacja
description: Dodawaj powtarzalne prace, takie jak czyszczenie odpieniacza albo wymiana skarpet filtracyjnych, dostawaj przypomnienia o terminach i oznaczaj zadania jako wykonane albo je odkładaj.
section: Cora Mobile
reviewed: 2026-10-17
order: 28
group: Records
twin: max-records
---

Konserwacja przechowuje prace, których akwarium regularnie wymaga, z przypomnieniem dla każdej z nich.

Dotknij **Konserwacja** w rzędzie przycisków pod panelem. Znajdziesz ją też w Ustawieniach → Twoje akwarium → **Konserwacja**.

![Lista konserwacji](img/mobile-maintenance.webp "Zgodność, liczba zaległych zadań i każde zadanie z ostatnim wykonaniem i kolejnym terminem.")

## Podsumowanie {#summary}

Na górze zobaczysz **Zgodność konserwacji**, czyli jaka część zadań jest teraz w terminie, i ile zadań jest zaległych.

Każde zadanie na liście ma kolor: zaległe, z bliskim terminem albo zaplanowane. Widać też, kiedy ostatnio je wykonano i kiedy przypada następny termin.

## Dodawanie zadania {#adding-a-task}

Dotknij **Dodaj zadanie**, a potem wybierz:

- **Z szablonu** dla typowej pracy z wpisanym już interwałem. Wybierz ją, ustaw następny termin i godzinę przypomnienia, a potem dotknij **Potwierdź**.
- **Własne zadanie** dla własnej pracy. Podaj **Nazwę zadania**, **Interwał (dni)**, **Kategorię** i **Następny termin**. Włącz **Przypomnienie** i wybierz **Przypomnij mi o**, jeśli chcesz dostać powiadomienie.

Niektóre szablony, z interwałem, od którego startują:

| Zadanie | Interwał |
|---|---|
| Zmień skarpety filtracyjne | 3 dni |
| Wyczyść kubek odpieniacza | 7 dni |
| Wymiana wody | 7 dni |
| Przetestuj parametry wody | 7 dni |
| Wymień węgiel | 30 dni |
| Skalibruj sondę pH | 30 dni |
| Wyczyść pompy cyrkulacyjne | 90 dni |
| Wgraj wyniki ICP | 90 dni |

Interwał każdego zadania możesz później zmienić.

### Zadania, które Cora dodaje dla sprzętu Red Sea {#red-sea-tasks}

Gdy podłączysz Red Sea ReefDose, ReefATO+, ReefMat albo ReefRun, Cora dodaje serwis, którego wymaga to urządzenie, od razu z właściwym interwałem:

| Urządzenie | Zadanie | Interwał |
|---|---|---|
| ReefATO+ | Wymień czujnik EC ReefATO+ | 42 dni |
| ReefATO+ | Wymień pompę powrotną ReefATO+ | 135 dni |
| ReefMat | Wymień węgiel w ReefMat | 25 dni |
| ReefRun | Sprawdź venturi odpieniacza ReefRun | 35 dni |
| ReefRun | Wymień wirnik odpieniacza ReefRun | 135 dni |
| ReefRun | Skalibruj czujnik pełnego kubka ReefRun | 28 dni |
| ReefRun | Skalibruj czujnik nadmiernego odpieniania ReefRun | 28 dni |
| ReefRun, każda pompa | Zrób przegląd silnika pompy ReefRun | 135 dni |
| ReefRun, każda pompa | Wyczyść sitko pompy ReefRun | 42 dni |
| ReefDose, każda głowica | Skalibruj głowicę ReefDose | 90 dni |
| ReefDose, każda głowica | Wymień wężyk głowicy ReefDose | 450 dni |

Działają jak każde zadanie dodane samodzielnie. Możesz zmienić ich nazwę, interwał, odłożyć je albo usunąć. Jeśli usuniesz któreś, Cora nie doda go ponownie dla tego urządzenia.

### Przetestuj wodę {#test-water}

Jeśli na karcie pierwszego testu dotkniesz **Przypominaj mi o teście co tydzień**, Cora doda cotygodniowe zadanie **Przetestuj wodę**, z terminem w wybrany **Dzień testu**. Działa jak każde inne zadanie. Zobacz [Konfiguracja Cora Mobile](/help/mobile-setup). Przypomnienie o testach możesz też dodać w dowolnej chwili szablonem **Przetestuj parametry wody**.

### Z automatyzacji {#from-an-automation}

[Automatyzacja](/help/mobile-automation) z akcją **Utwórz zadanie konserwacyjne** może dodać pracę do tej listy, gdy zadziała jej reguła, albo ustawić termin istniejącego zadania na teraz. Nowe zadanie to **Zadanie jednorazowe** z terminem na teraz, z dopiskiem *Utworzone przez automatyzację* i powodem. Znika z listy, gdy je wykonasz. Dopóki jest otwarte, ta sama automatyzacja nie doda kolejnego. Dostajesz jedno powiadomienie.

## Przypomnienia {#reminders}

Otwórz zadanie i włącz **Przypomnienie**, a potem wybierz **Przypomnij mi o**. Dostaniesz powiadomienie dzień przed terminem i w dniu terminu. Gdy zadanie jest zaległe, przypomnienie przychodzi co kilka dni. Jeśli kilka zadań w jednym akwarium ma termin w tym samym czasie, przychodzą jako jedno powiadomienie.

Przypomnienia należą do **Przypomnień o konserwacji** w [Ustawienia → Powiadomienia](/help/mobile-notifications). Jeśli wolisz tylko widzieć zadanie na liście, wyłącz jego **Przypomnienie**.

## Oznaczanie zadania jako wykonanego {#marking-done}

Przesuń zadanie palcem w prawo albo otwórz je i dotknij **Zakończ**. Jeśli przesunięto je przez pomyłkę, dotknij **Cofnij** w komunikacie, który się pojawi.

Cora zapisuje godzinę zakończenia i od niej liczy następny termin. Jeśli więc zrobisz coś trzy dni po terminie, następny termin też przesunie się o trzy dni. Jeśli zadanie jest po terminie, Cora najpierw pyta **Kiedy to zostało zrobione?** Wybierz **Przed chwilą** albo **Wybierz datę i godzinę**, jeśli zrobiono to wcześniej (patrz niżej).

Arkusz zadania pokazuje **Historię zakończeń**, w tym to, jak bardzo każde wykonanie było spóźnione.

:::note Wykonanie zadania tworzy też wpis w dzienniku
Cora dodaje za Ciebie krótki wpis w [dzienniku](/help/mobile-journal), z informacją, czy zadanie było spóźnione. Dodaj własny wpis, gdy jest coś więcej do powiedzenia, na przykład gdy pompa była pełna piasku albo skarpety były czarne po jednym dniu.
:::

## Oznaczanie zadania jako zrobionego wcześniej {#done-earlier}

Zrobiono to wczoraj i zapomniano odhaczyć? Otwórz zadanie, dotknij **Zrobione wcześniej…** i wybierz datę oraz godzinę. Cora datuje wykonanie, wpis w dzienniku i następny termin od tej godziny, więc następny termin to wybrana godzina plus odstęp.

Możesz cofnąć się o najwyżej rok, ale nie przed ostatnie wykonanie zadania. Jeśli wybierzesz godzinę, która jeszcze nie nadeszła, albo wcześniejszą niż ostatnie wykonanie, Cora to zgłosi i niczego nie zapisze.

## Edytowanie zadania {#editing}

Dotknij zadania, żeby je otworzyć. Możesz zmienić **Nazwę zadania**, **Interwał (dni)**, **Notatki (opcjonalnie)**, **Następny termin** i przypomnienie, a potem dotknąć **Zapisz**. **Usuń** je usuwa.

## Odkładanie {#snoozing}

Nie możesz teraz zająć się pracą? Otwórz ją, dotknij **Odłóż** i wybierz **1 dzień**, **3 dni**, **1 tydzień**, **2 tygodnie** albo **1 miesiąc**. Zostanie na liście jako **Odłożone** z nową datą i do tego czasu nie dostaniesz przypomnienia.

:::warning Oznaczaj zadanie jako wykonane dopiero po wykonaniu
Następny termin liczy się od chwili, w której zadanie zostało zrobione. Jeśli oznaczysz otwarte zadanie jako wykonane, przesuną się wszystkie kolejne terminy. Jeśli zrobiono je wcześniej, użyj **Zrobione wcześniej…** i wybierz prawdziwą godzinę. Jeśli go nie zrobiono, zamiast tego odłóż zadanie.
:::

Zadania nie da się wstrzymać. Pracę, która nie dotyczy bieżącego sezonu, odłóż na **1 miesiąc** albo usuń i dodaj ponownie później.

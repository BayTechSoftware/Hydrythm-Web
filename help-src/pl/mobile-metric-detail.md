---
title: Zaglądanie w parametr
description: Dotknij dowolnego widżetu po pełną historię, każde źródło, które go zgłasza, i gdzie zmienić jego zakres.
section: Cora Mobile
reviewed: 2026-09-09
order: 8
group: Your dashboard
---

Widżet pokazuje Ci liczbę. Dotknięcie go pokazuje historię za tą liczbą.

## Co otrzymujesz

![Zaglądanie w parametr](img/mobile-metric-detail.webp "Zakresy na górze, potem źródła zgłaszające ten parametr, potem wykres z zacienionym pasmem alertu.")

**Wykres historii**, z własnym selektorem zakresu: **1h · 6h · 12h · 24h · 3d · 7d** i dłuższe.

**Filtr źródła.** Pod zakresami znajduje się rząd plakietek: **Wszystkie**, plus jedna na źródło zgłaszające ten parametr, na przykład *Apex*, *Cora*, *Red Sea* albo *Manual*. Wybierz jedną, aby zobaczyć tylko jej odczyty. To jest sposób, jak porównać sondę z testem kroplowym wprost: przełączaj się między nimi na tym samym wykresie.

**Link do kalkulatora dawek**, dla parametrów, które dozujesz. Wykorzystuje objętość akwarium z Twojego [profilu akwarium](/help/mobile-tank-profile) i siły z [Dozowania](/help/mobile-dosing).

**Nakładka porównania.** *Compare with* rysuje drugi parametr na tym samym wykresie (alkaliczność względem wapnia, pH względem temperatury), więc związek, który podejrzewasz, staje się widoczny, a nie tylko pamiętany.

**Statystyki podsumowujące** dla okna na ekranie: **MIN**, **ŚR** i **MAKS**, pokazane jako rząd pod aktualną wartością.

**Znaczniki dawek** na wykresie, dzięki czemu zmianę można porównać z tym, co faktycznie zdozowałeś.

**Lista surowych odczytów**: każdy pojedynczy odczyt za linią, z jego źródłem i znacznikiem czasu.

**Twoje pasmo alertu**, zacienione na wykresie, dzięki czemu odczyt jest odczytywany względem swojego zakresu, a nie w izolacji. Aby zmienić sam zakres, przytrzymaj widżet na pulpicie. Zobacz [Alerty i progi](/help/mobile-alerts).

**Zapisz odczyt** ręcznie.

## Wybieranie zakresu

Właściwy zakres zależy od rytmu parametru:

| Parametr | Użyteczne okno |
|---|---|
| pH | 24 godziny; zmienia się w cyklu dobowym |
| Temperatura | 24 godziny albo 7 dni |
| Alkaliczność | 7 albo 30 dni |
| Elementy śladowe | 30 dni albo rok |

:::note Sprawdź wiek odczytu na płaskim trendzie
Linia, która się nie zmieniła, może wskazywać na stabilny parametr albo na źródło, które przestało zgłaszać. Wiek pokazany przy wartości rozróżnia te dwie sytuacje.
:::

## Porównywanie źródeł

Gdy więcej niż jedno źródło zgłasza parametr, Cora zachowuje je odrębnie, a nie uśrednia. Użyj plakietek źródeł, aby zobaczyć każde po kolei.

Trwałe przesunięcie między sondą i ręcznie zapisanym testem zwykle wskazuje, że sonda wymaga kalibracji.

[Wynik ICP](/help/mobile-icp-health) jest użyteczną trzecią opinią, ale nie arbitrem. Laboratoria różnią się między sobą, a obsługa, przechowywanie i transport próbki wszystkie wpływają na wynik. Traktuj jeden ICP jako dowód, nie jako prawdziwą wartość; dwa zgadzające się testy są warte znacznie więcej niż jeden.

## Wybieranie, któremu źródłu ufa widżet

Jeśli chcesz, aby widżet śledził jedno konkretne źródło, ustaw to w ustawieniach widżetu. Zobacz **[Edytowanie pulpitu](/help/mobile-dashboard-editing)**.

## Wykluczanie błędnego odczytu

Sonda, która skoczyła, źle odczytany test, próbka pobrana w trakcie podmiany wody: jeden błędny odczyt zniekształca wykres, średnie i wszystko, co wnioskuje na ich podstawie.

![Lista surowych odczytów](img/mobile-readings.webp "Każdy odczyt za linią, z jego źródłem i czasem.")

Otwórz listę odczytów z ikony na górnym pasku, a potem dotknij odczytu, aby go wykluczyć. Ekran mówi to wprost: *wykluczone ze średnich i wglądów, ale zostaje w Twoim zapisie.* Nic nie jest usuwane i można to przywrócić.

:::warning Wyklucz błędny odczyt, nie niewygodny
Wykluczanie jest dla odczytów, o których wiesz, że są nieprawidłowe. Odczyt, który Ci się nie podoba, ale któremu nie możesz nic zarzucić, jest danymi, i usunięcie go czyni każde późniejsze porównanie mniej wiarygodnym.
:::

## Zapisywanie opieki nad sondą

Zapisanie kalibracji albo czyszczenia z tego miejsca oznacza datę przy tym źródle, więc późniejszą niezgodność można odczytać w odniesieniu do tego, kiedy sonda była ostatnio obsłużona. Zobacz [Sondy](/help/mobile-probes).

## Zapisywanie odczytu ręcznie

Wpisz to, co mówi Twój test kroplowy. Odczyty zapisane ręcznie są pełnoprawne: otrzymują własne źródło i znacznik czasu, pojawiają się na wykresie, zasilają Reef Buddy i to z nimi Cora porównuje Twój sprzęt.

:::note Cora sprawdza wpisy, które wyglądają nieprawdopodobnie
Jeśli wartość jest daleka od tego, w czym akwarium normalnie działa, jesteś proszony o jej potwierdzenie, zanim zostanie zapisana. To wychwytuje przecinek dziesiętny w złym miejscu albo odczyt wpisany przy złym parametrze. Potwierdź, a odczyt zostanie zapisany normalnie.
:::

---
title: Szczegóły parametru
description: Dotknij widżetu, żeby zobaczyć pełną historię, wszystkie źródła parametru i miejsce, gdzie zmienisz jego zakres.
section: Cora Mobile
reviewed: 2026-09-09
order: 8
group: Your dashboard
---

Widżet pokazuje liczbę. Gdy go dotkniesz, zobaczysz, co za nią stoi.

## Co tu znajdziesz

![Szczegóły parametru](img/mobile-metric-detail.webp "Na górze zakresy czasu, niżej źródła tego parametru, a pod nimi wykres z zaznaczonym zakresem alertu.")

**Wykres historii** z własnym wyborem okresu: **1h · 6h · 12h · 24h · 3d · 7d** i dłuższe.

**Filtr źródeł.** Pod zakresami jest rząd etykiet: **Wszystkie** i po jednej dla każdego źródła tego parametru, np. *Apex*, *Cora*, *Red Sea* albo *Ręczny*. Wybierz jedną, a zobaczysz tylko odczyty z tego źródła. Tak najłatwiej porównać sondę z testem kropelkowym. Przełączaj się między nimi na tym samym wykresie.

**Link do kalkulatora dawek** przy parametrach, które dozujesz. Kalkulator bierze objętość akwarium z [profilu akwarium](/help/mobile-tank-profile) i stężenia z [Dozowania](/help/mobile-dosing).

**Nakładanie wykresów.** **Porównaj z** rysuje drugi parametr na tym samym wykresie (np. alkaliczność i wapń albo pH i temperaturę). Zależność, którą podejrzewasz, widać wtedy na wykresie i nie musisz jej pamiętać.

**Statystyki** dla okresu widocznego na ekranie: **MIN**, **ŚR** i **MAKS**, w rzędzie pod bieżącą wartością.

**Znaczniki dawek** na wykresie. Zmianę parametru zestawisz z tym, co naprawdę podano.

**Lista odczytów**, czyli każdy pojedynczy odczyt, z którego powstała linia, ze źródłem i czasem.

**Twój zakres alertu** zaznaczony na wykresie. Każdy odczyt widać na tle zakresu, a nie w oderwaniu od niego. Żeby zmienić sam zakres, przytrzymaj widżet na pulpicie. Więcej w [Alertach i progach](/help/mobile-alerts).

**Ręczne wpisanie odczytu.**

## Jaki okres wybrać

Dobry okres zależy od tego, jak zmienia się parametr:

| Parametr | Przydatny okres |
|---|---|
| pH | 24 godziny, bo zmienia się w cyklu dobowym |
| Temperatura | 24 godziny albo 7 dni |
| Alkaliczność | 7 albo 30 dni |
| Pierwiastki śladowe | 30 dni albo rok |

:::note Przy płaskiej linii sprawdź wiek odczytu
Linia bez zmian może oznaczać stabilny parametr, ale też źródło, które przestało wysyłać dane. Rozróżnisz to po wieku odczytu obok wartości.
:::

## Porównywanie źródeł

Gdy parametr podaje kilka źródeł, Cora trzyma je osobno i ich nie uśrednia. Przełączaj etykiety źródeł, żeby zobaczyć każde po kolei.

Stała różnica między sondą a wynikiem wpisanym ręcznie zwykle znaczy, że sondę trzeba skalibrować.

[Wynik ICP](/help/mobile-icp-health) to przydatna trzecia opinia, ale nie rozstrzygający sędzia. Laboratoria różnią się między sobą, a na wynik wpływa to, jak próbkę pobrano, przechowywano i transportowano. Pojedynczy ICP traktuj jako wskazówkę, a nie prawdziwą wartość. Dwa zgodne testy są warte znacznie więcej niż jeden.

## Z którego źródła korzysta widżet

Jeśli chcesz, żeby widżet pokazywał jedno konkretne źródło, ustaw to w ustawieniach widżetu. Więcej w **[Edytowaniu pulpitu](/help/mobile-dashboard-editing)**.

## Wykluczanie błędnego odczytu

Skok sondy, źle odczytany test, próbka pobrana w trakcie podmiany wody. Jeden błędny odczyt psuje wykres, średnie i wszystko, co na nich bazuje.

![Lista odczytów](img/mobile-readings.webp "Każdy odczyt, z którego powstała linia, ze źródłem i czasem.")

Otwórz listę odczytów ikoną na górnym pasku i dotknij odczytu, żeby go wykluczyć. Ekran mówi to wprost: *odczyt jest wykluczony z uśrednień i wniosków, ale zostaje w Twoim dzienniku.* Nic nie jest usuwane i odczyt można przywrócić.

:::warning Wykluczaj błędne odczyty, a nie niewygodne
Wykluczanie jest dla odczytów, o których wiesz, że są nieprawidłowe. Odczyt, który Ci się nie podoba, ale nic mu nie brakuje, to też dane. Jeśli go usuniesz, każde późniejsze porównanie będzie mniej uczciwe.
:::

## Zapisywanie konserwacji sondy

Gdy zapiszesz tutaj kalibrację albo czyszczenie, przy tym źródle pojawi się data. Późniejszą rozbieżność ocenisz wtedy na tle tego, kiedy sonda była ostatnio obsługiwana. Więcej w [Sondach](/help/mobile-probes).

## Ręczne wpisywanie odczytu

Wpisz wynik z testu kropelkowego. Wyniki wpisane ręcznie mają taką samą wagę jak inne. Dostają własne źródło i czas, pojawiają się na wykresie, trafiają do Reef Buddy i właśnie z nimi Cora porównuje Twój sprzęt.

:::note Cora sprawdza wartości, które wyglądają podejrzanie
Jeśli wartość mocno odbiega od tego, co zwykle jest w akwarium, Cora poprosi o potwierdzenie przed zapisaniem. Tak wychwyci przecinek w złym miejscu albo odczyt wpisany przy złym parametrze. Po potwierdzeniu odczyt zapisuje się normalnie.
:::

---
title: Szczegóły parametru
description: Dotknij widżetu, żeby zobaczyć pełną historię, wszystkie źródła parametru i miejsce, gdzie zmienisz jego zakres.
section: Cora Mobile
reviewed: 2026-10-12
order: 8
group: Your dashboard
---

Widżet pokazuje liczbę. Gdy go dotkniesz, zobaczysz, co za nią stoi.

Są dwa sposoby, żeby tu wejść. Dotknij widżetu na pulpicie albo dotknij **Historia parametrów** w rzędzie przycisków pod widżetami i wybierz parametr. **Historia parametrów** wymienia każdy parametr, który ma dane, nawet taki bez widżetu na pulpicie.

## Co tu znajdziesz

![Szczegóły parametru](img/mobile-metric-detail.webp "Na górze listy rozwijane, a pod nimi wykres z zaznaczonym zakresem alertu.")

**Wykres historii.** Trzy listy rozwijane nad nim ustawiają, co pokazuje. **Parametr** przełącza na dowolny inny parametr, który ma dane, i zachowuje Twój okres. **Okres** biegnie od 1h przez 6h, 12h, 24h, 3d, 7d, 15d, 30d, 90d i 180d aż do 360d i Wszystko. **Źródło** zaczyna od **Wszystkie źródła** i wymienia źródła, które zgłaszają ten parametr w tym akwarium, np. *Apex*, *Cora*, *Red Sea* albo *Ręczny*. Wybierz jedno, a zobaczysz tylko odczyty z tego źródła. Tak najłatwiej porównać sondę z testem kropelkowym. Przełączaj się między nimi na tym samym wykresie.

Ekran zawsze otwiera się na 24h i **Wszystkie źródła**. Nie pamięta, co wybrano ostatnio.

**Wiersz z wartościami Najnowszy, Min, Śr i Maks** dla okresu widocznego na ekranie.

**Link do kalkulatora dawek** przy parametrach, które dozujesz. Kalkulator bierze objętość akwarium z [profilu akwarium](/help/mobile-tank-profile) i stężenia z [Dozowania](/help/mobile-dosing).

**Nakładanie wykresów.** **Porównaj** rysuje drugi parametr na tym samym wykresie (np. alkaliczność i wapń albo pH i temperaturę). Lista zawiera każdy parametr, który ma akwarium. Zależność, którą podejrzewasz, widać wtedy na wykresie i nie musisz jej pamiętać. Dotknij etykiety jeszcze raz, aby zdjąć drugą linię.

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

Gdy parametr podaje kilka źródeł, Cora trzyma je osobno i ich nie uśrednia. Użyj listy **Źródło**, żeby zobaczyć każde po kolei.

Na pulpicie pokazuje się najnowszy odczyt. Wartość na żywo zastępuje tylko odczyt z późniejszym czasem pomiaru, z dowolnego źródła. Starszy odczyt trafia do historii i nie nadpisuje tego, co jest na widżecie. Jeśli przypiąłeś źródło dla widżetu, Cora trzyma się tego źródła.

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

Wpisz wynik z testu kropelkowego. Lista jest podzielona na grupy, a grupa **Pierwiastki śladowe** obejmuje jod, żelazo i miedź w µg/L oraz potas w mg/L. Wyniki wpisane ręcznie mają taką samą wagę jak inne. Dostają własne źródło i czas, pojawiają się na wykresie, trafiają do Reef Buddy i właśnie z nimi Cora porównuje Twój sprzęt.

:::note Cora sprawdza wartości, które wyglądają podejrzanie
Jeśli wartość mocno odbiega od tego, co zwykle jest w akwarium, Cora poprosi o potwierdzenie przed zapisaniem. Tak wychwyci przecinek w złym miejscu albo odczyt wpisany przy złym parametrze. Po potwierdzeniu odczyt zapisuje się normalnie.
:::

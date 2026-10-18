---
title: Szczegóły parametru
description: Dotknij widżetu, żeby zobaczyć pełną historię parametru, porównać źródła i parametry, wykluczyć błędny odczyt i zapisać konserwację sondy.
section: Cora Mobile
reviewed: 2026-10-17
order: 7
group: Your dashboard
---

Widżet pokazuje liczbę. Dotknij go, żeby zobaczyć historię, która za nią stoi.

Są dwa sposoby, żeby tu wejść. Dotknij widżetu na panelu albo dotknij **Historia parametrów** w rzędzie przycisków pod widżetami i wybierz parametr. **Historia parametrów** wymienia każdy parametr, który ma dane, nawet taki bez widżetu na panelu.

## Co tu znajdziesz {#what-you-get}

![Szczegóły parametru](img/mobile-metric-detail.webp "Listy rozwijane na górze, a pod nimi wykres z zacieniowanym pasmem alertu.")

- Wykres historii. Rząd nad nim ustawia, co pokazuje. **Parametr** przełącza na dowolny inny parametr, który ma dane, i zachowuje okres. **Okres** biegnie od 1h przez 6h, 12h, 24h, 3d, 7d, 15d, 30d, 90d, 180d i 360d aż do Wszystko. **Źródło** zaczyna od **Wszystkie źródła** i wymienia źródła, które zgłaszają ten parametr w tym akwarium, na przykład *Apex*, *Cora*, *Red Sea* albo *Ręczne*. Wybierz jedno, żeby zobaczyć tylko jego odczyty.
- **Porównaj**, na końcu tego samego rzędu, rysuje na wykresie drugi parametr, na przykład alkaliczność z wapniem albo pH z temperaturą. Przycisk pokazuje wtedy **vs** i nazwę drugiego parametru. Dotknij go ponownie, żeby zdjąć drugą linię.
- Rząd z wartościami **Najnowszy**, **Min**, **Śr** i **Maks** dla okresu widocznego na ekranie.
- Ikony na górnym pasku: **Odczyty** otwiera listę surowych odczytów, a **Zapisz konserwację sondy** zapisuje kalibrację albo czyszczenie. Przy alkaliczności, wapniu i magnezie jest też kalkulator dawek, który bierze objętość akwarium z [profilu akwarium](/help/mobile-tank-profile) i stężenia z [Dozowania](/help/mobile-dosing).

Ekran zawsze otwiera się na 24h i **Wszystkie źródła**. Nie pamięta, co wybrano ostatnio.

Ciężar właściwy (SG) zawsze pokazuje trzy lub cztery miejsca po przecinku, więc 1,022 nie zamienia się w 1,02. Tak jest samo w Cora Mobile i Cora Max, na panelu, na wykresie i na liście odczytów.

## Jak czytać wykres {#reading-the-chart}

- Zielone pasmo to Twój zakres alertu, więc każdy odczyt widzisz na jego tle. Żeby zmienić zakres, przytrzymaj widżet na panelu. Więcej w [Alertach i progach](/help/mobile-alerts).
- Linia przerywana oznacza zapisaną dawkę, więc zestawisz zmianę z tym, co podano.
- **Maks. 30 dni** i **Min. 30 dni** to linie przerywane z wartościami skrajnymi z ostatnich 30 dni.
- Pusta kropka to odczyt, który wykluczono.
- Gdy **Porównaj** jest włączone, drugi parametr używa prawej osi.

## Jaki okres wybrać {#choosing-a-range}

Wybierz okres pasujący do tego, jak zmienia się parametr.

| Parametr | Przydatny okres |
|---|---|
| pH | 24 godziny, bo waha się w cyklu dobowym |
| Temperatura | 24 godziny albo 7 dni |
| Alkaliczność | 7 albo 30 dni |
| Pierwiastki śladowe | 30 dni albo rok |

:::note Płaska linia? Sprawdź wiek odczytu
Linia, która się nie rusza, może oznaczać stabilny parametr. Może też oznaczać, że źródło przestało raportować. Rozstrzygnie to wiek obok wartości na widżecie.
:::

## Porównywanie źródeł {#comparing-sources}

Gdy parametr zgłasza więcej niż jedno źródło, Cora trzyma je osobno i ich nie uśrednia. Użyj listy **Źródło**, żeby obejrzeć każde z nich. To najszybszy sposób na porównanie sondy z testem kropelkowym.

Na panelu widać najnowsze. Wartość na żywo zastępuje tylko odczyt z późniejszym czasem pomiaru, z dowolnego źródła. Starszy odczyt trafia do historii i nie nadpisuje tego, co jest na widżecie. Jeśli przypięto źródło w **Mapowaniu parametrów**, Cora trzyma się tego źródła.

Jeśli sonda i testy zapisywane ręcznie stale różnią się o tyle samo, sondę zwykle trzeba skalibrować.

[Wynik ICP](/help/mobile-icp-health) to przydatna trzecia opinia, ale nie rozstrzyga sprawy. Laboratoria różnią się między sobą, a na wynik wpływa sposób pobrania, przechowywania i wysyłki próbki. Pojedynczy ICP traktuj jako dowód. Dwa zgodne testy są warte dużo więcej niż jeden.

## Za którym źródłem idzie odczyt {#choosing-which-source-a-widget-trusts}

Źródło ustawia się dla akwarium i parametru, a nie dla widżetu. Przejdź do **Ustawień**, dotknij akwarium, dotknij **Mapowanie parametrów**, a potem zakładki **Źródła**. Wybierz sondę albo **Automatycznie (wygrywa najnowszy odczyt)**. Wybór dotyczy tego parametru wszędzie w tym akwarium. Więcej w [Mapowaniu parametrów](/help/mobile-probes).

## Wykluczanie błędnego odczytu {#excluding-a-bad-reading}

Może sonda skoczyła, test został źle odczytany albo próbkę pobrano w trakcie podmiany wody. Jeden błędny odczyt psuje wykres, średnie i wszystko, co z nich wyliczono.

![Lista odczytów pH w Cora Mobile](img/mobile-readings.webp "Każdy odczyt, z którego powstała linia, z czasem i źródłem. Dotknij odczytu, żeby go wykluczyć.")

Dotknij **Odczyty** na górnym pasku, a potem odczytu. Cora zapyta **Wykluczyć ten odczyt?** i wyjaśni, że odczyt zostaje w Twoim dzienniku, ale przestaje się liczyć do średnich, trendów, spostrzeżeń i asystenta. Dotknij **Wyklucz**. Nic nie zostaje usunięte i w ten sam sposób możesz odczyt przywrócić.

Odczytów starszych niż 90 dni nie da się wykluczyć ani przywrócić.

:::warning Wykluczaj błędne odczyty, a nie niewygodne
Wykluczaj tylko odczyt, o którym wiesz, że jest nieprawidłowy. Jeśli odczyt po prostu Ci się nie podoba, ale nie widzisz w nim błędu, to prawdziwe dane. Usunięcie go sprawi, że każde późniejsze porównanie będzie mniej uczciwe.
:::

## Zapisywanie konserwacji sondy {#recording-probe-care}

Dotknij **Zapisz konserwację sondy** (ikona czujnika na górnym pasku) i wybierz, co zrobiono: kalibrację, czyszczenie, wymianę, przestawienie albo porównanie. Cora zapisze datę przy tym źródle, więc świeża kalibracja nie zostanie wzięta za dryf. Później, gdy sonda nie zgodzi się z czymś, zobaczysz, kiedy ostatnio była obsługiwana. Więcej w [Mapowaniu parametrów](/help/mobile-probes).

## Ręczne zapisywanie odczytu {#logging-a-reading-by-hand}

Odczyty zapisujesz z panelu, a nie z tego ekranu. Dotknij **Zapisz parametry** pod widżetami i wpisz wynik testu kropelkowego. Lista jest pogrupowana, a grupa **Pierwiastki śladowe** obejmuje jod, żelazo i miedź w µg/L oraz potas w mg/L. Odczyty zapisane ręcznie liczą się tak samo jak inne. Dostają własne źródło i czas, pojawiają się na wykresie i trafiają do Reef Buddy. To też z nimi Cora porównuje Twój sprzęt.

:::note Cora sprawdza wpisy, które wyglądają dziwnie
Jeśli wartość mocno odbiega od tego, gdzie akwarium było dotąd, Cora poprosi o potwierdzenie przed zapisaniem. Tak wyłapie przecinek w złym miejscu albo odczyt wpisany przy złym parametrze. Po potwierdzeniu odczyt zapisuje się normalnie.
:::

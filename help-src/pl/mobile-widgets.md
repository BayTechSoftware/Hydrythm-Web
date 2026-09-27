---
title: Opis widżetów
description: Każdy typ widżetu w Corze (wartość, wskaźnik, wykres, stan, gniazdo i kafelki urządzeń) i kiedy go używać.
section: Cora Mobile
reviewed: 2026-09-17
order: 7
group: Your dashboard
---

Widżet to jedna kafelka na Twoim pulpicie, pokazująca jedną rzecz. Ta strona opisuje każdy typ i co można skonfigurować.

Dodawaj je i rozmieszczaj w **[edytorze pulpitu](/help/mobile-dashboard-editing)**; dotknij tam widżetu, aby otworzyć jego ustawienia.

![Konfigurowanie widżetu](img/mobile-widget-config.webp "Typ, parametr, a potem szerokość i wysokość.")

## Dziewięć typów

| Typ | Pokazuje |
|---|---|
| **Wartość** | Aktualny odczyt, jego jednostkę, wiek i źródło |
| **Wskaźnik** | Łuk z zaznaczonym Twoim zakresem i gałką na wartości |
| **Wykres** | Trend w wybranym przez Ciebie oknie czasowym |
| **Stan** | Stan jako tekst: działa, bezczynny, zamknięty |
| **Gniazdo** | Trójstanowa kontrolka: Auto, Off, On |
| **ReefBeat** | Jedno urządzenie Red Sea, z własnym podsumowaniem |
| **Moduł Apex** | Jeden zamontowany moduł Apex, na przykład Trident lub DŌS |
| **Jecod** | Jedna pompa Jecod, z jej trybem i intensywnością |
| **Maxspect** *(beta)* | Jeden gyre, z obydwoma silnikami |

Ostatnie cztery to kafelki **urządzeń**: są przypisane do konkretnego sprzętu, a nie do parametru, i każdy pokazuje to, co dane urządzenie zgłasza.

## Rozmiar

**Szerokość** i **Wysokość** mają zawsze wartość **1×** albo **2×**. Wykres nigdy nie ma jednej komórki szerokości.

## Value

Zwykła liczba. Aktualny odczyt, jego jednostka, jak stary jest i skąd pochodzi.

Użyj go dla parametrów, które sprawdzasz liczbowo, a nie przez trend: wapń, magnez, azotany.

**Ustawienia:** etykieta, źródło, rozmiar.

## Gauge

Łuk z zaznaczonym Twoim docelowym zakresem i gałką na aktualnej wartości. Kolor gałki mówi, gdzie jesteś: w paśmie, dryfujesz albo jesteś poza nim.

Użyj go dla parametrów, które aktywnie zarządzasz: alkaliczność, pH, zasolenie, temperatura.

**Ustawienia:** etykieta, źródło, zakres (dziedziczony z celów Twojego akwarium, jeśli nie zostanie tutaj nadpisany), rozmiar.

:::note Ustaw wskaźniki na dwie kolumny lub więcej
Przy jednej kolumnie łuk jest zbyt mały, by odczytać go na pierwszy rzut oka; użyj widżetu **value** zamiast tego, jeśli miejsca jest mało.
:::

## Graph

Mikrowykres w wybranym przez Ciebie oknie czasowym, z zaznaczonym maksimum i minimum oraz podaną aktualną wartością.

Dla parametru, który testujesz (Tridentem lub testem kroplowym), linia łączy Twoje faktyczne testy. Jeśli okno zawiera tylko jeden test, linia dochodzi z testu przed nim, a maksimum i minimum nie są zaznaczone. Bez żadnego testu w oknie, albo bez wcześniejszego testu, do którego można połączyć jeden test, kafelek pokazuje **Zbieranie…** zamiast linii.

Użyj go dla wszystkiego, co się zmienia: pH w ciągu dnia, temperatura podczas upału, alkaliczność między dawkami.

**Ustawienia:** etykieta, źródło, **okno czasowe** (1 godzina, 6 godzin, 24 godziny, 7 dni, 30 dni, 1 rok), rozmiar.

Trend ma zawsze **co najmniej dwie komórki szerokości**; mikrowykres wciśnięty w jedną komórkę nic nie mówi, więc edytor nie pozwoli takiego stworzyć.

:::note Wybierz okno odpowiadające rytmowi
pH zmienia się w cyklu dobowym, więc 24 godziny pokazują jego kształt. Alkaliczność zmienia się w ciągu dni, więc 7 lub 30 mówi więcej niż 24 kiedykolwiek pokaże.
:::

## Status

Tekst, a nie liczba, dla rzeczy będących stanem. Działa, bezczynny, otwarty, zamknięty, karmienie.

**Ustawienia:** etykieta, źródło, rozmiar.

## Outlet

Trójstanowy przełącznik dla gniazda: **Auto**, **Wyłączone**, **On**.

- **Auto** przekazuje gniazdo z powrotem temu, co normalnie nim zarządza: harmonogramowi, regule albo kontrolerowi, do którego należy.
- **Wyłączone** i **On** to ręczne nadpisania, które trwają, aż je zmienisz z powrotem.

**Ustawienia:** etykieta, które gniazdo, rozmiar.

:::warning Ręczne nadpisanie nie wygasa samo
Off znaczy wyłączone, aż ustawisz z powrotem na Auto. Jeśli wyłączysz pompę powrotną, aby popracować w akwarium, ustaw ją z powrotem na Auto, gdy skończysz; Cora nie zrobi tego za Ciebie.
:::

## ReefBeat

Jedna kafelka dla całego urządzenia, pokazująca jego własne podsumowanie, a nie jeden parametr: stan i zbiornik ATO, głowice jednostki dozującej, liczbę pozostałych dni maty.

Które urządzenia oferują kafelkę, zależy od tego, co masz podłączone. Zobacz **[Podłączanie sprzętu](/help/mobile-connections)**.

**Ustawienia:** etykieta, które urządzenie, rozmiar.

## Co pokazuje widżet parametru

W widżecie opartym na zmierzonym parametrze (Value, Gauge, Graph i Status) obecne są zawsze te trzy rzeczy. Kafelki gniazd i urządzeń pokazują za to własny stan, bo nie stoi za nimi jeden konkretny odczyt:

- **Wartość**, duża
- **Wiek** (`now`, `1h`, `2d`): jak stary jest odczyt, nie jak niedawno odświeżył się ekran
- **Źródło**: mały znaczek mówiący, skąd pochodzi liczba

Dotknij dowolnego widżetu, aby otworzyć jego pełną historię, każde źródło, które go zgłasza, i obowiązujące progi.

## Rozmiary

Widżety mają jedną lub dwie komórki szerokości i jedną lub dwie komórki wysokości, z wyjątkiem **trendu**, który ma zawsze co najmniej dwie szerokości. Na trzykolumnowym pulpicie wskaźnik o szerokości dwóch komórek zajmuje dwie trzecie rzędu, co zwykle jest właściwym kształtem dla Twojego najważniejszego parametru.

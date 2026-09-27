---
title: Rodzaje widżetów
description: Wszystkie typy widżetów w Corze (wartość, wskaźnik, wykres, stan, gniazdo i kafelki urządzeń) i kiedy których używać.
section: Cora Mobile
reviewed: 2026-09-17
order: 7
group: Your dashboard
---

Widżet to jeden kafelek na pulpicie, który pokazuje jedną rzecz. Tutaj opisujemy każdy typ i jego ustawienia.

Widżety dodajesz i układasz w **[edytorze pulpitu](/help/mobile-dashboard-editing)**. Tam też dotknięcie widżetu otwiera jego ustawienia.

![Ustawienia widżetu](img/mobile-widget-config.webp "Typ, parametr, a potem szerokość i wysokość.")

## Dziewięć typów

| Typ | Co pokazuje |
|---|---|
| **Wartość** | Bieżący odczyt z jednostką, wiekiem i źródłem |
| **Wskaźnik** | Łuk z zaznaczonym Twoim zakresem i znacznikiem na bieżącej wartości |
| **Wykres** | Trend w wybranym okresie |
| **Stan** | Stan opisany słowem: pracuje, bezczynny, zamknięty |
| **Gniazdo** | Przełącznik z trzema pozycjami: AUTO, WYŁ., WŁ. |
| **ReefBeat** | Jedno urządzenie Red Sea z jego własnym podsumowaniem |
| **Moduł Apex** | Jeden zamontowany moduł Apex, np. Trident albo DŌS |
| **Jecod** | Jedna pompa Jecod z trybem i intensywnością |
| **Maxspect** *(beta)* | Jeden gyre z oboma silnikami |

Ostatnie cztery to kafelki **urządzeń**. Są powiązane z konkretnym sprzętem, a nie z parametrem, i pokazują to, co zgłasza dane urządzenie.

## Rozmiar

**Szerokość** i **Wysokość** mają wartość **1×** albo **2×**, więc widżet ma jedną albo dwie komórki szerokości i jedną albo dwie wysokości. Wykres nigdy nie ma szerokości jednej komórki. Na pulpicie z trzema kolumnami wskaźnik o szerokości dwóch komórek zajmuje dwie trzecie rzędu. Zwykle to dobry kształt dla najważniejszego parametru.

## Wartość

Sama liczba: bieżący odczyt, jednostka, wiek odczytu i jego źródło.

Pasuje do parametrów, które sprawdzasz po liczbie, a nie po trendzie, np. wapnia, magnezu, azotanów.

Ustawienia: etykieta, źródło, rozmiar.

## Wskaźnik

Łuk z zaznaczonym zakresem docelowym i znacznikiem na bieżącej wartości. Kolor znacznika pokazuje, gdzie jesteś: w zakresie, blisko granicy albo poza nim.

Pasuje do parametrów, którymi aktywnie zarządzasz, np. alkaliczności, pH, zasolenia, temperatury.

Ustawienia: etykieta, źródło, zakres (brany z wartości docelowych akwarium, chyba że zmienisz go tutaj), rozmiar.

:::note Wskaźnik najlepiej wygląda na dwóch kolumnach
Na jednej kolumnie łuk jest za mały, żeby odczytać go jednym spojrzeniem. Jeśli brakuje miejsca, użyj widżetu **Wartość**.
:::

## Wykres

Mały wykres liniowy dla wybranego okresu, z zaznaczonym maksimum i minimum oraz podaną bieżącą wartością.

Dla parametru, który testujesz (Tridentem albo testem kropelkowym), linia łączy Twoje rzeczywiste testy. Jeśli w okresie jest tylko jeden test, linia biegnie od testu sprzed tego okresu, a maksimum i minimum nie są zaznaczone. Jeśli w okresie nie ma żadnego testu albo pojedynczego testu nie ma z czym połączyć, kafelek pokazuje **Zbieranie…** w miejscu linii.

Pasuje do wszystkiego, co się zmienia: pH w ciągu dnia, temperatury w czasie upałów, alkaliczności między dawkami.

Ustawienia: etykieta, źródło, **okno czasowe** (1 godzina, 6 godzin, 24 godziny, 7 dni, 30 dni, 1 rok), rozmiar.

Wykres ma zawsze **co najmniej dwie komórki szerokości**. Wykres ściśnięty w jedną komórkę nic nie mówi, więc edytor na to nie pozwala.

:::note Dopasuj okres do rytmu parametru
pH zmienia się w cyklu dobowym, więc 24 godziny pokazują jego przebieg. Alkaliczność zmienia się w ciągu dni, więc 7 albo 30 dni powie więcej niż 24 godziny.
:::

## Stan

Słowo, a nie liczba. Dla rzeczy, które mają stan: pracuje, bezczynny, otwarty, zamknięty, karmienie.

Ustawienia: etykieta, źródło, rozmiar.

## Gniazdo

Przełącznik gniazda z trzema pozycjami: **AUTO**, **WYŁ.** i **WŁ.**

- **AUTO** oddaje gniazdo temu, co nim zwykle steruje: harmonogramowi, regule albo kontrolerowi, do którego należy.
- **WYŁ.** i **WŁ.** to ręczne ustawienia, które obowiązują, dopóki ich nie zmienisz.

Ustawienia: etykieta, wybór gniazda, rozmiar.

:::warning Ręczne ustawienie nie wygasa samo
WYŁ. oznacza wyłączone, dopóki nie przestawisz gniazda z powrotem na AUTO. Jeśli wyłączasz pompę powrotną na czas pracy w akwarium, po skończeniu ustaw ją z powrotem na AUTO. Cora nie zrobi tego za Ciebie.
:::

## ReefBeat

Jeden kafelek dla całego urządzenia. Pokazuje jego własne podsumowanie, a nie pojedynczy parametr: stan ATO i zbiornika, głowice pompy dozującej albo liczbę dni, na które wystarczy rolki maty.

To, które urządzenia mają swój kafelek, zależy od podłączonego sprzętu. Więcej w **[Podłączaniu sprzętu](/help/mobile-connections)**.

Ustawienia: etykieta, wybór urządzenia, rozmiar.

## Co pokazuje widżet parametru

Widżet oparty na zmierzonym parametrze (Wartość, Wskaźnik, Wykres i Stan) zawsze pokazuje trzy rzeczy. Kafelki gniazd i urządzeń pokazują swój stan, bo nie stoi za nimi pojedynczy odczyt.

- **Wartość**, dużymi cyframi
- **Wiek** (`teraz`, `1g`, `2d`): jak stary jest odczyt, a nie kiedy odświeżył się ekran
- **Źródło**: mały znaczek, który mówi, skąd pochodzi liczba

Dotknij widżetu, żeby zobaczyć pełną historię, wszystkie źródła tego parametru i obowiązujące progi.

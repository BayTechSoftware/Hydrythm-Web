---
title: Rodzaje widżetów
description: Każdy typ widżetu na pulpicie Cora Mobile, od wartości, wskaźnika, wykresu, stanu i gniazda po kafelki urządzeń, i kiedy używać każdego z nich.
section: Cora Mobile
reviewed: 2026-10-13
order: 9
group: Your dashboard
---

Widżet to jeden kafelek na pulpicie, który pokazuje jedną rzecz. Ta strona omawia każdy typ i to, co możesz w nim ustawić.

Widżety dodajesz i układasz w [edytorze pulpitu](/help/mobile-dashboard-editing). Dotknij tam widżetu, żeby otworzyć jego ustawienia: **Typ** i **Parametr** dla parametru, gniazdo albo urządzenie dla pozostałych, potem **Szerokość** i **Wysokość**, a dla wykresu **Zakres czasu**.

![Arkusz ustawień widżetu w Cora Mobile](img/mobile-widget-config.webp "Dolna połowa ustawień widżetu: parametr, szerokość, wysokość i zakres czasu, a pod nimi Usuń i Gotowe.")

## Piętnaście typów {#the-fifteen-types}

| Typ | Co pokazuje |
|---|---|
| **Wartość** | Bieżący odczyt, jego jednostkę, wiek i źródło |
| **Wskaźnik** | Łuk z naniesionym Twoim zakresem i znacznikiem na wartości |
| **Wykres** | Trend w wybranym zakresie czasu |
| **Stan** | Odczyt jako zwykły tekst z kolorową kropką |
| **Gniazdo** | Przełącznik z trzema pozycjami: Auto, Wył., Wł. |
| **ReefBeat** | Jedno urządzenie Red Sea z jego własnym podsumowaniem |
| **Moduł Apex** | Jeden zamontowany moduł Apex, na przykład Trident albo DŌS |
| **Jecod** | Jedną pompę Jecod z trybem i intensywnością |
| **Maxspect** *(Beta)* | Jeden Gyre z oboma silnikami |
| **GHL** *(Beta)* | Jeden kontroler ProfiLux albo Mitras z jego własnym podsumowaniem |
| **HYDROS** *(Beta)* | Jeden kontroler HYDROS z jego własnym podsumowaniem |
| **Radion** *(Beta)* | Jedną lampę EcoTech Radion albo połączoną sieć Radion |
| **VorTech** *(Beta)* | Jedną pompę EcoTech VorTech z trybem i prędkością |
| **Versa** *(Beta)* | Jeden dozownik EcoTech Versa z jego głowicami |
| **Kamera** *(Beta)* | Podgląd na żywo z jednej z Twoich kamer, do trzech kolumn szerokości i dwóch rzędów wysokości |

Wszystko po Gnieździe to kafelki **urządzeń**. Każdy należy do konkretnego sprzętu, a nie do parametru, i pokazuje to, co zgłasza dane urządzenie. Cora Max ma też kafelek **Scena**, który dodajesz na Cora Max. Zobacz [Edytowanie pulpitu Cora Max](/help/max-dashboard-editing).

:::note Kafelki Beta
Maxspect, GHL, HYDROS, EcoTech (Radion, VorTech i Versa) oraz Kamera to integracje Beta, dostępne tylko dla użytkowników Beta. Te kafelki widzisz dopiero wtedy, gdy masz to urządzenie. Zobacz [Funkcje Beta](/help/mobile-beta).
:::

## Rozmiar {#sizing}

**Szerokość** i **Wysokość** mogą mieć wartość **1×** albo **2×**, więc widżet ma jedną albo dwie komórki szerokości i jedną albo dwie wysokości. Kamera może mieć do **3×** szerokości. Wykres nigdy nie ma szerokości jednej komórki. Na pulpicie z trzema kolumnami wskaźnik o szerokości dwóch komórek zajmuje dwie trzecie rzędu. To zwykle dobry kształt dla najważniejszego parametru.

## Co pokazuje widżet parametru {#what-a-parameter-widget-shows}

Widżety Wartość, Wskaźnik, Wykres i Stan pokazują zmierzony parametr i zawsze pokazują trzy rzeczy. Kafelki gniazd i urządzeń pokazują swój stan, bo nie stoi za nimi jeden odczyt.

- **Wartość**, dużymi znakami
- **Wiek** (`teraz`, `1g`, `2d`), czyli jak dawno źródło ostatnio potwierdziło wartość. Dla sondy to chwila, gdy jej urządzenie ostatnio się zgłosiło, więc stały odczyt pozostaje świeży. Dla wyniku testu kropelkowego albo ICP to chwila wykonania testu. Więcej w [Jak czytać pulpit](/help/mobile-dashboard#how-to-read-a-parameter-widget).
- **Źródło**, mały znaczek, który mówi, skąd pochodzi liczba

Widżet parametru nie ma własnego ustawienia zakresu ani źródła. Zakres pochodzi z progów alertów akwarium (przytrzymaj widżet na pulpicie), a źródło z [Mapowania parametrów](/help/mobile-probes). Dotknij widżetu na pulpicie, żeby zobaczyć jego pełną historię, każde źródło, które go zgłasza, i pasmo alertu.

## Wartość {#value}

To zwykła liczba. Pokazuje bieżący odczyt, jego jednostkę, wiek i źródło.

Używaj jej dla parametrów, które sprawdzasz po liczbie bardziej niż po trendzie, na przykład wapnia, magnezu albo azotanów.

## Wskaźnik {#gauge}

Wskaźnik to łuk z naniesionym zakresem alertu i znacznikiem na bieżącej wartości. Kolor znacznika mówi, gdzie jesteś: w zakresie, w dryfie albo poza nim.

Używaj go dla parametrów, którymi aktywnie zarządzasz, na przykład alkaliczności, pH, zasolenia albo temperatury.

:::note Wskaźnik niech ma co najmniej dwie kolumny szerokości
Przy jednej kolumnie łuk jest za mały, żeby szybko go odczytać. Jeśli brakuje miejsca, użyj widżetu **Wartość**.
:::

## Wykres {#graph}

Wykres to mała linia trendu w wybranym zakresie czasu: 1h, 6h, 24h, 7d, 30d albo 1y. Zaznacza maksimum i minimum i podpisuje bieżącą wartość.

Dla parametru, który testujesz (Tridentem albo testem kropelkowym), linia łączy Twoje prawdziwe testy. Jeśli w tym okresie jest tylko jeden test, linia biegnie od testu sprzed niego i nie ma maksimum ani minimum. Jeśli w okresie nie ma testu albo pojedynczego testu nie ma z czym połączyć, kafelek pokazuje **Zbieranie…** zamiast linii.

Używaj go do wszystkiego, co się zmienia, na przykład pH w ciągu dnia, temperatury w upał albo alkaliczności między dawkami.

Wykres ma zawsze **co najmniej dwie komórki szerokości**. Linia ściśnięta w jedną komórkę nic nie mówi, więc edytor na to nie pozwala.

:::note Wybierz zakres pasujący do parametru
pH waha się w cyklu dobowym, więc 24 godziny pokazują jego wzorzec. Alkaliczność zmienia się w ciągu dni, więc 7 albo 30 dni powie znacznie więcej.
:::

## Stan {#status}

Pokazuje odczyt jako zwykły tekst z kolorową kropką: w zakresie, w dryfie albo poza nim. Używaj go dla parametru, który nie ma przydatnego zakresu dla wskaźnika.

## Gniazdo {#outlet}

To przełącznik z trzema pozycjami dla gniazda Apex: **Auto**, **Wył.** i **Wł.** Wybierasz, którym gniazdem steruje.

- **Auto** oddaje gniazdo temu, co nim zwykle steruje. Może to być harmonogram, reguła albo kontroler, do którego należy.
- **Wył.** i **Wł.** to ręczne nadpisania. Obowiązują, dopóki ich nie zmienisz.

:::warning Ręczne nadpisania nie wygasają
Wył. oznacza wyłączone, dopóki nie ustawisz z powrotem Auto. Jeśli wyłączasz pompę powrotną na czas pracy w akwarium, po skończeniu ustaw ją z powrotem na Auto. Cora nie zrobi tego za Ciebie.
:::

## ReefBeat {#reefbeat}

To jeden kafelek dla całego urządzenia. Pokazuje jego własne podsumowanie zamiast pojedynczego parametru, na przykład stan ATO i zbiornika, głowice dozownika albo na ile dni wystarczy rolki maty. Wybierasz, które urządzenie pokazuje.

To, które urządzenia mogą mieć kafelek, zależy od tego, co podłączono. Zobacz [Podłączanie sprzętu](/help/mobile-connections).

## Kafelki dozowników {#doser-tiles}

Kafelek dozownika (Apex DŌS, ReefDose albo EcoTech Versa) pokazuje jeden wiersz na głowicę. Nazwa głowicy nigdy nie jest zmniejszana poniżej czytelnego rozmiaru. Na wysokim kafelku wiersz zajmuje dwie linie, z nazwą w pierwszej i tym, co zostało, w drugiej, na przykład *40d* i *2.8 L*. Na niskim kafelku linia ze szczegółami jest pomijana, a nazwa pozostaje czytelna.

To, co jest pierwsze, ustawiasz w **Pokaż pozostałe jako**: **Dni** albo **Mililitry (mL)**. Głowica ReefDose bez własnej nazwy jest pokazana jako nazwa urządzenia, a po niej „head” i jej numer. Kafelek dozownika Jecod jest tylko do odczytu i pokazuje plan dzienny, bo Jecod nie zgłasza, ile zostało w butelce.

---
title: Kontrola sprzętu z Cora Max
description: Strony urządzeń na dużym ekranie: sondy, gniazda, głowice dozujące, testery i pompy.
section: Cora Max
reviewed: 2026-09-27
order: 6
group: Equipment
---

Cora Max dosięga tego samego sprzętu co Twój telefon, z jedną stroną na urządzenie. Otwórz je z **Ustawienia → Urządzenia** albo dotykając kafelka urządzenia na pulpicie.

![Strona Apex na Cora Max](img/max-device-control.webp "Cykle karmienia i każde gniazdo, rozmieszczone dla ekranu ściennego.")

:::warning Te kontrolki działają na żywym sprzęcie
Nie ma podglądu i nie ma cofnięcia. Polecenie jest wysyłane w momencie dotknięcia, ale *wysłane* nie znaczy *wykonane*: wraca jako **Potwierdzono**, **Niepotwierdzone**, **Odmówiono** albo **Bez zmian**, i [Activity](/help/max-activity) jest miejscem, gdzie widzisz które.
:::

## Co ma stronę

| Urządzenie | Pokazuje |
|---|---|
| **Neptune Apex** | Sondy i gniazda, każde gniazdo przełączalne |
| **Trident** | Stan testu, poziomy reagentu i odpadów oraz możliwość rozpoczęcia testu |
| **DŌS**, w tym DŌS QD | Dozowanie każdej głowicy, harmonogram, runway i objętość pojemnika (z wstrzymaniem, napełnieniem, dozowaniem teraz i jednorazowym dwudziestosekundowym pomiarem) |
| **Red Sea ReefBeat** | To, czym jest jednostka: głowice dozujące, zbiornik, dni rolki, tryb pompy |
| **Jecod** | Tryb i intensywność pompy oraz jej program dnia |
| **Maxspect** *(beta)* | Tryb i prędkość dla **Gyre A** i **Gyre B**, **Stan pompy** (odliczanie czyszczenia, prąd głowicy A, zamontowane głowice, firmware) oraz jego harmonogram, tylko do podglądu |

Jeśli jednostka Red Sea zatrzyma się sama, jej strona mówi, co jest nie tak, i umieszcza rozwiązanie przy tym: **Wznów**, **Usuń stan awaryjny**, **Czujnik wyczyszczony**, **Nowa rolka już załadowana**, albo **Resetuj** dla głowicy dozującej.

## Głowice DŌS

Głowica DŌS musi zostać zmierzona raz, zanim Cora zdozuje nią ręcznie. **Zmierz, aby dozować** uruchamia głowicę na dwadzieścia sekund do pojemnika pomiarowego, a Ty wpisujesz, ile wyszło. Cora zachowuje jeden pomiar na głowicę i używa najnowszego, niezależnie które Cora Max go wykonało; strona głowicy pokazuje, gdzie i kiedy została zmierzona.

Po ręcznej dawce głowica, którą ustawiłeś na Off w Apex Fusion, zostaje Off. Każda inna głowica wraca do Auto.

### Do czego służy głowica

Każda głowica może mieć ustawiony **typ użycia**, z formularza ustawień: **Suplement**, **Podmiana wody: nowa słona woda wchodzi**, **Podmiana wody: stara woda wychodzi**, **Kalkwasser**, **Reaktor wapniowy**, **Pokarm** albo **Dolewka**, albo **Inne**. Typ użycia zmienia dwie rzeczy:

- **Jak duży pojemnik może śledzić.** Głowica Supplement śledzi do 20 litrów; każdy inny typ użycia może śledzić dużo większy pojemnik, do 500 litrów, więc głowica prowadząca podmianę wody albo reaktor wapniowy nie jest traktowana jak mała butelka dozująca.
- **Czy może wykonać dużą dawkę ręcznie.** Głowice Supplement i Food zachowują dzisiejszy mały, ostrożny sufit. Każdy inny typ użycia może otrzymać własny limit **Największa dawka ręczna**, do sztywnego sufitu 10 litrów, i własny **dzienny limit dla automatyzacji i Asystenta**.

Para do podmiany wody (nowa woda solna wchodzi, stara wychodzi) może być połączona jako **Sparowana głowica**, z kwotą **Ostrzeżenie o równowadze powyżej**: jeśli sumy dnia dla obu głowic rozjeżdżają się o więcej niż tę kwotę, Cora ostrzega Cię, bo para poza równowagą zwykle znaczy, że jedna strona nie pompuje jak oczekiwano.

### Jeśli duża dawka jest przerwana

Duża dawka tymczasowo zmienia to, co głowica robi na Apex, a potem przywraca jej normalny harmonogram. Jeśli połączenie zrywa się w połowie, Cora Max pokazuje baner na stronie tej głowicy: *"A large dose on [head] did not finish cleanly. Cora keeps trying to put its program back; check it in Apex Fusion."*

Sprawdź głowicę w Apex Fusion samodzielnie, a potem dotknij **Głowicę sprawdzono w Fusion**, aby zamknąć baner. Zrób to tylko po potwierdzeniu, że to własny harmonogram głowicy, nie program dozowania Cory, faktycznie działa.

**Jeśli to nie działa:** jeśli baner nie chce się zamknąć albo wciąż wraca, zobacz [Rozwiązywanie problemów](/help/troubleshooting).

## Harmonogramy

Programy dnia pomp Jecod mogą być tworzone przy ścianie tak samo jak na telefonie. Edytor jest ten sam: wykres dnia, lista okresów i wiersz akcji. Zobacz [Planowanie pracy sprzętu](/help/mobile-schedules).

Harmonogram gyre Maxspect *(beta)* można tutaj podglądać, ale nie zapisać. Ustaw go w aplikacji Maxspect.

## Gniazda

Gniazda są też dostępne z szuflady **Gniazda i karmienie** na dole pulpitu, która wypisuje gniazda włączone dla tego pulpitu w jednym miejscu (wszystkie, jeśli żadne nie zostało wybrane). Zobacz [Gniazda i kontrolki](/help/max-controls).

Głowice DŌS nigdy nie pojawiają się na liście gniazd, więc głowicy nie można tam włączyć i zostawić działającej; dozuj z jej własnej strony. Duży Apex z kilkoma modułami pokazuje wszystkie swoje gniazda i sondy.

## Materiały eksploatacyjne

Progi uzupełnienia (reagent, pojemniki, zbiorniki) są ustawiane z własnej strony urządzenia tutaj, dokładnie jak na telefonie. Zobacz [Materiały eksploatacyjne](/help/mobile-consumables).

## Zapisywanie i obliczanie przy akwarium

Dwie rzeczy są często wygodniejsze przy ścianie niż na telefonie:

- **Zapisz parametry**: wpisz wyniki testu na klawiaturze ekranowej, z menu akwarium
- **Kalkulator dawek**: wylicz korektę, wykorzystując objętość akwarium i siły Twoich produktów, ze strony parametru. Używa tej samej objętości i sił produktów co telefon, więc dawka wyliczona tutaj zgadza się z tą wyliczoną tam. Zobacz [Dozowanie](/help/mobile-dosing).

## Na drugim Cora Max

Gdy więcej niż jedno Cora Max pokazuje akwarium, jedno z nich odczytuje sprzęt tego akwarium; strony urządzeń nazywają je Cora Max przy akwarium. Inne wciąż otwierają strony urządzeń (plakietka stanu pokazująca **Chmura** znaczy, że ten ekran jest jednym z nich). Pokazują to, co Cora Max przy akwarium ostatnio odczytało, i jak dawno temu, i przekazują każde polecenie przez Cora Cloud do tego Cora Max, aby je wykonało.

Kilka rzeczy zostaje przy Cora Max przy akwarium:

- **Zmierz, aby dozować** i **Zmierz ponownie** pojawiają się tylko tam. Gdy głowica jest już zmierzona, **Dawkuj teraz** działa z każdego Cora Max.
- Harmonogram Jecod może być zmieniony z innego Cora Max tylko, jeśli Cora Max przy akwarium odczytało pompę w ostatniej godzinie, i nigdy dla pompy, która rozmawia tylko przez Bluetooth. Jedno **Zastosuj do pompy** stamtąd wysyła maksymalnie 12 zmian, więc wysyłaj większą edycję w częściach.

## Co zostało zmienione i przez co

Każda akcja jest zapisywana wraz z jej przyczyną. Zobacz [Aktywność i oś czasu](/help/mobile-activity).

---
title: Automatyzacje i sceny
description: Twórz reguły, które działają same (wyzwalacze, warunki, akcje), i łącz akcje w sceny.
section: Cora Mobile
reviewed: 2026-09-27
order: 17
group: Alerts and automation
---

Automatyzacja to reguła, którą Cora wykonuje za Ciebie: *gdy stanie się to, sprawdź tamto i zrób to.* Scena łączy kilka akcji w jedną całość, którą możesz uruchomić ręcznie albo zaplanować.

**Ustawienia → Automatyzacja.**

![Lista automatyzacji](img/mobile-automation.webp "Automatyzacje i Sceny to osobne zakładki. Każda reguła ma swój przełącznik.")

Na ekranie są dwie zakładki, **Automatyzacje** i **Sceny**, oraz przycisk **Nowa automatyzacja**. Przy każdej regule widać jednolinijkowy opis tego, co robi, przełącznik i menu do edycji albo usuwania. Reguła, która jeszcze ani razu nie zadziałała, ma odpowiednie oznaczenie.

:::warning Reguły sterują prawdziwym sprzętem
Reguła, która przełącza pompę, przełączy ją także wtedy, gdy nie patrzysz. Twórz reguły po jednej i sprawdź, czy każda robi to, czego się spodziewasz, zanim dodasz następną.
:::

## Z czego składa się reguła

Każda reguła ma te same trzy części:

**Wyzwalacz**: co ją uruchamia
**Warunki**: co musi być dodatkowo spełnione
**Akcje**: co reguła potem robi, po kolei

## Co może uruchomić regułę

Są cztery wyzwalacze:

| Wyzwalacz | Kiedy działa |
|---|---|
| **Parametr** | Parametr przekracza ustawioną wartość w wybranym kierunku |
| **Alert** | Alert się pojawia, znika albo jedno i drugie |
| **Harmonogram** | O wybranej godzinie, w Twojej strefie czasowej |
| **Stan urządzenia** | Urządzenie traci połączenie albo znów jest online |

## Warunki

Warunki decydują, czy akcje się wykonają. Masz zwykłe porównania (równe, różne, większe, mniejsze i tak dalej) i możesz je łączyć przez **i**, **lub** oraz **nie**.

Jest też warunek **kroku**, który sprawdza, jak poszedł *poprzedni* krok. Dzięki niemu napiszesz „spróbuj tego, a jeśli się nie uda, zrób coś innego”.

## Co może zrobić reguła

Akcje wymagające sprzętu pojawiają się tylko przy akwarium, które ma ten sprzęt:

| Akcja | Co robi |
|---|---|
| **Steruj sprzętem Apex** | Przełącza gniazdo |
| **Steruj sprzętem Red Sea** | Steruje urządzeniem ReefBeat |
| **Steruj pompą cyrkulacyjną** | Ustawia przepływ, tryb fali albo moc pompy Jecod. Może też użyć **Wstrzymaj na czas karmienia**, a wtedy Cora Max przy akwarium przywraca pompę po karmieniu |
| **Steruj sprzętem Cora** | Przełącza smart wtyczkę |
| **Steruj urządzeniem IR** | Wysyła polecenie podczerwienią |
| **Uruchom cykl karmienia Apex** | Zaczyna karmienie |
| **Uruchom test Trident** | Zleca test |
| **Powiadom mnie** | Wysyła Ci powiadomienie push |
| **Czekaj przed następnym krokiem** | Robi przerwę przed dalszym ciągiem |
| **Uruchom scenariusz** | Uruchamia scenę z wnętrza tej reguły |
| **Zarządzaj automatyzacją** | Włącza albo wyłącza inną regułę |
| **Zdawkuj z głowicy DŌS** | Podaje odmierzoną dawkę z głowicy DŌS |

:::warning Dawki z reguły nie da się cofnąć
Raz podanej dawki nie wyjmiesz z akwarium. Reguła może dozować tylko ze **skalibrowanej** głowicy. Dozowanie bez nadzoru ma limit **10 mL na głowicę na dobę** i żadna reguła go nie przekroczy, bez względu na to, jak jest napisana. Akcje dozowania pojawią się dopiero wtedy, gdy Cora rozpozna Twoje głowice jako głowice dozujące.
:::

:::note Przerwa porządkuje kroki w jednej regule
Dzięki przerwie jedna reguła może wykonać kroki po kolei, np. wyłączyć gniazdo, odczekać i włączyć je ponownie. Nie potrzebujesz do tego drugiej reguły ani harmonogramu.
:::

## Sceny

Scena to nazwana grupa akcji, np. „Podmiana wody”, „Tryb zdjęć” albo „Noc”. Uruchomisz ją ręcznie, z harmonogramu albo z innej reguły.

Scena może wywołać inną scenę. Cora nie uruchomi sceny zagnieżdżonej głębiej niż pozwala limit ani sceny, która wywołuje samą siebie. Taka pętla działałaby na akwarium bez końca.

Po uruchomieniu sceny zobaczysz krok po kroku, co się stało, także to, co się nie udało.

Gdy uruchamiasz scenę ręcznie, Cora najpierw prosi o potwierdzenie, bo scena może przełączyć kilka urządzeń naraz.

## Sceny tworzone na Cora Max

Sceny możesz też tworzyć i edytować bezpośrednio na Cora Max. Na telefonie i na Cora Max to ten sam zestaw scen, wspólny dla całego konta. Starszy Cora Max w domu nadal uruchomi scenę utworzoną na telefonie. Edycja na samym urządzeniu to nowsza funkcja, więc starszy Cora Max może pokazać scenę, ale nie pozwoli jej tam zmienić. Wtedy edytuj ją na telefonie.

## Wyłączanie reguły

Każda reguła ma przełącznik. Po wyłączeniu reguła zostaje zapisana. Przydaje się to, gdy chcesz wrócić do niej w kolejnym sezonie bez tworzenia jej od nowa.

## Co zrobiła reguła

Każda akcja reguły jest zapisywana z tą regułą jako źródłem. Znajdziesz je w **[Aktywności](/help/mobile-activity)**.

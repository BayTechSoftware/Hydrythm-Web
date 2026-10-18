---
title: Automatyzacje i sceny
description: Spraw, żeby Cora działała sama, gdy zmieni się odczyt, pojawi się alert, nadejdzie godzina albo urządzenie przejdzie w tryb offline, i łącz akcje w sceny uruchamiane jednym dotknięciem.
section: Cora Mobile
reviewed: 2026-10-18
order: 24
group: Alerts and automation
twin: max-automation
---

Automatyzacja to reguła, którą Cora wykonuje za Ciebie: *gdy stanie się to, sprawdź tamto, a potem zrób to.* Scena łączy kilka akcji w jedną całość, którą uruchamiasz, kiedy chcesz.

Przejdź do **Ustawienia → Automatyzacje**.

![Ekran Automatyzacje w Cora Mobile, z zakładkami Automatyzacje i Sceny](img/mobile-automation.webp "Automatyzacje i Sceny to osobne zakładki. Każda reguła ma własny przełącznik.")

Ekran ma dwie zakładki, **Automatyzacje** i **Sceny**, z przyciskiem **Nowa automatyzacja** albo **Nowa scena**. Każda reguła pokazuje jednolinijkowe podsumowanie, przełącznik i menu z **Edytuj** albo **Usuń**. Reguła, która jeszcze nie zadziałała, mówi o tym.

:::warning Reguły działają na prawdziwy sprzęt
Jeśli reguła przełącza pompę, pompa przełączy się także wtedy, gdy nie patrzysz. Twórz reguły po jednej i sprawdź, czy każda robi to, czego się spodziewasz, zanim dodasz następną.
:::

## Budowa reguły {#shape}

Każda automatyzacja ma trzy części.

- Wyzwalacz ją budzi.
- Warunki muszą być dodatkowo spełnione.
- Akcje to to, co potem robi, po kolei.

![Pusty formularz Nowa automatyzacja w Cora Mobile](img/mobile-rule-builder.webp "Nowa automatyzacja: wyzwalacze, warunki Jeśli, akcje, Inaczej jeśli i Inaczej, a potem czas wstrzymania i okno czasowe.")

## Co może obudzić regułę {#triggers}

Dodaj jeden albo więcej wyzwalaczy w **Gdy: dowolny wyzwalacz**. Każdy z nich uruchamia regułę.

| Wyzwalacz | Działa, gdy |
|---|---|
| **Gdy parametr się zmienia** | Parametr przekroczy ustawioną wartość. Wybierz **Kierunek**: **Wzrost**, **Spadek** albo **Każda zmiana** |
| **Gdy alert się aktywuje** | Alert zostaje **Zgłoszony**, **Usunięty** albo jedno i drugie. Możesz ograniczyć to do alertów **Próg** albo **Tempo zmiany**. |
| **O określonej godzinie** | O godzinie dnia, w Twojej strefie czasowej |
| **Gdy urządzenie traci połączenie** | Twój Cora Max przechodzi w tryb **Offline**, wraca **Online** albo jedno i drugie |

:::tip Dowiedz się, gdy Cora Max zniknie
Reguła z **Gdy urządzenie traci połączenie** i **Powiadom mnie** powie Ci, gdy Cora Max, który odczytuje Twój sprzęt, straci zasilanie albo Wi-Fi.
:::

## Warunki {#conditions}

Warunki decydują, czy akcje się wykonają. Dotknij **Dodaj warunek** i wybierz:

- **Porównanie parametru**, czyli odczyt powyżej, poniżej albo równy wartości
- **Parametr w / poza zakresem**
- **Alert aktywny**
- **Gniazdo jest wł. / wył.**, dla gniazda Apex
- **Godzina dnia**, czyli okno, na przykład od 22:00 do 06:00
- **Jak przebiegł wcześniejszy krok**, który sprawdza, czy wcześniejszy krok poszedł **OK**, czy został **Pominięto**. Użyj go do „spróbuj tego, a jeśli nie zadziała, zrób zamiast tego tamto”

Przy kilku warunkach ustaw **Dopasowanie** na **Wszystkie (I)** albo **Którykolwiek (LUB)**.

## Gałęzie i warunki kroków {#branches}

Automatyzacja może robić różne rzeczy w różnych przypadkach. Jej pierwszy blok to **Jeśli**. Dotknij **Inaczej jeśli**, żeby dodać kolejny przypadek, albo dodaj blok **Inaczej** na wszystko inne. Cora wykonuje pierwszy blok, którego warunki są spełnione.

Możesz też uzależnić pojedynczą akcję. Dotknij **Tylko jeśli…** przy tym kroku i nadaj mu własny warunek. Bez warunku krok wykonuje się zawsze.

## Kiedy może działać {#when-it-may-run}

- **Czas wstrzymania między wykonaniami** nie pozwala regule zadziałać ponownie za szybko. Zaczyna się od 10 min.
- **Wykonuj tylko między** ogranicza regułę do okna czasowego, na przykład tylko w dzień.
- **Testuj z wartościami na żywo** sprawdza regułę na bieżących odczytach akwarium, nic nie robiąc. Mówi, co *by się wykonało* albo dlaczego nic by się nie wykonało.

## Co może zrobić reguła {#actions}

Akcja, która wymaga sprzętu, pojawia się tylko przy akwarium, które ma ten sprzęt.

| Akcja | Co robi |
|---|---|
| **Steruj sprzętem Apex** | Przełącza gniazdo |
| **Uruchom cykl karmienia Apex** | Zaczyna karmienie. Apex kończy je według własnego timera |
| **Uruchom test Trident** | Zaczyna test. Każde uruchomienie zużywa odczynnik |
| **Zdawkuj z głowicy DŌS** | Podaje odmierzoną dawkę z głowicy DŌS |
| **Steruj sprzętem Red Sea** | Steruje urządzeniem ReefBeat |
| **Steruj pompą cyrkulacyjną** | Ustawia przepływ, tryb fali albo zasilanie pompy Jecod albo **Wstrzymaj na czas karmienia**. Cora Max przy akwarium przywraca pompę, gdy karmienie się skończy |
| **Powiadom mnie** | Wysyła Ci powiadomienie z własnym **Tytułem** i **Wiadomością** |
| **Czekaj przed następnym krokiem** | Robi przerwę przed kontynuacją |
| **Uruchom scenę** | Uruchamia scenę z wnętrza tej reguły |
| **Zarządzaj automatyzacją** | Włącza albo wyłącza inną regułę |
| **Utwórz zadanie konserwacyjne** | Dodaje pracę do listy [konserwacji](/help/mobile-maintenance) akwarium, na przykład wymianę wkładu skrubera CO2, gdy pH spadnie poniżej wartości |


:::warning Dawki nie da się cofnąć i ma limit
Dawki nie wyjmiesz z akwarium. Reguła może dozować tylko z głowicy, którą zmierzono funkcją **Zmierz, aby dozować** na Cora Max. Dawkę wykonuje Cora Max przy akwarium. Dozowanie z reguł ma limit **10 mL na głowicę dziennie**, niezależnie od tego, jak reguła jest napisana.
:::

:::note Co robi Utwórz zadanie konserwacyjne
Wybierz akwarium, a potem **Istniejące zadanie** (istniejące zadanie dostaje termin na teraz) albo **Nowe zadanie** (podaj **Nazwę zadania**). Nowe zadanie jest jednorazowe, z terminem od razu, a reguła nie tworzy go ponownie, dopóki jest otwarte. Dostajesz jedno powiadomienie, a jednorazowe zadanie znika z listy, gdy je wykonasz.
:::

:::note Czekanie jest krótkie
**Czekaj przed następnym krokiem** robi przerwę do 60 sekund, a gałąź może czekać łącznie 60 sekund. Po przerwie następny krok widzi świeże odczyty. Do dłuższego wstrzymania, na przykład pompy powrotnej wyłączonej na 30 minut podczas podmiany wody, użyj sceny z **Działaj przez** (niżej).
:::

## Sceny {#scenes}

Scena to nazwana grupa akcji, na przykład „Podmiana wody”, „Tryb zdjęć” albo „Noc”. Dotknij **Nowa automatyzacja** albo **Nowa scena** i wybierz **Scena** na górze. Scena nie ma wyzwalacza. Uruchamiasz ją przyciskiem **Uruchom teraz** na liście, z wnętrza reguły przez **Uruchom scenę** albo według harmonogramu przez regułę z **O określonej godzinie**.

**Działaj przez** ustala, jak długo trwa scena: liczbę minut albo godzin albo **Aż to zmienię**. Gdy czas minie, Cora przełącza gniazda sceny z powrotem do stanu sprzed sceny. Pozostały sprzęt zostaje taki, jakim zostawiła go scena. Gdy działa scena czasowa, lista pokazuje odliczanie i przycisk **Zatrzymaj**, który kończy ją wcześniej.

Jeśli scena przełącza ważne gniazdo, na przykład grzałkę, chłodziarkę, pompę powrotną albo dolewkę, Cora pyta przed jej uruchomieniem i wymienia te kroki. Możesz to wyłączyć przełącznikiem **Pytaj przed uruchomieniem** w scenie.

Scena może wywołać inną scenę, do 3 poziomów w głąb. Cora nie uruchomi sceny, która wywołuje samą siebie, bo mogłaby się zapętlić i ciągle działać na akwarium.

Po uruchomieniu sceny zobaczysz krok po kroku, co się stało, w tym wszystko, co się nie udało albo nie wykonało.

## Sceny utworzone na Cora Max {#scenes-on-cora-max}

Sceny możesz też tworzyć i edytować na Cora Max. To ten sam zestaw scen, wspólny dla całego konta. Starszy Cora Max nadal uruchomi scenę utworzoną w telefonie. Edycja na urządzeniu jest jednak nowsza, więc starszy Cora Max może pokazać scenę, ale nie pozwolić jej zmienić. Wtedy edytuj ją w telefonie.

## Wyłączanie reguły {#turning-a-rule-off}

Każda reguła ma przełącznik. Wyłączenie reguły zachowuje jej ustawienia, co przydaje się, gdy chcesz do niej wrócić w kolejnym sezonie.

## Co zrobiła reguła {#seeing-what-a-rule-did}

Każda akcja wykonana przez regułę jest zapisywana z przyczyną **Reguła automatyzacji**. Znajdziesz ją w [Aktywności](/help/mobile-activity).

Krok, który się nie powiódł albo musiałby czekać, nie zostaje w zawieszeniu. Wygasa od razu, przebieg jest zapisany jako nieudany, a Ty dostajesz powiadomienie z nazwą automatyzacji, krokiem i przyczyną. Krok nie udaje się na przykład wtedy, gdy jego urządzenie jest offline, żaden Cora Max nie może go wykonać, urządzenie go odrzuca albo nie odpowiada, albo grzałka lub chłodziarka została przełączona chwilę temu. Dla kroku na usuniętym akwarium nie dostajesz powiadomienia.

---
title: Automatyzacje i scenki
description: Zbuduj reguły, które działają same (wyzwalacze, warunki, akcje), i pogrupuj je w scenki.
section: Cora Mobile
reviewed: 2026-09-27
order: 17
group: Alerts and automation
---

Automatyzacja to reguła, którą Cora wykonuje za Ciebie: *gdy to się stanie, sprawdź to, potem zrób to.* Scenki grupują kilka akcji w jedną rzecz, którą możesz uruchomić albo zaplanować.

**Ustawienia → Automation.**

![Lista automatyzacji](img/mobile-automation.webp "Automations i Scenes to odrębne zakładki. Każda reguła ma przełącznik włączenia.")

Ekran ma dwie zakładki (**Automatyzacje** i **Sceny**) oraz przycisk **Nowa automatyzacja**. Każda reguła pokazuje jednolinijkowe podsumowanie tego, co robi, przełącznik włączenia i menu do edycji lub usunięcia. Reguła, która jeszcze nie zadziałała, jest tak oznaczona.

:::warning Działają na rzeczywistym sprzęcie
Reguła, która przełącza pompę, przełącza ją niezależnie od tego, czy patrzysz. Buduj po jednej naraz i sprawdzaj, czy każda robi to, czego oczekujesz, przed dodaniem następnej.
:::

## Kształt reguły

Każda reguła ma te same trzy części:

**Wyzwalacz**: co ją wybudza
**Conditions**: co też musi być prawdą
**Actions**: co potem robi, po kolei

## Co może wybudzić regułę

Cztery rzeczy:

| Wyzwalacz | Uruchamia się, gdy |
|---|---|
| **Parametr** | Parametr przekracza ustawioną przez Ciebie wartość, w wybranym przez Ciebie kierunku |
| **Alert** | Alert zostaje podniesiony, zamknięty, albo dowolne z tych dwóch |
| **Harmonogram** | Godzina dnia, w Twojej własnej strefie czasowej |
| **Device status** | Urządzenie przechodzi offline albo wraca |

## Warunki

Warunki decydują, czy akcje faktycznie się wykonają. Masz dostęp do zwykłych porównań (równa się, nie równa się, większe niż, mniejsze niż i tak dalej) i możesz je łączyć za pomocą **i**, **or** i **not**.

Jest też warunek **step**, który sprawdza, jak zakończył się *poprzedni* krok. To pozwala napisać "spróbuj tego; jeśli nie zadziałało, zrób to za to."

## Co reguła może zrobić

Akcja, która wymaga sprzętu, jest oferowana tylko na akwarium, które ten sprzęt ma:

| Akcja | Co robi |
|---|---|
| **Steruj sprzętem Apex** | Przełącza gniazdo |
| **Steruj sprzętem Red Sea** | Steruje jednostką ReefBeat |
| **Steruj pompą cyrkulacyjną** | Ustawia przepływ, tryb fali lub moc pompy Jecod, albo **Wstrzymaj na czas karmienia**: Cora Max przy akwarium przywraca pompę, gdy karmienie się kończy |
| **Steruj sprzętem Cora** | Przełącza smart wtyczkę |
| **Steruj urządzeniem IR** | Wysyła polecenie w podczerwieni |
| **Uruchom cykl karmienia Apex** | Uruchamia karmienie |
| **Uruchom test Trident** | Wywołuje test |
| **Powiadom mnie** | Wysyła Ci powiadomienie push |
| **Czekaj przed następnym krokiem** | Wstrzymuje przed kontynuowaniem |
| **Uruchom scenariusz** | Uruchamia inną scenkę z wewnątrz tej reguły |
| **Zarządzaj automatyzacją** | Włącza albo wyłącza inną regułę |
| **Zdawkuj z głowicy DŌS** | Wykonuje zmierzoną dawkę z głowicy DŌS |

:::warning Dozowanie z reguły jest nieodwracalne i ograniczone
Dawki nie można wycofać z akwarium. Głowica musi być **skalibrowana**, zanim reguła może z niej dozować, a dozowanie bez nadzoru jest ograniczone do **10 mL na głowicę dziennie**; reguła nie może tego przekroczyć, niezależnie jak jest napisana. Akcje dozowania pojawiają się tylko wtedy, gdy Twoje głowice są rozpoznane jako głowice dozujące.
:::

:::note Użyj Wait, aby uszeregować kroki w jednej regule
Wstrzymanie pozwala jednej regule wykonać uporządkowaną procedurę (na przykład wyłączenie gniazda, poczekanie, a potem włączenie go z powrotem) bez drugiej reguły i harmonogramu.
:::

## Scenki

Scenka to nazwana grupa akcji, którą możesz uruchomić na żądanie, z harmonogramu albo z wewnątrz innej reguły: "Podmiana wody", "Tryb zdjęcia", "Noc".

Scenka może wywołać inną scenkę. Cora odmawia uruchomienia scenki zagnieżdżonej głębiej niż limit głębokości i odmawia scenki, która wywołałaby samą siebie, aby zapobiec pętli, która działałaby na akwarium bez końca.

Po uruchomieniu scenki dostajesz informację, co się stało, krok po kroku, w tym o wszystkim, co się nie powiodło.

Ręczne uruchomienie scenki prosi najpierw o potwierdzenie, bo scenka może przełączyć kilka urządzeń jednocześnie.

## Scenki tworzone na Cora Max

Scenki można też budować i edytować prosto na tablecie Cora Max, nie tylko na telefonie: to jest ten sam zestaw scenek w obu przypadkach, wspólny dla całego konta. Jeśli gospodarstwo domowe ma starsze Cora Max, może wciąż uruchomić scenkę utworzoną na telefonie; tylko edycja na samym urządzeniu jest nowszą możliwością, więc starszy tablet może pokazać scenkę bez umożliwienia jej zmiany tam. Edytuj ją za to z telefonu.

## Wyłączanie reguły

Każda reguła ma przełącznik włączenia. Jego wyłączenie zachowuje definicję reguły, przydatne, gdy chcesz mieć regułę z powrotem w następnym sezonie, a nie budować ją od nowa.

## Sprawdzanie, co reguła zrobiła

Każda akcja podjęta przez regułę jest zapisywana z regułą jako jej przyczyną. Zobacz **[Aktywność](/help/mobile-activity)**.

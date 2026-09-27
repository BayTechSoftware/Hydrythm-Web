---
title: Ekran główny Cora Max
description: Co znaczy wszystko na wyświetlaczu Cora Max: górny pasek, siatka pulpitu i szuflada gniazd.
section: Cora Max
reviewed: 2026-09-27
order: 2
group: Getting started
---

Cora Max pokazuje jedno akwarium naraz, wypełniając ekran odczytami na żywo, które można przeczytać z drugiego końca pokoju.

![Ekran główny Cora Max](img/max-home.webp "Jedno akwarium, wypełniające ekran.")

## Górny pasek

Od lewej do prawej:

- **Ikona siatki** otwiera Reef Room, przegląd każdego akwarium, które ten ekran pokazuje
- **Nazwa akwarium**, ze strzałką. Dotknięcie jej otwiera **menu akwarium**: każdy ekran dla wyświetlanego akwarium, od zapisania wyniku testu do rozmieszczania pulpitu. Pełna lista jest poniżej.
- **Plakietki alertów**: wszystko aktualnie poza zakresem, z **+n**, gdy jest więcej, niż się mieści. Dotknij, aby zobaczyć wszystkie.
- **Zegar**
- **Plakietka stanu**: co ten ekran robi w tej chwili. Zielony jest sprawny, bursztynowy wymaga uwagi, czerwony to usterka. Pełne słownictwo jest poniżej.
- **Bateria i Wi-Fi**
- **Ikona urządzeń**: wszystko podłączone i jak sobie radzi
- **Ikona Reef Buddy**: otwiera dzisiejszy briefing. Punkt znaczy, że briefing nie został jeszcze przeczytany
- **Ikona Cora Assistant**: uruchamia rozmowę głosową
- **Zębatka**: ustawienia

### Co znaczy plakietka stanu

| Plakietka | Znaczenie |
|---|---|
| **Online** | Ten ekran zbiera Twoje odczyty i są one aktualne |
| **Chmura** | Inne Cora zbiera odczyty tego akwarium, a ten ekran je pokazuje. Równie aktualne jak **Online**; z więcej niż jednym Cora, ekran, który nie zbiera danych, pokazuje to |
| **Odpytywanie Apex**, **Głos aktywny** | Pracuje nad czymś w tej chwili |
| **Odpytywanie wyłączone** | Zbieranie jest wyłączone dla tego akwarium. Możesz je włączyć z powrotem z Cora Mobile |
| **Aktualizowanie** | Zbieranie jest wstrzymane, podczas gdy instaluje się aktualizacja |
| **Nieaktualne** | Odczyty przestały przychodzić. Ekran pokazuje ostatni otrzymany |
| **Apex retry 12s** | Twój Apex nie odpowiedział. Cora Max spróbuje ponownie, gdy odliczanie się skończy |
| **Synchronizacja z chmurą nie powiodła się** | Twój Apex odpowiedział, ale jego odczyty nie mogły zostać zapisane w Cora Cloud, więc pulpit zostaje w tyle. Cora Max wciąż próbuje ponownie |
| **Offline** | Brak połączenia. Ekran pokazuje ostatnie otrzymane dane |
| **Offline, retrying in 45s** | Twoja sieć działa, ale Cora Cloud jest niedostępna od ponad 30 sekund. Cora Max łączy się z powrotem sama; odliczanie to czas do kolejnej próby |
| **Główne Cora offline** | Ten ekran jest drugim Cora Max dla tego akwarium, a **główne Cora Max** (to przypięte do odpytywania sprzętu tego akwarium) przeszło offline. Ten ekran pokazuje dalej ostatnie dane, które ma, aż główne wróci, albo aż wybierzesz inne główne Cora Max. Zobacz [Więcej niż jedno urządzenie Cora](/help/mobile-multi-device) |
| **Hasło Apex** | Twój Apex odrzucił zapisane hasło. Zobacz [Rozwiązywanie problemów](/help/troubleshooting) |

:::note Jak działa odliczanie ponownych prób
Cora Max próbuje połączyć się ponownie w ustalonym tempie: około 15 sekund po pierwszym zerwaniu, 15 sekund po tym, potem dwa razy po 30 sekund, a potem raz na minutę, aż się powiedzie. Nie próbuje natychmiast i nie poddaje się; ekran pokazujący **Offline, retrying in 45s** robi dokładnie to, co powinien.
:::

:::warning Cora Assistant zaczyna słuchać od razu
Dotknięcie ikony Cora Assistant zaczyna żywą sesję głosową. Jeśli chciałeś otworzyć ustawienia, to jest zębatka po prawej stronie.
:::

## Pulpit

Reszta ekranu to pulpit: ustalona siatka widżetów, wszystkie widoczne naraz. Pulpit Cora Max się nie przewija.

Widżety działają tak samo jak na telefonie, w rozmiarze czytelnym z odległości. Zobacz **[Opis widżetów](/help/mobile-widgets)** po to, co każdy kształt pokazuje, i **[Edytowanie pulpitu Cora Max](/help/max-dashboard-editing)**, aby zmienić, co na nim jest.

Każdy widżet pokazujący zmierzony parametr niesie swój **wiek** i swoje **źródło**, tak jak na telefonie. Liczba z `2d` przy niej ma dwa dni i jest pokazana jako taka. Kafelki urządzeń i kontrolek pokazują za to własny stan.

## Menu akwarium

![Menu akwarium](img/max-menu.webp "Wszystko dla aktualnego akwarium, z nazwy akwarium na górnym pasku.")

Dotknięcie nazwy akwarium otwiera menu dla akwarium aktualnie na ekranie:

| Pozycja | Otwiera |
|---|---|
| **Zapisz parametry** | Wpisanie odczytów z testu kroplowego na klawiaturze ekranowej |
| **Dziennik** | [Dziennik](/help/mobile-journal) dla tego akwarium |
| **Reef Buddy** | Aktualny [briefing](/help/mobile-reef-buddy) |
| **Raporty zdrowia** | Oceny zdrowia |
| **Konserwacja** | [Listę zadań](/help/mobile-maintenance) |
| **Raporty ICP** | Przesłane [wyniki laboratoryjne](/help/mobile-icp-health) |
| **Alerty** | Zdrowe pasmo dla każdej metryki tego akwarium |
| **Obsada** | [Inwentarz](/help/mobile-livestock) tego akwarium, tylko do odczytu na tym ekranie |
| **Aktywność** | [Każde gniazdo, karmienie i dawkę](/help/max-activity) i co z tego wynikło |
| **Układ panelu** | [Rozmieszczenie widżetów na tym ekranie](/help/max-dashboard-editing) |
| **Ustawienia akwarium** | Pełny ekran ustawień tego akwarium |

## Przełączanie akwariów

Użyj **ikony siatki** po lewej stronie górnego paska, aby dostać się do [Reef Room](/help/max-reef-room), potem otwórz akwarium, które chcesz. Każde akwarium zachowuje swój własny układ pulpitu, więc cały ekran się zmienia, gdy przechodzisz między nimi.

## Szuflada Outlets & Feed

Zakładka na dole ekranu wysuwa szufladę z każdym gniazdem w systemie i kontrolkami karmienia.

- **Outlets**: każde przełączane między Auto, Off i On
- **Karmienie**: wstrzymuje właściwy sprzęt na czas karmienia i wszystko potem przywraca

:::warning Ta szuflada steruje rzeczywistym sprzętem
Wszystko w niej działa na rzeczywistym sprzęcie. Polecenie jest wysyłane w momencie dotknięcia, ale *wysłane* nie znaczy *wykonane*; wraca jako Confirmed, Unconfirmed, Refused albo No change, i [Activity](/help/max-activity) jest miejscem, gdzie widzisz które. Tryb karmienia jest bezpiecznym sposobem na wstrzymanie przepływu na czas karmienia, bo przywraca wszystko samo; ręczne Off zostaje wyłączone, aż to zmienisz z powrotem.
:::

## Jeśli coś wygląda nie na miejscu

Jeśli odczyty wyglądają nieaktualnie albo plakietka stanu jest bursztynowa albo czerwona, zacznij od **[Rozwiązywania problemów](/help/troubleshooting)**.

---
title: Dodawanie, edytowanie i usuwanie urządzeń
description: Dodaj sprzęt do Cory, przypisz go do akwarium, zmień jego nazwę, sprawdź, czy działa poprawnie, i usuń go, wszystko z zakładki Urządzenia.
section: Cora Mobile
reviewed: 2026-10-13
order: 11
group: Equipment
twin: max-devices
---

W zakładce **Urządzenia** dodajesz, przypisujesz, nazywasz, sprawdzasz i usuwasz każdy element sprzętu. Urządzenia są pogrupowane według marek, a każdą grupę możesz zwinąć.

![Zakładka Urządzenia](img/mobile-devices.webp "Sprzęt pogrupowany według marek. Każdą grupę można zwinąć.")

## Dodawanie sprzętu {#adding-equipment}

1. W zakładce **Urządzenia** dotknij **Dodaj urządzenie**.
2. Wybierz markę: **Cora**, **Neptune Apex**, **Red Sea**, **Jecod** albo **AquaWiz**.
3. Wykonaj kroki dla danej marki. W zależności od marki to skanowanie sieci, adres IP, logowanie albo klucz urządzenia. [Podłączanie sprzętu](/help/mobile-connections) opisuje kroki dla każdej marki.
4. Wybierz akwarium, do którego należy.

![Lista marek w Dodaj urządzenie](img/mobile-add-device-brands.webp "Wybierz markę dodawanego urządzenia.")



:::note Bez Cora Max część sprzętu działa tylko lokalnie
Ze sprzętem Neptune Apex, Red Sea i Jecod łączysz się przez sieć domową albo Bluetooth. Bez Cora Max ekran dodawania pokazuje *Bez Cora Max ta integracja działa tylko lokalnie w aplikacji Mobile.* Telefon odczytuje go i nim steruje tylko wtedy, gdy jest w tej samej sieci (albo w zasięgu Bluetooth). Poza domem widzisz ostatnie odczyty zapisane przez telefon i nie możesz nim sterować. Cora Max przy akwarium odczytuje go przez całą dobę i przekazuje Twoje polecenia. Więcej w [Podłączaniu sprzętu](/help/mobile-connections#local-only).
:::

Gdy dodajesz sprzęt ze swojej sieci, telefon musi być w tej samej sieci co sprzęt.

### Pojemność Bluetooth {#bluetooth-capacity}

Cora Max dzieli swój Bluetooth między cały sprzęt, który odczytuje, więc nadąży tylko z ograniczoną liczbą urządzeń. Gdy dodajesz pompę Jecod łączącą się przez Bluetooth, Cora najpierw sprawdza, jak bardzo obciążony jest Cora Max akwarium. Zwykle nic nie widzisz. W przeciwnym razie pojawia się jeden z dwóch komunikatów:

- **Bluetooth robi się zajęty**: *Ten Cora Max zbliża się do limitu Bluetooth. Więcej urządzeń może aktualizować się rzadziej. Dodaj drugi Cora Max, jeśli planujesz dodać więcej.* Dotknij **Dalej**, aby mimo to dodać urządzenie, albo **Anuluj**.
- **Osiągnięto limit Bluetooth**: *Ten Cora Max osiągnął limit Bluetooth. Dodaj drugi Cora Max dla tych urządzeń.* Urządzenie nie zostaje dodane. Dotknij **OK**.

Cora sprawdza główny Cora Max akwarium albo, jeśli żaden nie jest wybrany, Cora Max z największym zapasem. Więcej w [Więcej niż jedno urządzenie Cora](/help/mobile-multi-device#primary-cora-max).

## Parowanie Cora Max {#pairing-a-cora-max}

![Ekran Dodaj swoje Cora w Cora Mobile, szukający urządzeń](img/mobile-add-device.webp "Dodaj urządzenie, potem Cora. Cora Mobile szuka w Twojej sieci Wi-Fi i przez Bluetooth, a niżej jest Wpisz adres IP ręcznie.")

**Cora** służy do parowania nowego Cora Max. Znajduje urządzenia już podłączone do Twojej sieci Wi-Fi albo pobliskie przez Bluetooth. Jeśli nie może znaleźć Twojego, użyj **Wpisz adres IP ręcznie** na tym samym ekranie. Pełny opis jest w [Konfiguracji Cora Max](/help/max-setup).

## Strona urządzenia {#a-devices-page}

Dotknij dowolnego urządzenia na liście, żeby otworzyć jego stronę. Najpierw są jego elementy sterowania, a potem sekcje, które działają tak samo dla każdej marki.

- **Stan** pokazuje **Model**, **Numer seryjny**, **Oprogramowanie** i to, kiedy Cora ostatnio miała z nim kontakt (**Ostatnio widziano**).
- **Akwaria** pokazuje, do którego akwarium (albo akwariów) jest przypisane. Dotknij **Zmień**, żeby przypisać je inaczej.
- **Połączenie** to miejsce, w którym edytujesz jego adres IP, dane logowania albo klucz urządzenia.
- **Usuń urządzenie**, na samym dole.

Cora Max i Neptune Apex mogą obsługiwać więcej niż jedno akwarium, więc ich wybór akwarium to lista z polami wyboru. Cora Max można przypisać do maksymalnie czterech. Zobacz [Więcej niż jedno urządzenie Cora](/help/mobile-multi-device). Wszystko inne obsługuje jedno akwarium naraz. Wybranie innego przenosi tam urządzenie i zdejmuje je ze starego.

:::warning Przypisz akwarium, zanim zaczniesz polegać na odczytach
Urządzenie bez akwarium nadal raportuje, ale jego liczby nie mają gdzie trafić. Jeśli właśnie dodane urządzenie nie pokazuje się na pulpicie, najpierw sprawdź to.
:::

Co robią elementy sterowania każdej marki, opisuje [Sterowanie sprzętem](/help/mobile-device-control).

## Zmiana nazwy {#renaming}

Otwórz urządzenie i dotknij ołówka obok nazwy. Użyj nazwy, której używasz na co dzień, na przykład „Powrotna”, „Lewy gyre” albo „Grzałka w sumpie”. Nazwa pojawia się na widżetach, w alertach i we wszystkim, o co pytasz Corę.

Nazwa może mieć do 40 znaków. Zostaw ją pustą, żeby wrócić do własnej nazwy urządzenia. Jeśli dwa urządzenia tego samego rodzaju nie mają nazwy, Cora odróżnia je krótkim kodem po nazwie. Cora nigdy nie używa numeru seryjnego jako nazwy.

Nowa nazwa obowiązuje tylko w Corze. Nie zmienia nazwy w aplikacji producenta.

## Czy urządzenie działa poprawnie {#health}

Każde urządzenie to jeden wiersz w zakładce Urządzenia, z ikoną, nazwą, modelem i akwarium. Kropka w wierszu pokazuje jego stan.

| Kropka | Co oznacza |
|---|---|
| Szara | Cora jeszcze nie wie |
| Zielona | Działa normalnie |
| Pomarańczowa | Ostrzeżenie albo usterka |
| Czerwona | Offline |

Więcej zobaczysz po otwarciu urządzenia. Jego sekcja **Stan** pokazuje, kiedy Cora ostatnio miała z nim kontakt. Dobrze, gdy czas jest niedawny i nie ma ostrzeżenia.

| Co widzisz | Co oznacza |
|---|---|
| Niedawny czas aktualizacji | Działa normalnie |
| „Zaktualizowano 3 godz. temu” przy czymś, co raportuje tylko co kilka godzin | Wszystko w porządku |
| „Nie udało się połączyć…” | Problem z siecią albo urządzenie jest wyłączone |
| „…odmówiło logowania” | Konto producenta trzeba połączyć ponownie. Otwórz urządzenie i zaloguj się jeszcze raz |
| Starsze odczyty, gdy jesteś poza domem | Normalne dla Apex, Red Sea i Jecod bez Cora Max przy akwarium (zobacz wyżej) |
| Nic | Urządzenie nigdy nie raportowało. Sprawdź przypisanie do akwarium i połączenie |

Gdy urządzenie przestanie raportować, Cora może Cię o tym powiadomić. Czasy opisują [Alerty i progi](/help/mobile-alerts). W innych sprawach zobacz [Rozwiązywanie problemów](/help/troubleshooting).

## Usuwanie urządzenia {#removing-a-device}

Otwórz urządzenie i dotknij **Usuń urządzenie** albo przesuń jego wiersz w lewo w zakładce Urządzenia. Cora poprosi o potwierdzenie: *„{name} zostanie usunięty z Cora. Samo urządzenie nie jest resetowane ani zmieniane.”*

**Twoje odczyty zostają.** Usunięcie urządzenia sprawia, że Cora przestaje zbierać z niego nowe dane. Zebrana już historia zostaje przy akwarium, a każdy widżet, który z niego korzystał, zachowuje wcześniejsze odczyty.

Tracisz połączenie na żywo. Jeśli urządzenie łączyło się przez konto producenta, tracisz też zapisane dane logowania, więc po ponownym dodaniu trzeba będzie znów się zalogować.

:::tip Wycisz uciążliwe urządzenie bez usuwania
Jeśli urządzenie działa dobrze, ale za często wywołuje alerty, zmień jego progi albo ustawienia powiadomień w [Alertach i progach](/help/mobile-alerts). Zachowasz połączenie i dane, a hałas ustanie.
:::

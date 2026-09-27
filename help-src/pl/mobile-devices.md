---
title: Dodawanie, edytowanie i usuwanie urządzeń
description: Jak dodać sprzęt do Cory, przypisać go do akwarium, zmienić jego nazwę i usunąć go bez problemów.
section: Cora Mobile
reviewed: 2026-09-27
order: 9
group: Equipment
---

Zakładka **Urządzenia** to wszystko, co masz podłączone, pogrupowane według marki. Każda grupa się zwija, więc pokój pełen sprzętu zostaje czytelny.

![Zakładka Devices](img/mobile-devices.webp "Sprzęt jest pogrupowany według marki. Każda grupa się zwija.")

## Dodawanie sprzętu

Pod listą znajdują się trzy przyciski, które robią różne rzeczy:

| Przycisk | Dodaje |
|---|---|
| **Dodaj urządzenie** | Cora Max. Znajduje urządzenia już w Twojej sieci Wi-Fi albo pobliskie przez Bluetooth. **Wpisz adres IP ręcznie** znajduje się na tym samym ekranie, jeśli wyszukiwanie go nie znajdzie. |
| **Znajdź pompę w Twojej sieci** | Pompy Jecod, które ogłaszają się w lokalnej sieci |
| **Dodaj AquaWiz** | Kontroler AquaWiz, przez Twoje konto AquaWiz |

![Dodawanie Cora Max](img/mobile-add-device.webp "Add Device przeszukuje Wi-Fi i Bluetooth w poszukiwaniu Cora Max.")

Inny sprzęt (Neptune Apex i Red Sea ReefBeat) łączy się z poziomu akwarium, a nie z tej listy. Zobacz [Podłączanie sprzętu](/help/mobile-connections).

Dodawanie sprzętu takiego jak grzałka, pompa czy skimmer oferuje **autouzupełnianie** marki i modelu: zacznij pisać, a Cora zaproponuje coś z obszernej, zweryfikowanej listy marek sprzętu. Jeśli Twojej nie ma na liście, wpisz ją mimo to; Cora zachowa to, co wpiszesz.

:::note Cora i Twój telefon muszą być w tej samej sieci
Sprzęt wykryty lokalnie musi być w tej samej sieci co Twój telefon w momencie dodawania. **Po konfiguracji jest wciąż dostępny tylko w tej sieci** (lub przez Bluetooth, dla urządzeń, które go używają), o ile jakieś urządzenie Cora na miejscu nie może go odpytać za Ciebie.

Sprzęt, który poprawnie odczytuje się w domu, może więc pokazywać starsze wartości, gdy jesteś poza domem, o ile żaden Cora Max na miejscu nie może go odpytywać. To odzwierciedla, skąd sprzęt jest dostępny, a nie usterkę.
:::

## Przypisywanie urządzenia do akwarium

Większość sprzętu należy do dokładnie jednego akwarium, i to jest to, co sprawia, że jego odczyty pojawiają się na pulpicie tego akwarium.

**Cora Max jest wyjątkiem**: można je przypisać do maksymalnie czterech akwariów i przełącza się między nimi na ekranie. Zobacz [Więcej niż jedno urządzenie Cora](/help/mobile-multi-device).

Otwórz urządzenie i wybierz **Akwarium**. Jeśli prowadzisz więcej niż jeden system, to jest ustawienie, które ma największe znaczenie: grzałka przypisana do złego akwarium zgłasza się doskonale, tylko w złe miejsce.

:::warning Przypisz akwarium, zanim zaczniesz ufać odczytom
Urządzenie bez akwarium wciąż zgłasza dane, ale jego liczby nie mają gdzie wylądować. Jeśli właśnie dodane urządzenie nie pojawia się na pulpicie, sprawdź to najpierw.
:::

## Zmiana nazwy

Otwórz urządzenie i zmień jego nazwę. Użyj nazwy, którą stosujesz na co dzień: "Powrotna", "Lewy gyre", "Grzałka w sumpie". Nazwa pojawia się na widżetach, w alertach i we wszystkim, o co pytasz Corę, więc nazwa, która coś dla Ciebie znaczy, sprawia, że wszystko dalej jest jasne.

Zmiana nazwy działa tylko w Corze. Nie zmienia nazwy w aplikacji producenta.

## Sprawdzanie, czy urządzenie jest sprawne

Każdy wiersz pokazuje swój aktualny stan. To, co chcesz zobaczyć, to niedawny czas aktualizacji i brak ostrzeżenia.

| Co widzisz | Co to znaczy |
|---|---|
| Niedawny czas aktualizacji | Działa normalnie |
| "Zaktualizowano 3 godz. temu" na czymś, co zgłasza się co godzinę | W porządku |
| "Nie można było się połączyć…" | Problem z siecią albo urządzenie jest wyłączone |
| "…odrzucił logowanie" | Konto producenta wymaga ponownego połączenia; otwórz urządzenie i zaloguj się ponownie |
| Nic | Nigdy się nie zgłosiło; sprawdź przypisanie akwarium i połączenie |

## Usuwanie urządzenia

Otwórz urządzenie i wybierz **Usuń**. Zostaniesz poproszony o potwierdzenie i poinformowany, co dokładnie zostanie usunięte.

**Twoje odczyty są zachowywane.** Usunięcie urządzenia zatrzymuje zbieranie nowych danych przez Corę; historia, którą już zebrano, zostaje przy akwarium, a każdy widżet skierowany na to urządzenie zachowuje swoje wcześniejsze odczyty.

To, co utracisz, to bieżące połączenie oraz, jeśli urządzenie łączyło się przez konto producenta, zapisane logowanie. Dodanie go z powrotem oznacza ponowne zalogowanie.

:::tip Ucisz hałaśliwe urządzenie bez jego usuwania
Jeśli urządzenie działa poprawnie, ale zbyt często alertuje, dostosuj jego progi albo ustawienia powiadomień; zobacz **[Alerty i progi](/help/mobile-alerts)**. To zachowuje połączenie i dane, jednocześnie zatrzymując hałas.
:::

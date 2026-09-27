---
title: Dodawanie, edytowanie i usuwanie urządzeń
description: Jak dodać sprzęt do Cory, przypisać go do akwarium, zmienić jego nazwę i bezpiecznie go usunąć.
section: Cora Mobile
reviewed: 2026-09-27
order: 9
group: Equipment
---

W zakładce **Urządzenia** jest cały podłączony sprzęt, pogrupowany według marek. Każdą grupę można zwinąć, więc nawet przy dużej ilości sprzętu lista pozostaje czytelna.

![Zakładka Urządzenia](img/mobile-devices.webp "Sprzęt pogrupowany według marek. Każdą grupę można zwinąć.")

## Dodawanie sprzętu

Pod listą są trzy przyciski i każdy służy do czegoś innego:

| Przycisk | Co dodaje |
|---|---|
| **Dodaj urządzenie** | Cora Max. Wyszukuje urządzenia w Twojej sieci Wi-Fi albo w pobliżu przez Bluetooth. Jeśli wyszukiwanie nic nie znajdzie, na tym samym ekranie jest przycisk **Wpisz adres IP ręcznie**. |
| **Znajdź pompę w Twojej sieci** | Pompy Jecod, które same ogłaszają się w sieci lokalnej |
| **Dodaj AquaWiz** | Kontroler AquaWiz, przez Twoje konto AquaWiz |

![Dodawanie Cora Max](img/mobile-add-device.webp "Dodaj urządzenie szuka Cora Max przez Wi-Fi i Bluetooth.")

Pozostały sprzęt, czyli Neptune Apex i Red Sea ReefBeat, podłączasz z poziomu akwarium, a nie z tej listy. Więcej w [Podłączaniu sprzętu](/help/mobile-connections).

Gdy dodajesz sprzęt, np. grzałkę, pompę albo odpieniacz, Cora **podpowiada** markę i model. Zacznij pisać, a Cora zaproponuje nazwy z dużej, sprawdzonej listy marek. Jeśli Twojej marki nie ma, i tak ją wpisz. Cora zapisze to, co wpiszesz.

:::note Cora i telefon muszą być w tej samej sieci
Sprzęt wykrywany lokalnie musi przy dodawaniu być w tej samej sieci co telefon. **Po konfiguracji też jest osiągalny tylko w tej sieci** (albo przez Bluetooth, jeśli z niego korzysta), chyba że na miejscu jest urządzenie Cora, które się z nim połączy.

Sprzęt, który w domu pokazuje dobre odczyty, poza domem może więc pokazywać starsze wartości, jeśli na miejscu nie ma Cora Max, który by go odpytywał. To nie usterka. Po prostu sprzęt jest osiągalny tylko z określonego miejsca.
:::

## Przypisanie urządzenia do akwarium

Większość sprzętu należy do dokładnie jednego akwarium. Dzięki temu jego odczyty pojawiają się na pulpicie tego akwarium.

**Wyjątkiem jest Cora Max.** Można go przypisać do maksymalnie czterech akwariów i przełączać się między nimi na ekranie. Szczegóły są na stronie [Więcej niż jedno urządzenie Cora](/help/mobile-multi-device).

Otwórz urządzenie i wybierz **Akwarium**. Jeśli masz więcej niż jeden system, to najważniejsze ustawienie. Grzałka przypisana do złego akwarium działa bez zarzutu, tylko jej odczyty trafiają w złe miejsce.

:::warning Przypisz akwarium, zanim zaczniesz polegać na odczytach
Urządzenie bez akwarium nadal wysyła odczyty, ale nie mają one gdzie trafić. Jeśli nowo dodane urządzenie nie pojawia się na pulpicie, najpierw sprawdź właśnie to.
:::

## Zmiana nazwy

Otwórz urządzenie i zmień nazwę. Nazwij je tak, jak mówisz o nim na co dzień, np. „Powrotna”, „Lewy gyre”, „Grzałka w sumpie”. Nazwa pojawia się na widżetach, w alertach i w rozmowach z Corą, więc czytelna dla Ciebie nazwa ułatwia wszystko.

Nowa nazwa obowiązuje tylko w Corze. W aplikacji producenta nazwa się nie zmienia.

## Czy urządzenie działa poprawnie

Każdy wiersz pokazuje bieżący stan. Dobrze, gdy widać niedawny czas aktualizacji i żadnego ostrzeżenia.

| Co widzisz | Co to znaczy |
|---|---|
| Niedawny czas aktualizacji | Wszystko działa |
| „Zaktualizowano 3 godz. temu” przy urządzeniu, które zgłasza się tylko co kilka godzin | Wszystko w porządku |
| „Nie udało się połączyć…” | Problem z siecią albo urządzenie jest wyłączone |
| „…odmówiło logowania” | Trzeba ponownie połączyć konto producenta. Otwórz urządzenie i zaloguj się jeszcze raz |
| Nic | Urządzenie nigdy nie wysłało danych. Sprawdź przypisanie do akwarium i połączenie |

## Usuwanie urządzenia

Otwórz urządzenie i wybierz **Usuń**. Cora poprosi o potwierdzenie i powie dokładnie, co zostanie usunięte.

**Odczyty zostają.** Po usunięciu urządzenia Cora przestaje zbierać z niego nowe dane. Zebrana historia zostaje przy akwarium, a widżety, które z niego korzystały, zachowują wcześniejsze odczyty.

Tracisz połączenie na żywo, a jeśli urządzenie łączyło się przez konto producenta, także zapisane dane logowania. Gdy dodasz je ponownie, trzeba będzie znów się zalogować.

:::tip Wycisz uciążliwe urządzenie bez usuwania
Jeśli urządzenie działa dobrze, ale za często wywołuje alerty, zmień jego progi albo ustawienia powiadomień. Więcej w **[Alertach i progach](/help/mobile-alerts)**. Połączenie i dane zostają, a powiadomień będzie mniej.
:::

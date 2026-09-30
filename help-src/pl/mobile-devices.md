---
title: Dodawanie, edytowanie i usuwanie urządzeń
description: Jak dodać sprzęt do Cory, przypisać go do akwarium i bezpiecznie go usunąć, wszystko w jednym miejscu.
section: Cora Mobile
reviewed: 2026-09-30
order: 9
group: Equipment
---

Dodawaj, edytuj, przypisuj i usuwaj każde urządzenie w zakładce **Urządzenia**, pogrupowane według marek. Każdą grupę można zwinąć, więc nawet przy dużej ilości sprzętu lista pozostaje czytelna.

![Zakładka Urządzenia](img/mobile-devices.webp "Sprzęt pogrupowany według marek. Każdą grupę można zwinąć.")

## Dodawanie sprzętu

Dotknij **Dodaj urządzenie**, a potem wybierz markę: **Cora**, **Neptune Apex**, **Red Sea**, **Jecod**, **Maxspect**, **GHL** *(beta)*, **HYDROS** *(beta)* albo **AquaWiz**. Każda otwiera dokładnie to, czego potrzebuje, żeby znaleźć Twój sprzęt: skanowanie sieci, adres IP, logowanie albo klucz urządzenia. [Podłączanie sprzętu](/help/mobile-connections) opisuje, czego potrzebuje każda marka.

**Cora** to sposób na sparowanie nowego Cora Max. Wyszukuje urządzenia w Twojej sieci Wi-Fi albo w pobliżu przez Bluetooth. Jeśli wyszukiwanie nic nie znajdzie, na tym samym ekranie jest przycisk **Wpisz adres IP ręcznie**.

Gdy dodajesz sprzęt, np. grzałkę, pompę albo odpieniacz, Cora **podpowiada** markę i model. Zacznij pisać, a Cora zaproponuje nazwy z dużej, sprawdzonej listy marek. Jeśli Twojej marki nie ma, i tak ją wpisz. Cora zapisze to, co wpiszesz.

:::note Cora i telefon muszą być w tej samej sieci
Sprzęt wykrywany lokalnie musi przy dodawaniu być w tej samej sieci co telefon. **Po konfiguracji też jest osiągalny tylko w tej sieci** (albo przez Bluetooth, jeśli z niego korzysta), chyba że na miejscu jest urządzenie Cora, które się z nim połączy.

Sprzęt, który w domu pokazuje dobre odczyty, poza domem może więc pokazywać starsze wartości, jeśli na miejscu nie ma Cora Max, który by go odpytywał. To nie usterka. Po prostu sprzęt jest osiągalny tylko z określonego miejsca.
:::

## Strona urządzenia

Otwórz dowolne urządzenie z listy. Najpierw są jego przyciski sterujące, a pod nimi trzy sekcje, które działają tak samo dla każdej marki.

- **Akwaria** pokazuje, do którego akwarium (albo akwariów) jest przypisane. Dotknij **Zmień**, żeby je przepisać.
- **Połączenie** to miejsce, gdzie edytujesz jego adres IP, dane logowania albo klucz urządzenia.
- **Usuń urządzenie**, na samym dole.

Cora Max, Neptune Apex i GHL mogą obsługiwać więcej niż jedno akwarium, więc ich wybór akwarium to lista zaznaczeń. Cora Max można przypisać do maksymalnie czterech akwariów. Zobacz [Więcej niż jedno urządzenie Cora](/help/mobile-multi-device). Wszystko inne, w tym HYDROS, obsługuje jedno akwarium naraz: wybranie innego przenosi tam urządzenie i zdejmuje je ze starego.

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
| „Czeka na Cora Max” | Kontroler GHL, który właśnie dodano: pojawi się, gdy tylko Cora Max w jego sieci go odczyta |
| Nic | Urządzenie nigdy nie wysłało danych. Sprawdź przypisanie do akwarium i połączenie |

## Usuwanie urządzenia

Otwórz urządzenie i dotknij **Usuń urządzenie**. Cora poprosi o potwierdzenie: *„{name} zostanie usunięty z Cora. Samo urządzenie nie jest resetowane ani zmieniane.”*

**Odczyty zostają.** Po usunięciu urządzenia Cora przestaje zbierać z niego nowe dane. Zebrana historia zostaje przy akwarium, a widżety, które z niego korzystały, zachowują wcześniejsze odczyty.

Tracisz połączenie na żywo, a jeśli urządzenie łączyło się przez konto producenta, także zapisane dane logowania. Gdy dodasz je ponownie, trzeba będzie znów się zalogować.

:::tip Wycisz uciążliwe urządzenie bez usuwania
Jeśli urządzenie działa dobrze, ale za często wywołuje alerty, zmień jego progi albo ustawienia powiadomień. Więcej w **[Alertach i progach](/help/mobile-alerts)**. Połączenie i dane zostają, a powiadomień będzie mniej.
:::

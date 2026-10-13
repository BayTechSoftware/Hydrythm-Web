---
title: Edytowanie pulpitu Cora Max
description: Wybierz siatkę, dodaj widżety i zapisz układy pulpitu na Cora Max.
section: Cora Max
reviewed: 2026-10-13
order: 4
group: Your dashboard
---

Pulpit Cora Max ma **stałą siatkę**. Wszystkie kafelki muszą zmieścić się na jednym ekranie, bo ekranu nie da się przewijać. To główna różnica w porównaniu z pulpitem na telefonie.

Edytor otworzysz z **menu akwarium**. Dotknij nazwy akwarium na górnym pasku, a potem **Układ panelu**. Ta sama opcja jest w **Ustawienia → Ustawienia akwarium → [Twoje akwarium] → Układ panelu**.

![Edytor pulpitu na Cora Max](img/max-dashboard-editor.webp "U góry rozmiary siatki, niżej kafelki. Każdy kafelek pokazuje swój typ i źródło danych, a nie odczyt, bo to ekran układu. Nic się nie zapisze, dopóki nie dotkniesz Zapisz.")

:::tip Pulpit możesz też edytować na telefonie
W Cora Mobile przejdź do **Urządzenia → Twój Cora Max → Edytuj panel** i ułóż ten sam układ. To szybsze niż przestawianie kafelków na ekranie na ścianie, a zmiany od razu pojawiają się na Cora Max.
:::

## Wybór siatki

Najpierw wybierz gęstość siatki, bo jej zmiana układa wszystkie kafelki od nowa.

| Siatka | Kafelki | Jak to wygląda |
|---|---|---|
| 2×2, 3×2, 3×3 | 4–9 | Duże kafelki. Czytelne z drugiego końca pokoju. |
| 4×4, 5×3, 6×4 | 16–24 | Zwykle najlepsze dla pełnego systemu. |
| 6×5, 8×4, 8×5 | 30–40 | Gęsto. Cały pokój z akwariami na jednym ekranie. |
| 9×5, 10×5 | 45–50 | Bardzo gęsto. Najlepiej na największych ekranach. |
| **Auto** | do 32 | Cora dobiera kształt do liczby dodanych kafelków. |

Stała siatka mieści tyle kafelków, ile ma pól, czyli do 50 przy 10×5. Tylko **Auto** ma własny limit. Kończy się na 32 kafelkach, bo przy większej liczbie tekst jest za mały, żeby przeczytać go z daleka.

:::note Nie wiesz, co wybrać? Zacznij od Auto
Dodaj potrzebne kafelki i zostaw siatkę na **Auto**. Cora dobierze kształt, w którym się zmieszczą. Jeśli wynik Ci się spodoba, możesz potem ustawić ten sam stały kształt.
:::

:::warning Zmiana siatki usuwa kafelki tylko wtedy, gdy brakuje miejsca
Po zmianie siatki kafelki są układane od nowa, a nie usuwane według pozycji. Kafelki, które mieszczą się w nowej siatce, zostają na swoich miejscach, a pozostałe są dokładane po kolei. Tracisz kafelki tylko wtedy, gdy nowa siatka ma **mniej pól, niż masz kafelków**. Cora powie Ci wtedy, ile ich ubyło. Przejście z 10×5 (50 pól) na 3×3 (9 pól) usunie większość z nich.
:::

## Dodawanie i układanie kafelków

U góry edytora widać trzy gesty: **Dotknij kafelek, aby edytować · przytrzymaj, aby przenieść · ✕, aby usunąć**. Kafelek może mieć szerokość i wysokość jednego albo dwóch pól.

**Gniazda i karmienie** dodaje w jednym kroku wszystkie sterowalne gniazda i cykle karmienia, więc nie musisz dodawać ich po kolei. **Wyczyść wszystko** opróżnia siatkę, jeśli chcesz zacząć od nowa.

Szesnaście typów kafelków (Wartość, Wskaźnik, Wykres, Stan, Gniazdo, Scena, ReefBeat, Moduł Apex, Jecod, Maxspect *(Beta)*, GHL *(Beta)*, HYDROS *(Beta)*, Radion *(Beta)*, VorTech *(Beta)*, Versa *(Beta)* i Kamera *(Beta)*) opisuje [Rodzaje widżetów](/help/mobile-widgets).

Kafelki Beta należą do integracji Beta, które mogą dodawać tylko użytkownicy Beta, i widzisz taki kafelek dopiero wtedy, gdy masz to urządzenie. Zobacz [Funkcje Beta](/help/mobile-beta).

## Szablony

**Szablony** są u góry edytora, obok **Zaprojektuj z AI**. Działają w każdym planie i nigdy nie używają AI, więc działają też bez udostępniania danych AI.

Otwierają **Szablony pulpitu**, kilka gotowych układów zbudowanych z tego, co to akwarium zgłasza i co ma podłączone:

- **Przegląd**: mało dużych kafelków, z podstawowymi parametrami jako wskaźnikami i najważniejszymi urządzeniami
- **Sprzęt**: najpierw po jednym kafelku na urządzenie, potem gniazda i podstawowe parametry
- **Parametry**: najpierw wykresy i odczyty, a urządzenia i gniazda na końcu
- **Kamera**: duży podgląd na żywo w lewym górnym rogu, a obok podstawowe parametry. Pojawia się tylko wtedy, gdy akwarium ma kamerę. Kamery są w wersji Beta i dostępne tylko dla użytkowników Beta.

Każdy szablon pokazuje podgląd oraz liczbę kafelków i siatkę. Dotknij **Użyj tego**. Cora najpierw zapyta **Zastąpić pulpit?** Dotknij **Najpierw zapisz obecny jako preset**, jeśli chcesz zachować obecny układ, albo **Zastąp**. Nic nie jest zapisane, dopóki nie dotkniesz **Zapisz**.

## Zaprojektuj z AI

W płatnym planie edytor ma przycisk **Zaprojektuj z AI**. Cora proponuje cały układ na podstawie tego, co to akwarium zgłasza i co ma podłączone, i pokazuje, ile ma kafelków i na jakiej siatce. Dotknij **Użyj tego**, aby wstawić go do edytora, albo **Spróbuj ponownie**, aby dostać inny. Możesz zrobić 5 projektów na akwarium dziennie.

Projekt z AI zastępuje to, co jest teraz na tym pulpicie. Nic nie jest zapisane, dopóki nie dotkniesz **Zapisz**, a obecny układ możesz najpierw zachować, zapisując go jako jeden ze swoich pulpitów. W planie darmowym **Zaprojektuj z AI** prowadzi do planów. Wymaga też włączonego udostępniania danych AI w aplikacji Cora.

## Pulpit czytany z daleka

Ekran na ścianie czyta się z większej odległości niż telefon i zwykle tylko rzuca się na niego okiem.

- **Najważniejsze parametry ustaw jako kafelki 2×2.** Alkaliczność, temperatura, pH, czyli to, co chcesz odczytać bez podchodzenia.
- **Sterowanie umieść przy krawędziach.** Po kafelki gniazd sięgasz najczęściej, a z boku łatwiej w nie trafić.
- **Grupuj według tematu, a nie typu kafelka.** Wszystko o dozowaniu w jednym miejscu, wszystko o przepływie w drugim. Ekran na ścianie przeglądasz obszarami.
- **Pierwiastki śladowe mogą być małe.** Pierwiastki śladowe i inne wolno zmieniające się wartości sprawdzasz tylko od czasu do czasu. Wystarczy im kafelek wartości 1×1.

## Zapisywanie układów

Zmiany w edytorze zaczynają działać dopiero po dotknięciu **Zapisz**. Jeśli wyjdziesz bez zapisywania, zmiany przepadną.

W **Moje panele** możesz zachować układy, do których chcesz wracać, i przełączać się między nimi bez układania wszystkiego od nowa. Gęsty układ na co dzień i układ z dużymi kafelkami na czas pracy przy akwarium przydają się w różnych sytuacjach. Przełączenie się między nimi to jedno dotknięcie.

## Kilka akwariów

Każde akwarium ma własny układ. Edytujesz je osobno, każde w ustawieniach danego akwarium.

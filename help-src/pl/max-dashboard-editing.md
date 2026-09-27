---
title: Edytowanie pulpitu Cora Max
description: Wybierz siatkę, dodaj widżety i zapisuj układy dla wyświetlacza Cora Max.
section: Cora Max
reviewed: 2026-09-09
order: 4
group: Your dashboard
---

Pulpit Cora Max używa **ustalonej siatki**. Każdy kafelek musi zmieścić się na jednym ekranie; wyświetlacz się nie przewija. To jest główna różnica względem pulpitu na telefonie.

Otwórz edytor z **menu akwarium**: dotknij nazwy akwarium na górnym pasku, potem **Układ panelu**. Jest też w **Ustawienia → Ustawienia akwarium → [your tank] → Układ panelu**.

![Edytor pulpitu na Cora Max](img/max-dashboard-editor.webp "Rozmiary siatki na górze, potem kafelki. Każdy pokazuje swój typ i źródło, nie odczyt; to jest ekran układu. Nic nie jest zapisywane, aż dotkniesz Save.")

:::tip Możesz to też edytować z telefonu
**Urządzenia → Twój Cora Max → Edytuj panel** buduje ten sam układ z Cora Mobile. Jest szybsze niż rozmieszczanie kafelków ręcznie na ścianie, a wynik pojawia się na ekranie od razu.
:::

## Wybieranie siatki

Wybierz gęstość najpierw, bo jej zmiana przepływa wszystko na nowo.

| Siatka | Kafelki | Wygląda jak |
|---|---|---|
| 2×2, 3×2, 3×3 | 4-9 | Duże. Czytelne z drugiego końca pokoju. |
| 4×4, 5×3, 6×4 | 16-24 | Zwykły wybór dla pełnego systemu. |
| 6×5, 8×4, 8×5 | 30-40 | Gęste. Cały pokój z akwariami naraz. |
| 9×5, 10×5 | 45-50 | Bardzo gęste. Najlepsze na największych ekranach. |
| **Auto** | do 32 | Cora wybiera kształt pasujący do liczby dodanych kafelków. |

Ustalona siatka pomieści tyle kafelków, ile ma komórek, do 50 na 10×5. **Auto** jest jedyną opcją z własnym sufitem: zatrzymuje się na 32 kafelkach, bo poza tym tekst staje się za mały, aby czytać z odległości.

:::note Zacznij od Auto, jeśli nie jesteś pewien
Dodaj kafelki, które chcesz, i zostaw siatkę na **Auto**; Cora wybiera kształt, który je pomieści. Jeśli wynik Ci się podoba, przypnij go do tego ustalonego kształtu potem.
:::

:::warning Zmiana siatki może odrzucić kafelki, ale tylko, gdy nie ma miejsca
Kafelki są przepływane na nowo do nowego kształtu, a nie odrzucane według pozycji: wszystko już w prawidłowej komórce zostaje na miejscu, a resztę pakuje się z powrotem, po kolei. Kafelki są tracone tylko, gdy nowa siatka ma **mniej komórek niż masz kafelków**, i Cora mówi Ci, ile poszło. Przejście z 10×5 (50 komórek) na 3×3 (9) utraci większość z nich.
:::

## Dodawanie i rozmieszczanie

Edytor mówi Ci trzy gesty na górze: **dotknij kafelka, aby edytować**, **przytrzymaj, aby go przenieść**, i **✕, aby go usunąć**. Kafelki mogą mieć jedną albo dwie komórki szerokości i jedną albo dwie komórki wysokości.

**Gniazda i karmienie** dodaje Twoje sterowalne gniazda i cykle karmienia w jednym kroku, a nie kafelek po kafelku. **Wyczyść wszystko** czyści siatkę, abyś mógł zacząć od nowa.

Dziewięć typów kafelków (Value, Gauge, Graph, Status, Outlet, ReefBeat, Apex module, Jecod i Maxspect *(beta)*) są opisane w **[Opisie widżetów](/help/mobile-widgets)**.

## Projektowanie na odległość

Wyświetlacz ścienny jest czytany z większej odległości niż telefon, i zwykle jednym rzutem oka, a nie z uwagą.

- **Umieść swoje główne parametry po dwa.** Alkaliczność, temperatura, pH: rzeczy, które chcesz przeczytać bez podchodzenia.
- **Umieść kontrolki na krawędziach.** Kafelki gniazd to te, po które sięgasz; łatwiej je trafić po bokach.
- **Grupuj według tematu, nie typu.** Wszystko o dozowaniu razem, wszystko o przepływie razem. Skanujesz ścianę według obszaru.
- **Zostaw elementy śladowe małe.** Elementy śladowe i inne wolno zmieniające się liczby są odniesieniem, nie monitorowaniem; kafelek wartości jeden na jeden jest w pełni wystarczający.

## Zapisywanie układów

Nic, co robisz w edytorze, nie wchodzi w życie, aż dotkniesz **Zapisz**. Opuszczenie bez zapisania odrzuca zmiany.

**Moje panele** przechowuje układy, do których chcesz wracać, więc możesz przełączać się między nimi, zamiast budować od nowa. Gęsty codzienny układ i układ z dużymi kafelkami na czas pracy przy akwarium odpowiadają różnym chwilom, a przełączanie między nimi zajmuje jedno dotknięcie.

## Wiele akwariów

Każde akwarium ma swój własny układ. Edytuj je odrębnie, po jednym naraz, z własnych ustawień tego akwarium.

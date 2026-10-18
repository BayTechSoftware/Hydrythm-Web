---
title: Edytowanie panelu Cora Max
description: Dodawaj, przenoś i usuwaj kafelki na panelu Cora Max, wybierz siatkę, użyj szablonów albo Zaprojektuj z AI i zapisuj układy do ponownego użycia na dowolnym Cora Max.
section: Cora Max
reviewed: 2026-10-17
order: 4
group: Your dashboard
twin: mobile-dashboard-editing
---

Ta strona pokazuje, jak układać kafelki na panelu Cora Max. Pulpit ma **stałą siatkę**: ekran się nie przewija, więc każdy kafelek musi zmieścić się na jednym ekranie. To główna różnica w porównaniu z panelem w telefonie.

Edytor otworzysz z **menu akwarium**: dotknij nazwy akwarium na górnym pasku, a potem **Układ panelu**. Jest też w **Ustawienia → [Twoje akwarium] → Układ panelu**.

![Edytor panelu na Cora Max](img/max-dashboard-editor.webp "Rozmiary siatki na górze, a pod nimi kafelki. To ekran układu, więc każdy kafelek pokazuje swój typ i źródło zamiast odczytu. Nic się nie zapisze, dopóki nie naciśniesz Zapisz.")

:::tip Możesz też edytować go z telefonu
W Cora Mobile otwórz zakładkę **Urządzenia**, dotknij swojego Cora Max, a potem **Układ panelu** na karcie akwarium. To szybsze niż ręczne układanie kafelków na ekranie na ścianie, a wynik pojawi się na Cora Max, gdy tylko zapiszesz.
:::

## Wybór siatki {#choosing-a-grid}

Najpierw wybierz rozmiar siatki. Późniejsza zmiana przestawia wszystkie kafelki.

| Siatka | Kafelki | Jak to wygląda |
|---|---|---|
| 2×2, 3×2, 3×3 | 4–9 | Duże. Łatwe do przeczytania z drugiego końca pokoju. |
| 4×4, 5×3, 6×4 | 16–24 | Zwykły wybór dla pełnego systemu. |
| 6×5, 8×4, 8×5 | 30–40 | Gęsto. Cały pokój z akwariami na jednym ekranie. |
| 9×5, 10×5 | 45–50 | Bardzo gęsto. Najlepsze na największych ekranach. |
| **Auto** | do 32 | Cora wybiera kształt, który mieści tyle kafelków, ile dodano. |

Stała siatka mieści tyle kafelków, ile ma komórek, do 50 przy 10×5. **Auto** ma własny limit 32 kafelków. Powyżej tekst robi się za mały, żeby przeczytać go z daleka.

:::note Nie wiesz? Zacznij od Auto
Dodaj kafelki, które chcesz, i zostaw siatkę na **Auto**. Cora wybierze kształt, który je pomieści. Jeśli Ci się spodoba, możesz potem przełączyć się na ten stały kształt.
:::

:::warning Zmiana siatki usuwa kafelki tylko wtedy, gdy się nie mieszczą
Gdy zmieniasz siatkę, Cora nie wyrzuca kafelków według pozycji. Kafelki, które nadal mają prawidłową komórkę, zostają na miejscu, a pozostałe są dokładane z powrotem po kolei. Tracisz kafelki tylko wtedy, gdy nowa siatka ma **mniej komórek, niż masz kafelków**, a Cora powie Ci, ile ubyło. Przejście z 10×5 (50 komórek) na 3×3 (9) usuwa większość z nich.
:::

## Dodawanie i układanie kafelków {#adding-and-arranging}

1. Dotknij pustej komórki (pokazuje **+**), żeby otworzyć **Dodaj widżet**.
2. W **TYP** wybierz rodzaj kafelka, a potem to, co ma pokazywać (odczyt, gniazdo, urządzenie albo scenę).
3. W **ROZMIAR** wybierz, jak duży ma być. Kafelek może mieć jedną albo dwie komórki szerokości i jedną albo dwie wysokości. Wykres ma też **ZAKRES CZASU**. Kafelek dozownika ma **Pokaż pozostałe jako**, w **Dni** albo **Mililitry (mL)**.
4. Dotknij **Dodaj**.

Gesty są wymienione u góry edytora: **Dotknij kafelek, aby edytować**, **przytrzymaj, aby przenieść** i **✕, aby usunąć**. **Wyczyść wszystko** opróżnia siatkę, żeby zacząć od nowa.

Typy kafelków to Wartość, Wskaźnik, Wykres, Stan, Gniazdo, Scena, ReefBeat, Moduł Apex i Jecod. Znajdziesz je w [Rodzajach widżetów](/help/mobile-widgets). Kafelek **Scena** istnieje tylko na Cora Max. Uruchamia [scenę](/help/max-automation) jednym dotknięciem.


## Gniazda i karmienie {#outlets-feed}

**Gniazda i karmienie** w edytorze wybiera, które gniazda i cykle karmienia pojawią się w **Sterowaniu**, szufladzie wysuwanej z dołu panelu. Nie dodaje kafelków. Jeśli nic nie wybierzesz, Sterowanie wymienia wszystkie. Żeby umieścić gniazdo na samej siatce, dodaj kafelek **Gniazdo**. Więcej w [Gniazdach i sterowaniu](/help/max-controls).

Gdy usuniesz urządzenie z akwarium, jego kafelki same znikają z panelu, w telefonie i na każdym Cora Max tego akwarium. Kafelek, którego urządzenia już nie ma, pokazuje **To urządzenie nie jest już w tym akwarium** i niczego nie otwiera.

## Szablony {#templates}

**Szablony** są na górze edytora, obok **Moje panele** i **Zaprojektuj z AI**. Działają w każdym planie i nigdy nie używają AI, więc działają też bez udostępniania danych AI.

Otwierają **Szablony panelu**, kilka gotowych układów zbudowanych z tego, co to akwarium zgłasza i co ma podłączone:

- **Przegląd**: mało dużych kafelków, z podstawowymi parametrami jako wskaźnikami i głównymi urządzeniami
- **Sprzęt**: najpierw po jednym kafelku na urządzenie, potem gniazda i podstawowe parametry
- **Parametry**: najpierw wykresy i odczyty, a urządzenia i gniazda na końcu

Każdy pokazuje podgląd oraz liczbę kafelków i siatkę. Dotknij **Użyj tego**. Cora najpierw zapyta **Zastąpić panel?** Dotknij **Najpierw zapisz obecny projekt**, jeśli chcesz zachować obecny układ, albo **Zastąp**. Nic się nie zapisze, dopóki nie naciśniesz **Zapisz**.

## Zaprojektuj z AI {#design-with-ai}

Edytor ma przycisk **Zaprojektuj z AI**. Działa w płatnym planie i w okresie próbnym. Cora proponuje cały układ na podstawie tego, co to akwarium zgłasza i co ma podłączone, i pokazuje, ile ma kafelków i na jakiej siatce. Dotknij **Użyj tego**, żeby wstawić go do edytora, albo **Spróbuj ponownie**, żeby dostać inny. Możesz zrobić 5 projektów na akwarium dziennie.

Projekt z AI zastępuje to, co jest teraz na tym panelu. Nic się nie zapisze, dopóki nie naciśniesz **Zapisz**, a obecny układ możesz najpierw zachować, zapisując go w **Moje panele**. W planie darmowym **Zaprojektuj z AI** kieruje do planów. Wymaga też udostępniania danych AI włączonego w Cora Mobile. Więcej w [Pytaniach do Cory](/help/mobile-assistant).

## Projektowanie pod czytanie z daleka {#designing-for-distance}

Ekran na ścianie czyta się z dalszej odległości niż telefon i zwykle jednym rzutem oka.

- Najważniejsze parametry ustaw jako kafelki dwa na dwa. Alkaliczność, temperaturę i pH chcesz odczytać bez podchodzenia.
- Sterowanie umieść przy krawędziach. Po kafelki gniazd sięgasz najczęściej, a z boku łatwiej w nie trafić.
- Grupuj kafelki według tematu. Wszystko o dozowaniu trzymaj razem i wszystko o przepływie razem, bo ścianę przeglądasz obszarami.
- Pierwiastki śladowe niech będą małe. One i inne wolno zmieniające się liczby służą do wglądu, więc kafelek wartości jeden na jeden w zupełności wystarczy.

## Zapisywanie i ponowne używanie układów {#saving-layouts}

Nic, co robisz w edytorze, nie zacznie działać, dopóki nie naciśniesz **Zapisz**. Jeśli wychodzisz z niezapisanymi zmianami, Cora najpierw zapyta **Odrzucić zmiany?**

**Moje panele** przechowuje projekty, do których chcesz wracać. Są zapisane na Twoim koncie, a nie na tym ekranie, więc każdy Cora Max na koncie może je wczytać, dla innego akwarium albo na ekranie zastępczym.

- **Zapisz ten projekt** zachowuje to, co jest w edytorze. Możesz mieć do 30 projektów.
- **Wczytaj** wstawia zapisany projekt do edytora. Projekty zapisane z telefonu mają oznaczenie **Telefon**.
- Przed wczytaniem Cora powie, ile kafelków się przeniesie. To, czego nie da się przenieść, na przykład odczyt, którego to akwarium nie zgłasza, albo urządzenie spoza tego akwarium, jest wymienione pod **Pozostawione:** z powodem.

Możesz na przykład trzymać gęsty układ na co dzień i układ z dużymi kafelkami na czas pracy przy akwarium.

## Kilka akwariów {#multiple-tanks}

Każde akwarium ma własny układ. Przełącz się na to akwarium i otwórz **Układ panelu** z jego menu akwarium albo użyj **Ustawienia → [to akwarium] → Układ panelu**.

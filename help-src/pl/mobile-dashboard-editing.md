---
title: Edytowanie panelu
description: Dodawaj, przenoś, zmieniaj rozmiar i usuwaj widżety na panelu w telefonie, ustaw liczbę kolumn i edytuj z telefonu panel Cora Max.
section: Cora Mobile
reviewed: 2026-10-18
order: 8
group: Your dashboard
twin: max-dashboard-editing
---

Edytor panelu ustala, które widżety są na panelu akwarium i jak są ułożone. Każde akwarium ma własny układ, który idzie za Twoim kontem na każdy telefon, na którym się zalogujesz.

## Jak otworzyć edytor {#opening-the-editor}

Przewiń panel w dół i dotknij **Edytuj panel**, tuż pod widżetami. Edytor otwiera się jako **Edytuj panel**, z podpowiedzią **Przytrzymaj kafelek, aby go przenieść. Dotknij, aby skonfigurować.**

:::note Ołówek w nagłówku akwarium otwiera coś innego
Otwiera **Edytuj akwarium**, czyli profil akwarium z objętością, obsadą, dozowaniem, oświetleniem i przepływem. Opisuje go [Profil akwarium](/help/mobile-tank-profile).
:::

![Ekran Edytuj panel w Cora Mobile](img/mobile-edit.webp "Kolumny na górze, a pod nimi każdy kafelek z nazwą i typem. Dotknij czerwonego krzyżyka, żeby go usunąć.")

## Liczba kolumn {#setting-the-column-count}

Wybierz **2**, **3** albo **4** obok **KOLUMNY** na górze edytora. Siatka rośnie w dół, gdy dodajesz widżety, a panel się przewija.

| Kolumny | Kiedy wybrać |
|---|---|
| 2 | Śledzisz kilka parametrów i chcesz dużych kafelków |
| 3 | Ustawienie domyślne. Pasuje do większości akwariów |
| 4 | Chcesz gęstszego widoku albo masz duży telefon |

## Dodawanie widżetu {#adding-a-widget}

1. Dotknij **Dodaj kafelek** pod siatką albo dotknij pustej komórki.
2. W **Dodaj kafelek** wybierz jego rodzaj. **Parametr** obejmuje wartość, wskaźnik, wykres albo stan parametru. **Gniazdo** steruje gniazdem Apex. Pozostałe wiersze są dla sprzętu, na przykład **ReefBeat**, **Trident**, **DŌS** albo **Jecod**. Większość z nich pojawia się tylko wtedy, gdy akwarium ma ten sprzęt. **Oświetlenie**, **Pompa cyrkulacyjna** i **Pompa** wymieniają wszystkie lampy, pompy cyrkulacyjne i pompy w akwarium, niezależnie od marki, a każdy wiersz pojawia się tylko wtedy, gdy akwarium ma takie urządzenie. **ReefBeat** i **Jecod** zachowują resztę swoich urządzeń, na przykład ReefDose albo dozownik Jecod.
3. Wybierz parametr, gniazdo albo urządzenie.
4. Dla parametru wybierz typ. Każdy opisują [Rodzaje widżetów](/help/mobile-widgets).

Widzisz tylko parametry, które ma akwarium. Parametr bez źródła pojawi się, gdy podłączysz sprzęt, który go podaje, albo zapiszesz odczyt ręcznie.

Siatka mieści do 20 rzędów. Gdy jest pełna, Cora pokaże **Panel jest pełny: najpierw usuń jakiś kafelek.** Wykres potrzebuje dwóch wolnych komórek obok siebie.


Gdy usuniesz urządzenie z akwarium, jego kafelki same znikają z panelu, w telefonie i na każdym Cora Max tego akwarium. Kafelek, którego urządzenia już nie ma, pokazuje **To urządzenie nie jest już w tym akwarium** i niczego nie otwiera.

## Układanie widżetów {#arranging-widgets}

- Żeby przenieść widżet, przytrzymaj go, a potem przeciągnij. Pozostałe przesuną się wokół niego.
- Żeby usunąć widżet, dotknij czerwonego krzyżyka w jego rogu albo dotknij widżetu, a potem **Usuń**.
- Żeby zmienić ustawienia widżetu, dotknij go.

## Ustawienia widżetu {#widget-settings}

Dotknij widżetu w edytorze, żeby otworzyć jego ustawienia. W zależności od widżetu możesz ustawić:

| Ustawienie | Dotyczy |
|---|---|
| **Typ** | Widżetów parametrów: Wartość, Wskaźnik, Wykres albo Stan |
| **Parametr** | Widżetów parametrów: który parametr pokazuje |
| Gniazdo albo urządzenie | Kafelków gniazd i sprzętu: które pokazuje |
| **Pokaż pozostałe jako** | Kafelków dozowników: **Dni** albo **Mililitry (mL)** |
| **Szerokość** | Każdego widżetu: **1×** albo **2×**. Wykres ma zawsze co najmniej 2 szerokości |
| **Wysokość** | Każdego widżetu: **1×** albo **2×** |
| **Zakres czasu** | Wykresu: 1h, 6h, 24h, 7d, 30d albo 1y |

Dotknij **Gotowe**, żeby zachować ustawienia, albo **Usuń**, żeby zdjąć widżet.

Widżet nie ma własnej etykiety, źródła ani zakresu. Jego zakres alertu pochodzi z progów alertów akwarium: przytrzymaj widżet na panelu albo zobacz [Alerty i progi](/help/mobile-alerts). To, za którym źródłem idzie parametr, ustawiasz dla każdego akwarium w [Mapowaniu parametrów](/help/mobile-probes).

## Zapisywanie {#saving}

Dotknij **Zapisz**, żeby zachować układ. Żeby porzucić zmiany, dotknij ikony zamknięcia. Jeśli coś zmieniono, Cora zapyta **Odrzucić zmiany?** Dotknij **Odrzuć** albo **Kontynuuj edycję**, żeby wrócić.

Edytor w telefonie nie ma cofania ani zapisanych projektów. Odczyty, historia i wpisy w dzienniku są przechowywane osobno od układu, więc edycja panelu nigdy ich nie usunie.

## Edytowanie panelu Cora Max {#editing-the-cora-max-dashboard}

Pulpit Cora Max edytujesz osobno, z **Urządzenia →** Twój Cora Max **→ Układ panelu**, na karcie akwarium. Ma stałą siatkę, która się nie przewija, i nic nie trafi na Cora Max, dopóki nie dotkniesz **Zapisz i opublikuj**.

Ten edytor ma trzy dodatki, których nie ma panel w telefonie:

- **Moje panele** przechowuje na Twoim koncie do 30 zapisanych projektów. Każdy Cora Max na koncie może wczytać dowolny z nich. Kafelki, których docelowy panel nie wypełni, są wymienione pod **Pozostawione:** przed wczytaniem.
- **Szablony** otwiera **Szablony panelu**: **Przegląd**, **Sprzęt** i **Parametry**. Działają w każdym planie i nie używają AI.
- **Zaprojektuj z AI**, w płatnym planie albo w okresie próbnym, proponuje cały układ na podstawie tego, co akwarium zgłasza i co ma podłączone. Możesz zrobić 5 projektów na akwarium dziennie.

Jak działa każdy z nich, opisuje [Edytowanie panelu Cora Max](/help/max-dashboard-editing).

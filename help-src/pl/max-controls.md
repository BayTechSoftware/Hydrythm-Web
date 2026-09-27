---
title: Gniazda i kontrolki
description: Przełączanie gniazd z Cora Max, używanie trybu karmienia i co Auto naprawdę znaczy.
section: Cora Max
reviewed: 2026-09-09
order: 5
group: Equipment
---

Cora Max może przełączać sprzęt w Twoim systemie: z widżetów kontrolnych na pulpicie, z szuflady Outlets & Feed albo głosem.

:::warning Te kontrolki działają na Twoim akwarium
Nie ma cofnięcia. Gniazda oznaczone kłódką proszą Cię najpierw o potwierdzenie; resztę stosuje się od razu po dotknięciu. Polecenie może wrócić jako **Potwierdzono**, **Niepotwierdzone** (wysłane, nic nie zgłoszono z powrotem), **Odmówiono** albo **Bez zmian**; zobacz [Kontrola sprzętu](/help/mobile-device-control).
:::

## Trzy stany

Każde gniazdo jest w jednym z trzech stanów.

**Auto** przekazuje gniazdo z powrotem do jego programowania Apex. Tu gniazdo powinno zostawać większość czasu.

**Wyłączone** i **On** to ręczne nadpisania. Wchodzą w życie natychmiast i **trwają, aż je zmienisz z powrotem**. Nie wygasają i nic nie przywraca ich za Ciebie.

:::warning Ręczne nadpisanie nie wygasa samo
Ustaw je z powrotem na **Auto**, gdy skończysz; nic tego za Ciebie nie zrobi. Może wciąż zostać zmienione później przez Ciebie, głosem albo przez automatyzację; nadpisanie nie jest blokadą.
:::

## Przełączanie z pulpitu

Widżety kontrolne pokazują trzy stany z aktualnym podświetlonym. Dotknij stanu, który chcesz.

Niektóre gniazda niosą **kłódkę**. Nie musi być nigdzie wyłączona; znaczy, że gniazdo prosi Cię o potwierdzenie przed zmianą, więc przypadkowe dotknięcie nie może przełączyć czegoś krytycznego. Zobacz poniżej.

## Szuflada Controls

Wysuń zakładkę na dole pulpitu, aby otworzyć **Sterowanie**: każde gniazdo w systemie w jednym miejscu, niezależnie od tego, czy ma widżet, plus cykle karmienia.

![Szuflada Controls](img/max-controls.webp "Cykle karmienia na górze, potem każde gniazdo.")

Gniazdo niosące **kłódkę** wymaga wyraźnego potwierdzenia przed zmianą. Dotknięcie go otwiera okno nazywające gniazdo, jego aktualny stan i nadpisanie, które zamierzasz zastosować. To jest krok potwierdzenia, nie blokada do wyłączenia gdzie indziej.

## Tryb karmienia

Tryb karmienia to bezpieczny sposób na wstrzymanie przepływu na czas karmienia. Wstrzymuje sprzęt, który powinien być wstrzymany, zostawia w spokoju sprzęt, który nie powinien, i **przywraca wszystko sam**, gdy czas się kończy.

Użyj go zamiast ręcznego wyłączania pomp, bo przywraca system bez zależności od Twojej pamięci.

Cykle karmienia są oznaczone literami **A**, **B**, **C** i **D**: cykle zdefiniowane przez Twój kontroler, każdy wstrzymujący inny zestaw sprzętu. Wybierz ten, który odpowiada temu, co robisz. **Cancel** kończy działający cykl wcześniej i przywraca wszystko natychmiast.

Uruchom jeden z szuflady Controls albo powiedz *"start feed mode"*.

## Głosem

Możesz przełączać gniazda głosem: *"wyłącz skimmer"*, *"ustaw wentylator z powrotem na auto"*.

Wszystko, co dosięga Twojego sprzętu, jest **potwierdzane, zanim się wykona**: Cora mówi Ci, co zamierza zrobić, i czeka na Twoją zgodę. Nie działa na poleceniu, którego nie jest pewna.

Zobacz **[Rozmowa z Corą na Cora Max](/help/max-voice)**.

## Sprawdzanie, co się stało

Każde żądanie jest zapisywane, wraz z tym, co o to poprosiło (ta aplikacja, ekran Cora, głos, Asystent, reguła automatyzacji, smart przycisk albo Twoje konto) i jak dotarło. Na Twoim telefonie to jest **Ustawienia → Aktywność**.

To jest pierwsze miejsce do sprawdzenia, gdy coś się zmieniło, a Ty nie wiesz czemu.

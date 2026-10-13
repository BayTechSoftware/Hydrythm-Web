---
title: Gniazda i sterowanie
description: Przełączaj gniazda Apex z Cora Max, uruchamiaj albo przerywaj tryb karmienia, korzystaj z szuflady Gniazda i karmienie i poznaj znaczenie stanów Auto, Wył. i Wł.
section: Cora Max
reviewed: 2026-10-13
order: 5
group: Equipment
---

Ta strona opisuje przełączanie gniazd i uruchamianie trybu karmienia z Cora Max. Zrobisz to kafelkami gniazd na pulpicie, z szuflady **Gniazda i karmienie** albo głosem.

:::warning Te przyciski działają na Twoje akwarium
Nie da się tego cofnąć. Gniazda z kłódką najpierw proszą o potwierdzenie. Pozostałe zmieniają się od razu po dotknięciu. Polecenie może wrócić jako **Potwierdzono**, **Niepotwierdzone** (wysłane, ale nic nie odpowiedziało), **Odmówiono** albo **Bez zmian**. Więcej w [Sterowaniu sprzętem](/help/mobile-device-control).
:::

## Trzy stany {#the-three-states}

Każde gniazdo jest w jednym z trzech stanów.

**AUTO** oddaje gniazdo z powrotem programowi Apex. Przez większość czasu gniazdo powinno być właśnie w tym stanie.

**WYŁ.** i **WŁ.** to ręczne nadpisania. Działają od razu i **zostają, dopóki ich nie zmienisz**. Nie wygasają i nic nie przywróci ich za Ciebie.

:::warning Ręczne nadpisanie nie wygasa
Gdy skończysz, ustaw gniazdo z powrotem na **AUTO**, bo nic innego tego nie zrobi. Nadpisanie to jednak nie blokada. Później możesz je zmienić Ty, Twój głos albo automatyzacja.
:::

## Przełączanie z pulpitu {#switching-from-the-dashboard}

Kafelki gniazd pokazują trzy stany, a bieżący jest podświetlony. Dotknij tego, który chcesz.

Niektóre gniazda mają **kłódkę**. Oznacza ona, że gniazdo prosi o potwierdzenie przed zmianą, więc przypadkowe dotknięcie nie przełączy niczego ważnego. Po dotknięciu okno pokazuje gniazdo, jego bieżący stan, nadpisanie, które zamierzasz ustawić, i to, co może ono zrobić z akwarium. Nie ma żadnej blokady do wyłączania gdzie indziej.

Domyślnie kłódkę mają grzałki, chłodziarki, pompy powrotne, dolewka (ATO), karmniki i każde gniazdo, którego Cora nie potrafi sklasyfikować. Oświetlenie, odpieniacze, pompy cyrkulacyjne, pompy dozujące, reaktory, UV i wentylatory przełączają się jednym dotknięciem.

## Szuflada Gniazda i karmienie {#the-controls-drawer}

Zobaczysz ją tylko przy akwarium z Neptune Apex. Dotknij małej etykiety **Gniazda i karmienie** na dole pulpitu albo przesuń palcem w górę w dowolnym miejscu pulpitu. Otworzy się **Sterowanie** z sekcją **KARMIENIE** u góry i **GNIAZDA** pod nią.

![Szuflada Sterowanie](img/max-controls.webp "U góry cykle karmienia, niżej gniazda wybrane dla tego pulpitu.")

Pokazuje gniazda i cykle karmienia wybrane w **Gniazda i karmienie** w [edytorze pulpitu](/help/max-dashboard-editing#outlets-feed), albo wszystkie, jeśli żadnych nie wybrano. Gniazda z kłódką także tu proszą o potwierdzenie. Gniazda w innych kontrolerach przełączasz na ich własnych stronach urządzeń, zobacz [Sterowanie sprzętem z Cora Max](/help/max-device-control).

Jeśli po dotknięciu gniazda pojawi się *Apex nie odpowiedział: mogło się to już zastosować*, sprawdź gniazdo przed kolejną próbą.

## Tryb karmienia {#feed-mode}

Tryb karmienia to bezpieczny sposób na wstrzymanie przepływu na czas karmienia. Twój Apex wstrzymuje sprzęt, który ma stanąć, nie rusza reszty i **sam przywraca wszystko**, gdy czas minie.

Używaj go zamiast ręcznego wyłączania pomp. Przywróci system, nawet jeśli zapomnisz.

Cykle karmienia to Feed A, Feed B, Feed C i Feed D, pokazane jako **A**, **B**, **C** i **D** w **KARMIENIE**. To cykle zaprogramowane w Twoim Apex i każdy może wstrzymywać inny zestaw sprzętu. Wybierz ten, który pasuje do tego, co robisz. **Anuluj** kończy działający cykl wcześniej i od razu wszystko przywraca.

Uruchom go z szuflady albo powiedz *„włącz tryb karmienia”*.

Jeśli Cora Max mówi, że Apex nie odpowiedział, karmienie może już trwać. Sprawdź pompę powrotną, zanim uruchomisz je ponownie.

## Głosem {#by-voice}

Gniazda możesz przełączać głosem, na przykład *„wyłącz odpieniacz”* albo *„ustaw wentylator z powrotem na auto”*.

Zanim cokolwiek dotrze do sprzętu, Cora **najpierw pyta Cię o zgodę**. Mówi, co zamierza zrobić, i czeka na Twoje OK. Jeśli nie jest pewna, o co prosisz, nic nie zrobi.

Więcej w [Rozmowie z Corą](/help/max-voice).

## Co się stało {#seeing-what-happened}

Każde żądanie jest zapisywane razem z tym, co o nie poprosiło i jak poszło, niezależnie od tego, czy przyszło z Cora Mobile, Cora Max, głosu, Asystenta czy automatyzacji. Na Cora Max dotknij nazwy akwarium na górnym pasku i wybierz **Aktywność**. Na telefonie znajdziesz je w **Ustawienia → Aktywność**. Więcej w [Aktywności na Cora Max](/help/max-activity).

Gdy coś się zmieniło i nie wiesz dlaczego, zajrzyj tam najpierw.

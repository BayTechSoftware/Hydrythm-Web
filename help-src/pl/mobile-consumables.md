---
title: Materiały eksploatacyjne i alerty uzupełnienia
description: Ustaw alerty uzupełnienia dla odczynników, pojemników dozujących, zbiorników dolewki i rolek filtracyjnych i daj Corze znać, gdy je uzupełnisz.
section: Cora Mobile
reviewed: 2026-10-13
order: 16
group: Equipment
---

Ustaw alerty uzupełnienia, żeby Cora ostrzegła Cię, zanim skończy się odczynnik, płyn do dozowania, woda do dolewki albo rolka filtracyjna. Otwórz urządzenie w zakładce **Urządzenia** (albo dotknij jego kafelka na pulpicie), a potem dotknij **dzwonka** na górnym pasku.

## Ustawianie alertu uzupełnienia {#setting-a-refill-alert}

![Arkusz Alerty dla ReefDose 4, z progiem dni i przełącznikiem dla każdej głowicy](img/mobile-consumables.webp "Jeden próg na głowicę, każdy z własnym przełącznikiem.")

Arkusz nazywa się **Alerty:**, a po tym następuje nazwa urządzenia. Jeśli sprzęt ma więcej niż jeden pojemnik, każdy dostaje własny próg i własny przełącznik, więc głowicę, którą uważnie pilnujesz, i tę, której prawie nie ruszasz, możesz ustawić inaczej. Wyłączenie przełącznika zachowuje wartość na później.

Gdzie to ustawić:

- **Większość urządzeń**: dzwonek na górnym pasku strony urządzenia.
- **DŌS**: karta **Alerty** na stronie DŌS albo dzwonek. Zobacz [Alerty dozownika](/help/mobile-device-control#doser-alerts).
- **Dozowniki AquaWiz i GHL**: ich reguła w zakładce **Reguły** w [Centrum alertów](/help/mobile-alerts).

Większość progów ustawia się w dniach, a nie w objętości. Cora liczy, na jak długo wystarczy to, co zostało, przy Twoim tempie zużycia. Z „wapnia zostało na cztery dni” od razu wiesz, co zrobić. Z „zostało 180 mL” już nie.

## Przed czym możesz dostać ostrzeżenie {#thresholds}

| Urządzenie | Próg | Domyślnie |
|---|---|---|
| Trident | **Pozostałe testy** (odczynnik, którego jest najmniej) | 10 testów |
| Trident | **Butelka odpadów** (pełna butelka sprawi, że kolejny test się nie uda) | 85% pełna |
| Głowica DŌS | *[głowica] · pozostałe dni* | 7 dni |
| Głowica DŌS | *[głowica] · pozostało*, w mL | 100 mL |
| Głowica DŌS, która odbiera starą wodę | **Pozostałe miejsce w zbiorniku odpadów** | |
| Głowica DŌS | **Alerty o pominiętej dawce** (przełącznik) | |
| Głowica ReefDose | Na ile dni wystarczy suplementu | 7 dni |
| ReefATO+ | **Zapas w zbiorniku**, szacowany na podstawie ostatniego zużycia na dolewkę | 2 dni |
| ReefMat | **Pozostała rolka**, szacowana na podstawie tego, jak szybko przesuwa się rolka | 3 dni |
| AquaWiz | Ile zostało suplementu alkaliczności | 100 mL |
| Dozownik GHL *(Beta)* | Jak pełny jest pojemnik | 20% |
| EcoTech Versa *(Beta)* | Na ile dni wystarczy suplementu i jak pełny jest pojemnik | 7 dni, 10% |

Urządzenie Focustronic *(Beta)* pokazuje na swojej stronie własne ostrzeżenia o odczynniku i buforze.

:::note Beta
**Beta.** GHL, EcoTech i Focustronic są w wersji Beta i są dostępne tylko dla użytkowników Beta. Jeśli nie jesteś użytkownikiem Beta, nie zobaczysz ich w **Dodaj urządzenie**. Aby poprosić o dostęp do Beta, skontaktuj się z [pomocą techniczną](/support.html).
:::

Alert materiału eksploatacyjnego działa jak każdy inny alert. Pojawia się w [Centrum alertów](/help/mobile-alerts) i może wysłać powiadomienie na telefon. Po przekroczeniu poziomu dostajesz **jedno** powiadomienie, a alert znika, gdy poziom znów będzie powyżej progu.

## Jaki próg wybrać {#choosing-a-threshold}

Ustaw go na tyle wcześnie, żeby zdążyć zareagować. Jeśli zadziała w dniu, w którym coś się kończy, nie jest żadnym ostrzeżeniem.

:::warning Część sprzętu pracuje dalej na pusto
Głowica DŌS z pustym pojemnikiem dalej realizuje harmonogram i zgłasza dawki, których nigdy nie podała. Nie ma własnego ostrzeżenia o niskim poziomie. Wyłapiesz to właśnie alertem uzupełnienia, więc ustaw go dla każdej głowicy, z której dozujesz.
:::

## Po uzupełnieniu {#after-refilling}

Daj znać Corze na stronie urządzenia, żeby alert zniknął, a kolejne ostrzeżenie zostało policzone od właściwego poziomu.

| Urządzenie | Dotknij |
|---|---|
| Głowica DŌS | **Napełnij**, a potem **Pełny**, albo ustaw **Pozostała objętość** |
| Zbiornik odpadów DŌS | Po opróżnieniu przywróć jego wolne miejsce do pełnego |
| Głowica ReefDose | **Pozostało w butelce** |
| ReefMat | **Nowa rolka (Beta)** po założeniu nowej rolki |
| EcoTech Versa *(Beta)* | **Oznacz jako uzupełniony** |

Trident, ReefATO+ i AquaWiz same podają swoje poziomy, więc w Corze nie trzeba niczego resetować.

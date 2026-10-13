---
title: Lampy, pompy i dozowniki EcoTech
description: Połącz z Corą lampy EcoTech Radion, pompy VorTech i dozowniki Versa przez Bluetooth i zobacz, co możesz z nimi zrobić.
section: Cora Mobile
reviewed: 2026-10-13
order: 18
group: Equipment
---

:::note Beta
**Beta.** EcoTech jest w wersji Beta i jest dostępny tylko dla użytkowników Beta. Jeśli nie jesteś użytkownikiem Beta, nie zobaczysz go w **Dodaj urządzenie**. Aby poprosić o dostęp do Beta, skontaktuj się z [pomocą techniczną](/support.html).
:::

Na tej stronie połączysz z Corą lampy EcoTech Radion, pompy VorTech i dozowniki Versa i nauczysz się nimi sterować. Zacznij od **Urządzenia → Dodaj urządzenie → EcoTech**. Ten sam wiersz znajduje też urządzenia AquaIllumination, NYOS Quantum, Nero i Orbit, które są w tej samej sieci Bluetooth.

## Czego potrzebujesz {#what-you-need}

- Cora Max w akwarium. To on wykonuje odczyt i wysyła Twoje polecenia do sprzętu przez Bluetooth. Bez niego wiersz **EcoTech** pokazuje **Wymaga Cora Max** i pozostaje wyszarzony.
- Włączonego Bluetooth w telefonie, z uprawnieniem Bluetooth dla Cory. Cora prosi o nie przy skanowaniu.
- Włączonego sprzętu w zasięgu Cora Max.

## Łączenie {#linking-it}

1. Przejdź do **Urządzenia → Dodaj urządzenie → EcoTech**.
2. Cora skanuje pobliskie lampy, pompy i dozowniki. Lampy połączone już z własną aplikacją EcoTech Mobius mogą się nie pokazać.
3. Sprzęt z tej samej sieci Bluetooth jest zgrupowany jako jeden **Zbiornik Mobius**. Dotknij **Połącz z…** i wybierz akwarium Cora, do którego należy.
4. Nazwij grupę, gdy Cora o to poprosi, i gotowe.

Urządzenie oznaczone **Tylko odczyt** pokazuje swoje odczyty, ale Cora nie może jeszcze nim sterować. Sterowanie tym modelem pojawi się, gdy zostanie przetestowane.

Jeśli w tej samej sieci Bluetooth są też lampy innego akwarium, a oba akwaria odczytują różne Cora Max, Cora pokaże **Odczytywane przez jeden Cora Max**. Jeden Cora Max odczytuje wtedy całą sieć dla obu akwariów.

Jeśli nic nie znaleziono, sprawdź, czy Bluetooth jest włączony, a sprzęt zasilony, i dotknij **Skanuj ponownie**.

## Lampy Radion {#radion}

![Strona Radion w Cora Mobile](img/mobile-radion.webp "Stan, lampy w tej sieci (wszystkie albo jedna), a pod nimi intensywność i każdy kanał koloru.")

Strona lampy ma edytor harmonogramu i szybkie sceny (**Harmonogram**, **Burza**, **Chmury**, **Kolory**, **Karmienie**, **Wyłączone**). Możesz też ustawić aklimatyzację, wentylator, cykl księżycowy i zegar.

W edytorze harmonogramu **Podgląd dnia** odtwarza cały dzień w przyspieszeniu, więc zobaczysz go bez czekania. **Zatrzymaj podgląd** przywraca lampy. **Cofnij** i **Ponów** przechodzą przez Twoje zmiany, a **Zacznij od…** zaczyna nowy harmonogram od kopii istniejącego.

Cora odczytuje lampy co jakiś czas. W **Ustawieniach Radion**, w sekcji **Odczyt**, pole **Odczytuj światła co** ustawia, jak często. Rzadziej jest łagodniej dla lamp. Otwarcie strony i każde polecenie nadal odczytują lampy od razu.

**Ustawienia Radion** mają też:

- **Ustaw zegar**, do ustawienia zegara lampy.
- **Aklimatyzacja**, dla nowych koralowców: cały harmonogram rośnie stopniowo przez ustawioną liczbę dni. Włączenie jej zaczyna ją od nowa od niższego poziomu.
- **Alerty**: **Światło przestaje odpowiadać**, **Usterka: ciepło, wentylator lub LED**, **Zegar przesunięty o 5 min** i **Temperatura LED**. Włącz te, które chcesz.

## Pompy VorTech {#vortech}

Kafelek VorTech pokazuje tryb i prędkość pompy. Możesz zmienić tryb i **Prędkość**, edytować harmonogram i uruchomić **Karmienie** na kilka minut. Karmienie zwalnia wszystkie pompy VorTech w akwarium, a po jego końcu wracają one do swoich harmonogramów. Przy każdym trybie jest krótki opis, od równomiernego przepływu po fale jak na grzbiecie rafy, pływy i pulsy. Pompa oferuje tylko te tryby, które obsługuje.

## Dozowniki Versa {#versa}

Strona Versy pokazuje jej pojemnik, dawki i limity. Możesz ustawić rozmiar pojemnika, dotknąć **Oznacz jako uzupełniony**, użyć **Dozuj teraz**, **Wstrzymaj** dozowanie do północy i edytować harmonogram. Cora przechowuje historię dawek każdej głowicy. Dzwonek ustawia alerty uzupełnienia w pozostałych dniach albo w tym, jak pełny jest pojemnik, tak jak opisują [Materiały eksploatacyjne](/help/mobile-consumables).

:::warning Jeszcze niesprawdzone na sprzęcie
Polecenia dla pomp VorTech i dozowników Versa nie zostały jeszcze sprawdzone na prawdziwym sprzęcie. Odczyt działa. Przy pierwszych zmianach sprawdzaj sam sprzęt i daj nam znać, co widzisz, przez [Zgłaszanie problemu](/help/mobile-support).
:::

## Alerty {#alerts}

Cora uznaje urządzenie EcoTech za ciche po trzech brakujących odczytach, liczonych według jego własnego interwału odczytu. Sieć z samymi lampami jest domyślnie odczytywana co 30 minut, więc trwa to co najmniej 90 minut. Zobacz [Alerty i progi](/help/mobile-alerts). Lampy Radion mają też własne alerty w **Ustawieniach Radion**, opisane wyżej.

## Na Cora Max {#on-cora-max}

Ten sam sprzęt ma własne strony na ekranie na ścianie. Więcej w [Sterowaniu sprzętem z Cora Max](/help/max-device-control).

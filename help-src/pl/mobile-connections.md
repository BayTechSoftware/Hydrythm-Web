---
title: Podłączanie sprzętu
description: Jak podłączyć do Cory urządzenie Neptune Apex, Red Sea ReefBeat, Jecod albo AquaWiz oraz, w wersji Beta, sprzęt Maxspect, GHL, HYDROS, Focustronic i Inkbird.
section: Cora Mobile
reviewed: 2026-10-13
order: 12
group: Equipment
---

Ta strona pokazuje, jak podłączyć do Cory sprzęt każdej marki i czego potrzebuje każde połączenie. Wszystkie zaczynają się tak samo: **Urządzenia → Dodaj urządzenie**, a potem wybór marki.

![Lista Dodaj urządzenie u użytkownika Beta](img/mobile-add-device-beta.webp "Lista marek. Marki Beta mają chip Beta.")

Marki oznaczone *(Beta)* są dostępne tylko dla użytkowników Beta. Zobacz [Funkcje Beta](/help/mobile-beta).

| Marka | Co otwiera | Bez Cora Max |
|---|---|---|
| Cora | Wyszukiwanie nowego Cora Max przez Wi-Fi albo Bluetooth | |
| Neptune Apex | Skanowanie sieci albo jego adres IP, a potem wybór akwariów, które obsługuje | Tylko lokalnie |
| Red Sea | Skanowanie Twojej sieci, a potem wybór akwarium dla każdego urządzenia | Tylko lokalnie |
| Jecod / Jebao | Skanowanie Twojej sieci albo Bluetooth | Tylko lokalnie |
| AquaWiz | Logowanie do AquaWiz | Działa |
| Maxspect *(Beta)* | To samo skanowanie co Jecod | **Wymaga Cora Max** |
| GHL *(Beta)* | Jego adres, interfejs, a dla mini także login | **Wymaga Cora Max** |
| HYDROS *(Beta)* | Klucz urządzenia z aplikacji HYDROS | Działa |
| Focustronic *(Beta)* | Logowanie do Focustronic, a potem wybór akwarium dla każdego urządzenia | Działa |
| EcoTech *(Beta)* | Wyszukiwanie przez Bluetooth lamp Radion, pomp VorTech i dozowników Versa. Zobacz [Lampy, pompy i dozowniki EcoTech](/help/mobile-ecotech) | **Wymaga Cora Max** |
| Inkbird *(Beta)* | Wyszukiwanie przez Bluetooth monitora powietrza w pomieszczeniu | **Wymaga Cora Max** |
| Kamera *(Beta)* | Wyze, Tapo, Sonoff albo inna kamera RTSP. Zobacz [Kamery i Czuwanie skimmera](/help/mobile-cameras) | **Wymaga Cora Max** |

## Bez Cora Max: tylko lokalnie {#local-only}

Sprzęt Neptune Apex, Red Sea i Jecod jest w Twojej sieci domowej (albo na Bluetooth). Jeśli nie masz Cora Max (albo nie ma go przy akwarium, do którego dodajesz sprzęt), ekran dodawania tych marek pokazuje *Bez Cora Max ta integracja działa tylko lokalnie w aplikacji Mobile.* To oznacza, że:

- Telefon odczytuje sprzęt i nim steruje, gdy Cora Mobile jest otwarta w tej samej sieci albo w zasięgu Bluetooth.
- Poza domem widzisz ostatnie odczyty zapisane przez telefon i nie możesz nim sterować.

Cora Max przy akwarium odczytuje ten sprzęt przez całą dobę i przekazuje Twoje polecenia, gdy jesteś poza domem. Z AquaWiz, HYDROS i Focustronic Cora łączy się przez własną usługę producenta, więc działają z każdego miejsca bez Cora Max. Wiersze oznaczone **Wymaga Cora Max** są wyszarzone, dopóki akwarium go nie ma. Więcej w [Więcej niż jedno urządzenie Cora](/help/mobile-multi-device).

## Neptune Apex {#neptune-apex}

Cora odczytuje Twój Apex przez sieć lokalną, w tym sondy, gniazda i zamontowane moduły rozszerzeń.

1. Przejdź do **Urządzenia → Dodaj urządzenie → Neptune Apex**.
2. Dotknij **Skanuj sieć w poszukiwaniu APEX** i wybierz swój Apex albo wpisz jego adres w **Lub wpisz IP ręcznie:**.
3. Wypełnij **Login Apex (tylko jeśli został ustawiony w Apex):**. Zostaw hasło puste, jeśli go nie ustawiono.
4. Dotknij **Wczytaj metryki z APEX** i zaznacz te, które chcesz, w **Metryki do śledzenia**.
5. Ustaw **Częstotliwość odpytywania**. Nie zostawiaj jej wyłączonej: przy wyłączonym odpytywaniu nic nie odczytuje Apex, a jego odczyty stają się nieaktualne.
6. Dotknij **Dalej**, zaznacz każde akwarium w **Którym akwariom służy ten Apex?**, a potem dotknij **Zapisz**. Apex może obsługiwać więcej niż jedno akwarium.

Jeśli skanowanie nic nie znajdzie, sprawdź, czy telefon jest w tej samej sieci Wi-Fi co Apex, albo wpisz adres IP samodzielnie.

Po połączeniu każda sonda, którą zgłasza Apex, staje się źródłem, które możesz umieścić na pulpicie. Gniazda pojawiają się jako elementy sterowania, a każdy zamontowany moduł rozszerzeń dostaje własny kafelek urządzenia. Twoje własne programowanie Apex działa dalej dokładnie tak, jak je ustawiono. Czym możesz sterować, opisuje [Sterowanie sprzętem](/help/mobile-device-control#neptune-apex).

## Red Sea ReefBeat {#red-sea-reefbeat}

Cora łączy się ze sprzętem ReefBeat w sieci lokalnej. Obsługuje **ReefDose**, **ReefATO+**, **ReefMat** i **ReefRun**, a także **ReefControl**, **ReefControl Power**, **ReefWave** i **ReefLED**, które mają w nazwie *(Beta)*, ale są dostępne dla wszystkich.

1. Najpierw skonfiguruj urządzenie w aplikacji ReefBeat od Red Sea i sprawdź, czy jest w tej samej sieci co telefon.
2. Przejdź do **Urządzenia → Dodaj urządzenie → Red Sea**. Cora przeskanuje Twoją sieć.
3. Wybierz, do którego akwarium należy każde urządzenie.

Urządzenie Red Sea obsługuje jedno akwarium. Wybranie innego przenosi je tam.

Każde urządzenie dostaje własną stronę, a jego odczyty stają się źródłami. ReefDose zgłasza swoje głowice i pojemniki, ReefATO+ swój zbiornik i dolewki, ReefMat liczbę pozostałych dni, a ReefRun stan pomp. ReefControl zgłasza swoje sondy w ten sam sposób. ReefWave i ReefLED na razie pokazują tylko swój tryb. Co pozwala robić każda strona, opisuje [Sterowanie sprzętem](/help/mobile-device-control#red-sea).

## Jecod / Jebao {#jecod}

Cora łączy się z pompami Jecod i może je odczytywać i nimi sterować. Dodaj pompę z **Urządzenia → Dodaj urządzenie → Jecod**. Pompa Jecod łączy się z Corą na jeden z dwóch sposobów i od tego zależy, co możesz z nią robić.

![Ekran dodawania pompy w Cora Mobile, bez znalezionych jeszcze pomp](img/mobile-connections.webp "Jeszcze nic nie znaleziono: skanowanie wyjaśnia, czego potrzebuje i dlaczego pompa może nie odpowiedzieć na jedno wyszukiwanie.")

**Przez Twoją sieć.** Skanowanie znajduje pompy, które same się ogłaszają, więc nie musisz wpisywać adresu. Pompę sieciową możesz odczytywać i nią sterować, gdy jest zasilona i osiągalna. Oznacza to, że telefon jest w tej samej sieci albo Cora Max w tej sieci przekazuje Twoje polecenia. Jeśli jesteś poza domem i na miejscu nie ma Cora Max, widzisz pompę sieciową, ale nie możesz nią sterować.

:::note Pompa często nie odpowiada na pierwsze skanowanie
Pompy odpowiadają na jedno skanowanie, a na następne już nie. Jeśli Twojej nie ma na liście, przeskanuj ponownie, zanim uznasz, że jest nieosiągalna.
:::

Jeśli wyszukiwanie nic nie znajdzie, wynik pokazuje adresy sprawdzone przez Wi-Fi. Jeśli aplikacja Jebao pokazuje dla pompy inny adres, telefon jest w innej sieci. Sieć gościnna albo IoT, a także pasmo wyłącznie 5 GHz, nie widzi tych pomp. Na iPhonie Cora potrzebuje też dostępu do sieci lokalnej, żeby widzieć pompy w Twojej sieci Wi-Fi. Bez niego lista zostaje pusta i nie pojawia się żaden błąd, więc wynik to wyjaśnia i proponuje **Otwórz Ustawienia**, żeby włączyć dostęp ponownie. Możesz tam też przejść w każdej chwili z **Ustawienia → Dostęp do urządzeń**, opisanego w [Ustawieniach](/help/mobile-settings).

**Przez Bluetooth.** Z niektórymi pompami połączy się tylko telefon stojący blisko nich. Strona pompy o tym mówi i pokazuje ostatnio odczytane ustawienia oraz ich wiek. Cora potrzebuje do tego uprawnienia Bluetooth. Nadaj je przed dodaniem pompy Bluetooth, bo inaczej Cora w ogóle jej nie znajdzie.

:::warning Musisz być blisko pompy Bluetooth
Jej strona pokazuje ostatnie ustawienia odczytane przez Corę i to, jak dawno to było. Każda zmiana, nawet uruchomienie przerwy na karmienie, wymaga pompy w zasięgu. Stań blisko niej i ponownie otwórz stronę.
:::

Przy obu połączeniach dostajesz stan na żywo, tryb i intensywność, przerwę na karmienie i program dnia. Przerwa na karmienie uruchomiona z telefonu przy niektórych pompach wymaga otwartej strony pompy. Szczegóły są w [Sterowaniu sprzętem](/help/mobile-device-control#jecod), a program dnia opisują [Harmonogramy sprzętu](/help/mobile-schedules).

## AquaWiz KH Controller {#aquawiz-kh-controller}

Cora odczytuje alkaliczność z kontrolera AquaWiz KH przez Twoje konto AquaWiz, więc działa to poza domem i nie wymaga Cora Max.

1. Przejdź do **Urządzenia → Dodaj urządzenie → AquaWiz**.
2. Wpisz nazwę użytkownika i hasło AquaWiz i dotknij **Połącz**.
3. Wybierz akwarium, włącz **Odczytuj też jego pH**, jeśli chcesz, i dotknij **Połącz z Cora**.

Gdy **Automatycznie utrzymuj połączenie** jest włączone, Cora przechowuje Twoje hasło AquaWiz i sama odnawia połączenie. Gdy jest wyłączone, Cora przechowuje tylko token logowania, który AquaWiz unieważnia mniej więcej co 30 dni, i wysyła Ci powiadomienie, gdy trzeba zalogować się ponownie.

Dostajesz alkaliczność jako źródło, aktualizowaną tak często, jak Twój kontroler miareczkuje, a także pH, jeśli to włączono i Twoje urządzenie je zgłasza. Co pokazuje karta AquaWiz i jej alert suplementu, opisuje [Sterowanie sprzętem](/help/mobile-device-control#aquawiz).

:::warning Cora używa tego samego logowania AquaWiz
AquaWiz daje każdemu kontu jedno logowanie, więc Cora używa tego samego co aplikacja AquaWiz. Jeśli zmienisz hasło AquaWiz, Cora się rozłączy. Połącz ją potem ponownie z wiersza urządzenia. Żeby całkowicie odebrać Corze dostęp, usuń urządzenie w Corze i zmień hasło AquaWiz.
:::

## Maxspect {#maxspect}

:::note Beta
**Beta.** Maxspect jest w wersji Beta i jest dostępny tylko dla użytkowników Beta. Jeśli nie jesteś użytkownikiem Beta, nie zobaczysz go w **Dodaj urządzenie**. Aby poprosić o dostęp do Beta, skontaktuj się z [pomocą techniczną](/support.html). Część funkcji sterowania może być ograniczona, a to, co tu widzisz, może się zmieniać między aktualizacjami. Jeśli coś nie działa tak, jak opisano, daj nam znać przez [Zgłaszanie problemu](/help/mobile-support).
:::

Cora łączy się z pompami Maxspect Gyre i może je odczytywać i nimi sterować. Dodaj pompę z **Urządzenia → Dodaj urządzenie → Maxspect**, tym samym skanowaniem, którego używa Jecod. Wymaga Cora Max w akwarium. Bez niego wiersz pokazuje **Wymaga Cora Max**.

Gdy dodajesz Gyre, musi być w tej samej sieci co telefon. Potem Cora Mobile łączy się z nim przez Cora Max akwarium, nawet gdy jesteś poza domem. Wzór fali, prędkość, harmonogram i **Stan pompy** opisuje [Sterowanie sprzętem](/help/mobile-device-control#maxspect).

## GHL ProfiLux i Mitras {#ghl-profilux-and-mitras}

:::note Beta
**Beta.** GHL jest w wersji Beta i jest dostępny tylko dla użytkowników Beta. Jeśli nie jesteś użytkownikiem Beta, nie zobaczysz go w **Dodaj urządzenie**. Aby poprosić o dostęp do Beta, skontaktuj się z [pomocą techniczną](/support.html). Część odczytów albo funkcji sterowania może jeszcze nie działać. Jeśli coś nie działa tak, jak opisano, daj nam znać przez [Zgłaszanie problemu](/help/mobile-support).
:::

Cora odczytuje kontroler GHL ProfiLux albo Mitras: sondy, gniazda, dozowniki, czujniki poziomu, a w modelach Director także wyniki testów KH i jonów.

1. Przejdź do **Urządzenia → Dodaj urządzenie → GHL**. Wymaga Cora Max w akwarium, a bez niego pokazuje **Wymaga Cora Max**.
2. Telefon nie może go wyszukać, więc wpisz jego adres i samodzielnie wybierz interfejs: **Oficjalne API**, **HTTP** albo **ProfiLux mini** (który wymaga też loginu).
3. Wybierz, do którego akwarium należy. Kontroler GHL może obsługiwać więcej niż jedno akwarium.

Kontroler GHL nie łączy się z telefonem bezpośrednio. Pokazuje **Czeka na Cora Max**, dopóki nie odczyta go Cora Max w jego sieci, a potem jego odczyty i elementy sterowania pojawiają się wszędzie.

API GHL musi być włączone, żeby Cora w ogóle mogła połączyć się z kontrolerem. GHL wyłącza je po każdej aktualizacji oprogramowania, więc jeśli nic się nie pojawia, sprawdź to najpierw. [Rozwiązywanie problemów](/help/troubleshooting) opisuje, co zrobić. Sterowanie opisuje [Sterowanie sprzętem](/help/mobile-device-control#ghl).

## HYDROS {#hydros}

:::note Beta
**Beta.** HYDROS jest w wersji Beta i jest dostępny tylko dla użytkowników Beta. Jeśli nie jesteś użytkownikiem Beta, nie zobaczysz go w **Dodaj urządzenie**. Aby poprosić o dostęp do Beta, skontaktuj się z [pomocą techniczną](/support.html). Część odczytów albo funkcji sterowania może jeszcze nie działać. Jeśli coś nie działa tak, jak opisano, daj nam znać przez [Zgłaszanie problemu](/help/mobile-support).
:::

HYDROS nie wymaga, żeby telefon i kontroler były w tej samej sieci, ani Cora Max. Cora łączy się z nim przez własną chmurę HYDROS, więc działa poza domem, a nawet przy zamkniętej Cora Mobile.

1. W aplikacji HYDROS utwórz **klucz urządzenia** (device key) dla dostawcy **cora-iq**. Wybierz **Read**, jeśli chcesz tylko jego odczytów, albo **Write**, jeśli chcesz też sterować nim z Cory.
2. W Cora Mobile przejdź do **Urządzenia → Dodaj urządzenie → HYDROS**. Ekran nazywa się **Dodaj HYDROS (Beta)**.
3. Wklej klucz w **Klucz urządzenia HYDROS**, dotknij **Sprawdź klucz**, wybierz akwarium i dotknij **Połącz**.

Po połączeniu Cora importuje ostatnie 33 dni jego historii, a potem odczytuje dalej od tego miejsca. [Sterowanie sprzętem](/help/mobile-device-control#hydros) opisuje, co możesz odczytywać i, z kluczem zapisu, czym sterować.

## Focustronic {#focustronic}

:::note Beta
**Beta.** Focustronic jest w wersji Beta i jest dostępny tylko dla użytkowników Beta. Jeśli nie jesteś użytkownikiem Beta, nie zobaczysz go w **Dodaj urządzenie**. Aby poprosić o dostęp do Beta, skontaktuj się z [pomocą techniczną](/support.html).
:::

Cora odczytuje urządzenia Focustronic Alkatronic, Dosetronic i Mastertronic przez Twoje konto Focustronic, więc działa to poza domem i nie wymaga Cora Max.

1. Przejdź do **Urządzenia → Dodaj urządzenie → Focustronic** i zaloguj się tym samym kontem, którego używasz w aplikacji Focustronic.
2. Wybierz, do którego akwarium należy każde urządzenie, a potem dotknij **Połącz z Cora**.

**Pozostań zalogowany** pozwala Corze przechowywać Twoje hasło Focustronic, zaszyfrowane, i samej logować się ponownie. Jeśli to wyłączysz, Cora przechowuje tylko tymczasowe logowanie i wysyła Ci powiadomienie, gdy trzeba zalogować się ponownie. Jeśli Focustronic odrzuci logowanie, otwórz **Dodaj Focustronic** i zaloguj się ponownie.

Co pokazuje każde urządzenie, a także **Zmierz teraz**, **Dozuj teraz** i **Testuj teraz**, opisuje [Sterowanie sprzętem](/help/mobile-device-control#focustronic).

## Monitor powietrza w pomieszczeniu Inkbird {#inkbird-room-air-monitor}

:::note Beta
**Beta.** Inkbird jest w wersji Beta i jest dostępny tylko dla użytkowników Beta. Jeśli nie jesteś użytkownikiem Beta, nie zobaczysz go w **Dodaj urządzenie**. Aby poprosić o dostęp do Beta, skontaktuj się z [pomocą techniczną](/support.html).
:::

Cora odczytuje monitor powietrza w pomieszczeniu Inkbird IAM-T1 albo IAM-T2. Odczytuje go przez Bluetooth Cora Max przy akwarium, a Cora nigdy niczego nie zapisuje w monitorze. Wiersz pokazuje **Wymaga Cora Max**, dopóki akwarium go nie ma.

1. Przejdź do **Urządzenia → Dodaj urządzenie → Inkbird**. Cora szuka monitorów w pobliżu. Bluetooth musi być włączony, z uprawnieniem dla Cory.
2. Wybierz swój i dotknij **Połącz ze zbiornikiem**. Jeśli żaden się nie pojawi, podejdź bliżej i dotknij **Szukaj ponownie**.

Strona monitora pokazuje jego ostatni odczyt. **Interwał pomiaru** ustala, jak często odczytuje go Cora Max. Dopóki Cora Max go nie odczyta, strona pokazuje **Oczekiwanie na Cora Max**. Jeśli ucichnie, pokazuje **Brak danych**, a Cora Cię ostrzega. Odczyty z pomieszczenia trafiają też do [Reef Buddy](/help/mobile-reef-buddy). Żeby zakończyć, dotknij **Odłącz**. Cora Max przestaje go odczytywać, a historia zostaje.

## Ręczne zapisywanie {#logging-by-hand}

Niektóre parametry pochodzą z testu kropelkowego, a nie ze sprzętu. Żeby wpisać wynik, przewiń na dół pulpitu i dotknij **Zapisz parametry**.

Odczyty zapisane ręcznie liczą się tak samo jak inne. Pokazują się na widżetach z własnym źródłem i wiekiem i trafiają do Reef Buddy. Cora porównuje też z nimi Twoje sondy, gdy mówi, że dwa źródła się nie zgadzają.

## Gdy połączenie przestaje działać {#if-a-connection-stops-working}

Wiersz urządzenia mówi, jaki to rodzaj problemu. Znajdź go w tabeli w [Dodawaniu, edytowaniu i usuwaniu urządzeń](/help/mobile-devices#health). We wszystkim, czego tam nie ma, zobacz [Rozwiązywanie problemów](/help/troubleshooting).

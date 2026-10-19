---
title: Podłączanie sprzętu
description: Jak podłączyć do Cory urządzenie Neptune Apex, Red Sea ReefBeat, Jecod albo AquaWiz.
section: Cora Mobile
reviewed: 2026-10-18
order: 12
group: Equipment
---

Ta strona pokazuje, jak podłączyć do Cory sprzęt każdej marki i czego potrzebuje każde połączenie. Wszystkie zaczynają się tak samo: **Urządzenia → Dodaj urządzenie**, a potem wybór marki.

![Lista marek w Dodaj urządzenie](img/mobile-add-device-brands.webp "Lista marek.")


| Marka | Co otwiera | Bez Cora Max |
|---|---|---|
| Cora | Wyszukiwanie nowego Cora Max przez Wi-Fi albo Bluetooth | |
| Neptune Apex | Skanowanie sieci albo jego adres IP, a potem wybór akwariów, które obsługuje | Tylko lokalnie |
| Red Sea | Skanowanie Twojej sieci, a potem wybór akwarium dla każdego urządzenia | Tylko lokalnie |
| Jecod / Jebao | Skanowanie Twojej sieci albo Bluetooth | Tylko lokalnie |
| AquaWiz | Logowanie do AquaWiz | Działa |

## Bez Cora Max: tylko lokalnie {#local-only}

Sprzęt Neptune Apex, Red Sea i Jecod jest w Twojej sieci domowej (albo na Bluetooth). Jeśli nie masz Cora Max (albo nie ma go przy akwarium, do którego dodajesz sprzęt), ekran dodawania tych marek pokazuje *Bez Cora Max ta integracja działa tylko lokalnie w aplikacji Mobile.* To oznacza, że:

- Telefon odczytuje sprzęt i nim steruje, gdy Cora Mobile jest otwarta w tej samej sieci albo w zasięgu Bluetooth.
- Poza domem widzisz ostatnie odczyty zapisane przez telefon i nie możesz nim sterować.

Cora Max przy akwarium odczytuje ten sprzęt przez całą dobę i przekazuje Twoje polecenia, gdy jesteś poza domem. Z AquaWiz Cora łączy się przez własną usługę producenta, więc działa z każdego miejsca bez Cora Max. Więcej w [Więcej niż jedno urządzenie Cora](/help/mobile-multi-device).

## Neptune Apex {#neptune-apex}

Cora odczytuje Twój Apex przez sieć lokalną, w tym sondy, gniazda i zamontowane moduły rozszerzeń.

1. Przejdź do **Urządzenia → Dodaj urządzenie → Neptune Apex**.
2. Dotknij **Skanuj sieć w poszukiwaniu APEX** i wybierz swój Apex albo wpisz jego adres w **Lub wpisz IP ręcznie:**.
3. Wypełnij **Login Apex (tylko jeśli został ustawiony w Apex):**. Zostaw hasło puste, jeśli go nie ustawiono.
4. Dotknij **Wczytaj parametry z APEX** i zaznacz te, które chcesz, w **Parametry do śledzenia**.
5. Ustaw **Częstotliwość odpytywania**. Nie zostawiaj jej wyłączonej: przy wyłączonym odpytywaniu nic nie odczytuje Apex, a jego odczyty stają się nieaktualne.
6. Dotknij **Dalej**, zaznacz każde akwarium w **Którym akwariom służy ten Apex?**, a potem dotknij **Zapisz**. Apex może obsługiwać więcej niż jedno akwarium.

Jeśli skanowanie nic nie znajdzie, sprawdź, czy telefon jest w tej samej sieci Wi-Fi co Apex, albo wpisz adres IP samodzielnie.

Po połączeniu każda sonda, którą zgłasza Apex, staje się źródłem, które możesz umieścić na panelu. Gniazda pojawiają się jako elementy sterowania, a każdy zamontowany moduł rozszerzeń dostaje własny kafelek urządzenia. Twoje własne programowanie Apex działa dalej dokładnie tak, jak je ustawiono. Czym możesz sterować, opisuje [Sterowanie sprzętem](/help/mobile-device-control#neptune-apex).

## Red Sea ReefBeat {#red-sea-reefbeat}

Cora łączy się ze sprzętem ReefBeat w sieci lokalnej. Obsługuje **ReefDose**, **ReefATO+**, **ReefMat** i **ReefRun**.

1. Najpierw skonfiguruj urządzenie w aplikacji ReefBeat od Red Sea i sprawdź, czy jest w tej samej sieci co telefon.
2. Przejdź do **Urządzenia → Dodaj urządzenie → Red Sea**. Cora przeskanuje Twoją sieć.
3. Wybierz, do którego akwarium należy każde urządzenie.

Urządzenie Red Sea obsługuje jedno akwarium. Wybranie innego przenosi je tam.

Każde urządzenie dostaje własną stronę, a jego odczyty stają się źródłami. ReefDose zgłasza swoje głowice i pojemniki, ReefATO+ swój zbiornik i dolewki, ReefMat liczbę pozostałych dni, a ReefRun stan pomp. Co pozwala robić każda strona, opisuje [Sterowanie sprzętem](/help/mobile-device-control#red-sea).

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

Cora odczytuje alkaliczność z kontrolera AquaWiz KH przez chmurę AquaWiz, więc działa to poza domem i nie wymaga Cora Max. Cora Max dodaje odczyty co godzinę: zobacz [Jak Cora odczytuje Twój AquaWiz](#how-cora-reads-aquawiz).

1. Przejdź do **Urządzenia → Dodaj urządzenie → AquaWiz**.
2. Wpisz nazwę użytkownika i hasło AquaWiz i dotknij **Połącz**.
3. Wybierz akwarium, sprawdź **Odczytuj też jego pH** (dla urządzenia, które zgłasza pH, na początku jest włączone) i dotknij **Połącz z Cora**.

Gdy **Automatycznie utrzymuj połączenie** jest włączone, Cora przechowuje Twoje hasło AquaWiz i sama odnawia połączenie. Gdy jest wyłączone, Cora przechowuje tylko token logowania, który AquaWiz unieważnia mniej więcej co 30 dni, i wysyła Ci powiadomienie, gdy trzeba zalogować się ponownie.

Dostajesz alkaliczność jako źródło, a także pH, jeśli Twoje urządzenie je zgłasza i **Odczytuj też jego pH** jest włączone. Pierwszy odczyt przychodzi zaraz po połączeniu. Potem AquaWiz pozwala Corze automatycznie czytać swoją chmurę tylko co 12 godzin, więc odczyt stamtąd może mieć nawet pół doby. Cora Max przy akwarium może też sam czytać kontroler co godzinę, gdy może go osiągnąć. Otwórz stronę urządzenia, żeby zobaczyć, kiedy zmierzono każdy odczyt i skąd pochodzi, i dotknij **Odczytaj teraz**, żeby dostać świeży (najwyżej raz na 15 minut). Co pokazuje karta AquaWiz i jej alerty, opisuje [Sterowanie sprzętem](/help/mobile-device-control#aquawiz).

Aby przenieść kontroler do innego akwarium, otwórz jego stronę w **Urządzenia** i dotknij **Zmień** w sekcji **Akwaria**. Nie musisz ponownie logować się do AquaWiz.

:::warning Cora używa tego samego logowania AquaWiz
AquaWiz daje każdemu kontu jedno logowanie, więc Cora używa tego samego co aplikacja AquaWiz. Jeśli zmienisz hasło AquaWiz, Cora się rozłączy. Połącz ją potem ponownie z wiersza urządzenia. Żeby całkowicie odebrać Corze dostęp, usuń urządzenie w Corze i zmień hasło AquaWiz.
:::

### Jak Cora odczytuje Twój AquaWiz {#how-cora-reads-aquawiz}

Cora dociera do AquaWiz maksymalnie trzema drogami, które działają razem.

| Droga | Co daje Corze | Jak często |
| --- | --- | --- |
| Twoje logowanie do AquaWiz | Znajduje Twoje kontrolery, odczytuje ich ustawienia (docelowe KH, siłę dozowania, pojemnik) i pobiera dzienną historię. | Raz na dobę i gdy potrzebne są ustawienia |
| Usługa Cora od AquaWiz | Najnowszy odczyt KH i pH. | Po połączeniu, potem co 12 godzin (limit AquaWiz) oraz gdy otworzysz stronę urządzenia lub dotkniesz **Odczytaj teraz** (najwyżej co 15 minut) |
| Cora Max przy akwarium | Odczytuje kontroler bezpośrednio przez jego własne Wi-Fi i dodaje alerty pompy, sondy pH i pojemnika z wodą. | Co godzinę |

Bez Cora Max odczyty przychodzą co 12 godzin, taki jest limit AquaWiz, więc odczyt może mieć nawet pół doby. **Chcesz odczyty co godzinę? Dodaj Cora Max przy akwarium.** [Zobacz Cora Max](https://coraiq.tech/pl/#max) i [skonfiguruj go](/help/max-setup). Wymaga kontrolera w zasięgu Wi-Fi Cora Max oraz oprogramowania kontrolera z dostępem lokalnym. Szczegóły są w [Odczyt co godzinę z Cora Max](/help/max-device-control#aquawiz-hourly).

Karta urządzenia pokazuje, skąd pochodzi każdy odczyt: **Co godzinę z Twojego Cora Max** albo **Z chmury AquaWiz, co 12 godzin**.


## Ręczne zapisywanie {#logging-by-hand}

Niektóre parametry pochodzą z testu kropelkowego, a nie ze sprzętu. Żeby wpisać wynik, przewiń na dół panelu i dotknij **Zapisz parametry**.

Odczyty zapisane ręcznie liczą się tak samo jak inne. Pokazują się na widżetach z własnym źródłem i wiekiem i trafiają do Reef Buddy. Cora porównuje też z nimi Twoje sondy, gdy mówi, że dwa źródła się nie zgadzają.

## Gdy połączenie przestaje działać {#if-a-connection-stops-working}

Wiersz urządzenia mówi, jaki to rodzaj problemu. Znajdź go w tabeli w [Dodawaniu, edytowaniu i usuwaniu urządzeń](/help/mobile-devices#health). We wszystkim, czego tam nie ma, zobacz [Rozwiązywanie problemów](/help/troubleshooting).

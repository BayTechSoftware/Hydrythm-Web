---
title: Podłączanie sprzętu
description: Jak podłączyć do Cory sprzęt Neptune Apex, Red Sea ReefBeat, Jecod, AquaWiz, GHL i HYDROS.
section: Cora Mobile
reviewed: 2026-09-30
order: 10
group: Equipment
---

Cora współpracuje ze sprzętem, który już masz. Tutaj znajdziesz listę obsługiwanego sprzętu i to, czego potrzebuje każde połączenie.

Każda marka łączy się trochę inaczej, więc zacznij od miejsca właściwego dla Twojego sprzętu:

| Marka | Gdzie zacząć |
|---|---|
| Neptune Apex | Od akwarium. Połączenie z Apex jest w jego profilu |
| Red Sea ReefBeat | Od akwarium |
| Jecod / Jebao | **Urządzenia → Znajdź pompę w Twojej sieci** albo Bluetooth |
| AquaWiz | **Urządzenia → Dodaj AquaWiz** |
| Maxspect *(beta)* | **Urządzenia → Znajdź pompę w Twojej sieci** |
| GHL ProfiLux / Mitras *(beta)* | Cora Max, z ustawień akwarium |
| HYDROS *(beta)* | **Urządzenia → Dodaj HYDROS (Beta)** |
| Cora Max | **Urządzenia → Dodaj urządzenie** |

## Neptune Apex

Cora odczytuje Apex przez sieć lokalną: sondy, gniazda i zamontowane moduły rozszerzeń.

Potrzebujesz adresu Apex w Twojej sieci i danych logowania do niego.

Każda sonda, którą zgłasza Apex, staje się źródłem, które możesz umieścić na pulpicie. Gniazda pojawiają się jako przełączniki, a zamontowane moduły rozszerzeń dostają własne kafelki urządzeń.

:::note Apex zachowuje własne programowanie
Cora odczytuje Apex, pokazuje go obok reszty sprzętu i przełącza gniazda, gdy ją o to poprosisz. Twoje programowanie w Apex działa dalej dokładnie tak, jak je ustawiono.
:::

## Red Sea ReefBeat

Cora łączy się ze sprzętem ReefBeat w sieci lokalnej. Obsługiwane są **ReefDose**, **ReefATO+**, **ReefMat**, **ReefRun**, a w wersji beta także **ReefControl**, **ReefControl Power**, **ReefWave** i **ReefLED**.

Sprzęt musi być już skonfigurowany w ReefBeat, a przy dodawaniu musi być w tej samej sieci co telefon.

Każde urządzenie dostaje własną stronę, a jego odczyty stają się źródłami. ReefDose zgłasza głowice i pojemniki. ReefATO+ zgłasza zbiornik i dolewki. ReefMat podaje, na ile dni wystarczy maty. ReefRun zgłasza stan pompy. ReefControl zgłasza swoje sondy w ten sam sposób. ReefWave i ReefLED *(beta)* na razie pokazują tylko tryb, wyłącznie do podglądu.

## Jecod / Jebao

Cora łączy się z pompami Jecod, odczytuje je i nimi steruje. Pompa Jecod łączy się z Corą na jeden z dwóch sposobów i od tego zależy, co możesz z nią zrobić.

![Wyszukiwanie pompy](img/mobile-connections.webp "Wyszukiwanie wyjaśnia, czego potrzebuje i czemu pompa może się nie pojawić za pierwszym razem.")

Pierwszy sposób to Twoja sieć. Użyj **Znajdź pompę w Twojej sieci**. Cora znajdzie pompy, które same się ogłaszają, więc nie trzeba wpisywać adresu. Pompę sieciową możesz odczytywać i sterować nią, gdy ma zasilanie **i jest osiągalna**. Oznacza to, że telefon jest w tej samej sieci albo Cora Max w tej sieci pośredniczy w połączeniu. Poza domem, jeśli na miejscu nie ma Cora Max, pompę tylko sieciową zobaczysz, ale nie zmienisz jej ustawień.

:::note Pompa często nie odpowiada za pierwszym razem
Pompy odpowiadają na jedno wyszukiwanie, a na następne już nie. Jeśli Twojej nie ma na liście, wyszukaj jeszcze raz. To nie znaczy, że jest nieosiągalna.
:::

Jeśli wyszukiwanie nic nie znajdzie, wynik pokaże adresy sprawdzone przez Wi-Fi. Jeśli w aplikacji Jebao pompa ma inny adres, telefon jest w innej sieci. W sieci gościnnej, sieci IoT albo w paśmie tylko 5 GHz te pompy nie są widoczne. Na iPhonie Cora potrzebuje też dostępu do sieci lokalnej, żeby widzieć pompy w Twoim Wi-Fi. Bez niego lista zostaje pusta i nie pojawia się żaden błąd. Dlatego wynik to wyjaśnia i proponuje przycisk **Otwórz Ustawienia**, żeby włączyć ten dostęp. To samo miejsce otworzysz w każdej chwili przez **Ustawienia → Dostęp do urządzeń**. Więcej w [Ustawieniach](/help/mobile-settings).

Drugi sposób to Bluetooth. Część pomp jest osiągalna tylko z telefonu, który jest blisko nich. Strona takiej pompy mówi o tym wprost. Pokazuje też ostatnie ustawienia, które udało się odczytać, i to, jak dawno to było.

Do tego Cora potrzebuje uprawnienia Bluetooth. Włącz je, zanim dodasz pompę Bluetooth. Bez niego Cora w ogóle nie wykryje pompy.

Cora pokazuje bieżący stan, tryb i intensywność, pauzę na karmienie oraz program dnia. Więcej w [Harmonogramach sprzętu](/help/mobile-schedules).

:::warning Pompa Bluetooth działa tylko z bliska
Jej strona pokazuje ostatnie ustawienia odczytane przez Corę i czas odczytu. Żeby cokolwiek zmienić, także włączyć pauzę na karmienie, pompa musi być w zasięgu. Podejdź do niej i otwórz stronę jeszcze raz.
:::

## Kontroler AquaWiz KH

Cora odczytuje alkaliczność z kontrolera AquaWiz KH przez Twoje konto AquaWiz.

Potrzebujesz nazwy użytkownika i hasła AquaWiz. Cora loguje się w Twoim imieniu i zachowuje to logowanie, żeby dalej odczytywać dane.

Alkaliczność staje się źródłem, które odświeża się tak często, jak kontroler wykonuje miareczkowanie. Jeśli Twój kontroler zgłasza pH, możesz je dodać.

Karta urządzenia pokazuje też Twoje docelowe KH, moc dawki i, dla urządzenia z ustawionym dozowaniem, jego maksymalną dawkę na godzinę oraz ile suplementu alkaliczności zostało w pojemniku. Te wartości pochodzą wprost z ustawień AquaWiz. Zmieniasz je w aplikacji AquaWiz. Jeśli Twoje urządzenie śledzi pojemnik, Cora ostrzega, gdy suplementu zaczyna brakować, domyślnie przy 100 mL.

:::warning Jedno wspólne logowanie
AquaWiz daje jedno logowanie na konto, więc Cora używa tego samego logowania co aplikacja AquaWiz. Po zmianie hasła AquaWiz Cora straci połączenie. Połącz ją ponownie z wiersza urządzenia. Jeśli chcesz całkiem odebrać Corze dostęp, usuń urządzenie w Corze i zmień hasło AquaWiz.
:::

## Maxspect

:::note Obsługa Maxspect jest w wersji beta
Obsługę gyre Maxspect wciąż testujemy i rozwijamy. Część ustawień może być ograniczona, a to, co tu widzisz, może się zmienić z kolejną aktualizacją. Jeśli coś nie działa tak, jak opisano, napisz do nas przez [Pomoc](/help/mobile-support).
:::

Cora łączy się z pompami Maxspect Gyre, odczytuje je i nimi steruje.

Przy dodawaniu gyre i telefon muszą być w tej samej sieci. Użyj **Urządzenia → Znajdź pompę w Twojej sieci**.

Cora pokazuje wzór fali i prędkość dla **Gyre A** i **Gyre B**, harmonogram gyre (tylko do podglądu, ustawiasz go w aplikacji Maxspect), **Stan pompy** oraz to, czy pompa pracuje i kiedy odczytano ją ostatnio. Więcej w [Sterowaniu sprzętem](/help/mobile-device-control).

:::note Jak Cora Mobile łączy się z gyre
Jeśli akwarium obsługuje Cora Max, Cora Mobile łączy się przez niego, także poza domem. **Zmień ustawienia** zaczyna wtedy od ostatniego odczytu z tego Cora Max. W przeciwnym razie telefon łączy się z gyre bezpośrednio i musi być w jego sieci. Otwarcie strony gyre odczytuje go wtedy od razu. Jeśli strona pokazuje starszy zapisany odczyt, przycisk **Zmień ustawienia** pozostaje ukryty, dopóki nie odświeżysz strony.
:::

## GHL ProfiLux i Mitras

:::note Obsługa GHL jest w wersji beta
Obsługę GHL wciąż testujemy i rozwijamy. Część odczytów albo funkcji sterowania może jeszcze nie działać, a to, co tu widzisz, może się zmienić z kolejną aktualizacją. Jeśli coś nie działa tak, jak opisano, napisz do nas przez [Pomoc](/help/mobile-support).
:::

Cora odczytuje kontroler GHL ProfiLux albo Mitras przez Twoją sieć lokalną: sondy, gniazda, dozowniki, czujniki poziomu, a w modelach Director także wyniki testów KH i jonów.

Podłączasz go z poziomu **Cora Max**, a nie telefonu: otwórz ustawienia akwarium i dodaj tam jego adres IP. Kroki opisuje [Sterowanie sprzętem z Cora Max](/help/max-device-control). Gdy już jest podłączony, jego odczyty i sterowanie pojawiają się też na telefonie.

Żeby Cora w ogóle dotarła do kontrolera, API GHL musi być włączone. GHL wyłącza je po każdej aktualizacji firmware, więc warto to sprawdzić najpierw, jeśli nic się nie pojawia. Co robić dalej, opisuje [Rozwiązywanie problemów](/help/troubleshooting).

## HYDROS

:::note Obsługa HYDROS jest w wersji beta
Obsługę HYDROS wciąż testujemy i rozwijamy. Część odczytów albo funkcji sterowania może jeszcze nie działać, a to, co tu widzisz, może się zmienić z kolejną aktualizacją. Jeśli coś nie działa tak, jak opisano, napisz do nas przez [Pomoc](/help/mobile-support).
:::

HYDROS to jedyna integracja, która nie wymaga, żeby Cora i kontroler były w tej samej sieci. Cora łączy się z nim przez własną chmurę HYDROS, więc działa też poza domem, a nawet przy zamkniętej aplikacji.

Żeby go podłączyć, otwórz aplikację HYDROS i utwórz **klucz urządzenia** dla dostawcy **cora-iq**. Wybierz **Odczyt**, jeśli chcesz tylko jego odczytów, albo **Zapis**, jeśli chcesz też sterować nim z Cory. Potem przejdź do **Urządzenia → Dodaj HYDROS (Beta)** i wklej klucz.

Po połączeniu Cora importuje historię z ostatnich 33 dni, a potem czyta dalej od tego miejsca. Co możesz odczytać, a z kluczem zapisu też kontrolować, opisuje [Sterowanie sprzętem](/help/mobile-device-control).

## Wpisywanie wyników ręcznie

Część parametrów pochodzi z testów kropelkowych, a nie ze sprzętu. Żeby wpisać wynik, przewiń pulpit na sam dół i dotknij **Zapisz parametry**.

Wyniki wpisane ręcznie mają taką samą wagę jak inne. Pojawiają się na widżetach, mają własne źródło i wiek, trafiają do Reef Buddy. Właśnie z nimi Cora porównuje sondy, gdy informuje, że dwa źródła podają różne wartości.

## Gdy połączenie przestaje działać

Wiersz urządzenia podpowiada, jaki to rodzaj problemu. Sprawdź tabelę w **[Dodawaniu, edytowaniu i usuwaniu urządzeń](/help/mobile-devices)**. Jeśli Twojego problemu tam nie ma, zajrzyj do **[Rozwiązywania problemów](/help/troubleshooting)**.

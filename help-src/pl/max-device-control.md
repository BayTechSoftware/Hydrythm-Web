---
title: Sterowanie sprzętem z Cora Max
description: Strony urządzeń na dużym ekranie: sondy, gniazda, głowice dozujące, testery i pompy.
section: Cora Max
reviewed: 2026-09-30
order: 6
group: Equipment
---

Cora Max steruje tym samym sprzętem co telefon. Każde urządzenie ma własną stronę. Otworzysz ją w **Ustawienia → Urządzenia** albo po dotknięciu kafelka urządzenia na pulpicie.

![Strona Apex na Cora Max](img/max-device-control.webp "Cykle karmienia i wszystkie gniazda, ułożone pod ekran na ścianie.")

:::warning Te przyciski działają na prawdziwym sprzęcie
Nie ma podglądu ani cofania. Polecenie wychodzi w chwili dotknięcia, ale *wysłane* nie znaczy *wykonane*. Wynik to **Potwierdzono**, **Niepotwierdzone**, **Odmówiono** albo **Bez zmian**, a który z nich, sprawdzisz w [Aktywność](/help/max-activity).
:::

## Które urządzenia mają stronę

| Urządzenie | Co pokazuje |
|---|---|
| **Neptune Apex** | Sondy i gniazda. Każde gniazdo można przełączyć |
| **Trident** | Stan testu, poziom reagentów i odpadów. Możesz też uruchomić test |
| **DŌS**, także DŌS QD | Dozowanie każdej głowicy, harmonogram, na ile dni wystarczy zapas, objętość pojemnika (z pauzą, napełnianiem, dawką od ręki i jednorazowym dwudziestosekundowym pomiarem) |
| **Red Sea ReefBeat** | Zależnie od urządzenia: głowice dozujące, zbiornik, dni rolki, tryb pompy, a do tego pełny edytor planu ReefDose, programu ReefRun i ustawień ReefMat *(beta)* |
| **ReefControl**, **ReefControl Power**, **ReefWave**, **ReefLED** *(beta)* | Sondy ReefControl. Gniazda ReefControl Power jako gniazda, włącz albo wyłącz, bez automatycznego trybu. ReefWave i ReefLED tylko do podglądu |
| **Jecod** | Tryb i moc pompy oraz jej program dnia |
| **Maxspect** *(beta)* | Tryb i prędkość dla **Gyre A** i **Gyre B**, **Stan pompy** (odliczanie do czyszczenia, prąd głowicy A, zamontowane głowice, firmware) i harmonogram, tylko do podglądu |
| **GHL ProfiLux / Mitras** *(beta)* | Sondy, gniazda, dozowniki, czujniki poziomu, a w modelach Director także wyniki testów KH i jonów |
| **HYDROS** *(beta)* | To, co zgłasza jego klucz urządzenia: wejścia, a z kluczem zapisu także wyjścia, tryby, głowice dozujące i komendy testera |

Jeśli urządzenie Red Sea samo się zatrzyma, jego strona pokaże, co się stało, a obok przycisk do rozwiązania problemu: **Wznów**, **Usuń stan awaryjny**, **Czujnik wyczyszczony**, **Nowa rolka już załadowana** albo **Resetuj** dla głowicy dozującej.

Plan ReefDose, program prędkości ReefRun oraz zaplanowany posuw, model, pozycja i nowa rolka ReefMat działają tu dokładnie tak samo jak na telefonie. Więcej w [Podłączanie sprzętu](/help/mobile-connections) i [Sterowanie sprzętem](/help/mobile-device-control).

## Głowice DŌS

Zanim Cora zadozuje coś ręcznie daną głowicą, trzeba ją raz zmierzyć. **Zmierz, aby dozować** uruchamia głowicę na dwadzieścia sekund. Płyn leci do naczynia pomiarowego, a Ty wpisujesz, ile go wyszło. Cora przechowuje jeden pomiar na głowicę i używa najnowszego, bez względu na to, który Cora Max go wykonał. Na stronie głowicy widać, gdzie i kiedy ją zmierzono.

Po ręcznej dawce głowica, która w Apex Fusion ma ustawione Off, zostaje na Off. Każda inna głowica wraca do Auto.

### Do czego służy głowica

W ustawieniach głowicy możesz wybrać jej **przeznaczenie**: **Suplement**, **Podmiana wody: nowa słona woda wchodzi**, **Podmiana wody: stara woda wychodzi**, **Kalkwasser**, **Reaktor wapniowy**, **Pokarm**, **Dolewka** albo **Inne**. Od przeznaczenia zależą dwie rzeczy:

- **Wielkość pojemnika, którą głowica może śledzić.** Głowica z przeznaczeniem **Suplement** śledzi pojemnik do 20 litrów. Przy każdym innym przeznaczeniu pojemnik może być dużo większy, do 500 litrów. Głowica do podmiany wody albo reaktora wapniowego nie jest więc traktowana jak mała butelka z suplementem.
- **Czy głowica może podać ręcznie dużą dawkę.** Głowice **Suplement** i **Pokarm** mają taki sam mały, ostrożny limit jak dotąd. Każde inne przeznaczenie może mieć własny limit **Największa dawka ręczna**, maksymalnie 10 litrów, i własny **Dzienny limit dla automatyzacji i Asystenta**. Duża dawka ręczna wymaga też włączenia **Duże dawki (Beta)** w ustawieniach głowicy. Domyślnie jest wyłączone: włącz je dopiero po obejrzeniu pierwszej dużej dawki wykonanej przy akwarium.

Parę głowic do podmiany wody (nowa słona woda wchodzi, stara wychodzi) możesz połączyć jako **Sparowana głowica** i ustawić **Ostrzeżenie o równowadze powyżej**. Jeśli dzienne sumy obu głowic różnią się o więcej niż ta wartość, Cora Cię ostrzeże. Taka różnica zwykle oznacza, że jedna strona nie pompuje tak, jak powinna.

### Gdy duża dawka zostanie przerwana

Na czas dużej dawki Cora zmienia to, co głowica robi na Apex, a potem przywraca jej zwykły harmonogram. Jeśli w trakcie zerwie się połączenie, Cora Max pokaże na stronie tej głowicy baner: *„Duża dawka na [głowica] nie zakończyła się poprawnie. Cora wciąż próbuje przywrócić jej program: sprawdź to w Apex Fusion.”*

Sprawdź głowicę w Apex Fusion, a potem dotknij **Głowicę sprawdzono w Fusion**, żeby zamknąć baner. Zrób to dopiero wtedy, gdy upewnisz się, że działa własny harmonogram głowicy, a nie program dozowania Cory.

Jeśli baner nie znika albo ciągle wraca, zajrzyj do [Rozwiązywanie problemów](/help/troubleshooting).

## GHL ProfiLux i Mitras

:::note Obsługa GHL jest w wersji beta
Obsługę GHL wciąż testujemy i rozwijamy. Część odczytów albo funkcji sterowania może jeszcze nie działać, a to, co tu widzisz, może się zmienić z kolejną aktualizacją.
:::

Podłącz kontroler GHL z **Ustawienia → [Twoje akwarium] → Kontroler GHL (Beta)**. Wpisz jego adres IP w Twojej sieci i dotknij **Wykryj**. Cora najpierw próbuje oficjalnego API kontrolera, potem innych interfejsów, i mówi, który z nich znalazła.

Jeśli nic nie odpowie, a kontroler to ProfiLux mini, Cora oferuje rozwiązanie zastępcze: wpisz jego dane logowania, a Cora odczyta jego sondy, gniazda, dozowniki i czujniki poziomu. Gdy **Zezwól na sterowanie z Cora (Beta)** jest włączone, mini może też przełączać swoje gniazda, tak samo jak każdy inny kontroler GHL. Wszystko inne, na przykład wartości docelowe i pauza na karmienie, wymaga ProfiLux 3, 4 albo Mitras.

Sterowanie pozostaje wyłączone, dopóki nie włączysz **Zezwol na sterowanie z Cora (Beta)** na stronie urządzenia. Domyślnie jest wyłączone. Gdy jest włączone, gniazdo można ustawić na **Zawsze wlaczone**, **Zawsze wylaczone** albo **Powrot do automatycznego**, a wartość docelowa, na przykład temperatura albo pH, pokazuje swój dozwolony zakres i odrzuca wartość spoza niego. Oba rodzaje zmian są zapisywane na samym kontrolerze i tam zostają, nawet jeśli Cora później straci z nim kontakt. Zmiana, która wygląda, jakby dotyczyła grzałki albo pompy powrotnej, prosi o podwójne potwierdzenie.

Jeśli pojemnik dozownika zaczyna się kończyć, Cora ostrzega tak samo jak przy innych materiałach eksploatacyjnych. Domyślnie próg to 20% pojemności, a zmienisz go w regule dozownika w [Centrum alertów](/help/mobile-alerts).

Jeśli kontroler nie przyjmie zmiany, prawdopodobnie jego API GHL jest wyłączone. GHL wyłącza je po każdej aktualizacji firmware; włącz je z powrotem w **System → GHL API** w GHL Control Center albo GHL Connect. Resztę opisuje [Rozwiązywanie problemów](/help/troubleshooting).

## HYDROS

:::note Obsługa HYDROS jest w wersji beta
Obsługę HYDROS wciąż testujemy i rozwijamy. Część odczytów albo funkcji sterowania może jeszcze nie działać, a to, co tu widzisz, może się zmienić z kolejną aktualizacją.
:::

HYDROS to jedyna integracja, która dociera do swojego kontrolera przez chmurę, więc działa nawet wtedy, gdy Cora Max jest w innej sieci niż kontroler. Połącz go z **Ustawienia → [Twoje akwarium] → HYDROS (Beta)**.

W aplikacji HYDROS utwórz klucz urządzenia dla dostawcy **cora-iq**, wybierając **Odczyt** tylko dla odczytów albo **Zapis**, żeby też nim sterować. Wklej klucz, dotknij **Zweryfikuj**, wybierz akwarium, a potem **Zapisz**. Po połączeniu importowana jest historia z ostatnich 33 dni.

Odczyt i sterowanie działają tak samo jak na telefonie; wyjścia, tryby, głowice dozujące i komendy testera, a także limity dawek dla poszczególnych głowic, opisuje [Sterowanie sprzętem](/help/mobile-device-control).

## Harmonogramy

Programy dnia pomp Jecod możesz tworzyć na Cora Max tak samo jak na telefonie. Edytor jest ten sam: wykres dnia, lista okresów i wiersz akcji. Więcej w [Harmonogramy sprzętu](/help/mobile-schedules).

Harmonogram Maxspect Gyre *(beta)* możesz tu obejrzeć, ale nie zapiszesz zmian. Ustawisz go w aplikacji Maxspect.

## Gniazda

Gniazda są też w szufladzie **Gniazda i karmienie** na dole pulpitu. Zebrane są tam gniazda włączone dla tego pulpitu (albo wszystkie, jeśli żadnych nie wybrano). Więcej w [Gniazda i sterowanie](/help/max-controls).

Głowice DŌS nigdy nie pojawiają się na liście gniazd, więc nie da się tam włączyć głowicy i zostawić jej włączonej. Dozuj z jej własnej strony. Duży Apex z kilkoma modułami pokazuje wszystkie swoje gniazda i sondy.

## Materiały eksploatacyjne

Progi uzupełniania (reagent, pojemniki, zbiorniki) ustawiasz na stronie danego urządzenia, tak samo jak na telefonie. Więcej w [Materiały eksploatacyjne](/help/mobile-consumables).

## Zapisywanie wyników i obliczenia przy akwarium

Dwie rzeczy często wygodniej zrobić przy akwarium niż na telefonie:

- **Zapisz parametry** w menu akwarium. Wyniki testów wpisujesz na klawiaturze ekranowej.
- **Kalkulator dawki** na stronie parametru. Obliczysz w nim korektę na podstawie objętości akwarium i stężenia Twoich preparatów. Kalkulator korzysta z tych samych danych co telefon, więc dawka wyliczona tutaj będzie taka sama jak tam. Więcej w [Dozowanie](/help/mobile-dosing).

## Na drugim Cora Max

Gdy jedno akwarium pokazuje kilka ekranów Cora Max, sprzęt tego akwarium odczytuje tylko jeden z nich. Na stronach urządzeń nazywa się go Cora Max przy akwarium. Pozostałe też otwierają strony urządzeń (plakietka stanu **Chmura** oznacza, że ten ekran jest jednym z nich). Pokazują to, co ostatnio odczytał Cora Max przy akwarium, i jak dawno to było. Każde polecenie przekazują przez Cora Cloud do Cora Max przy akwarium, który je wykonuje.

Kilka rzeczy działa tylko na Cora Max przy akwarium:

- **Zmierz, aby dozować** i **Zmierz ponownie** są tylko tam. Gdy głowica jest już zmierzona, **Dawkuj teraz** działa z każdego Cora Max.
- Harmonogram Jecod zmienisz z innego Cora Max tylko wtedy, gdy Cora Max przy akwarium odczytał pompę w ciągu ostatniej godziny. Nie zadziała to nigdy dla pompy, która łączy się tylko przez Bluetooth. Jedno **Zastosuj do pompy** z innego ekranu wysyła najwyżej 12 zmian, więc większą zmianę wysyłaj w częściach.

## Co i przez co zostało zmienione

Każda akcja jest zapisywana razem z jej przyczyną. Więcej w [Aktywność i oś czasu](/help/mobile-activity).

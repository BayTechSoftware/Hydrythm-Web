---
title: Sterowanie sprzętem z Cora Max
description: Strony urządzeń na Cora Max dla Neptune Apex, Trident i DŌS, Red Sea ReefBeat, Jecod, AquaWiz i marek Beta, według marki.
section: Cora Max
reviewed: 2026-10-13
order: 6
group: Equipment
twin: mobile-device-control
---

Ta strona opisuje, co możesz zobaczyć i zrobić na stronie każdego urządzenia na Cora Max, marka po marce. Cora Max łączy się z tym samym sprzętem co telefon. Stronę urządzenia otworzysz ikoną urządzeń na górnym pasku, z **Ustawienia → Urządzenia** albo dotykając kafelka urządzenia na pulpicie.

![Strona Apex na Cora Max z przyciskami karmienia i gniazdami](img/max-device-control.webp "Feed A do D i Anuluj, a pod nimi gniazda, ułożone pod ekran na ścianie.")

:::warning Te przyciski działają na pracujący sprzęt
Nie ma podglądu ani cofania. Polecenie wychodzi w chwili dotknięcia, ale wysłanie nie oznacza wykonania. Wraca jako **Potwierdzono**, **Niepotwierdzone**, **Odmówiono** albo **Bez zmian**, a który wynik, zobaczysz w [Aktywności](/help/max-activity).
:::

Sprzęt dodajesz, przypisujesz i usuwasz w telefonie. Cora Max pokazuje go, gdy Twoje konto go ma. Zobacz [Podłączanie sprzętu](/help/mobile-connections).

## Co ma stronę {#what-has-a-page}

| Urządzenie | Co pokazuje |
|---|---|
| **Neptune Apex** | Sondy i gniazda. Każde gniazdo możesz przełączać |
| **Trident** | Stan testu, poziom odczynników i odpadów oraz przycisk uruchomienia testu |
| **DŌS**, w tym DŌS QD | Dozowanie każdej głowicy, harmonogram, zapas i objętość pojemnika (z pauzą, napełnianiem, dawką od razu i jednorazowym dwudziestosekundowym pomiarem) |
| **Red Sea ReefBeat** | To, co ma urządzenie: głowice dozujące, zbiornik, dni rolki, tryb pompy, a także pełny edytor planu ReefDose i programu ReefRun oraz ustawienia ReefMat *(Beta)* |
| **Red Sea ReefControl**, **ReefControl Power**, **ReefWave**, **ReefLED** *(Beta)* | Sondy ReefControl. Gniazda ReefControl Power jako gniazda, włączone albo wyłączone, na razie bez trybu automatycznego. ReefWave i ReefLED tylko do podglądu |
| **Jecod** | Tryb i intensywność pompy oraz jej program dnia |
| **AquaWiz** | Nie ma własnej strony. Jest na liście w **Urządzenia**, a jego odczyty trafiają na pulpit |
| **Maxspect** *(Beta)* | Tryb i prędkość dla **Gyre A** i **Gyre B**, **Stan pompy** (odliczanie do czyszczenia, prąd głowicy A, zamontowane głowice, oprogramowanie) i jego harmonogram, tylko do podglądu |
| **GHL ProfiLux / Mitras** *(Beta)* | Sondy, gniazda, dozowniki, czujniki poziomu, a w modelach Director także wyniki testów KH i jonów |
| **HYDROS** *(Beta)* | To, co zgłasza jego klucz urządzenia: wejścia, a z kluczem zapisu także wyjścia, tryby, głowice dozujące i polecenia testera |
| **Focustronic** *(Beta)* | Stan, ostatni test, pompy i fiolki oraz **Zmierz teraz**, **Dozuj teraz** albo **Testuj teraz**, zależnie od urządzenia |
| **EcoTech** *(Beta)* | Lampy Radion, pompy VorTech i dozowniki Versa, każde z własną stroną. Polecenia dla VorTech i Versa nie zostały jeszcze sprawdzone na sprzęcie |
| **Inkbird** *(Beta)* | Odczyty powietrza w pomieszczeniu, tylko do odczytu |
| **Kamera** *(Beta)* | Obraz z kamery, jako kafelek na pulpicie albo na własnej stronie, z Czuwaniem skimmera w płatnych planach |

:::note Beta
**Beta.** Maxspect, GHL, HYDROS, Focustronic, EcoTech, Inkbird i kamery są w wersji Beta i są dostępne tylko dla użytkowników Beta. Jeśli nie jesteś użytkownikiem Beta, nie zobaczysz ich w **Dodaj urządzenie**. Aby poprosić o dostęp do Beta, skontaktuj się z [pomocą techniczną](/support.html). Część odczytów albo funkcji sterowania może jeszcze nie działać.
:::

Większość stron urządzeń ma ołówek do zmiany nazwy urządzenia. Nowa nazwa pojawia się też w telefonie. Więcej w [Urządzeniach i ich stanie](/help/max-devices).

## Neptune Apex {#neptune-apex}

Strona Apex wymienia sondy i gniazda, z cyklami karmienia na górze. Każde gniazdo przełączasz między **AUTO**, **WYŁ.** i **WŁ.**, a gniazda z kłódką proszą o potwierdzenie. Jak działają trzy stany i tryb karmienia, opisują [Gniazda i sterowanie](/help/max-controls).

Do gniazd dotrzesz też z szuflady **Gniazda i karmienie** na dole pulpitu. Wymienia gniazda włączone dla tego pulpitu (albo wszystkie, jeśli żadnych nie wybrano).

Duży Apex z kilkoma modułami pokazuje wszystkie swoje gniazda i sondy. Głowice DŌS nigdy nie pojawiają się na liście gniazd, więc nie włączysz tam żadnej i nie zostawisz jej pracującej. Dozuj ze strony samej głowicy.

### Trident {#trident}

Strona Trident pokazuje stan testu oraz poziom odczynników i odpadów. Możesz stąd uruchomić test i ustawić alert uzupełnienia przyciskiem **Ustawienia alertów**.

## Głowice DŌS {#dos-heads}

Głowicę DŌS trzeba raz zmierzyć, zanim Cora zacznie nią dozować ręcznie. **Zmierz, aby dozować** uruchamia głowicę na dwadzieścia sekund do naczynia pomiarowego, a Ty wpisujesz, ile wypłynęło. Cora przechowuje jeden pomiar na głowicę i używa najnowszego, niezależnie od tego, który Cora Max go wykonał. Strona głowicy pokazuje, gdzie i kiedy ją zmierzono.

Po ręcznej dawce głowica ustawiona w Apex Fusion na Off zostaje na Off. Każda inna wraca do Auto.

DŌS nie ma czujnika poziomu i dozuje dalej z pustego pojemnika. Ustaw alert uzupełnienia przyciskiem **Ustawienia alertów** na stronie DŌS. Więcej w [Alertach dozownika](/help/mobile-device-control#doser-alerts).

### Do czego służy głowica {#what-a-head-is-used-for}

W arkuszu ustawień głowicy możesz ustawić, do czego jest **Używana do**. Możliwości to **Suplement**, **Podmiana wody: nowa słona woda wchodzi**, **Podmiana wody: stara woda wychodzi**, **Kalkwasser**, **Reaktor wapniowy**, **Pokarm** albo **Dolewka** oraz **Inne**. Przeznaczenie zmienia dwie rzeczy.

- Jak duży pojemnik głowica może śledzić. Przy każdym przeznaczeniu głowica może śledzić pojemnik do 1000 litrów. Powyżej własnego licznika Apex, który liczy do 150 litrów, Cora sama śledzi objętość i co 100 litrów zeruje licznik Apex.
- Czy głowica może podać ręcznie dużą dawkę. Głowice Suplement i Pokarm zachowują dotychczasowy mały, ostrożny limit. Każde inne przeznaczenie może mieć własny limit **Największa dawka ręczna**, do twardej granicy 10 litrów, i własny **Dzienny limit dla automatyzacji i Asystenta**. Duża dawka ręczna wymaga też włączenia **Duże dawki (Beta)** w ustawieniach głowicy, domyślnie wyłączonego. Włącz je dopiero wtedy, gdy obejrzysz przy akwarium pierwszą dużą dawkę.

Parę głowic do podmiany wody (nowa słona woda wchodzi, stara wychodzi) możesz połączyć jako **Sparowana głowica** i ustawić wartość **Ostrzeżenie o równowadze powyżej**. Jeśli dzienne sumy obu głowic rozjadą się bardziej niż o tę wartość, Cora Cię ostrzeże. Para bez równowagi zwykle oznacza, że jedna strona nie pompuje tak, jak powinna.

### Gdy duża dawka zostanie przerwana {#if-a-large-dose-is-interrupted}

Duża dawka na jakiś czas zmienia to, co głowica robi na Apex, a potem przywraca jej zwykły harmonogram. Jeśli w trakcie połączenie się zerwie, Cora Max pokaże na stronie tej głowicy baner: *„Duża dawka na [głowica] nie zakończyła się poprawnie. Cora wciąż próbuje przywrócić jej program: sprawdź to w Apex Fusion.”*

Samodzielnie sprawdź głowicę w Apex Fusion, a potem dotknij **Głowicę sprawdzono w Fusion**, żeby usunąć baner. Zrób to dopiero wtedy, gdy potwierdzisz, że działa własny harmonogram głowicy, a nie program dozowania Cory.

Jeśli baner nie znika albo ciągle wraca, zajrzyj do [Rozwiązywania problemów](/help/troubleshooting).

## Red Sea ReefBeat {#red-sea}

Każde urządzenie Red Sea ma stronę dopasowaną do tego, co robi: głowice i pojemniki ReefDose, zbiornik ReefATO+, dni rolki ReefMat i prędkości pomp ReefRun. Alerty zasobów dla głowic ReefDose, zbiornika ReefATO+ i rolki ReefMat ustawiasz przyciskiem **Ustawienia alertów** na stronie urządzenia.

Jeśli urządzenie Red Sea samo się zatrzyma, jego strona mówi, co jest nie tak, i daje rozwiązanie tuż obok. To **Wznów**, **Usuń stan awaryjny**, **Czujnik wyczyszczony**, **Nowa rolka już załadowana** albo **Resetuj** dla głowicy dozującej.

Plan ReefDose, program prędkości ReefRun oraz zaplanowany posuw, model, pozycja i nowa rolka ReefMat działają tu tak samo jak w telefonie. Szczegóły są w [Sterowaniu sprzętem](/help/mobile-device-control).

ReefControl, ReefControl Power, ReefWave i ReefLED mają w nazwie *(Beta)*, ale są dostępne dla wszystkich. ReefControl pokazuje swoje sondy. Gniazda ReefControl Power pojawiają się jako gniazda, tylko włączone albo wyłączone. ReefWave i ReefLED są na razie tylko do podglądu.

## Jecod {#jecod}

Strona Jecod pokazuje tryb i intensywność pompy, a Ty możesz zmienić oba.

Programy dnia pomp Jecod możesz pisać przy ścianie tak samo jak w telefonie. Edytor jest taki sam, z wykresem dnia, listą okresów i rzędem akcji. Więcej w [Harmonogramach sprzętu](/help/mobile-schedules).

## AquaWiz {#aquawiz}

AquaWiz KH Controller nie ma na Cora Max własnej strony. Jest na liście w **Urządzenia**, gdzie możesz zmienić jego nazwę, a jego odczyty pokazują się na pulpicie jak każde inne źródło. Konfigurujesz go i zarządzasz nim w telefonie, zobacz [Podłączanie sprzętu](/help/mobile-connections).

## Maxspect {#maxspect}

:::note Beta
**Beta.** Maxspect jest w wersji Beta i jest dostępny tylko dla użytkowników Beta. Jeśli nie jesteś użytkownikiem Beta, nie zobaczysz go w **Dodaj urządzenie**. Aby poprosić o dostęp do Beta, skontaktuj się z [pomocą techniczną](/support.html). Część odczytów albo funkcji sterowania może jeszcze nie działać.
:::

Strona Maxspect pokazuje tryb i prędkość **Gyre A** i **Gyre B** oraz **Stan pompy**. Możesz tu podejrzeć harmonogram Gyre, ale nie możesz go zapisać. Ustaw go w aplikacji Maxspect.

## GHL ProfiLux i Mitras {#ghl}

:::note Beta
**Beta.** GHL jest w wersji Beta i jest dostępny tylko dla użytkowników Beta. Jeśli nie jesteś użytkownikiem Beta, nie zobaczysz go w **Dodaj urządzenie**. Aby poprosić o dostęp do Beta, skontaktuj się z [pomocą techniczną](/support.html). Część odczytów albo funkcji sterowania może jeszcze nie działać.
:::

Podłącz kontroler GHL z telefonu: **Urządzenia → Dodaj urządzenie → GHL**. Kroki opisuje [Podłączanie sprzętu](/help/mobile-connections). Cora Max pokazuje go i nim steruje, gdy odczyta go Cora Max w jego sieci, ale sama konfiguracja odbywa się w telefonie.

ProfiLux mini odczytuje swoje sondy, gniazda, dozowniki i czujniki poziomu. Gdy **Zezwól na sterowanie z Cora (Beta)** jest włączone, mini może też przełączać swoje gniazda, tak samo jak każdy inny kontroler GHL. Wszystko inne, na przykład wartości zadane i przerwa na karmienie, wymaga ProfiLux 3, 4 albo Mitras.

Sterowanie jest wyłączone, dopóki nie włączysz **Zezwól na sterowanie z Cora (Beta)** na stronie urządzenia. Domyślnie jest wyłączone. Po włączeniu gniazdo można ustawić na **Zawsze włączone**, **Zawsze wyłączone** albo **Powrót do automatycznego**, a wartość zadana, na przykład temperatura albo pH, pokazuje dozwolony zakres i odrzuca wartość spoza niego. Oba rodzaje zmian są zapisywane w samym kontrolerze i zostają tam, nawet jeśli Cora później straci z nim kontakt. Zmiana, która wygląda na dotyczącą grzałki albo pompy powrotnej, prosi o potwierdzenie dwa razy.

Jeśli w pojemniku dozownika kończy się płyn, Cora ostrzega Cię tak samo jak przy innych materiałach eksploatacyjnych. Domyślnie przy 20% napełnienia, a zmienisz to w regule dozownika w [Centrum alertów](/help/mobile-alerts).

Jeśli kontroler nie przyjmuje zmiany, prawdopodobnie jego API GHL jest wyłączone. GHL wyłącza je po każdej aktualizacji oprogramowania. Włącz je ponownie w **System → GHL API** w GHL Control Center albo GHL Connect. Resztę opisuje [Rozwiązywanie problemów](/help/troubleshooting).

## HYDROS {#hydros}

:::note Beta
**Beta.** HYDROS jest w wersji Beta i jest dostępny tylko dla użytkowników Beta. Jeśli nie jesteś użytkownikiem Beta, nie zobaczysz go w **Dodaj urządzenie**. Aby poprosić o dostęp do Beta, skontaktuj się z [pomocą techniczną](/support.html). Część odczytów albo funkcji sterowania może jeszcze nie działać.
:::

HYDROS łączy się ze swoim kontrolerem przez chmurę HYDROS, więc działa nawet wtedy, gdy Cora Max jest w innej sieci niż kontroler. Konfiguruje się go tylko w telefonie: **Urządzenia → Dodaj urządzenie → HYDROS**. Kroki opisuje [Podłączanie sprzętu](/help/mobile-connections).

Odczyt i sterowanie działają tak samo jak w telefonie. Wyjścia, tryby, głowice dozujące, polecenia testera i limity dawek dla poszczególnych głowic opisuje [Sterowanie sprzętem](/help/mobile-device-control).

## Focustronic {#focustronic}

:::note Beta
**Beta.** Focustronic jest w wersji Beta i jest dostępny tylko dla użytkowników Beta. Jeśli nie jesteś użytkownikiem Beta, nie zobaczysz go w **Dodaj urządzenie**. Aby poprosić o dostęp do Beta, skontaktuj się z [pomocą techniczną](/support.html). Część odczytów albo funkcji sterowania może jeszcze nie działać.
:::

Strona Focustronic pokazuje stan urządzenia, jego ostatni test oraz pompy i fiolki. W **Sterowanie**:

- Alkatronic ma **Zmierz teraz**.
- Dosetronic ma **Dozuj teraz** dla każdej pompy. Wpisz ilość, do 500 mL naraz, dotknij **Sprawdź**, a potem potwierdź. Dawki nie da się cofnąć, a Cora nigdy jej nie ponawia.
- Mastertronic ma profil testu do wyboru i **Testuj teraz**.

Te polecenia idą przez serwery Focustronic, nad którymi Cora nie ma kontroli. Urządzenie konfigurujesz w telefonie, zobacz [Podłączanie sprzętu](/help/mobile-connections).

## EcoTech, Inkbird i kamery {#ecotech-inkbird-and-cameras}

:::note Beta
**Beta.** EcoTech, Inkbird i kamery są w wersji Beta i są dostępne tylko dla użytkowników Beta. Jeśli nie jesteś użytkownikiem Beta, nie zobaczysz ich w **Dodaj urządzenie**. Aby poprosić o dostęp do Beta, skontaktuj się z [pomocą techniczną](/support.html).
:::

Łączysz je z telefonu, a odczytuje je Cora Max przy akwarium.

### EcoTech {#ecotech}

Lampy Radion, pompy VorTech i dozowniki Versa mają własne strony z przyciskiem **Ustawienia alertów** dla ich zasobów. Szczegóły są w [Lampach, pompach i dozownikach EcoTech](/help/mobile-ecotech).

### Inkbird {#inkbird}

Monitor powietrza w pomieszczeniu Inkbird pokazuje swoje odczyty i nic więcej.

### Kamery i Czuwanie skimmera {#cameras}

Żeby pokazać kamerę na ścianie, dodaj kafelek **Kamera** w [edytorze pulpitu](/help/max-dashboard-editing). Dotknij kafelka, żeby otworzyć kamerę na pełnym ekranie. Jej przyciski znikają po kilku sekundach, a dotknięcie je przywraca.

Gdy Czuwanie skimmera jest włączone (płatne plany), kafelek kamery i widok na pełnym ekranie pokazują poziom w kubku i wiek odczytu, na przykład *Kubek 42% · 5 min temu*. Robi się bursztynowy w granicach 10 punktów od Twojego poziomu alertu i czerwony, gdy go osiągnie. Na kamerze na pełnym ekranie **Alarm przy 80%** (albo Twój poziom) otwiera **Alarm kubka odpieniacza**, gdzie ustawiasz poziom. Gdy kubek go osiągnie, dostaniesz jedno powiadomienie.

Konfigurację kamery i Czuwania skimmera opisują [Kamery i Czuwanie skimmera](/help/mobile-cameras).

## Materiały eksploatacyjne {#consumables}

Progi uzupełnienia (odczynnik, pojemniki, zbiorniki) ustawiasz tu na stronie samego urządzenia, tak samo jak w telefonie. Więcej w [Materiałach eksploatacyjnych](/help/mobile-consumables).

## Zapisywanie i liczenie przy akwarium {#logging-and-calculating-at-the-tank}

Dwie rzeczy często łatwiej zrobić przy ścianie niż w telefonie.

- **Zapisz parametry** pozwala wpisać wyniki testów na klawiaturze ekranowej. Jest w menu akwarium.
- **Kalkulator dawki** liczy korektę na podstawie objętości akwarium i stężeń Twoich produktów. Otwórz go ze strony parametru. Używa tej samej objętości i tych samych stężeń co telefon, więc dawka policzona tutaj zgadza się z policzoną tam. Więcej w [Dozowaniu](/help/mobile-dosing).

## Na drugim Cora Max {#on-a-second-cora-max}

Gdy akwarium pokazuje więcej niż jeden Cora Max, jeden z nich odczytuje sprzęt tego akwarium. Strony urządzeń nazywają go Cora Max przy akwarium. Pozostałe też mogą otwierać strony urządzeń, a etykieta stanu **Chmura** oznacza, że jesteś na jednym z nich. Pokazują to, co Cora Max przy akwarium ostatnio odczytał, i jak dawno. Każde polecenie idzie przez Cora Cloud do Cora Max przy akwarium, który je wykonuje.

Kilka rzeczy działa tylko na Cora Max przy akwarium.

- **Zmierz, aby dozować** i **Zmierz ponownie** pojawiają się tylko tam. Gdy głowica jest już zmierzona, **Dawkuj teraz** działa z każdego Cora Max.
- Harmonogram Jecod zmienisz z innego Cora Max tylko wtedy, gdy Cora Max przy akwarium odczytał pompę w ciągu ostatniej godziny, i nigdy dla pompy, która łączy się tylko przez Bluetooth. Jedno **Zastosuj do pompy** z innego Cora Max wysyła najwyżej 12 zmian, więc większą edycję wyślij w częściach.

## Co zostało zmienione i przez co {#what-was-changed-and-by-what}

Każda akcja jest zapisywana razem z tym, co ją spowodowało. Więcej w [Aktywności na Cora Max](/help/max-activity).

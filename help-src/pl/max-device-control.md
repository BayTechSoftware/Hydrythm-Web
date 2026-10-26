---
title: Sterowanie sprzętem z Cora Max
description: Strony urządzeń na Cora Max dla Neptune Apex, Trident i DŌS, Red Sea ReefBeat, Jecod i AquaWiz, według marki.
section: Cora Max
reviewed: 2026-10-24
order: 6
group: Equipment
twin: mobile-device-control
---

Ta strona opisuje, co możesz zobaczyć i zrobić na stronie każdego urządzenia na Cora Max, marka po marce. Cora Max łączy się z tym samym sprzętem co telefon. Stronę urządzenia otworzysz ikoną urządzeń na górnym pasku, z **Ustawienia → Urządzenia** albo dotykając kafelka urządzenia na panelu.

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
| **Red Sea ReefBeat** | To, co ma urządzenie: głowice dozujące, zbiornik, dni rolki, tryb pompy |
| **Jecod** | Tryb i intensywność pompy oraz jej harmonogram |
| **AquaWiz** | Nie ma własnej strony. Jest na liście w **Urządzenia**, a jego odczyty trafiają na panel |

Większość stron urządzeń ma ołówek do zmiany nazwy urządzenia. Nowa nazwa pojawia się też w telefonie. Więcej w [Urządzeniach i ich stanie](/help/max-devices).

## Neptune Apex {#neptune-apex}

Strona Apex wymienia sondy i gniazda, z cyklami karmienia na górze. Każde gniazdo przełączasz między **AUTO**, **WYŁ.** i **WŁ.**, a gniazda z kłódką proszą o potwierdzenie. Jak działają trzy stany i tryb karmienia, opisują [Gniazda i sterowanie](/help/max-controls).

Do gniazd dotrzesz też z szuflady **Gniazda i karmienie** na dole panelu. Wymienia gniazda włączone dla tego panelu (albo wszystkie, jeśli żadnych nie wybrano).

Duży Apex z kilkoma modułami pokazuje wszystkie swoje gniazda i sondy. Głowice DŌS nigdy nie pojawiają się na liście gniazd, więc nie włączysz tam żadnej i nie zostawisz jej pracującej. Dozuj ze strony samej głowicy.

### Trident {#trident}

Strona Trident pokazuje stan testu oraz poziom odczynników i odpadów. Możesz stąd uruchomić test i ustawić alert uzupełnienia przyciskiem **Ustawienia alertów**.

## Głowice DŌS {#dos-heads}

Głowicę DŌS trzeba raz zmierzyć, zanim Cora zacznie nią dozować ręcznie. **Zmierz, aby dozować** uruchamia głowicę na dwadzieścia sekund do naczynia pomiarowego, a Ty wpisujesz, ile wypłynęło. Cora przechowuje jeden pomiar na głowicę i używa najnowszego, niezależnie od tego, który Cora Max go wykonał. Strona głowicy pokazuje, gdzie i kiedy ją zmierzono.

Po ręcznej dawce głowica ustawiona w Apex Fusion na Off zostaje na Off. Każda inna wraca do Auto.

DŌS nie ma czujnika poziomu i dozuje dalej z pustego pojemnika. Ustaw alert uzupełnienia przyciskiem **Ustawienia alertów** na stronie DŌS. Więcej w [Alertach dozownika](/help/mobile-device-control#doser-alerts).

### Do czego służy głowica {#what-a-head-is-used-for}

W arkuszu ustawień głowicy możesz ustawić jej przeznaczenie w polu **Używana do**. Możliwości to **Suplement**, **Podmiana wody: nowa słona woda wchodzi**, **Podmiana wody: stara woda wychodzi**, **Kalkwasser**, **Reaktor wapniowy**, **Pokarm** albo **Dolewka** oraz **Inne**. Przeznaczenie zmienia dwie rzeczy.

- Jak duży pojemnik głowica może śledzić. Przy każdym przeznaczeniu głowica może śledzić pojemnik do 1000 litrów. Powyżej własnego licznika Apex, który liczy do 150 litrów, Cora sama śledzi objętość i co 100 litrów zeruje licznik Apex.
- Czy głowica może podać ręcznie dużą dawkę. Głowice Suplement i Pokarm zachowują dotychczasowy mały, ostrożny limit. Każde inne przeznaczenie może mieć własny limit **Największa dawka ręczna**, do twardej granicy 10 litrów, i własny **Dzienny limit dla automatyzacji i Asystenta**.

Parę głowic do podmiany wody (nowa słona woda wchodzi, stara wychodzi) możesz połączyć jako **Sparowana głowica** i ustawić wartość **Ostrzeżenie o równowadze powyżej**. Jeśli dzienne sumy obu głowic rozjadą się bardziej niż o tę wartość, Cora Cię ostrzeże. Para bez równowagi zwykle oznacza, że jedna strona nie pompuje tak, jak powinna.


## Red Sea ReefBeat {#red-sea}

Każde urządzenie Red Sea ma stronę dopasowaną do tego, co robi: głowice i pojemniki ReefDose, zbiornik ReefATO+, dni rolki ReefMat i prędkości pomp ReefRun. Alerty zasobów dla głowic ReefDose, zbiornika ReefATO+ i rolki ReefMat ustawiasz przyciskiem **Ustawienia alertów** na stronie urządzenia.

Jeśli urządzenie Red Sea samo się zatrzyma, jego strona mówi, co jest nie tak, i daje rozwiązanie tuż obok. To **Wznów**, **Usuń stan awaryjny**, **Czujnik wyczyszczony**, **Nowa rolka już załadowana** albo **Resetuj** dla głowicy dozującej.



## Jecod {#jecod}

Strona Jecod pokazuje tryb i intensywność pompy, a Ty możesz zmienić oba. Jej stan jest w wierszu tytułu, obok nazwy pompy. Górny pasek ma przełącznik, wzór działający teraz i **Karmienie** z czterema przyciskami: **5**, **10**, **15** i **30** min. Dotknij przycisku, aby wstrzymać pompę na ten czas. Pod paskiem są dwie karty:

- **Cały dzień tak samo**: dotknij ustawienia, aby działało cały dzień.
- **Harmonogram**: wykres doby i lista planów, z **teraz** przy bieżącym. **Edytuj** otwiera edytor, a menu ⋮ zawiera **Skopiuj harmonogram do…**, **Zapisz harmonogram jako…** i **Zapisane harmonogramy…**.

Działająca karta ma obwódkę i znacznik **Działa**. Pompa Jecod nie ma przycisku **Zakończ karmienie**. Każda pompa Jecod, która może się wstrzymać na czas karmienia, pokazuje przyciski **5**, **10**, **15** i **30** min. W Jecod Pro robi to samo kafelek Karmienie we wzorach fal, na 10 minut. Przez Cora Max oddalony od akwarium pompa Jecod karmi tylko przez 10 minut. Pompa, która teraz nie może karmić, pokazuje powód w jednym krótkim wierszu pod przyciskami, a długie dotknięcie pokazuje całe zdanie. Karmienie rozpoczęte z telefonu kończy też Cora Max: po upływie czasu pompa wraca do swojego programu.

Programy dnia pomp Jecod możesz pisać przy ścianie tak samo jak w telefonie. Edytor jest taki sam, z wykresem dnia, listą okresów i rzędem akcji. Więcej w [Harmonogramach sprzętu](/help/mobile-schedules).

## AquaWiz {#aquawiz}

AquaWiz KH Controller nie ma na Cora Max własnej strony. Jest na liście w **Urządzenia**, gdzie możesz zmienić jego nazwę, a jego odczyty pokazują się na panelu jak każde inne źródło. Konfigurujesz go i zarządzasz nim w telefonie, zobacz [Podłączanie sprzętu](/help/mobile-connections).

### Godzinowy odczyt z Cora Max {#aquawiz-hourly}

AquaWiz pozwala Corze czytać swoją chmurę tylko co 12 godzin. Żeby alkaliczność była aktualna, główny Cora Max akwarium czyta też kontroler bezpośrednio, raz na godzinę, dziesięć minut przed pełną godziną:

- Na kilka sekund łączy się z własnym Wi-Fi kontrolera, czyta ostatni wynik i od razu wraca do Twojego domowego Wi-Fi. W tym czasie Cora Max jest offline przez około 4 sekundy.
- Hasło do Twojego domowego Wi-Fi nigdy nie jest przy tym zapisywane ani nigdzie wysyłane.
- Robi to tylko główny Cora Max akwarium. Drugi Cora Max przy tym samym akwarium nie.
- Czeka, gdy Cora Max jest zajęty (rozmawia z Tobą, aktualizuje się, paruje albo zmienia Wi-Fi), i próbuje ponownie co minutę lub dwie do końca tej godziny. Potem czeka na następną godzinę.
- Kontroler musi być w zasięgu Wi-Fi Cora Max, a jego oprogramowanie musi umożliwiać dostęp lokalny. Jeśli dwa odczyty z rzędu się nie uda, Cora Max przestaje próbować do końca dnia, a odczyt z chmury co 12 godzin działa dalej.

Odczyt z Cora Max pokazuje **Co godzinę z Twojego Cora Max** na karcie AquaWiz w telefonie. Przynosi też alerty poziomu w pojemniku z wodą opisane w [Alerty](/help/mobile-alerts#equipment-faults). Alerty pompy i sondy pH nie wymagają Cora Max.


## Gdy Bluetooth przestaje działać {#bluetooth-stopped}

Cora Max odczytuje oświetlenie, pompy i czujniki przez Bluetooth. Jeśli jego Bluetooth przestanie działać i przywraca go tylko ponowne uruchomienie, na ekranie pojawia się karta: **Bluetooth przestał działać**, z przyciskami **Uruchom ponownie** i **Później**. Kroki są w [Cora Max pokazuje „Bluetooth przestał działać”](/help/troubleshooting#bluetooth-stopped-working).

## Materiały eksploatacyjne {#consumables}

Progi uzupełnienia (odczynnik, pojemniki, zbiorniki) ustawiasz tu na stronie samego urządzenia, tak samo jak w telefonie. Więcej w [Materiałach eksploatacyjnych](/help/mobile-consumables).

## Zapisywanie i liczenie przy akwarium {#logging-and-calculating-at-the-tank}

Dwie rzeczy często łatwiej zrobić przy ścianie niż w telefonie.

- **Zapisz parametry** pozwala wpisać wyniki testów na klawiaturze ekranowej. Jest w menu akwarium.
- **Kalkulator dawki** liczy korektę na podstawie objętości akwarium i stężeń Twoich produktów. Otwórz go ze strony parametru. Używa tej samej objętości i tych samych stężeń co telefon, więc dawka policzona tutaj zgadza się z policzoną tam. Więcej w [Dozowaniu](/help/mobile-dosing).

## Na drugim Cora Max {#on-a-second-cora-max}

Gdy akwarium pokazuje więcej niż jeden Cora Max, jeden z nich odczytuje sprzęt tego akwarium. Strony urządzeń nazywają go Cora Max przy akwarium. Pozostałe też mogą otwierać strony urządzeń, a etykieta stanu **Chmura** oznacza, że jesteś na jednym z nich. Pokazują to, co Cora Max przy akwarium ostatnio odczytał, i jak dawno. Każde polecenie idzie przez Cora Cloud do Cora Max przy akwarium, który je wykonuje.

Kilka rzeczy działa tylko na Cora Max przy akwarium.

- **Zmierz, aby dozować** i **Zmierz ponownie** pojawiają się tylko tam. Gdy głowica jest już zmierzona, **Dozuj teraz** działa z każdego Cora Max.
- Harmonogram Jecod zmienisz z innego Cora Max tylko wtedy, gdy Cora Max przy akwarium odczytał pompę w ciągu ostatniej godziny, i nigdy dla pompy, która łączy się tylko przez Bluetooth. Jedno **Zastosuj do pompy** z innego Cora Max wysyła najwyżej 12 zmian, więc większą edycję wyślij w częściach.

## Co zostało zmienione i przez co {#what-was-changed-and-by-what}

Każda akcja jest zapisywana razem z tym, co ją spowodowało. Więcej w [Aktywności na Cora Max](/help/max-activity).

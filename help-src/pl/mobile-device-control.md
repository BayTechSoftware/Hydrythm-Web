---
title: Sterowanie sprzętem
description: Otwórz stronę urządzenia, żeby zobaczyć jego stan na żywo i przełączać gniazda, pompy, głowice dozujące i testery, marka po marce.
section: Cora Mobile
reviewed: 2026-10-13
order: 13
group: Equipment
twin: max-device-control
---

Na własnej stronie urządzenia zobaczysz jego stan na żywo i zmienisz to, co robi. Otworzysz ją z **Urządzenia** → dotknij urządzenia albo dotknij jego kafelka na pulpicie.

![Strona ReefATO+ w Cora Mobile](img/mobile-device-detail.webp "Stan, dzisiejsze odczyty i poziom wody, a pod nimi wyciek, dolewki i kalibracja sondy.")

Każda strona urządzenia jest ułożona tak samo. Na górze są nazwa i szczegóły, potem rząd odczytów na żywo, stan, który zgłasza urządzenie, i jego elementy sterowania. Dzwonek na pasku tytułu ustawia progi alertów dla tego urządzenia, tak jak opisują [Materiały eksploatacyjne](/help/mobile-consumables). Jak w ogóle dodać urządzenie, opisuje [Podłączanie sprzętu](/help/mobile-connections).

Przejdź do swojego sprzętu: [Neptune Apex](#neptune-apex) · [Trident](#trident) · [DŌS](#dos) · [Red Sea](#red-sea) · [ReefDose](#reefdose) · [ReefRun](#reefrun) · [ReefMat](#reefmat) · [ReefATO+](#reefato) · [Alerty dozownika](#doser-alerts) · [Jecod](#jecod) · [AquaWiz](#aquawiz) · [Maxspect](#maxspect) · [GHL](#ghl) · [HYDROS](#hydros) · [Focustronic](#focustronic) · [EcoTech, Inkbird i kamery](#ecotech-inkbird-cameras)

:::warning Te przyciski działają na pracujący sprzęt
Nie ma podglądu ani cofania. Niektóre elementy sterowania najpierw proszą o potwierdzenie.
:::

## Co się dzieje, gdy wysyłasz polecenie {#what-happens-when-you-send-a-command}

Polecenie nie zawsze przechodzi. Cora mówi, która z czterech rzeczy się stała:

| Wynik | Znaczenie |
|---|---|
| **Potwierdzono** | Sprzęt przyjął zmianę i zgłosił nowy stan |
| **Niepotwierdzone** | Polecenie wyszło, ale nic nie odpowiedziało. **Oznacza to „nie wiemy”. Nie oznacza, że zadziałało.** Sprawdź stan samego urządzenia |
| **Odmówiono** | Coś je odrzuciło (reguła bezpieczeństwa, blokada albo sam sprzęt) albo żadne urządzenie Cora nie przejęło go na czas. Zostało anulowane i nic się nie wykonało |
| **Bez zmian** | Sprzęt był już ustawiony tak, jak prosisz |

Każdy wynik jest zapisywany w [Aktywności](/help/mobile-activity), razem z tym, co go spowodowało.

Bez Cora Max przy akwarium sprzęt Neptune Apex, Red Sea i Jecod działa tylko lokalnie: żeby wysłać polecenie, telefon musi być w tej samej sieci (albo w zasięgu Bluetooth). Z Cora Max przy akwarium Cora Mobile wysyła polecenie przez ten Cora Max, nawet gdy jesteś poza domem.

## Neptune Apex {#neptune-apex}

![Strona Apex w Cora Mobile z jego stanem, modułami Trident i DŌS, Mapowaniem parametrów i akwarium, które obsługuje](img/mobile-apex.webp "Strona Apex: Stan, Moduły, Mapowanie parametrów i Akwaria.")

Strona Apex pokazuje stan kontrolera, a potem **Moduły**, **Mapowanie parametrów** i **Akwaria**.

- **Moduły** wymieniają każdy zamontowany Trident i DŌS. Dotknij jednego, żeby otworzyć jego stronę.
- W **Mapowaniu parametrów** wybierasz, co dostarcza każda sonda. Sondy zgłaszają się do Cory jako źródła, które możesz umieścić na pulpicie. Zobacz [Mapowanie parametrów i sondy](/help/mobile-probes).
- **Akwaria** pokazują, które akwaria obsługuje Apex. Dotknij **Zmień**, żeby je edytować.
- **Gniazda** przełączasz między **AUTO**, **WYŁ.** i **WŁ.** widżetem **Gniazdo** na pulpicie. AUTO oddaje sterowanie programowi Apex. Zobacz [Rodzaje widżetów](/help/mobile-widgets#outlet).

Twój Apex dalej realizuje własny program. Cora zmienia gniazdo tylko wtedy, gdy o to poprosisz.

## Trident {#trident}

Strona Trident pokazuje bieżący stan testu oraz poziom odczynników i wody odpadowej. Możesz stąd uruchomić test.

Możesz też ustawić alert dla pozostałych testów i dla butelki odpadów, żeby Cora ostrzegła Cię, zanim skończy się odczynnik albo butelka się zapełni. Zobacz [Materiały eksploatacyjne](/help/mobile-consumables).

## DŌS {#dos}

![Strona DŌS z informacją, że DŌS nie odpowiada na AquaBus, z ostatnim zapasem, dzisiejszą dawką i planem dziennym, a pod nimi wiersz Alerty](img/mobile-dos.webp "DŌS poza AquaBus: strona pokazuje ostatnie znane wartości, kartę Wymaga uwagi i wiersz Alerty.")

DŌS QD działa dokładnie tak jak DŌS i wszystko tutaj dotyczy obu. Gdy Cora Max odczytuje Twój Apex, głowice dozujące pojawiają się na stronie DŌS. Nigdy nie pojawiają się na liście gniazd.

Każda głowica dozująca pokazuje, co dozuje, swój harmonogram, ile dozowała dziś i ile zostało w pojemniku. Pokazuje też **Zasięg**, czyli na ile dni to wystarczy przy obecnym tempie.

Jeśli DŌS przestanie odpowiadać na AquaBus, jego strona pokazuje **Poza magistralą** i kartę **Wymaga uwagi**. Wartości na stronie to wtedy ostatnie zgłoszone, a nie to, co dzieje się teraz. Sprawdź kabel AquaBus modułu i Apex.

Dla każdej głowicy możesz:

- **Wstrzymaj** i **Wznów** jej harmonogram
- **Napełnij**, żeby powiedzieć Corze, że pojemnik znów jest pełny, albo ustawić, ile w nim jest (**Całkowita objętość** to rozmiar pojemnika, **Pozostała objętość** to to, co jest w nim teraz, a **Pełny** ustawia jedno na drugie)
- **Dawkuj teraz**, żeby podać ręcznie odmierzoną dawkę

:::note Harmonogramy edytuj w Apex Fusion
Cora pokazuje harmonogram i śledzi, co zostało zdozowane, ale nie zmienia harmonogramu. Harmonogram, tempo dozowania i liczbę dawek edytujesz w aplikacji Apex Fusion. Wstrzymywanie, napełnianie i dozowanie ręczne działają tutaj.
:::

:::note Zmierz głowicę, zanim zaczniesz dozować ręcznie
Cora nie zadozuje ręcznie z głowicy, dopóki nie zostanie zmierzona. **Zmierz, aby dozować** i **Zmierz ponownie** są na Cora Max, który dozuje dla tego akwarium. Cora uruchamia głowicę na dwadzieścia sekund, Ty mierzysz, ile wypłynęło, a Cora wylicza prawdziwe tempo głowicy. Jeden pomiar działa dla każdego Cora Max i Cora Mobile. Zmierz każdą głowicę raz i ponownie po wymianie wężyka.
:::

:::warning DŌS dozuje dalej, gdy pojemnik jest pusty
Urządzenie nie ma czujnika poziomu i samo się nie zatrzyma. Ustaw alert uzupełnienia dla każdej głowicy w **Alerty** na stronie DŌS, żeby Cora ostrzegła Cię, zanim pojemnik wyschnie. Zobacz [Alerty dozownika](#doser-alerts).
:::

### Do czego służy każda głowica {#dos-head-use}

Nadaj każdej głowicy przeznaczenie, żeby Cora wiedziała, co robi, i poprawnie o niej mówiła. Możliwości to **Suplement**, **Podmiana wody: nowa słona woda wchodzi**, **Podmiana wody: stara woda wychodzi**, **Kalkwasser**, **Reaktor wapniowy**, **Pokarm**, **Dolewka** i **Inne**. Ustaw to w **Używana do** w ustawieniach głowicy.

Dwa przeznaczenia do podmiany wody działają w **parach**. Ustaw **Sparowana głowica** jednej głowicy na głowicę, która przenosi wodę w drugą stronę, a Cora potraktuje je jako jedną parę do podmiany wody.

Pojemnik może mieć do 1000 L, przy każdym przeznaczeniu. Sam Apex liczy tylko do 150 L, więc powyżej tego Cora sama śledzi pojemnik na podstawie tego, co dozuje głowica. Wpisz **Całkowitą objętość** przy konfiguracji. Cora też od czasu do czasu zeruje własny licznik Apex, a Aktywność pokazuje to jako *Własny licznik Apex zresetowano do 150 L*.

Każda głowica ma też limit **Największa dawka ręczna**, żeby literówka nie zamieniła dawki ręcznej w coś znacznie większego, niż chodziło. Duże dawki ręczne stają się dostępne dopiero wtedy, gdy tempo głowicy zostało zmierzone prawdziwym testem przy akwarium i gdy włączysz **Duże dawki (Beta)** w ustawieniach głowicy. Domyślnie jest wyłączone. Włącz je dopiero wtedy, gdy obejrzysz przy akwarium pierwszą dużą dawkę.

## Red Sea ReefBeat {#red-sea}

Każde urządzenie Red Sea ma stronę dopasowaną do tego, co robi:

| Urządzenie | Strona pokazuje | Możesz |
|---|---|---|
| [ReefDose](#reefdose) | Każdą głowicę, jej pojemnik i to, co dozowała | Dozować, zmienić dawkę dzienną, edytować **Plan dozowania (Beta)** |
| [ReefRun](#reefrun) | Prędkość i stan pompy powrotnej i pompy odpieniacza | Zmienić prędkość, przełączyć pompę, edytować **Harmonogram pompy (Beta)** |
| [ReefMat](#reefmat) | Pozostałą rolkę, w dniach i metrach | Przesunąć matę, ustawić **Ustawienia ReefMat (Beta)**, zarejestrować nową rolkę |
| [ReefATO+](#reefato) | Poziom w zbiorniku i aktywność dolewki | Ustawić alert zbiornika |
| **ReefControl** *(Beta)* | Swoje sondy temperatury, pH, zasolenia i ORP | Przeglądać odczyty |
| **ReefWave**, **ReefLED** *(Beta)* | Swój bieżący tryb | Na razie tylko podgląd |

ReefControl, ReefControl Power, ReefWave i ReefLED mają w nazwie *(Beta)*, ale są dostępne dla wszystkich. Zobacz [Funkcje Beta](/help/mobile-beta).

Gniazda **ReefControl Power** *(Beta)* pojawiają się jako gniazda, przełączane tym samym elementem sterowania co gniazdo Apex, tylko włączone albo wyłączone. Nie mają jeszcze trybu automatycznego.

Gdy jesteś poza siecią urządzenia, Cora Mobile wysyła polecenia Red Sea przez Cora Max przy akwarium. Jeśli żaden Cora Max nie może tego zrobić, strona o tym mówi i nic nie jest wysyłane.

## ReefDose {#reefdose}

![Strona ReefDose 4 w Cora Mobile](img/mobile-reefdose.webp "Stan, głowice i dzisiejsza suma, Używaj dozownika do zużycia, a pod nimi każda głowica dozująca.")

Dla każdej głowicy możesz ustawić **Dawka dzienna** i **Pozostało w butelce**, uruchomić **Dawkuj teraz** i **Aktywuj harmonogram**. Alerty uzupełnienia ustawiasz dla każdej głowicy dzwonkiem, tak jak opisują [Alerty dozownika](#doser-alerts).

Sekcja **Dozowanie** pokazuje **Nadchodzące dawki**, to, co każda głowica dozowała dziś (**Dozowano dziś do tej pory**), oraz **Dozowane na głowicę** za **Ostatnie 7 dni** albo **Łącznie**. Cora odczytuje to, gdy Cora Max albo Twój telefon jest w Twojej sieci domowej.

### Edytowanie planu dozowania *(Beta)* {#reefdose-plan}

Dotknij ikony kalendarza na stronie ReefDose, żeby otworzyć **Plan dozowania (Beta)**.

Plan to suma dzienna podzielona na maksymalnie cztery okna czasowe. Każde okno ma godzinę początku i końca, liczbę dawek do podania i prędkość: **Cichy**, **Normalny** albo **Szybki**. Dodawaj i usuwaj okna, a potem zapisz. Cora pokaże, co zamierzasz wysłać, i poprosi o potwierdzenie, zanim zastąpi cały plan głowicy.

Edytor najpierw odczytuje plan, który już jest w urządzeniu, więc edytujesz prawdziwy plan, a nie pusty formularz.

## ReefRun {#reefrun}

ReefRun steruje pompami powrotnymi i pompami odpieniaczy. To nie jest pompa cyrkulacyjna. Możesz zmienić prędkość pompy, włączyć ją albo wyłączyć i dostosować ustawienia odpieniacza.

Dotknij ikony kalendarza, żeby otworzyć **Harmonogram pompy (Beta)**. Program to maksymalnie sześć segmentów na jednym porcie pompy. Każdy segment ma godzinę początku i prędkość i może dodać krótki impuls. Prędkość to 0 albo od 5% w górę. Tak jak przy planie ReefDose, najpierw odczytywany jest program z urządzenia, a **Zapisz** prosi o potwierdzenie, zanim zastąpi cały program pompy.

## ReefMat {#reefmat}

Strona ReefMat pokazuje, ile zostało rolki, w dniach i metrach. Dotknij **Przewiń teraz**, żeby ręcznie przesunąć matę. Cora najpierw zapyta **Przewinąć matę teraz?** Możesz też ustawić alert uzupełnienia rolki.

Dotknij koła zębatego, żeby otworzyć **Ustawienia ReefMat (Beta)**:

- **Zaplanowany posuw** włącza przesuwanie o stałych porach, niezależne od czujnika automatycznego posuwu, który już jest na stronie. Włącz go i ustaw, jak często i o ile ma przesuwać matę każdy posuw.
- **Model ReefMat** i **Pozycja silnika** (**Lewa** albo **Prawa**) mówią Corze, jakie masz urządzenie i w jakim ułożeniu.

Po założeniu nowej rolki daj znać Corze przez **Nowa rolka (Beta)**: podaj jej grubość, a jeśli znasz, także średnicę zewnętrzną. **Przewiń teraz** przesuwa tylko już założoną matę.

## ReefATO+ {#reefato}

Strona ReefATO+ pokazuje poziom w zbiorniku i ostatnie dolewki. Alert zbiornika ustawisz dzwonkiem. Cora szacuje, na ile dni wystarczy zbiornik, na podstawie ostatniego zużycia na dolewkę, a o to też możesz zapytać Asystenta.

## Gdy urządzenie Red Sea samo się zatrzyma {#red-sea-stops}

Urządzenie może samo się zatrzymać. Pompa ReefRun robi to na przykład wtedy, gdy kubek odpieniacza się zapełni. Wtedy strona mówi dlaczego i proponuje rozwiązanie:

| Urządzenie | Strona pokazuje | Dotknij |
|---|---|---|
| ReefRun | Która pompa stanęła i dlaczego, na przykład *Pełny kubek. Opróżnij go, a potem wznów.* | **Wznów** |
| ReefRun albo ReefMat | **Zatrzymanie awaryjne** | **Usuń stan awaryjny** |
| ReefMat | **Mata zablokowana**, **Błąd instalacji** albo **Błąd konfiguracji** | **Wznów** |
| ReefMat | *Załaduj nową rolkę, a potem potwierdź to w aplikacji Red Sea.* | **Nowa rolka już załadowana** |
| ReefMat | **Czujnik wymaga wyczyszczenia** | **Czujnik wyczyszczony** |
| ReefDose | **Awaria głowicy**, z nazwą głowicy | **Resetuj** |
| ReefATO+ | **Usuń awarię** | **Wznów** |

Niektóre z nich najpierw proszą o potwierdzenie. Poza siecią urządzenia idą przez Cora Max przy akwarium, tak jak opisuje [Red Sea ReefBeat](#red-sea).

## Alerty dozownika {#doser-alerts}

DŌS i ReefDose mają alerty na własnej stronie. Zakładka **Reguły** w [Centrum alertów](/help/mobile-alerts) ma po jednym wierszu na dozownik, który ją otwiera, a przycisk **Otwórz dozownik** przy alercie dozownika też Cię tu przenosi.

Na stronie DŌS dotknij karty **Alerty** (albo dzwonka na pasku tytułu). Arkusz wymienia każdą głowicę i dla każdej możesz ustawić:

- *[głowica] · pozostałe dni*, na przykład *Jod · pozostałe dni*: dostajesz alert, gdy zapasu jest na mniej dni niż ta liczba
- *[głowica] · pozostało*: dostajesz alert, gdy w pojemniku zostanie mniej niż ta ilość
- **Pozostałe miejsce w zbiorniku odpadów**, dla głowicy, która odbiera starą wodę: dostajesz alert, gdy zbiornik odpadów się zapełnia
- **Alerty o pominiętej dawce**: przełącznik, który informuje, gdy głowica pominie zaplanowaną dawkę

Każdy próg ma własny przełącznik, więc możesz jeden wyłączyć i zachować jego wartość. Gdy skończysz, dotknij **Zapisz**.

Na stronie ReefDose dotknij dzwonka na pasku tytułu. Każda głowica ma własny próg pozostałych dni i przełącznik.

Wartości domyślne i inne materiały eksploatacyjne opisują [Materiały eksploatacyjne](/help/mobile-consumables).

## Pompy Jecod / Jebao {#jecod}

Strona pompy pokazuje bieżący wzór fali (tryb) i intensywność, a Ty możesz zmienić oba. Wybierz na górze **Tak samo cały dzień** albo **Harmonogram**. Układanie programu dnia, jego kopiowanie, zapisywanie i udostępnianie opisują [Harmonogramy sprzętu](/help/mobile-schedules).

Jeśli pompa należy do grupy, strona pokazuje jej rolę, na przykład **Prowadzi grupę**, **Podąża: zgodnie** albo **Podąża: przemiennie**.

### Przerwa na karmienie {#jecod-feeding}

Przerwę na karmienie uruchomisz w sekcji **Karmienie** na stronie pompy. Niektóre pompy same kończą przerwę, a strona pokazuje wtedy *Pompa zakończy to sama.*

:::warning Podczas przerwy na karmienie nie zamykaj strony pompy
Niektóre pompy same nie kończą karmienia, a strona o tym mówi. Dla nich i dla każdej pompy na harmonogramie Cora Mobile przywraca wzór fali i harmonogram tylko wtedy, gdy strona pompy pozostaje otwarta. Jeśli wyjdziesz ze strony, pompa zostaje zatrzymana w trybie karmienia albo poza harmonogramem, dopóki znów czegoś nie zmienisz albo nie dotkniesz **Harmonogram**.
:::

Pompa Bluetooth musi być w zasięgu telefonu, żeby uruchomić karmienie, a pompa sieciowa musi być w Twojej sieci.

### Sprawdzanie awarii {#jecod-fault-checks}

**Sprawdzanie awarii** ustala, jak często Cora ponownie odczytuje pompę, żeby ostrzec Cię o awarii, na przykład zablokowanej pompie albo pracy na sucho. Jeśli to wyłączysz, te ostrzeżenia dla tej pompy przestaną przychodzić. Sprawdzanie awarii wymaga Cora Max przy akwarium. Twój wybór zostaje zapisany, a sprawdzanie zaczyna się, gdy taki Cora Max zostanie dodany. **Użyj tego dla każdej pompy w tym akwarium** kopiuje to ustawienie do wszystkich.

## AquaWiz {#aquawiz}

Karta AquaWiz pokazuje odczyty alkaliczności, a także pH, jeśli Twoje urządzenie je zgłasza. Pokazuje też docelowe KH, siłę dawki, a dla urządzenia z ustawionym dozowaniem także maksymalną dawkę na godzinę i to, ile suplementu alkaliczności zostało w pojemniku. Te wartości pochodzą prosto z Twoich ustawień AquaWiz, więc zmieniasz je w aplikacji AquaWiz. Cora nie może sterować AquaWiz.

Jeśli Twoje urządzenie śledzi pojemnik, Cora ostrzega Cię, gdy kończy się suplement, domyślnie przy 100 mL. Zmienisz to w jego regule w [Centrum alertów](/help/mobile-alerts).

## Maxspect {#maxspect}

:::note Beta
**Beta.** Maxspect jest w wersji Beta i jest dostępny tylko dla użytkowników Beta. Jeśli nie jesteś użytkownikiem Beta, nie zobaczysz go w **Dodaj urządzenie**. Aby poprosić o dostęp do Beta, [skontaktuj się z pomocą techniczną](/support.html). Część funkcji sterowania może być ograniczona, a to, co tu widzisz, może się zmieniać między aktualizacjami. Jeśli coś nie działa tak, jak opisano, daj nam znać przez [Zgłaszanie problemu](/help/mobile-support). Więcej w [Funkcjach Beta](/help/mobile-beta).
:::

Strona Gyre pokazuje, czy Gyre pracuje, wzór fali i prędkość **Gyre A** i **Gyre B** oraz kiedy je ostatnio odczytano. Stąd możesz:

- Włączyć albo wyłączyć Gyre przełącznikiem obok jego stanu. Cora najpierw poprosi o potwierdzenie. Wyłączenie zatrzymuje oba Gyre i nie rusza harmonogramu.
- Dotknąć **Zmień ustawienia**, żeby ustawić wzór fali i prędkość każdego Gyre, czas trwania dla wzorów, które go mają, oraz to, czy oba Gyre są połączone. Cora wymieni, co się zmieni, i poprosi o potwierdzenie. Tryb naprzemienny ustawia się w aplikacji Maxspect, a Gyre, który w nim pracuje, zachowuje swoje narastania i czasy utrzymania.
- Dotknąć **Ustaw program**, jeśli programu zapisanego w Gyre nie da się odczytać. Ustawia oba Gyre, żeby urządzenie mogło znów ruszyć.
- Zobaczyć program dnia Gyre na karcie **Harmonogram**. Tutaj możesz go tylko podejrzeć. Harmonogram ustawiasz w aplikacji Maxspect.
- Sprawdzić **Stan pompy**. Pokazuje, kiedy pompa będzie wymagała czyszczenia (pompa sama to odlicza), prąd pobierany przez głowicę A, zamontowane głowice i oprogramowanie. Dotknij **Odczytaj**, żeby to pobrać.

:::note Jak Cora Mobile łączy się z Gyre
Jeśli akwarium obsługuje Cora Max, Cora Mobile łączy się przez ten Cora Max, nawet gdy jesteś poza domem. **Zmień ustawienia** zaczyna wtedy od ostatniego odczytu tego Cora Max. W przeciwnym razie telefon rozmawia z Gyre bezpośrednio i musi być w jego sieci. Otwarcie strony odczytuje Gyre. Jeśli strona pokazuje starszy zapisany odczyt, **Zmień ustawienia** jest ukryte, dopóki nie dotkniesz odświeżenia.
:::

## GHL ProfiLux i Mitras {#ghl}

:::note Beta
**Beta.** GHL jest w wersji Beta i jest dostępny tylko dla użytkowników Beta. Jeśli nie jesteś użytkownikiem Beta, nie zobaczysz go w **Dodaj urządzenie**. Aby poprosić o dostęp do Beta, [skontaktuj się z pomocą techniczną](/support.html). Część odczytów albo funkcji sterowania może jeszcze nie działać, a to, co tu widzisz, może się zmieniać między aktualizacjami. Jeśli coś nie działa tak, jak opisano, daj nam znać przez [Zgłaszanie problemu](/help/mobile-support). Więcej w [Funkcjach Beta](/help/mobile-beta).
:::

Strona kontrolera pokazuje jego sondy, gniazda, dozowniki i czujniki poziomu, a w modelach Director także wyniki testów KH i jonów.

Sterowanie jest wyłączone, dopóki nie włączysz **Zezwól na sterowanie z Cora (Beta)** na stronie urządzenia. Domyślnie jest wyłączone, a jego włączenie pozwala Corze wysyłać do tego kontrolera polecenia przerwy na karmienie, konserwacji, podmiany wody, burzy, oświetlenia, wartości zadanych i gniazd. Gdy już możesz dodać urządzenie, ten przełącznik nie wymaga dodatkowego dostępu.

Po włączeniu:

- Gniazdo można ustawić na **Zawsze włączone**, **Zawsze wyłączone** albo **Powrót do automatycznego**, żeby oddać je własnemu programowi kontrolera.
- Wartość zadana, na przykład temperatura albo pH, pokazuje dozwolony zakres i odrzuca wartość spoza niego.

:::warning Zmiana gniazda albo wartości zadanej zapisuje się w samym kontrolerze
Nie jest przechowywana tylko w Corze. Ustawienie gniazda na Zawsze włączone albo Zawsze wyłączone nadpisuje dla niego własny program kontrolera, dopóki nie wybierzesz Powrót do automatycznego.
:::

Jeśli gniazdo albo wartość zadana wygląda na należącą do grzałki albo pompy powrotnej, Cora prosi o potwierdzenie dwa razy przed wysłaniem.

Jeśli w pojemniku dozownika kończy się płyn, Cora ostrzega Cię tak samo jak przy innych materiałach eksploatacyjnych. Domyślnie przy 20% napełnienia, a zmienisz to w regule dozownika w [Centrum alertów](/help/mobile-alerts).

:::note ProfiLux mini
Mini może tylko przełączać swoje gniazda. Wszystko inne tutaj, na przykład wartości zadane i przerwa na karmienie, wymaga ProfiLux 3, 4 albo Mitras.
:::

Jeśli kontroler odrzuci zmianę, sprawdź, czy jego API GHL jest włączone z pełnym dostępem. GHL wyłącza je po każdej aktualizacji oprogramowania. Kroki opisuje [Rozwiązywanie problemów](/help/troubleshooting).

## HYDROS {#hydros}

:::note Beta
**Beta.** HYDROS jest w wersji Beta i jest dostępny tylko dla użytkowników Beta. Jeśli nie jesteś użytkownikiem Beta, nie zobaczysz go w **Dodaj urządzenie**. Aby poprosić o dostęp do Beta, [skontaktuj się z pomocą techniczną](/support.html). Część odczytów albo funkcji sterowania może jeszcze nie działać, a to, co tu widzisz, może się zmieniać między aktualizacjami. Jeśli coś nie działa tak, jak opisano, daj nam znać przez [Zgłaszanie problemu](/help/mobile-support). Więcej w [Funkcjach Beta](/help/mobile-beta).
:::

To, co tu widzisz, zależy od klucza, którym połączono urządzenie. Klucz **Read** daje tylko jego wejścia. Klucz **Write** dodaje wyjścia, tryby, dozowanie i polecenia testera, a także baner na stronie, który przypomina, jakiego klucza używasz.

Przy kluczu zapisu sterowanie też jest wyłączone, dopóki nie włączysz **Zezwól na sterowanie z Cora (Beta)** na stronie urządzenia. Domyślnie jest wyłączone.

Po włączeniu strona może pokazywać:

- **Wyjścia**, jako przełącznik dla wyjścia włącz/wyłącz, suwak dla poziomu, na przykład pompy albo oświetlenia, albo przycisk dla flagi. Nadpisane wyjście pokazuje **Nadpisane** z przyciskiem **Powrót do harmonogramu**, który oddaje je jego własnemu programowi.
- **Tryby**, na przykład Feed albo Water Change, jako rząd opcji. Dotknięcie jednej prosi o potwierdzenie.
- **Głowice dozujące**, każdą z przyciskiem **Dozuj** i pozycją **Ustawienia głowicy**, gdzie ustawiasz jej własne limity: największą dawkę ręczną i dzienny limit. Prośba o więcej niż limit głowicy albo więcej, niż zostało z jej dziennego limitu, zostaje odrzucona z liczbami w komunikacie.
- **Polecenia testera**, dla podłączonego iV albo Maven, uruchamiane przyciskiem i najpierw potwierdzane.

Jeśli kontroler od jakiegoś czasu się nie zgłaszał, strona o tym mówi, a odczyty mogą być nieaktualne. Polecenie wysłane, gdy kontroler wygląda na offline, w ogóle nie zostaje wysłane, a strona też o tym mówi.

## Focustronic {#focustronic}

:::note Beta
**Beta.** Focustronic jest w wersji Beta i jest dostępny tylko dla użytkowników Beta. Jeśli nie jesteś użytkownikiem Beta, nie zobaczysz go w **Dodaj urządzenie**. Aby poprosić o dostęp do Beta, [skontaktuj się z pomocą techniczną](/support.html). Więcej w [Funkcjach Beta](/help/mobile-beta).
:::

Każde urządzenie pokazuje swój stan, oprogramowanie, ostatni test, a w przypadku Alkatronic zmierzoną alkaliczność i pH. Widzisz też pompy z ilością pozostałą w każdej, parametry, fiolki i ostrzeżenia o odczynniku albo buforze. Cora prosi Focustronic o nowe odczyty co 30 minut.

W **Sterowanie** możesz użyć **Zmierz teraz**, **Dozuj teraz** z pompy (do 500 mL naraz), a w Mastertronic **Testuj teraz**. Każde z nich najpierw prosi o potwierdzenie. Cora nigdy nie ponawia dawki, więc jeśli wynik jest nieznany, sprawdź urządzenie. Polecenia idą przez serwery Focustronic, nad którymi Cora nie ma kontroli, i są dostępne tylko wtedy, gdy urządzenie jest online.

## EcoTech, Inkbird i kamery {#ecotech-inkbird-cameras}

:::note Beta
**Beta.** EcoTech, Inkbird i kamery są w wersji Beta i są dostępne tylko dla użytkowników Beta. Jeśli nie jesteś użytkownikiem Beta, nie zobaczysz ich w **Dodaj urządzenie**. Aby poprosić o dostęp do Beta, [skontaktuj się z pomocą techniczną](/support.html).
:::

Mają własne strony:

- Lampy EcoTech Radion, pompy VorTech i dozowniki Versa: [Lampy, pompy i dozowniki EcoTech](/help/mobile-ecotech)
- Monitory powietrza w pomieszczeniu Inkbird tylko zgłaszają odczyty, więc nie ma czym sterować: [Podłączanie sprzętu](/help/mobile-connections#inkbird-room-air-monitor)
- Kamery i Czuwanie skimmera: [Kamery i Czuwanie skimmera](/help/mobile-cameras)

## Co się dzieje po zmianie {#what-happens-after-you-change-something}

Każda zmiana jest zapisywana w [Aktywności](/help/mobile-activity), razem z miejscem, z którego przyszła. Jeśli urządzenie nie przyjmie zmiany, to też jest tam zapisane.

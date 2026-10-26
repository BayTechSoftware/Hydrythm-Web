---
title: Sterowanie sprzętem
description: Otwórz stronę urządzenia, żeby zobaczyć jego stan na żywo i przełączać gniazda, pompy, głowice dozujące i testery, marka po marce.
section: Cora Mobile
reviewed: 2026-10-24
order: 13
group: Equipment
twin: max-device-control
---

Na własnej stronie urządzenia zobaczysz jego stan na żywo i zmienisz to, co robi. Otworzysz ją z **Urządzenia** → dotknij urządzenia albo dotknij jego kafelka na panelu.

![Strona ReefATO+ w Cora Mobile](img/mobile-device-detail.webp "Stan, dzisiejsze odczyty i poziom wody, a pod nimi wyciek, dolewki i kalibracja sondy.")

Każda strona urządzenia jest ułożona tak samo. Na górze są nazwa i szczegóły, potem rząd odczytów na żywo, stan, który zgłasza urządzenie, i jego elementy sterowania. Dzwonek na pasku tytułu ustawia progi alertów dla tego urządzenia, tak jak opisują [Materiały eksploatacyjne](/help/mobile-consumables). Jak w ogóle dodać urządzenie, opisuje [Podłączanie sprzętu](/help/mobile-connections).

Przejdź do swojego sprzętu: [Neptune Apex](#neptune-apex) · [Trident](#trident) · [DŌS](#dos) · [Red Sea](#red-sea) · [ReefDose](#reefdose) · [ReefRun](#reefrun) · [ReefMat](#reefmat) · [ReefATO+](#reefato) · [Alerty dozownika](#doser-alerts) · [Jecod](#jecod) · [AquaWiz](#aquawiz)

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
- W **Mapowaniu parametrów** wybierasz, co dostarcza każda sonda. Sondy zgłaszają się do Cory jako źródła, które możesz umieścić na panelu. Zobacz [Mapowanie parametrów i sondy](/help/mobile-probes).
- **Akwaria** pokazują, które akwaria obsługuje Apex. Dotknij **Zmień**, żeby je edytować.
- **Gniazda** przełączasz między **AUTO**, **WYŁ.** i **WŁ.** widżetem **Gniazdo** na panelu. AUTO oddaje sterowanie programowi Apex. Zobacz [Rodzaje widżetów](/help/mobile-widgets#outlet).

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
- **Dozuj teraz**, żeby podać ręcznie odmierzoną dawkę

:::note Harmonogramy edytuj w Apex Fusion
Cora pokazuje harmonogram i śledzi, co zostało zdozowane, ale nie zmienia harmonogramu. Harmonogram, szybkość dozowania i liczbę dawek edytujesz w aplikacji Apex Fusion. Wstrzymywanie, napełnianie i dozowanie ręczne działają tutaj.
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

Każda głowica poza Suplementem i Pokarmem ma też limit **Największa dawka ręczna**, żeby literówka nie zamieniła dawki ręcznej w coś znacznie większego, niż chodziło. Głowice Suplement i Pokarm zachowują zamiast tego mały, stały limit. Gdy ten limit jest ustawiony, głowica może mieć też **Dzienny limit dla automatyzacji i Asystenta**, który zastępuje domyślne 10 mL dziennie.

## Red Sea ReefBeat {#red-sea}

Każde urządzenie Red Sea ma stronę dopasowaną do tego, co robi:

| Urządzenie | Strona pokazuje | Możesz |
|---|---|---|
| [ReefDose](#reefdose) | Każdą głowicę, jej pojemnik i to, co dozowała | Dozować, zmienić dawkę dzienną |
| [ReefRun](#reefrun) | Prędkość i stan pompy powrotnej i pompy odpieniacza | Zmienić prędkość, przełączyć pompę |
| [ReefMat](#reefmat) | Pozostałą rolkę, w dniach i metrach | Przesunąć matę |
| [ReefATO+](#reefato) | Poziom w zbiorniku i aktywność dolewki | Ustawić alert zbiornika |



Gdy jesteś poza siecią urządzenia, Cora Mobile wysyła polecenia Red Sea przez Cora Max przy akwarium. Jeśli żaden Cora Max nie może tego zrobić, strona o tym mówi i nic nie jest wysyłane.

## ReefDose {#reefdose}

![Strona ReefDose 4 w Cora Mobile](img/mobile-reefdose.webp "Stan, głowice i dzisiejsza suma, Używaj dozownika do zużycia, a pod nimi każda głowica dozująca.")

Dla każdej głowicy możesz ustawić **Dawka dzienna** i **Pozostało w butelce**, uruchomić **Dozuj teraz** i **Aktywuj harmonogram**. Alerty uzupełnienia ustawiasz dla każdej głowicy dzwonkiem, tak jak opisują [Alerty dozownika](#doser-alerts).

Sekcja **Dozowanie** pokazuje **Nadchodzące dawki**, to, co każda głowica dozowała dziś (**Dozowano dziś do tej pory**), oraz **Dozowane na głowicę** za **Ostatnie 7 dni** albo **Łącznie**. Cora odczytuje to, gdy Cora Max albo Twój telefon jest w Twojej sieci domowej.


## ReefRun {#reefrun}

ReefRun steruje pompami powrotnymi i pompami odpieniaczy. To nie jest pompa cyrkulacyjna. Możesz zmienić prędkość pompy, włączyć ją albo wyłączyć i dostosować ustawienia odpieniacza.


## ReefMat {#reefmat}

Strona ReefMat pokazuje, ile zostało rolki, w dniach i metrach. Dotknij **Przewiń teraz**, żeby ręcznie przesunąć matę. Cora najpierw zapyta **Przewinąć matę teraz?** Możesz też ustawić alert uzupełnienia rolki.


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

Strona pompy pokazuje bieżący wzór fali (tryb) i intensywność, a Ty możesz zmienić oba. Jej stan jest w wierszu tytułu, obok nazwy pompy. Przełącznik z **Cały dzień tak samo** i **Harmonogram** oznacza działający tryb napisem *· działa*, a strona otwiera się na nim. Układanie programu dnia, jego kopiowanie, zapisywanie i udostępnianie opisują [Harmonogramy sprzętu](/help/mobile-schedules).

Jeśli pompa należy do grupy, strona pokazuje jej rolę, na przykład **Prowadzi grupę**, **Podąża: zgodnie** albo **Podąża: przemiennie**.

### Przerwa na karmienie {#jecod-feeding}

Przerwę na karmienie uruchomisz w **Karmienie** na stronie pompy: dotknij **5**, **10**, **15** lub **30** min. Niektóre pompy same kończą przerwę, a strona pokazuje wtedy *Pompa zakończy to sama.*

:::warning Podczas przerwy na karmienie nie zamykaj strony pompy
Niektóre pompy same nie kończą karmienia, a strona o tym mówi. Dla nich i dla każdej pompy na harmonogramie Cora Mobile przywraca wzór fali i harmonogram tylko wtedy, gdy strona pompy pozostaje otwarta. Jeśli wyjdziesz ze strony, pompa zostaje zatrzymana w trybie karmienia albo poza harmonogramem, dopóki znów czegoś nie zmienisz albo nie dotkniesz **Harmonogram**.
:::

Jeśli w Twoim domu jest Cora Max, to on kończy karmienie i przywraca pompę do jej programu po upływie czasu, nawet gdy Cora Mobile jest zamknięty. Ostrzeżenie powyżej dotyczy wtedy tylko sytuacji bez Cora Max.

Pompa Bluetooth musi być w zasięgu telefonu, żeby uruchomić karmienie, a pompa sieciowa musi być w Twojej sieci.

### Sprawdzanie awarii {#jecod-fault-checks}

**Sprawdzanie awarii** ustala, jak często Cora ponownie odczytuje pompę, żeby ostrzec Cię o awarii, na przykład zablokowanej pompie albo pracy na sucho. Jeśli to wyłączysz, te ostrzeżenia dla tej pompy przestaną przychodzić. Sprawdzanie awarii wymaga Cora Max przy akwarium. Twój wybór zostaje zapisany, a sprawdzanie zaczyna się, gdy taki Cora Max zostanie dodany. **Użyj tego dla każdej pompy w tym akwarium** kopiuje to ustawienie do wszystkich.

## AquaWiz {#aquawiz}

Karta AquaWiz pokazuje odczyty alkaliczności, a także pH, jeśli Twoje urządzenie je zgłasza. Cora nie może sterować AquaWiz, więc zmieniaj jego ustawienia w aplikacji AquaWiz.

W sekcji **Kontroler** na stronie urządzenia Cora pokazuje to, co zgłasza kontroler, każdy wiersz tylko wtedy, gdy kontroler go zgłasza:

- docelowe KH;
- ile suplementu alkaliczności zostało, wraz z poziomem ostrzegawczym ustawionym na kontrolerze (na przykład *niski poziom od 100 mL*);
- ile mL potrzeba na 1 dKH (na przykład *48 mL na dawkę dKH*);
- maksymalną dawkę na pomiar (*Do 20 mL na pomiar*);
- wersję oprogramowania.

Pod odczytami karta mówi, kiedy zrobiono ostatni pomiar (na przykład *Pomiar: 14:00*) i skąd pochodzi: **Co godzinę z Twojego Cora Max** albo **Z chmury AquaWiz, co 12 godzin**. Pokazuje też **zmianę pH**. Otwarcie strony prosi o świeży odczyt, a **Odczytaj teraz** prosi o niego jeszcze raz, najwyżej raz na 15 minut. Jeśli odczyt się nie zmienił, to normalne: urządzenie mierzy tylko od czasu do czasu.

Karta pokazuje też pompę i sondę pH, a Cora ostrzega Cię, gdy pompa zgłasza usterkę albo sonda pH uległa awarii lub kończy się jej żywotność. Działa to dla każdego AquaWiz, z Cora Max lub bez. Gdy Cora Max czyta urządzenie co godzinę, karta pokazuje także poziom w pojemniku z wodą, a Cora ostrzega Cię, gdy jest niski lub wysoki dłużej niż godzinę.

Jeśli Twoje urządzenie śledzi pojemnik, Cora ostrzega Cię, gdy kończy się suplement, przy poziomie ostrzegawczym ustawionym na kontrolerze. Nadal możesz go zmienić w jego regule w [Centrum alertów](/help/mobile-alerts), a Twoja zmiana zostaje.


## Co się dzieje po zmianie {#what-happens-after-you-change-something}

Każda zmiana jest zapisywana w [Aktywności](/help/mobile-activity), razem z miejscem, z którego przyszła. Jeśli urządzenie nie przyjmie zmiany, to też jest tam zapisane.

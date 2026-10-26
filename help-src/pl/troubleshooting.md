---
title: Rozwiązywanie problemów
description: Napraw nieaktualny odczyt, urządzenie w trybie offline, polecenie, które nie przeszło, Cora Max, którego nie da się sparować, albo alert, który nie znika.
section: Help
reviewed: 2026-10-24
order: 1
---

Znajdź grupę, do której należy Twój problem, a potem komunikat albo objaw, który widzisz. Nagłówki w cudzysłowie to dokładne słowa, które pokazuje Cora.

- [Odczyty i widżety](#readings-and-widgets)
- [Urządzenie przestało raportować albo jest nieosiągalne](#device-not-reporting)
- [Polecenie nie przeszło](#command-did-not-go-through)
- [Cora Max](#cora-max)
- [Alerty, powiadomienia i codzienne podsumowanie](#alerts-and-notifications)
- [Cora Assistant i głos](#cora-assistant-and-voice)
- [Wyniki z laboratorium i raporty zdrowia](#lab-results-and-health-reports)
- [Język, jednostki i logowanie](#language-units-and-signing-in)


## Odczyty i widżety {#readings-and-widgets}

### Widżet nie pokazuje wartości {#a-widget-shows-no-value}

Sprawdź po kolei.

1. Spójrz na wiek pobliskich widżetów. Jeśli wszystkie też są stare, chodzi o połączenie, a nie o parametr.
2. Otwórz zakładkę **Urządzenia**. Jeśli urządzenie jest nieosiągalne, jego wiersz ma czerwoną kropkę albo o tym mówi.
3. Sprawdź, w którym akwarium jest urządzenie. Urządzenie raportujące do niewłaściwego akwarium wygląda dokładnie tak samo jak takie, które nie raportuje. Otwórz urządzenie i sprawdź jego akwarium.
4. Sprawdź, czy coś to mierzy. Nic nie zgłasza fosforanów, jeśli nie masz sprzętu, który je mierzy, albo nie zapisujesz ich ręcznie.

### Widżet jest szary {#a-widget-is-grey}

Szary oznacza, że Cora nie ocenia tego odczytu. Są trzy typowe powody.

1. Alert dla niego jest wyłączony. Włącz go ponownie w zakładce **Reguły** w Centrum alertów.
2. Nie ma zakresu, według którego można go ocenić. Przytrzymaj widżet i ustaw zakres.
3. Odczyt jest za stary. Sprawdź wiek na widżecie, a potem zapisz nowy odczyt albo sprawdź urządzenie.

Co oznacza każdy kolor, opisuje [Jak czytać panel](/help/mobile-dashboard#colours).

### Odczyt jest nieaktualny {#a-reading-is-stale}

Wiek na widżecie jest prawdziwy. Nic nowego nie przyszło.

- Parametry zapisywane ręcznie stają się nieaktualne, gdy nikt nie zapisał odczytu. Zapisz go.
- Odczyty ze sprzętu stają się nieaktualne, gdy urządzenie przestaje raportować. Sprawdź jego wiersz w **Urządzenia**.
- Część sprzętu raportuje tylko od czasu do czasu. Titrator, który mierzy co godzinę, zwykle pokazuje `1g`. To normalne.

### Dwa źródła się nie zgadzają {#two-sources-disagree}

Nic się nie zepsuło. Gdy sonda i test kropelkowy się nie zgadzają, mówi Ci to coś prawdziwego o Twoim systemie.

Zwykle sondę trzeba skalibrować. Czasem test kropelkowy jest stary. Skalibruj sondę, przetestuj ponownie świeżym odczynnikiem i porównaj oba w tych samych warunkach. Jeśli jeden odczyt był ewidentnie błędny, możesz go wykluczyć. Zobacz [Szczegóły parametru](/help/mobile-metric-detail).

[Wynik ICP](/help/mobile-icp-health) daje trzecią liczbę do porównania, ale sam nie rozstrzygnie sprawy. Laboratoria różnią się między sobą, a sposób obchodzenia się z próbką i jej wysyłki zmienia wynik.

### Widżet pokazuje złe jednostki {#a-widget-shows-the-wrong-units}

To jednostki wyświetlania akwarium. Twoje dane są w porządku, a wartości są przechowywane tak samo, niezależnie od tego, jak je pokazano.

1. Otwórz **Ustawienia**, otwórz to akwarium i wybierz **Jednostki**.
2. Zmień je tam. Każdy telefon i Cora Max, który pokazuje to akwarium, się dostosuje.

### Wskaźnik albo próg wygląda inaczej po zmianie jednostek {#a-gauge-or-threshold-looks-different-after-changing-display-}

Tak ma być. Wskaźniki, kafelki i historia rysują się w wybranej jednostce. Wartości pod spodem się nie zmieniły.

### Pulpit wygląda źle po edycji {#my-dashboard-looks-wrong-after-editing}

Odczyty, historia i dziennik są przechowywane osobno od układu, więc nic nie przepadło.

- **W telefonie** edytor nie ma cofania ani zapisanych projektów. Otwórz **Edytuj panel** i ułóż widżety z powrotem. Więcej w [Edytowaniu panelu](/help/mobile-dashboard-editing).
- **Na Cora Max** wczytaj zapisany projekt: otwórz **Układ panelu**, dotknij **Moje panele** i wybierz jeden. Jeśli żadnego nie zapisano, odbuduj układ i dotknij **Zapisz ten projekt**, żeby następnym razem wystarczyło jedno dotknięcie. Więcej w [Edytowaniu panelu Cora Max](/help/max-dashboard-editing#saving-layouts).

### Ustalanie, dlaczego coś się zmieniło {#establishing-why-something-changed}

**Ustawienia → Aktywność** wymienia każde przełączenie gniazda, karmienie i dawkę oraz to, co o nie poprosiło: Cora Mobile, Cora Max, głos, Asystent, automatyzacja albo Twoje konto. Więcej w [Aktywności i osi czasu](/help/mobile-activity).

## Urządzenie przestało raportować albo jest nieosiągalne {#device-not-reporting}

### „[Urządzenie]: przestał raportować” {#device-stopped-reporting}

Cora wysyła to, gdy urządzenie ucichnie. Nie oznacza to, że urządzenie jest zepsute, tylko że Cora od jakiegoś czasu nic od niego nie dostała. Jak długo Cora czeka dla każdej marki, opisują [Alerty i progi](/help/mobile-alerts#stopped-reporting).

1. Sprawdź zasilanie urządzenia i jego zasięg Wi-Fi albo Bluetooth.
2. Sprawdź, czy Cora Max, który je odczytuje, jest włączony i online. Bez Cora Max telefon odczytuje urządzenie Neptune Apex, Red Sea albo Jecod tylko wtedy, gdy Cora Mobile jest otwarta w tej samej sieci Wi-Fi.
3. Poczekaj na następny odczyt. Gdy urządzenie znów zacznie raportować, dostaniesz drugie powiadomienie.


### „Urządzenie jest offline. Wyświetlany jest ostatni znany stan.” {#device-is-offline-showing-last-known-state}

Urządzenie przestało raportować, a Cora pokazuje ostatnie wartości, które miała. Nie są aktualne.

1. Sprawdź własne połączenie sieciowe urządzenia.
2. Nie traktuj wartości jako bieżących, dopóki wiersz nie przestanie pokazywać offline.

### Urządzenie jest nieosiągalne {#a-device-cannot-be-reached}

Zwykle chodzi o sieć.

1. Czy sprzęt jest włączony i działa we własnej aplikacji?
2. Czy jest w tej samej sieci, w której go dodano?
3. Czy coś zmieniło się w routerze (nowy sprzęt, nowa nazwa sieci, izolacja sieci gościnnej)?

Sprzęt w sieci lokalnej musi być osiągalny w tej sieci. Sprzęt, który łączy się przez konto producenta, nie musi, ale to konto nadal musi być ważne. Jeśli zmienił się adres urządzenia, otwórz je w zakładce **Urządzenia** i dotknij **Edytuj połączenie** w **Połączenie**.

### Urządzenie mówi, że logowanie zostało odrzucone {#a-device-says-the-sign-in-was-refused}

Producent odrzucił zapisane logowanie. Prawie zawsze dlatego, że zmieniono hasło u producenta. Otwórz wiersz urządzenia i zaloguj się ponownie. AquaWiz jest wyjątkiem: Cora nie przechowuje dla niego hasła, więc zmiana hasła AquaWiz niczego nie zmienia.

### „Odczyty Red Sea przestały się aktualizować” {#red-sea-readings-have-stopped-updating}

Nic w tym akwarium nie odczytuje teraz Twojego sprzętu Red Sea, więc odczyty na ekranie się nie odświeżają.

1. Otwórz **Ustawienia**, otwórz akwarium, a potem **Główne Cora Max**. Sprawdź, czy ustawiono Cora Max albo wybrano **Każde aktywne (automatycznie)**.
2. Jeśli nie masz Cora Max, otwórz akwarium w Cora Mobile, gdy telefon jest w tej samej sieci Wi-Fi co sprzęt Red Sea.
3. Sprawdź, czy sprzęt Red Sea jest włączony i online we własnej aplikacji.

### Część ustawień ReefBeat jest wyszarzona albo ich brakuje {#some-reefbeat-settings-are-greyed-out-or-missing}

To normalne. Własne ustawienia urządzenia Red Sea otwierają się tylko wtedy, gdy telefon jest w tej samej sieci co urządzenie. Poza tą siecią widzisz odczyty, a polecenia nadal idą przez Cora Max w akwarium, jeśli je ma. Własne ustawienia urządzenia pozostają niedostępne.

1. Dołącz do sieci Wi-Fi akwarium, żeby zmienić te ustawienia.
2. Odczyty i historia działają, gdy jesteś poza domem.


### Odczyt AquaWiz ma kilka godzin {#an-aquawiz-reading-is-hours-old}

To może być normalne. AquaWiz pozwala Corze czytać swoją chmurę tylko co 12 godzin, więc bez Cora Max odczyt może mieć nawet pół doby. Otwórz stronę urządzenia w Cora Mobile: pokazuje, kiedy odczyt zmierzono i skąd pochodzi, a **Odczytaj teraz** prosi o świeży (najwyżej raz na 15 minut).

Jeśli masz Cora Max, a karta nadal pokazuje **Z chmury AquaWiz, co 12 godzin**:

- Sprawdź, czy kontroler jest w zasięgu Wi-Fi głównego Cora Max akwarium.
- Sprawdź w aplikacji AquaWiz, czy oprogramowanie kontrolera jest aktualne; starsze nie ma dostępu lokalnego.
- Po dwóch nieudanych odczytach z rzędu Cora Max czeka do następnego dnia. Jeśli nadal się nie udaje, skontaktuj się z pomocą.

### AquaWiz prosi o ponowne połączenie {#an-aquawiz-says-to-link-it-again}

AquaWiz zgłosił, że nazwa użytkownika zapisana w Corze nie jest już właścicielem tego kontrolera, na przykład dlatego, że kontroler przeszedł na inne konto AquaWiz. Urządzenie jest pomarańczowe. Otwórz **Urządzenia → Dodaj urządzenie → AquaWiz**, zaloguj się kontem, które jest właścicielem kontrolera, i połącz go ponownie. Cora nie przechowuje hasła ani tokenu AquaWiz, więc nic innego nie wygasa.

## Polecenie nie przeszło {#command-did-not-go-through}

Każde polecenie kończy się jako **Potwierdzono**, **Niepotwierdzone**, **Odmówiono** albo **Bez zmian**. Co oznacza każdy wynik, opisuje [Sterowanie sprzętem](/help/mobile-device-control).

### „Nie udało się połączyć z tą pompą: nic nie wysłano” {#could-not-reach-this-pump-nothing-was-sent}

Polecenie do pompy Jecod albo Jebao nigdy nie wyszło z Cory. W telefonie komunikat brzmi *„Nie udało się połączyć z tą pompą. Musi być w tej samej sieci Wi-Fi co Twój telefon.”* Zwykle pompa jest wyłączona albo nie jest w swojej sieci.

1. Sprawdź, czy pompa jest włączona.
2. Sprawdź, czy jest w tej samej sieci, w której ją dodano, i czy telefon albo Cora Max też jest w tej sieci.
3. Dotknij **Spróbuj ponownie**.

### „Nie udało się połączyć z tą pompą przez Bluetooth. Podejdź bliżej i spróbuj ponownie.” {#could-not-reach-this-pump-over-bluetooth-stand-near-it-and-t}

Telefon jest poza zasięgiem pompy Jecod, która łączy się tylko przez Bluetooth. Podejdź bliżej pompy i dotknij **Spróbuj ponownie**.


### „Nie udało się połączyć z Apex: nic się nie zmieniło” / „nic nie zdozowano” {#could-not-reach-the-apex-nothing-changed-nothing-was-dosed}

Neptune Apex, Trident albo głowica DŌS nie odpowiedziały na polecenie albo prośbę o dawkę.

1. Otwórz własną aplikację Apex i sprawdź, czy jest online.
2. Sprawdź połączenie sieciowe telefonu albo Cora Max, którego używasz. Zmiana głowicy DŌS z telefonu wymaga telefonu w tej samej sieci co Apex.
3. Dotknij **Spróbuj ponownie**.

### „Nie udało się wysłać: … Ten Cora Max nie ma danych Apex” {#this-could-not-be-sent-no-device-on-this-tank-can-send-it}

Cora Max pokazuje to, gdy nie ma sposobu, żeby połączyć się z Twoim Apex, a żadne inne urządzenie w akwarium nie może wysłać polecenia za niego. Komunikat mówi, żeby dodać dane Apex w Ustawieniach, ale teraz ustawia się je w telefonie.

1. W telefonie otwórz **Urządzenia**, potem swój Apex, i sprawdź jego adres oraz dane logowania w **Połączenie**. Popraw je przez **Edytuj połączenie**.
2. Albo ustaw działający Cora Max jako **Główne Cora Max** dla tego akwarium: **Ustawienia**, otwórz akwarium, a potem **Główne Cora Max**.

### Karmienie nie uruchamia się z telefonu {#feed-does-not-start}

W telefonie **Karmienie** pokazuje się tylko przy akwarium z Neptune Apex i uruchamia jeden z cykli karmienia zaprogramowanych w Apex.

- *„Żadne urządzenie Cora w tym akwarium nie może połączyć się z Apex, a Ty nie jesteś w jego sieci.”* Dołącz do sieci Wi-Fi Apex albo sparuj Cora Max z akwarium.
- *„Apex nie odpowiedział, ale karmienie może już trwać.”* Sprawdź kontroler, zanim spróbujesz ponownie.


## Cora Max {#cora-max}

### Mój Cora Max jest offline {#my-cora-max-is-offline}

W telefonie jego wiersz w zakładce **Urządzenia** ma czerwoną kropkę. Gdy jest offline, sprzęt, który odczytuje, przestaje się aktualizować, możesz dostać alerty „przestał raportować” dla tego sprzętu, a polecenia wysłane z daleka mogą wracać jako *„Nic nie zostało wysłane”*.

1. Sprawdź, czy Cora Max ma zasilanie i czy ekran jest włączony.
2. Na Cora Max sprawdź **Ustawienia → Ustawienia Cora Max → Wi-Fi** i to, czy router działa.
3. Jeśli przy akwarium jest inny Cora Max, ustaw **Główne Cora Max** na **Każde aktywne (automatycznie)**, żeby mógł przejąć pracę. Zobacz [Więcej niż jedno urządzenie Cora](/help/mobile-multi-device#primary-cora-max).
4. Jeśli nie uruchamia się poprawnie, zobacz [Aktualizacje i odzyskiwanie](/help/max-updates).

:::tip Dowiedz się następnym razem
W Cora Mobile otwórz **Ustawienia → Automatyzacje** i utwórz regułę z wyzwalaczem **Gdy urządzenie traci połączenie**, wybierz swój Cora Max i dodaj akcję **Powiadom mnie**. Więcej w [Automatyzacjach i scenach](/help/mobile-automation).
:::

### Parowanie Cora Max się nie udaje {#pairing-a-cora-max-fails}

Cora Mobile znajduje nowy Cora Max przez Bluetooth, a potem przekazuje mu Twoją sieć Wi-Fi. Zanim zaczniesz, miej w Cora Mobile co najmniej jedno akwarium, włączony Bluetooth i telefon blisko ekranu. Jeśli parowanie zatrzyma się w połowie, Cora Mobile powie dlaczego, z przyciskami **Anuluj** i **Spróbuj ponownie** pod spodem.

- *„Bluetooth jest wyłączony. Włącz go, a potem dotknij Skanuj ponownie.”* Włącz Bluetooth i skanuj ponownie.
- *„Uprawnienie do Bluetooth jest wyłączone dla Cora. Włącz je w Ustawieniach, a potem dotknij Skanuj ponownie.”* Zezwól na Bluetooth dla Cora w ustawieniach telefonu. Przeniesie Cię tam **Ustawienia → Dostęp do urządzeń** w Cora Mobile.
- *„Nie znaleziono pobliskich urządzeń konfiguracyjnych Cora przez Bluetooth.”* Stań obok Cora Max, sprawdź, czy pokazuje ekran konfiguracji, i skanuj ponownie.
- **Nie znaleziono akwariów**: najpierw utwórz akwarium w Cora Mobile, a potem paruj.
- *„Twój telefon nie mógł połączyć się z Cora Max w sieci Wi-Fi.”* Podłącz telefon i Cora Max do tej samej sieci Wi-Fi. Na iPhonie sprawdź też, czy Cora ma dostęp do sieci lokalnej (**Ustawienia → Dostęp do urządzeń**). Potem dotknij **Spróbuj ponownie**.
- *„Cora Max nie zaakceptowało tej sesji parowania.”* Ponowna próba nie pomoże. Zamknij ekran i zacznij od nowa z **Urządzenia → Dodaj urządzenie → Cora**.

Przy każdym innym komunikacie dotknij **Spróbuj ponownie**. Całą konfigurację opisuje [Konfiguracja Cora Max](/help/max-setup).

### Cora Max pokazuje stare dane {#cora-max-shows-old-data}

Spójrz na etykietę stanu na górnym pasku. **Online** i **Chmura** są w porządku. Jeśli masz więcej niż jeden Cora Max, ten, który nie zbiera danych, pokazuje **Chmura**, a jego odczyty są tak samo aktualne. **Nieaktualne** albo **Offline** oznacza, że Cora Max stracił źródło i pokazuje ostatnie dane, które dostał.

- Sprawdź Wi-Fi w **Ustawienia → Ustawienia Cora Max → Wi-Fi**.
- Sprawdź, czy sama sieć działa.
- Jeśli etykieta pokazuje **Online** albo **Chmura**, a dane nadal są stare, problem jest przed Cora Max. Sprawdź to samo akwarium w telefonie.

### Cora Max pokazuje „Hasło Apex” {#cora-max-shows-apex-password}

Twój Apex odrzucił logowanie zapisane w Corze, zwykle dlatego, że zmieniono hasło Apex. W telefonie otwórz **Urządzenia**, potem swój Apex, i dotknij **Edytuj połączenie** w **Połączenie**, żeby wpisać nowe.

### „Apex odrzucił ten login” {#the-apex-refused-this-login}

Ten komunikat zobaczysz po dotknięciu **Dalej** przy dodawaniu albo edycji Neptune Apex. Cora wypróbowała login, który wpisano (jeśli wpisano hasło), potem fabryczny login Apex, a na końcu brak loginu, i Apex odrzucił wszystkie.

1. Dotknij **Anuluj**.
2. Sprawdź nazwę użytkownika i hasło ustawione w Apex, w **Network Setup**, **Login**. Jeśli Twój Apex nie ma logowania, zostaw oba pola puste.
3. Wpisz je ponownie i dotknij **Dalej**.

**Zapisz mimo to** zachowuje wpisane dane bez zaliczonego testu. Użyj tego tylko wtedy, gdy masz pewność, że login jest poprawny. Jeśli później zmienisz login w Apex, wpisz nowy tak, jak opisano w [Cora Max pokazuje „Hasło Apex”](#cora-max-shows-apex-password).

### Cora Max pokazuje „Zapis w chmurze odrzucony” {#cora-max-shows-cloud-save-refused}

Cora Cloud odmawia zapisania części danych z tego ekranu. Z Twoim akwarium ani z Cora Max nic złego się nie dzieje i nic nie trzeba zmieniać na ekranie. Rozwiązaniem jest aktualizacja Cora Cloud.

1. Otwórz **Ustawienia → Ustawienia Cora Max** i przewiń do **STAN**. Linia **Zapis w chmurze** mówi, które dane są odrzucane, na przykład odczyty albo gniazda urządzenia.
2. [Skontaktuj się z pomocą techniczną](/support.html) i powiedz nam, co mówi ta linia.

W międzyczasie odczyty nadal pokazują się na Cora Max. Po prostu nie są zapisywane na Twoim koncie, dopóki nie pojawi się poprawka.

### Drugi Cora Max pokazuje „Główne Cora offline” {#a-secondary-cora-max-shows-main-cora-offline}

Główne Cora Max tego akwarium przeszło w tryb offline. Ten ekran pokazuje ostatnie otrzymane dane, więc nie są na żywo.

1. Sprawdź zasilanie i Wi-Fi głównego Cora Max.
2. Poczekaj, aż połączy się ponownie, albo zmień **Główne Cora Max** na urządzenie, które jest online.

### Cora Max nie łączy się ponownie od razu po awarii Wi-Fi {#cora-max-wont-reconnect-right-away-after-a-wi-fi-outage}

Po utracie połączenia Cora Max czeka przed każdą kolejną próbą trochę dłużej, żeby nie zalewać Twojej sieci. Przerwa rośnie do około minuty.

1. Daj mu około minuty po tym, jak sieć wróci.
2. Jeśli nadal się nie połączył, sprawdź **Ustawienia → Ustawienia Cora Max → Wi-Fi**.

### Cora Max pokazuje „Bluetooth przestał działać” {#bluetooth-stopped-working}

Karta z tym tytułem zakrywa ekran: *Cora Max nie może połączyć się z Twoimi urządzeniami Bluetooth (oświetlenie, pompy, czujniki). Ponowne uruchomienie Cora Max rozwiązuje problem.* Pojawia się, gdy Bluetooth w Cora Max przestał działać i przywraca go tylko ponowne uruchomienie.

1. Dotknij **Uruchom ponownie**. Cora Max uruchomi się ponownie.
2. Jeśli to zły moment, dotknij **Później**. Karta znika na 30 minut i wraca, dopóki problem trwa.
3. Jeśli po dotknięciu **Uruchom ponownie** nic się nie restartuje, uruchom Cora Max ponownie, wyłączając i włączając jego zasilanie.

### Zmiana nazwy Cora Max w telefonie nie zmienia tego, co pokazuje {#renaming-a-cora-max-on-the-phone-doesnt-change-what-the-tabl}

Nazwa ustawiona w telefonie to etykieta tego urządzenia na koncie. Nazwa, którą Cora Max pokazuje na własnym ekranie parowania, może być inna.

1. Sprawdź, na którą nazwę patrzysz: tę z listy urządzeń w telefonie czy tę z ekranu parowania Cora Max.
2. Żeby zmienić etykietę na koncie, zmień nazwę z listy urządzeń w telefonie.

### Nie mogę znaleźć, gdzie wyłączyć słowo aktywujące {#i-cant-find-where-to-turn-off-the-wake-word-on-cora-max}

Słowo aktywujące jest w ustawieniach dźwięku, a nie w ustawieniach Cora Assistant.

1. Na Cora Max przejdź do **Ustawienia → Ustawienia Cora Max** i znajdź **Słowo aktywujące** w **DŹWIĘK I GŁOS**.
2. Wyłącz je. Nadal możesz dotknąć ikony **Cora Assistant**, żeby zacząć rozmowę.

Więcej w [Rozmowie z Corą](/help/max-voice).

### Blokada rodzicielska nie wpuszcza nikogo do Ustawień {#child-lock-wont-let-anyone-into-settings}

Tak działa blokada rodzicielska. Po określonym czasie bez dotyku nie pozwala nikomu przełączać sprzętu z tego ekranu, ani dotykiem, ani głosem. Odczyty dalej się aktualizują i nadal możesz zadawać Corze pytania. Żeby odblokować:

1. Naciśnij **Głośniej** albo **Ciszej** trzy razy w ciągu dwóch sekund, albo
2. Przytrzymaj pięć palców w prawym górnym rogu ekranu przez dziesięć sekund.

Więcej w [Ustawieniach Cora Max](/help/max-settings#child-lock).

### Scena utworzona w telefonie nie daje się edytować na Cora Max {#a-scene-made-on-the-phone-doesnt-show-up-as-editable-on-cora}

Tylko nowsze wersje Cora Max potrafią edytować sceny na ekranie. Starsze nadal uruchamiają sceny utworzone w telefonie, ale nie mogą ich edytować.

1. Zaktualizuj Cora Max ([Aktualizacje i odzyskiwanie](/help/max-updates)) albo
2. Edytuj tę scenę dalej w telefonie. I tak działa na Cora Max.

## Alerty, powiadomienia i codzienne podsumowanie {#alerts-and-notifications}

### Alert nie znika {#an-alert-is-not-clearing}

Alert znika, gdy odczyt wraca do zakresu. Jeśli nie znika, są trzy prawdopodobne powody.

- Odczyt naprawdę jest poza zakresem. Spójrz na historię widżetu.
- Zakres nie pasuje do Twojego akwarium. Zobacz [Alerty i progi](/help/mobile-alerts).
- Źródło jest nie w porządku. Sonda, która wymaga kalibracji, zgłasza liczbę, która naprawdę jest poza zakresem. Napraw sondę i nie ruszaj zakresu.

### Alert dalej powiadamia po potwierdzeniu {#an-alert-wont-stop-notifying-even-after-ive-acknowledged-it}

**Uśpij** i **Odrzuć** na Cora Max wyciszają tylko ten jeden Cora Max. Telefon dalej dostaje powiadomienia, dopóki odczyt jest poza zakresem.

1. Żeby słyszeć o nim rzadziej, otwórz regułę alertu w Cora Mobile i ustaw dłuższy **Czas wstrzymania między alertami** (do 1 tygodnia).
2. Jeśli zakres nie pasuje do Twojego akwarium, zmień sam zakres.

### Nie dostaję powiadomień {#im-not-getting-notifications}

1. W **Ustawienia → Powiadomienia** sprawdź, czy kategoria może wysyłać powiadomienia.
2. Sprawdź uprawnienie do powiadomień dla Cory w samym telefonie.
3. Codzienne podsumowanie milczy w dni, w które nic się nie zmieniło. Jeśli przestało przychodzić całkiem, zobacz następny wpis.

Więcej w [Powiadomieniach](/help/mobile-notifications).

### Codzienne podsumowanie przestało przychodzić {#my-daily-briefing-stopped}

- Okres próbny się skończył. Reef Buddy jest częścią płatnych planów. Po 30-dniowym okresie próbnym konto darmowe przestaje dostawać codzienne podsumowanie. Zobacz [Plany i subskrypcje](/help/mobile-plans).
- Akwarium nie jest objęte Twoim planem. Każdy plan obejmuje określoną liczbę akwariów, liczonych w kolejności z **Ustawienia → Zmień kolejność akwariów**. Przesuń akwarium wyżej, żeby je objąć.
- Dziś nic się nie zmieniło. W spokojny dzień podsumowanie milczy.

Więcej w [Reef Buddy](/help/mobile-reef-buddy).

### Alerty przychodzą z usuniętego akwarium {#alerts-from-a-removed-tank}

Usunięte akwarium jest zachowane ze względu na historię, ale nie wysyła alertów ani przypomnień, a jego automatyzacje się zatrzymują. Jeśli mimo to jakiś dostaniesz:

1. Otwórz **Ustawienia → Usunięte akwaria**. Jeśli akwarium nie ma na liście, nie zostało usunięte.
2. Zaktualizuj Cora Mobile i swój Cora Max do najnowszej wersji.
3. Alerty nadal przychodzą? Napisz do pomocy technicznej, podając treść alertu i godzinę. Zobacz [Zgłaszanie problemu](/help/mobile-support).

Więcej w [Zarządzaniu akwariami](/help/mobile-tanks).


## Cora Assistant i głos {#cora-assistant-and-voice}

### Cora Assistant odpowiada o niewłaściwym akwarium {#cora-assistant-answers-about-the-wrong-tank}

Przed pytaniem nie wybrano akwarium albo wybrane jest niewłaściwe. Wybierz akwarium, o które Ci chodzi, i zapytaj ponownie. Więcej w [Pytaniach do Cory](/help/mobile-assistant).

### Cora Assistant odmawia odpowiedzi albo znów pokazuje ekran zgody {#cora-assistant-refuses-to-answer-or-shows-a-consent-screen-a}

**Pozwól Cora Assistant korzystać z zapisanych danych akwarium** jest wyłączone, więc nie ma na czym oprzeć odpowiedzi. Dotknij **Zgadzam się i kontynuuję** na ekranie zgody albo włącz przełącznik w **Ustawienia → Cora Assistant**.

### Cora Max pokazuje „Głos wymaga Twojej zgody” {#voice-needs-your-ok}

Głos na Cora Max korzysta z tego samego wyboru udostępniania danych co Cora Assistant w telefonie. W Cora Mobile otwórz **Ustawienia → Cora Assistant** i włącz **Pozwól Cora Assistant korzystać z zapisanych danych akwarium**, a potem spróbuj ponownie. Więcej w [Rozmowie z Corą](/help/max-voice).

## Wyniki z laboratorium i raporty zdrowia {#lab-results-and-health-reports}

### Wynik ICP od laboratorium albo z e-maila nigdy się nie pojawił {#a-lab-or-emailed-icp-result-never-showed-up}

Wynik zostaje dołączony dopiero wtedy, gdy ma akwarium. Czasem Cora musi też rozpoznać nadawcę i potrzebuje Twojej zgody, żeby go odczytać.

1. Jeśli widzisz *„Cora Assistant potrzebuje Twojej zgody, aby go odczytać.”*, otwórz **Ustawienia → Cora Assistant** i włącz **Pozwól Cora Assistant korzystać z zapisanych danych akwarium**. Wynik dotrze, gdy się zgodzisz.
2. Sprawdź podpowiedź, którą Cora pokazuje, gdy pierwszy raz wysyłasz jej wynik.
3. Gdy Cora zapyta, potwierdź, do którego akwarium należy wynik.
4. Jeśli wysyłano już wcześniej wynik, wyślij ten z tego samego adresu e-mail.

Więcej w [ICP i raportach zdrowia](/help/mobile-icp-health).

### Plik ICP nie chce się przesłać {#my-icp-file-wont-upload}

Cora odczytuje raport PDF, który przysyła laboratorium. Zdjęć i zrzutów ekranu nie da się odczytać. Najpierw pobierz PDF od laboratorium, a potem znów dotknij **Przesłać ICP**.

### Ekran robi się czarny po raporcie zdrowia albo przesłaniu ICP {#black-screen-after-a-report}

Mogło się to zdarzać w Cora Mobile 1.2 i wcześniejszych, a Cora Mobile 1.3 to naprawia: zaktualizuj Cora Mobile z App Store albo Google Play. Jeśli zobaczysz to przed aktualizacją, zamknij Cora Mobile i otwórz ją ponownie. Raport został zapisany i znajdziesz go w **Inteligencja**.

## Język, jednostki i logowanie {#language-units-and-signing-in}

### Wszystko nagle jest w złym języku {#everything-is-suddenly-in-the-wrong-language}

Ktoś zmienił język konta na jednym z Twoich urządzeń. To jedno ustawienie dla całego konta.

1. Otwórz **Ustawienia → Język** w Cora Mobile albo na Cora Max.
2. Ustaw go z powrotem. Zmiana działa wszędzie.

### Stary alert albo raport jest w innym języku po zmianie {#an-old-alert-or-report-is-still-in-a-different-language-afte}

Tak ma być. Cora nie tłumaczy ponownie niczego, co już napisała. Nowe alerty, raporty i podsumowania są w nowym języku.

### „Nie udało się połączyć z Cora. Sprawdź Wi-Fi lub dane mobilne i spróbuj ponownie.” {#could-not-reach-cora-check-your-wi-fi-or-mobile-data-then-tr}

Telefon nie może połączyć się z Cora Cloud, żeby się zalogować. Chodzi o połączenie telefonu, a nie o sprzęt akwarium.

1. Sprawdź, czy telefon ma działające Wi-Fi albo dane mobilne.
2. Spróbuj innej sieci, jeśli masz.
3. Dotknij **Spróbuj ponownie**.

Inne problemy z logowaniem opisuje [Logowanie i odzyskiwanie konta](/help/mobile-account).

## Nadal problem {#still-stuck}

Napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** albo zgłoś problem z Cora Mobile, jak opisuje [Zgłaszanie problemu](/help/mobile-support). Podaj, które akwarium, które urządzenie, który ekran i czego się spodziewano.

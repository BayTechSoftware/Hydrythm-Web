---
title: Rozwiązywanie problemów
description: Odczyty przestały napływać, urządzenie jest offline, alert nie znika albo coś wygląda nie tak. Zacznij tutaj.
section: Help
reviewed: 2026-09-30
order: 1
---

Znajdź na liście objaw, który widzisz.

## Widżet nie pokazuje wartości

Sprawdź po kolei:

1. **Wiek odczytów na sąsiednich widżetach.** Jeśli wszystkie są nieaktualne, problem dotyczy połączenia, a nie parametru.
2. **Zakładkę Urządzenia.** Jeśli z urządzeniem nie ma połączenia, zobaczysz to w jego wierszu.
3. **Przypisanie do akwarium.** Urządzenie, które wysyła dane do niewłaściwego akwarium, wygląda dokładnie tak jak urządzenie, które nic nie wysyła. Otwórz urządzenie i sprawdź, do którego akwarium jest przypisane.
4. **Czy źródło w ogóle istnieje.** Odczytu fosforanów nie będzie, jeśli nie masz sprzętu, który je mierzy, ani nie wpisujesz ich ręcznie.

## Odczyt jest nieaktualny

Wiek odczytu mówi prawdę: nic nowego nie dotarło.

- **Parametry wpisywane ręcznie** stają się nieaktualne, gdy nikt nie wpisał nowego odczytu. Zapisz nowy wynik.
- **Odczyty ze sprzętu** stają się nieaktualne, gdy urządzenie przestało wysyłać dane. Sprawdź jego wiersz w **Urządzenia**.
- **Niektóre urządzenia z założenia mierzą rzadko.** Titrator, który mierzy raz na godzinę, zwykle pokazuje `1h`. To nie jest błąd.

## Nie ma połączenia z urządzeniem

Zwykle winna jest sieć.

1. Czy sprzęt jest włączony i działa w swojej aplikacji?
2. Czy jest w tej samej sieci, w której go dodano?
3. Czy zmienił się router (nowy sprzęt, nowa nazwa sieci, izolacja sieci dla gości)?

Sprzęt, który łączy się przez sieć lokalną, musi być w niej dostępny. Sprzęt, który łączy się przez konto producenta, nie musi, ale to konto musi być nadal ważne.

## Urządzenie zgłasza odrzucone logowanie

Producent odrzucił zapisane dane logowania. Prawie zawsze dlatego, że hasło do konta u producenta zostało zmienione.

Otwórz wiersz urządzenia i zaloguj się ponownie.

## Parowanie Cora Max się nie udaje

Jeśli dodawanie Cora Max zatrzyma się w połowie, Cora Mobile pokaże, który krok się nie udał i dlaczego. Pod komunikatem są przyciski **Anuluj** i **Spróbuj ponownie**.

- *„Twój telefon nie mógł połączyć się z Cora Max w sieci Wi-Fi.”* Połącz telefon i Cora Max z tą samą siecią Wi-Fi. Na iPhonie sprawdź też, czy Cora ma dostęp do sieci lokalnej. Przejdziesz tam przez **Ustawienia → Dostęp do urządzeń** (więcej w [Ustawienia](/help/mobile-settings)). Potem dotknij **Spróbuj ponownie**.
- *„Cora Max nie zaakceptowało tej sesji parowania.”* Ponowna próba nic nie da. Zamknij ekran i zacznij od nowa w **Urządzenia → Dodaj urządzenie → Cora**.

Przy każdym innym komunikacie dotknij **Spróbuj ponownie**.

## Cora Max pokazuje stare dane

Sprawdź plakietkę stanu na górnym pasku. **Online** i **Chmura** oznaczają, że wszystko działa. Gdy masz kilka urządzeń Cora, ekran, który nie zbiera danych, pokazuje **Chmura**, a jego odczyty są tak samo aktualne. **Nieaktualne** albo **Offline** oznacza, że ekran stracił źródło danych i pokazuje ostatnie, które dostał. Tak ma być, ale te dane nie są aktualne.

- Sprawdź Wi-Fi w **Ustawienia → Ustawienia Cora Max → Wi-Fi**
- Sprawdź, czy sama sieć działa
- Jeśli plakietka pokazuje **Online** albo **Chmura**, a dane dalej są stare, problem leży wcześniej. Sprawdź to samo akwarium na telefonie

## Alert nie znika

Alert znika, gdy odczyt wróci do zakresu. Jeśli tak się nie dzieje:

- **Odczyt naprawdę jest poza zakresem.** Sprawdź historię widżetu.
- **Próg nie pasuje do Twojego akwarium.** Więcej w [Alerty i progi](/help/mobile-alerts).
- **Źródło podaje złą wartość.** Sonda, która wymaga kalibracji, podaje liczbę, która faktycznie jest poza zakresem. Popraw sondę, a nie próg.

## Dwa źródła pokazują co innego

To znak, że Cora działa, a nie że coś się zepsuło. Gdy sonda i test kropelkowy pokazują co innego, to prawdziwa informacja o Twoim systemie.

Wynik ICP może być tu przydatną trzecią opinią, ale nie rozstrzyga sporu. Laboratoria różnią się między sobą, a na wynik wpływa to, jak próbkę pobrano i przewieziono. Dwa zgodne testy są warte o wiele więcej niż jeden.

Zwykle trzeba skalibrować sondę. Czasem test kropelkowy jest przeterminowany. Skalibruj sondę, zrób test jeszcze raz ze świeżym odczynnikiem i porównaj oba wyniki w tych samych warunkach. [Wynik ICP](/help/mobile-icp-health) będzie trzecim punktem odniesienia.

## Nie dostaję powiadomień

1. W **Ustawienia → Powiadomienia** sprawdź, czy ta kategoria może wysyłać powiadomienia push
2. Sprawdź w ustawieniach telefonu, czy Cora ma zgodę na powiadomienia
3. Pamiętaj, że w dni, gdy nic się nie zmieniło, codzienny briefing celowo milczy

## Dlaczego coś się zmieniło

**Ustawienia → Aktywność** pokazuje każde przełączenie gniazda, karmienie, dawkę i zmianę wtyczki. Przy każdym wpisie widać, skąd przyszło polecenie: z Cora Mobile, z ekranu Cora, głosem, od Asystenta, z reguły automatyzacji, z inteligentnego przycisku albo z Twojego konta.

## Pulpit wygląda źle po edycji

Wczytaj zapisany układ. Otwórz **Moje panele** i wybierz jeden z nich.

Jeśli nie masz zapisanego układu, ułóż pulpit od nowa i zapisz go. Potem powrót do niego zajmie jedno dotknięcie.

Odczyty, historia i wpisy w dzienniku są przechowywane osobno od układu, więc nic z nich nie przepadnie.

## „Odczyty Red Sea przestały się aktualizować”

Żadne urządzenie w sieci tego akwarium nie odpytuje teraz sprzętu Red Sea, więc odczyty na ekranie się nie odświeżają.

1. Otwórz **Ustawienia → Główne Cora Max** i sprawdź, czy jest ustawiony Cora Max (albo wybrana opcja **Każde aktywne (automatycznie)**).
2. Otwórz akwarium na urządzeniu, które jest w tej samej sieci Wi-Fi co sprzęt Red Sea.
3. Sprawdź, czy sprzęt Red Sea jest włączony i online w swojej aplikacji.

Jeśli to nie pomoże, napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** i podaj nazwę akwarium i urządzenia.

## „GHL API jest wyłączone”

GHL wyłącza swoje oficjalne API po każdej aktualizacji firmware, więc to normalne po aktualizacji, a nie usterka. Włącz je z powrotem w **System → GHL API** w GHL Control Center albo GHL Connect, bezpośrednio na kontrolerze. Cora sprawdza to na bieżąco i sama połączy się ponownie, gdy tylko API wróci.

## „Kontroler GHL jest nieosiągalny”

Cora Max nie może dotrzeć do adresu IP kontrolera w Twojej sieci.

1. Sprawdź, czy kontroler jest włączony i podłączony do Twojej sieci.
2. Sprawdź, czy jego adres IP się nie zmienił. Jeśli tak, otwórz je na telefonie (**Urządzenia**) i zaktualizuj w sekcji **Połączenie**.
3. Sprawdź, czy Cora Max obsługujący to akwarium jest w tej samej sieci co kontroler.

Jeśli to nie pomoże, napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** i podaj nazwę akwarium i urządzenia.

## Kontroler HYDROS pokazuje się jako offline albo nie zgłasza danych

HYDROS raportuje przez własną chmurę, więc zwykle oznacza to, że sam kontroler stracił zasilanie albo własne połączenie sieciowe, a nie że problem leży po stronie Cory. Sprawdź go w aplikacji HYDROS. Odczyty w Corze nadrobią zaległości, gdy kontroler wróci do sieci, a polecenie wysłane, gdy wygląda na offline, w ogóle nie zostanie wysłane.

Jeśli urządzenie HYDROS pokazuje **Klucz odwołany**, jego klucz urządzenia został usunięty albo zastąpiony w aplikacji HYDROS. Utwórz nowy klucz i połącz go ponownie z **Urządzenia → Dodaj HYDROS (Beta)** albo z poziomu ustawień akwarium na Cora Max.

## „Nie udało się połączyć z tą pompą: nic nie wysłano”

Polecenie do pompy Jecod albo Jebao w ogóle nie zostało wysłane. Zwykle pompa jest wyłączona albo nie ma jej w sieci.

1. Sprawdź, czy pompa jest włączona.
2. Sprawdź, czy jest w tej samej sieci, w której ją dodano.
3. Dotknij **Spróbuj ponownie**.

Jeśli to nie pomoże, napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** i podaj nazwę akwarium i urządzenia.

## „Nie udało się połączyć z tą pompą przez Bluetooth. Podejdź bliżej i spróbuj ponownie.”

Pompa Jecod, która łączy się tylko przez Bluetooth, jest poza zasięgiem telefonu.

1. Podejdź bliżej do pompy.
2. Dotknij **Spróbuj ponownie**.

Jeśli to nie pomoże, napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** i podaj nazwę akwarium i urządzenia.

## „Nie udało się połączyć z tym Gyre. Żadne karmienie nie zostało rozpoczęte.”

Pompa Maxspect Gyre (integracja w wersji beta) nie odpowiedziała, gdy Cora próbowała włączyć na niej tryb karmienia.

1. Sprawdź, czy pompa jest włączona i jest w swojej sieci.
2. Dotknij **Spróbuj ponownie**.

Jeśli to nie pomoże, napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** i podaj nazwę akwarium i urządzenia.

## „Nie udało się połączyć z tym Gyre. Jego program nie został zmieniony.”

Harmonogram nie dotarł do pompy Maxspect Gyre (integracja w wersji beta).

1. Sprawdź, czy telefon albo Cora Max jest w tej samej sieci co pompa.
2. Dotknij **Spróbuj ponownie** na ekranie harmonogramu.

Jeśli to nie pomoże, napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** i podaj nazwę akwarium i urządzenia.

## „Nie udało się połączyć z Apex: nic się nie zmieniło” albo „nic nie zdozowano”

Neptune Apex, Trident albo głowica DŌS nie odpowiedziały na polecenie albo na prośbę o dawkę.

1. Otwórz aplikację Apex i sprawdź, czy urządzenie jest online.
2. Sprawdź połączenie z siecią na urządzeniu, którego używasz.
3. Dotknij **Spróbuj ponownie**.

Jeśli to nie pomoże, napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** i podaj nazwę akwarium i urządzenia.

## „Nie można tego wysłać: żadne urządzenie w tym akwarium nie może tego wysłać”

Żadne urządzenie Cora w tym akwarium nie ma danych połączenia z Apex potrzebnych do wykonania polecenia albo urządzenie, które je ma, jest offline.

1. Dodaj dane Apex w **Ustawienia** na urządzeniu, które jest teraz online, albo
2. Ustaw inny, działający Cora Max jako **Główne Cora Max** dla tego akwarium.

Jeśli to nie pomoże, napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** i podaj nazwę akwarium i urządzenia.

## Dodatkowy Cora Max pokazuje „Główne Cora offline”

Główny tablet tego akwarium jest offline, więc ten dodatkowy ekran pokazuje ostatnie dane, które dostał, a nie dane na żywo.

1. Sprawdź zasilanie i Wi-Fi głównego tabletu.
2. Poczekaj, aż znów się połączy, albo ustaw jako **Główne Cora Max** urządzenie, które jest teraz online.

Jeśli to nie pomoże, napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** i podaj nazwę akwarium i urządzenia.

## „Urządzenie jest offline. Wyświetlany jest ostatni znany stan.”

To zwykła obsługa braku połączenia. Urządzenie przestało wysyłać dane, a Cora pokazuje ostatnie wartości i nie udaje, że są aktualne.

1. Sprawdź połączenie urządzenia z siecią.
2. Pamiętaj, że pokazane wartości nie są na żywo, dopóki w wierszu urządzenia widać offline.

Jeśli to nie pomoże, napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** i podaj nazwę akwarium i urządzenia.

## Niektóre ustawienia ReefBeat są wyszarzone albo ich brakuje

Tak ma być, to nie błąd. Ustawienia samego urządzenia (w odróżnieniu od odczytów) otwierają się tylko wtedy, gdy telefon jest w tej samej sieci co urządzenie. Poza tą siecią widać tylko odczyty.

1. Żeby zmienić te ustawienia, połącz się z siecią Wi-Fi, w której jest akwarium.
2. Odczyty i historia działają normalnie także poza domem.

Jeśli to nie pomoże, napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## „Nie udało się połączyć z Cora. Sprawdź Wi-Fi lub dane mobilne i spróbuj ponownie.”

Podczas logowania telefon nie ma działającego połączenia z Cora Cloud. Problem dotyczy połączenia samego telefonu, a nie sprzętu w akwarium.

1. Sprawdź, czy telefon ma działające Wi-Fi albo dane mobilne.
2. Jeśli możesz, spróbuj innej sieci.
3. Dotknij **Spróbuj ponownie**.

Jeśli to nie pomoże, napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Wszystko nagle jest w innym języku

Ktoś zmienił język konta na jednym z urządzeń. Język to jedno ustawienie dla całego konta, a nie dla pojedynczego urządzenia.

1. Otwórz **Ustawienia → Język** w Cora Mobile albo na Cora Max.
2. Jeśli język zmieniono przez pomyłkę, przywróć poprzedni. Zmiana od razu zadziała wszędzie.

Jeśli to nie pomoże, napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Stary alert albo raport jest w innym języku po zmianie

Tak ma być, to nie błąd. Cora nie tłumaczy ponownie treści, które już powstały. Tylko nowe alerty, raporty i briefingi są w nowym języku.

1. Nie trzeba nic naprawiać. Nowe treści będą już w aktualnym języku.

Jeśli masz inne pytania, napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Alert dalej powiadamia, chociaż został potwierdzony

**Uśpij** i **Odrzuć** na Cora Max wyciszają alert tylko na tym jednym Cora Max. Telefon dalej dostaje powiadomienia, dopóki odczyt jest poza zakresem.

1. Żeby telefon powiadamiał Cię rzadziej, otwórz regułę alertu w Cora Mobile i ustaw dłuższy **Czas wstrzymania między alertami** (najwyżej 1 tydzień).
2. Jeśli próg nie pasuje do Twojego akwarium, zmień sam próg.

Jeśli to nie pomoże, zajrzyj do [Alerty i progi](/help/mobile-alerts) albo napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Dawka zatrzymała się w połowie i pojawił się alert o przywróceniu

Głowica DŌS straciła połączenie w trakcie dawki. Cora celowo o tym informuje i nie zakłada, że cała dawka została podana.

1. Otwórz alert i sprawdź, ile płynu faktycznie podano, zanim dawka się zatrzymała.
2. Wznów albo popraw dawkę na podstawie tej ilości, a nie ilości zaplanowanej na początku.

Jeśli to nie pomoże, napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** i podaj nazwę akwarium i urządzenia.

## Scena utworzona na telefonie nie daje się edytować na Cora Max

Edytowanie scen bezpośrednio na tablecie to nowsza funkcja Cora Max. Starsze oprogramowanie uruchomi sceny utworzone na telefonie, ale nie pozwoli ich tam edytować.

1. Zaktualizuj Cora Max albo
2. Edytuj tę scenę dalej na telefonie. Na tablecie i tak będzie działać.

Jeśli to nie pomoże, zajrzyj do [Aktualizacje i tryb odzyskiwania](/help/max-updates) albo napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Assistant odpowiada o niewłaściwym akwarium

Przed pytaniem nie wybrano akwarium albo aktywne jest niewłaściwe akwarium.

1. Najpierw wybierz akwarium, o które chodzi.
2. Zadaj pytanie jeszcze raz.

Jeśli to nie pomoże, zajrzyj do [Asystent](/help/mobile-assistant) albo napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Assistant nie odpowiada albo znowu pokazuje ekran zgody

Opcja **Pozwól Cora Assistant korzystać z zapisanych danych akwarium** jest wyłączona, więc Asystent nie ma danych, na których może się oprzeć.

1. Na ekranie zgody dotknij **Zgadzam się i kontynuuję**, żeby ją z powrotem włączyć.

Jeśli to nie pomoże, zajrzyj do [Asystent](/help/mobile-assistant) albo napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Wynik ICP z laboratorium albo z e-maila się nie pojawił

Zanim wynik trafi do Cory, trzeba wybrać dla niego akwarium. Czasem Cora musi też rozpoznać nadawcę.

1. Przeczytaj wskazówkę, która pojawia się przy pierwszym wysłaniu wyniku do Cory.
2. Gdy Cora zapyta, wybierz akwarium, do którego ma trafić wynik.
3. Jeśli już wcześniej wysyłano takie wyniki, sprawdź, czy e-mail wyszedł z tego samego adresu co poprzednio.

Jeśli to nie pomoże, zajrzyj do [ICP i raporty zdrowia](/help/mobile-icp-health) albo napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Powiadomienie o wyniku ICP z e-maila nie podaje nazwy laboratorium

To znany błąd: w powiadomieniu push z przyciskiem **Wybierz zbiornik** brakowało nazwy laboratorium. W aktualnych wersjach jest już poprawiony.

1. Zaktualizuj Cora Mobile do najnowszej wersji.
2. Sam wynik jest w porządku. Nazwy brakowało tylko w tekście powiadomienia.

Jeśli to nie pomoże, napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Widżet pokazuje złe jednostki

To ustawienie jednostek akwarium, a nie problem z danymi. Wartości są zapisywane tak samo bez względu na to, jak są wyświetlane.

1. Otwórz **Ustawienia** tego akwarium i sprawdź jednostki.
2. Zmień je tam. Każdy telefon i każdy Cora Max, który pokazuje to akwarium, dostosuje się do zmiany.

Jeśli to nie pomoże, napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Wskaźnik albo próg wygląda inaczej po zmianie jednostek

Tak ma być. Wskaźniki, kafelki i historia są rysowane od nowa w wybranej jednostce. Same wartości się nie zmieniły.

1. Nie trzeba nic naprawiać. Zmienił się tylko wygląd.

Jeśli masz inne pytania, napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Max nie łączy się od razu po awarii Wi-Fi

Po utracie połączenia Cora Max przed każdą kolejną próbą czeka trochę dłużej, żeby nie przeciążać sieci. Odstęp rośnie mniej więcej do minuty.

1. Gdy sieć wróci, poczekaj około minuty.
2. Jeśli po tym czasie Cora Max dalej nie ma połączenia, sprawdź Wi-Fi w **Ustawienia → Ustawienia Cora Max → Wi-Fi**.

Jeśli to nie pomoże, zajrzyj do [Ekran główny Cora Max](/help/max-tour) albo napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Zmiana nazwy Cora Max na telefonie nie zmienia nazwy na tablecie

Nazwa ustawiona na telefonie to etykieta urządzenia na koncie. Nazwa, którą tablet pokazuje podczas parowania, może być inna.

1. Sprawdź, o którą nazwę chodzi: tę z listy urządzeń na telefonie czy tę z ekranu parowania na tablecie.
2. Jeśli chcesz zmienić etykietę na koncie, zmień nazwę na liście urządzeń w telefonie.

Jeśli to nie pomoże, napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** i podaj nazwę urządzenia.

## Gdzie wyłączyć frazę aktywującą na Cora Max

Przełącznik frazy aktywującej jest w sekcji **Dźwięk i głos**, a nie w ustawieniach Cora Assistant. Wiele osób się tego nie spodziewa.

1. Przejdź do **Ustawienia → Ustawienia Cora Max → Dźwięk i głos → Nasłuchiwanie słowa aktywującego**.
2. Wyłącz je. Sesję głosową dalej zaczniesz, dotykając ikony Cora.

Jeśli to nie pomoże, zajrzyj do [Ustawienia Cora Max](/help/max-settings) albo napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Blokada rodzicielska nie pozwala wejść do Ustawień

Tak właśnie działa blokada rodzicielska. Po ustalonym czasie bez dotyku nikt nie przełączy sprzętu z tego ekranu, ani dotykiem, ani głosem. Odczyty dalej się aktualizują, a Corę nadal możesz o coś zapytać.

1. Naciśnij przycisk głośności (w górę albo w dół) trzy razy w ciągu dwóch sekund albo
2. Przytrzymaj pięć palców w prawym górnym rogu ekranu przez dziesięć sekund.

Jeśli to nie pomoże, zajrzyj do [Rozmowa z Corą na Cora Max](/help/max-voice) albo napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Nadal nie działa?

Napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**. Podaj, którego akwarium i którego ekranu dotyczy problem i co spodziewasz się zobaczyć. Dzięki temu szybciej dostaniesz pomocną odpowiedź.

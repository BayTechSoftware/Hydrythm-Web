---
title: Rozwiązywanie problemów
description: Odczyty się zatrzymały, urządzenie przeszło offline, alerty nie gasną, albo coś wygląda nie tak. Zacznij tutaj.
section: Help
reviewed: 2026-09-27
order: 1
---

Zacznij od symptomu.

## Widżet nie pokazuje wartości

Przejdź przez tę listę:

1. **Sprawdź wiek pobliskich widżetów.** Jeśli wszystko jest nieaktualne, problem jest w połączeniu, nie w parametrze.
2. **Otwórz zakładkę Devices.** Urządzenie, którego nie można dosięgnąć, mówi to wprost w swoim wierszu.
3. **Sprawdź przypisanie akwarium.** Urządzenie zgłaszające się do złego akwarium wygląda tak samo jak urządzenie, które się nie zgłasza. Otwórz urządzenie i potwierdź jego akwarium.
4. **Sprawdź, czy źródło istnieje.** Nic nie zgłasza fosforanu, jeśli nie masz sprzętu, który go mierzy, albo nie zapisujesz go ręcznie.

## Odczyt jest nieaktualny

Plakietka wieku mówi Ci prawdę: nic nowego nie przyszło.

- **Parametry zapisywane ręcznie** stają się nieaktualne, gdy żaden odczyt nie został wpisany. Zapisz jeden.
- **Odczyty sprzętu** stające się nieaktualne znaczą, że urządzenie przestało się zgłaszać; sprawdź jego wiersz w **Urządzenia**.
- **Część sprzętu jest z założenia wolna.** Tytrator, który mierzy co godzinę, normalnie pokazuje `1h`. To nie jest usterka.

## Nie można dosięgnąć urządzenia

Zwykle sieć.

1. Czy sprzęt jest zasilany i działa we własnej aplikacji?
2. Czy jest w tej samej sieci, w której został dodany?
3. Czy Twój router się zmienił (nowy sprzęt, nowa nazwa sieci, izolacja sieci gościnnej)?

Sprzęt łączący się przez Twoją lokalną sieć musi być dostępny w tej sieci. Sprzęt łączący się przez konto producenta nie musi, ale wymaga, aby to konto było wciąż prawidłowe.

## Urządzenie mówi, że logowanie zostało odmówione

Producent odrzucił zapisane logowanie. Prawie zawsze bo zmieniłeś hasło u niego.

Otwórz wiersz urządzenia i zaloguj się ponownie.

## Parowanie Cora Max się nie powodzi

Jeśli dodawanie Cora Max zatrzymuje się w połowie, Cora Mobile mówi, który krok się nie powiódł i czemu, z **Anuluj** i **Spróbuj ponownie** poniżej.

- *"Your phone could not reach the Cora Max on your Wi-Fi."* Umieść swój telefon i Cora Max w tej samej sieci Wi-Fi. Na iPhone sprawdź też, czy Cora ma dostęp do sieci lokalnej: **Ustawienia → Dostęp do urządzeń** przenosi Cię tam (zobacz [Ustawienia](/help/mobile-settings)). Potem dotknij **Spróbuj ponownie**.
- *"The Cora Max did not accept this pairing session."* Ponowna próba nie pomoże. Zamknij ekran i zacznij od nowa z **Urządzenia → Dodaj urządzenie**.

Dla każdej innej wiadomości dotknij **Spróbuj ponownie**.

## Cora Max pokazuje stare dane

Sprawdź plakietkę stanu na górnym pasku. **Online** i **Chmura** są obie sprawne: z więcej niż jednym Cora, ekran, który nie zbiera danych, pokazuje **Chmura**, a jego odczyty są równie aktualne. **Nieaktualne** albo **Offline** znaczy, że ekran utracił swoje źródło i pokazuje ostatnie otrzymane dane (prawidłowe zachowanie, ale nie aktualne).

- Sprawdź Wi-Fi w **Ustawienia → Cora Max → Network**
- Sprawdź, czy sama sieć działa
- Jeśli plakietka pokazuje **Online** albo **Chmura**, a dane wciąż są stare, problem jest wcześniej w łańcuchu: sprawdź to samo akwarium na telefonie

## Alert nie gaśnie

Alert gaśnie, gdy odczyt wraca do zakresu. Jeśli nie gaśnie:

- **Odczyt naprawdę jest poza zakresem.** Spójrz na historię widżetu.
- **Próg jest niewłaściwy dla Twojego akwarium.** Zobacz [Alerty i progi](/help/mobile-alerts).
- **Źródło jest błędne.** Sonda wymagająca kalibracji zgłasza liczbę, która naprawdę jest poza zakresem. Napraw sondę, nie próg.

## Dwa źródła się nie zgadzają

To Cora działająca prawidłowo, nie Cora zawodząca. Gdy Twoja sonda i Twój test kroplowy się nie zgadzają, jest to prawdziwy fakt o Twoim systemie.

Wynik ICP jest tutaj użyteczną trzecią opinią, ale nie rozstrzyga sporu: laboratoria różnią się między sobą, a obsługa i transport próbki wpływają na wynik. Dwa zgadzające się testy są warte znacznie więcej niż jeden.

Zwykle sonda wymaga kalibracji; czasem test kroplowy jest stary. Skalibruj sondę, wykonaj test ponownie ze świeżym reagentem i porównaj obydwa w tych samych warunkach. [Wynik ICP](/help/mobile-icp-health) dodaje trzeci punkt danych do tego porównania.

## Nie otrzymuję powiadomień

1. **Ustawienia → Powiadomienia**: sprawdź, czy ta kategoria może wysyłać push
2. Sprawdź własne uprawnienia powiadomień Twojego telefonu dla Cory
3. Pamiętaj, że codzienny briefing jest celowo cichy w dniach, gdy nic się nie zmieniło

## Ustalanie, czemu coś się zmieniło

**Ustawienia → Aktywność** wypisuje każde przełączenie gniazda, karmienie, dawkę i zmianę wtyczki, wraz z tym, co o to poprosiło: Cora Mobile, ekran Cora, głos, Asystent, reguła automatyzacji, smart przycisk albo Twoje konto.

## Mój pulpit wygląda źle po edycji

Wczytaj zapisany projekt: **Moje panele**, potem wybierz jeden.

Jeśli żadnego nie zapisałeś, zbuduj układ od nowa, a potem zapisz go jako projekt. Od tego momentu powrót do niego to jedno dotknięcie.

W każdym razie odczyty, historia i wpisy dziennika są przechowywane odrębnie od układu, więc nic za pulpitem nie jest utracone.

## "Red Sea readings have stopped updating"

**Co to znaczy:** Żadne urządzenie w sieci tego akwarium nie odpytuje obecnie Twojego sprzętu Red Sea, więc odczyty na ekranie nie zostały odświeżone.

**Co robić:**
1. Otwórz **Ustawienia → Główne Cora Max** i sprawdź, czy Cora Max jest ustawione (albo wybrane jest **Każde aktywne (automatycznie)**).
2. Otwórz akwarium na urządzeniu w tej samej sieci Wi-Fi co sprzęt Red Sea.
3. Potwierdź, że sprzęt Red Sea jest zasilany i online w swojej własnej aplikacji.

**Wciąż nie działa?** Wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** z nazwą akwarium i urządzenia.

## "Could not reach this pump: nothing was sent"

**Co to znaczy:** Polecenie do pompy Jecod albo Jebao nigdy nie opuściło aplikacji, zwykle bo pompa jest wyłączona albo poza swoją siecią.

**Co robić:**
1. Sprawdź, czy pompa jest zasilana.
2. Sprawdź, czy jest w tej samej sieci, w której została dodana.
3. Dotknij **Spróbuj ponownie**.

**Wciąż nie działa?** Wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** z nazwą akwarium i urządzenia.

## "Nie udało się połączyć z tą pompą przez Bluetooth. Podejdź bliżej i spróbuj ponownie."

**Co to znaczy:** Urządzenie Jecod tylko Bluetooth jest poza zasięgiem Twojego telefonu.

**Co robić:**
1. Podejdź bliżej do pompy.
2. Dotknij **Spróbuj ponownie**.

**Wciąż nie działa?** Wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** z nazwą akwarium i urządzenia.

## "Nie udało się połączyć z tym Gyre. Żadne karmienie nie zostało rozpoczęte."

**Co to znaczy:** Gyre Maxspect (integracja beta) nie odpowiedziało, gdy Cora próbowała uruchomić na nim tryb karmienia.

**Co robić:**
1. Sprawdź, czy gyre jest zasilane i w swojej sieci.
2. Dotknij **Spróbuj ponownie**.

**Wciąż nie działa?** Wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** z nazwą akwarium i urządzenia.

## "Nie udało się połączyć z tym Gyre. Jego program nie został zmieniony."

**Co to znaczy:** Wysłanie harmonogramu do gyre Maxspect (integracja beta) nie dosięgło go.

**Co robić:**
1. Sprawdź, czy Twój telefon albo Cora Max jest w sieci gyre.
2. Dotknij **Spróbuj ponownie** z ekranu harmonogramu.

**Wciąż nie działa?** Wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** z nazwą akwarium i urządzenia.

## "Could not reach the Apex: nothing changed" / "nothing was dosed"

**Co to znaczy:** Neptune Apex, Trident albo głowica DŌS nie odpowiedziały na polecenie albo prośbę o dawkę.

**Co robić:**
1. Otwórz własną aplikację Apex i potwierdź, że jest online.
2. Sprawdź połączenie sieciowe na używanym urządzeniu.
3. Dotknij **Spróbuj ponownie**.

**Wciąż nie działa?** Wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** z nazwą akwarium i urządzenia.

## "This could not be sent: no device on this tank can send it"

**Co to znaczy:** Żadne urządzenie Cora na tym akwarium nie ma szczegółów połączenia z Apex potrzebnych do wykonania polecenia, albo to, które je ma, jest offline.

**Co robić:**
1. Dodaj szczegóły Apex w **Ustawienia** na urządzeniu, które jest aktualnie online, albo
2. Ustaw inne, działające Cora Max jako **Główne Cora Max** dla tego akwarium.

**Wciąż nie działa?** Wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** z nazwą akwarium i urządzenia.

## Wtórne Cora Max pokazuje "Główne Cora offline"

**Co to znaczy:** Główny tablet dla tego akwarium przeszedł offline, więc ten wtórny ekran pokazuje ostatnie otrzymane dane, a nie dane na żywo.

**Co robić:**
1. Sprawdź zasilanie i Wi-Fi głównego tabletu.
2. Poczekaj, aż połączy się z powrotem, albo zmień **Główne Cora Max** na urządzenie, które jest aktualnie online.

**Wciąż nie działa?** Wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** z nazwą akwarium i urządzenia.

## "Device is offline. Showing last known state."

**Co to znaczy:** Normalna obsługa braku połączenia: urządzenie przestało się zgłaszać, a Cora pokazuje ostatnie wartości, które miała, zamiast udawać, że są aktualne.

**Co robić:**
1. Sprawdź własne połączenie sieciowe urządzenia.
2. Traktuj pokazane wartości jako nie na żywo, aż wiersz nie mówi już offline.

**Wciąż nie działa?** Wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** z nazwą akwarium i urządzenia.

## Niektóre ustawienia ReefBeat są wyszarzone albo brakujące

**Co to znaczy:** To jest zamierzone, nie usterka. Ustawienia natywne urządzenia (w przeciwieństwie do odczytów) otwierają się tylko, gdy Twój telefon jest w tej samej sieci co samo urządzenie; poza tą siecią pokazywane są tylko odczyty.

**Co robić:**
1. Odwiedź własne Wi-Fi akwarium, aby zmienić te ustawienia.
2. Odczyty i historia wciąż działają normalnie poza akwarium.

**Wciąż nie działa?** Wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## "Nie udało się połączyć z Cora. Sprawdź Wi-Fi lub dane mobilne i spróbuj ponownie."

**Co to znaczy:** Twój telefon nie ma użytecznego połączenia z Cora Cloud podczas logowania. To dotyczy własnej łączności Twojego telefonu, nie sprzętu akwarium.

**Co robić:**
1. Sprawdź, czy Twój telefon ma działające Wi-Fi albo dane mobilne.
2. Wypróbuj inną sieć, jeśli jest dostępna.
3. **Spróbuj ponownie**.

**Wciąż nie działa?** Wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Wszystko jest nagle w złym języku

**Co to znaczy:** Język konta został zmieniony z dowolnego urządzenia. Język jest jednym ustawieniem dla całego konta, nie na urządzenie.

**Co robić:**
1. Otwórz **Ustawienia → Język** w dowolnej aplikacji.
2. Ustaw go z powrotem, jeśli został zmieniony przez przypadek; zmiana stosuje się wszędzie naraz.

**Wciąż nie działa?** Wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Stary alert albo raport jest wciąż w innym języku po zmianie

**Co to znaczy:** To jest oczekiwane, nie błąd. Cora nie tłumaczy ponownie treści, które zostały już wygenerowane; tylko nowe alerty, raporty i briefingi używają nowego języka.

**Co robić:**
1. Nic do naprawienia. Poczekaj na nową treść, która użyje aktualnego języka.

**Wciąż nie działa?** Wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Alert nie przestaje powiadamiać, mimo że go potwierdziłem

**Co to znaczy:** Pomylenie **Odrzuć** (zamyka alert na dobre) z **Odłóż** (wycisza go tymczasowo, do tygodnia).

**Co robić:**
1. Jeśli rozumiesz i akceptujesz warunek, użyj **Odrzuć**.
2. Jeśli chcesz tylko chwili spokoju, użyj **Odłóż** i wybierz długość.

**Wciąż nie działa?** Zobacz [Alerty i progi](/help/mobile-alerts), albo wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Dawka zatrzymała się w połowie i pojawił się alert "restore"

**Co to znaczy:** Głowica DŌS utraciła kontakt w trakcie dawkowania, więc Cora mówi Ci to celowo, zamiast zakładać, że cała dawka weszła.

**Co robić:**
1. Otwórz alert i sprawdź, ile faktycznie zostało zdozowane, przed zatrzymaniem.
2. Wznów albo dostosuj dawkę na podstawie tej ilości, nie ilości pierwotnie zaplanowanej.

**Wciąż nie działa?** Wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** z nazwą akwarium i urządzenia.

## Scenka utworzona na telefonie nie pojawia się jako edytowalna na Cora Max

**Co to znaczy:** Edytowanie scenek prosto na tablecie jest nowszą możliwością Cora Max. Starszy firmware wciąż może uruchamiać scenki utworzone na telefonie, tylko nie może ich tam edytować.

**Co robić:**
1. Zaktualizuj Cora Max, albo
2. Kontynuuj edycję tej scenki z telefonu; wciąż będzie działać na tablecie w każdym przypadku.

**Wciąż nie działa?** Zobacz [Aktualizacje i przywracanie](/help/max-updates), albo wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Assistant odpowiada o złym akwarium

**Co to znaczy:** Żadne akwarium nie zostało wybrane przed zapytaniem, albo złe akwarium jest aktualnie aktywne.

**Co robić:**
1. Wybierz najpierw akwarium, o które Ci chodzi.
2. Zapytaj ponownie.

**Wciąż nie działa?** Zobacz [Asystent](/help/mobile-assistant), albo wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Assistant odmawia odpowiedzi albo pokazuje ekran zgody ponownie

**Co to znaczy:** "Pozwól Cora Assistant korzystać z zapisanych danych akwarium" zostało wyłączone, więc nie ma z czego odpowiadać.

**Co robić:**
1. Dotknij **Zgadzam się i kontynuuję** na ekranie zgody, aby włączyć to z powrotem.

**Wciąż nie działa?** Zobacz [Asystent](/help/mobile-assistant), albo wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Wynik ICP z laboratorium albo e-maila nigdy się nie pojawił

**Co to znaczy:** Wprowadzenie wyniku do Cory wymaga wybranego dla niego akwarium, a czasem rozpoznanego nadawcy, zanim się gdziekolwiek dołączy.

**Co robić:**
1. Sprawdź wskazówkę wstępną pokazaną pierwszy raz, gdy wysyłasz wynik do Cory.
2. Potwierdź, do którego akwarium wynik powinien się dołączyć, gdy zostaniesz zapytany.
3. Upewnij się, że e-mail został wysłany z adresu, którego użyłeś wcześniej, jeśli wysyłałeś już taki poprzednio.

**Wciąż nie działa?** Zobacz [ICP i raporty zdrowia](/help/mobile-icp-health), albo wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Powiadomienie o ICP z e-maila nie nazywa żadnego laboratorium

**Co to znaczy:** Znany problem z powiadomieniem push "choose tank" brakującym nazwy laboratorium. Zostało to naprawione w aktualnych wersjach.

**Co robić:**
1. Upewnij się, że Cora Mobile jest zaktualizowana do najnowszej wersji.
2. Sam wynik nie jest tym dotknięty; tylko tekst powiadomienia nie miał nazwy.

**Wciąż nie działa?** Wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Widżet pokazuje złe jednostki

**Co to znaczy:** To jest ustawienie jednostek wyświetlania akwarium, nie problem z danymi. Wartości są przechowywane w ten sam sposób niezależnie od tego, jak są wyświetlane.

**Co robić:**
1. Otwórz **Ustawienia** dla tego akwarium i sprawdź jego jednostki wyświetlania.
2. Zmień je tam; każdy telefon i Cora Max pokazujące to akwarium zaktualizują się, aby się zgadzać.

**Wciąż nie działa?** Wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Wskaźnik albo próg wygląda inaczej po zmianie jednostek wyświetlania

**Co to znaczy:** Oczekiwane. Wskaźniki, kafelki i historia rysują się na nowo w wybranej przez Ciebie jednostce; wartości bazowe się nie zmieniły.

**Co robić:**
1. Nic do naprawienia; to jest tylko kosmetyczne.

**Wciąż nie działa?** Wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Max nie łączy się z powrotem od razu po przerwie w Wi-Fi

**Co to znaczy:** Po utracie połączenia Cora Max czeka trochę dłużej przed każdą kolejną próbą, zamiast bombardować sieć, wydłużając odstęp do około minuty, zanim spróbuje ponownie.

**Co robić:**
1. Poczekaj około minuty, gdy Twoja sieć wróci.
2. Jeśli wciąż nie połączyło się po tym czasie, sprawdź Wi-Fi w **Ustawienia → Network**.

**Wciąż nie działa?** Zobacz [Ekran główny Cora Max](/help/max-tour), albo wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Zmiana nazwy Cora Max na telefonie nie zmienia tego, co pokazuje tablet

**Co to znaczy:** Nazwa, którą ustawiasz z telefonu, jest etykietą tego urządzenia na poziomie konta. Nazwa pokazana na samym tablecie podczas parowania może być czymś innym.

**Co robić:**
1. Sprawdź, na którą "nazwę" patrzysz: tę na Twojej liście urządzeń na telefonie, czy tę na własnym ekranie parowania tabletu.
2. Zmień nazwę z listy urządzeń telefonu, jeśli to etykieta konta, którą chcesz zmienić.

**Wciąż nie działa?** Wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** z nazwą urządzenia.

## Nie mogę znaleźć, gdzie wyłączyć frazę budzącą na Cora Max

**Co to znaczy:** Przełącznik frazy budzącej znajduje się w **Audio**, nie w grupie ustawień Cora Assistant, co zaskakuje większość osób.

**Co robić:**
1. Przejdź do **Ustawienia → Audio → Nasłuchiwanie słowa aktywującego**.
2. Wyłącz to; wciąż możesz dotknąć ikony Cora, aby uruchomić sesję głosową.

**Wciąż nie działa?** Zobacz [Ustawienia na Cora Max](/help/max-settings), albo wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Blokada rodzicielska nie pozwala nikomu wejść do Settings

**Co to znaczy:** To działa zgodnie z zamierzeniem. Blokada rodzicielska blokuje ekran dotykowy i kontrolki głosowe po ustalonym czasie bez dotyku; odczyty wciąż się aktualizują pod nią.

**Co robić:**
1. Naciśnij **Volume Up** albo **Volume Down** trzy razy w ciągu dwóch sekund, albo
2. Przytrzymaj pięć palców w prawym górnym rogu ekranu na dziesięć sekund.

**Wciąż nie działa?** Zobacz [Głos na Cora Max](/help/max-voice), albo wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Wciąż zablokowany

Wyślij e-mail na **[cora@coraiq.tech](mailto:cora@coraiq.tech)**. Powiedz nam, które akwarium, który ekran i czego się spodziewałeś zobaczyć; to daje Ci szybciej użyteczną odpowiedź.

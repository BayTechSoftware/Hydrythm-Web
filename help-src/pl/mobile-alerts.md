---
title: Alerty i progi
description: Ustaw zakres dla każdego parametru, wybierz, o czym chcesz być informowany, i zrozum, czemu alert się uruchomił.
section: Cora Mobile
reviewed: 2026-09-27
order: 15
group: Alerts and automation
---

Alert powstaje, gdy odczyt wychodzi poza ustawiony dla niego zakres. Ty ustawiasz zakresy i Ty kontrolujesz, które alerty docierają do Twojego telefonu.

Otwórz **Centrum alertów** ze rzędu skrótów na dole pulpitu.

![Alert Center](img/mobile-alerts.webp "Aktywne alerty, każdy ze swoją ważnością, tym, co go wywołało, i kiedy.")

## Alert Center

Dwie zakładki:

- **Aktywny**: aktualnie podniesione alerty, z liczbą na plakietce
- **Reguły**: progi i reguły tempa zmiany, które je tworzą

Każdy aktywny alert pokazuje parametr i akwarium, odczyt, który go wywołał, prostą wyjaśnienie, plakietkę ważności, rodzaj reguły, która się uruchomiła (**Próg** lub **Tempo zmiany**), oraz czas jego uruchomienia.

Dwie akcje przy każdym:

- **Wyświetl regułę**: otwiera regułę, która go podniosła, dzięki czemu możesz dostosować zakres
- **Wyjaśnij ten alert**: prosi Asystenta o zinterpretowanie go w oparciu o historię Twojego akwarium

## Ustawianie zakresu

Parametry, które Cora może oceniać, mają docelowy zakres, a wartości domyślne pochodzą z typu i wieku Twojego akwarium ustawionego podczas konfiguracji, zwykle rozsądny punkt wyjścia. Parametr bez użytecznego zakresu nie jest oceniany wcale: pozostaje neutralnie szary, a nie odgadywany.

Aby zmienić zakres: **przytrzymaj jego widżet** na pulpicie, co otwiera progi tego parametru bezpośrednio. Zwykłe dotknięcie otwiera za to widok parametru; te dwa gesty prowadzą w różne miejsca, a przytrzymanie jest skrótem, który warto pamiętać.

Jeśli parametr nie ma jeszcze reguły, pola zaczynają od wartości domyślnej Cory, a notatka pod nimi mówi to wprost. Zmień jakąkolwiek wartość, aby ustawić swoją własną.

Aby zobaczyć je wszystkie razem, użyj **Alerty** w rzędzie przycisków pod pulpitem.

Możesz ustawić:

- **Zakres**: dolną i górną wartość, dla rzeczy takich jak alkaliczność czy temperatura
- **Sufit**: tylko górną wartość, dla rzeczy, gdzie niska wartość jest w porządku, jak azotany czy fosforany
- **Podłogę**: tylko dolną wartość

:::tip Ustaw zakres, w jakim faktycznie działa Twoje akwarium
Wartości domyślne są punktem wyjścia, nie wyrokiem. Akwarium prowadzone przy niskiej zawartości substancji odżywczych na poziomie 6 dKH nie jest "błędne", bo tabela mówiła 8-9. Ustaw zakres, w jakim faktycznie działasz, a Cora powie Ci, gdy *Ty* zaczniesz od niego odchodzić.
:::

## Co wywołuje alert

Alert uruchamia się, gdy odczyt przekracza próg. Cora sprawdza każdy odczyt, gdy przychodzi, więc jeden odczyt poza Twoim zakresem wystarczy, aby go podnieść.

Gdy alert jest już podniesiony, nie będzie Cię wciąż powiadamiać o tej samej rzeczy; jest czas wstrzymania, zanim może się uruchomić ponownie. I **gaśnie sam**, w chwili, gdy odczyt wraca do zakresu; nie ma niczego do potwierdzenia.

Możesz też ustawić regułę **tempa zmiany**, która obserwuje, jak szybko zmienia się parametr, a nie to, gdzie aktualnie się znajduje. Jest to ta, którą warto użyć dla rzeczy, gdzie szybkość zmiany ma większe znaczenie niż sama liczba.

## Gdzie pojawiają się alerty

- **Dzwonek**, w prawym górnym rogu każdego ekranu, przechowuje Twoją historię. Liczba mówi, ile z nich jeszcze nie przeczytałeś.
- **Powiadomienia push** docierają do Twojego telefonu, gdy je zezwolisz.
- **Widżet** robi się bursztynowy albo czerwony na pulpicie.
- **Cora Max** pokazuje te same alerty na dużym ekranie.

## Gdy sprzęt wymaga uwagi

Niektóre alerty dotyczą sprzętu, a nie odczytu. Gdy urządzenie takie jak Trident albo pompa Jecod zgłasza usterkę, Cora wysyła powiadomienie, które nazywa akwarium i urządzenie, na przykład *"Akwarium Display: pompa powrotna wymaga uwagi"*, i mówi, co jest nie tak, na przykład zablokowany wirnik. Gdy usterka mija, następuje drugie powiadomienie: *"Akwarium Display: pompa powrotna jest znowu w porządku"*. Obydwa są w kategorii **Awarie sprzętu** w **Ustawienia → Powiadomienia**.

Gyre Maxspect (beta) może podnieść ten sam alert, gdy Cora Max w jego sieci wykryje obie głowice ustawione na 0%, albo nie otrzyma odpowiedzi od gyre dwa razy z rzędu. Traktuj to jako ostrzeżenie, nie zabezpieczenie: Cora Max sprawdza od czasu do czasu, a nie w sposób ciągły, i tylko wtedy, gdy działa i może dosięgnąć gyre.

## "Red Sea readings have stopped updating"

Możesz zobaczyć ten baner na stronie parametru akwarium:

> Odczyty Red Sea przestały się aktualizować. Żadne urządzenie nie odpytuje obecnie urządzeń Red Sea tego akwarium: sprawdź Primary Cora Max w Settings albo otwórz to akwarium na urządzeniu w tej samej sieci Wi-Fi.

To znaczy, że żaden telefon czy Cora Max nie odpytuje obecnie sprzętu ReefBeat tego akwarium, więc pokazane odczyty są starsze, niekoniecznie błędne. Dotknij banera, aby otworzyć **Główne Cora Max** i wybrać urządzenie, które jest włączone, albo ustawić je na **Każde aktywne (automatycznie)**. Zobacz [Więcej niż jedno urządzenie Cora](/help/mobile-multi-device). Jeśli to nie ustępuje, zobacz [Rozwiązywanie problemów](/help/troubleshooting).

## Wybieranie, co do Ciebie dociera

**Ustawienia → Notifications.** Możesz kontrolować:

- Które z kategorii powiadomień mogą wysyłać push

Reef Buddy nie ma własnego przełącznika: wysyła briefing, gdy jest coś warte zareagowania, i milczy, gdy nie jest.

:::note Cora jest zbudowana, aby milczeć
Codzienny briefing to jedno powiadomienie push na akwarium dziennie, i w dniu, gdy nic nie wymaga Twojej uwagi, zwykle nie odzywa się wcale, zamiast mówić, że wszystko jest w porządku. Jeśli Cora wysyła powiadomienie, coś się zmieniło.
:::

## Czasy wstrzymania: jak często ten sam alert może Cię powiadamiać

Każda reguła ma swój własny **Czas wstrzymania między alertami**, ustawiany podczas dodawania lub edytowania reguły (w zakładce **Reguły** Alert Center). Czas wstrzymania nie skrywa samego alertu: ogranicza tylko, jak często Cora wysyła Ci o nim powiadomienie push. Odczyt pozostaje oceniany, a alert pozostaje widoczny na widżecie i w dzwonku cały czas.

Możesz wybrać: 15 min, 30 min, 1 godz., 2 godz., 4 godz., 8 godz., 1 dzień, 3 dni albo **1 tydzień**.

Krótki czas wstrzymania odpowiada szybko zmieniającemu się odczytowi, takiemu jak temperatura. Długi, do tygodnia, odpowiada czemuś, co pozostaje błędne przez dni, gdy czekasz na część, jak Trident bez reagentu albo pusty pojemnik dozujący: bez długiego czasu wstrzymania Cora wysyłałaby powiadomienia o tym samym znanym problemie kilka razy dziennie.

:::note Wyciszanie aktywnego alertu odbywa się na Cora Max
Cora Mobile nie ma własnego przycisku Snooze na aktywnym alercie; ta kontrolka jest na ekranie Cora Max przy akwarium i wycisza ten sam alert na długość czasu wstrzymania, który wybrałeś tutaj. Z telefonu sposobem na zmianę tego, jak często słyszysz o czymś, jest ten czas wstrzymania dla danej reguły, nie wyciszenie dla danego alertu.
:::

## Zamykanie alertu

Alert gaśnie, gdy odczyt wraca do zakresu. Nie ma niczego do odrzucenia; to jest stwierdzenie o akwarium, nie zadanie.

:::note Przejściowe odczyty podnoszą alerty
Jeden odczyt poza zakresem wystarczy, aby podnieść alert, więc sonda, która skoczy, wywoła jeden. Jeśli źródło jest niewiarygodne, skalibruj je ponownie albo skieruj widżet na inne źródło, zamiast rozszerzać próg.
:::

Jeśli odczyt jest błędny, a nie akwarium (na przykład sonda wymagająca kalibracji), naprawiaj źródło. Rozszerzenie progu, aby uciszyć wadliwą sondę, skrywa też następny prawdziwy problem.

## Wyłączanie alertów dla parametru

Otwórz regułę w zakładce **Reguły** Alert Center i wyłącz jej **przełącznik włączenia**. Reguła i jej zakres są zachowywane, więc możesz je włączyć z powrotem bez budowania od nowa.

:::warning Wycisz parametr bez usuwania jego zakresu
Usunięcie progu nie musi zatrzymać każdej oceny tego odczytu; domyślne pasma odniesienia wciąż kolorują wartość i wciąż mogą zasilać briefing. Użyj przełącznika włączenia reguły.
:::

---
title: Alerty i progi
description: Ustaw prawidłowy zakres dla każdego odczytu, wybierz, jak często alert może Cię powiadamiać, i sprawdź, dlaczego urządzenie „przestało raportować”.
section: Cora Mobile
reviewed: 2026-10-17
order: 22
group: Alerts and automation
twin: max-alerts
---

Dostajesz alert, gdy odczyt wyjdzie poza zakres, który dla niego ustawiono. Ta strona opisuje ustawianie tych zakresów, to, co dzieje się, gdy alert się pojawi, i jak długo Cora czeka, zanim powie, że urządzenie przestało raportować.

Żeby otworzyć **Centrum alertów**, dotknij **Alerty** w rzędzie przycisków pod panelem. Znajdziesz je też w Ustawieniach → Twoje akwarium → **Progi alertów**.

![Zakładka Aktywne w Centrum alertów w Cora Mobile](img/mobile-alerts.webp "Aktywne alerty, każdy z ważnością, przyczyną i czasem, oraz Wyświetl regułę i Wyjaśnij ten alert.")

## Centrum alertów {#alert-center}

Ma dwie zakładki. **Aktywne** wymienia alerty, które trwają teraz, z licznikiem na plakietce. **Reguły** zawiera reguły, które je wywołują.

Każdy aktywny alert pokazuje parametr i akwarium, odczyt, który go wywołał, krótkie wyjaśnienie, chip ważności, rodzaj reguły, która zadziałała (**Próg** albo **Tempo zmiany**), i czas. Ma dwa przyciski:

- **Wyświetl regułę** otwiera regułę, która za nim stoi, żeby poprawić zakres. Przy alercie dozownika, na przykład gdy w głowicy DŌS albo ReefDose kończy się płyn albo pominięto dawkę, ten przycisk to **Otwórz dozownik**. Otwiera stronę tego dozownika z jego alertami.
- **Wyjaśnij ten alert** otwiera Cora Assistant z gotowym do wysłania pytaniem o alert. Sprawdź je, zmień, jeśli chcesz, i wyślij.

## Zakładka Reguły {#rules}

![Zakładka Reguły](img/mobile-alert-rules.webp "Reguły pogrupowane według parametru, każda z własnym przełącznikiem.")

Reguły są pogrupowane według parametru. Każda ma własny przełącznik w swoim wierszu, więc możesz ją wyłączyć bez otwierania. Wiersz pokazuje też **Aktywny teraz**, gdy jej alert trwa, albo kiedy ostatnio zadziałała (albo **Nigdy nie zadziałał**).

Reguły głowicy dozującej mają nazwę od głowicy i tego, co obserwują, na przykład *Jod · pozostałe dni* albo *Jod · pozostało*. Pominięta dawka pojawia się jako *Jod · pominięta dawka*. Każdy DŌS i każdy ReefDose ma tu jeden własny wiersz, a alerty jego głowic nie są wymieniane osobno. Dotknij wiersza, żeby otworzyć stronę tego dozownika. Zobacz [Alerty dozownika](/help/mobile-device-control#doser-alerts).

Na dole:

- **Dodaj zalecane reguły** dodaje brakujące reguły zalecane przez Corę. Pomija parametr, który ma już regułę. W akwarium bez żadnych reguł ten przycisk to **Dodaj domyślne reguły**.
- **Dodaj własną regułę** tworzy Twoją własną regułę. Wybierz parametr i **Typ reguły**, **Próg** albo **Tempo zmiany**. Przycisk **Dodaj regułę** w prawym dolnym rogu robi to samo.

### Edytowanie reguły {#editing-a-rule}

Dotknij wiersza reguły, żeby ją otworzyć. Znajdziesz tam:

- **Minimum alertu** i **Maksimum alertu**, czyli sam zakres. Zostaw jedno puste, żeby ustawić tylko górną albo dolną granicę.
- **Polecane**, które przywraca zakres sugerowany przez Corę.
- **Zakres wskaźnika (wyświetlacz Cora)**, z **Min. wskaźnika** i **Maks. wskaźnika**. Ustalają tylko skalę wskaźnika na Cora Max. Nigdy nie wywołują alertu.
- **Czas wstrzymania między alertami**, opisany [niżej](#cooldowns).
- **Włączone** i przycisk usuwania.

Reguła usterki urządzenia, na przykład Tridenta bez odczynnika, nie ma zakresu. Wybierasz tylko jej czas wstrzymania.

## Ustawianie zakresu {#setting-a-range}

Parametry, które Cora potrafi ocenić, mają zakres docelowy. Wartości domyślne pochodzą z typu i wieku akwarium podanych przy konfiguracji i są rozsądnym początkiem. Jeśli parametr nie ma przydatnego zakresu, Cora go nie ocenia, a jego widżet zostaje neutralnie szary.

Najszybciej zmienisz zakres, przytrzymując widżet parametru na panelu. Otworzą się jego progi. Zwykłe dotknięcie otwiera zamiast tego widok parametru.

![Arkusz edycji progu pH w Cora Mobile](img/mobile-threshold-sheet.webp "Minimum i maksimum alertu, zakres wskaźnika dla Cora Max i czas wstrzymania między alertami.")

Jeśli parametr nie ma jeszcze reguły, pola zaczynają od wartości domyślnych Cory, a notatka pod nimi o tym mówi. Zmień dowolną wartość, żeby ustawić własną.

Możesz ustawić:

- zakres, z dolną i górną granicą, dla takich rzeczy jak alkaliczność albo temperatura
- górną granicę, tylko z maksimum, dla rzeczy, przy których niska wartość nie szkodzi, jak azotany albo fosforany
- dolną granicę, tylko z minimum

:::tip Ustaw zakres, w którym naprawdę pracuje Twoje akwarium
Wartości domyślne to tylko punkt wyjścia. Akwarium z niską zawartością biogenów na 6 dKH nie jest „złe” dlatego, że tabela podaje 8–9. Ustaw zakres, w którym pracujesz, a Cora powie Ci, gdy *Ty* zaczniesz dryfować.
:::

## Co wywołuje alert {#what-triggers-an-alert}

Alert pojawia się, gdy odczyt przekroczy próg. Cora sprawdza każdy odczyt, gdy tylko nadejdzie, więc wystarczy jeden odczyt poza zakresem.

Reguła tempa zmiany obserwuje, jak szybko zmienia się parametr, a nie gdzie jest. Używaj jej, gdy szybkość zmiany jest ważniejsza niż sama liczba.

Gdy alert już trwa, nie będzie Cię ciągle powiadamiać o tym samym. [Czas wstrzymania](#cooldowns) reguły decyduje, kiedy może powiadomić Cię ponownie.

## Gdzie pojawiają się alerty

- Dzwonek w prawym górnym rogu głównych zakładek przechowuje historię. Liczba pokazuje, ilu jeszcze nie przeczytano. Więcej w [Powiadomieniach](/help/mobile-notifications).
- Powiadomienie push trafia na telefon, jeśli ta kategoria jest włączona.
- Widżet na panelu robi się pomarańczowy albo czerwony.
- Cora Max pokazuje te same alerty na swoim ekranie.

## Gdy sprzęt wymaga uwagi {#equipment-faults}

Niektóre alerty dotyczą sprzętu, a nie odczytu. Gdy urządzenie, na przykład Trident albo pompa Jecod, zgłosi usterkę, Cora wysyła powiadomienie z nazwą akwarium i urządzenia, na przykład *„Akwarium główne: Pompa powrotna wymaga uwagi”*. Podaje też, co jest nie tak, na przykład zablokowany wirnik. Gdy usterka minie, dostaniesz drugie: *„Akwarium główne: Pompa powrotna znów działa poprawnie”*. Oba należą do **Awarie sprzętu** w **Ustawienia → Powiadomienia**.

AquaWiz KH Controller czytany co godzinę przez Twój Cora Max wywołuje ten sam rodzaj alertu, gdy:

- jego pompa dozująca zgłasza usterkę;
- jego sonda pH uległa awarii albo kończy żywotność;
- poziom w jego zbiorniku na wodę przez ponad godzinę pozostaje niski lub wysoki.

Potrzebny jest do tego godzinowy odczyt z Cora Max (od następnej aktualizacji Cora Max) (zobacz [Sterowanie sprzętem z Cora Max](/help/max-device-control#aquawiz-hourly)): odczyt z chmury AquaWiz co 12 godzin ich nie niesie.


## Urządzenie przestało raportować {#stopped-reporting}

Gdy podłączone urządzenie ucichnie, Cora wysyła *„[Urządzenie]: przestał raportować”*. Nie oznacza to, że urządzenie jest zepsute, tylko że Cora od jakiegoś czasu nic od niego nie dostała. Gdy wróci, dostaniesz drugie powiadomienie, *„[Urządzenie]: znów raportuje”*.

Jak długo Cora czeka, zależy od urządzenia:

| Urządzenie | Cora czeka |
|---|---|
| Neptune Apex | Około 30 minut bez aktualizacji |
| Red Sea ReefBeat | Około 30 minut |
| AquaWiz | Około 25 godzin, bo AquaWiz pozwala Corze czytać swoją chmurę tylko co 12 godzin |
| Pompy Jecod | Trzy brakujące odczyty z rzędu, według interwału odczytu pompy (90 minut przy domyślnych 30) |
| Wtyczka Zigbee | Nie wróciła 30 minut po restarcie bramki. Nadaj jej nazwę przez **Zmień nazwę**, aby alert ją wskazywał |

Co sprawdzić, zależy od tego, jak Cora odczytuje urządzenie.

- Apex, ReefBeat i Jecod odczytuje Cora Max przez Wi-Fi. Sprawdź zasilanie i Wi-Fi urządzenia oraz to, czy Cora Max, który je odczytuje, jest włączony i online.
- AquaWiz jest odczytywany przez Twoje konto u producenta. Sprawdź połączenie z kontem na stronie urządzenia w Cora Mobile.


Te powiadomienia należą do **Awarie sprzętu** w **Ustawienia → Powiadomienia**.


Akwarium Red Sea może też pokazać baner *„Odczyty Red Sea przestały się aktualizować”*, gdy żaden telefon ani Cora Max nie odczytuje jego sprzętu ReefBeat. Dotknij go, żeby wybrać **Główne Cora Max**. Pełne rozwiązanie jest w [Rozwiązywaniu problemów](/help/troubleshooting#red-sea-readings-have-stopped-updating).

## Co do Ciebie dociera {#choosing-what-reaches-you}

W **Ustawienia → Powiadomienia** wybierasz, które kategorie mogą wysyłać Ci powiadomienia. Zobacz [Powiadomienia](/help/mobile-notifications), gdzie opisano też [ciszę w nocy](/help/mobile-notifications#quiet-at-night).

Reef Buddy nie ma własnego przełącznika. Jego porę ustala wiersz **Godzina podsumowania**, tuż pod Powiadomieniami w Ustawieniach. W planie darmowym nie ma powiadomienia o podsumowaniu.

:::note Cora milczy, chyba że coś się zmieniło
Codzienne podsumowanie to jedno powiadomienie na akwarium dziennie. W dzień, w którym nic Cię nie potrzebuje, zwykle milczy, zamiast mówić, że wszystko w porządku. Jeśli Cora wysyła powiadomienie, coś się zmieniło.
:::

## Czasy wstrzymania: jak często ten sam alert może Cię powiadamiać {#cooldowns}

Każda reguła ma własny **Czas wstrzymania między alertami**. Ustawiasz go przy dodawaniu albo edycji reguły. Reguła, która nigdy go nie miała, używa 1 h.

Czas wstrzymania nie ukrywa alertu. Ogranicza tylko to, jak często Cora wysyła o nim powiadomienie. Odczyt jest nadal oceniany, a alert przez cały czas widać na widżecie i pod dzwonkiem.

Możesz wybrać 15 min, 30 min, 1 h, 2 h, 4 h, 8 h, 1 dzień, 3 dni albo 1 tydzień.

Krótki czas pasuje do szybko zmieniającego się odczytu, takiego jak temperatura. Długi, do tygodnia, pasuje do czegoś, co pozostaje złe przez dni, gdy czekasz na część, na przykład Tridenta bez odczynnika albo pustego pojemnika dozującego.

:::note Odłóż jest na Cora Max
Cora Mobile nie ma przycisku Odłóż przy aktywnym alercie. Odłóż jest na ekranie Cora Max przy akwarium i wycisza alert na czas wstrzymania wybrany tutaj. W telefonie to czas wstrzymania reguły decyduje, jak często słyszysz o danej sprawie.
:::

## Znikanie alertu {#clearing-an-alert}

Alert znika sam, gdy odczyt wróci do zakresu. Nie ma czego zamykać. Dostajesz wtedy jedno powiadomienie, na przykład *„Akwarium główne: Wapń wrócił do normy”*. Jeśli problem wróci później, dostaniesz nowy alert.

:::note Krótkie skoki też wywołują alerty
Do wywołania alertu wystarczy jeden odczyt poza zakresem, więc sonda, która skacze, go wywoła. Jeśli źródło jest niepewne, skalibruj je albo skieruj widżet na inne źródło. Nie poszerzaj progu.
:::

Czasem błędny jest odczyt, a akwarium jest w porządku, na przykład gdy sonda wymaga kalibracji. W takim przypadku napraw źródło. Jeśli poszerzysz próg, żeby uciszyć złą sondę, przegapisz też następny prawdziwy problem.

## Wyłączanie alertu {#turning-an-alert-off}

Wyłącz przełącznik w wierszu reguły w zakładce **Reguły**. Cora zachowuje regułę i jej zakres, więc możesz ją włączyć ponownie bez ustawiania od nowa.

Dopóki reguła jest wyłączona, Cora nie ocenia tego odczytu. Jego widżet zostaje neutralnie szary i nigdy nie wywoła alertu.

:::warning Wyłącz parametr bez usuwania zakresu
Usunięcie reguły nie zawsze sprawia, że Cora przestaje oceniać ten odczyt. Domyślne zakresy odniesienia nadal kolorują wartość i mogą trafiać do podsumowania. Użyj przełącznika reguły.
:::

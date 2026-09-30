---
title: Alerty i progi
description: Ustaw zakres dla każdego parametru, wybierz, o czym chcesz wiedzieć, i sprawdź, dlaczego pojawił się alert.
section: Cora Mobile
reviewed: 2026-09-30
order: 15
group: Alerts and automation
---

Alert pojawia się, gdy odczyt wyjdzie poza ustawiony zakres. Zakresy ustawiasz Ty i Ty decydujesz, które alerty trafiają na telefon.

**Centrum alertów** otworzysz z rzędu skrótów na dole pulpitu.

![Centrum alertów](img/mobile-alerts.webp "Aktywne alerty z poziomem ważności, przyczyną i czasem.")

## Centrum alertów

Są tu dwie zakładki:

- **Aktywne**: alerty, które trwają teraz, z licznikiem na plakietce
- **Reguły**: progi i reguły tempa zmiany, z których te alerty się biorą

Przy każdym aktywnym alercie widać parametr i akwarium, odczyt, który go wywołał, krótkie wyjaśnienie, poziom ważności, rodzaj reguły (**Próg** albo **Tempo zmiany**) i godzinę.

Każdy alert ma dwa przyciski:

- **Wyświetl regułę** otwiera regułę, która go wywołała. Tam możesz poprawić zakres.
- **Wyjaśnij ten alert** prosi Asystenta, żeby ocenił alert na tle historii Twojego akwarium.

## Ustawianie zakresu

Parametry, które Cora potrafi ocenić, mają zakres docelowy. Wartości domyślne wynikają z typu i wieku akwarium podanych przy konfiguracji i zwykle są rozsądnym punktem wyjścia. Parametr bez sensownego zakresu nie jest oceniany. Zostaje szary, a Cora niczego nie zgaduje.

Żeby zmienić zakres, **przytrzymaj widżet** parametru na pulpicie. Od razu otworzą się jego progi. Zwykłe dotknięcie otwiera widok parametru, więc warto zapamiętać to przytrzymanie.

Jeśli parametr nie ma jeszcze reguły, pola pokazują wartości domyślne Cora i informuje o tym notatka pod nimi. Zmień dowolną wartość, a ustawisz własną.

Wszystkie zakresy naraz zobaczysz pod przyciskiem **Alerty** w rzędzie pod pulpitem.

Możesz ustawić:

- **Zakres**, czyli dolną i górną granicę, np. dla alkaliczności albo temperatury
- **Górną granicę**, gdy niska wartość nie szkodzi, np. dla azotanów czy fosforanów
- **Dolną granicę**, jeśli liczy się tylko minimum

:::tip Ustaw zakres, w którym naprawdę trzymasz akwarium
Wartości domyślne to punkt wyjścia, a nie wyrok. Akwarium z niską zawartością składników odżywczych na 6 dKH nie jest „złe” tylko dlatego, że tabela podaje 8–9. Ustaw zakres, w którym naprawdę pracujesz, a Cora da znać, gdy zaczniesz z niego wychodzić.
:::

## Kiedy pojawia się alert

Alert pojawia się, gdy odczyt przekroczy próg. Cora sprawdza każdy odczyt od razu po nadejściu, więc wystarczy jeden odczyt spoza zakresu.

Gdy alert już trwa, Cora nie powiadamia Cię o nim w kółko. Zanim alert znów się odezwie, musi minąć czas wstrzymania. Alert **znika sam**, gdy tylko odczyt wróci do zakresu. Nie trzeba niczego potwierdzać.

Możesz też ustawić regułę **tempa zmiany**. Sprawdza ona, jak szybko zmienia się parametr, a nie gdzie jest teraz. Przydaje się tam, gdzie liczy się tempo zmiany bardziej niż sama wartość.

## Gdzie widać alerty

- **Dzwonek** w prawym górnym rogu każdego ekranu przechowuje historię. Liczba przy nim to alerty, których jeszcze nie przeczytano.
- **Powiadomienia push** przychodzą na telefon, jeśli na nie pozwolisz.
- **Widżet** na pulpicie zmienia kolor na bursztynowy albo czerwony.
- **Cora Max** pokazuje te same alerty na dużym ekranie.

## Gdy sprzęt wymaga uwagi

Część alertów dotyczy sprzętu, a nie odczytu. Gdy urządzenie, np. Trident albo pompa Jecod, zgłosi usterkę, Cora wysyła powiadomienie z nazwą akwarium i urządzenia, np. *„Akwarium główne: Pompa powrotna wymaga uwagi”*, i podaje, co się stało, np. zablokowany wirnik. Gdy usterka minie, przychodzi drugie powiadomienie: *„Akwarium główne: Pompa powrotna znów działa poprawnie”*. Oba należą do kategorii **Awarie sprzętu** w **Ustawienia → Powiadomienia**.

Gyre Maxspect (beta) może wywołać ten sam alert, gdy Cora Max w jego sieci wykryje obie głowice ustawione na 0% albo dwa razy z rzędu nie dostanie odpowiedzi od gyre. Traktuj to jako ostrzeżenie, a nie zabezpieczenie. Cora Max sprawdza gyre co jakiś czas, nie bez przerwy. Robi to tylko wtedy, gdy działa i ma połączenie z gyre.

## Urządzenie przestało się zgłaszać

Gdy Neptune Apex, urządzenie Red Sea ReefBeat, AquaWiz, pompa Jecod albo gyre Maxspect ucichną, Cora informuje o tym: *„[Urządzenie]: przestało się zgłaszać”*. Sprawdź zasilanie i Wi-Fi urządzenia oraz to, czy Cora Max, który je odczytuje, jest włączony. Większość sprzętu dostaje ten alert po około 30 minutach bez aktualizacji. AquaWiz odpytuje rzadziej, więc czeka około 3 godzin. Gdy urządzenie znów zacznie się zgłaszać, przychodzi drugie powiadomienie.

Alert ten należy do kategorii **Awarie sprzętu** w **Ustawienia → Powiadomienia**, razem z alertami usterek opisanymi wyżej.

## „Odczyty Red Sea przestały się aktualizować”

Na stronie parametru akwarium może pojawić się taki baner:

> Odczyty Red Sea przestały się aktualizować. Żadne urządzenie nie odczytuje teraz urządzeń Red Sea tego akwarium: sprawdź główny Cora Max w Ustawieniach albo otwórz to akwarium na urządzeniu w tej samej sieci Wi-Fi.

Oznacza to, że żaden telefon ani Cora Max nie odpytuje teraz sprzętu ReefBeat tego akwarium. Widoczne odczyty są więc stare, ale niekoniecznie błędne. Dotknij banera, żeby otworzyć **Główne Cora Max**. Wybierz tam urządzenie, które jest włączone, albo ustaw **Każde aktywne (automatycznie)**. Szczegóły są na stronie [Więcej niż jedno urządzenie Cora](/help/mobile-multi-device). Jeśli baner nie znika, zajrzyj do [Rozwiązywania problemów](/help/troubleshooting).

## Co ma do Ciebie docierać

W **Ustawienia → Powiadomienia** wybierasz:

- które kategorie powiadomień mogą wysyłać push

Reef Buddy nie ma osobnego przełącznika. Wysyła briefing, gdy jest coś do zrobienia, a gdy nie ma, milczy.

:::note Cora z założenia nie przeszkadza
Codzienny briefing to jedno powiadomienie push na akwarium dziennie. W dzień, w którym nic nie wymaga uwagi, zwykle w ogóle się nie pojawia i nie pisze, że wszystko jest w porządku. Jeśli Cora wysyła powiadomienie, coś się zmieniło.
:::

## Czas wstrzymania: jak często ten sam alert może powiadamiać

Każda reguła ma własny **Czas wstrzymania między alertami**. Ustawiasz go przy dodawaniu albo edycji reguły, w zakładce **Reguły** w Centrum alertów. Czas wstrzymania nie ukrywa alertu. Ogranicza tylko to, jak często Cora wysyła o nim push. Odczyt nadal jest oceniany, a alert przez cały czas widać na widżecie i pod dzwonkiem.

Do wyboru jest 15 min, 30 min, 1 godz., 2 godz., 4 godz., 8 godz., 1 dzień, 3 dni i **1 tydzień**.

Krótki czas pasuje do odczytu, który zmienia się szybko, np. temperatury. Długi, aż do tygodnia, pasuje do problemu, który trwa dniami, gdy czekasz na część. Tak jest na przykład z Tridentem bez odczynnika albo z pustym pojemnikiem pompy dozującej. Bez długiego czasu wstrzymania Cora wysyłałaby push o tym samym znanym problemie kilka razy dziennie.

:::note Aktywny alert wyciszysz na Cora Max
Cora Mobile nie ma przycisku odkładania przy aktywnym alercie. Ten przycisk jest na ekranie Cora Max przy akwarium i wycisza alert na czas wstrzymania ustawiony tutaj. Na telefonie o tym, jak często słyszysz o danym problemie, decyduje czas wstrzymania reguły.
:::

## Kiedy alert znika

Alert znika, gdy odczyt wróci do zakresu. Nie trzeba go zamykać. To informacja o stanie akwarium, a nie zadanie do odhaczenia.

:::note Chwilowe skoki też wywołują alerty
Wystarczy jeden odczyt spoza zakresu, więc skok sondy też wywoła alert. Jeśli źródło jest niepewne, skalibruj je albo przełącz widżet na inne źródło. Nie poszerzaj progu.
:::

Jeśli błędny jest odczyt, a nie stan akwarium (np. sonda wymaga kalibracji), napraw źródło. Szerszy próg uciszy wadliwą sondę, ale ukryje też następny prawdziwy problem.

## Wyłączanie alertów dla parametru

Otwórz regułę w zakładce **Reguły** w Centrum alertów i wyłącz jej **przełącznik**. Reguła i zakres zostają zapisane, więc możesz ją później włączyć bez ustawiania od nowa.

:::warning Wycisz parametr, ale nie usuwaj zakresu
Usunięcie progu nie zawsze kończy ocenę odczytu. Domyślne zakresy odniesienia nadal nadają wartości kolor i mogą trafiać do briefingu. Użyj przełącznika reguły.
:::

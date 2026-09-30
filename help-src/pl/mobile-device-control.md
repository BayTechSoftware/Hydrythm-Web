---
title: Sterowanie sprzętem
description: Otwórz stronę urządzenia, żeby zobaczyć jego stan na żywo i nim sterować: gniazda, pompy, głowice dozujące i testery.
section: Cora Mobile
reviewed: 2026-09-30
order: 11
group: Equipment
---

Każde podłączone urządzenie ma w Corze własną stronę. Widać na niej stan na żywo i wszystkie ustawienia, które urządzenie obsługuje. Otworzysz ją w zakładce **Urządzenia**.

![Strona urządzenia](img/mobile-device-detail.webp "Odczyty na żywo na górze, niżej ustawienia, które obsługuje urządzenie.")

Każda strona urządzenia wygląda podobnie. Na górze jest opis urządzenia, potem rząd odczytów na żywo, stan zgłaszany przez urządzenie, a na końcu przyciski sterowania. Dzwonek na pasku tytułu ustawia progi alertów dla tego urządzenia. Więcej w [Materiałach eksploatacyjnych](/help/mobile-consumables).

:::warning Te przyciski sterują prawdziwym sprzętem
Nie ma podglądu ani cofania. Niektóre przyciski najpierw proszą o potwierdzenie.
:::

## Co się dzieje po wysłaniu polecenia

Polecenie nie zawsze się udaje. Cora nie zakłada, że się udało, tylko mówi, który z czterech wyników wystąpił:

| Wynik | Co oznacza |
|---|---|
| **Potwierdzono** | Sprzęt potwierdził zmianę i zgłosił nowy stan |
| **Niepotwierdzone** | Polecenie zostało wysłane, ale nic nie wróciło. **To znaczy „nie wiemy”, a nie „zadziałało”**. Sprawdź stan na samym urządzeniu |
| **Odmówiono** | Coś zablokowało polecenie (reguła bezpieczeństwa, blokada albo sam sprzęt) albo żadne urządzenie Cora nie odebrało go na czas. Polecenie anulowano i nic się nie wykonało |
| **Bez zmian** | Sprzęt już był w żądanym stanie |

Każdy wynik trafia do [Aktywności](/help/mobile-activity) razem z informacją, skąd przyszło polecenie.

## Neptune Apex

Na stronie Apex są Twoje sondy i gniazda.

- **Sondy** przekazują odczyty do Cory jako źródła, które możesz umieścić na pulpicie.
- **Gniazda** mają trzy stany: **AUTO**, **WYŁ.** i **WŁ.** AUTO oddaje sterowanie Twojemu programowi w Apex.
- **Zamontowane moduły** (Trident, DŌS i inne) mają własne strony.

## Trident

Strona pokazuje bieżący stan testu, ilość pozostałego odczynnika i poziom wody odpadowej. Stąd też uruchomisz test.

Możesz tu ustawić próg alertu dla liczby pozostałych testów. Cora ostrzeże Cię wtedy, zanim skończy się odczynnik. Więcej w [Materiałach eksploatacyjnych](/help/mobile-consumables).

## DŌS

DŌS QD działa tak samo jak DŌS i wszystko poniżej dotyczy obu. Gdy Cora Max odczytuje Twój Apex, głowice dozujące są na stronie DŌS, nigdy na liście gniazd.

Przy każdej głowicy widać, co dozuje, jej harmonogram, ile podała dzisiaj, ile zostało w pojemniku i **Zasięg**, czyli na ile dni wystarczy płynu przy obecnym tempie.

Dla każdej głowicy możesz:

- **Wstrzymaj** albo **Wznów** jej harmonogram
- **Napełnij**, czyli podać Corze, że pojemnik jest znów pełny, albo wpisać, ile w nim jest
- **Dawkuj teraz**, czyli podać odmierzoną dawkę ręcznie

:::note Harmonogramy edytujesz w Apex Fusion
Cora pokazuje harmonogram i śledzi, ile już podano, ale go nie zmienia. Harmonogram, tempo i liczbę dawek zmieniasz w aplikacji Apex Fusion. Wstrzymywanie, napełnianie i ręczne dozowanie działają tutaj.
:::

:::note Zanim zadozujesz ręcznie, zmierz głowicę
Cora nie zadozuje ręcznie z głowicy, która nie była zmierzona. Przyciski **Zmierz, aby dozować** i **Zmierz ponownie** są na Cora Max, który dozuje dla danego akwarium. Cora włącza głowicę na dwadzieścia sekund, Ty mierzysz, ile wypłynęło, a Cora wylicza prawdziwe tempo głowicy. Jeden pomiar wystarcza dla wszystkich Cora Max i Cora Mobile. Zmierz więc każdą głowicę raz i powtórz pomiar po wymianie wężyka.
:::

:::warning DŌS dozuje dalej z pustego pojemnika
Urządzenie nie ma czujnika poziomu i samo się nie zatrzyma. Ustaw alert uzupełnienia na stronie głowicy, żeby Cora ostrzegła Cię, zanim pojemnik się opróżni.
:::

### Do czego służy głowica

Każda głowica ma ustawiony **typ użycia**. Dzięki temu Cora wie, co głowica robi, i dobrze o niej mówi. Do wyboru są: **Suplement**, **Podmiana wody: nowa słona woda wchodzi**, **Podmiana wody: stara woda wychodzi**, **Kalkwasser**, **Reaktor wapniowy**, **Pokarm**, **Dolewka** i **Inne**. Typ ustawiasz w polu **Używana do** w ustawieniach głowicy.

Dwa typy dla podmiany wody działają **w parze**. W jednej głowicy ustaw **Sparowana głowica** na tę drugą, która przenosi wodę w przeciwną stronę. Cora potraktuje je wtedy jako jedną parę do podmiany wody.

Każda głowica ma też limit **Największa dawka ręczna**. Chroni on przed literówką, przez którą ręczna dawka byłaby dużo większa niż planowana. Duże dawki ręczne są dostępne dopiero wtedy, gdy tempo głowicy zmierzono prawdziwym testem przy akwarium, i dopiero po włączeniu **Duże dawki (Beta)** w ustawieniach głowicy. Domyślnie jest wyłączone: włącz je dopiero po obejrzeniu pierwszej dużej dawki wykonanej przy akwarium.

## Red Sea ReefBeat

Każde urządzenie ma stronę dopasowaną do tego, czym jest:

| Urządzenie | Co pokazuje strona | Co możesz zrobić |
|---|---|---|
| **ReefDose** | Każdą głowicę, jej pojemnik i to, ile podała | Dla każdej głowicy: **Dawka dzienna**, **Pozostało w butelce**, **Dawkuj teraz** i **Aktywuj harmonogram**, a do tego pełny edytor **Plan dozowania** *(beta)*. Ustawić alerty uzupełnienia dla każdej głowicy |
| **ReefATO+** | Poziom w zbiorniku i pracę dolewki | Ustawić alert zbiornika. Zapytać Asystenta, na ile dni starczy zbiornika |
| **ReefMat** | Ile zostało rolki, w dniach i metrach | Przewinąć rolkę, ustawić alert uzupełnienia, a w wersji beta włączyć zaplanowany posuw, ustawić model i pozycję silnika oraz zarejestrować nową rolkę |
| **ReefRun** | Prędkość i stan pompy powrotnej i pompy odpieniacza | Zmienić prędkość, włączyć albo wyłączyć pompę, zmienić ustawienia odpieniacza i edytować pełny program prędkości *(beta)* |
| **ReefControl** *(beta)* | Jego sondy temperatury, pH, zasolenia i ORP | Podejrzeć odczyty |
| **ReefWave**, **ReefLED** *(beta)* | Jego bieżący tryb | Na razie tylko do podglądu |

**ReefRun to sterownik pompy powrotnej i pompy odpieniacza**, a nie pompa cyrkulacyjna. **ReefControl Power** *(beta)* pokazuje swoje gniazda jako gniazda sterowane z tego samego panelu co gniazdo Apex, tylko włącz albo wyłącz. Automatyczny tryb dla nich jeszcze nie działa.

## Edytowanie planu ReefDose albo programu ReefRun *(beta)*

Dotknij ikony kalendarza na stronie ReefDose albo ReefRun, żeby otworzyć jego plan.

Plan ReefDose to dzienna suma podzielona na maksymalnie cztery przedziały czasowe. Każdy przedział ma czas rozpoczęcia i zakończenia, liczbę dawek do podania i prędkość: **Cichy**, **Normalny** albo **Szybki**. Dodawaj i usuwaj przedziały, a potem zapisz. Cora pokazuje, co zamierza wysłać, i prosi o potwierdzenie, zanim zastąpi cały plan głowicy.

Program ReefRun to maksymalnie sześć segmentów na jednym porcie pompy. Każdy segment ma czas rozpoczęcia i prędkość, a do tego może dodać krótki impuls. Prędkość to albo 0, albo od 5% wzwyż. Zapis też prosi o potwierdzenie i zastępuje cały program pompy.

Oba edytory najpierw odczytują plan, który już jest na urządzeniu, więc edytujesz to, co naprawdę tam jest, a nie pusty formularz.

## Ustawienia ReefMat *(beta)*

Dotknij ikony koła zębatego na stronie ReefMat, żeby zobaczyć trzy kolejne ustawienia.

- **Zaplanowany posuw** włącza posuw o stałej porze, niezależny od czujnika automatycznego posuwu, który już jest na stronie. Włącz go i ustaw, jak często i o ile mata ma się przesuwać przy każdym posuwie.
- **Model ReefMat** i **Pozycja silnika** (**Lewa** albo **Prawa**) mówią Corze, jakie urządzenie i w jakiej orientacji masz.

Po założeniu nowej rolki poinformuj o tym Corę przyciskiem **Nowa rolka**: podaj jej grubość, a jeśli znasz, także zewnętrzną średnicę. To coś innego niż **Przewiń rolkę**, który tylko przesuwa matę, którą już masz założoną.

Urządzenie może zatrzymać się samo, np. pompa ReefRun, gdy kubek odpieniacza się zapełni. Wtedy jego strona mówi, dlaczego, i podpowiada, co zrobić:

| Urządzenie | Komunikat na stronie | Dotknij |
|---|---|---|
| ReefRun | Która pompa stanęła i dlaczego, np. *Pełny kubek. Opróżnij go, a potem wznów.* | **Wznów** |
| ReefRun albo ReefMat | **Zatrzymanie awaryjne** | **Usuń stan awaryjny** |
| ReefMat | **Mata zablokowana**, **Błąd instalacji** albo **Błąd konfiguracji** | **Wznów** |
| ReefMat | *Załaduj nową rolkę, a potem potwierdź to w aplikacji Red Sea.* | **Nowa rolka już załadowana** |
| ReefMat | **Czujnik wymaga wyczyszczenia** | **Czujnik wyczyszczony** |
| ReefDose | **Awaria głowicy** z nazwą głowicy | **Resetuj** |
| ReefATO+ | **Usuń awarię** | **Wznów** |

Część z nich najpierw prosi o potwierdzenie. Gdy jesteś poza siecią urządzenia, Cora Mobile wysyła polecenie przez Cora Max przy akwarium. Jeśli żaden Cora Max nie może tego zrobić, strona mówi to wprost i nic nie zostaje wysłane.

## Pompy Jecod

Strona pompy pokazuje bieżący tryb i intensywność. Możesz zmienić jedno i drugie.

Możesz też:

- **Skopiuj harmonogram do…**, żeby przenieść harmonogram tej pompy na inną
- **Zapisz harmonogram jako…** i **Zapisane harmonogramy…**, żeby zachować harmonogram i później go przywrócić
- **Udostępnij ten harmonogram** i **Wklej kod harmonogramu…**, żeby przenieść harmonogram do innego systemu jako krótki kod

## Maxspect

:::note Obsługa Maxspect jest w wersji beta
Obsługę gyre Maxspect wciąż testujemy i rozwijamy. Część ustawień może być ograniczona, a to, co tu widzisz, może się zmienić z kolejną aktualizacją. Jeśli coś nie działa tak, jak opisano, napisz do nas przez [Pomoc](/help/mobile-support).
:::

Strona gyre pokazuje, czy gyre pracuje, wzór fali i prędkość **Gyre A** i **Gyre B** oraz czas ostatniego odczytu. Możesz tu:

- Włączyć albo wyłączyć gyre przełącznikiem obok jego stanu. Cora najpierw prosi o potwierdzenie. Wyłączenie zatrzymuje oba gyre, a harmonogram zostaje bez zmian.
- Dotknąć **Zmień ustawienia**, żeby ustawić wzór fali i prędkość pompy każdego gyre (oraz czas trwania, jeśli dany wzór go ma) i to, czy oba gyre są połączone. Cora pokazuje, co się zmieni, i przed zastosowaniem prosi o potwierdzenie. Tryb naprzemienny ustawiasz w aplikacji Maxspect. Gyre, który z niego korzysta, zachowuje swoje narastania i czasy utrzymania.
- Dotknąć **Ustaw program**, gdy programu zapisanego w gyre nie da się odczytać. Ten przycisk ustawia oba gyre, żeby gyre mógł znowu ruszyć.
- Zobaczyć program dnia gyre na karcie **Harmonogram**. Służy tylko do podglądu, a harmonogram ustawiasz w aplikacji Maxspect.
- Sprawdzić **Stan pompy**: kiedy pompa będzie wymagać czyszczenia (pompa sama odlicza ten czas), jaki prąd pobiera głowica A, które głowice są zamontowane i jaki jest firmware. Dotknij **Odczytaj**, żeby pobrać te dane.

:::note Jak Cora Mobile łączy się z gyre
Jeśli akwarium obsługuje Cora Max, Cora Mobile łączy się przez niego, także poza domem. **Zmień ustawienia** zaczyna wtedy od ostatniego odczytu z tego Cora Max. W przeciwnym razie telefon łączy się z gyre bezpośrednio i musi być w jego sieci. Otwarcie strony odczytuje wtedy gyre. Jeśli strona pokazuje starszy zapisany odczyt, przycisk **Zmień ustawienia** pozostaje ukryty, dopóki nie odświeżysz strony.
:::

## GHL ProfiLux i Mitras

:::note Obsługa GHL jest w wersji beta
Obsługę GHL wciąż testujemy i rozwijamy. Część odczytów albo funkcji sterowania może jeszcze nie działać, a to, co tu widzisz, może się zmienić z kolejną aktualizacją. Jeśli coś nie działa tak, jak opisano, napisz do nas przez [Pomoc](/help/mobile-support).
:::

Strona kontrolera pokazuje jego sondy, gniazda, dozowniki i czujniki poziomu, a w modelach Director także wyniki testów KH i jonów.

Sterowanie pozostaje wyłączone, dopóki nie włączysz **Zezwól na sterowanie z Cora (Beta)** na stronie urządzenia. Domyślnie jest wyłączone, a jego włączenie pozwala Corze wysyłać do tego kontrolera polecenia pauzy karmienia, konserwacji, wymiany wody, burzy, oświetlenia, wartości docelowych i gniazd.

Gdy jest włączone:

- Gniazdo można ustawić na **Zawsze włączone**, **Zawsze wyłączone** albo **Powrót do automatycznego**, żeby oddać je z powrotem programowi kontrolera.
- Wartość docelowa, na przykład temperatura albo pH, pokazuje swój dozwolony zakres i odrzuca wartość spoza niego.

:::warning Zmiana gniazda albo wartości docelowej jest zapisywana na samym kontrolerze
Nie jest przechowywana tylko w Corze. Ustawienie gniazda na Zawsze włączone albo Zawsze wyłączone zastępuje własne programowanie kontrolera dla tego gniazda, dopóki nie wybierzesz Powrót do automatycznego.
:::

Jeśli gniazdo albo wartość docelowa wyglądają, jakby należały do grzałki albo pompy powrotnej, Cora prosi o podwójne potwierdzenie przed wysłaniem.

Jeśli pojemnik dozownika zaczyna się kończyć, Cora ostrzega tak samo jak przy innych materiałach eksploatacyjnych. Domyślnie próg to 20% pojemności, a zmienisz go w regule dozownika w [Centrum alertów](/help/mobile-alerts).

:::note ProfiLux mini
Mini może tylko przełączać swoje gniazda. Wszystko inne tutaj, na przykład wartości docelowe i pauza na karmienie, wymaga ProfiLux 3, 4 albo Mitras.
:::

Jeśli kontroler odrzuci zmianę, sprawdź, czy jego API GHL jest włączone z pełnym dostępem. GHL wyłącza to po każdej aktualizacji firmware. Kroki opisuje [Rozwiązywanie problemów](/help/troubleshooting).

## HYDROS

:::note Obsługa HYDROS jest w wersji beta
Obsługę HYDROS wciąż testujemy i rozwijamy. Część odczytów albo funkcji sterowania może jeszcze nie działać, a to, co tu widzisz, może się zmienić z kolejną aktualizacją. Jeśli coś nie działa tak, jak opisano, napisz do nas przez [Pomoc](/help/mobile-support).
:::

To, co tu widzisz, zależy od użytego klucza połączenia. Klucz **Odczyt** daje tylko jego wejścia. Klucz **Zapis** dodaje wyjścia, tryby, dozowanie i komendy testera, a także baner na stronie przypominający, jakiego klucza dotyczy.

Przy kluczu zapisu sterowanie też pozostaje wyłączone, dopóki nie włączysz **Zezwól na kontrolę z Cora (Beta)** na stronie urządzenia. Domyślnie jest wyłączone.

Gdy jest włączone, strona może pokazywać:

- **Wyjścia**: przełącznik dla wyjścia typu włącz/wyłącz, suwak dla poziomu, na przykład pompy albo światła, albo przycisk dla flagi. Nadpisane wyjście pokazuje **Nadpisane** z przyciskiem **Powrót do harmonogramu**, który oddaje je z powrotem jego własnemu programowi.
- **Tryby**, na przykład Karmienie albo Wymiana wody, jako rząd opcji. Dotknięcie jednej z nich prosi o potwierdzenie.
- **Głowice dozujące**, każda z przyciskiem **Dozuj** i pozycją **Ustawienia głowicy**, gdzie ustawiasz jej własne limity: największą dawkę ręczną i dzienny limit. Prośba o więcej niż limit głowicy, albo więcej niż zostało jej z dziennego limitu na dany dzień, jest odrzucana z podanymi liczbami w komunikacie.
- **Komendy testera** dla podłączonego iV albo Maven: uruchamiane przyciskiem i najpierw potwierdzane.

Jeśli kontroler nie zgłaszał się od jakiegoś czasu, strona to pokazuje, a odczyty mogą być nieaktualne. Polecenie wysłane, gdy wygląda na offline, w ogóle nie zostaje wysłane, o czym strona też informuje.

## Co się dzieje po zmianie

Każda zmiana trafia do [Aktywności](/help/mobile-activity) razem z miejscem, z którego ją zlecono. Jeśli urządzenie nie przyjmie zmiany, to też zostanie tam zapisane.

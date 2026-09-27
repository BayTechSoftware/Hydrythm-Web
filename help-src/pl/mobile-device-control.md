---
title: Kontrola sprzętu
description: Otwórz własną stronę urządzenia, aby zobaczyć jego stan na żywo i sterować nim: gniazda, pompy, głowice dozujące i testery.
section: Cora Mobile
reviewed: 2026-09-27
order: 11
group: Equipment
---

Podłączony sprzęt ma swoją własną stronę w Corze, pokazującą stan na żywo i oferującą wszystkie kontrolki, jakie to urządzenie wspiera. Otwórz taką stronę z zakładki **Urządzenia**.

![Strona urządzenia](img/mobile-device-detail.webp "Odczyty na żywo na górze, potem kontrolki wspierane przez to urządzenie.")

Każda strona urządzenia ma ten sam układ: identyfikacja na górze, rząd odczytów na żywo, stan zgłaszany przez urządzenie, a potem jego kontrolki. Dzwonek na pasku tytułu ustawia progi alertów dla tego urządzenia; zobacz [Materiały eksploatacyjne](/help/mobile-consumables).

:::warning Te kontrolki działają na żywym sprzęcie
Nie ma podglądu i nie ma cofnięcia. Niektóre kontrolki proszą też najpierw o potwierdzenie.
:::

## Co się dzieje, gdy wysyłasz polecenie

Polecenie nie zawsze się powiedzie, i Cora mówi Ci, które z czterech zdarzeń nastąpiło, a nie zakłada domyślnie:

| Wynik | Znaczy |
|---|---|
| **Potwierdzono** | Sprzęt potwierdził zmianę i zgłosił swój nowy stan |
| **Niepotwierdzone** | Polecenie zostało wysłane, ale nic nie zgłoszono z powrotem. **To znaczy "nie wiemy", nie "zadziałało"**; sprawdź stan samego urządzenia |
| **Odmówiono** | Coś odmówiło (reguła bezpieczeństwa, blokada albo sam sprzęt) albo żadne urządzenie Cora nie odebrało go na czas, więc zostało anulowane i nic nie zostało wykonane |
| **Bez zmian** | Sprzęt był już w stanie, o który poprosiłeś |

Każdy wynik jest zapisywany w [Aktywności](/help/mobile-activity) wraz z tym, co go spowodowało.

## Neptune Apex

Strona Apex wypisuje Twoje sondy i gniazda.

- **Sondy** zgłaszają się do Cory jako źródła i można je umieścić na pulpicie.
- **Gniazda** przełączają się między **Auto**, **Wyłączone** i **On**. Auto przekazuje kontrolę Twojemu programowaniu Apex.
- **Zamontowane moduły** (Trident, DŌS i inne) mają każdy swoją własną stronę.

## Trident

Pokazuje aktualny stan testu, poziomy pozostałego reagentu i wody odpadowej oraz pozwala rozpocząć test.

Na tej stronie możesz ustawić próg alertu dla liczby pozostałych testów, aby Cora ostrzegła Cię, zanim skończy się reagent. Zobacz [Materiały eksploatacyjne](/help/mobile-consumables).

## DŌS

DŌS QD działa dokładnie jak DŌS, i wszystko tutaj dotyczy obu. Gdy Cora Max odczytuje Twój Apex, głowice dozujące pojawiają się na stronie DŌS, nigdy na liście gniazd.

Każda głowica dozująca pokazuje, co dozuje, swój harmonogram, co dozowała dzisiaj, ile zostało w pojemniku i jej **runway**: ile dni to wystarczy przy aktualnym tempie.

Dla każdej głowicy możesz:

- **Wstrzymaj** i **Wznów** jej harmonogram
- **Napełnij**: powiedzieć Corze, że pojemnik jest znowu pełny, albo ustawić w nim objętość
- **Dawkuj teraz**: zmierzoną, ręczną dawkę

:::note Harmonogramy edytuje się w Apex Fusion, nie tutaj
Cora pokazuje harmonogram i śledzi, co zostało zdozowane, ale go nie zmienia. Edytowanie harmonogramu, tempa dawki albo liczby dawek odbywa się w aplikacji Apex Fusion. Wstrzymywanie, napełnianie i dozowanie ręczne są tutaj wszystkie wspierane.
:::

:::note Zmierz głowicę, zanim zdozujesz nią ręcznie
Cora nie zdozuje głowicą ręcznie, aż zostanie zmierzona. **Zmierz, aby dozować** i **Zmierz ponownie** znajdują się na Cora Max, który dozuje dla danego akwarium: Cora uruchamia głowicę na dwadzieścia sekund, Ty mierzysz, co wyszło, a Cora wylicza rzeczywiste tempo głowicy. Jeden pomiar obsługuje każde Cora Max i Cora Mobile, więc zmierz każdą głowicę raz, i ponownie po zmianie jej przewodów.
:::

:::warning DŌS dozuje dalej, gdy pojemnik jest pusty
Jednostka nie ma czujnika poziomu i nie zatrzymuje się sama. Ustaw alert uzupełnienia na stronie głowicy, aby Cora ostrzegła Cię, zanim pojemnik wyschnie.
:::

### Do czego służy każda głowica

Każda głowica ma ustawiony **typ użycia**, dzięki czemu Cora wie, co ona robi, i może o niej mówić poprawnie: **Suplement**, **Podmiana wody: nowa słona woda wchodzi**, **Podmiana wody: stara woda wychodzi**, **Kalkwasser**, **Reaktor wapniowy**, **Pokarm**, **Dolewka** albo **Inne**. Ustawiasz to w **Używana do** w ustawieniach głowicy.

Dwa typy użycia dla podmiany wody są przeznaczone do **parowania**: ustaw **Sparowana głowica** jednej głowicy na drugą, przenoszącą wodę w drugą stronę, a Cora będzie traktować je jako jedną parę do podmiany wody, a nie dwie niepowiązane głowice.

Każda głowica ma też sufit **Największa dawka ręczna**, aby błędnie wpisana ręczna dawka nie była dużo większa niż zamierzona. Duże dawki ręczne stają się dostępne tylko wtedy, gdy tempo głowicy zostało zmierzone względem rzeczywistego testu przy akwarium.

## Red Sea ReefBeat

Każda jednostka ma stronę odpowiednią do tego, czym jest:

| Jednostka | Strona pokazuje | Możesz |
|---|---|---|
| **ReefDose** | Każdą głowicę, jej pojemnik i to, co zdozowała | Dla każdej głowicy: **Dawka dzienna**, **Pozostało w butelce**, **Dawkuj teraz** i **Aktywuj harmonogram**. Ustaw alerty uzupełnienia dla każdej głowicy |
| **ReefATO+** | Poziom zbiornika i aktywność dolewki | Ustawić alert zbiornika |
| **ReefMat** | Pozostałą rolkę, w dniach i metrach | Przesunąć rolkę, ustawić alert uzupełnienia |
| **ReefRun** | Prędkość i stan pompy powrotnej i skimmerowej | Zmienić prędkość, przełączyć pompę, dostosować ustawienia skimmera |

**ReefRun to kontroler pompy powrotnej i skimmerowej**, a nie pompa falowa.

Jednostka może zatrzymać się sama, na przykład pompa ReefRun, gdy kubek skimmera się napełni. Gdy to się stanie, jej strona mówi, dlaczego, i proponuje rozwiązanie:

| Jednostka | Strona mówi | Dotknij |
|---|---|---|
| ReefRun | Która pompa się zatrzymała i czemu, na przykład *Pełny kubek. Opróżnij go, a potem wznów.* | **Wznów** |
| ReefRun lub ReefMat | **Zatrzymanie awaryjne** | **Usuń stan awaryjny** |
| ReefMat | **Mata zablokowana**, **Błąd instalacji** lub **Błąd konfiguracji** | **Wznów** |
| ReefMat | *Załaduj nową rolkę, a potem potwierdź to w aplikacji Red Sea.* | **Nowa rolka już załadowana** |
| ReefMat | **Czujnik wymaga wyczyszczenia** | **Czujnik wyczyszczony** |
| ReefDose | **Awaria głowicy**, z nazwą głowicy | **Resetuj** |
| ReefATO+ | **Usuń awarię** | **Wznów** |

Niektóre z nich proszą najpierw o potwierdzenie. Poza siecią jednostki Cora Mobile wysyła je przez Cora Max przy akwarium; jeśli żaden Cora Max nie może tego zrobić, strona mówi to wprost i nic nie zostaje wysłane.

## Pompy Jecod

Strona pompy pokazuje jej aktualny tryb i intensywność i pozwala zmienić obie te wartości.

Możesz też:

- **Skopiuj harmonogram do…**: skopiować harmonogram tej pompy na inną
- **Zapisz harmonogram jako…** i **Zapisane harmonogramy…**: zachować harmonogram i zastosować go później ponownie
- **Udostępnij ten harmonogram** i **Wklej kod harmonogramu…**: przenieść harmonogram między systemami jako krótki kod

## Maxspect

:::note Wsparcie dla Maxspect jest w wersji beta
Wsparcie dla gyre Maxspect jest wciąż testowane i rozwijane, więc niektóre kontrolki mogą być ograniczone, a to, co widzisz tutaj, może się zmienić między aktualizacjami. Jeśli coś nie działa tak, jak opisano, powiedz nam o tym w [Pomoc](/help/mobile-support).
:::

Strona gyre pokazuje, czy gyre działa, wzór fali i prędkość **Gyre A** i **Gyre B** oraz kiedy zostało to ostatnio odczytane. Z niej możesz:

- Włączyć lub wyłączyć gyre przełącznikiem przy jego stanie. Cora najpierw prosi o potwierdzenie. Wyłączenie zatrzymuje obydwa gyre i zachowuje harmonogram bez zmian.
- Dotknąć **Zmień ustawienia**, aby ustawić wzór fali i prędkość pompy każdego gyre (oraz czas trwania, dla wzoru, który go ma), i czy dwa gyre są połączone. Cora wypisuje, co się zmieni, i prosi o potwierdzenie przed zastosowaniem. Alternowanie ustawia się w aplikacji Maxspect: gyre je uruchamiające zachowuje swoje narastania i czasy trzymania.
- Dotknąć **Ustaw program** za to, gdy programu zapisanego na gyre nie można odczytać. Ustawia oba gyre, aby gyre mogło znowu wystartować.
- Zobaczyć program dnia gyre na karcie **Harmonogram**. Jest tylko do podglądu: harmonogram ustawiasz w aplikacji Maxspect.
- Sprawdzić **Stan pompy**: kiedy pompa będzie następnie wymagać czyszczenia (pompa sama odlicza ten czas), pobór prądu przez głowicę A, które głowice są zamontowane, oraz firmware. Dotknij **Odczytaj**, aby to pobrać.

:::note Jak Cora Mobile dociera do gyre
Gdy akwarium obsługuje Cora Max, Cora Mobile działa przez ten Cora Max, także wtedy, gdy jesteś poza domem, a **Zmień ustawienia** wychodzi od ostatniego odczytu tego Cora Max. W innym przypadku Twój telefon rozmawia z gyre bezpośrednio i musi być w sieci gyre. Otwarcie strony wtedy odczytuje gyre; jeśli strona pokazuje starszy zapisany odczyt, **Zmień ustawienia** zostaje ukryte, aż dotkniesz odświeżenia.
:::

## Co się dzieje po zmianie czegoś

Każda zmiana jest zapisywana w [Aktywności](/help/mobile-activity) wraz z miejscem, z którego pochodziło żądanie. Jeśli urządzenie nie przyjmie zmiany, niepowodzenie jest tam także zapisywane.

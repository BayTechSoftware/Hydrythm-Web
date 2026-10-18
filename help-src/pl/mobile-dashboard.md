---
title: Jak czytać panel
description: Jak czytać panel Cory: widżety, wiek i źródła odczytów, znaczenie kolorów i karty, które pojawiają się i znikają.
section: Cora Mobile
reviewed: 2026-10-18
order: 6
group: Your dashboard
---

Pulpit to siatka **widżetów** dla jednego akwarium. Każdy widżet pokazuje jedną rzecz. Ty decydujesz, co na nim jest, tak jak opisuje [Edytowanie panelu](/help/mobile-dashboard-editing).

![Pulpit Cora Mobile](img/mobile-dashboard.webp "Nagłówek akwarium i karta Reef Buddy, a pod nimi wskaźniki, wartości, wykresy i kafelki urządzeń.")

## Nagłówek akwarium {#the-tank-header}

Każdy panel zaczyna się od:

- Nazwy akwarium z małym symbolem obok. Dotknij nazwy, żeby zmienić nazwę akwarium. Tylko to robi.
- **Karmienie**, tylko przy akwarium z Neptune Apex. Otwiera **Tryb karmienia** z cyklami Twojego Apex od **Karmienie A** do **Karmienie D**. To Twój Apex decyduje, co się wstrzymuje i kiedy wraca, tak jak to w nim ustawiono. Gdy cykl działa, przycisk pokazuje, który, na przykład **Karmienie A**. Dotknij go i wybierz **Odwołaj karmienie**, żeby zakończyć go wcześniej. Poza domem polecenie wysyła za Ciebie Cora Max przy akwarium.
- Ikony gazety, która otwiera najnowsze podsumowanie **Reef Buddy**.
- Ikony udostępniania, która tworzy zdjęcie akwarium. Zobacz [Udostępnianie akwarium](/help/mobile-sharing).
- Linijki, która otwiera **Jednostki** dla tego akwarium. Zobacz [Profil akwarium](/help/mobile-tank-profile#units).
- Ołówka po prawej, który otwiera [profil akwarium](/help/mobile-tank-profile).

:::note Trzy podobne elementy
Nazwa akwarium zmienia nazwę akwarium. Ołówek po prawej otwiera **profil** akwarium. Żeby edytować sam panel, dotknij **Edytuj panel** tuż pod widżetami.
:::

Jeśli masz więcej niż jedno akwarium, przesuwaj palcem w bok, żeby się między nimi przełączać. Zobacz [Zarządzanie akwariami](/help/mobile-tanks).

## Karta Reef Buddy {#the-reef-buddy-card}

Nad widżetami karta podsumowuje ostatnie podsumowanie dnia. Pokazuje nagłówek, wynik na 100, gdy Cora ma dość danych, datę, z której pochodzi, oraz liczbę spostrzeżeń i dryfujących odczytów. Dotknij jej, żeby otworzyć całe podsumowanie, albo zamknij ją przyciskiem **×**. Nowa karta pojawi się z następnym podsumowaniem. Więcej w [Reef Buddy](/help/mobile-reef-buddy).

## Jak czytać widżet parametru {#how-to-read-a-parameter-widget}

Widżet **zmierzonego parametru** zawsze pokazuje te same trzy rzeczy w tych samych miejscach. Kafelki urządzeń i sterowania, takie jak gniazdo, dozownik albo pompa, pokazują zamiast tego swój stan, bo nie stoi za nimi jeden odczyt.

Wartość to sam odczyt, duży i na środku.

Wiek jest pod nią albo obok, jako `teraz`, `1g` albo `2d`. Mówi, jak dawno źródło ostatnio potwierdziło tę wartość, a nie kiedy ostatnio odświeżył się ekran. Dla sondy to chwila, gdy jej urządzenie ostatnio się zgłosiło, więc stały odczyt z działającej sondy pozostaje świeży, nawet gdy liczba się nie zmienia. Dla wyniku testu kropelkowego albo ICP to chwila wykonania testu. Wiek, który przy sondzie ciągle rośnie, oznacza, że jej urządzenie przestało raportować.

Znaczek źródła to mały symbol obok wieku. Pokazuje, skąd pochodzi liczba: z sondy, kontrolera, wyniku z laboratorium albo od Ciebie z testu kropelkowego. Dotknij widżetu, żeby zobaczyć pełną nazwę źródła i niedawną historię.

:::note Dlaczego wiek ma znaczenie
Idealny odczyt alkaliczności sprzed czterech dni nie jest Twoją alkalicznością dzisiaj. Każda wartość pokazuje swój wiek, żeby różnicę było widać od razu.
:::

## Kolory {#colours}

Cora używa niewielu kolorów i każdy zawsze znaczy to samo:

| Kolor | Znaczenie |
|---|---|
| Zielony | Spokojnie w zakresie dla tego parametru |
| Pomarańczowy | Blisko granicy. **Zwykle nadal w zakresie**, w jego ostatniej dziesiątej części |
| Czerwony | Poza granicą. Warto zareagować |
| Szary | Brak oceny. Nie ma świeżego odczytu albo zakresu, według którego można go ocenić |

:::note Pomarańczowy zwykle znaczy „na razie dobrze, ale coś dryfuje”
Pomarańczowy to margines. Odczyt w zakresie, ale w jego ostatnich 10%, robi się pomarańczowy, więc widzisz dryf, gdy jest jeszcze czas na reakcję.

Są dwa doprecyzowania.

**Zakres ustawiony przez Ciebie to twarda granica.** Po jej przekroczeniu widżet od razu robi się czerwony, bez pomarańczowego marginesu. Zakres **podany przez Corę** jest łagodniejszy. Przez pierwsze 10% poza granicą widżet jest pomarańczowy, a dalej czerwony.

**Limit jednostronny**, na przykład górna granica dla zanieczyszczenia albo dolna dla biogenu, jest oceniany tylko na górnej krawędzi. Dlatego miedź na zerze jest zielona i nie robi się pomarańczowa za to, że leży przy dole skali.
:::

Widżet z pomarańczową albo czerwoną ramką wymaga uwagi. Ramkę dostaje cały widżet, więc zauważysz go podczas przewijania.

Żeby zmienić zakres, przytrzymaj widżet. Więcej w [Alertach i progach](/help/mobile-alerts).

## Karty, które pojawiają się i znikają {#cards-that-come-and-go}

Niektóre karty pojawiają się tylko wtedy, gdy jest coś do powiedzenia. Większość z nich jest między nagłówkiem a widżetami.

| Karta | Kiedy się pojawia | Co dotknąć |
|---|---|---|
| **Zaczynasz nowe akwarium?** | Przy akwarium bez żadnych odczytów. Po rozpoczęciu zmienia się w **Kontynuuj cyklowanie** | Kartę, żeby zacząć cyklowanie z przewodnikiem. Zobacz [Ścieżki z przewodnikiem](/help/mobile-journeys) |
| **Parametry akwarium** z *Jeszcze brak odczytów* | Akwarium nie ma jeszcze odczytów | **Skonfiguruj akwarium** |
| *Nie udało się połączyć z Twoimi odczytami: wyświetlanie danych z pamięci podręcznej.* | Cora nie może wczytać najnowszych odczytów, często z braku połączenia | **Spróbuj ponownie** |
| **Wynik laboratoryjny od {lab} czeka na Ciebie.** | Laboratorium przysłało wynik, a Cora musi wiedzieć, do którego akwarium należy | **Wybierz akwarium**. Zobacz [ICP i raporty zdrowia](/help/mobile-icp-health) |
| Zachęta do profilu (**Odblokuj lepsze spostrzeżenia**) | Profil akwarium jest wypełniony w mniej niż 80% | Kartę, żeby dalej wypełniać profil |
| **Okres próbny Cora Advanced: pozostało 9 dni** | Ostatnie dni okresu próbnego | Kartę albo **Zachowaj Advanced**. Zobacz [Plany i subskrypcje](/help/mobile-plans) |
| **Reef Buddy** | Podsumowanie jest gotowe | Kartę |
| **Jak zwykle karmisz?** | Nie ustawiono planu karmienia | **Ustaw plan karmienia** |
| *Odczyty Red Sea przestały się aktualizować.* | Nic nie odczytuje urządzeń Red Sea tego akwarium | Zobacz [Alerty i progi](/help/mobile-alerts) |
| **Zapisz pierwszy test wody** | Brak odczytów i podłączonego sprzętu, pod widżetami | Kartę. Zobacz [Konfiguracja Cora Mobile](/help/mobile-setup#the-first-test-card) |

## Pod widżetami {#below-the-widgets}

![Dół panelu w Cora Mobile](img/mobile-dashboard-foot.webp "Edytuj panel, przyciski Zapisz parametry, Historia parametrów i Karmienie oraz skróty do czterech rodzajów zapisków.")

Od góry do dołu znajdziesz:

- Linijkę z informacją, kiedy panel ostatnio się zaktualizował i z jakich źródeł korzystał, a obok niej **Edytuj panel**. To otwiera [edytor panelu](/help/mobile-dashboard-editing).
- Kartę **Zapisz pierwszy test wody**, przy akwarium bez odczytów i bez podłączonego sprzętu.
- **Zapisz parametry**, do ręcznego wpisywania wyników testów kropelkowych.
- **Historia parametrów**, żeby otworzyć historię dowolnego parametru, który ma dane, nawet takiego bez widżetu. Zobacz [Szczegóły parametru](/help/mobile-metric-detail).
- **Karmienie**, żeby zapisać karmienie, które odbiega od planu. Zobacz [Dziennik](/help/mobile-journal).
- **Dziennik · Alerty · Konserwacja · Obsada**, skróty do tych miejsc dla tego akwarium.

## Dotknięcie i przytrzymanie {#tapping-through}

Dotknij widżetu parametru, żeby otworzyć jego szczegóły. Zobaczysz pełną historię na wykresie, każde źródło, które go zgłaszało, i pasmo alertu. Stamtąd porównasz źródła, wykluczysz błędny odczyt albo zapiszesz konserwację sondy. Zobacz [Szczegóły parametru](/help/mobile-metric-detail).

**Przytrzymaj** widżet parametru, żeby ustawić jego zakres alertu prosto z panelu.

## Gdy widżet nie ma wartości {#if-a-widget-has-no-value}

Widżet pokazuje wartość, gdy ją dostanie. Jeśli jest pusty, zwykle chodzi o jedno z tych:

- Urządzenie jest offline. Sprawdź zakładkę **Urządzenia**.
- Parametr nie ma jeszcze źródła. Zapisz go ręcznie albo podłącz sprzęt, który go zgłasza.
- Dla tego parametru nigdy niczego nie zgłoszono ani nie zapisano.

Stary odczyt nie znika tylko dlatego, że jest starszy niż okno wykresu. Zostaje na widżecie razem z wiekiem, więc nieaktualna wartość wygląda na nieaktualną, a nie na brakującą.

W innych sprawach zajrzyj do [Rozwiązywania problemów](/help/troubleshooting#a-widget-shows-no-value).

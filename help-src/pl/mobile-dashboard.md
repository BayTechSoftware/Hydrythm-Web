---
title: Odczytywanie pulpitu
description: Jak odczytywać pulpit Cory: widżety, aktualność, źródła i co znaczą kolory.
section: Cora Mobile
reviewed: 2026-09-09
order: 5
group: Your dashboard
---

Pulpit to siatka **widżetów**, każdy pokazujący jedną rzecz o jednym akwarium. To, co się na nim znajdzie, zależy całkowicie od Ciebie; zobacz **[Edytowanie pulpitu](/help/mobile-dashboard-editing)**.

![Pulpit Cora Mobile](img/mobile-dashboard.webp "Wskaźniki, liczby, trendy i kontrolki na jednym ekranie.")

## Nagłówek akwarium

Na górze każdego pulpitu:

- **Nazwa akwarium**, z małym symbolem przy niej: to jest **szybka zmiana nazwy**, nic więcej
- **Karmienie**: wstrzymuje przepływ i skimming na czas karmienia, a potem wszystko przywraca
- **Reef Buddy**: otwiera dzisiejszy briefing
- **Udostępnij**: wysyła zrzut pulpitu
- **Ołówek po prawej stronie**: otwiera [profil akwarium](/help/mobile-tank-profile)

:::note Trzy podobne kontrolki, trzy miejsca docelowe
Symbol przy nazwie zmienia nazwę akwarium. Ołówek po prawej stronie otwiera **profil** akwarium. Edytowanie samego pulpitu to żadne z nich; to jest **Edytuj panel**, na *dole* pulpitu, pod widżetami.
:::

Przy więcej niż jednym akwarium przesuń palcem w bok, aby przechodzić między nimi.

## Karta Reef Buddy

Pod nagłówkiem karta podsumowuje najnowszy briefing: nagłówek, oceny **Stabilność** i **Dane** oraz liczbę wglądów. Dotknij jej, aby otworzyć cały briefing, albo zamknij ją przyciskiem **×**. Kolejny briefing pojawi się na nowej karcie.

## Jak odczytywać widżet parametru

Widżet pokazujący **zmierzony parametr** zawiera te same trzy elementy w tych samych miejscach. Kafelki urządzeń i kontrolek (gniazdo, jednostka dozująca, pompa) pokazują własny stan, bo nie stoi za nimi jeden konkretny odczyt.

**Wartość** to sam odczyt, duży i na środku.

**Wiek** znajduje się pod nią lub przy niej: `now`, `1h`, `2d`. To ile czasu temu wykonano odczyt, nie ile czasu temu odświeżył się ekran. Liczba, która nie zmieniła się od dwóch dni, pokazuje `2d`, i to jest informacja.

**Znaczek źródła** to mały symbol przy wieku. Mówi Ci, skąd pochodzi liczba: sonda, kontroler, wynik laboratoryjny albo Ty z testem kroplowym. Dotknij dowolnego widżetu, aby zobaczyć źródło wypisane wprost wraz z jego niedawną historią.

:::note Czemu wiek jest tak ważny
Perfekcyjny odczyt alkaliczności z czterech dni temu nie jest aktualnym odczytem alkaliczności. Wiek znajduje się przy każdej wartości, dzięki czemu widzisz różnicę na pierwszy rzut oka.
:::

## Kolory

Cora używa kolorów oszczędnie i zawsze w tym samym znaczeniu:

| Kolor | Znaczenie |
|---|---|
| Zielony | Komfortowo w zakresie dla danego parametru |
| Bursztynowy | Blisko granicy: **zwykle wciąż w zakresie**, w ostatniej jego dziesiątej części |
| Czerwony | Poza granicą i warto zareagować |
| Szary | Brak oceny: brak niedawnego odczytu albo brak zakresu, względem którego można ocenić |

:::note Bursztynowy zwykle znaczy "wciąż w porządku, ale coś się dzieje"
Bursztynowy to *margines*, nie przekroczenie. Odczyt wewnątrz zakresu, ale w ostatnich 10% jego szerokości, jest oznaczany bursztynowym kolorem celowo, aby dryf był widoczny, gdy jeszcze jest czas na reakcję, a nie w chwili, gdy staje się problemem.

Z tego wynikają dwa dodatkowe rozróżnienia.

**Zakres, który ustawiłeś samodzielnie, jest traktowany jako zadeklarowana granica.** Przekrocz go, a widżet od razu robi się czerwony: bez marginesu bursztynowego, bo tę linię wyznaczyłeś sam, świadomie. Zakres **dostarczony przez Corę** jest łagodniejszym odniesieniem: przekroczenie go pokazuje bursztynowy kolor przez pierwsze 10% poza granicą, a dalej robi się czerwony.

**Jednostronny limit** (sufit dla zanieczyszczenia albo podłoga dla substancji odżywczej) jest oceniany tylko na swojej górnej granicy, więc miedź na zero jest zielona, a nie bursztynowa za to, że leży blisko dołu skali.
:::

Widżet obrysowany bursztynowym lub czerwonym kolorem to taki, który wymaga uwagi. Obrys jest na widżecie, nie tylko na liczbie, więc jest widoczny podczas przewijania.

## Pod widżetami

![Dół pulpitu](img/mobile-dashboard-foot.webp "Edit dashboard, Log Parameters i skróty do czterech obszarów zapisów.")

Na dole pulpitu:

- **Edytuj panel**: otwiera [edytor pulpitu](/help/mobile-dashboard-editing)
- **Zapisz parametry**: pozwala ręcznie wpisać odczyty z testu kroplowego
- **Journal · Alerts · Maintenance · Livestock**: skróty do tych obszarów dla tego akwarium

Linia powyżej nich pokazuje, kiedy pulpit ostatnio się zaktualizował i z jakich źródeł korzystał.

## Przechodzenie w głąb

Dotknij dowolnego widżetu, aby otworzyć jego szczegóły: całą historię jako wykres, każde źródło, które ją zgłosiło, oraz aktualnie zastosowane progi. Odtąd możesz ręcznie zapisać nowy odczyt, zmienić zakres albo spojrzeć dalej w przeszłość.

## Jeśli widżet nie ma wartości

Widżet pokazuje wartość, gdy ją otrzyma. Gdy jest pusty, powód jest zwykle jednym z tych:

- Urządzenie jest offline; sprawdź zakładkę **Urządzenia**
- Parametr nie ma jeszcze źródła; zapisz go ręcznie albo podłącz sprzęt, który go zgłasza
- Parametr nigdy nie został zgłoszony ani zapisany; nic dla niego jeszcze nie zarejestrowano

Stary odczyt nie zniknie, bo okno wykresu jest krótsze niż jego wiek. Zostaje na widżecie z pokazanym wiekiem, więc nieaktualna wartość wygląda jak nieaktualna, a nie jak brakująca.

Zobacz **[Rozwiązywanie problemów](/help/troubleshooting)** w sprawach wykraczających poza to.

---
title: Jak czytać pulpit
description: Jak czytać pulpit Cory: widżety, wiek odczytów, źródła i znaczenie kolorów.
section: Cora Mobile
reviewed: 2026-09-09
order: 5
group: Your dashboard
---

Pulpit to siatka **widżetów**. Każdy pokazuje jedną rzecz z jednego akwarium. Co na nim będzie, zależy tylko od Ciebie. Więcej w **[Edytowaniu pulpitu](/help/mobile-dashboard-editing)**.

![Pulpit Cora Mobile](img/mobile-dashboard.webp "Wskaźniki, liczby, trendy i przełączniki na jednym ekranie.")

## Nagłówek akwarium

Na górze każdego pulpitu są:

- **Nazwa akwarium** z małym symbolem obok. Ten symbol służy tylko do **szybkiej zmiany nazwy**.
- **Karmienie** wstrzymuje przepływ i odpieniacz na czas karmienia, a potem wszystko przywraca.
- **Reef Buddy** otwiera dzisiejszy poranny briefing.
- **Udostępnij** wysyła zrzut pulpitu.
- **Ołówek po prawej** otwiera [profil akwarium](/help/mobile-tank-profile).

:::note Trzy podobne przyciski, trzy różne miejsca
Symbol przy nazwie zmienia nazwę akwarium. Ołówek po prawej otwiera **profil** akwarium. Sam pulpit edytujesz jeszcze gdzie indziej: przyciskiem **Edytuj panel** na *dole* pulpitu, pod widżetami.
:::

Jeśli masz kilka akwariów, przesuwaj palcem w bok, żeby przełączać się między nimi.

## Karta Reef Buddy

Pod nagłówkiem jest karta z podsumowaniem ostatniego briefingu: nagłówek, oceny **Stabilność** i **Dane** oraz liczba spostrzeżeń. Dotknij jej, żeby otworzyć cały briefing, albo zamknij ją przyciskiem **×**. Nowa karta pojawi się z następnym briefingiem.

## Jak czytać widżet parametru

Widżet **zmierzonego parametru** ma zawsze te same trzy elementy w tych samych miejscach. Kafelki urządzeń i sterowania (gniazdo, pompa dozująca, pompa) pokazują za to swój stan, bo nie stoi za nimi jeden odczyt.

**Wartość** to sam odczyt, duży i na środku.

**Wiek** jest pod nią albo obok: `teraz`, `1g`, `2d`. Mówi, jak dawno zrobiono odczyt, a nie kiedy odświeżył się ekran. Wartość, która nie zmieniła się od dwóch dni, pokazuje `2d`. To też jest informacja.

**Znaczek źródła** to mały symbol obok wieku. Pokazuje, skąd pochodzi liczba: z sondy, kontrolera, wyniku laboratoryjnego albo z Twojego testu kropelkowego. Dotknij widżetu, a zobaczysz pełną nazwę źródła i niedawną historię.

:::note Dlaczego wiek jest tak ważny
Idealny odczyt alkaliczności sprzed czterech dni nie jest bieżącym odczytem alkaliczności. Wiek jest przy każdej wartości, żeby różnicę było widać od razu.
:::

## Kolory

Cora używa kolorów oszczędnie i zawsze w tym samym znaczeniu:

| Kolor | Znaczenie |
|---|---|
| Zielony | Wartość jest spokojnie w zakresie |
| Bursztynowy | Blisko granicy. **Zwykle nadal w zakresie**, ale w jego ostatniej dziesiątej części |
| Czerwony | Poza granicą. Warto zareagować |
| Szary | Brak oceny: nie ma świeżego odczytu albo zakresu, do którego można porównać |

:::note Bursztynowy zwykle znaczy „jeszcze dobrze, ale coś się zmienia”
Bursztynowy oznacza *margines*, a nie przekroczenie. Odczyt w zakresie, ale w jego ostatnich 10%, dostaje bursztynowy kolor. Dzięki temu dryf widać, zanim stanie się problemem, gdy jest jeszcze czas na reakcję.

Są dwa doprecyzowania.

**Zakres ustawiony przez Ciebie to granica.** Po jej przekroczeniu widżet od razu robi się czerwony, bez bursztynowego marginesu, bo tę granicę wyznaczasz świadomie. Zakres **podany przez Corę** jest łagodniejszym punktem odniesienia. Przez pierwsze 10% poza granicą widżet jest bursztynowy, a dalej czerwony.

**Limit jednostronny** (górna granica dla zanieczyszczenia albo dolna dla składnika odżywczego) jest oceniany tylko przy górnej krawędzi. Dlatego miedź na zerze jest zielona i nie dostaje bursztynowego koloru za to, że leży przy dole skali.
:::

Widżet z bursztynową albo czerwoną ramką wymaga uwagi. Ramka obejmuje cały widżet, nie samą liczbę, więc widać ją podczas przewijania.

## Pod widżetami

![Dół pulpitu](img/mobile-dashboard-foot.webp "Edytuj panel, Zapisz parametry i skróty do czterech rodzajów zapisów.")

Na dole pulpitu są:

- **Edytuj panel** otwiera [edytor pulpitu](/help/mobile-dashboard-editing).
- **Zapisz parametry** służy do ręcznego wpisania wyników testów kropelkowych.
- **Dziennik · Alerty · Konserwacja · Obsada** to skróty do tych miejsc dla tego akwarium.

Linijka nad nimi pokazuje, kiedy pulpit się ostatnio zaktualizował i z jakich źródeł korzystał.

## Szczegóły widżetu

Dotknij widżetu, żeby otworzyć szczegóły: pełną historię na wykresie, wszystkie źródła, które podawały ten parametr, i obecne progi. Stamtąd wpiszesz nowy odczyt ręcznie, zmienisz zakres albo cofniesz się dalej w historii.

## Gdy widżet nie ma wartości

Widżet pokazuje wartość, gdy ją dostanie. Jeśli jest pusty, zwykle chodzi o jedno z tych:

- Urządzenie jest offline. Sprawdź zakładkę **Urządzenia**.
- Parametr nie ma jeszcze źródła. Wpisz go ręcznie albo podłącz sprzęt, który go mierzy.
- Parametr nigdy nie został zgłoszony ani wpisany, więc nie ma jeszcze żadnego zapisu.

Stary odczyt nie znika dlatego, że okno wykresu jest krótsze niż jego wiek. Zostaje na widżecie razem z wiekiem, więc od razu widać, że jest stary, a nie że go brakuje.

W innych sprawach zajrzyj do **[Rozwiązywania problemów](/help/troubleshooting)**.

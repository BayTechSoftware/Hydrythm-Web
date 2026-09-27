---
title: Scenki na Cora Max
description: Budowanie, uruchamianie i edytowanie scenek prosto na ekranie Cora Max.
section: Cora Max
reviewed: 2026-09-27
order: 15
group: Automation
---

**Scenka** to zapisany zestaw akcji na sprzęcie, który działa razem, albo na ustalony czas, albo aż to zatrzymasz. Scenki działają tak samo, niezależnie od tego, czy budujesz je na telefonie, czy na Cora Max; ta strona opisuje robienie tego przy ścianie.

## Gdzie znaleźć scenki

**Ustawienia → Automatyzacje** wypisuje każdą scenkę na każdym Twoim akwarium, z plakietką filtra dla każdego akwarium, gdy masz więcej niż jedno. Otwiera tę samą listę, niezależnie od tego, czy scenka została zbudowana na telefonie, czy na Cora Max.

Dotknij scenki, aby ją edytować, albo dotknij **+**, aby zbudować nową. Jeśli masz więcej niż jedno akwarium i żaden filtr nie jest wybrany, Cora Max pyta, do którego akwarium nowa scenka należy.

## Budowanie scenki

1. Nadaj scence **nazwę**.
2. Dodaj **kroki**. Z Cora Max krok może przełączyć gniazdo Apex (**On**, **Wyłączone** albo **Auto**) albo wtyczkę Zigbee (**on**, **wyłączona** albo **toggle**). Kroki dodane na telefonie dla innych rodzajów sprzętu wciąż tutaj się pokazują i wciąż mogą być przestawiane albo usuwane, mimo że ten ekran nie może dodać kolejnego takiego kroku.
3. Wybierz, jak długo działa: ustaloną liczbę minut albo **permanent** (działa, aż to zatrzymasz).
4. Wybierz, czy uruchomienie scenki wymaga kroku **confirmation**. Zostaw to włączone, o ile nie jesteś pewien, że scenka nigdy nie dotyka niczego, co byłoby niebezpieczne zmienić bez drugiego spojrzenia.
5. Zapisz.

:::note Głowice dozujące DŌS nigdy nie są krokiem scenki
Scenka, zbudowana na Cora Max albo na telefonie, nigdy nie może włączyć głowicy dozującej. To jest zamierzone: dawka nie jest rodzajem akcji, którą scenka powinna móc wywołać przez przypadek.
:::

## Uruchamianie scenki

Scenki pojawiają się jako kafelki na pulpicie. Dotknij **Uruchom**, aby jedną uruchomić.

Jeśli scenka wymaga potwierdzenia, Cora Max wypisuje dokładnie, co zamierza zrobić, jedna linia na krok, przed tym, jak coś się stanie. Przeczytaj to, a potem wybierz uruchomienie albo anulowanie.

Podczas działania scenki na czas jej kafelek pokazuje odliczanie do zakończenia i przycisk **Zatrzymaj**, aby zakończyć wcześniej. Kafelek scenki permanentnej zostaje w stanie działania, aż go zatrzymasz.

Uruchamianie albo zatrzymywanie scenki zawsze przechodzi przez Cora Cloud, tak jak każde inne polecenie; zobacz [Co zostało zmienione i przez co](/help/max-activity) po to, gdzie zapisywany jest wynik.

**Jeśli to nie działa:** jeśli scenka nie chce się uruchomić albo nie chce się zatrzymać, zobacz [Rozwiązywanie problemów](/help/troubleshooting).

:::note Blokada rodzicielska obejmuje też scenki
Jeśli [blokada rodzicielska](/help/max-voice) jest włączona, uruchamianie albo zatrzymywanie scenki z tego ekranu jest blokowane razem z każdą inną kontrolką. Pytania o scenkę wciąż działają głosem; uruchomienie albo zatrzymanie jej nie.
:::

## Edytowanie albo usuwanie scenki

Otwórz scenkę z **Ustawienia → Automatyzacje** albo przytrzymaj jej kafelek na pulpicie, aby zmienić jej nazwę, kroki, czas trwania albo ustawienie potwierdzenia, albo aby ją usunąć.

:::note Starsze ekrany Cora Max mogą uruchomić scenkę, ale nie edytować jej
Budowanie i edytowanie scenek przy ścianie jest nowszą możliwością Cora Max. Starsze Cora Max na tym samym koncie wciąż może pokazać i uruchomić scenkę utworzoną na telefonie albo na nowszym Cora Max; po prostu nie może jej zmienić. Zaktualizuj Cora Max albo edytuj scenkę z telefonu albo z nowszego ekranu, jeśli to się zdarzy.
:::

Zobacz [Scenki i automatyzacje](/help/mobile-automation) po to, co scenka może robić w większych szczegółach, i jak są budowane na telefonie.

---
title: Sceny na Cora Max
description: Jak tworzyć, uruchamiać i edytować sceny bezpośrednio na ekranie Cora Max.
section: Cora Max
reviewed: 2026-09-27
order: 15
group: Automation
---

**Scena** to zapisany zestaw akcji na sprzęcie, które działają razem przez ustalony czas albo do chwili, gdy je zatrzymasz. Sceny działają tak samo, bez względu na to, czy tworzysz je na telefonie, czy na Cora Max. Ta strona opisuje pracę ze scenami na Cora Max.

## Gdzie są sceny

W **Ustawienia → Automatyzacje** zobaczysz wszystkie sceny ze wszystkich akwariów. Jeśli masz więcej niż jedno akwarium, nad listą są plakietki filtrów, po jednej na akwarium. Lista jest ta sama, bez względu na to, gdzie scenę utworzono.

Dotknij sceny, żeby ją edytować, albo dotknij **+**, żeby utworzyć nową. Jeśli masz kilka akwariów i nie wybierzesz filtra, Cora Max zapyta, do którego akwarium ma należeć nowa scena.

## Tworzenie sceny

1. Wpisz **Nazwa sceny**.
2. Dodaj **Kroki**. Na Cora Max krok może przełączyć gniazdo Apex (**WŁ.**, **WYŁ.** albo **AUTO**) albo wtyczkę Zigbee (**Włącz**, **Wyłącz** albo **Przełącz**). Kroki dodane na telefonie dla innego sprzętu też tu widać. Możesz zmienić ich kolejność albo je usunąć, ale nie dodasz tu nowego kroku tego rodzaju.
3. Wybierz czas działania: określoną liczbę minut albo **Stałe** (scena działa, dopóki jej nie zatrzymasz).
4. Zdecyduj, czy scena ma prosić o potwierdzenie przed uruchomieniem (**Pytaj przed uruchomieniem**). Zostaw to włączone, chyba że masz pewność, że scena nie zmienia niczego, co wymaga drugiego spojrzenia.
5. Zapisz.

:::note Głowice dozujące DŌS nie mogą być krokiem sceny
Żadna scena, utworzona na Cora Max czy na telefonie, nie włączy głowicy dozującej. Dawki nie da się w ten sposób podać przez przypadek.
:::

## Uruchamianie sceny

Sceny widać na pulpicie jako kafelki. Dotknij **Uruchom**, żeby uruchomić scenę.

Jeśli scena wymaga potwierdzenia, Cora Max najpierw pokaże dokładnie, co zrobi, po jednej linii na krok. Przeczytaj listę, a potem uruchom scenę albo anuluj.

Gdy działa scena z ustalonym czasem, jej kafelek odlicza czas do końca. Ma też przycisk **Zatrzymaj**, jeśli chcesz ją zakończyć wcześniej. Kafelek stałej sceny pokazuje, że działa, dopóki jej nie zatrzymasz.

Uruchomienie i zatrzymanie sceny zawsze przechodzi przez Cora Cloud, tak jak każde inne polecenie. Wynik znajdziesz w [Co zostało zmienione i przez co](/help/max-activity).

Jeśli scena nie chce się uruchomić albo zatrzymać, zajrzyj do [Rozwiązywanie problemów](/help/troubleshooting).

:::note Blokada rodzicielska dotyczy też scen
Gdy włączona jest [Blokada rodzicielska](/help/max-voice), z tego ekranu nie uruchomisz ani nie zatrzymasz sceny, tak jak nie użyjesz innych przycisków sterowania. Głosem możesz dalej pytać o scenę, ale nie uruchomisz jej ani nie zatrzymasz.
:::

## Edytowanie i usuwanie sceny

Otwórz scenę w **Ustawienia → Automatyzacje** albo przytrzymaj jej kafelek na pulpicie. Możesz wtedy zmienić nazwę, kroki, czas działania i potwierdzenie albo usunąć scenę.

:::note Starszy Cora Max uruchomi scenę, ale jej nie zmieni
Tworzenie i edytowanie scen na ekranie to nowsza funkcja Cora Max. Starszy Cora Max na tym samym koncie pokaże i uruchomi scenę utworzoną na telefonie albo na nowszym Cora Max, ale nie może jej zmienić. W takiej sytuacji zaktualizuj Cora Max albo edytuj scenę na telefonie lub nowszym ekranie.
:::

Więcej o tym, co potrafi scena i jak tworzy się ją na telefonie, przeczytasz w [Sceny i automatyzacje](/help/mobile-automation).

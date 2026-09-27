---
title: Sondy
description: Zmapuj sondy swojego kontrolera na parametry Cory i zapisuj kalibrację i czyszczenie.
section: Cora Mobile
reviewed: 2026-09-09
order: 13
group: Equipment
---

Kontroler zgłasza sondy pod własnymi nazwami. Mapowanie sond mówi Corze, która z nich jest Twoją sondą pH, która temperaturą, i tak dalej.

## Mapowanie sond

Otwórz swój **profil akwarium** (ołówek na górze pulpitu), rozwiń sekcję swojego kontrolera i wybierz **Mapowanie sond**.

![Mapowanie sond](img/mobile-probes.webp "Każda sonda zgłaszana przez Twój kontroler, jej odczyt na żywo i to, co Cora z nią robi.")

Każda sonda zgłaszana przez Twój kontroler jest wypisana wraz z jej aktualnym odczytem. Cora automatycznie wykrywa standardowe nazwy, a wiersz pokazuje, którą dopasowała, więc zadaniem tutaj jest zwykle poprawienie tych, których nie mogła umieścić, a nie mapowanie wszystkich ręcznie.

Każdy wiersz oferuje trzy możliwości:

- **A Cora parameter**: metryka, którą ta sonda mierzy.
- **Własna**: dla sondy, dla której Cora nie ma standardowego parametru. Podajesz krótki token wielkimi literami, i sonda jest śledzona pod tą nazwą.
- **Ignoruj**: dla sond, których wcale nie chcesz zapisywać.

Zignorowana lub niezmapowana sonda nie pojawi się na pulpicie i nie zasili alertów.

Mapowania zaczynają działać od następnego zapisanego odczytu, więc poprawka tutaj nie zmienia historii; zmienia to, co jest zapisywane od tej pory. Naciśnij **Zapisz**, aby je zastosować.

:::warning Niezmapowana sonda jest niewidoczna dla Cory
Jeśli parametr nie pokazuje żadnych odczytów, mimo że sonda działa, sprawdź najpierw mapowanie.
:::

## Wiele sond dla jednego parametru

System z dwiema sondami temperatury może zmapować obie. Cora zachowuje je jako odrębne źródła; ustawienie źródła w widżecie decyduje, którą z nich śledzi kafelek, a [widok parametru](/help/mobile-metric-detail) pozwala je porównać.

## Zapisywanie opieki nad sondami

Sondy dryfują. Cora może śledzić, kiedy każda z nich była ostatnio kalibrowana lub czyszczona, dzięki czemu możesz odróżnić rzeczywistą zmianę od sondy, która wymaga uwagi.

Zapisz kalibrację lub czyszczenie z wpisu sondy. Świetnie sprawdza się też jako powtarzające się [zadanie konserwacji](/help/mobile-maintenance).

:::note Historia kalibracji wyjaśnia niezgodności
Gdy sonda i test kroplowy się nie zgadzają, data ostatniej kalibracji sondy jest zwykle pierwszą rzeczą, którą warto sprawdzić.
:::

---
title: Sondy
description: Przypisz sondy kontrolera do parametrów Cory i zapisuj kalibrację oraz czyszczenie.
section: Cora Mobile
reviewed: 2026-09-09
order: 13
group: Equipment
---

Kontroler nazywa sondy po swojemu. W mapowaniu sond wskazujesz Corze, która z nich mierzy pH, która temperaturę i tak dalej.

## Mapowanie sond

Otwórz **profil akwarium** (ołówek na górze pulpitu), rozwiń sekcję swojego kontrolera i wybierz **Mapowanie sond**.

![Mapowanie sond](img/mobile-probes.webp "Każda sonda zgłaszana przez kontroler, jej odczyt na żywo i to, co robi z nią Cora.")

Na liście jest każda sonda, którą zgłasza kontroler, razem z bieżącym odczytem. Cora sama rozpoznaje standardowe nazwy, a w wierszu widać, co dopasowała. Zwykle wystarczy więc poprawić te sondy, których Cora nie umiała przypisać. Nie trzeba mapować wszystkich ręcznie.

W każdym wierszu są trzy możliwości:

- **Parametr Cory**, czyli to, co mierzy ta sonda.
- **Własny…** dla sondy, dla której Cora nie ma standardowego parametru. Podajesz krótki identyfikator wielkimi literami i sonda jest śledzona pod tą nazwą.
- **Ignoruj** dla sond, których w ogóle nie chcesz zapisywać.

Zignorowana albo nieprzypisana sonda nie pojawi się na pulpicie i nie wywoła alertów.

Mapowanie działa od następnego zapisanego odczytu. Poprawka nie zmienia więc historii, tylko to, co będzie zapisywane od teraz. Dotknij **Zapisz**, żeby zastosować zmiany.

:::warning Cora nie widzi nieprzypisanej sondy
Jeśli parametr nie ma żadnych odczytów, choć sonda działa, najpierw sprawdź mapowanie.
:::

## Kilka sond dla jednego parametru

W systemie z dwiema sondami temperatury możesz przypisać obie. Cora traktuje je jako osobne źródła. Ustawienie źródła w widżecie decyduje, którą z nich pokazuje kafelek, a w [szczegółach parametru](/help/mobile-metric-detail) porównasz obie.

## Zapisywanie konserwacji sond

Sondy z czasem dryfują. Cora może śledzić, kiedy każdą z nich ostatnio kalibrowano albo czyszczono. Dzięki temu odróżnisz prawdziwą zmianę od sondy, która wymaga uwagi.

Kalibrację albo czyszczenie zapiszesz we wpisie sondy. To dobry kandydat na powtarzalne [zadanie konserwacyjne](/help/mobile-maintenance).

:::note Historia kalibracji wyjaśnia rozbieżności
Gdy sonda i test kropelkowy podają różne wartości, najpierw sprawdź, kiedy sonda była ostatnio kalibrowana.
:::

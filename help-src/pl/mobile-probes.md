---
title: Sondy
description: Sprawdź, która sonda zasila każdy odczyt na wszystkich kontrolerach, i zapisuj kalibrację oraz czyszczenie.
section: Cora Mobile
reviewed: 2026-09-30
order: 13
group: Equipment
---

Jeśli masz więcej niż jeden kontroler, albo dwie sondy mierzące to samo, Cora musi wiedzieć, któremu odczytowi ufać. Mapowanie sond to miejsce, w którym to ustalasz, i w którym najpierw mówisz Corze, czym jest każda sonda.

Otwórz **profil akwarium** (ołówek na górze pulpitu) i wybierz **Mapowanie sond**.

## Skąd pochodzi każdy odczyt

![Skąd pochodzi każdy odczyt](img/mobile-probes.webp "Każdy parametr, sonda, która go zasila, i przycisk wyboru, żeby to zmienić.")

Ta sekcja wymienia każdy parametr, który Cora śledzi dla tego akwarium, na przykład pH albo temperaturę, i pokazuje, która sonda go teraz zasila.

Dotknij odczytu, żeby zobaczyć każdą sondę, która go zgłasza, na wszystkich podłączonych kontrolerach. Każda pozycja pokazuje markę, własną nazwę sondy nadaną przez kontroler i jej wartość na żywo. Wybierz jedną, żeby ją przypiąć, albo wybierz **Automatycznie**, żeby Cora korzystała z tej, która akurat raportuje.

Znacznik przy każdym odczycie pokazuje, co obowiązuje: **Automatycznie** albo **Wybrane przez Ciebie**, gdy przypniesz sondę.

Jeśli przypięta sonda przestanie raportować, Cora pokaże, kiedy ostatnio się odezwała, i zaproponuje **Powrót do Automatycznego**, żeby martwa sonda nie zablokowała odczytu.

Dotknij **Zmień nazwę**, żeby nadać odczytowi własną nazwę wyświetlaną. To coś innego niż nazwa, którą nadajesz samej sondzie. To właśnie ta nazwa pojawia się na pulpicie, w alertach i w Reef Buddy.

:::note Czujnika wycieku nie można tu przypisać ponownie
Alarm czujnika wycieku zależy od jego własnej nazwy, więc jest wykluczony z tego wyboru. Działa tak samo jak dotychczas.
:::

## Sondy: określ, czym jest każda z nich

Niżej zobaczysz każdą sondę znaną Corze, pogrupowaną według urządzenia, które ją zgłasza, razem z bieżącym odczytem. Cora sama rozpoznaje standardowe nazwy sond, a w wierszu widać, co dopasowała. Zwykle wystarczy poprawić tylko te kilka, których nie umiała przypisać.

Każdy wiersz daje trzy możliwości.

- **Parametr Cory**, czyli to, co mierzy ta sonda.
- **Własny…** dla sondy, dla której Cora nie ma standardowego parametru. Podajesz krótki identyfikator wielkimi literami i sonda jest śledzona pod tą nazwą.
- **Ignoruj** dla sond, których w ogóle nie chcesz zapisywać.

Zignorowana albo nieprzypisana sonda nie pojawi się na pulpicie i nie wywoła alertów.

Mapowanie działa od następnego zapisanego odczytu. Poprawka nie zmienia więc historii, tylko to, co będzie zapisywane od teraz. Dotknij **Zapisz**, żeby zastosować zmiany.

:::warning Cora nie widzi nieprzypisanej sondy
Jeśli parametr nie ma żadnych odczytów, choć sonda działa, najpierw sprawdź jej mapowanie.
:::

## Kilka sond dla jednego parametru

Jeśli masz dwie sondy temperatury, czy to na tym samym kontrolerze, czy na dwóch różnych, zmapuj obie. Cora traktuje je jako osobne źródła, a sekcja **Skąd pochodzi każdy odczyt** powyżej to miejsce, w którym wybierzesz, która z nich napędza odczyt, albo zostawisz ustawienie Automatycznie. Porównasz je w [szczegółach parametru](/help/mobile-metric-detail).

## Zapisywanie konserwacji sond

Sondy z czasem dryfują. Cora może śledzić, kiedy każdą z nich ostatnio kalibrowano albo czyszczono. Dzięki temu odróżnisz prawdziwą zmianę od sondy, która wymaga uwagi.

Kalibrację albo czyszczenie zapiszesz we wpisie sondy. To dobry kandydat na powtarzalne [zadanie konserwacyjne](/help/mobile-maintenance).

:::note Historia kalibracji wyjaśnia rozbieżności
Gdy sonda i test kropelkowy podają różne wartości, najpierw sprawdź, kiedy sonda była ostatnio kalibrowana.
:::

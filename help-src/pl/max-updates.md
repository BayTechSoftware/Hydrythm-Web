---
title: Aktualizacje i odzyskiwanie
description: Jak Cora Max sam się aktualizuje, okno instalacji i kanał aktualizacji, sprawdzanie wersji, PIN odzyskiwania i co zrobić, gdy Cora Max się nie uruchamia.
section: Cora Max
reviewed: 2026-10-17
order: 15
group: Settings and account
---

Cora Max sam dba o aktualne oprogramowanie. Ta strona wyjaśnia, kiedy instalują się aktualizacje, jak sprawdzić wersję i jak przywrócić Cora Max do działania, gdy nie chce się normalnie uruchomić.

## Automatyczne aktualizacje

Nowe wersje pobierają się w tle, gdy tylko się pojawią. Instalują się w **Oknie instalacji**, od 3 do 5 rano, chyba że to zmienisz, więc ekran nie uruchomi się ponownie, gdy na niego patrzysz. Gdy wersja ma informacje o zmianach, Cora Max je pokazuje.

Nie musisz nic robić, żeby mieć aktualną wersję.

## Sprawdzanie wersji i ustawień aktualizacji {#checking-the-version-and-update-settings}

![Sieć i aktualizacje na Cora Max](img/max-updates.webp "Aktualizacja oprogramowania w sekcji SIEĆ I AKTUALIZACJE w Ustawieniach Cora Max.")

Twoja wersja jest na karcie na górze **Ustawienia → Ustawienia Cora Max** (*Cora Max · oprogramowanie 0.28.170*) oraz w **POMOC I O APLIKACJI → O aplikacji**.

**Ustawienia → Ustawienia Cora Max → Aktualizacja oprogramowania** (w **SIEĆ I AKTUALIZACJE**) pokazuje Twoją wersję i to, czy czeka aktualizacja. Dotknij **Sprawdź aktualizacje**, żeby sprawdzić teraz, albo **Pobierz i zainstaluj**, gdy jakaś jest.

W **Ustawieniach aktualizacji** na tym samym ekranie:

- **Okno instalacji** ustawia godziny, w których mogą instalować się aktualizacje, z godziną **Początek** i **Koniec**, w czasie lokalnym tego ekranu. Strefę czasową ustawiasz w Cora Mobile, w **Urządzenia →** Twój Cora Max **→ Strefa czasowa**.

Żeby sprawdzić, czy ten ekran odczytuje Twoje urządzenia i zapisuje do Cora Cloud, wróć do **Ustawienia Cora Max** i przewiń do **STAN**. Pokazuje dla każdego akwarium **Stan odpytywania**, **Ostatnie odpytanie**, **Ostatni zapis do chmury** i **Zapis w chmurze**.

Jeśli aktualizacja pobiera się wolno, sprawdź połączenie za pomocą **Testu prędkości sieci** na tym samym ekranie. **Uruchom test** pobiera do 16 MB pliku aktualizacji z Cora Cloud, przez najwyżej 20 sekund, i pokazuje prędkość w MB/s.

## Gdy jest dostępna aktualizacja

Pojawi się okno z opisem nowości i dwoma możliwościami.

- **Zaktualizuj teraz** instaluje od razu i uruchamia ponownie. Trwa to około minuty. Nie odłączaj zasilania Cora Max.
- **Odłóż na 24 godziny** ukrywa okno i zapyta ponownie za dobę.

Gdy aktualizacja czeka, mała kropka pojawia się na ikonie **Ustawienia** na górnym pasku i w wierszu **Aktualizacja oprogramowania**. Kropka zostaje po odłożeniu, więc nadal widać, że aktualizacja czeka. Znika na czas instalacji.

Jeśli nic nie zrobisz, aktualizacja zainstaluje się sama w **Oknie instalacji**.

Możesz też uruchomić ją z telefonu: w Cora Mobile otwórz **Urządzenia →** Twój Cora Max i dotknij **Zaktualizuj do v…**.

:::note Aktualizacja nie usuwa odczytów
Twoje dane są na Twoim koncie. Po ponownym uruchomieniu Cora Max ma te same akwaria, panele i historię.
:::

## Odzyskiwanie {#recovery}

Odzyskiwanie to tryb serwisowy na wypadek, gdy Cora Max nie chce się normalnie uruchomić albo gdy trzeba naprawić jego konfigurację bez laptopa.

1. Przytrzymaj **pięć palców** w prawym górnym rogu ekranu przez **dziesięć sekund**.
2. Otworzy się okno **PIN odzyskiwania**. Wpisz sześciocyfrowy PIN i dotknij **Potwierdź**.

PIN pojawił się przy parowaniu Cora Max. Znajdziesz go też w Cora Mobile w **Urządzenia →** Twój Cora Max **→ PIN odzyskiwania**. Sam Cora Max nigdy go nie pokazuje, więc gość ani dziecko opierające się o ekran nie wejdą w odzyskiwanie.

Jeśli trzy razy wpiszesz zły PIN, odzyskiwanie zablokuje się na 30 sekund, a po każdej kolejnej złej próbie na dłużej. **Za dużo prób** mówi, ile trzeba czekać. Jeśli Cora Max od parowania ani razu nie był online, nie ma jeszcze PIN-u i pokazuje **Odzyskiwanie jest niedostępne**. Najpierw połącz go z Wi-Fi.

W **Odzyskiwaniu** możesz:

- **Skonfiguruj Wi-Fi ponownie**: wybierz nową sieć Wi-Fi i hasło
- **Sparuj urządzenie ponownie**: usuń parowanie i skonfiguruj urządzenie od nowa z Cora Mobile
- **Sprawdź aktualizacje teraz**: sprawdź aktualizacje od razu
- **Ustawienia fabryczne**: usuń parowanie i wszystkie ustawienia z ekranu

Dane akwarium zapisane już w Cora Cloud zostają w każdym przypadku.

Jeśli Cora Max kilka razy z rzędu nie uruchomi się poprawnie, może też sam wrócić do poprzedniej wersji.

:::note Ten sam gest odblokowuje blokadę rodzicielską
Jeśli włączona jest [Blokada rodzicielska](/help/max-settings#child-lock), przytrzymanie pięciu palców w rogu odblokowuje też ekran. Dotknij **Anuluj** w oknie **PIN odzyskiwania**, jeśli chcesz tylko odblokować ekran.
:::

:::warning Ekran w trybie odzyskiwania niczym nie steruje
Kontroler dalej działa według własnego programu. Ale krok [automatyzacji](/help/mobile-automation), który musi wykonać **ten Cora Max**, nie zadziała, gdy jest on w trybie odzyskiwania. Reguła się uruchomi, ale krok nigdy nie dotrze do sprzętu.
:::

## Gdy Cora Max pokazuje „Cora Max napotkał problem”

Ten ekran oznacza, że coś poszło nie tak podczas uruchamiania albo działania Cora Max. Pokazuje **Kod pomocy** (zaczyna się od *CXB-*).

1. Zapisz kod pomocy.
2. Poczekaj. Cora Max sam uruchomi się ponownie po około 10 minutach. Żeby uruchomić go ponownie od razu, przytrzymaj pięć palców w prawym górnym rogu przez 10 sekund.
3. Jeśli to się powtarza, napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** i podaj kod pomocy.

## Gdy urządzenie nie uruchamia się ponownie

Napisz na **[cora@coraiq.tech](mailto:cora@coraiq.tech)** i podaj wersję widoczną na ekranie oraz wyświetlany komunikat. Nie paruj go wcześniej ponownie. Stan parowania często pomaga ustalić, co się stało.

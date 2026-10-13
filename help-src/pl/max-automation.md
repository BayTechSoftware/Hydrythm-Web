---
title: Sceny na Cora Max
description: Twórz, uruchamiaj, edytuj i usuwaj sceny na Cora Max, z Ustawienia → Automatyzacje albo z kafelka sceny na pulpicie.
section: Cora Max
reviewed: 2026-10-13
order: 9
group: Alerts and automation
twin: mobile-automation
---

**Scena** to zapisany zestaw akcji na sprzęcie, które działają razem, przez ustalony czas albo dopóki ich nie zatrzymasz. Na Cora Max możesz tworzyć, uruchamiać i edytować sceny. Sceny utworzone na telefonie i na Cora Max to te same sceny. Reguły automatyzacji (w rodzaju „gdy stanie się to, zrób tamto”) ustawiasz na telefonie. Więcej w [Scenach i automatyzacjach](/help/mobile-automation).

![Lista Sceny na Cora Max, z chipem filtra dla każdego akwarium i przyciskiem Nowa scena](img/max-automation.webp "Lista Sceny filtrowana według akwarium. Gdy nie ma jeszcze scen, lista o tym mówi i proponuje Nowa scena.")

## Gdzie są sceny

**Ustawienia → Automatyzacje** otwiera **Sceny**, listę wszystkich scen ze wszystkich akwariów. Jeśli masz więcej niż jedno akwarium, jest chip filtra dla każdego z nich, a także **Wszystkie akwaria**.

Dotknij sceny, żeby ją edytować, albo dotknij **Nowa scena**, żeby utworzyć nową. Jeśli masz więcej niż jedno akwarium i nie wybrano filtra, Cora Max zapyta **Dla którego akwarium jest ta scena?**

## Tworzenie sceny

![Pusty formularz Nowa scena na Cora Max](img/max-scene-builder.webp "Nowa scena: nazwa, Stałe albo Czasowe, Pytaj przed uruchomieniem, a potem Dodaj krok.")

1. Wpisz **Nazwę sceny**.
2. Dotknij **Dodaj krok** i wybierz, co robi ten krok. Widzisz tylko rodzaje sprzętu, które ma to akwarium:
   - **Gniazdo Apex**: przełącz gniazdo Neptune Apex na **WŁ.**, **WYŁ.** albo **AUTO**.
   - **Steruj sprzętem Red Sea**: na przykład **ReefDose: dawkuj teraz**, **ReefDose: ustaw dawkę dzienną**, **ReefRun: ustaw prędkość pompy**, **ATO: zacznij ręczne napełnianie** albo **ReefMat: przesuń rolkę**.
   - **Steruj pompą cyrkulacyjną**: ustaw przepływ albo tryb fali pompy Jecod, włącz ją lub wyłącz albo **Wstrzymaj na czas karmienia**.
   - **Uruchom karmienie na Gyre**: wstrzymaj Maxspect Gyre na czas karmienia. Sam ruszy ponownie.
   - **GHL**: przerwa na karmienie, konserwacja, podmiana wody, scena oświetlenia i inne polecenia kontrolera.
   - **HYDROS**: tryb, poziom wyjścia, dawka albo **HYDROS: powrót do harmonogramu**.
3. W ten sam sposób dodaj kolejne kroki. Możesz zmieniać ich kolejność albo je usuwać. Krok, którego ten ekran nie potrafi edytować, ma oznaczenie **Nieedytowalne tutaj**. Edytuj go na telefonie.
4. Wybierz, jak długo scena działa. **Czasowe** działa przez liczbę minut ustawioną w **Czas trwania (minuty)**. **Stałe** działa, dopóki jej nie zatrzymasz.
5. Zostaw **Pytaj przed uruchomieniem** włączone, chyba że masz pewność, że scena nigdy nie dotyka niczego, co wymaga drugiego spojrzenia.
6. Dotknij **Zapisz**.

:::note Dawki w scenie
Głowica Neptune DŌS nigdy nie może być krokiem sceny. Krok **ReefDose: dawkuj teraz** może i ma własne pole **Maks. na dawkę (ml)**. Zostaw je puste, a limit wyniesie 10 mL. Dawka powyżej tego limitu jest odrzucana, nigdy zmniejszana. W każdej scenie, która dozuje, zostaw **Pytaj przed uruchomieniem** włączone.
:::

:::note Beta
**Beta.** Maxspect, GHL i HYDROS są w wersji Beta i są dostępne tylko dla użytkowników Beta. Jeśli nie jesteś użytkownikiem Beta, nie zobaczysz ich w **Dodaj urządzenie**. Aby poprosić o dostęp do Beta, skontaktuj się z [pomocą techniczną](/support.html).
:::

## Uruchamianie sceny

Sceny widać na pulpicie jako kafelki. Dotknij **Uruchom**, żeby uruchomić scenę.

Jeśli scena pyta przed uruchomieniem, Cora Max najpierw wymienia, co zamierza zrobić, po jednej linijce na krok. Przeczytaj to, a potem uruchom scenę albo anuluj.

Gdy działa scena czasowa, jej kafelek odlicza czas do końca i pokazuje **Zatrzymaj**, jeśli chcesz ją zakończyć wcześniej. Kafelek sceny stałej pokazuje, że działa, dopóki nie dotkniesz **Zatrzymaj**. Gdy scena się kończy albo ją zatrzymasz, kafelek pokazuje **Przywracanie…**, a Cora w tym czasie przywraca sprzęt.

Uruchomienie i zatrzymanie sceny idzie przez Cora Cloud, jak każde inne polecenie. Wynik znajdziesz w [Aktywności](/help/max-activity).

Na Cora Max nie da się uruchamiać scen głosem. Użyj kafelka, **Ustawienia → Automatyzacje** albo telefonu.

Jeśli scena nie chce się uruchomić albo zatrzymać, zajrzyj do [Rozwiązywania problemów](/help/troubleshooting).

:::note Blokada rodzicielska obejmuje też sceny
Gdy [Blokada rodzicielska](/help/max-settings#child-lock) zablokowała ekran, nie uruchomisz z niego, nie zatrzymasz ani nie edytujesz sceny, tak jak każdego innego elementu sterowania.
:::

## Edytowanie i usuwanie sceny

Żeby zmienić scenę, otwórz ją z **Ustawienia → Automatyzacje** albo przytrzymaj jej kafelek na pulpicie. Zmień, co trzeba, i dotknij **Zapisz**. Żeby ją usunąć, dotknij **Usuń scenę**. Nie da się tego cofnąć.

:::note Starszy Cora Max uruchomi scenę, ale jej nie zmieni
Starsze wersje Cora Max nadal pokazują i uruchamiają każdą scenę, ale nie mogą jej zmienić. Zaktualizuj Cora Max ([Aktualizacje i odzyskiwanie](/help/max-updates)) albo edytuj scenę na telefonie.
:::

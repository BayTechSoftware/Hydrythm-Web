---
title: Mapowanie parametrów i sondy
description: Zobacz odczyty każdego urządzenia na jednej liście, wybierz parametr, jako który się pokazują, i urządzenie, które je zasila, oraz zapisuj kalibrację i czyszczenie sond.
section: Cora Mobile
reviewed: 2026-11-03
order: 15
group: Equipment
---

W **Mapowaniu parametrów** mówisz Corze, jako jaki parametr ma się pokazywać każdy odczyt, a gdy dwa urządzenia zgłaszają to samo, któremu ufać. Przejdź do **Ustawień**, otwórz akwarium i dotknij **Mapowanie parametrów**.

Jest ono między **Edytuj akwarium** a **Progi alertów**. Ołówek na górze panelu otwiera **Edytuj akwarium**, gdzie go nie ma. Trafisz tu też ze stron urządzeń Neptune Apex.

Ekran to jedna lista urządzeń z polem wyszukiwania (**Szukaj parametrów**) nad nią. Wyszukiwanie obejmuje nazwy parametrów, nazwy odczytów, urządzenia i marki. To samo pole wyszukiwania jest w każdym wyborze parametru.

## Jedna lista urządzeń {#mapping}

Pod polem wyszukiwania Cora opisuje ekran jednym zdaniem: odczyty każdego urządzenia i parametr akwarium, jako który są pokazywane. Dotknij odczytu, aby go zmienić.

- **Każde urządzenie jest pod nazwą, którą mu nadano.** Urządzenie bez nazwy jest pod swoją marką, a dwa nienazwane urządzenia tej samej marki są numerowane („AquaWiz 1”, „AquaWiz 2”). Numery seryjne i identyfikatory urządzeń nigdy nie służą za nazwy; są za przyciskiem **Pokaż szczegóły** na stronie urządzenia. Zobacz [Strona urządzenia](/help/mobile-devices#a-devices-page).
- **Każdy odczyt jest pod urządzeniem, które naprawdę go zgłasza.** Każdy wiersz pokazuje nazwę odczytu u urządzenia, jego ostatnią wartość i **Pokazywany jako**, czyli parametr akwarium, który zasila. Ukryty przez Ciebie odczyt ma napis **Niepokazywany**.
- **Akwarium ma jeden Neptune Apex**, choćby czytało go wiele urządzeń Cora. Jego sondy tworzą jedną listę w jednej sekcji **Apex** (albo pod nazwą, którą mu nadano). Moduł rozszerzeń Apex, taki jak DŌS albo Trident, jest wymieniony pod własną nazwą. Jego odczytów nie da się przekierować; dotknięcie jednego pozwala zamiast tego zmienić nazwę parametru.
- **Urządzenie współdzielone z innymi akwariami jest na liście każdego akwarium, z którym jest połączone.** Jego sekcja mówi *Także w akwariach:* i podaje nazwy pozostałych akwariów, a dalej *Zmiany tutaj dotyczą tylko tego akwarium.*
- **Urządzenie z dwoma odczytami lub mniej jest od razu otwarte**; dłuższe zaczyna zamknięte i pokazuje liczbę odczytów, chyba że któryś z jego odczytów dzieli parametr z innym urządzeniem. Dotknij nazwy urządzenia, aby je otworzyć lub zamknąć. Podczas wyszukiwania wszystkie trafienia są otwarte.

Cora sama rozpoznaje standardowe nazwy odczytów, więc większość wierszy pokazuje już właściwy parametr. Popraw tylko te kilka, których nie umiała przypisać.

Zmiana jest zapisywana w chwili wyboru i nie ma przycisku zapisu. Zaczyna działać przy następnych odczytach. Poprawka tutaj nie zmienia historii: wcześniejsze odczyty zostają tam, gdzie są, a zmienia się tylko to, co będzie zapisywane od tej chwili. Mapowania ustawione przed tym układem zostają bez zmian.

:::warning Cora nie widzi ukrytego odczytu
Jeśli parametr nie ma odczytów, choć urządzenie działa, sprawdź, czy jego odczyt nie ma napisu **Niepokazywany**.
:::

:::note Czujnika wycieku nie przypiszesz tu ponownie
Alarm czujnika wycieku zależy od jego własnej nazwy, więc jego wiersz mówi *Alarm wycieku zależy od tej nazwy, więc nie można jej tu zmienić.* Działa tak samo jak zawsze.
:::

:::note Urządzenia, które wciąż czekają na aktualizację
Urządzenie czekające na aktualizację oprogramowania mówi *Zmiany tutaj zaczną działać po aktualizacji oprogramowania tego urządzenia.* Twój wybór jest zapisany i zadziała po zainstalowaniu aktualizacji.
:::

## Wybór, jako co pokazuje się odczyt {#shows-as}

Dotknij odczytu, aby otworzyć **Pokazuj ten odczyt jako**. Na górze jest sam odczyt: urządzenie, nazwa odczytu i jego wartość. Pod nim:

- **Twoje parametry** wymieniają każdy parametr tego akwarium. Każda opcja mówi, skąd pochodzą jej odczyty, więc nigdy nie musisz zgadywać między dwiema podobnymi nazwami:
  - *Pochodzi z* i nazwa urządzenia, które go zasila, albo *Pochodzi też z* i nazwa innego urządzenia, gdy ten odczyt już pokazuje się jako ten parametr.
  - *Żadne urządzenie nie dostarcza teraz jego odczytów. Ostatnia wartość …* z informacją, jak dawno, dla parametru, którego urządzenie zamilkło.
  - *Z twoich wyników testów* albo *Z wyników ICP*, z ostatnią wartością, dla parametru, który ma tylko twoje własne wyniki.

  Ołówek (**Zmień nazwę**) obok parametru nadaje mu własną nazwę. To ona pojawia się na panelu, w alertach i w Reef Buddy. Zostaw nazwę pustą, aby ją zresetować.
- **Więcej parametrów** jest zwinięte. Zawiera standardowe parametry, których to akwarium jeszcze nie ma.
- **Nowy parametr…** tworzy osobny parametr, oddzielnie od innych parametrów. Zobacz niżej.
- **Nie pokazuj tego odczytu** (*Cora go pomija*) sprawia, że odczyt nie jest zapisywany jako żaden parametr. Ukryty odczyt nie pojawia się na żadnym panelu i nie wywołuje alertów.

Arkusz kończy się napisem *Zapisywane od razu po wyborze. Wcześniejsze odczyty zostają tam, gdzie są.*

### Nowy parametr {#new-parameter}

Użyj **Nowy parametr…**, gdy odczyt nie powinien się mieszać z innym o tej samej nazwie, na przykład druga sonda pH w sumpie. Cora otwiera **Nowy parametr** i wyjaśnia, że odczyt z tego urządzenia będzie pokazywany jako osobny parametr, a jego jednostka pochodzi z urządzenia.

1. Wpisz **Nazwę**. Dowolna nazwa, na przykład *pH sump* lub *pH 2*, do 32 znaków.
2. Dotknij **Utwórz**. **Utwórz** pozostaje szare, dopóki nazwa jest pusta. **Anuluj** zamyka okno i niczego nie zmienia.

Odczyt zasila teraz nowy parametr. Nazwa zachowuje wpisaną pisownię. Jeśli wpiszesz nazwę parametru, który już masz, odczyt do niego dołączy, a jego nazwa się nie zmieni. Żaden zakres alertów nie jest kopiowany z innego parametru.

## Testy i wyniki laboratoryjne {#tests-and-lab-results}

Twoje własne wyniki testów i wyniki ICP są na samym dole, w **Testy i wyniki laboratoryjne**. Sekcja zaczyna zwinięta, bo sam raport ICP ma dziesiątki pierwiastków. Dotknij jej, aby ją otworzyć. Wyniki są pogrupowane pod **Wyniki ICP** i **Twoje wyniki testów**.

Każdy wynik mapuje się na parametr tak samo jak odczyt urządzenia. Dotknij jednego, aby otworzyć **Pokazuj ten odczyt jako** i wybrać parametr, pod którym się wyświetla, na przykład żeby pH z testu kropelkowego było osobno od pH z sondy. Cora mówi o tym w sekcji: nowe wyniki trafiają pod wybrany parametr, wcześniejsze zostają tam, gdzie są. Wynik testu lub ICP nigdy nie jest odrzucany, więc **Nie pokazuj tego odczytu** nie jest dla niego dostępne.

Parametry, których nie zasila żaden odczyt powyżej i które nie są testami, są pod **Inne parametry**. Dotknij jednego, aby zmienić jego nazwę.

## Kilka sond dla jednego parametru {#multiple-probes}

Jeśli dwa odczyty pokazują się jako ten sam parametr, czy to z dwóch sond jednego urządzenia, czy z dwóch różnych urządzeń, na górze listy pojawia się baner. Mówi na przykład *pH dostaje odczyty z 2 urządzeń* (albo *2 sond*), a dalej, co robi Cora: *Pokazywany jest najnowszy.* albo *Używane:* wybrane urządzenie. Dotknij go albo **Wybierz jeden**, aby otworzyć arkusz.

- **Najnowszy odczyt** (*Urządzenie, które zgłosiło się ostatnie*) pozwala Corze używać urządzenia, które zgłosiło się ostatnio. Pozostałe zostają w historii.
- Wybierz urządzenie lub sondę, aby śledzić tylko ją. Każda pokazuje swoją wartość i ile minut temu się zgłosiła. Twój wybór dotyczy tego parametru w całym akwarium: jego kafelka, wykresu i alertów, a nie jednego widżetu.
- **Pokaż jeden z nich osobno** (*Na przykład druga sonda w sumpie*) pyta **Który pokazać osobno?**, a potem otwiera **Pokazuj ten odczyt jako** dla wybranego.

Jeśli wybrane urządzenie przestanie raportować, baner mówi *Nie raportuje od* i podaje czas oraz proponuje **Użyj najnowszego**, żeby martwa sonda nie zablokowała odczytu.

Źródła porównasz w [widoku parametru](/help/mobile-metric-detail).

Gdy dwa źródła zgłaszają ten sam parametr, wygrywa najnowszy pomiar. Wartość na ekranie zastępuje tylko odczyt z późniejszym czasem pomiaru, z jakiegokolwiek urządzenia. Starszy odczyt, albo urządzenie, które wysyła ponownie stary odczyt, trafia do historii i nie nadpisuje bieżącej wartości. Jeśli wybrano urządzenie, Cora trzyma się tego urządzenia.

Profil akwarium ma też sekcję **Źródła parametrów** (ukrytą podczas tworzenia nowego akwarium). Ustawia to samo w krótszej formie. Używaj Mapowania parametrów, gdy chcesz mieć w jednym miejscu każde urządzenie i każdy odczyt.

## Zapisywanie konserwacji sond {#recording-probe-care}

Sondy dryfują. Gdy kalibrujesz, czyścisz albo wymieniasz sondę, powiedz o tym Corze, żeby nie wzięła skoku odczytu za prawdziwą zmianę w akwarium.

1. Dotknij widżetu parametru na panelu, na przykład pH, temperatury, zasolenia albo ORP.
2. Dotknij **Zapisz konserwację sondy** (ikona czujnika) na górnym pasku.
3. Wybierz, co zrobiono: **Skalibrowano**, **Wyczyszczono**, **Wymieniono**, **Zmieniono położenie** albo **Porównano z referencją**. Możesz dodać **Odczyt referencyjny** i notatkę.
4. Dotknij **Zapisz konserwację sondy**.

Widok parametru pokazuje wtedy, ile czasu minęło od kalibracji tej sondy. Konserwacja sond dobrze sprawdza się też jako powtarzalne [zadanie konserwacyjne](/help/mobile-maintenance).

:::note Daty kalibracji wyjaśniają rozbieżności
Gdy sonda i test kropelkowy podają różne wartości, sprawdź, kiedy ostatnio kalibrowano sondę. Zwykle to jest odpowiedź.
:::

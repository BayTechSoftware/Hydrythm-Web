---
title: Mapowanie parametrów i sondy
description: Wybierz, która sonda dostarcza każdy odczyt, powiedz Corze, co mierzy każda sonda, i zapisuj kalibrację oraz czyszczenie sond.
section: Cora Mobile
reviewed: 2026-10-13
order: 15
group: Equipment
---

W **Mapowaniu parametrów** mówisz Corze, co mierzy każda sonda, a gdy dwie sondy zgłaszają to samo, której z nich ufać. Przejdź do **Ustawień**, otwórz akwarium i dotknij **Mapowanie parametrów**.

Jest ono między **Edytuj akwarium** a **Progi alertów**. Ołówek na górze pulpitu otwiera **Edytuj akwarium**, gdzie go nie ma. Trafisz tu też ze stron urządzeń Neptune Apex i GHL (Beta). GHL jest dostępny tylko dla użytkowników Beta. Zobacz [Funkcje Beta](/help/mobile-beta).

Ekran ma pole wyszukiwania (**Szukaj parametrów**) i dwie zakładki, **Mapowanie** i **Źródła**. Wyszukiwanie obejmuje nazwy parametrów, nazwy sond, urządzenia i marki. To samo pole wyszukiwania jest w każdym wyborze parametru.

## Sondy: powiedz Corze, czym jest każda z nich {#mapping}

![Zakładka Mapowanie](img/mobile-probe-mapping.webp "Każda sonda, pogrupowana według urządzenia, które ją zgłasza, z parametrem, do którego jest przypisana.")

Zakładka **Mapowanie** otwiera się pierwsza. Wymienia każdą sondę znaną Corze, pogrupowaną według urządzenia, które ją zgłasza, z jej bieżącym odczytem. Cora sama rozpoznaje standardowe nazwy sond, a każdy wiersz pokazuje, co dopasowała. Zwykle wystarczy poprawić tylko tych kilka, których nie umiała przypisać.

Każdy wiersz daje trzy możliwości.

- **Parametr Cory** to wartość, którą mierzy ta sonda.
- **Własny…** jest dla sondy, dla której Cora nie ma standardowego parametru. Wpisz krótką nazwę wielkimi literami w **Własny parametr (token WIELKIMI LITERAMI)**, a Cora będzie ją śledzić pod tą nazwą.
- **Ignoruj** jest dla sond, których w ogóle nie chcesz zapisywać.

Zignorowana albo nieprzypisana sonda nie pojawi się na pulpicie i nie wywoła alertów.

Mapowanie zaczyna działać przy następnych odczytach. Poprawka tutaj nie zmienia historii. Zmienia tylko to, co będzie zapisywane od tej chwili. Dotknij **Zapisz**, żeby zastosować zmiany.

:::warning Cora nie widzi nieprzypisanej sondy
Jeśli parametr nie ma odczytów, choć sonda działa, najpierw sprawdź jej mapowanie.
:::

## Skąd pochodzi każdy odczyt {#sources}

![Zakładka Źródła](img/mobile-probes.webp "Każdy odczyt, sonda, która go dostarcza, i czy jest Automatycznie, czy Wybrane przez Ciebie.")

Zakładka **Źródła** wymienia każdą wartość, którą Cora śledzi dla tego akwarium, na przykład pH albo temperaturę, i pokazuje, która sonda ją teraz dostarcza.

Dotknij odczytu, żeby zobaczyć każdą sondę, która go zgłasza, na wszystkich podłączonych kontrolerach. Przy każdej widać markę, własną nazwę sondy i jej wartość na żywo. Wybierz jedną, żeby ją przypiąć, albo wybierz **Automatycznie (wygrywa najnowszy odczyt)**, żeby Cora używała tej sondy, która zgłosiła się ostatnio. Pozostałe zostają w historii.

Znacznik przy każdym odczycie pokazuje, co obowiązuje: **Automatycznie** albo **Wybrane przez Ciebie**, gdy przypniesz sondę. Twój wybór dotyczy tego odczytu w całym akwarium, a nie jednego widżetu.

Jeśli przypięta sonda przestanie raportować, Cora pokaże, kiedy ostatnio się odezwała, i zaproponuje **Powrót do Automatycznego**, żeby martwa sonda nie zablokowała odczytu.

Dotknij **Zmień nazwę**, żeby nadać odczytowi własną nazwę wyświetlaną. Jest ona niezależna od nazwy, którą nadajesz samej sondzie. To ona pojawia się na pulpicie, w alertach i w Reef Buddy.

Profil akwarium ma też sekcję **Źródła parametrów** (ukrytą podczas tworzenia nowego akwarium). Ustawia to samo w krótszej formie. Używaj Mapowania parametrów, gdy chcesz mieć w jednym miejscu każdą sondę z każdego kontrolera.

:::note Czujnika wycieku nie przypiszesz tu ponownie
Alarm czujnika wycieku zależy od jego własnej nazwy, więc jest wykluczony z tego wyboru. Działa tak samo jak zawsze.
:::

## Kilka sond dla jednego parametru {#multiple-probes}

Jeśli masz dwie sondy temperatury, na tym samym kontrolerze albo na dwóch różnych, zmapuj obie. Cora traktuje je jako osobne źródła, a w zakładce **Źródła** wybierasz, która z nich dostarcza odczyt, albo zostawiasz Automatycznie. Porównasz je w [widoku parametru](/help/mobile-metric-detail).

Gdy dwa źródła zgłaszają ten sam parametr, wygrywa najnowszy pomiar. Wartość na ekranie zastępuje tylko odczyt z późniejszym czasem pomiaru, z jakiegokolwiek urządzenia. Starszy odczyt, albo urządzenie, które wysyła ponownie stary odczyt, trafia do historii i nie nadpisuje bieżącej wartości. Jeśli przypięto źródło w zakładce **Źródła**, Cora trzyma się tego źródła.

## Zapisywanie konserwacji sond {#recording-probe-care}

Sondy dryfują. Gdy kalibrujesz, czyścisz albo wymieniasz sondę, powiedz o tym Corze, żeby nie wzięła skoku odczytu za prawdziwą zmianę w akwarium.

1. Dotknij widżetu parametru na pulpicie, na przykład pH, temperatury, zasolenia albo ORP.
2. Dotknij **Zapisz konserwację sondy** (ikona czujnika) na górnym pasku.
3. Wybierz, co zrobiono: **Skalibrowano**, **Wyczyszczono**, **Wymieniono**, **Zmieniono położenie** albo **Porównano z referencją**. Możesz dodać **Odczyt referencyjny** i notatkę.
4. Dotknij **Zapisz konserwację sondy**.

Widok parametru pokazuje wtedy, ile czasu minęło od kalibracji tej sondy. Konserwacja sond dobrze sprawdza się też jako powtarzalne [zadanie konserwacyjne](/help/mobile-maintenance).

:::note Daty kalibracji wyjaśniają rozbieżności
Gdy sonda i test kropelkowy podają różne wartości, sprawdź, kiedy ostatnio kalibrowano sondę. Zwykle to jest odpowiedź.
:::

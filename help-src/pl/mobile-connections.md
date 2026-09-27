---
title: Podłączanie sprzętu
description: Jak podłączyć do Cory sprzęt Neptune Apex, Red Sea ReefBeat, Jecod i AquaWiz.
section: Cora Mobile
reviewed: 2026-09-17
order: 10
group: Equipment
---

Cora współpracuje ze sprzętem, który już posiadasz. Ta strona opisuje, co jest wspierane i czego wymaga każde połączenie.

Każda marka łączy się w sposób, który jej najbardziej odpowiada, więc zacznij od punktu wejścia dla Twojego sprzętu:

| Marka | Zacznij od |
|---|---|
| Neptune Apex | Akwarium; jego profil zawiera połączenie z Apex |
| Red Sea ReefBeat | Akwarium |
| Jecod / Jebao | **Urządzenia → Znajdź pompę w Twojej sieci** albo Bluetooth |
| AquaWiz | **Urządzenia → Dodaj AquaWiz** |
| Maxspect *(beta)* | **Urządzenia → Znajdź pompę w Twojej sieci** |
| Cora Max | **Urządzenia → Dodaj urządzenie** |

## Neptune Apex

Cora odczytuje Twój Apex przez Twoją lokalną sieć: sondy, gniazda i wszystkie zamontowane moduły rozszerzeń.

**Będziesz potrzebować:** adresu Twojego Apex w sieci i jego logowania.

**Co otrzymujesz:** każda sonda, którą zgłasza Twój Apex, staje się źródłem, które możesz umieścić na pulpicie. Gniazda pojawiają się jako kontrolki. Zamontowane moduły rozszerzeń otrzymują własne kafelki urządzeń.

:::note Twój Apex zachowuje własne programowanie
Cora odczytuje Twój Apex, pokazuje go razem z resztą i może przełączać gniazda, gdy o to poprosisz. Twoje własne programowanie działa dalej dokładnie tak, jak je skonfigurowałeś.
:::

## Red Sea ReefBeat

Cora rozmawia z urządzeniami ReefBeat w Twojej lokalnej sieci. Wspierane jednostki to **ReefDose**, **ReefATO+**, **ReefMat** i **ReefRun**.

**Będziesz potrzebować:** sprzętu już skonfigurowanego w ReefBeat i w tej samej sieci co Twój telefon w momencie dodawania.

**Co otrzymujesz:** stronę urządzenia dla każdej jednostki, plus odczyty każdej jednostki jako źródła. ReefDose zgłasza swoje głowice i pojemniki; ReefATO+ zgłasza swój zbiornik i dolewki; ReefMat zgłasza pozostałe dni; ReefRun zgłasza stan pompy.

## Jecod / Jebao

Cora łączy się z pompami Jecod i może je odczytywać oraz kontrolować. Jednostki Jecod łączą się z Corą w jeden z dwóch sposobów, i to, którego używa Twoja, decyduje o tym, co jest możliwe.

![Znajdowanie pompy](img/mobile-connections.webp "Skan wyjaśnia, czego potrzebuje i dlaczego pompa może nie pojawić się przy pierwszym przeszukaniu.")

**Przez Twoją sieć.** Użyj **Znajdź pompę w Twojej sieci**; znajduje jednostki, które się ogłaszają, więc nie trzeba wpisywać żadnego adresu. Pompę sieciową można odczytywać i sterować nią, gdy jest zasilana **i dostępna**: albo Twój telefon jest w tej samej sieci, albo Cora Max w tej sieci przekazuje połączenie za Ciebie. Poza domem, bez Cora Max na miejscu, pompa dostępna tylko przez sieć jest widoczna, ale nie można nią sterować.

:::note Pompa często nie odpowiada na pierwsze przeszukanie
Pompy odpowiadają na jeden skan i pomijają następny. Jeśli Twojej nie ma na liście, przeskanuj ponownie, zamiast zakładać, że jest nieosiągalna.
:::

Jeśli wyszukiwanie nic nie znajdzie, wynik pokazuje adresy, które zostały sprawdzone przez Wi-Fi. Jeśli Twoja pompa ma inny adres w aplikacji Jebao, Twój telefon jest w innej sieci. Sieć gościnna albo IoT, albo pasmo tylko 5 GHz, nie zobaczy tych pomp. Na iPhone Cora potrzebuje też dostępu do sieci lokalnej, aby zobaczyć pompy w Twoim Wi-Fi. Jeśli jest wyłączony, lista zostaje pusta i nie pojawia się żaden błąd, więc wynik to wyjaśnia i proponuje **Otwórz Ustawienia**, aby go z powrotem włączyć. **Ustawienia → Dostęp do urządzeń** otwiera to samo miejsce w każdej chwili; zobacz [Ustawienia](/help/mobile-settings).

**Przez Bluetooth.** Niektóre pompy są dostępne tylko z telefonu znajdującego się blisko nich. Strona pompy mówi o tym wprost i pokazuje ostatnie ustawienia, które udało się odczytać, wraz z ich wiekiem.

Cora potrzebuje do tego uprawnienia Bluetooth. Udziel go przed dodaniem pompy Bluetooth: bez uprawnienia pompa nie może zostać wykryta w ogóle, a nie tylko dłużej się pojawia.

**Co otrzymujesz:** aktualny stan, tryb i intensywność, wstrzymanie na czas karmienia oraz program dnia. Zobacz [Planowanie pracy sprzętu](/help/mobile-schedules).

:::warning Pompa Bluetooth jest dostępna tylko, gdy jesteś blisko niej
Jej strona pokazuje ostatnie ustawienia odczytane przez Corę i jak dawno temu. Zmiana czegokolwiek, w tym uruchomienie wstrzymania na czas karmienia, wymaga, aby pompa była w zasięgu. Stań blisko niej i otwórz stronę ponownie.
:::

## Kontroler AquaWiz KH

Cora odczytuje alkaliczność z kontrolera AquaWiz KH przez Twoje konto AquaWiz.

**Będziesz potrzebować:** nazwy użytkownika i hasła AquaWiz. Cora loguje się w Twoim imieniu i zachowuje to logowanie, aby móc dalej odczytywać dane.

**Co otrzymujesz:** alkaliczność jako źródło, aktualizowaną tak często, jak Twój kontroler wykonuje miareczkowanie. pH jest dostępne jako opcja, jeśli Twoja jednostka je zgłasza.

:::warning Jedno logowanie, wspólne
AquaWiz wydaje jedno logowanie na konto, więc to, które przechowuje Cora, jest tym samym, którego używa ich własna aplikacja. Zmiana hasła AquaWiz odłączy Corę; połącz ją ponownie z wiersza urządzenia. Aby całkowicie odebrać Corze dostęp, usuń urządzenie w Corze i zmień swoje hasło AquaWiz.
:::

## Maxspect

:::note Wsparcie dla Maxspect jest w wersji beta
Wsparcie dla gyre Maxspect jest wciąż testowane i rozwijane, więc niektóre kontrolki mogą być ograniczone, a to, co widzisz tutaj, może się zmienić między aktualizacjami. Jeśli coś nie działa tak, jak opisano, powiedz nam o tym w [Pomoc](/help/mobile-support).
:::

Cora łączy się z pompami Maxspect Gyre i może je odczytywać oraz sterować nimi.

**Będziesz potrzebować:** w momencie dodawania, gyre i Twój telefon w tej samej sieci. Użyj **Urządzenia → Znajdź pompę w Twojej sieci**.

**Co otrzymujesz:** wzór fali i prędkość dla **Gyre A** i **Gyre B**, harmonogram gyre do podglądu (ustawiany w aplikacji Maxspect), **Stan pompy** oraz to, czy pompa działa, wraz z czasem ostatniego odczytu. Zobacz [Kontrola sprzętu](/help/mobile-device-control).

:::note Jak Cora Mobile dociera do gyre
Gdy akwarium obsługuje Cora Max, Cora Mobile działa przez ten Cora Max, także wtedy, gdy jesteś poza domem, a **Zmień ustawienia** wychodzi od ostatniego odczytu tego Cora Max. W innym przypadku Twój telefon rozmawia z gyre bezpośrednio i musi być w sieci gyre. Otwarcie strony gyre wtedy je odczytuje; jeśli strona pokazuje starszy zapisany odczyt, **Zmień ustawienia** zostaje ukryte, aż dotkniesz odświeżenia.
:::

## Zapisywanie ręczne

Niektóre parametry pochodzą z testu kroplowego, a nie ze sprzętu. Aby wpisać wynik, przewiń do dołu pulpitu i dotknij **Zapisz parametry**.

Odczyty zapisane ręcznie są pełnoprawne: pojawiają się na widżetach, mają własne źródło i wiek, zasilają Reef Buddy i to z nimi Cora porównuje Twoje sondy, gdy informuje, że dwa źródła się nie zgadzają.

## Jeśli połączenie przestaje działać

Wiersz urządzenia mówi, z jakim rodzajem problemu masz do czynienia. Zobacz tabelę w **[Dodawanie, edytowanie i usuwanie urządzeń](/help/mobile-devices)** oraz **[Rozwiązywanie problemów](/help/troubleshooting)** w sprawach, których to nie obejmuje.

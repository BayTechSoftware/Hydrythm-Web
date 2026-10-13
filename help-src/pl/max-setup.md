---
title: Konfiguracja Cora Max
description: Sparuj nowy Cora Max z Cora Mobile przez Bluetooth, połącz go z Wi-Fi, wybierz jego akwaria, a później przenieś go do innego akwarium.
section: Cora Max
reviewed: 2026-10-13
order: 1
group: Getting started
twin: mobile-setup
---

Ta strona prowadzi od nowego Cora Max do działającego ekranu na ścianie. Parujesz go z telefonu przez Bluetooth i nie wpisujesz niczego na samym ekranie.

:::tip Najpierw skonfiguruj akwaria w telefonie
Cora Max pokazuje akwaria i urządzenia z Twojego konta i sam nie może utworzyć akwarium. Najpierw [skonfiguruj je w Cora Mobile](/help/mobile-setup). Cora Max pobierze je, gdy tylko go sparujesz.
:::

## Czego potrzebujesz {#what-you-need}

- Cora Max podłączonego do zasilania i włączonego. Ma być stale podłączony.
- Cora Mobile w telefonie, zalogowanej, z utworzonym już **co najmniej jednym akwarium**.
- Włączonego Bluetooth w telefonie i telefonu blisko Cora Max.
- Nazwy i hasła Twojej sieci Wi-Fi.

Ustaw Cora Max tam, gdzie zobaczysz go z drugiego końca pokoju i możesz do niego mówić, z dala od chlapania i osadów soli.

## Co najpierw pokazuje ekran {#what-the-screen-shows-first}

Włącz Cora Max. Pokaże ekran parowania z napisem **Otwórz aplikację Cora na telefonie**, potem **Dotknij Dodaj urządzenie.** i **Wybierz to Cora Max z listy urządzeń.** Pod spodem pokazuje **Widoczne jako** i swoją nazwę, zakończoną krótkim kodem. Jeśli parujesz więcej niż jeden, po tym kodzie odróżnisz je w telefonie.

![Ekran parowania Cora Max, czekający na telefon](img/max-pairing-screen.webp "Czeka na telefon. Dolna linijka pokazuje nazwę, którą wyświetli telefon.")

Na tym samym ekranie jest krótka informacja o integracjach ze sprzętem innych producentów. Warunki zaakceptowane w Cora Mobile obejmują też Cora Max.

## Parowanie z telefonu {#pairing}

Wszystko inne dzieje się w Cora Mobile. Arkusz prowadzi Cię przez pięć kroków widocznych u jego góry: **Połącz · Wi-Fi · Logowanie · Akwaria · Gotowe**.

1. **Znajdź go.** Otwórz zakładkę **Urządzenia**, dotknij **Dodaj urządzenie**, a potem **Cora**. Ekran **Dodaj swoje Cora** wymienia urządzenia Cora w Twojej sieci i pobliskie urządzenia konfiguracyjne znalezione przez Bluetooth. Dotknij **Skanuj**, jeśli Twojego jeszcze nie ma, a potem dotknij swojego Cora Max.

   ![Ekran Dodaj swoje Cora w Cora Mobile, szukający urządzeń](img/mobile-add-device.webp "Dodaj urządzenie, potem Cora. Cora Mobile szuka w Twojej sieci Wi-Fi i przez Bluetooth, a niżej jest ręczne wpisanie adresu IP.")

2. **Połącz.** Telefon łączy się z Cora Max przez Bluetooth i pokazuje jego adres MAC, oprogramowanie, wariant i wersję sprzętu. Sprawdź, czy to właściwe urządzenie, a potem dotknij **Dalej**.

3. **Wi-Fi.** Wybierz sieć z listy albo dotknij **Skanuj ponownie** i wpisz hasło w telefonie. Od tej chwili telefon rozmawia z Cora Max przez Wi-Fi, więc trzymaj telefon w tej samej sieci.

4. **Logowanie.** Telefon łączy Cora Max z Twoim kontem. Dzieje się to samo, a Cora Max pokazuje własny postęp, na przykład **Weryfikowanie konta…** i **Konfigurowanie akwarium…**.

   ![Ekran parowania Cora Max z napisem Weryfikowanie konta](img/max-pairing-verifying.webp "Cora Max pokazuje każdy krok, gdy telefon łączy go z Twoim kontem.")

5. **Akwaria.** W **Przypisz akwaria** wybierz akwaria, którymi będzie zarządzał ten Cora Max, **najwyżej cztery**.

6. **Gotowe.** Telefon mówi, że Cora Max jest skonfigurowany, i pokazuje **PIN odzyskiwania**. Dotknij przycisku, który otwiera pulpit akwarium, albo **Przejdź do Urządzeń**. Cora Max pokaże **Sparowano**, a potem **Otwieranie panelu…**.

:::warning Zapisz PIN odzyskiwania
**PIN odzyskiwania** ma sześć cyfr i to jedyny sposób na wejście w odzyskiwanie na tym Cora Max. Żeby go użyć, przytrzymaj pięć palców w prawym górnym rogu ekranu przez dziesięć sekund, a potem wpisz PIN. Odzyskiwanie pozwala ponownie skonfigurować Wi-Fi, sparować urządzenie od nowa, sprawdzić aktualizację albo przywrócić ustawienia fabryczne. PIN znajdziesz ponownie w telefonie w **Urządzenia → Twój Cora Max → PIN odzyskiwania**, ale nigdy na samym Cora Max.
:::

### Gdy parowanie utknie {#if-pairing-gets-stuck}

- **Bluetooth jest wyłączony. Włącz go, a potem dotknij Skanuj ponownie.** Włącz Bluetooth i skanuj ponownie.
- **Uprawnienie do Bluetooth jest wyłączone dla Cora.** Zezwól na Bluetooth dla Cora w ustawieniach telefonu, a potem dotknij **Skanuj**. iPhone może też poprosić o dostęp do sieci lokalnej. Na to też zezwól.
- **Nie znaleziono pobliskich urządzeń konfiguracyjnych Cora przez Bluetooth.** Stań obok Cora Max, sprawdź, czy nadal pokazuje ekran parowania, i skanuj ponownie.
- **Nie znaleziono akwariów** w kroku Akwaria. Twoje konto nie ma jeszcze akwarium. Utwórz je w Cora Mobile, a potem powtórz ten krok.
- **Jeszcze niepołączone z Twoim akwarium** na końcu. Cora Max jest sparowany, ale połączenie z akwarium się nie zakończyło. Dotknij **Spróbuj teraz**. Dopóki się nie zakończy, alerty dla tego ekranu używają domyślnych zakresów.

Więcej rozwiązań w [Rozwiązywaniu problemów](/help/troubleshooting#pairing-a-cora-max-fails).

## Po sparowaniu {#after-pairing}

Cora Max widzi teraz te same akwaria, urządzenia, odczyty i zapiski co telefon.

- Jeśli któreś z Twoich akwariów miało wcześniej Cora Max, Cora Max zapyta **Przywrócić poprzedni układ dla tego akwarium?** **Przywróć** przywraca ustawienia ekranu, dźwięku i alertów zapisane przez poprzedni. **Zacznij od nowa** je pomija.
- Akwarium bez odczytów pokazuje **Jeszcze brak odczytów** i przycisk **Zapisz swój pierwszy test**.
- Cora Max buduje początkowy pulpit na podstawie profilu akwarium. Nie kopiuje pulpitu z telefonu.

Do jednego konta możesz sparować więcej niż jeden Cora Max, na przykład jeden w pokoju z akwarium, a drugi w salonie. Każdy może pokazywać inne akwaria i ma własny układ. Jeśli dwa pokazują to samo akwarium, [Więcej niż jedno urządzenie Cora](/help/mobile-multi-device) wyjaśnia, który z nich odczytuje sprzęt.

## Budowanie pulpitu {#building-the-dashboard}

Pulpit na dużym ekranie to stała siatka i wszystko musi zmieścić się na jednym ekranie. Najszybciej ułożysz go z telefonu: otwórz zakładkę **Urządzenia**, dotknij swojego Cora Max, a potem **Układ panelu** na karcie akwarium. Możesz to też zrobić przy ścianie z menu akwarium.

Żeby użyć ponownie układu z innego Cora Max albo innego akwarium, wczytaj go z **Moje panele** w edytorze. Więcej w [Edytowaniu pulpitu Cora Max](/help/max-dashboard-editing).

## Przenoszenie Cora Max do innego akwarium {#changing-which-tanks-it-shows}

To, które akwaria pokazuje Cora Max, zmieniasz w telefonie. Własne ustawienia Cora Max tego nie potrafią.

1. W Cora Mobile otwórz zakładkę **Urządzenia** i dotknij swojego Cora Max.
2. W **Akwaria** dotknij **Dodaj akwarium** i wybierz akwarium. Cora Max mieści do czterech. Gdy ma już cztery, przycisku nie ma, więc najpierw usuń jedno.
3. Żeby zdjąć akwarium z tego ekranu, dotknij czerwonej ikony usuwania (**Usuń akwarium**) na karcie tego akwarium, a potem **Usuń**.

Żeby przenieść Cora Max z jednego akwarium do drugiego, dodaj nowe akwarium, a potem usuń stare. Nowe akwarium dostaje początkowy pulpit zbudowany z jego profilu. Ułóż go w **Układ panelu**.

Jeśli ten Cora Max był przypiętym Głównym Cora Max usuniętego akwarium, przypięcie zostaje usunięte, a akwarium wraca do **Każde aktywne (automatycznie)**. Więcej w [Urządzeniach i ich stanie](/help/max-devices).

## Aktualizacje {#updates}

Cora Max sam się aktualizuje. Nowa wersja pobiera się w tle i instaluje w nocy. Twoja wersja jest na górze **Ustawienia → Ustawienia Cora Max**. Więcej w [Aktualizacjach i odzyskiwaniu](/help/max-updates).

## Przenoszenie do innej sieci Wi-Fi {#moving-it-to-a-different-network}

Przejdź do **Ustawienia → Ustawienia Cora Max → Wi-Fi**, wybierz nową sieć i wpisz hasło. Cora Max pozostaje sparowany, więc nie musisz konfigurować go od nowa.

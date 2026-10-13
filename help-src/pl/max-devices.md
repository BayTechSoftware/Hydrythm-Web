---
title: Urządzenia i ich stan
description: Zobacz sprzęt, który odczytuje Cora Max, i zmień jego nazwę, wybierz, który Cora Max odczytuje każde akwarium, napraw akwarium, którego odczyty przestały napływać, i zarządzaj Cora Max z telefonu.
section: Cora Max
reviewed: 2026-10-13
order: 7
group: Equipment
twin: mobile-devices
---

**Ustawienia → Urządzenia** na Cora Max wymienia sprzęt, który widzi, i stan każdego urządzenia. Ikona urządzeń na górnym pasku otwiera tę samą listę, przefiltrowaną do akwarium widocznego na ekranie.

## Lista urządzeń {#the-device-list}

![Lista urządzeń na Cora Max, filtrowana według akwarium i pogrupowana według marki](img/max-devices.webp "Filtr akwarium, a pod nim każde urządzenie pogrupowane według marki, z jednolinijkowym podsumowaniem i akwarium.")

Cora Max widzi ten sam sprzęt co telefon, bo oba odczytują to samo konto.

Chipami filtra na górze pokażesz **Wszystkie akwaria** albo tylko jedno. Urządzenia są pogrupowane według marki. Każda pozycja ma kropkę stanu (szarą, gdy Cora jeszcze nie wie, zieloną, gdy działa, pomarańczową przy ostrzeżeniu albo usterce, czerwoną, gdy jest offline), jednolinijkowe podsumowanie tego, co urządzenie zawiera (*21 gniazd · 4 karmienia*, *zostało 19 testów*), akwarium, do którego należy, i czas **Ostatnio widziano**. Urządzenia Beta mają chip **Beta**.

Dotknij urządzenia, żeby otworzyć jego stronę. Każda strona urządzenia zaczyna się od sekcji **Stan**. Co potrafi każda strona, opisuje [Sterowanie sprzętem z Cora Max](/help/max-device-control).

Jeśli lista pokazuje **Wciąż wczytywanie części urządzeń: ta lista może być niekompletna.**, daj jej chwilę.

:::note Beta
**Beta.** Lampy, pompy i dozowniki EcoTech, monitory powietrza w pomieszczeniu Inkbird i kamery są w wersji Beta i są dostępne tylko dla użytkowników Beta. Jeśli nie jesteś użytkownikiem Beta, nie zobaczysz ich w **Dodaj urządzenie**. Aby poprosić o dostęp do Beta, skontaktuj się z [pomocą techniczną](/support.html). Więcej w [Funkcjach Beta](/help/mobile-beta).
:::

### Zmiana nazwy urządzenia {#renaming-a-device}

Dotknij ołówka w wierszu urządzenia albo na jego stronie i wpisz nową nazwę. Zostaw nazwę pustą, żeby wrócić do własnej nazwy urządzenia. Nazwa jest wspólna z telefonem, więc zmieni się też tam.

### Dodawanie i usuwanie urządzeń {#adding-and-removing-devices}

Urządzenia dodajesz, przypisujesz i usuwasz w telefonie. Cora Max je pokazuje i nimi steruje. Gdy nie ma jeszcze żadnych urządzeń, ten ekran pokazuje **Dodaj urządzenia w aplikacji Cora.** Więcej w [Dodawaniu, edytowaniu i usuwaniu urządzeń](/help/mobile-devices).

## Główne Cora Max: które urządzenie łączy się ze sprzętem {#primary-cora-max}

**Główne Cora Max** to Cora Max (albo inne urządzenie Cora), który odczytuje kontroler akwarium i pozostały sprzęt dla całego konta. Każde akwarium potrzebuje tylko jednego takiego urządzenia. Każdy inny ekran pokazuje to, co ono odczytuje.

Żeby to sprawdzić albo zmienić, otwórz **Ustawienia → [Twoje akwarium] → Główne Cora Max**. Masz dwie możliwości.

- **Każde aktywne (automatycznie)** oznacza, że pracą dzieli się każde urządzenie Cora online, które może połączyć się ze sprzętem tego akwarium, a wygrywa najnowszy zapis. Używaj tego, chyba że masz powód, żeby przypiąć jedno urządzenie.
- Przypnij jedno urządzenie, żeby tylko ono odczytywało sprzęt. Jeśli przejdzie w tryb offline, żaden inny Cora Max go nie zastąpi. Sprzęt odczytuje wtedy tylko Cora Mobile otwarta w tej samej sieci Wi-Fi, dopóki nie przypniesz innego urządzenia albo nie wrócisz do **Każde aktywne (automatycznie)**.

Ustawiasz to raz dla akwarium i działa na każdym ekranie Cora. Możesz to zmienić na każdym Cora Max, który pokazuje to akwarium, albo w Cora Mobile (**Ustaw jako główne Cora Max** na stronie Cora Max). Więcej w [Więcej niż jedno urządzenie Cora](/help/mobile-multi-device).

:::note Główne Cora Max i Urządzenie odpowiadające to dwa osobne ustawienia
Główne Cora Max decyduje, które urządzenie **odczytuje Twój sprzęt**. **Urządzenie odpowiadające** w Cora Mobile decyduje, które **odpowiada na „Hey Cora”**. Jeśli masz więcej niż jeden Cora Max, możesz ustawić je osobno. Więcej w [Rozmowie z Corą](/help/max-voice).
:::

## Gdy odczyty akwarium przestają napływać {#if-a-tanks-readings-stop}

Jeśli odczyty jednego akwarium przestały napływać, a inne akwarium na tym samym ekranie dalej się aktualizuje, zacznij tutaj.

1. Otwórz **Ustawienia → [to akwarium] → Główne Cora Max**. Sprawdź, czy przypisano urządzenie i czy jest online.
2. Jeśli inny Cora Max tego akwarium pokazuje na górnym pasku **Główne Cora offline**, główne urządzenie straciło połączenie. Co oznacza etykieta stanu, wyjaśnia [Ekran główny Cora Max](/help/max-tour#what-the-status-pill-means).
3. **Ustawienia → Ustawienia Cora Max → SIEĆ I AKTUALIZACJE → Odpytywanie urządzeń** pokazuje, jak często ten Cora Max odczytuje Twoje urządzenia. Tutaj możesz to tylko podejrzeć. Ustawia się to w Cora Mobile.
4. Sprawdź sekcję **Stan** w **Ustawienia → Ustawienia Cora Max**. Pokazuje dla każdego akwarium stan odpytywania, czas ostatniego odpytania i ostatni zapis do chmury, niczego nie zmieniając.

Jeśli to nie pomoże, zajrzyj do [Rozwiązywania problemów](/help/troubleshooting).

## Zarządzanie Cora Max z telefonu {#managing-a-cora-max-from-your-phone}

Otwórz zakładkę **Urządzenia** w telefonie i dotknij Cora Max. Górna karta pokazuje jego wariant, oprogramowanie i czas ostatniego widzenia. Stamtąd możesz zmienić jego nazwę, a gdy jest nowa wersja, dotknąć **Zaktualizuj do v…**, żeby zainstalować ją od razu. Tuż pod nią jest karta **PIN odzyskiwania**.

![Strona Cora Max w Cora Mobile z Blokadą rodzicielską, Odpytywaniem urządzenia, Strefą czasową i Przypisanymi akwariami](img/max-from-phone.webp "Własne ustawienia jednego Cora Max w telefonie: Blokada rodzicielska, Odpytywanie urządzenia i Strefa czasowa, a pod nimi jego akwaria.")

Te ustawienia dotyczą tylko **tego jednego ekranu**, tak jakby zmienić je przy ścianie:

| Sekcja | Ustawienia |
|---|---|
| **Ekran** | **Jasność**, **Przygaszaj po** |
| **Dźwięk i głos** | **Dźwięk alertu** włącza albo wyłącza dźwięk alertu na tym ekranie, a **Głośność alertów** ustawia jego głośność. Alerty nadal pokazują się na ekranie, a historia alertów i powiadomienia push się nie zmieniają |
| **Blokada rodzicielska** | **Blokada rodzicielska** blokuje ekran dotykowy tego ekranu i nie pozwala mu przełączać sprzętu głosem |
| **Sieć i aktualizacje** | **Odpytywanie urządzenia** (jak często odczytuje Twój sprzęt) i **Strefa czasowa** (używana do nocnego przygaszania i okna aktualizacji) |

W **Akwaria** każde akwarium, które pokazuje ten Cora Max, ma kartę z **Układ panelu**, **Edytuj akwarium** i urządzeniem odpytującym. **Dodaj akwarium** i ikona usuwania zmieniają, które akwaria pokazuje, a te zmiany dotyczą całego konta. Możesz je wprowadzić tylko w telefonie. Kroki opisuje [Konfiguracja Cora Max](/help/max-setup#changing-which-tanks-it-shows). To, które urządzenie jest Głównym Cora Max akwarium, możesz zmienić w telefonie albo na Cora Max.

W **Reset** przycisk **Zresetuj wyświetlacz** przywraca ekran do ekranu parowania. Zostaje on w Twojej sieci Wi-Fi, więc możesz sparować go ponownie przez Bluetooth, a dane akwarium zostają zachowane. **Usuń urządzenie** usuwa go z Twojego konta. Odczyty akwarium zostają zachowane, a później możesz go sparować ponownie.

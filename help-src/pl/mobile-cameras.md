---
title: Kamery i czuwanie skimmera
description: Dodaj do Cory kamerę Wyze, Tapo, Sonoff albo inną RTSP, oglądaj ją na kafelku lub na pełnym ekranie i pozwól czuwaniu skimmera ostrzec Cię, zanim kubek się przeleje.
section: Cora Mobile
reviewed: 2026-10-12
order: 35
group: Equipment
---

:::note Beta
**Beta.** Kamery są w wersji Beta i dostępne tylko dla użytkowników Beta. Jeśli nie jesteś użytkownikiem Beta, nie zobaczysz ich w **Dodaj urządzenie**. Aby poprosić o dostęp do Beta, skontaktuj się z [pomocą techniczną](/support.html).
:::

Dodaj kamerę, żeby widzieć akwarium w Corze, na telefonie i na Cora Max. Kamera wymaga Cora Max w akwarium, więc wiersz **Kamera** pokazuje **Wymaga Cora Max**, dopóki akwarium go nie ma.

## Dodawanie kamery

1. Przejdź do **Urządzenia → Dodaj urządzenie → Kamera**, a potem **Dodaj kamerę**.
2. Wybierz typ: Wyze, Tapo, Sonoff albo **Inna kamera (RTSP)**.
3. Wykonaj kroki, które pokazuje Cora dla tego typu. Mówią, co najpierw włączyć w aplikacji samej kamery.
4. Wpisz nazwę, adres strumienia, nazwę użytkownika, hasło i akwarium, a potem dotknij **Testuj połączenie**. Gdy kamera odpowie, dotknij **Dodaj kamerę**.

Podczas dodawania telefon musi być w tej samej sieci Wi-Fi co kamera. Adres musi należeć do Twojej sieci domowej, a nazwę użytkownika i hasło wpisujesz w osobnych polach, nie w adresie.

Przetestowano kamery Wyze, Tapo i Sonoff (Wyze Cam v4, Tapo C120 i Sonoff Cam S3W). Inne kamery z RTSP też mogą działać.

| Kamera | Co włączyć najpierw |
|---|---|
| Wyze | W aplikacji Wyze otwórz kamerę, potem Ustawienia, Ustawienia zaawansowane, RTSP. Włącz RTSP, wybierz nazwę użytkownika i hasło, a potem uruchom kamerę ponownie. Kamera potrzebuje firmware 4.52.17 albo nowszego. |
| Tapo | W aplikacji Tapo otwórz Ustawienia, Ustawienia zaawansowane, Konto kamery i utwórz nazwę użytkownika oraz hasło. To nie jest Twoje konto TP-Link. Kamera Tapo może jednocześnie obsługiwać tylko dwie z trzech rzeczy: Tapo Care, nagrywanie na kartę SD i przesyłanie do innych aplikacji. |
| Sonoff | W eWeLink włącz RTSP dla kamery i ustaw jej konto. Cora wypełnia za Ciebie ustawienie **Adres Sonoff**. |
| Inna kamera (RTSP) | Włącz RTSP albo ONVIF w aplikacji kamery, ustaw login do kamery i wpisz adres strumienia z jej instrukcji. Zostaw login pusty, jeśli Twoja kamera go nie ma. |

## Zmiana ustawień kamery

Otwórz kamerę i użyj jej menu: **Zmień nazwę**, **Edytuj adresy**, **Zmień hasło** albo **Usuń kamerę**. Usunięcie kamery kasuje też jej zapisane hasło.

## Oglądanie

Kamera może być kafelkiem na pulpicie, do 3×2, a otworzysz ją na **Pełny ekran** i możesz ją **Obróć**.

W domu, gdy telefon jest w sieci Wi-Fi kamery, Cora odtwarza **Wideo na żywo** prosto z kamery. Poza domem albo gdy wybierzesz **Zdjęcia**, Twój Cora Max robi zdjęcia z kamery, a Cora pokazuje je jako obraz prawie na żywo, odświeżany co kilka sekund. Jeśli Cora Max nie przysyła obrazów, kafelek o tym informuje.

## Czuwanie skimmera

:::note Beta
**Beta.** Czuwanie skimmera jest w wersji Beta i dostępne tylko dla użytkowników Beta. Wymaga też płatnego planu: **Czuwanie skimmera jest częścią płatnych planów.** Aby poprosić o dostęp do Beta, skontaktuj się z [pomocą techniczną](/support.html).
:::

Czuwanie skimmera obserwuje kubek odpieniacza przez kamerę i ostrzega Cię, zanim się przeleje. Znajdziesz je na stronie kamery, na karcie **Czuwanie skimmera**.

1. Skieruj kamerę na kubek i włącz **Obserwuj kubek**.
2. Dotknij **Zaznacz kubek**. Przeciągnij ramkę na kubek i dopasuj rogi: dolną krawędź na dnie kubka, górną tuż pod jego brzegiem, tam gdzie kubek jest pełny.
3. Opróżnij kubek i dotknij **Kubek jest teraz pusty**. Cora robi zdjęcie pustego kubka do porównania. Trwa to około 10 sekund. Jeśli przesuniesz kamerę albo ramkę, zrób to jeszcze raz.
4. Ustaw **Alert przy** na poziom napełnienia, przy którym ma Cię ostrzec. Karta pokazuje go w procentach.

Cora Max sprawdza kubek co kilka minut. Karta pokazuje ostatni odczyt i to, jak dawno go zrobiono. **Sprawdź teraz** prosi o natychmiastowe sprawdzenie i trwa około 10 sekund. **Ostatnie 24 godziny** pokazuje, jak kubek napełniał się w ciągu doby.

Jeśli obraz trudno odczytać, karta o tym informuje, na przykład **Zbyt jasne światło za kubkiem**.

### Wskazówki dla kamery

**Wskazówki dla kamery** na karcie dają te same rady co tutaj.

- Ustaw w kamerze widzenie nocne na Włączone (zawsze podczerwień), a nie na Auto, aby każdy obraz wyglądał tak samo w dzień i w nocy.
- Ustaw reflektor kamery na Ręczny i zostaw go wyłączony. Bąbelki i woda w sumpie liczą się jako ruch i ciągle go włączają.
- Unikaj silnego światła świecącego prosto w kamerę zza kubka.

## Co dzieje się ze zdjęciami

W domu wideo jest odtwarzane prosto z kamery i nie jest nagrywane. Poza domem dla każdej kamery zachowywane jest tylko jedno zdjęcie, a każde nowe zastępuje poprzednie. Czuwanie skimmera przechowuje ostatnie zdjęcie zaznaczonego kubka, odczyty napełnienia z ostatnich 24 godzin (same liczby) i jedno małe zdjęcie pustego kubka. Są usuwane, gdy usuniesz kamerę, akwarium albo swoje konto. Pełne szczegóły znajdziesz w [polityce prywatności](/privacy-policy.html).

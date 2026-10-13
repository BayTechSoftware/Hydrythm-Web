---
title: Kamery i Czuwanie skimmera
description: Dodaj do Cory kamerę Wyze, Tapo, Sonoff albo inną kamerę RTSP, oglądaj akwarium na kafelku albo na pełnym ekranie i pozwól, żeby Czuwanie skimmera ostrzegło Cię, zanim kubek odpieniacza się przepełni.
section: Cora Mobile
reviewed: 2026-10-13
order: 17
group: Equipment
---

:::note Beta
**Beta.** Kamery są w wersji Beta i są dostępne tylko dla użytkowników Beta. Jeśli nie jesteś użytkownikiem Beta, nie zobaczysz ich w **Dodaj urządzenie**. Aby poprosić o dostęp do Beta, skontaktuj się z [pomocą techniczną](/support.html). Więcej w [Funkcjach Beta](/help/mobile-beta).
:::

Dodaj kamerę, żeby widzieć akwarium w Corze, w telefonie i na Cora Max, i żeby Czuwanie skimmera pilnowało kubka odpieniacza. Zacznij od **Urządzenia → Dodaj urządzenie → Kamera**. Kamera wymaga Cora Max w akwarium, więc wiersz **Kamera** pokazuje **Wymaga Cora Max**, dopóki akwarium go nie ma.

## Dodawanie kamery {#adding-a-camera}

1. Przejdź do **Urządzenia → Dodaj urządzenie → Kamera**, a potem **Dodaj kamerę**.
2. Wybierz typ: Wyze, Tapo, Sonoff albo **Inna kamera (RTSP)**.
3. Wykonaj kroki, które Cora pokazuje dla tego typu. Mówią, co najpierw włączyć we własnej aplikacji kamery.
4. Wpisz nazwę, adres strumienia, nazwę użytkownika, hasło i akwarium, a potem dotknij **Testuj połączenie**. Gdy kamera odpowie, dotknij **Dodaj kamerę**.

Podczas dodawania telefon musi być w tej samej sieci Wi-Fi co kamera. Adres musi być w Twojej sieci domowej, a nazwę użytkownika i hasło wpisujesz w osobnych polach, a nie w adresie.

Kamery Wyze, Tapo i Sonoff zostały przetestowane (Wyze Cam v4, Tapo C120 i Sonoff Cam S3W). Inne kamery z RTSP też mogą działać.

| Kamera | Co najpierw włączyć |
|---|---|
| Wyze | W aplikacji Wyze otwórz kamerę, potem Settings, Advanced Settings, RTSP. Włącz RTSP, wybierz nazwę użytkownika i hasło, a potem uruchom kamerę ponownie. Kamera potrzebuje oprogramowania 4.52.17 albo nowszego. |
| Tapo | W aplikacji Tapo otwórz Ustawienia, Ustawienia zaawansowane, Konto kamery i utwórz nazwę użytkownika i hasło. To nie jest Twoje konto TP-Link. Kamera Tapo może jednocześnie obsługiwać tylko dwie z tych rzeczy: Tapo Care, nagrywanie na kartę SD i przesyłanie obrazu do innych aplikacji. |
| Sonoff | W eWeLink włącz RTSP dla kamery i ustaw jej konto. Cora wypełnia za Ciebie gotowe ustawienie **Adres Sonoff**. |
| Inna kamera (RTSP) | Włącz RTSP albo ONVIF w aplikacji kamery, ustaw login kamery i wpisz adres strumienia z jej instrukcji. Zostaw login pusty, jeśli kamera go nie ma. |

## Zmiana kamery {#changing-a-camera}

Otwórz kamerę i użyj jej menu: **Zmień nazwę**, **Edytuj adresy**, **Zmień hasło** albo **Usuń kamerę**. Usunięcie kamery kasuje też jej zapisane hasło.

## Oglądanie {#watching-it}

![Strona kamery](img/mobile-camera.webp "Strona kamery, z obrazem na górze i kartą Czuwanie skimmera pod spodem.")

Kamera może być kafelkiem na pulpicie, o rozmiarze do 3×2. Zobacz [Edytowanie pulpitu](/help/mobile-dashboard-editing). Otwórz ją, żeby użyć **Pełny ekran** i **Obróć**.

W domu, gdy telefon jest w sieci Wi-Fi kamery, Cora odtwarza **Wideo na żywo** prosto z kamery. Poza domem albo gdy wybierzesz **Zdjęcia**, Twój Cora Max robi zdjęcia z kamery, a Cora pokazuje je prawie na żywo, odświeżane co kilka sekund. Jeśli Cora Max nie wysyła obrazów, kafelek o tym mówi.

## Czuwanie skimmera {#skimmer-watch}

:::note Beta
**Beta.** Czuwanie skimmera jest w wersji Beta i jest dostępne tylko dla użytkowników Beta. Wymaga też płatnego planu. Bez niego karta pokazuje **Czuwanie skimmera jest częścią płatnych planów.** i proponuje **Zobacz plany**. Aby poprosić o dostęp do Beta, skontaktuj się z [pomocą techniczną](/support.html).
:::

Czuwanie skimmera obserwuje kubek odpieniacza przez kamerę i ostrzega Cię, zanim się przepełni. Jest na stronie kamery, na karcie **Czuwanie skimmera**.

![Zaznaczanie kubka](img/mobile-camera-mark-cup.webp "Przeciągnij ramkę na kubek: dolna krawędź na dnie kubka, górna tuż pod brzegiem.")

1. Skieruj kamerę na kubek i włącz **Obserwuj kubek**.
2. Dotknij **Zaznacz kubek**. Przeciągnij ramkę na kubek i dopasuj rogi: dolna krawędź na dnie kubka, górna tuż pod brzegiem, tam, gdzie kubek jest pełny. Później przycisk ma nazwę **Przesuń ramkę kubka**.
3. Opróżnij kubek i dotknij **Kubek jest teraz pusty**. Cora robi zdjęcie pustego kubka do porównań. Trwa to około 10 sekund. Jeśli przesuniesz kamerę albo ramkę, zrób to ponownie.
4. Przeciągnij suwak **Alert przy** do poziomu napełnienia, przy którym chcesz dostać ostrzeżenie. Zostaw trochę zapasu, bo Cora sprawdza co 15 minut.

![Karta Czuwanie skimmera na stronie kamery](img/mobile-skimmer-watch.webp "Kubek jest teraz pusty, ostatni odczyt, ostatnie 24 godziny, Sprawdź teraz i wskazówki dla kamery.")

Cora Max sprawdza kubek co 15 minut. Karta pokazuje ostatni odczyt i to, jak dawno był, a kafelek kamery na pulpicie też pokazuje poziom w kubku. **Sprawdź teraz** sprawdza kubek od razu, co trwa około 10 sekund. **Ostatnie 24 godziny** pokazuje, jak kubek napełniał się w ciągu dnia.

Gdy kubek dojdzie do poziomu **Alert przy**, dostaniesz jedno powiadomienie. Jest wysyłane w kategorii **Awarie sprzętu**, więc nie wyłączaj jej w [Powiadomieniach](/help/mobile-notifications). Po opróżnieniu kubka alert jest gotowy, żeby zadziałać ponownie.

### Gdy odczyt wygląda źle {#skimmer-watch-problems}

| Karta pokazuje | Co zrobić |
|---|---|
| **Zbyt jasne światło za kubkiem** | Wyłącz albo przestaw światło za kubkiem. Zobacz wskazówki dla kamery niżej |
| **Niepewne (niska pewność)** | Obraz był trudny do odczytania. Sprawdź wskazówki dla kamery, a potem dotknij **Sprawdź teraz** |
| **Najpierw zaznacz kubek** | Dotknij **Zaznacz kubek** i narysuj ramkę |
| **Brak kalibracji: opróżnij kubek i dotknij Kubek jest teraz pusty** | Opróżnij kubek, a potem dotknij **Kubek jest teraz pusty** |
| **Ramka przesunięta: skalibruj ponownie** | Przesunięto ramkę. Opróżnij kubek i znów dotknij **Kubek jest teraz pusty** |
| **Cora Max nie mógł pobrać obrazu z kamery.** | Sprawdź, czy kamera jest włączona, a Cora Max akwarium jest online |
| **Ostatnie sprawdzenie nie powiodło się.** | Dotknij **Sprawdź teraz**. Jeśli błąd się powtarza, zobacz [Rozwiązywanie problemów](/help/troubleshooting) |
| **Brak odczytu. Cora Max sprawdza co 15 minut.** | Poczekaj na pierwsze sprawdzenie albo dotknij **Sprawdź teraz** |

### Wskazówki dla kamery {#camera-tips}

**Wskazówki dla kamery** na karcie dają te same rady co tutaj.

- Ustaw widzenie nocne kamery na Włączone (zawsze podczerwień), a nie Auto, żeby każdy obraz wyglądał tak samo w dzień i w nocy.
- Ustaw reflektor kamery na Ręczny i zostaw go wyłączony. Bąbelki i woda w sumpie liczą się jako ruch i ciągle go włączają.
- Nie pozwól, żeby silne światło świeciło prosto w kamerę zza kubka.

### Na Cora Max {#skimmer-watch-on-cora-max}

![Kafelki kamer na Cora Max, jeden z poziomem w kubku odpieniacza](img/max-skimmer-watch.webp "Na Cora Max kafelek kamery pokazuje poziom w kubku i wiek odczytu.")

Na Cora Max kafelek kamery i kamera na pełnym ekranie pokazują **Kubek** z poziomem napełnienia i wiekiem odczytu. Chip robi się bursztynowy, gdy kubek jest w granicach 10 punktów od Twojego poziomu alertu, i czerwony, gdy go osiągnie. Na kamerze na pełnym ekranie przycisk **Alarm przy** otwiera **Alarm kubka odpieniacza**, gdzie też możesz zmienić poziom. Podczas sprawdzania obraz na żywo może zatrzymać się na kilka sekund. Więcej w [Sterowaniu sprzętem z Cora Max](/help/max-device-control).

## Co dzieje się ze zdjęciami {#pictures}

W domu wideo jest odtwarzane prosto z kamery i nie jest nagrywane. Poza domem dla każdej kamery przechowywane jest tylko jedno zdjęcie, a każde nowe zastępuje poprzednie. Czuwanie skimmera przechowuje ostatnie zdjęcie zaznaczonego kubka, odczyty napełnienia z ostatnich 24 godzin (same liczby) i jedno małe zdjęcie pustego kubka. Są usuwane, gdy usuniesz kamerę albo konto. Pełne szczegóły są w [polityce prywatności](/privacy-policy.html).

---
title: Więcej niż jedno urządzenie Cora
description: Wybierz, które urządzenie odpowiada głosem, a które odpytuje każde akwarium.
section: Cora Mobile
reviewed: 2026-09-27
order: 29
group: Account
---

W domu może być więcej niż jeden Cora Max. Dwa ustawienia decydują, który co robi, żeby nie dublowały swojej pracy. Warto też wiedzieć, co w ogóle jest między nimi wspólne.

## Co jest wspólne, a co nie

| Wspólne dla wszystkich urządzeń | Osobne dla każdego ekranu |
|---|---|
| Akwaria, odczyty i historia | Układ pulpitu |
| Urządzenia i ich ustawienia | Wi-Fi, jasność, dźwięk |
| Dziennik, obsada, konserwacja | Fraza wybudzająca i blokada rodzicielska |
| Alerty, progi, automatyzacje | Akwaria widoczne na tym ekranie |
| Plany i wykorzystanie | |

Zmiana progu na jednym urządzeniu działa wszędzie. Zmiana układu pulpitu już nie. Każdy ekran ma własny układ, a telefon i Cora Max nigdy nie dzielą jednego.

## Cora Assistant: urządzenie odpowiadające

**Ustawienia → Cora Assistant → Urządzenie odpowiadające** określa, które **urządzenie Cora** odpowiada, gdy mówisz do pokoju. Odpowiada zawsze tylko jedno, bez względu na to, ile Cię słyszy. Wybierz to, które stoi najbliżej miejsca, gdzie zwykle jesteś.

To inne ustawienie niż opisane niżej Główne Cora Max. Urządzenie odpowiadające decyduje, które urządzenie odpowiada na Twój głos. Główne Cora Max decyduje, które urządzenie odpytuje sprzęt akwarium. Jeśli masz w domu dwa Cora Max, możesz ustawić je różnie.

![Wybór urządzenia odpowiadającego](img/mobile-voice-responder.webp "Przy każdym urządzeniu widać, na jaką frazę reaguje i czy jest online.")

Przy każdym urządzeniu na liście widać frazę wybudzającą, na którą reaguje, i to, czy jest online. **Te frazy nie muszą być takie same.** Fraza jest wbudowana w samo urządzenie, więc różne modele Cora mogą reagować na różne frazy. Sprawdź frazę w wierszu danego urządzenia i nie zakładaj, że w domu obowiązuje jedna.

:::note Telefonu nie ma na tej liście
Telefon nie reaguje na frazę wybudzającą. Rozmowę zaczynasz na nim dotknięciem. To działa zawsze i nie zależy od tego ustawienia. Na liście jest tylko sprzęt Cora z obsługą głosu.
:::

## Główne Cora Max

Sprzęt w Twojej sieci odczytuje Cora Max. Gdyby kilka urządzeń mogło odczytywać ten sam kontroler, bez tego ustawienia odpytywałyby go równolegle.

**Główne Cora Max** to wybór dla każdego akwarium osobno: które urządzenie odczytuje kontroler tego akwarium. W Cora Mobile otwórz akwarium i dotknij **Główne Cora Max**.

| Ustawienie | Jak działa |
|---|---|
| Wybrane urządzenie | Tylko to urządzenie Cora odpytuje kontroler. Pozostaje główne także wtedy, gdy jest offline, i inne urządzenia Cora go nie zastępują. Cora Mobile odpytuje kontroler tylko wtedy, gdy to urządzenie jest offline. |
| **Każde aktywne (automatycznie)** | Aplikacja i każde urządzenie Cora online dzielą się pracą (liczy się ostatni zapis). Gdy jedno przejdzie w tryb offline, inne pracuje dalej. Dobre, gdy masz tylko jedno urządzenie, i bezpieczniejsze ustawienie domyślne, jeśli nie wiesz, które urządzenie ma się tym zajmować. |

Gdy wybrane urządzenie jest offline, polecenie, które musi przez nie przejść, nie zostanie wykonane. Cora poinformuje Cię, że akwarium jest ustawione na to urządzenie, że urządzenie jest offline i że nic się nie wykonało. Spróbuj ponownie, gdy urządzenie wróci. Jeśli będzie offline dłużej, wybierz inne urządzenie albo **Każde aktywne (automatycznie)**.

:::note Gdy dwa urządzenia obsługują jedno akwarium, wybierz główne
Wybór głównego urządzenia odciąża kontroler i usuwa zdublowane odczyty z tego samego źródła.
:::

:::note To ustawienie dotyczy akwarium w całym koncie, a nie jednego urządzenia
Główne Cora Max należy do akwarium, a nie do telefonu czy Cora Max, na który akurat patrzysz. Zmiana na dowolnym urządzeniu działa w całym domu.
:::

## Co działa poza domem

Gdy jesteś poza siecią Wi-Fi akwarium, telefon nie łączy się ze sprzętem bezpośrednio. Polecenie trafia do Cora Cloud, a Cora Cloud przekazuje je do Cora Max przy akwarium. To ten Cora Max łączy się ze sprzętem.

W praktyce:

- **Odczyty i historia** są dostępne zawsze i wszędzie, bo są już zapisane w Cora Cloud.
- **Sterowanie sprzętem** (przełączenie gniazda, karmienie, dawka z głowicy, wstrzymanie pompy) działa też poza domem, jeśli Cora Max przy akwarium jest online i ma połączenie z tym sprzętem. Jeśli żaden nie ma, polecenie nie dotrze.
- **Ustawienia samego urządzenia** (a nie jego odczyty) czasem wymagają telefonu w *tej samej* sieci co urządzenie. Sam Cora Max przy akwarium wtedy nie wystarczy. Jeśli tak jest, strona urządzenia mówi o tym wprost.

Dwa komunikaty mówią, że polecenie nie przeszło bez problemu:

- **„Nic nie zostało wysłane”**: polecenie nie wyszło z telefonu albo żaden Cora Max przy akwarium nie mógł go przyjąć. Nic się nie wykonało. Zobaczysz to, gdy Główne Cora Max akwarium jest offline i żadne inne urządzenie w tym akwarium nie może go zastąpić.
- **„Mogło już zostać wykonane”**: polecenie zostało wysłane, ale żaden Cora Max nie potwierdził go na czas. Cora naprawdę nie wie, czy się wykonało. Zanim spróbujesz ponownie, sprawdź stan samego sprzętu, żeby nie wysłać polecenia dwa razy.

Jeśli któryś z tych komunikatów się powtarza, sprawdź, czy Cora Max przy akwarium jest online. Możesz też ustawić **Główne Cora Max** na **Każde aktywne (automatycznie)**, żeby polecenie mogło odebrać każde urządzenie online. Wszystkie możliwe wyniki polecenia opisuje [Sterowanie sprzętem](/help/mobile-device-control).

## Gdzie widać stan każdego urządzenia

Cora Max pokazuje stan odpytywania każdego akwarium w **Ustawienia → Ustawienia Cora Max → Stan**. Więcej w [Urządzeniach i ich stanie](/help/max-devices).

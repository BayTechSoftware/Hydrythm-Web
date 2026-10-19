---
title: Więcej niż jedno urządzenie Cora
description: Gdy masz więcej niż jedno urządzenie Cora, wybierz, które odpowiada na Twój głos, a które odpytuje każde akwarium, i sprawdź, co działa poza domem.
section: Cora Mobile
reviewed: 2026-10-13
order: 36
group: Settings and account
twin: max-reef-room
---

Ta strona jest dla domu z więcej niż jednym Cora Max albo z Cora Max i kilkoma telefonami. Dwa ustawienia decydują, które urządzenie co robi, żeby nie wykonywały dwa razy tej samej pracy. Warto też wiedzieć, co jest między nimi wspólne.

## Co jest wspólne, a co nie

| Wspólne dla wszystkich urządzeń | Należy do jednego Cora Max |
|---|---|
| Akwaria, odczyty i historia | Jego układ panelu |
| Urządzenia i ich ustawienia | Wi-Fi, jasność, dźwięk |
| Dziennik, obsada, konserwacja | Fraza aktywująca i blokada rodzicielska |
| Alerty, progi, automatyzacje | Które akwaria pokazuje ten ekran |
| Plany i wykorzystanie | |

Jeśli zmienisz próg na jednym urządzeniu, zmieni się wszędzie. Z układami panelu jest inaczej. Układ w telefonie idzie za Twoim kontem, więc każdy telefon, na którym się zalogujesz, pokazuje ten sam. Każdy Cora Max ma własny układ, a telefon i Cora Max nigdy nie dzielą jednego.

## Cora Assistant: Urządzenie odpowiadające {#cora-assistant-answering-device}

**Ustawienia → Cora Assistant → Urządzenie odpowiadające** wybiera **urządzenie Cora**, które odpowiada, gdy mówisz do pokoju. Niezależnie od tego, ile urządzeń Cię słyszy, odpowiada tylko jedno. Wybierz to, które jest najbliżej miejsca, w którym zwykle stoisz.

Frazy aktywującej nasłuchuje tylko Urządzenie odpowiadające. Gdy jest offline albo nie było widziane dłużej niż 15 minut, nasłuchiwanie przejmuje inny Cora Max i przestaje, gdy tamto wróci. Więcej w [Rozmowie z Corą](/help/max-voice).

To ustawienie jest niezależne od opisanego niżej Głównego Cora Max. Urządzenie odpowiadające decyduje, kto odpowiada na Twój głos. Główne Cora Max decyduje, kto odpytuje sprzęt akwarium. Mając w domu dwa Cora Max, możesz ustawić je różnie.

![Wybór Urządzenia odpowiadającego](img/mobile-voice-responder.webp "Przy każdym urządzeniu widać, na co reaguje i czy jest online.")

Każde urządzenie na liście pokazuje swoją frazę aktywującą i to, czy jest online. **Frazy aktywujące nie zawsze są takie same.** Fraza jest wytrenowana w urządzeniu, więc różne modele Cora mogą reagować na różne frazy. Sprawdź wiersz każdego urządzenia. Nie zakładaj, że cały dom używa jednej frazy.

:::note Telefonu nie ma na tej liście
Telefon nie nasłuchuje frazy aktywującej. Rozmowę zaczynasz na nim dotknięciem i to działa zawsze, niezależnie od tego ustawienia. Lista pokazuje tylko sprzęt Cora z obsługą głosu.
:::

## Główne Cora Max {#primary-cora-max}

Cora Max odczytuje sprzęt w Twojej sieci. Gdyby więcej niż jeden mógł połączyć się z tym samym kontrolerem, wszystkie odpytywałyby go równolegle.

**Główne Cora Max** pozwala wybrać dla każdego akwarium, które urządzenie odczytuje kontroler tego akwarium. W Cora Mobile otwórz akwarium i dotknij **Główne Cora Max**.

| Ustawienie | Działanie |
|---|---|
| Wybrane urządzenie | To jedyne urządzenie Cora, które odpytuje kontroler. Pozostaje główne, nawet gdy jest offline, a inne urządzenia Cora go nie zastępują. Cora Mobile odczytuje kontroler tylko wtedy, gdy to urządzenie jest offline. |
| **Każde aktywne (automatycznie)** | Cora Mobile i każde urządzenie Cora online dzielą się pracą (wygrywa ostatni zapis). Gdy jedno przejdzie w tryb offline, inne pracuje dalej. Dobre dla domu z jednym urządzeniem i bezpieczniejszy wybór, jeśli nie masz pewności, które urządzenie powinno obsługiwać akwarium. |

Gdy wybrane urządzenie jest offline, polecenie, które musi przez nie przejść, nie zostanie wykonane. Cora powie Ci, że akwarium jest ustawione na to urządzenie, że jest ono offline i że nic się nie wykonało. Spróbuj ponownie, gdy wróci. Jeśli będzie offline przez dłuższy czas, wybierz inne urządzenie albo **Każde aktywne (automatycznie)**.

:::note Dwa urządzenia pilnują jednego akwarium? Ustaw główne
Wybór głównego urządzenia odciąża kontroler i usuwa zdublowane odczyty z tego samego źródła.
:::

:::note To ustawienie należy do akwarium
Główne Cora Max ustawia się dla każdego akwarium w całym koncie. Nie należy do telefonu ani do Cora Max, który akurat masz w ręku. Zmień je na dowolnym urządzeniu, a zmieni się dla całego domu.
:::

## Co działa poza domem {#what-works-away-from-home}

Gdy jesteś poza siecią Wi-Fi akwarium, telefon nie łączy się ze sprzętem bezpośrednio. Polecenie trafia do Cora Cloud, która przekazuje je do Cora Max przy akwarium. To ten Cora Max łączy się ze sprzętem.

Co to dla Ciebie oznacza:

- **Odczyty i historia** są zawsze dostępne, gdziekolwiek jesteś. Są już zapisane w Cora Cloud.
- **Sterowanie sprzętem** działa też poza domem, jeśli Cora Max przy akwarium jest online i może połączyć się z tym sprzętem. Dotyczy to na przykład przełączenia gniazda, uruchomienia karmienia, dawki z głowicy albo wstrzymania pompy. Jeśli żaden Cora Max nie może się z nim połączyć, polecenie nie dotrze.
- **Własne ustawienia urządzenia** (jego natywne ustawienia, a nie odczyty) czasem wymagają telefonu w *tej samej* sieci co urządzenie. Cora Max przy akwarium wtedy nie wystarczy. Strona tego urządzenia mówi, kiedy tak jest.

Dwa komunikaty mówią, że polecenie nie przeszło bez problemu.

- **„Nic nie zostało wysłane”** oznacza, że polecenie nigdy nie wyszło z telefonu albo żaden Cora Max przy akwarium nie mógł go przyjąć. Nic się nie wykonało. Zobaczysz to, gdy Główne Cora Max akwarium jest offline, a żadne inne urządzenie przy tym akwarium nie może go zastąpić.
- **„Mogło już zostać wykonane”** oznacza, że polecenie wyszło, ale żaden Cora Max nie potwierdził go na czas. Cora naprawdę nie wie, czy się wykonało. Sprawdź sam sprzęt, zanim spróbujesz ponownie, żeby nie wysłać polecenia dwa razy.

Jeśli któryś z tych komunikatów się powtarza, sprawdź, czy Cora Max przy akwarium jest online. Możesz też ustawić **Główne Cora Max** na **Każde aktywne (automatycznie)**, żeby polecenie mogło przejąć każde urządzenie online. Wszystkie możliwe wyniki polecenia wymienia [Sterowanie sprzętem](/help/mobile-device-control).

## Gdzie widać stan każdego urządzenia

Cora Max pokazuje stan odpytywania każdego akwarium w **Ustawienia → Ustawienia Cora Max → Stan**. Więcej w [Urządzeniach i ich stanie](/help/max-devices).

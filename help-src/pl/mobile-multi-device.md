---
title: Więcej niż jedno urządzenie Cora
description: Wybierz, które urządzenie odpowiada głosem i które odpytuje każde akwarium.
section: Cora Mobile
reviewed: 2026-09-27
order: 29
group: Account
---

Gospodarstwo domowe może mieć więcej niż jedno Cora Max. Dwa ustawienia decydują, które co robi, dzięki czemu nie powielają swojej pracy, a trzecia rzecz, którą warto znać, to co jest między nimi wspólne w ogóle.

## Co jest wspólne, a co nie

| Wspólne dla każdego urządzenia | Należy do jednego ekranu |
|---|---|
| Akwaria, odczyty i historia | Jego układ pulpitu |
| Urządzenia i ich ustawienia | Wi-Fi, jasność, dźwięk |
| Dziennik, obsada, konserwacja | Fraza budząca i blokada rodzicielska |
| Alerty, progi, automatyzacje | Które akwaria pokazuje ten ekran |
| Plany i wykorzystanie | |

Zmiana progu na jednym urządzeniu zmienia go wszędzie. Zmiana układu pulpitu nie: każdy ekran zachowuje swój własny układ, a telefon i Cora Max nigdy go nie dzielą.

## Cora Assistant: urządzenie odpowiadające

**Ustawienia → Cora Assistant → Urządzenie odpowiadające** wybiera, które **urządzenie Cora** odpowiada, gdy mówisz do pokoju. Odpowiada tylko jedno, niezależnie od tego, ile może Cię usłyszeć; ustaw to na jednostkę najbliższą miejscu, w którym zwykle stoisz.

To jest inny wybór niż Primary Cora Max poniżej: Answering device decyduje, które urządzenie odpowiada na Twój głos, a Primary Cora Max decyduje, które urządzenie odpytuje sprzęt akwarium. Gospodarstwo domowe z dwoma tabletami może chcieć ustawić je inaczej.

![Wybór odpowiadającego głosowo](img/mobile-voice-responder.webp "Każde urządzenie pokazuje, na co nasłuchuje i czy jest online.")

Każde urządzenie na liście pokazuje frazę budzącą, na którą nasłuchuje, wraz z tym, czy jest online. **Te nie są wszystkie takie same.** Fraza budząca jest wytrenowana w samo urządzenie, więc różne modele Cora mogą nasłuchiwać różnych fraz. Odczytaj frazę z wiersza samego urządzenia, a nie zakładaj, że gospodarstwo domowe ma jedną wspólną.

:::note Twój telefon nie jest na tej liście
Telefon nie nasłuchuje frazy budzącej. Rozmowę na nim zaczynasz dotknięciem, co działa zawsze i nie jest zależne od tego ustawienia. Lista wybiera tylko sprzęt Cora z możliwością głosową.
:::

## Główne Cora Max

Sprzęt w Twojej sieci jest odczytywany przez Cora Max. Gdy więcej niż jedno urządzenie może odczytać ten sam kontroler, odpytywałyby go równolegle, gdyby nie to ustawienie.

**Główne Cora Max** to wybór, dla każdego akwarium odrębnie, które urządzenie odczytuje kontroler tego akwarium. W Cora Mobile otwórz akwarium i dotknij **Główne Cora Max**.

| Ustawienie | Zachowanie |
|---|---|
| Nazwane urządzenie | Staje się jedynym urządzeniem Cora, które odpytuje kontroler, i pozostaje główne nawet, gdy jest offline: inne urządzenia Cora nie przejmują jego roli. Cora Mobile odpytuje tylko, gdy jest offline. |
| **Każde aktywne (automatycznie)** | Aplikacja i każde online'owe urządzenie Cora dzielą tę pracę (wygrywa ostatni zapis), więc jeśli jedno przechodzi offline, inne przejmuje pracę. Odpowiednie dla gospodarstwa z jednym urządzeniem i bezpieczniejsza wartość domyślna, gdy nie jesteś pewien, które urządzenie powinno to obsługiwać. |

Gdy nazwane urządzenie jest offline, polecenie, które musi przejść przez nie, nie zostanie wykonane: Cora mówi Ci, że akwarium jest ustawione na to urządzenie, że jest ono offline i że nic nie zostało wykonane, więc możesz spróbować ponownie, gdy wróci. Jeśli będzie offline na dłużej, wybierz inne urządzenie albo **Każde aktywne (automatycznie)**.

:::note Ustaw główne urządzenie, gdy dwa urządzenia śledzą jedno akwarium
Nazwanie głównego urządzenia zmniejsza obciążenie kontrolera i usuwa zduplikowane odczyty z tego samego źródła.
:::

:::note To jest ustawienie dla całego konta, dla danego akwarium, nie dla danego urządzenia
Primary Cora Max należy do akwarium, nie do telefonu czy tabletu, na który akurat patrzysz. Zmiana go z jakiegokolwiek urządzenia zmienia je dla całego gospodarstwa domowego.
:::

## Co działa poza domem

Twój telefon nie rozmawia z Twoim sprzętem bezpośrednio, gdy jesteś poza własną siecią Wi-Fi akwarium. Zamiast tego polecenie wędruje do Cora Cloud, która przekazuje je do Cora Max stojącego przy akwarium; to Cora Max faktycznie dosięga sprzętu.

To znaczy:

- **Odczyty i historia** są zawsze dostępne, gdziekolwiek jesteś, bo są już zapisane w Cora Cloud.
- **Kontrola sprzętu** (przełączanie gniazda, uruchamianie karmienia, dozowanie głowicą, wstrzymywanie pompy) działa też poza domem, o ile Cora Max przy akwarium jest online i może dosięgnąć tego sprzętu. Jeśli żaden nie może, polecenie nie może zostać dostarczone.
- **Własne ustawienia urządzenia** (w przeciwieństwie do jego odczytów) czasem wymagają telefonu w *tej samej* sieci co samo urządzenie, nie tylko Cora Max przy akwarium. Gdzie to ma zastosowanie, strona mówi to wprost.

Dwie wiadomości mówią Ci, że polecenie po prostu się nie powiodło:

- **"Nothing was sent"**: polecenie nigdy nie opuściło Twojego telefonu albo żaden Cora Max przy akwarium nie mógł go przyjąć. Nic nie zostało wykonane. To zobaczysz, jeśli główne Cora Max akwarium jest offline i żadne inne urządzenie na tym akwarium nie może go zastąpić.
- **"It may already have run"**: polecenie zostało wysłane, ale żaden Cora Max nie odpowiedział na czas, aby to potwierdzić. Cora naprawdę nie wie, czy zostało wykonane. Sprawdź stan samego sprzętu przed ponowną próbą, aby nie wysłać polecenia dwukrotnie.

Jeśli którakolwiek z tych wiadomości powtarza się, sprawdź, czy Cora Max przy akwarium jest online, albo ustaw **Główne Cora Max** na **Każde aktywne (automatycznie)**, aby każde online'owe urządzenie mogło odebrać polecenie. Zobacz [Kontrola sprzętu](/help/mobile-device-control) po pełną listę wyników, jakie może mieć polecenie.

## Gdzie pokazany jest stan każdego urządzenia

Cora Max zgłasza własny stan odpytywania i głosu w **Ustawienia → Cora Max → Oprogramowanie → Stan i sterowanie urządzeniem**. Zobacz [Urządzenia i ich stan](/help/max-devices).

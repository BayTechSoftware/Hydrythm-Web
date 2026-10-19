---
title: Alerty na Cora Max
description: Co zrobić, gdy na Cora Max wyskoczy alert, jak go uśpić albo odrzucić, jak zmienić progi alertów przy ścianie i ustawić dźwięk alertu.
section: Cora Max
reviewed: 2026-10-13
order: 8
group: Alerts and automation
twin: mobile-alerts
---

Ta strona opisuje, co robi Cora Max, gdy coś wymaga Twojej uwagi, i co możesz zmienić przy ścianie. Jak działają zakresy, reguły i powiadomienia w telefonie, opisują [Alerty i progi](/help/mobile-alerts).

## Gdy pojawia się alert

Gdy odczyt wyjdzie poza zakres, urządzenie zgłosi usterkę, dawka zostanie pominięta albo kończy się zasób, Cora Max pokazuje alert na środku ekranu. Pod nim są trzy przyciski.

1. **Odpowiedz głosem** zaczyna rozmowę z Corą o tym alercie, więc nie musisz niczego więcej dotykać. Więcej w [Rozmowie z Corą](/help/max-voice).
2. **Uśpij** wycisza alert na tym Cora Max na jakiś czas. Przycisk pokazuje, na jak długo, na przykład **Uśpij na 1 h**. To czas wstrzymania ustawiony dla tego alertu w ustawieniach alertów w Cora Mobile i może wynosić nawet 1 tydzień (przydaje się przy czymś takim jak niski poziom odczynnika, który przez kilka dni się nie zmieni).
3. **Odrzuć** zamyka alert od razu. Na tym ekranie alert milczy, dopóki problem nie zniknie. Jeśli wróci później, dostaniesz nowy alert.

Gdy alert dotyczy dozownika, na przykład kończącego się płynu w głowicy DŌS albo ReefDose lub pominiętej dawki, karta ma też przycisk **Otwórz DŌS** albo **Otwórz ReefDose**. Przenosi on na stronę tego dozownika, gdzie ustawia się jego alerty.


Jeśli Uśpij albo Odrzuć pokaże błąd, spróbuj jeszcze raz. Jeśli błąd się powtarza, zobacz [Alert nie znika](/help/troubleshooting#an-alert-is-not-clearing).

:::note Uśpienie działa tylko na tym Cora Max
Gdy alert jest uśpiony albo odrzucony, ten Cora Max przestaje go wyświetlać, odtwarzać dźwięk i wypowiadać, a alert znika z górnego paska. Telefon nadal dostaje powiadomienia, inne ekrany Cora Max nadal pokazują alert, alert zostaje w **Historii powiadomień**, a ustawienia alertów się nie zmieniają.
:::

## Alerty na górnym pasku

Każdy aktywny alert pojawia się też jako mała etykieta na górnym pasku, dość duża, żeby zauważyć ją z drugiego końca pokoju. Jeśli wszystkie się nie mieszczą, zobaczysz **+2** (albo inną liczbę).

- Dotknij etykiety, żeby przywrócić ten alert na środek ekranu.
- Dotknij **+2**, żeby otworzyć **Aktywne alarmy**, listę wszystkiego, co jest aktywne. Dotknij pozycji na liście, żeby ją otworzyć.

## Skrzynka powiadomień

**Ustawienia → Ustawienia Cora Max → Historia powiadomień** to skrzynka całego Twojego konta. Zawiera każde podsumowanie, alarm i komunikat konta dla Twojego systemu, także te, których nie zgłosił ten ekran, i wszystko, co ominęło telefon. Gdy odczyt wyjdzie poza zakres i wróci, zobaczysz oba zdarzenia.

## Edytowanie progów {#editing-thresholds}

![Ustawienia akwarium na Cora Max, z Progami alertów, Jednostkami i Głównym Cora Max](img/max-tank-settings.webp "Najpierw Progi alertów i Jednostki, potem Główny Cora Max dla tego akwarium.")

Dotknij nazwy akwarium na górnym pasku i wybierz **Progi alertów** albo przejdź do **Ustawienia → [Twoje akwarium] → Progi alertów**. Oba otwierają te same zakresy, które widzisz w telefonie, a zmiana wprowadzona tutaj działa wszędzie.

Próg możesz też zmienić, przytrzymując jego widżet na panelu, albo głosem: *„Hey Cora, ustaw alert pH na 7,9 do 8,4.”* Cora powie, jaka to zmiana, i poczeka na Twoje OK.

Każdy parametr na liście ma własny przełącznik. Przy wyłączonym alercie widać **Alert wyłączony**. Cora zachowuje jego zakres, ale nie ocenia tego odczytu, dopóki alert jest wyłączony. Widżet zostaje neutralnie szary i nigdy nie wywoła alertu. Jeśli parametr nie ma jeszcze alertu, widać **Brak ustawionego alertu**, a **Dodaj alert** ustawia go z pokazanym zakresem.

![Lista Progi alertów na Cora Max](img/max-alerts.webp "Każdy odczyt ma własny przełącznik. Odczyt bez alertu pokazuje Brak ustawionego alertu i przycisk Dodaj alert.")

Arkusz progu ma ten sam przełącznik na górze, obok **Alert włączony** albo **Alert wyłączony**. Jeśli zapiszesz nowy zakres dla wyłączonego alertu, Cora zapyta **Włączyć ten alert?** Dotknij **Włącz**, żeby włączyć go z nowymi wartościami, albo **Zostaw wyłączony**, żeby zapisać wartości i zostawić alert wyłączony.

## Alerty urządzeń i zasobów {#doser-alerts}

Sprzęt, w którym coś się kończy, ma na swojej stronie na Cora Max przycisk **Ustawienia alertów**. Dotyczy to Tridenta (odczynniki i odpady), głowic DŌS, Red Sea ReefDose, ReefATO+ i ReefMat. Wybierz poziom, o którym chcesz wiedzieć, a po jego przekroczeniu dostaniesz jedno powiadomienie. W głowicy DŌS **Alerty o pominiętej dawce** informują też, gdy głowica pominie zaplanowane dawki.

Co oznacza każdy alert dozownika, opisują [Alerty dozownika](/help/mobile-device-control#doser-alerts).


## Dźwięk alertu, alerty głosowe i wybudzanie ekranu

Te ustawienia dotyczą tylko tego ekranu. Znajdziesz je w **Ustawienia → Ustawienia Cora Max**.

- **Dźwięk alertu** (w **DŹWIĘK I GŁOS**) odtwarza dźwięk, gdy przychodzi nowy alert. Suwak ustawia głośność.
- **Alerty głosowe** (w **DŹWIĘK I GŁOS**) sprawiają, że Cora wypowiada alert na głos.
- **Włącz ekran przy alarmie** (w **EKRAN**) rozjaśnia przyciemniony ekran, gdy przychodzi alert. Alerty krytyczne zawsze go wybudzają.

Żeby Cora Max w ogóle nie pokazywał alertów na ekranie, otwórz Cora Mobile, przejdź do **Urządzenia →** Twój Cora Max i wyłącz **Alerty**. Historia powiadomień i powiadomienia w telefonie się nie zmieniają.

:::note Jeden alert dla całego konta
Urządzenia nie wywołują osobnych kopii alertu. Cora Max, telefon i każdy inny ekran pokazują ten sam alert, który znika na wszystkich, gdy odczyt wróci do zakresu.
:::

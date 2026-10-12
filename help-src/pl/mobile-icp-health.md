---
title: ICP i raporty zdrowia
description: Prześlij test ICP, śledź każdy pierwiastek w czasie i zleć pełną ocenę zdrowia systemu.
section: Cora Mobile
reviewed: 2026-10-12
order: 26
group: Intelligence
---

W zakładce **Inteligencja** są Twoje wyniki laboratoryjne i zmiany w dłuższym okresie.

![Zakładka Inteligencja](img/mobile-intelligence.webp "Prześlij ICP, zleć raport zdrowia i zobacz, co się zmieniło od ostatniego razu.")

## Przesyłanie testu ICP

Dotknij **Przesłać ICP**, wybierz akwarium i dodaj wynik z laboratorium. Cora odczyta raport, zapisze każdy pierwiastek i porówna go z poprzednimi testami.

Nie musisz niczego przepisywać. Cora rozpoznaje popularne formaty raportów laboratoryjnych.

## Jaki e-mail może wykorzystać laboratorium

Laboratorium albo wynik wysłany e-mailem znajduje Twoje konto po adresie e-mail, który zna. To Twój e-mail do logowania oraz każdy e-mail laboratorium, który dodasz w **Ustawienia → karta Twojego konta → E-maile laboratorium i ICP**.

1. Dotknij **Dodaj e-mail laboratorium** i wpisz adres, którego używa Twoje laboratorium.
2. Dotknij **Wyślij kod**. Cora wysyła 6-cyfrowy kod na ten adres. Wygasa po 10 minutach.
3. Wpisz kod i dotknij **Potwierdź**. Jeśli go nie dostałeś, dotknij **Wyślij kod ponownie**.

Możesz dodać do 3 e-maili laboratorium. Każdy pokazuje **Potwierdzony** albo **Czeka na kod**, a **Usuń** zdejmuje go z listy. Potem wyniki wysłane na ten adres nie trafiają już na Twoje konto. Nie można dodać adresu, który należy już do innego konta Cora.

Jeśli zalogowałeś się ukrytym adresem Apple, laboratoria nie znajdą Twojego konta. Ekran ICP pokazuje wtedy kartę **Otrzymuj wyniki z laboratorium automatycznie**, która prowadzi do tego ustawienia. Przy logowaniu przez Apple wybierz **Udostępnij mój adres e-mail**, aby uniknąć problemu.

## Wysyłka do Cory: wyniki, które dostarcza laboratorium albo e-mail

Niektóre laboratoria mogą wysłać wynik prosto do Cory. Wynik ICP, który przyszedł e-mailem, też można tak przekierować. Nie musisz wtedy niczego przesyłać samodzielnie.

Gdy wynik dotrze, pojawi się baner: *„Wynik laboratoryjny od {lab} czeka na Ciebie.”* Dotknij **Wybierz zbiornik** i wybierz akwarium, do którego należy wynik. Cora nie zgadnie tego sama. Po wyborze Cora doda wynik do tego akwarium tak samo jak przesłany raport.

W samym raporcie, przy nagłówku, widać **Wysłane przez {lab}**. Dzięki temu odróżnisz go od raportu przesłanego samodzielnie.

:::note Za pierwszym razem
Gdy wynik pierwszy raz przyjdzie w ten sposób, Cora pokaże krótką podpowiedź, co się dzieje. Dzięki temu nie wygląda to na błąd.
:::

### Pierwszy wynik od nowego laboratorium

Gdy laboratorium wysyła Ci wynik po raz pierwszy, Cora prosi o jego zatwierdzenie, zanim doda go do jakiegokolwiek akwarium, nawet jeśli masz tylko jedno akwarium. Zobaczysz, kto go wysłał, i możesz zaznaczyć **Ufaj temu laboratorium**, żeby pominąć tę kontrolę przy kolejnym wyniku od tego samego laboratorium.

Dotknij **Zatwierdź**, żeby dodać wynik, albo **Odrzuć**, żeby go usunąć bez dodawania do żadnego akwarium. **Ustawienia → Zaufane laboratoria** pokazuje wszystkie laboratoria dodane w ten sposób do zaufanych, a **Odwołaj** usuwa jedno z nich, więc jego kolejny wynik znowu będzie wymagał zatwierdzenia.

Jeśli to nie działa, zajrzyj do [Rozwiązywania problemów](/help/troubleshooting).

![Raport ICP](img/mobile-icp-report.webp "Każdy raport ma ocenę i podsumowanie napisane dla Twojego akwarium.")

## Co dostajesz

**Ocenę** w skali do 100 i podsumowanie zwykłym językiem, co to oznacza dla Twojego systemu: typu akwarium, jego wieku i obsady.

Ocena wynika z porównania wyników z zakresami docelowymi, także z tymi, które ustawiasz samodzielnie. Każdy wynik poza zakresem ogranicza ocenę do 70 lub mniej, więc nie może ona pokazać **Zdrowe**. Wynik daleko poza zakresem ogranicza ją do 40 lub mniej, bez względu na to, jak dobre są pozostałe. Pod oceną jest etykieta: **Zdrowe** od 71 do 100, **Wymaga uwagi** od 40 do 70 i **Krytyczne** od 0 do 39. Raporty zdrowia są oceniane tak samo.

**Wszystkie śledzone pierwiastki**, czyli główne parametry, a także pierwiastki śladowe i zanieczyszczenia. Cora zapisuje wszystkie 71 pierwiastków, które może podać laboratorium, a linia, którą niektóre laboratoria nazywają *Acidity*, to pH.

W każdym wierszu pierwiastka widzisz zakres wydrukowany przez laboratorium, pokazany jako *Zakres laboratorium*, obok własnego zakresu Cory dla tego pierwiastka. Pierwiastek, dla którego Cora nie ma zakresu odniesienia, ma znacznik **Brak zakresu Cora**. Raport podaje, ile pierwiastków ma zakres Cory, a resztę ocenia na podstawie ogólnej wiedzy o akwariach rafowych. Asystent Cora komentuje każdy przebadany pierwiastek, a jego komentarz zostaje, nawet gdy nie ma zakresu Cory.

Jeśli laboratorium drukuje *n.d.* albo *not detected* dla pierwiastka, Cora zapisuje go jako 0 i pisze, że nie wykryto.

:::note Rozpuszczony CO2 to nie CO2 w pomieszczeniu
**Rozpuszczony CO₂** w raporcie ICP to CO2 w wodzie, w mg/L. To inny odczyt niż CO2 w powietrzu w pomieszczeniu, który mierzy monitor powietrza Inkbird w wersji Beta. Mają inne zakresy i nigdy się ich nie miesza. Zobacz [Funkcje Beta](/help/mobile-beta).
:::

**Największe zmiany.** Karta „Od Twojego ostatniego ICP” pokazuje, co zmieniło się najbardziej od ostatniego testu. Zwykle najszybciej tak zrozumiesz nowy raport.

**Trendy.** Dotknij **Trendy**, żeby zobaczyć dowolny pierwiastek we wszystkich przesłanych testach. Tu ICP przestaje być pojedynczym zdjęciem i zaczyna być naprawdę przydatne.

:::tip Ciekawie robi się od drugiego testu
Jeden ICP mówi, gdzie jesteś. Drugi pokazuje, w którą stronę zmierzasz, a z tą wiedzą łatwiej coś zrobić. Rób testy regularnie i nie czekaj, aż coś będzie nie tak.
:::

## Test wody RO/DI albo wody źródłowej

Jeśli przesyłasz próbkę wody RO/DI albo innej wody źródłowej, powiedz o tym przy przesyłaniu. Cora nie ocenia jej według celów Twojego akwarium. Podaje prosty werdykt, czy woda jest wystarczająco czysta do użycia, i trzyma te liczby poza odczytami akwarium. Raport zaznacza, ile wyników to woda źródłowa. Cora robi tak samo ze świeżo zmieszaną solą albo każdą inną próbką, która nie jest wodą z akwarium: mówi, jak wygląda próbka, i nie ocenia jej jak Twojego akwarium.

## Raporty zdrowia

**Raport zdrowia** to głębsza, okresowa ocena całego systemu. Bierze pod uwagę razem wszystkie parametry i źródła, dozowanie, historię i ostatnie wyniki ICP.

Dotknij **Raport zdrowia** i wybierz akwarium. Przygotowanie raportu chwilę trwa.

Korzystaj z niego, gdy chcesz przemyślanej oceny, a nie dzisiejszego skrótu. Na przykład przed dużą zmianą, po problemie albo co kilka tygodni dla kontroli.

## ICP a Twoje sondy

Cora porównuje wyniki laboratoryjne z tym, co podaje Twój sprzęt. Jeśli sonda alkaliczności pokazuje 8,4, a ICP 7,6, warto o tym wiedzieć. Cora pokazuje tę różnicę i nie wybiera po cichu jednej z wartości.

To jedna z najbardziej przydatnych rzeczy, jakie ICP daje w Corze. To **trzecia opinia, a nie rozstrzygający sędzia**. Laboratoria różnią się między sobą, a na wynik wpływa to, jak próbkę pobrano, przechowywano i transportowano. Pojedynczy ICP traktuj jako wskazówkę. Dwa zgodne testy są warte znacznie więcej niż jeden. Stała różnica to powód, żeby sprawdzić sondę, ale nie dowód, że sonda się myli.

:::tip Zmiana laboratorium albo metody
Zmiana laboratorium albo przejście między testami ICP-OES i ICP-MS w tym samym laboratorium może przesunąć wyniki, choć w akwarium nic się nie zmieniło. Cora zwraca na to uwagę przy porównaniu. ICP-OES nie mierzy bardzo niskich stężeń chromu, cyny, niklu, miedzi, kobaltu ani selenu. Wynik **Poniżej wykrywalności** dla tych pierwiastków w teście ICP-OES nie oznacza więc, że w akwarium ich nie ma.
:::

## Twój limit

Analizy ICP i raporty zdrowia są liczone w ramach Twojego planu. Linijka pod przyciskami pokazuje, ile wykorzystano w tym miesiącu.

Niezależnie od planu Cora przyjmuje najwyżej 10 przesłanych ICP dziennie. Przesłanie odrzucone z tego powodu nie zużywa żadnej analizy ICP z Twojego planu. Cora Mobile pokazuje wtedy jednak tylko ogólny błąd przesyłania. Jeśli po wielu próbach w jednym dniu przesyłanie przestaje działać, spróbuj jutro.

## Gdzie są raporty

Na ekranie Inteligencja oba rodzaje raportów są osobno. Wyniki laboratoryjne są w sekcji **Raporty ICP**, a wygenerowane przeglądy w **Raporty zdrowia**. Na każdej liście najnowsze są na górze, każdy z oceną. Dotknij raportu, żeby otworzyć go w całości.

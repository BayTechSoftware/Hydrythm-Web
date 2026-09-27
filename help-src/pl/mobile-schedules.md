---
title: Planowanie pracy sprzętu
description: Zbuduj program dnia dla pompy Jecod i skopiuj go między pompami, i podglądaj harmonogram gyre Maxspect (beta).
section: Cora Mobile
reviewed: 2026-09-17
order: 12
group: Equipment
---

Pompy i gyre mogą mieć **program dnia**: zestaw okresów, każdy z własną intensywnością, powtarzany codziennie. Cora może je tworzyć bezpośrednio dla pomp Jecod. Harmonogram gyre Maxspect *(beta)* można tutaj tylko podglądać: ustaw go w aplikacji Maxspect.

Otwórz urządzenie z zakładki **Urządzenia**.

![Harmonogram pompy](img/mobile-schedules.webp "Wykres dnia od 0 do 24 godzin, z każdym okresem wypisanym pod nim.")

## Same all day albo Schedule

Pompa działa w jednym z dwóch trybów, wybieranym na górze jej strony:

- **Tak samo cały dzień**: jedna intensywność, przez cały czas
- **Harmonogram**: program dnia z okresami

Twój wybór jest wysyłany do pompy, przez Cora Max przy akwarium, gdy Twój telefon nie jest w sieci pompy. Pompa Bluetooth musi być w zasięgu: dopóki nie jest, wybór tutaj tylko zmienia to, na co patrzysz.

## Edytor harmonogramu

Każdy ekran harmonogramu ma te same trzy części:

**Wykres dnia**: cały dzień od 0 do 24 godzin, z każdym okresem narysowanym jako blok, którego wysokość to jego intensywność. To najszybszy sposób, aby zobaczyć, czy program robi to, co myślisz.

**Lista okresów**: każdy okres pod wykresem, z jego godzinami, trybem i intensywnością: *Random, 00:00–03:00, Freq 50%, 40%*. Tutaj dodajesz, edytujesz i usuwasz okresy.

**Dodawanie i zmiana okresów**: **Dodaj do harmonogramu** dodaje okres. Otwórz okres, aby go zmienić, i dotknij **Zapisz**, albo **Usuń**, aby go usunąć; zostaniesz poproszony o potwierdzenie, zanim zniknie.

Gyre Maxspect *(beta)* ma dwie głowice, pokazane jako Gyre A i Gyre B, więc jego wykres dnia ma dwa tory, jeden dla każdej, a jego plany są wypisane pod **GYRE A** i **GYRE B**. Harmonogram gyre jest tylko do podglądu: jego wiersz akcji mówi **Tylko podgląd**, a harmonogram ustawia się w aplikacji Maxspect.

:::warning Harmonogram jest zapisywany na urządzeniu
Zapisanie wysyła program do sprzętu, który potem wykonuje go według swojego własnego zegara. Działa dalej niezależnie od tego, czy Cora jest dostępna.
:::

## Kopiowanie programu między pompami

Jeśli prowadzisz kilka pomp, które powinny działać podobnie, zbuduj jeden program i skopiuj go.

Otwórz pompę, której program chcesz skopiować, potem **Skopiuj harmonogram do…**, i wybierz pompę, na którą go skopiować.

## Zachowywanie i udostępnianie harmonogramu

Harmonogram, z którego jesteś zadowolony, nie musi być budowany od nowa:

- **Zapisz harmonogram jako…** zachowuje go pod nazwą, a **Zapisane harmonogramy…** stosuje go ponownie później.
- **Udostępnij ten harmonogram** zamienia go w krótki kod, a **Wklej kod harmonogramu…** stosuje kod, który ktoś Ci wysłał. To jest funkcja Cora Mobile; kod przenosi harmonogram, nie dostęp do Twojego konta.

## Poza siecią pompy

Gdy Twój telefon nie jest w sieci pompy, Cora Mobile działa przez Cora Max przy akwarium, z ograniczeniami:

- **Tak samo cały dzień** i **Harmonogram** przełączają pompę przez ten Cora Max.
- Okres, który dodajesz lub zmieniasz, przechodzi przez niego tylko, jeśli dotarł do pompy w ostatniej godzinie. Jeśli nie, harmonogram mówi to wprost i nie można go zmienić z miejsca, w którym jesteś.
- **Skopiuj harmonogram do…**, **Zapisz harmonogram jako…**, **Zapisane harmonogramy…**, **Udostępnij ten harmonogram** i **Wklej kod harmonogramu…** wymagają, aby Twój telefon był w sieci pompy. Do tego czasu są wyszarzone, a menu mówi, czemu.

Pompę Bluetooth można dosięgnąć tylko z telefonu znajdującego się blisko niej: stań w zasięgu, aby ją przełączyć, zmienić jej harmonogram albo użyć którejkolwiek z tych opcji.

## Stosowanie programu

Pompie można też podać przygotowany program w jednym kroku, a nie budować okresy ręcznie.

## Sprawdzanie, czy się przyjęło

Po zapisaniu strona urządzenia pokazuje program, który jednostka faktycznie wykonuje. Jeśli te dwa się różnią, zapis nie doszedł; sprawdź, czy urządzenie jest dostępne, i spróbuj ponownie.

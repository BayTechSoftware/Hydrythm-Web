---
title: Harmonogramy sprzętu
description: Ułóż program dnia dla pompy Jecod, skopiuj go na inne pompy i podejrzyj harmonogram gyre Maxspect (beta).
section: Cora Mobile
reviewed: 2026-09-17
order: 12
group: Equipment
---

Pompy i gyre mogą pracować według **programu dnia**. To zestaw okresów, każdy z własną intensywnością, powtarzany codziennie. W pompach Jecod Cora może sama tworzyć takie programy. Harmonogram gyre Maxspect *(beta)* możesz tu tylko podejrzeć, a ustawiasz go w aplikacji Maxspect.

Otwórz urządzenie w zakładce **Urządzenia**.

![Harmonogram pompy](img/mobile-schedules.webp "Wykres dnia od 0 do 24 godzin, a pod nim lista okresów.")

## Tak samo cały dzień albo Harmonogram

Pompa pracuje w jednym z dwóch trybów. Wybierasz go na górze jej strony:

- **Tak samo cały dzień**: jedna intensywność przez cały czas
- **Harmonogram**: program dnia z okresami

Wybór trafia do pompy. Jeśli telefon nie jest w sieci pompy, idzie przez Cora Max przy akwarium. Pompa Bluetooth musi być w zasięgu. Dopóki nie jest, wybór zmienia tylko to, co widzisz na ekranie.

## Edytor harmonogramu

Każdy ekran harmonogramu ma te same trzy części.

**Wykres dnia** pokazuje cały dzień od 0 do 24 godzin. Każdy okres jest blokiem, a jego wysokość to intensywność. Tak najszybciej sprawdzisz, czy program robi to, czego się spodziewasz.

**Lista okresów** jest pod wykresem. Przy każdym okresie widać godziny, tryb i intensywność, np. *Random, 00:00–03:00, Freq 50%, 40%*. Tutaj dodajesz, zmieniasz i usuwasz okresy.

**Dodaj do harmonogramu** dodaje nowy okres. Żeby zmienić okres, otwórz go i dotknij **Zapisz**. Żeby go usunąć, dotknij **Usuń**. Cora poprosi o potwierdzenie, zanim okres zniknie.

Gyre Maxspect *(beta)* ma dwie głowice, Gyre A i Gyre B, więc jego wykres dnia ma dwa tory, po jednym dla każdej. Plany są wypisane pod **GYRE A** i **GYRE B**. Harmonogram gyre służy tylko do podglądu. W wierszu akcji widać **Tylko podgląd**, a harmonogram ustawiasz w aplikacji Maxspect.

:::warning Harmonogram zapisuje się w urządzeniu
Po zapisaniu program trafia do sprzętu, a sprzęt realizuje go według własnego zegara. Działa dalej, nawet gdy Cora jest nieosiągalna.
:::

## Kopiowanie programu na inne pompy

Jeśli masz kilka pomp, które powinny pracować podobnie, ułóż jeden program i go skopiuj.

Otwórz pompę z programem, który chcesz skopiować, wybierz **Skopiuj harmonogram do…** i wskaż pompę docelową.

## Zapisywanie i udostępnianie harmonogramu

Dobrego harmonogramu nie musisz układać od nowa:

- **Zapisz harmonogram jako…** zachowuje go pod wybraną nazwą, a **Zapisane harmonogramy…** pozwala go później przywrócić.
- **Udostępnij ten harmonogram** zamienia go w krótki kod, a **Wklej kod harmonogramu…** wczytuje kod, który ktoś Ci wysłał. To funkcja Cora Mobile. Kod przenosi sam harmonogram, a nie dostęp do Twojego konta.

## Poza siecią pompy

Gdy telefon nie jest w sieci pompy, Cora Mobile łączy się przez Cora Max przy akwarium, ale z ograniczeniami:

- **Tak samo cały dzień** i **Harmonogram** przełączają pompę przez ten Cora Max.
- Dodany albo zmieniony okres przejdzie przez Cora Max tylko wtedy, gdy Cora Max łączył się z pompą w ciągu ostatniej godziny. Jeśli nie, harmonogram mówi to wprost i nie da się go zmienić z miejsca, w którym jesteś.
- **Skopiuj harmonogram do…**, **Zapisz harmonogram jako…**, **Zapisane harmonogramy…**, **Udostępnij ten harmonogram** i **Wklej kod harmonogramu…** wymagają telefonu w sieci pompy. Do tego czasu są wyszarzone, a menu wyjaśnia dlaczego.

Z pompą Bluetooth połączy się tylko telefon, który jest blisko niej. Podejdź w jej zasięg, żeby ją przełączyć, zmienić harmonogram albo użyć którejś z tych opcji.

## Zastosowanie programu

Pompie możesz jednym krokiem nadać zapisany harmonogram, bez ponownego układania okresów. Otwórz pompę, dotknij **Więcej** u góry i wybierz **Zapisane harmonogramy…**. Na liście są wszystkie harmonogramy zapisane dla tego akwarium, także te utworzone na innej pompie. Wybierz jeden i dotknij **Zastosuj**. Zastąpi on cały dzień pompy.

## Czy program się zapisał

Po zapisaniu strona urządzenia pokazuje program, który sprzęt naprawdę realizuje. Jeśli nie zgadza się z Twoim, zapis nie dotarł. Sprawdź, czy urządzenie jest osiągalne, i spróbuj ponownie.

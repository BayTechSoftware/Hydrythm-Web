---
title: Harmonogramy sprzętu
description: Ułóż harmonogram dla pompy Jecod w edytorze, skopiuj program z innych pomp lub na inne pompy, zapisz i udostępnij oraz sprawdź, czy pompa go przyjęła.
section: Cora Mobile
reviewed: 2026-11-03
order: 14
group: Equipment
---

Na tej stronie nadasz pompie Jecod **harmonogram**: zestaw okresów, każdy z własną intensywnością, powtarzany codziennie. Otwórz go z **Urządzenia** → dotknij pompy.

Lampy i pompy innych marek mają harmonogramy na własnych stronach: ReefDose od Red Sea w [Sterowaniu sprzętem](/help/mobile-device-control#red-sea).

![Strona pompy Jecod w Cora Mobile z wybranym Harmonogramem](img/mobile-schedules.webp "Harmonogram wybrany na górze, przerwa na karmienie, a pod nimi wykres dnia.")

## Ręcznie albo Harmonogram {#same-all-day-or-schedule}

Pompa pracuje w jednym z dwóch trybów. Wybierz go przełącznikiem na jej stronie. Działający jest oznaczony *· działa*, a strona otwiera się na nim.

- **Ręcznie** to jedna intensywność przez cały czas.
- **Harmonogram** to zestaw okresów powtarzany codziennie.

Gdy telefon jest w sieci pompy, Cora wysyła Twój wybór prosto do pompy. Jeśli nie jest, wybór idzie przez Cora Max przy akwarium. Pompa Bluetooth musi być w zasięgu. Dopóki nie jest, wybór zmienia tylko to, co widzisz na ekranie.

Przerwa na karmienie na chwilę zdejmuje pompę z harmonogramu, a w telefonie harmonogram wraca tylko wtedy, gdy strona pompy pozostaje otwarta. Zobacz [Przerwa na karmienie](/help/mobile-device-control#jecod-feeding).

## Edytor harmonogramu

Każdy ekran harmonogramu ma te same trzy części.

Na górze jest wykres dnia. Pokazuje cały dzień od 0 do 24 godzin, a każdy okres to blok, którego wysokość oznacza intensywność. Tak najszybciej sprawdzisz, czy program robi to, czego się spodziewasz.

Pod wykresem jest lista okresów. Przy każdym widać godziny, tryb i intensywność, na przykład *Random, 00:00–03:00, Freq 50%, 40%*. Tutaj dodajesz, zmieniasz i usuwasz okresy.

Każda zmiana harmonogramu przechodzi przez edytor. **Edytuj** otwiera go na dobie pompy, tak samo jak dotknięcie okresu albo **Dodaj do harmonogramu** na stronie pompy: edytor otwiera się z tym okresem albo nowym, gotowym do zmiany. W edytorze zmień okres i dotknij **Zapisz** albo usuń go przez **Usuń przedział**. **Cofnij** cofa o krok. Menu ⋮ ma **Zapisz harmonogram jako…**, **Zapisane harmonogramy…** i **Kopiuj z…**.

Nic nie jest wysyłane do pompy, dopóki nie dotkniesz **Zapisz w pompie**. Cora zapisuje wtedy całą dobę za jednym razem. Jeśli się nie uda, edytor mówi dlaczego i zachowuje Twoje zmiany. Jeśli zamykasz edytor przed zapisaniem, Cora najpierw pyta: *Odrzucić te zmiany?*


:::warning Zapisz w pompie wysyła harmonogram do urządzenia
Gdy dotkniesz **Zapisz w pompie**, Cora wysyła program do sprzętu, a sprzęt realizuje go według własnego zegara. Działa dalej niezależnie od tego, czy Cora może się z nim połączyć.
:::

## Kopiowanie programu na inne pompy {#copying-a-program-between-pumps}

Jeśli masz kilka pomp, które powinny pracować tak samo, ułóż jeden program i go skopiuj. Możesz kopiować w obie strony, a nic nie jest wysyłane, dopóki nie dotkniesz **Zapisz w pompie**.

- **Kopiuj z…** (w menu ⋮ harmonogramu i w menu edytora) pobiera harmonogram innej pompy cyrkulacyjnej z dowolnego Twojego akwarium. Każdy okres dostaje najbliższy tryb, jaki ma ta pompa, prędkości są ograniczane do tego, co może ona uruchomić, a **Co zmieni się w tej pompie** wymienia każdą zmianę. **Wczytaj do edytora** umieszcza kopię w edytorze tej pompy, gdzie możesz ją dopracować, a potem dotknąć **Zapisz w pompie**. Pompa, której harmonogramu Cora jeszcze nie odczytała, jest wyszarzona, z podanym powodem.
- **Skopiuj harmonogram do…** przekazuje dobę tej pompy innym pompom w dowolnym z Twoich akwariów, każda opisana jako *Akwarium · Pompa*. Zaznacz pompy i dotknij **Przejrzyj**. Nic nie jest jeszcze wysyłane. **Przejrzyj kopie** wymienia każdą pompę z jej stanem, **Nie zapisano**, **Zapisano na pompie** albo **Niepowodzenie** z powodem, oraz z liczbą zmian, które dostaje. **Otwórz edytor** otwiera własny edytor tej pompy ze skopiowaną dobą, z jego własnym **Zapisz w pompie**, które wysyła ją tylko do tej pompy. Jeśli zapis się nie uda, wersja robocza zostaje, więc możesz spróbować ponownie. Jeśli wychodzisz, gdy część pomp nie jest zapisana, Cora najpierw pyta: *Odrzucić niezapisane kopie?*

## Zachowywanie i udostępnianie harmonogramu

Gdy masz harmonogram, który Ci odpowiada, nie musisz układać go od nowa.

- **Zapisz harmonogram jako…** zachowuje go pod nazwą. **Zapisane harmonogramy…** przywraca go później: **Wczytaj do edytora** otwiera go w edytorze, a **Zapisz w pompie** go wysyła.
- **Udostępnij ten harmonogram** zamienia go w krótki kod. **Wklej kod harmonogramu…** wczytuje do edytora kod, który ktoś Ci wysłał, a nic nie jest wysyłane, dopóki nie dotkniesz **Zapisz w pompie**. To funkcja Cora Mobile. Kod przenosi tylko harmonogram. Nie daje nikomu dostępu do Twojego konta.

## Poza siecią pompy

Gdy telefon nie jest w sieci pompy, Cora Mobile łączy się przez Cora Max przy akwarium. Kilka rzeczy działa wtedy inaczej.

- **Ręcznie** i **Harmonogram** przełączają pompę przez ten Cora Max.
- Harmonogram, który zapisujesz w pompie, przejdzie tylko wtedy, gdy ten Cora Max połączył się z pompą w ciągu ostatniej godziny. Jeśli nie, harmonogram Ci o tym powie i nie zmienisz go z miejsca, w którym jesteś.
- **Skopiuj harmonogram do…**, **Zapisz harmonogram jako…**, **Zapisane harmonogramy…**, **Udostępnij ten harmonogram** i **Wklej kod harmonogramu…** wymagają telefonu w sieci pompy. Do tego czasu są wyszarzone, a menu wyjaśnia dlaczego.

Bez Cora Max przy akwarium możesz zmieniać pompę tylko wtedy, gdy telefon jest w jej sieci. Więcej w [Podłączaniu sprzętu](/help/mobile-connections#local-only).

Z pompą Bluetooth połączy się tylko telefon, który jest blisko niej. Stań w jej zasięgu, żeby ją przełączyć, zmienić harmonogram albo użyć którejś z tych opcji menu.

## Stosowanie programu

Pompie możesz jednym krokiem nadać zapisany harmonogram, bez ponownego układania okresów. Otwórz pompę, dotknij **Więcej** na górze i wybierz **Zapisane harmonogramy…**. Na liście są wszystkie harmonogramy zapisane dla tego akwarium, także te utworzone na innej pompie. Wybierz jeden i dotknij **Wczytaj do edytora**. Sprawdź go w edytorze, a potem dotknij **Zapisz w pompie**. Zastąpi on cały dzień pompy.

## Czy się zapisało

Po zapisaniu strona urządzenia pokazuje program, który realizuje pompa. Jeśli nie zgadza się z tym, co zapisano, zmiana nie dotarła. Sprawdź, czy urządzenie jest osiągalne, i spróbuj ponownie.

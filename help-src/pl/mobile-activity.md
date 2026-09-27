---
title: Aktywność i oś czasu
description: Wszystko, co przydarzyło się Twojemu sprzętowi, i co to spowodowało.
section: Cora Mobile
reviewed: 2026-09-09
order: 22
group: Records
---

Aktywność zapisuje każde **żądanie akcji** (każdą próbę zmiany czegoś) wraz z tym, co o to poprosiło i co się z tym stało.

Żądanie to nie to samo co zmiana. Odmówione żądania nie zostały wykonane, z jednym wyjątkiem: wpis mówiący *Żadne urządzenie nie odpowiedziało na czas* może się jednak wykonać, więc sprawdź sprzęt, zanim powtórzysz próbę. Żądania bez zmiany zastały sprzęt już w żądanym stanie, a niepotwierdzone może, ale nie musi, dotarło do urządzenia w ogóle. Wszystkie są zapisywane.

**Ustawienia → Activity.**

![Dziennik aktywności](img/mobile-activity.webp "Każda akcja, z miejscem, które o nią poprosiło.")

## Co jest zapisywane

Każde **żądanie**, nie tylko te, które zadziałały: przełączenia gniazd, cykle karmienia, dawki, zmiany wtyczek i wszystko, co zrobiła scenka albo automatyzacja.

Żądanie, które zostało **odmówione**, które nie spowodowało **żadnej zmiany** albo które wyszło i wróciło **niepotwierdzone**, jest zapisywane tak samo jak wykonane. To jest właśnie sens: polecenie, które po cichu nic nie zrobiło, jest dokładnie tym, co chcesz tu znaleźć.

## Co to spowodowało

Każdy wpis nazywa swoją przyczynę:

| Przyczyna | Znaczy |
|---|---|
| **Ta aplikacja** | Dotknąłeś tego tutaj |
| **Głos w tej aplikacji** | Zapytałeś, na tym telefonie |
| **Dotknięcie na Cora** | Ktoś użył ekranu Cora; wiersz mówi który |
| **Głos na Cora Max** | Ktoś powiedział coś do ekranu |
| **Cora Assistant** | Poprosiłeś Corę, aby to zrobiła |
| **Reguła automatyzacji** | Uruchomiła się reguła |
| **Smart przycisk** | Naciśnięto fizyczny przycisk |
| **Wysłane z Cora Cloud** | Wydane przez Twoje konto, a nie przez urządzenie przed Tobą |
| **Nieznane źródło** | Zapisane, zanim można było ustalić źródło |

## Jak dotarło

Każdy wiersz ma też plakietkę trasy, bo *jak* żądanie dotarło do Twojego sprzętu wiele wyjaśnia o tym, co poszło źle, gdy coś nie zadziałało:

| Plakietka | Znaczy |
|---|---|
| **LAN** | Wysłane przez Twoją własną sieć, bezpośrednio do sprzętu |
| **PRZEZ CHMURĘ** | Wysłane przez Twoje konto, dla sprzętu niedostępnego bezpośrednio |
| **TRASA ?** | Zapisane, zanim śledzono trasy: naprawdę nieznane, a nie zgadywane |

W systemie z więcej niż jednym Cora wiersz nazywa też, które urządzenie przekazało żądanie dalej.

## Oś czasu akwarium

Odrębnie od akcji sprzętu, każde akwarium ma **oś czasu**: odczyty, alerty, wpisy dziennika, wyniki ICP i zmiany obsady, ułożone po kolei.

Użyj aktywności, gdy pytasz *"co coś zrobiło?"*, a osi czasu, gdy pytasz *"co się działo wokół tej daty?"*

:::note Oś czasu i dziennik się uzupełniają
Oś czasu przechowuje to, co zapisała Cora; [dziennik](/help/mobile-journal) przechowuje to, co zrobiłeś Ty. Odczytane razem ustalają przyczynę i skutek wokół danej daty.
:::

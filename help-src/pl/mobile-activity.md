---
title: Aktywność i oś czasu
description: Co działo się z Twoim sprzętem i kto albo co to zleciło.
section: Cora Mobile
reviewed: 2026-09-09
order: 22
group: Records
---

Aktywność zapisuje każde **żądanie akcji**, czyli każdą próbę zmiany czegoś. Przy każdym widać, skąd przyszło i czym się skończyło.

Nie każde żądanie coś zmienia. Odrzucone żądania nie zostały wykonane, z jednym wyjątkiem: wpis *Żadne urządzenie nie odpowiedziało na czas* oznacza, że akcja mogła mimo wszystko się wykonać. Sprawdź sprzęt, zanim ją powtórzysz. Wynik bez zmiany oznacza, że sprzęt był już w żądanym stanie. Przy niepotwierdzonym żądaniu Cora nie wie, czy dotarło do urządzenia. Zapisywane są wszystkie wyniki.

**Ustawienia → Aktywność.**

![Dziennik aktywności](img/mobile-activity.webp "Każda akcja razem z miejscem, z którego ją zlecono.")

## Co jest zapisywane

Każde **żądanie**, także to, które nie zadziałało: przełączenie gniazda, cykl karmienia, dawka, zmiana wtyczki i wszystko, co zrobiła scena albo automatyzacja.

Żądanie **odrzucone**, takie, które **nic nie zmieniło**, i takie, które wróciło **niepotwierdzone**, trafia do listy tak samo jak wykonane. Właśnie o to chodzi. Polecenie, które po cichu nic nie zrobiło, to dokładnie to, czego tu szukasz.

## Skąd przyszło żądanie

Każdy wpis podaje swoje źródło:

| Źródło | Co oznacza |
|---|---|
| **Ta aplikacja** | Dotknięcie w Cora Mobile na tym telefonie |
| **Głos w tej aplikacji** | Polecenie głosowe na tym telefonie |
| **Dotknięcie na Cora** | Ktoś użył ekranu Cora, a wiersz podaje którego |
| **Głos na Cora Max** | Ktoś wydał polecenie głosowe na ekranie |
| **Cora Assistant** | Prośba do Cora Assistant |
| **Reguła automatyzacji** | Zadziałała reguła |
| **Smart przycisk** | Ktoś nacisnął fizyczny przycisk |
| **Wysłane z Cora Cloud** | Polecenie przyszło z Twojego konta przez Cora Cloud |
| **Nieznane źródło** | Wpis powstał, zanim dało się ustalić źródło |

## Jaką drogą dotarło

Każdy wiersz ma też etykietę trasy. Gdy coś nie zadziała, droga żądania do sprzętu często wyjaśnia, co poszło nie tak.

| Etykieta | Co oznacza |
|---|---|
| **LAN** | Żądanie poszło przez Twoją sieć prosto do sprzętu |
| **PRZEZ CHMURĘ** | Żądanie poszło przez Twoje konto, bo sprzęt nie był dostępny bezpośrednio |
| **TRASA ?** | Wpis sprzed śledzenia tras. Trasa jest naprawdę nieznana, Cora jej nie zgaduje |

Jeśli masz więcej niż jedno urządzenie Cora, wiersz podaje też, które z nich przekazało żądanie.

## Oś czasu akwarium

Poza akcjami sprzętu każde akwarium ma **oś czasu**. Są na niej po kolei odczyty, alerty, wpisy w dzienniku, wyniki ICP i zmiany obsady.

Do aktywności zaglądaj, gdy pytasz *„co coś zrobiło?”*. Do osi czasu, gdy pytasz *„co się działo w okolicach tej daty?”*.

:::note Oś czasu i dziennik się uzupełniają
Na osi czasu jest to, co zapisała Cora. W [dzienniku](/help/mobile-journal) są Twoje własne działania. Razem pokazują przyczynę i skutek w okolicach danej daty.
:::

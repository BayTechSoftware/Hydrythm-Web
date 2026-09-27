---
title: Powiadomienia
description: Wybierz, co ma docierać na telefon, i sprawdź, gdzie znaleźć to, co Cię ominęło.
section: Cora Mobile
reviewed: 2026-09-27
order: 16
group: Alerts and automation
---

W **Ustawienia → Powiadomienia** decydujesz o wszystkim, co Cora może Ci wysłać.

![Ustawienia powiadomień](img/mobile-notifications.webp "Każda kategoria może wysyłać push niezależnie od innych.")

## Co może wysyłać push

Każdą kategorię włączasz i wyłączasz osobno:

| Kategoria | Czego dotyczy |
|---|---|
| **Alerty parametrów** | Chemii wody poza ustawionym zakresem |
| **Przypomnienia o konserwacji** | Zaplanowanych zadań, np. podmian wody |
| **Awarie sprzętu** | Problemów zgłaszanych przez urządzenia, np. Tridenta, który przestał robić testy |
| **Kończące się zasoby** | Odczynnika, wody do dolewki, pojemników dozujących i pełnej butelki na odpady |
| **Raport ICP gotowy** | Wyników ICP, które są już przeanalizowane i gotowe do przeczytania |

Wyłączenie kategorii zatrzymuje tylko push. Zdarzenie nadal jest zapisywane i widać je pod dzwonkiem.

:::warning „Alerty parametrów” to tylko chemia wody
Łatwo pomyśleć, że ten przełącznik obejmuje wszystko, o czym może informować akwarium. Tak nie jest. Trident, który przestał robić testy, to **Awarie sprzętu**, a kończący się odczynnik to **Kończące się zasoby**. Każda z tych kategorii ma własny przełącznik. Jeśli od dawna masz włączone tylko Alerty parametrów i myślisz, że to wystarczy, sprawdź te dwie pozostałe.
:::

**Kończące się zasoby obejmują też butelkę na odpady**, choć ona się zapełnia, a nie opróżnia. Trafiła do tej kategorii, bo trzeba zrobić to samo: coś opróżnić albo wymienić, zanim testy się zatrzymają.

## Dzwonek

Jest w prawym górnym rogu każdego ekranu. Są pod nim wszystkie zdarzenia zgłoszone przez Corę, od najnowszych, także te, o których nie było push. Liczba przy dzwonku to zdarzenia, których jeszcze nie przeczytano.

Zajrzyj tu po dniu bez telefonu albo gdy coś zgłosiła kategoria, którą masz wyłączoną.

## Gdy nic nie przychodzi

Sprawdź po kolei:

1. **Ustawienia → Powiadomienia**: czy ta kategoria może wysyłać push?
2. Ustawienia telefonu: czy Cora w ogóle może wysyłać powiadomienia? Jeśli przy instalacji nie było na to zgody, ustawienia w Corze nic nie zmienią.
3. Czy w ogóle jest coś do wysłania? Reef Buddy milczy w dni, w które nic się nie zmieniło.

## Gdy przychodzi za dużo

Zanim wyłączysz powiadomienia, przejrzyj progi. Za dużo alertów zwykle oznacza, że zakres jest węższy niż wartości, w których naprawdę pracuje akwarium, albo że źródło wymaga kalibracji. Więcej w [Alertach i progach](/help/mobile-alerts).

Wyłączenie kategorii wyłącza ją w całości. Jeśli za często przychodzi jeden konkretny alert, zmień w jego regule **Czas wstrzymania między alertami**, od 15 minut do 1 tygodnia. Nie musisz wtedy wyłączać całej kategorii. Opcje czasu wstrzymania i to, jak działa odkładanie alertu na Cora Max, opisują [Alerty i progi](/help/mobile-alerts).

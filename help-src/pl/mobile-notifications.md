---
title: Powiadomienia
description: Wybierz, co dociera do Twojego telefonu, kiedy może przyjść, i gdzie przeczytać to, co przegapiłeś.
section: Cora Mobile
reviewed: 2026-09-27
order: 16
group: Alerts and automation
---

**Ustawienia → Powiadomienia** kontroluje wszystko, co Cora może Ci wysłać.

![Ustawienia powiadomień](img/mobile-notifications.webp "Każda kategoria może wysyłać push niezależnie.")

## Co może wysłać push

Każda kategoria jest przełączana niezależnie:

| Kategoria | Obejmuje |
|---|---|
| **Alerty parametrów** | Chemię wody poza ustawionym przez Ciebie zakresem |
| **Przypomnienia o konserwacji** | Zadania, które zaplanowałeś, jak podmiany wody |
| **Awarie sprzętu** | Urządzenie zgłaszające problem: na przykład Trident, który przestał testować |
| **Kończące się zasoby** | Reagent, wodę do dolewki, pojemniki dozujące i pełną butelkę odpadową |
| **Raport ICP gotowy** | Twoje wyniki ICP są przeanalizowane i gotowe do przeczytania |

Wyłączenie kategorii zatrzymuje push. Zdarzenie jest wciąż zapisywane i wciąż pojawia się w dzwonku.

:::warning "Alerty parametrów" znaczy chemia, i tylko chemia
Naturalne jest odczytanie tego przełącznika jako obejmującego wszystko, co akwarium może Ci powiedzieć. To nie tak. Trident, który przestał testować, to **Equipment Fault**, a kończący się reagent to **Kończące się zasoby**; każde ma swój własny przełącznik. Jeśli masz włączone Parameter Alerts od dawna i zakładałeś, że obejmuje resztę, sprawdź te dwa pozostałe.
:::

**Supplies Running Low obejmuje też butelkę odpadową**, która się zapełnia, a nie wyczerpuje. Jest w tej kategorii, bo wymagana akcja jest ta sama: coś do opróżnienia albo wymiany, zanim zatrzyma testy.

## Dzwonek

W prawym górnym rogu każdego ekranu. Przechowuje wszystko, co Cora podniosła, od najnowszego, niezależnie od tego, czy wysłała push. Liczba to to, czego jeszcze nie przeczytałeś.

To właściwe miejsce do sprawdzenia po dniu bez telefonu albo po tym, jak kategoria, którą wyłączyłeś, coś podniosła.

## Jeśli nic nie przychodzi

Przejdź przez tę listę:

1. **Ustawienia → Powiadomienia**: czy ta kategoria może wysyłać push?
2. Własne ustawienia Twojego telefonu: czy Cora może w ogóle powiadamiać? Uprawnienie odmówione podczas instalacji nadpisuje wszystko tutaj.
3. Czy jest w ogóle coś do wysłania? Reef Buddy milczy w dniach, gdy nic się nie zmieniło.

## Jeśli przychodzi za dużo

Przejrzyj swoje progi, zanim wyłączysz powiadomienia. Nadmierne alerty zwykle wskazują na zakres ustawiony ciaśniej niż to, w jakim akwarium faktycznie działa, albo na źródło wymagające kalibracji. Zobacz [Alerty i progi](/help/mobile-alerts).

Wyłączenie kategorii to wszystko-albo-nic dla tej kategorii. Jeśli za to jeden konkretny alert wysyła push za często, zmień jego **Czas wstrzymania między alertami** w samej regule, od 15 minut do 1 tygodnia, zamiast wyłączać całą kategorię. Zobacz [Alerty i progi](/help/mobile-alerts) po opcje czasu wstrzymania i co znaczy "snooze" na Cora Max.

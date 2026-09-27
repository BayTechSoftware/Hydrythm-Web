---
title: Urządzenia i ich stan
description: Co widzi Cora Max, które urządzenie odpytuje każde akwarium i co sprawdzić, gdy odpytywanie się zatrzymuje.
section: Cora Max
reviewed: 2026-09-27
order: 7
group: Equipment
---

**Ustawienia → Urządzenia** wypisuje sprzęt, który Cora Max widzi, i zgłasza, jak sobie radzi.

## Lista urządzeń

![Lista urządzeń](img/max-devices.webp "Filtruj według akwarium, a potem każde urządzenie z jednolinijkowym podsumowaniem tego, co zawiera.")

Cora Max widzi ten sam sprzęt co Twój telefon, bo obydwa czytają to samo konto.

Plakietki filtra na górze zwężają listę do **Wszystkie akwaria** albo jednego akwarium. Każdy wpis niesie punkt stanu, jednolinijkowe podsumowanie tego, co urządzenie zawiera (*21 gniazd · 4 karmienia*, *19 testów zostało*) oraz akwarium, do którego należy.

Dodawanie i konfigurowanie sprzętu jest łatwiejsze na telefonie; zobacz [Dodawanie, edytowanie i usuwanie urządzeń](/help/mobile-devices).

## Główne Cora Max: który tablet rozmawia z Twoim sprzętem

**Główne Cora Max** to tablet (albo inne urządzenie Cora), który odczytuje kontroler akwarium i inny sprzęt dla całego konta. Tylko jedno urządzenie musi to robić na akwarium; każdy inny ekran po prostu pokazuje to, co odczytuje.

Otwórz **Ustawienia → [your tank] → Główne Cora Max**, aby to zobaczyć albo zmienić. Są dwa rodzaje wyboru:

- **Każde aktywne (automatycznie)**: każde online'owe urządzenie Cora, które może dosięgnąć sprzętu tego akwarium, dzieli tę pracę, a wygrywa najnowszy zapis. To jest ustawienie do użycia, o ile nie masz konkretnego powodu, aby przypiąć jedno urządzenie.
- **Pin one device**: tylko to urządzenie odpytuje. Jeśli przypięte urządzenie przechodzi offline, nic nie odpytuje sprzętu tego akwarium, aż przypniesz inne albo przełączysz z powrotem na Any active (automatic).

Ten wybór jest dokonywany raz, dla akwarium, nie raz na ekran Cora. Zmień go z dowolnego Cora Max pokazującego to akwarium, albo z Cora Mobile; zobacz [Więcej niż jedno urządzenie Cora](/help/mobile-multi-device).

:::note Primary Cora Max to nie to samo co Cora Assistant
Primary Cora Max decyduje, które urządzenie **odczytuje Twój sprzęt**. Odrębne ustawienie, **Cora Assistant**, decyduje, które urządzenie **odpowiada na "Hey Cora"**. Gospodarstwo domowe z więcej niż jednym Cora Max może ustawić te dwie rzeczy niezależnie. Zobacz [Rozmowa z Corą na Cora Max](/help/max-voice).
:::

## Jeśli odczyty akwarium się zatrzymują

Jeśli odczyty jednego akwarium się zatrzymują, podczas gdy inne akwarium na tym samym ekranie wciąż się aktualizuje, zacznij od:

1. **Ustawienia → [that tank] → Główne Cora Max**: potwierdź, że urządzenie jest faktycznie przypisane i że jest online.
2. Jeśli wtórne Cora Max dla tego akwarium pokazuje plakietkę **Główne Cora offline** na górnym pasku, główne urządzenie utraciło połączenie; zobacz [Ekran główny Cora Max](/help/max-tour) po to, co znaczy plakietka stanu.
3. **Ustawienia → Ustawienia Cora Max → Sieć i aktualizacje → Odpytywanie urządzeń** pokazuje, jak często to urządzenie samo odczytuje Twoje urządzenia; ta wartość jest tutaj tylko do odczytu i jest ustawiana z Cora Mobile.

**Jeśli to nie działa:** zobacz [Rozwiązywanie problemów](/help/troubleshooting).

## Zarządzanie Cora Max z telefonu

Otwórz urządzenie z zakładki **Urządzenia** na telefonie, aby zobaczyć jego wariant, wersję firmware i kiedy było ostatnio widziane, oraz aby zmienić jego nazwę albo niektóre ustawienia bez podchodzenia do niego.

![Ustawienia Cora Max z telefonu](img/max-from-phone.webp "Interwał odpytywania, jasność, głośność, alerty na ekranie i licznik przygaszania.")

Ustawienia pokazane w ten sposób opisują **tylko ten ekran** (jego jasność, głośność, banery alertów na ekranie i licznik przygaszania), tak samo jak gdybyś je zmienił przy samej ścianie. Wyłączenie alertów na ekranie nie wpływa na historię alertów ani powiadomienia push.

Które akwaria pokazuje Cora Max, i które jest jego głównym Cora Max dla każdego akwarium, są wyborami dla całego konta; zmień je z dowolnego urządzenia, jak opisano powyżej.

:::note Stan urządzenia jest najpierw do odczytu
Sekcja **Stan** w **Ustawienia → Ustawienia Cora Max** na tym ekranie zgłasza stan odpytywania, czas ostatniego odpytania i ostatni zapis do chmury dla każdego akwarium, bez zmiany czegokolwiek. Użyj jej, aby ustalić, co się dzieje, przed zmianą ustawienia.
:::

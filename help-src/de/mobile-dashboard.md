---
title: Dein Dashboard lesen
description: So liest du Coras Dashboard: Widgets, Aktualität, Quellen und was die Farben bedeuten.
section: Cora Mobile
reviewed: 2026-09-09
order: 5
group: Your dashboard
---

Das Dashboard ist ein Raster aus **Widgets**, jedes zeigt eine Sache über ein Becken. Was darauf ist, entscheidest du ganz allein; siehe **[Dein Dashboard bearbeiten](/help/mobile-dashboard-editing)**.

![Ein Cora Mobile Dashboard](img/mobile-dashboard.webp "Anzeigen, Zahlen, Trends und Steuerungen auf einem Bildschirm.")

## Die Beckenkopfzeile

Oben auf jedem Dashboard:

- **Der Beckenname**, mit einem kleinen Symbol daneben: das ist eine **schnelle Umbenennung**, nicht mehr
- **Füttern**: pausiert Strömung und Abschäumung für eine Fütterung und stellt danach alles wieder her
- **Reef Buddy**: öffnet die heutige Zusammenfassung
- **Teilen**: sendet einen Schnappschuss des Dashboards
- **Der Stift rechts**: öffnet [das Beckenprofil](/help/mobile-tank-profile)

:::note Drei ähnliche Steuerelemente, drei Ziele
Das Symbol neben dem Namen benennt das Becken um. Der Stift rechts öffnet das **Profil** des Beckens. Das Bearbeiten des Dashboards selbst ist keines von beiden; das ist **Dashboard bearbeiten**, am *unteren Rand* des Dashboards, unterhalb der Widgets.
:::

Mit mehr als einem Becken wische seitwärts, um zwischen ihnen zu wechseln.

## Die Reef Buddy-Karte

Unter der Kopfzeile fasst eine Karte die neueste Zusammenfassung zusammen: eine Schlagzeile, ihre **Stabilitäts**- und **Daten**-Werte, und die Anzahl der Insights. Tippe darauf, um die vollständige Zusammenfassung zu öffnen, oder verwerfe sie mit **×**. Eine neue Karte erscheint mit der nächsten Zusammenfassung.

## Wie du ein Wasserwert-Widget liest

Ein Widget, das einen **gemessenen Wasserwert** zeigt, trägt dieselben drei Dinge an denselben Stellen. Geräte- und Steuerungskacheln (eine Steckdose, eine Dosiereinheit, eine Pumpe) zeigen stattdessen ihren eigenen Zustand, weil kein einzelner Messwert hinter ihnen steht.

**Der Wert** ist der Messwert selbst, groß und zentral.

**Das Alter** steht darunter oder daneben: `jetzt`, `1h`, `2d`. Das ist, wie lange es her ist, dass der Messwert erfasst wurde, nicht, wie lange es her ist, dass sich der Bildschirm aktualisiert hat. Eine Zahl, die sich seit zwei Tagen nicht bewegt hat, zeigt `2d`, und das ist eine Information.

**Das Quellen-Abzeichen** ist die kleine Markierung neben dem Alter. Es zeigt dir, woher die Zahl kommt: eine Sonde, ein Controller, ein Laborergebnis, oder du selbst mit einem Testkit. Tippe auf ein beliebiges Widget, um die Quelle ausgeschrieben zu sehen, zusammen mit ihrer letzten Historie.

:::note Warum das Alter so wichtig ist
Ein perfekter Alkalinitäts-Messwert von vor vier Tagen ist kein aktueller Alkalinitäts-Messwert. Das Alter steht neben jedem Wert, damit du den Unterschied auf einen Blick erkennst.
:::

## Farben

Cora setzt Farbe sparsam ein, und immer mit derselben Bedeutung:

| Farbe | Bedeutung |
|---|---|
| Grün | Deutlich innerhalb des Bereichs für diesen Wasserwert |
| Gelb | Nahe an einer Kante: **meist noch innerhalb des Bereichs**, innerhalb des letzten Zehntels davon |
| Rot | Über die Kante hinaus, und es lohnt sich, zu handeln |
| Grau | Kein Urteil: kein aktueller Messwert, oder kein nutzbarer Bereich zum Vergleich |

:::note Gelb bedeutet meist "noch in Ordnung, aber auf dem Weg wohin"
Gelb ist eine *Marge*, kein Verstoß. Ein Messwert innerhalb seines Bereichs, aber innerhalb der letzten 10 % davon, wird absichtlich gelb markiert, damit Abweichungen sichtbar sind, während noch Zeit zum Handeln bleibt, statt erst in dem Moment, in dem es zum Problem wird.

Daraus folgen zwei Verfeinerungen.

**Ein Bereich, den du selbst festgelegt hast, wird als erklärte Grenze behandelt.** Überschreite ihn, und das Widget wird direkt rot: keine gelbe Marge, weil du diese Linie absichtlich gezogen hast. Ein von **Cora vorgegebener** Bereich ist eine weichere Referenz: Ihn zu überschreiten zeigt für die ersten 10 % über der Kante Gelb, und wird darüber hinaus rot.

**Eine einseitige Grenze** (eine Obergrenze für einen Schadstoff, oder eine Untergrenze für einen Nährstoff) wird nur an ihrer hohen Kante bewertet, sodass Kupfer bei null grün angezeigt wird, statt gelb markiert zu werden, weil es nahe am unteren Ende der Skala liegt.
:::

Ein Widget mit gelbem oder rotem Rahmen braucht Aufmerksamkeit. Der Rahmen liegt am Widget, nicht nur an der Zahl, daher ist er auch beim Scrollen sichtbar.

## Unterhalb der Widgets

![Der untere Rand des Dashboards](img/mobile-dashboard-foot.webp "Dashboard bearbeiten, Wasserwerte protokollieren, und Verknüpfungen zu den vier Aufzeichnungsbereichen.")

Am unteren Rand des Dashboards:

- **Dashboard bearbeiten**: öffnet den [Dashboard-Editor](/help/mobile-dashboard-editing)
- **Wasserwerte protokollieren**: Testkit-Messwerte von Hand eingeben
- **Tagebuch · Warnungen · Wartung · Besatz**: Verknüpfungen zu diesen Bereichen für dieses Becken

Eine Zeile darüber zeigt, wann das Dashboard zuletzt aktualisiert wurde und auf welche Quellen es sich stützte.

## Durchtippen

Tippe auf ein beliebiges Widget, um dessen Detail zu öffnen: die vollständige Historie als Diagramm, jede Quelle, die es gemeldet hat, und die aktuell angewendeten Schwellenwerte. Von dort aus kannst du einen neuen Messwert von Hand protokollieren, den Bereich ändern, oder weiter zurückschauen.

## Wenn ein Widget keinen Wert hat

Ein Widget zeigt einen Wert, sobald es einen erhält. Wenn es leer ist, liegt das meist an einem dieser Gründe:

- Das Gerät ist offline; prüfe den Tab **Geräte**
- Der Wasserwert hat noch keine Quelle; protokolliere ihn von Hand, oder verbinde Ausrüstung, die ihn meldet
- Der Wasserwert wurde noch nie gemeldet oder protokolliert; dafür wurde noch nichts erfasst

Ein alter Messwert verschwindet nicht, weil das Diagrammfenster kürzer ist als sein Alter. Er bleibt mit seinem angezeigten Alter auf dem Widget, sodass ein veralteter Wert als veraltet erscheint, statt als fehlend.

Siehe **[Problembehebung](/help/troubleshooting)** für alles darüber hinaus.

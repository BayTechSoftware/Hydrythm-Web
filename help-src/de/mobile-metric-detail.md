---
title: Einen Wasserwert genauer ansehen
description: Tippe auf ein Widget, dann siehst du die ganze Historie, jede Quelle und wo du den Bereich änderst.
section: Cora Mobile
reviewed: 2026-09-09
order: 8
group: Your dashboard
---

Ein Widget zeigt dir eine Zahl. Tippst du darauf, siehst du die Geschichte dahinter.

## Was du hier findest

![Einen Wasserwert genauer betrachten](img/mobile-metric-detail.webp "Bereiche oben, dann die Quellen, die diesen Wasserwert melden, dann das Diagramm mit deinem schattierten Warnband.")

Ein **Historiendiagramm** mit eigener Zeitauswahl: **1h · 6h · 12h · 24h · 3d · 7d** und länger.

Einen **Quellenfilter**. Unter der Zeitauswahl steht eine Reihe Chips: **Alle** und je einer für jede Quelle, die diesen Wasserwert meldet, etwa *Apex*, *Cora*, *Red Sea* oder *Manuell*. Wähl einen aus, dann siehst du nur dessen Messwerte. So vergleichst du eine Sonde direkt mit einem Testkit, indem du im selben Diagramm zwischen beiden wechselst.

Einen **Link zum Dosierrechner** bei Wasserwerten, die du dosierst. Der Rechner nimmt das Beckenvolumen aus deinem [Beckenprofil](/help/mobile-tank-profile) und die Stärken aus [Dosierung](/help/mobile-dosing).

Eine **Vergleichsansicht**. Mit *Vergleichen mit* legst du einen zweiten Wasserwert ins selbe Diagramm, etwa Alkalinität und Calcium oder pH und Temperatur. Einen Zusammenhang, den du vermutest, siehst du dann direkt vor dir und musst ihn nicht im Kopf behalten.

**Kennzahlen** für den angezeigten Zeitraum: **MIN**, **DURCHSCHN.** und **MAX**, in einer Zeile unter dem aktuellen Wert.

**Dosiermarken** im Diagramm. So kannst du eine Bewegung mit dem abgleichen, was du tatsächlich dosiert hast.

Die **Liste der Rohmesswerte** mit jedem einzelnen Messwert hinter der Linie, samt Quelle und Zeitstempel.

Dein **Warnband**, schattiert im Diagramm. So liest du jeden Messwert im Verhältnis zu seinem Bereich. Den Bereich selbst änderst du, indem du das Widget auf dem Dashboard lange gedrückt hältst. Mehr dazu unter [Warnungen und Schwellenwerte](/help/mobile-alerts).

Und du kannst hier **einen Messwert von Hand eintragen**.

## Den passenden Zeitraum wählen

Welcher Zeitraum passt, hängt vom Rhythmus des Wasserwerts ab:

| Wasserwert | Sinnvoller Zeitraum |
|---|---|
| pH | 24 Stunden, weil er im Tagesverlauf schwankt |
| Temperatur | 24 Stunden oder 7 Tage |
| Alkalinität | 7 oder 30 Tage |
| Spurenelemente | 30 Tage oder ein Jahr |

:::note Ist die Linie flach, schau aufs Alter
Eine Linie, die sich nicht bewegt, kann einen stabilen Wert bedeuten oder eine Quelle, die nichts mehr meldet. Am Alter neben dem Wert erkennst du, was davon zutrifft.
:::

## Quellen vergleichen

Melden mehrere Quellen denselben Wasserwert, hält Cora sie getrennt und bildet keinen Mittelwert. Mit den Quellen-Chips schaust du dir eine nach der anderen an.

Weichen eine Sonde und ein von Hand eingetragener Test dauerhaft voneinander ab, muss meist die Sonde kalibriert werden.

Ein [ICP-Ergebnis](/help/mobile-icp-health) ist eine hilfreiche dritte Meinung, aber kein Schiedsrichter. Labore messen unterschiedlich, und Handhabung, Lagerung und Versand der Probe verändern das Ergebnis. Nimm einen einzelnen ICP als Hinweis und nicht als den wahren Wert. Zwei Tests, die übereinstimmen, sind viel mehr wert als einer.

## Festlegen, welcher Quelle ein Widget folgt

Soll ein Widget einer bestimmten Quelle folgen, stellst du das in den Einstellungen des Widgets ein. Wie das geht, steht unter **[Dein Dashboard bearbeiten](/help/mobile-dashboard-editing)**.

## Einen falschen Messwert ausschließen

Eine Sonde schlägt aus, ein Test wird falsch abgelesen, eine Probe stammt mitten aus dem Wasserwechsel. Ein einziger falscher Messwert verzerrt das Diagramm, die Durchschnitte und alles, was darauf aufbaut.

![Die Liste der Rohmesswerte](img/mobile-readings.webp "Jeder Messwert hinter der Linie, mit seiner Quelle und Zeit.")

Öffne die Messwertliste über das Symbol in der oberen Leiste und tippe auf den Messwert, den du ausschließen willst. Der Bildschirm sagt dir klar, was passiert: *aus Durchschnitten und Insights ausgeschlossen, bleibt aber in deinem Protokoll.* Gelöscht wird nichts, und du kannst den Messwert wiederherstellen.

:::warning Schließ falsche Messwerte aus, keine unbequemen
Das Ausschließen ist für Messwerte gedacht, von denen du weißt, dass sie ungültig sind. Ein Messwert, der dir nicht gefällt, an dem du aber keinen Fehler findest, gehört zu deinen Daten. Entfernst du ihn, wird jeder spätere Vergleich weniger ehrlich.
:::

## Sondenpflege festhalten

Trägst du hier eine Kalibrierung oder Reinigung ein, speichert Cora das Datum bei dieser Quelle. Weicht die Sonde später ab, siehst du gleich, wann sie zuletzt gepflegt wurde. Mehr dazu unter [Sonden](/help/mobile-probes).

## Einen Messwert von Hand eintragen

Trag ein, was dein Testkit anzeigt. Von Hand eingetragene Messwerte sind vollwertig. Sie bekommen eine eigene Quelle und einen Zeitstempel, erscheinen im Diagramm und fließen in Reef Buddy ein. Mit ihnen vergleicht Cora auch deine Geräte.

:::note Cora hakt nach, wenn ein Wert unplausibel wirkt
Liegt ein Wert weit weg von dem, was das Becken bisher gezeigt hat, fragt Cora vor dem Speichern nach. So fällt ein verrutschtes Komma auf oder ein Messwert, der beim falschen Wasserwert gelandet ist. Bestätigst du den Wert, wird er ganz normal gespeichert.
:::

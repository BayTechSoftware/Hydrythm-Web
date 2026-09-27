---
title: Einen Wasserwert genauer betrachten
description: Tippe auf ein beliebiges Widget für die vollständige Historie, jede Quelle, die ihn meldet, und wo du seinen Bereich änderst.
section: Cora Mobile
reviewed: 2026-09-09
order: 8
group: Your dashboard
---

Ein Widget zeigt dir eine Zahl. Darauf zu tippen zeigt dir die Geschichte hinter der Zahl.

## Was du bekommst

![Einen Wasserwert genauer betrachten](img/mobile-metric-detail.webp "Bereiche oben, dann die Quellen, die diesen Wasserwert melden, dann das Diagramm mit deinem schattierten Warnband.")

**Ein Historiendiagramm**, mit eigener Bereichsauswahl: **1h · 6h · 12h · 24h · 3d · 7d** und länger.

**Ein Quellenfilter.** Unter den Bereichen steht eine Reihe von Chips: **Alle**, plus einer pro Quelle, die diesen Wasserwert meldet, wie *Apex*, *Cora*, *Red Sea* oder *Manuell*. Wähle einen, um nur seine Messwerte zu sehen. So vergleichst du eine Sonde direkt gegen ein Testkit: Wechsle zwischen ihnen im selben Diagramm.

**Ein Link zum Dosierrechner**, für Wasserwerte, die du dosierst. Er nutzt das Beckenvolumen aus deinem [Beckenprofil](/help/mobile-tank-profile) und die Stärken aus [Dosierung](/help/mobile-dosing).

**Eine Vergleichsüberlagerung.** *Vergleichen mit* zeichnet einen zweiten Wasserwert in dasselbe Diagramm (Alkalinität gegen Calcium, pH gegen Temperatur), sodass ein vermuteter Zusammenhang sichtbar wird, statt nur erinnert zu werden.

**Zusammenfassende Statistiken** für das Fenster auf dem Bildschirm: **MIN**, **DURCHSCHN.** und **MAX**, als Zeile unter dem aktuellen Wert gezeigt.

**Dosierungsmarker** im Diagramm, sodass eine Bewegung mit dem verglichen werden kann, was du tatsächlich dosiert hast.

**Die Liste der Rohmesswerte**: jeder einzelne Messwert hinter der Linie, mit seiner Quelle und seinem Zeitstempel.

**Dein Warnband**, im Diagramm schattiert, sodass ein Messwert gegen seinen Bereich gelesen wird statt isoliert. Um den Bereich selbst zu ändern, halte das Widget auf dem Dashboard lange gedrückt. Siehe [Warnungen und Schwellenwerte](/help/mobile-alerts).

**Einen Messwert protokollieren** von Hand.

## Einen Bereich wählen

Der richtige Bereich hängt vom Rhythmus des Wasserwerts ab:

| Wasserwert | Nützliches Fenster |
|---|---|
| pH | 24 Stunden; es schwankt in einem Tageszyklus |
| Temperatur | 24 Stunden oder 7 Tage |
| Alkalinität | 7 oder 30 Tage |
| Spurenelemente | 30 Tage oder ein Jahr |

:::note Prüfe das Alter des Messwerts bei einem flachen Trend
Eine Linie, die sich nicht bewegt hat, kann einen stabilen Wasserwert oder eine Quelle bedeuten, die aufgehört hat zu melden. Das neben dem Wert angezeigte Alter unterscheidet die beiden.
:::

## Quellen vergleichen

Wenn mehr als eine Quelle einen Wasserwert meldet, behält Cora sie getrennt, statt sie zu mitteln. Nutze die Quellen-Chips, um jede nacheinander zu betrachten.

Ein anhaltender Versatz zwischen einer Sonde und einem von Hand protokollierten Test deutet meist darauf hin, dass die Sonde kalibriert werden muss.

Ein [ICP-Ergebnis](/help/mobile-icp-health) ist eine nützliche dritte Meinung, aber kein Schiedsrichter. Laboratorien unterscheiden sich voneinander, und die Handhabung, Lagerung und der Transport der Probe verändern alle das Ergebnis. Behandle einen einzelnen ICP als Hinweis, nicht als den wahren Wert; zwei übereinstimmende Tests sind weit mehr wert als einer.

## Wählen, welcher Quelle ein Widget vertraut

Wenn du willst, dass ein Widget einer bestimmten Quelle folgt, lege das in den Einstellungen des Widgets fest. Siehe **[Dein Dashboard bearbeiten](/help/mobile-dashboard-editing)**.

## Einen fehlerhaften Messwert ausschließen

Eine Sonde, die ausgeschlagen hat, ein falsch abgelesener Test, eine mitten im Wasserwechsel entnommene Probe: ein einzelner falscher Messwert verzerrt das Diagramm, die Durchschnitte und alles, das daraus schließt.

![Die Liste der Rohmesswerte](img/mobile-readings.webp "Jeder Messwert hinter der Linie, mit seiner Quelle und Zeit.")

Öffne die Messwertliste über das Symbol in der oberen Leiste, und tippe dann auf einen Messwert, um ihn auszuschließen. Der Bildschirm sagt es klar: *aus Durchschnitten und Insights ausgeschlossen, bleibt aber in deinem Protokoll.* Nichts wird gelöscht, und es kann wiederhergestellt werden.

:::warning Schließe einen falschen Messwert aus, nicht einen unerwünschten
Das Ausschließen ist für Messwerte, die du als ungültig erkannt hast. Ein Messwert, den du nicht magst, dem du aber nichts vorwerfen kannst, ist Daten, und ihn zu entfernen macht jeden späteren Vergleich weniger ehrlich.
:::

## Sondenpflege erfassen

Eine Kalibrierung oder Reinigung von hier aus zu protokollieren stempelt das Datum gegen diese Quelle, sodass ein späterer Widerspruch dagegen gelesen werden kann, wann die Sonde zuletzt versorgt wurde. Siehe [Sonden](/help/mobile-probes).

## Einen Messwert von Hand protokollieren

Trage ein, was dein Testkit sagt. Von Hand protokollierte Messwerte sind vollwertig: Sie bekommen ihre eigene Quelle und ihren Zeitstempel, sie erscheinen im Diagramm, sie speisen Reef Buddy, und sie sind das, wogegen Cora deine Ausrüstung vergleicht.

:::note Cora prüft Einträge, die unplausibel wirken
Wenn ein Wert weit von dem entfernt ist, was das Becken bisher gezeigt hat, wirst du gebeten, ihn zu bestätigen, bevor er gespeichert wird. Das fängt ein falsch gesetztes Komma oder einen gegen den falschen Wasserwert eingetragenen Messwert ab. Bestätige ihn, und der Messwert wird normal gespeichert.
:::

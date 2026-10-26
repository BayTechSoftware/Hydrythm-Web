---
title: Widget-Referenz
description: Jeder Widget-Typ auf dem Dashboard von Cora Mobile, von Wert, Anzeige, Diagramm, Status und Steckdose bis zu den Gerätekacheln, und wann du welchen nimmst.
section: Cora Mobile
reviewed: 2026-10-18
order: 9
group: Your dashboard
---

Ein Widget ist eine Kachel auf deinem Dashboard, und es zeigt eine Sache. Diese Seite geht jeden Typ durch und was du daran einstellen kannst.

Widgets fügst du im [Dashboard-Editor](/help/mobile-dashboard-editing) hinzu und ordnest sie dort an. Tippe dort auf ein Widget, um seine Einstellungen zu öffnen: **Typ** und **Wasserwert** bei einem Wasserwert, die Steckdose oder das Gerät bei den anderen, dann **Breite** und **Höhe** und **Zeitraum** bei einem Diagramm.

![Das Einstellungsfenster eines Widgets in Cora Mobile](img/mobile-widget-config.webp "Die untere Hälfte der Einstellungen eines Widgets: der Wasserwert, Breite, Höhe und Zeitraum, dann Entfernen und Fertig.")

## Die Widget-Typen {#the-widget-types}

| Typ | Zeigt |
|---|---|
| **Wert** | Den aktuellen Messwert, seine Einheit, sein Alter und seine Quelle |
| **Anzeige** | Einen Bogen mit deinem Bereich als Band und einem Knopf beim Wert |
| **Diagramm** | Einen Trend über einen Zeitraum, den du wählst |
| **Status** | Den Messwert als einfachen Text mit einem farbigen Punkt |
| **Steckdose** | Eine Steuerung mit drei Stellungen: Auto, Aus, Ein |
| **ReefBeat** | Ein Red Sea-Gerät, mit seiner eigenen Zusammenfassung |
| **Apex-Modul** | Ein eingebautes Apex-Modul, etwa ein Trident oder DŌS |
| **Jecod** | Eine Jecod-Pumpe, mit Modus und Intensität |

Alles nach Steckdose ist eine **Gerätekachel**. Jede gehört zu einem Stück Ausrüstung statt zu einem Wasserwert und zeigt, was dieses Gerät meldet. Cora Max hat außerdem eine Kachel **Szene**, die du auf Cora Max hinzufügst. Siehe [Das Cora Max-Dashboard bearbeiten](/help/max-dashboard-editing).


## Größe {#sizing}

**Breite** und **Höhe** können jeweils **1×** oder **2×** sein, ein Widget ist also eine oder zwei Zellen breit und eine oder zwei Zellen hoch. Ein Diagramm ist nie eine Zelle breit. Auf einem Dashboard mit drei Spalten belegt eine zwei Zellen breite Anzeige zwei Drittel der Zeile. Das ist meist eine gute Form für deinen wichtigsten Wasserwert.

## Was ein Wasserwert-Widget zeigt {#what-a-parameter-widget-shows}

Die Widgets Wert, Anzeige, Diagramm und Status zeigen alle einen gemessenen Wasserwert, und sie zeigen immer drei Dinge. Steckdosen- und Gerätekacheln zeigen ihren eigenen Zustand, weil hinter ihnen kein einzelner Messwert steht.

- **Den Wert**, in großer Schrift
- **Das Alter** (`now`, `1h`, `2d`), also wie lange es her ist, dass die Quelle den Wert zuletzt bestätigt hat. Bei einer Sonde ist das, wann ihr Gerät sich zuletzt gemeldet hat, ein gleichbleibender Messwert bleibt also frisch. Bei einem Testkit- oder ICP-Ergebnis ist es, wann du den Test gemacht hast. Mehr dazu unter [Dein Dashboard lesen](/help/mobile-dashboard#how-to-read-a-parameter-widget).
- **Die Quelle**, ein kleines Abzeichen, das sagt, woher die Zahl kommt

Ein Wasserwert-Widget hat keine eigene Einstellung für Bereich oder Quelle. Der Bereich kommt aus den Warnschwellen des Beckens (drück auf dem Dashboard lange auf das Widget) und die Quelle aus der [Parameterzuordnung](/help/mobile-probes). Tippe auf dem Dashboard auf das Widget, um seinen ganzen Verlauf, jede Quelle, die ihn meldet, und dein Warnband zu sehen.

## Wert {#value}

Das ist die reine Zahl. Sie zeigt den aktuellen Messwert, seine Einheit, wie alt er ist und woher er kommt.

Nimm ihn für Wasserwerte, bei denen du eher auf die Zahl schaust als auf den Trend, etwa Calcium, Magnesium oder Nitrat.

## Anzeige {#gauge}

Eine Anzeige ist ein Bogen, auf dem dein Warnbereich markiert ist, mit einem Knopf beim aktuellen Wert. Die Farbe des Knopfs sagt dir, wo du stehst: im Bereich, abdriftend oder außerhalb.

Nimm sie für die Wasserwerte, die du aktiv steuerst, etwa Alkalinität, pH, Salinität oder Temperatur.

:::note Mach Anzeigen mindestens zwei Spalten breit
In einer Spalte ist der Bogen zu klein, um ihn schnell abzulesen. Fehlt dir Platz, nimm ein Widget **Wert**.
:::

## Diagramm {#graph}

Ein Diagramm ist eine kleine Verlaufskurve über einen Zeitraum, den du wählst: 1h, 6h, 24h, 7d, 30d oder 1y. Es markiert Höchst- und Tiefstwert und beschriftet den aktuellen Wert.

Bei einem Wasserwert, den du testest (mit einem Trident oder einem Testkit), verbindet die Linie deine echten Tests. Gibt es im Zeitraum nur einen Test, kommt die Linie vom Test davor, und es gibt keinen Höchst- oder Tiefstwert. Gibt es im Zeitraum keinen Test oder nichts Früheres, mit dem sich ein einzelner Test verbinden ließe, zeigt die Kachel **Wird gesammelt…** statt einer Linie.

Nimm es für alles, was sich bewegt, etwa pH im Tagesverlauf, Temperatur in einer Hitzewelle oder Alkalinität zwischen Dosierungen.

Ein Diagramm ist immer **mindestens zwei Zellen breit**. Eine Verlaufskurve, die in eine Zelle gequetscht ist, sagt dir nichts, deshalb lässt der Editor das nicht zu.

:::note Wähl den Zeitraum, der zum Wasserwert passt
pH schwankt im Tagesrhythmus, 24 Stunden zeigen dir also das Muster. Alkalinität bewegt sich über Tage, 7 oder 30 Tage sagen dir also viel mehr.
:::

## Status {#status}

Das zeigt den Messwert als einfachen Text, mit einem farbigen Punkt für im Bereich, abdriftend oder außerhalb. Nimm es für einen Wasserwert, der keinen sinnvollen Bereich für eine Anzeige hat.

## Steckdose {#outlet}

Das ist ein Schalter mit drei Stellungen für eine Apex-Steckdose: **Auto**, **Aus** und **Ein**. Du wählst, welche Steckdose er steuert.

- **Auto** gibt die Steckdose an das zurück, was sie normalerweise steuert. Das kann ein Zeitplan sein, eine Regel oder der Controller, zu dem sie gehört.
- **Aus** und **Ein** sind manuelle Übersteuerungen. Sie bleiben, bis du sie zurückstellst.

:::warning Manuelle Übersteuerungen laufen nicht ab
Aus heißt aus, bis du es zurück auf Auto stellst. Schaltest du eine Rückförderpumpe aus, um im Becken zu arbeiten, stell sie danach zurück auf Auto. Cora tut das nicht für dich.
:::

## ReefBeat {#reefbeat}

Das ist eine Kachel für ein ganzes Stück Ausrüstung. Sie zeigt die eigene Zusammenfassung des Geräts statt eines einzelnen Wasserwerts, etwa Status und Nachfüllbehälter einer Nachfüllanlage, die Köpfe einer Dosierpumpe oder wie viele Tage ein Mattenroller noch hat. Du wählst, welches Gerät sie zeigt.

Welche Geräte eine Kachel haben können, hängt davon ab, was du verbunden hast. Siehe [Deine Ausrüstung verbinden](/help/mobile-connections).

## Dosierpumpen-Kacheln {#doser-tiles}

Eine Kachel für eine Dosierpumpe (ein Apex DŌS oder ein ReefDose) zeigt eine Zeile pro Kopf. Ein Kopfname wird nie unter eine lesbare Größe verkleinert. Auf einer hohen Kachel nimmt die Zeile zwei Zeilen ein, mit dem Namen in der ersten und dem, was übrig ist, in der zweiten, zum Beispiel *40d* und *2.8 L*. Auf einer niedrigen Kachel fällt die Detailzeile weg, und der Name bleibt lesbar.

Leg mit **Restmenge anzeigen als** fest, was zuerst kommt: **Tage** oder **Milliliter (mL)**. Ein ReefDose-Kopf ohne eigenen Namen wird als Gerätename, gefolgt von "Kopf" und seiner Nummer, angezeigt. Eine Jecod-Dosierpumpen-Kachel ist nur zum Lesen und zeigt den Tagesplan, weil Jecod nicht meldet, wie viel noch in der Flasche ist.

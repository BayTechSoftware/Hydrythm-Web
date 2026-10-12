---
title: Widget-Referenz
description: Alle Widget-Typen in Cora, von Wert, Anzeige, Diagramm, Status und Steckdose bis zu den Gerätekacheln, und wann du welchen nimmst.
section: Cora Mobile
reviewed: 2026-10-12
order: 7
group: Your dashboard
---

Ein Widget ist eine Kachel auf deinem Dashboard, die eine Sache zeigt. Hier findest du alle Typen und was du bei ihnen einstellen kannst.

Du fügst Widgets im **[Dashboard-Editor](/help/mobile-dashboard-editing)** hinzu und ordnest sie dort an. Tippst du dort auf ein Widget, öffnen sich seine Einstellungen.

![Ein Widget konfigurieren](img/mobile-widget-config.webp "Typ, Wasserwert, dann Breite und Höhe.")

## Die sechzehn Typen

| Typ | Zeigt |
|---|---|
| **Wert** | den aktuellen Messwert mit Einheit, Alter und Quelle |
| **Anzeige** | einen Bogen, auf dem dein Bereich eingezeichnet ist, mit einem Knopf beim aktuellen Wert |
| **Diagramm** | einen Verlauf über einen Zeitraum, den du wählst |
| **Status** | einen Zustand als Text, etwa läuft, ruht, geschlossen |
| **Steckdose** | einen Schalter mit drei Stellungen: Auto, Aus, Ein |
| **Szene** | eine Szene, die du mit einem Tipp startest. Du fügst sie auf dem Cora Max hinzu |
| **ReefBeat** | ein Red Sea-Gerät mit eigener Zusammenfassung |
| **Apex-Modul** | ein eingebautes Apex-Modul, etwa ein Trident oder DŌS |
| **Jecod** | eine Jecod-Pumpe mit Modus und Intensität |
| **Maxspect** *(Beta)* | eine Gyre mit beiden Motoren |
| **GHL** *(Beta)* | ein ProfiLux- oder Mitras-Controller mit eigener Zusammenfassung |
| **HYDROS** *(Beta)* | ein HYDROS-Controller mit eigener Zusammenfassung |
| **Radion** *(Beta)* | eine EcoTech Radion-Leuchte oder ein verknüpftes Radion-Netz |
| **VorTech** *(Beta)* | eine EcoTech VorTech-Pumpe mit Modus und Geschwindigkeit |
| **Versa** *(Beta)* | ein EcoTech Versa-Dosierer mit seinen Köpfen |
| **Kamera** *(Beta)* | eine Live-Ansicht einer deiner Kameras, bis zu drei Spalten breit und zwei Zeilen hoch |

Alles nach Szene sind **Gerätekacheln**. Sie gehören zu einem Gerät und nicht zu einem Wasserwert und zeigen, was dieses Gerät meldet.

:::note Beta-Kacheln
Maxspect, GHL, HYDROS, EcoTech (Radion, VorTech und Versa) und Kamera sind Beta-Anbindungen, die nur Beta-Nutzern offen stehen. Diese Kacheln siehst du erst, wenn du das Gerät hast. Siehe [Beta-Funktionen](/help/mobile-beta).
:::

## Größe

**Breite** und **Höhe** sind jeweils **1×** oder **2×**. Ein Widget ist also eine oder zwei Zellen breit und eine oder zwei Zellen hoch. Ein Diagramm ist nie nur eine Zelle breit. Auf einem Dashboard mit drei Spalten belegt eine zwei Zellen breite Anzeige zwei Drittel der Zeile. Für deinen wichtigsten Wasserwert passt diese Form meist am besten.

## Wert

Die reine Zahl: der aktuelle Messwert mit Einheit, wie alt er ist und woher er kommt.

Nimm ihn für Wasserwerte, bei denen dich die Zahl interessiert und weniger der Verlauf, etwa Calcium, Magnesium oder Nitrat.

Einstellbar sind Bezeichnung, Quelle und Größe.

## Anzeige

Ein Bogen, auf dem dein Zielbereich eingezeichnet ist, mit einem Knopf beim aktuellen Wert. An der Farbe des Knopfs siehst du, wo du stehst: im Bereich, auf dem Weg nach draußen oder außerhalb.

Nimm sie für die Wasserwerte, die du aktiv steuerst, etwa Alkalinität, pH, Salinität und Temperatur.

Einstellbar sind Bezeichnung, Quelle, Bereich (kommt aus den Zielwerten deines Beckens, außer du legst hier einen eigenen fest) und Größe.

:::note Gib Anzeigen mindestens zwei Spalten
In einer einzelnen Spalte ist der Bogen zu klein, um ihn schnell abzulesen. Ist wenig Platz, nimm lieber ein **Wert**-Widget.
:::

## Diagramm

Eine kleine Verlaufskurve über einen Zeitraum, den du wählst. Höchst- und Tiefstwert sind markiert, und der aktuelle Wert ist hervorgehoben.

Bei einem Wasserwert, den du testest (mit Trident oder Testkit), verbindet die Linie deine tatsächlichen Tests. Liegt im Zeitraum nur ein Test, kommt die Linie vom Test davor, und Höchst- und Tiefstwert werden nicht markiert. Gibt es im Zeitraum keinen Test oder keinen früheren Test, mit dem sich ein einzelner verbinden ließe, zeigt die Kachel **Wird gesammelt…** und keine Linie.

Nimm es für alles, was sich bewegt, etwa pH im Tagesverlauf, Temperatur während einer Hitzewelle oder Alkalinität zwischen den Dosierungen.

Einstellbar sind Bezeichnung, Quelle, **Zeitfenster** (1 Stunde, 6 Stunden, 24 Stunden, 7 Tage, 30 Tage, 1 Jahr) und Größe.

Ein Verlauf ist immer **mindestens zwei Zellen breit**. In einer einzelnen Zelle würde die Kurve nichts aussagen, deshalb lässt der Editor das nicht zu.

:::note Wähl den Zeitraum passend zum Rhythmus
pH schwankt im Tagesverlauf. In 24 Stunden siehst du also die typische Kurve. Alkalinität verändert sich über Tage. Da sagen dir 7 oder 30 Tage viel mehr als 24 Stunden.
:::

## Status

Ein Zustand als Text, für alles, was sich nicht in Zahlen ausdrücken lässt: läuft, ruht, offen, geschlossen, füttert.

Einstellbar sind Bezeichnung, Quelle und Größe.

## Steckdose

Ein Schalter mit drei Stellungen für eine Steckdose: **Auto**, **Aus**, **Ein**.

- **Auto** gibt die Steckdose an das zurück, was sie sonst steuert, also einen Zeitplan, eine Regel oder den Controller, zu dem sie gehört.
- **Aus** und **Ein** schalten sie von Hand. Das bleibt so, bis du es zurückstellst.

Einstellbar sind Bezeichnung, Steckdose und Größe.

:::warning Von Hand geschaltet bleibt geschaltet
Aus bleibt aus, bis du wieder auf Auto stellst. Schaltest du die Rückförderpumpe aus, um im Becken zu arbeiten, stell sie danach wieder auf Auto. Cora macht das nicht für dich.
:::

## ReefBeat

Eine Kachel für ein ganzes Gerät. Sie zeigt eine eigene Zusammenfassung und keinen einzelnen Wasserwert, etwa Status und Vorratsbehälter einer Nachfüllanlage, die Köpfe einer Dosiereinheit oder die verbleibenden Tage eines Mattenrollers.

Für welche Geräte es eine Kachel gibt, hängt davon ab, was du verbunden hast. Mehr dazu unter **[Deine Ausrüstung verbinden](/help/mobile-connections)**.

Einstellbar sind Bezeichnung, Gerät und Größe.

## Dosierer-Kacheln

Eine Kachel für einen Dosierer (ein Apex DŌS, ein ReefDose oder ein EcoTech Versa) zeigt eine Zeile pro Kopf. Ein Kopfname wird nie unter eine lesbare Größe geschrumpft. Auf einer hohen Kachel belegt die Zeile zwei Zeilen, mit dem Namen in der ersten und dem Rest in der zweiten, zum Beispiel *40d* und *2.8 L*. Auf einer niedrigen Kachel entfällt die Detailzeile, und der Name bleibt lesbar.

Mit **Restmenge anzeigen als** legst du fest, was zuerst kommt: **Tage** oder **Milliliter (mL)**. Ein ReefDose-Kopf ohne eigenen Namen wird als Gerätename gefolgt von "Kopf" und seiner Nummer gezeigt. Eine Jecod-Dosierer-Kachel ist schreibgeschützt und zeigt den Tagesplan, weil Jecod nicht meldet, wie viel noch in der Flasche ist.

## Was ein Wasserwert-Widget zeigt

Ein Widget für einen gemessenen Wasserwert (Wert, Anzeige, Diagramm und Status) zeigt immer drei Dinge. Steckdosen- und Gerätekacheln zeigen stattdessen ihren eigenen Zustand, denn hinter ihnen steht kein einzelner Messwert:

- **den Wert**, groß
- **das Alter** (`jetzt`, `1h`, `2d`), also wie alt der Messwert ist und nicht, wann der Bildschirm zuletzt aktualisiert wurde
- **die Quelle** als kleines Abzeichen, das zeigt, woher die Zahl kommt

Tippe auf ein Widget, dann siehst du die ganze Historie, jede Quelle, die den Wert meldet, und die gerade geltenden Schwellenwerte.

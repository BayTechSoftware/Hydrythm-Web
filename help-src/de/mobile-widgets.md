---
title: Widget-Referenz
description: Jeder Widget-Typ in Cora (Wert, Anzeige, Diagramm, Status, Steckdose und die Gerätekacheln) und wann du welchen nutzt.
section: Cora Mobile
reviewed: 2026-09-17
order: 7
group: Your dashboard
---

Ein Widget ist eine Kachel auf deinem Dashboard, die eine Sache zeigt. Diese Seite deckt jeden Typ ab und was du konfigurieren kannst.

Füge sie im **[Dashboard-Editor](/help/mobile-dashboard-editing)** hinzu und ordne sie an; tippe dort auf ein Widget, um seine Einstellungen zu öffnen.

![Ein Widget konfigurieren](img/mobile-widget-config.webp "Typ, Wasserwert, dann Breite und Höhe.")

## Die neun Typen

| Typ | Zeigt |
|---|---|
| **Wert** | Den aktuellen Messwert, seine Einheit, sein Alter und seine Quelle |
| **Anzeige** | Einen Bogen mit deinem Bereich darauf gebändert und einem Zeiger am Wert |
| **Diagramm** | Einen Trend über ein von dir gewähltes Fenster |
| **Status** | Einen Zustand als Text: läuft, ruht, geschlossen |
| **Steckdose** | Eine Dreiwege-Steuerung: Auto, Aus, Ein |
| **ReefBeat** | Ein Red Sea-Gerät, mit seiner eigenen Zusammenfassung |
| **Apex-Modul** | Ein eingebautes Apex-Modul, wie ein Trident oder DŌS |
| **Jecod** | Eine Jecod-Pumpe, mit ihrem Modus und ihrer Intensität |
| **Maxspect** *(Beta)* | Eine Gyre, mit beiden Motoren |

Die letzten vier sind **Geräte**-Kacheln: Sie sind an ein Stück Ausrüstung gebunden statt an einen Wasserwert, und jede zeigt, was dieses Gerät meldet.

## Größe

**Breite** und **Höhe** sind jeweils **1×** oder **2×**. Ein Diagramm ist nie eine Zelle breit.

## Wert

Die einfache Zahl. Aktueller Messwert, seine Einheit, wie alt er ist, und woher er kommt.

Nutze das für Wasserwerte, die du numerisch prüfst statt nach Trend: Calcium, Magnesium, Nitrat.

**Einstellungen:** Bezeichnung, Quelle, Größe.

## Anzeige

Ein Bogen mit deinem Zielbereich darauf gebändert und einem Zeiger am aktuellen Wert. Die Farbe des Zeigers sagt dir, wo du stehst: innerhalb des Bandes, abweichend, oder außerhalb.

Nutze das für die Wasserwerte, die du aktiv steuerst: Alkalinität, pH, Salinität, Temperatur.

**Einstellungen:** Bezeichnung, Quelle, Bereich (übernommen von deinen Beckenzielen, sofern du ihn hier nicht überschreibst), Größe.

:::note Stelle Anzeigen auf zwei Spalten oder mehr
Bei einer einzelnen Spalte ist der Bogen zu klein, um ihn auf einen Blick zu lesen; nutze statt dessen ein **Wert**-Widget, wenn der Platz begrenzt ist.
:::

## Diagramm

Eine Sparkline über ein von dir gewähltes Fenster, mit markiertem Höchst- und Tiefstwert, und dem aktuellen Wert hervorgehoben.

Bei einem Wasserwert, den du testest (per Trident oder mit einem Testkit), verbindet die Linie deine tatsächlichen Tests. Wenn das Fenster nur einen Test enthält, läuft die Linie vom Test davor herein, und es wird kein Höchst- oder Tiefstwert markiert. Ohne Test im Fenster, oder ohne etwas Früheres, mit dem ein einzelner Test verbunden werden könnte, zeigt die Kachel **Wird gesammelt…** statt einer Linie.

Nutze das für alles, was sich bewegt: pH über den Tag, Temperatur während einer Hitzewelle, Alkalinität zwischen Dosierungen.

**Einstellungen:** Bezeichnung, Quelle, **Zeitfenster** (1 Stunde, 6 Stunden, 24 Stunden, 7 Tage, 30 Tage, 1 Jahr), Größe.

Ein Trend ist immer **mindestens zwei Zellen breit**; eine in eine Zelle gepresste Sparkline sagt dir nichts, daher erstellt der Editor keine solche.

:::note Wähle das Fenster passend zum Rhythmus
pH schwankt in einem Tageszyklus, daher zeigen dir 24 Stunden die Form. Alkalinität bewegt sich über Tage, daher sagen dir 7 oder 30 mehr, als 24 es je könnte.
:::

## Status

Text statt einer Zahl, für Dinge, die ein Zustand sind. Läuft, ruht, offen, geschlossen, füttert.

**Einstellungen:** Bezeichnung, Quelle, Größe.

## Steckdose

Ein Dreiwege-Schalter für eine Steckdose: **Auto**, **Aus**, **Ein**.

- **Auto** gibt die Steckdose an das zurück, was sie normalerweise steuert: einen Zeitplan, eine Regel, oder den Controller, zu dem sie gehört.
- **Aus** und **Ein** sind manuelle Übersteuerungen, die bleiben, bis du sie zurückänderst.

**Einstellungen:** Bezeichnung, welche Steckdose, Größe.

:::warning Eine manuelle Übersteuerung läuft nicht ab
Aus bedeutet aus, bis du es zurück auf Auto stellst. Wenn du eine Rückförderpumpe ausschaltest, um im Becken zu arbeiten, stelle sie zurück auf Auto, wenn du fertig bist; Cora tut das nicht für dich.
:::

## ReefBeat

Eine Kachel für ein ganzes Ausrüstungsstück, die eine eigene Zusammenfassung zeigt statt eines einzelnen Wasserwerts: den Status und das Reservoir eines ATO, die Köpfe einer Dosiereinheit, die verbleibenden Tage eines Mattenrollers.

Welche Geräte eine Kachel anbieten, hängt davon ab, was du verbunden hast. Siehe **[Deine Ausrüstung verbinden](/help/mobile-connections)**.

**Einstellungen:** Bezeichnung, welches Gerät, Größe.

## Was ein Wasserwert-Widget zeigt

Bei einem Widget, das auf einem gemessenen Wasserwert basiert (Wert, Anzeige, Diagramm und Status), sind immer drei Dinge vorhanden. Steckdosen- und Gerätekacheln zeigen statt dessen ihren eigenen Zustand, weil kein einzelner Messwert hinter ihnen steht:

- **Der Wert**, groß
- **Das Alter** (`jetzt`, `1h`, `2d`): wie alt der Messwert ist, nicht wie kürzlich sich der Bildschirm aktualisiert hat
- **Die Quelle**: ein kleines Abzeichen, das sagt, woher die Zahl kommt

Tippe auf ein beliebiges Widget, um seine vollständige Historie zu öffnen, jede Quelle, die es meldet, und die aktuell geltenden Schwellenwerte.

## Größen

Widgets sind eine oder zwei Zellen breit und eine oder zwei Zellen hoch, außer einem **Trend**, der immer mindestens zwei breit ist. Auf einem dreispaltigen Dashboard nimmt eine zwei breite Anzeige zwei Drittel der Zeile ein, meist die richtige Form für deinen wichtigsten Wasserwert.

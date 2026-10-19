---
title: Dein Dashboard bearbeiten
description: Widgets auf deinem Handy-Dashboard hinzufügen, verschieben, in der Größe ändern und entfernen, die Spaltenzahl festlegen und ein Cora Max-Dashboard vom Handy aus bearbeiten.
section: Cora Mobile
reviewed: 2026-10-18
order: 8
group: Your dashboard
twin: max-dashboard-editing
---

Der Dashboard-Editor legt fest, welche Widgets auf dem Dashboard eines Beckens erscheinen und wie sie angeordnet sind. Jedes Becken hat sein eigenes Layout, und es folgt deinem Konto auf jedes Handy, auf dem du dich anmeldest.

## Den Editor öffnen {#opening-the-editor}

Scroll das Dashboard nach unten und tippe auf **Dashboard bearbeiten**, direkt unter den Widgets. Der Editor öffnet sich als **Dashboard bearbeiten**, mit dem Hinweis **Lange auf eine Kachel drücken, um sie zu verschieben. Tippen zum Konfigurieren.**

:::note Der Stift in der Beckenkopfzeile öffnet etwas anderes
Er öffnet **Becken bearbeiten**, das Beckenprofil mit Volumen, Besatz, Dosierung, Beleuchtung und Strömung. Darum geht es unter [Dein Beckenprofil](/help/mobile-tank-profile).
:::

![Der Bildschirm Dashboard bearbeiten in Cora Mobile](img/mobile-edit.webp "Oben die Spalten, dann jede Kachel mit ihrem Namen und Typ. Tippe auf ein rotes Kreuz, um sie zu entfernen.")

## Die Spaltenzahl festlegen {#setting-the-column-count}

Wähl oben im Editor neben **SPALTEN** **2**, **3** oder **4**. Das Raster wächst nach unten, wenn du Widgets hinzufügst, und das Dashboard scrollt.

| Spalten | Nimm sie, wenn |
|---|---|
| 2 | Du wenige Wasserwerte beobachtest und große Kacheln willst |
| 3 | Der Standard. Passt für die meisten Becken |
| 4 | Du eine dichte Ansicht willst oder ein großes Handy hast |

## Ein Widget hinzufügen {#adding-a-widget}

1. Tippe unter dem Raster auf **Kachel hinzufügen** oder auf eine leere Zelle.
2. Wähl unter **Kachel hinzufügen**, welche Art es ist. **Wasserwert** umfasst einen Wert, eine Anzeige, ein Diagramm oder einen Status für einen Wasserwert. **Steckdose** steuert eine Apex-Steckdose. Die anderen Zeilen sind für Ausrüstung, etwa **ReefBeat**, **Trident**, **DŌS** oder **Jecod**. Die meisten erscheinen nur, wenn das Becken diese Ausrüstung hat. **Licht**, **Strömungspumpe** und **Pumpe** listen alle Leuchten, Strömungspumpen und Pumpen des Beckens auf, egal von welcher Marke, und jede erscheint nur, wenn das Becken so ein Gerät hat. **ReefBeat** und **Jecod** behalten die übrigen Geräte, etwa eine ReefDose oder eine Jecod-Dosierpumpe.
3. Wähl den Wasserwert, die Steckdose oder das Gerät.
4. Bei einem Wasserwert wählst du den Typ. Die [Widget-Referenz](/help/mobile-widgets) beschreibt jeden.

Du siehst nur Wasserwerte, die das Becken hat. Ein Wasserwert ohne Quelle erscheint, sobald du Ausrüstung verbindest, die ihn meldet, oder einen Messwert von Hand einträgst.

Das Raster fasst bis zu 20 Zeilen. Ist es voll, sagt Cora **Dashboard ist voll: Entferne zuerst eine Kachel.** Ein Diagramm braucht zwei freie Zellen nebeneinander.

Entfernst du ein Gerät aus einem Becken, verschwinden seine Kacheln von selbst vom Dashboard, auf deinem Handy und auf jedem Cora Max dieses Beckens. Eine Kachel, deren Gerät weg ist, sagt **Dieses Gerät ist nicht mehr in diesem Becken** und öffnet nichts.

## Widgets anordnen {#arranging-widgets}

- Um ein Widget zu verschieben, halt es gedrückt und zieh es. Die anderen weichen aus.
- Um ein Widget zu entfernen, tippe auf das rote Kreuz in seiner Ecke oder tippe auf das Widget und dann auf **Entfernen**.
- Um die Einstellungen eines Widgets zu ändern, tippe darauf.

## Widget-Einstellungen {#widget-settings}

Tippe im Editor auf ein Widget, um seine Einstellungen zu öffnen. Je nach Widget kannst du festlegen:

| Einstellung | Gilt für |
|---|---|
| **Typ** | Wasserwert-Widgets: Wert, Anzeige, Diagramm oder Status |
| **Wasserwert** | Wasserwert-Widgets: welchen Wasserwert es zeigt |
| Die Steckdose oder das Gerät | Steckdosen- und Ausrüstungskacheln: welche oder welches sie zeigen |
| **Restmenge anzeigen als** | Dosierpumpen-Kacheln: **Tage** oder **Milliliter (mL)** |
| **Breite** | Jedes Widget: **1×** oder **2×**. Ein Diagramm ist immer mindestens 2 breit |
| **Höhe** | Jedes Widget: **1×** oder **2×** |
| **Zeitraum** | Diagramm: 1h, 6h, 24h, 7d, 30d oder 1y |

Tippe auf **Fertig**, um die Einstellungen zu behalten, oder auf **Entfernen**, um das Widget herauszunehmen.

Ein Widget hat keine eigene Beschriftung, Quelle oder einen eigenen Bereich. Sein Warnbereich kommt aus den Warnschwellen des Beckens: Drück auf dem Dashboard lange auf das Widget oder siehe [Warnungen und Schwellenwerte](/help/mobile-alerts). Welcher Quelle ein Wasserwert folgt, legst du pro Becken unter [Parameterzuordnung](/help/mobile-probes) fest.

## Speichern {#saving}

Tippe auf **Speichern**, um das Layout zu behalten. Um deine Änderungen zu verwerfen, tippe auf das Schließen-Symbol. Hast du etwas geändert, fragt Cora **Änderungen verwerfen?** Tippe auf **Verwerfen** oder auf **Weiter bearbeiten**, um zurückzugehen.

Der Handy-Editor hat kein Rückgängig und keine gespeicherten Designs. Messwerte, Verlauf und Tagebucheinträge werden getrennt vom Layout gespeichert, beim Bearbeiten eines Dashboards kann davon also nie etwas verloren gehen.

## Das Cora Max-Dashboard bearbeiten {#editing-the-cora-max-dashboard}

Das Cora Max-Dashboard bearbeitest du getrennt, über **Geräte →** dein Cora Max **→ Dashboard-Layout**, auf der Karte des Beckens. Es nutzt ein festes Raster, das nicht scrollt, und auf Cora Max kommt nichts an, bis du auf **Speichern & veröffentlichen** tippst.

Dieser Editor hat drei Extras, die das Handy-Dashboard nicht hat:

- **Meine Dashboards** bewahrt bis zu 30 gespeicherte Designs in deinem Konto auf. Jedes Cora Max im Konto kann eins laden. Kacheln, die das Ziel nicht füllen kann, stehen vor dem Laden unter **Zurückgelassen:**.
- **Vorlagen** öffnet **Dashboard-Vorlagen**: **Übersicht**, **Ausrüstung** und **Wasserwerte**. Es ist in jedem Abo offen und nutzt keine KI.
- **Mit KI gestalten**, mit einem kostenpflichtigen Abo oder während der Testphase, schlägt ein ganzes Layout vor, ausgehend von dem, was das Becken meldet und verknüpft hat. Du kannst 5 Entwürfe pro Becken und Tag erstellen.

Wie jedes davon funktioniert, steht unter [Das Cora Max-Dashboard bearbeiten](/help/max-dashboard-editing).

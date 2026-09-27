---
title: Das Cora Max Dashboard bearbeiten
description: Wähle ein Raster, füge Widgets hinzu, und speichere Layouts für das Cora Max Display.
section: Cora Max
reviewed: 2026-09-09
order: 4
group: Your dashboard
---

Das Cora Max Dashboard nutzt ein **festes Raster**. Jede Kachel muss auf einen Bildschirm passen; das Display scrollt nicht. Das ist der Hauptunterschied zum Handy-Dashboard.

Öffne den Editor über das **Beckenmenü**: tippe auf den Beckennamen in der oberen Leiste, dann **Dashboard-Layout**. Er befindet sich auch unter **Einstellungen → Beckeneinstellungen → [dein Becken] → Dashboard-Layout**.

![Der Dashboard-Editor auf Cora Max](img/max-dashboard-editor.webp "Rastergrößen oben, dann die Kacheln. Jede zeigt ihren Typ und ihre Quelle, keinen Messwert; das ist ein Layout-Bildschirm. Nichts wird geschrieben, bis du auf Speichern tippst.")

:::tip Du kannst es auch von deinem Handy aus bearbeiten
**Geräte → dein Cora Max → Dashboard bearbeiten** erstellt dasselbe Layout von Cora Mobile aus. Das geht schneller, als Kacheln von Hand an einer Wand anzuordnen, und das Ergebnis erscheint sofort auf dem Bildschirm.
:::

## Ein Raster wählen

Wähle zuerst die Dichte, denn sie zu ändern ordnet alles neu an.

| Raster | Kacheln | Fühlt sich an wie |
|---|---|---|
| 2×2, 3×2, 3×3 | 4–9 | Groß. Quer durch den Raum lesbar. |
| 4×4, 5×3, 6×4 | 16–24 | Die übliche Wahl für ein vollständiges System. |
| 6×5, 8×4, 8×5 | 30–40 | Dicht. Ein ganzer Riffraum auf einmal. |
| 9×5, 10×5 | 45–50 | Sehr dicht. Am besten auf den größten Bildschirmen. |
| **Auto** | bis zu 32 | Cora wählt eine Form passend zur Anzahl der hinzugefügten Kacheln. |

Ein festes Raster fasst so viele Kacheln, wie es Zellen hat, bis zu 50 bei 10×5. **Auto** ist die einzige Option mit eigener Obergrenze: Sie stoppt bei 32 Kacheln, weil der Text darüber hinaus zu klein wird, um aus der Entfernung lesbar zu sein.

:::note Beginne mit Auto, wenn du unsicher bist
Füge die Kacheln hinzu, die du willst, und lass das Raster auf **Auto**; Cora wählt eine passende Form. Wenn dir das Ergebnis gefällt, lege es danach auf diese feste Form fest.
:::

:::warning Das Ändern des Rasters kann Kacheln verwerfen, aber nur, wenn kein Platz ist
Kacheln werden in die neue Form neu angeordnet, statt nach Position verworfen zu werden: Alles, das schon in einer gültigen Zelle ist, bleibt, und der Rest wird der Reihe nach wieder eingepackt. Kacheln gehen nur verloren, wenn das neue Raster **weniger Zellen hat, als du Kacheln hast**, und Cora sagt dir, wie viele weg sind. Von 10×5 (50 Zellen) auf 3×3 (9) zu wechseln verliert die meisten davon.
:::

## Hinzufügen und Anordnen

Der Editor nennt oben die drei Gesten: **auf eine Kachel tippen, um sie zu bearbeiten**, **lange drücken, um sie zu verschieben**, und **✕, um sie zu entfernen**. Kacheln können eine oder zwei Zellen breit und eine oder zwei Zellen hoch sein.

**Steckdosen & Fütterung** fügt deine steuerbaren Steckdosen und Fütterungszyklen in einem Schritt hinzu, statt eine Kachel nach der anderen. **Alles löschen** leert das Raster, damit du neu beginnen kannst.

Die neun Kachel-Typen (Wert, Anzeige, Diagramm, Status, Steckdose, ReefBeat, Apex-Modul, Jecod und Maxspect *(Beta)*) sind in der **[Widget-Referenz](/help/mobile-widgets)** beschrieben.

## Für die Entfernung gestalten

Ein Wandbildschirm wird von weiter weg gelesen als ein Handy, und meist auf einen Blick statt mit Aufmerksamkeit.

- **Gib deinen Hauptwasserwerten Zwei-mal-zwei.** Alkalinität, Temperatur, pH: die Dinge, die du ohne Hinlaufen lesen willst.
- **Setze Steuerungen an die Ränder.** Steckdosenkacheln sind die, nach denen du greifst; sie sind an den Seiten leichter zu treffen.
- **Gruppiere nach Thema, nicht nach Typ.** Alles zur Dosierung zusammen, alles zur Strömung zusammen. Du überblickst eine Wand nach Bereich.
- **Lass die Spurenelemente klein.** Spurenelemente und andere langsame Zahlen sind Referenz, keine Überwachung; eine Eins-mal-eins-Wert-Kachel reicht völlig.

## Layouts speichern

Nichts, was du im Editor tust, wirkt sich aus, bis du auf **Speichern** tippst. Ohne zu speichern zu verlassen verwirft die Änderungen.

**Meine Dashboards** behält Layouts, zu denen du zurückkehren willst, sodass du zwischen ihnen wechseln kannst, statt sie neu aufzubauen. Ein dichtes Alltagslayout und ein Layout mit großen Kacheln für die Arbeit am Becken passen zu unterschiedlichen Momenten, und zwischen ihnen zu wechseln braucht nur einen Tipp.

## Mehrere Becken

Jedes Becken hat sein eigenes Layout. Bearbeite sie getrennt, ein Becken nach dem anderen, über die eigenen Einstellungen dieses Beckens.

---
title: Das Cora Max-Dashboard bearbeiten
description: Raster wählen, Widgets hinzufügen und Layouts für den Cora Max-Bildschirm speichern.
section: Cora Max
reviewed: 2026-09-09
order: 4
group: Your dashboard
---

Das Cora Max-Dashboard hat ein **festes Raster**. Alle Kacheln müssen auf einen Bildschirm passen, denn der Bildschirm scrollt nicht. Das ist der größte Unterschied zum Dashboard auf dem Handy.

Den Editor öffnest du über das **Beckenmenü**: Tippe in der oberen Leiste auf den Beckennamen und dann auf **Dashboard-Layout**. Du findest ihn auch unter **Einstellungen → Beckeneinstellungen → [dein Becken] → Dashboard-Layout**.

![Der Dashboard-Editor auf Cora Max](img/max-dashboard-editor.webp "Oben die Rastergrößen, darunter die Kacheln. Jede Kachel zeigt ihren Typ und ihre Quelle, aber keinen Messwert, denn hier geht es nur um das Layout. Gespeichert wird erst, wenn du auf Speichern tippst.")

:::tip Du kannst das Dashboard auch auf dem Handy bearbeiten
Unter **Geräte → dein Cora Max → Dashboard bearbeiten** baust du in Cora Mobile dasselbe Layout. Das geht schneller, als Kacheln an der Wand von Hand anzuordnen, und das Ergebnis erscheint sofort auf dem Bildschirm.
:::

## Ein Raster wählen

Wähle zuerst die Dichte. Änderst du sie später, ordnen sich alle Kacheln neu an.

| Raster | Kacheln | So wirkt es |
|---|---|---|
| 2×2, 3×2, 3×3 | 4–9 | Groß. Quer durch den Raum lesbar. |
| 4×4, 5×3, 6×4 | 16–24 | Die übliche Wahl für ein komplettes System. |
| 6×5, 8×4, 8×5 | 30–40 | Dicht. Ein ganzer Riffraum auf einen Blick. |
| 9×5, 10×5 | 45–50 | Sehr dicht. Am besten auf den größten Bildschirmen. |
| **Auto** | bis zu 32 | Cora wählt eine Form, die zur Zahl deiner Kacheln passt. |

Ein festes Raster fasst so viele Kacheln, wie es Zellen hat, bei 10×5 also bis zu 50. Nur **Auto** hat eine eigene Obergrenze von 32 Kacheln. Bei mehr Kacheln wird die Schrift zu klein, um sie aus der Entfernung zu lesen.

:::note Im Zweifel mit Auto anfangen
Füge die Kacheln hinzu, die du haben willst, und lass das Raster auf **Auto**. Cora wählt dann eine passende Form. Gefällt dir das Ergebnis, kannst du diese Form danach fest einstellen.
:::

:::warning Beim Rasterwechsel gehen Kacheln nur verloren, wenn der Platz fehlt
Cora verwirft beim Wechsel keine Kacheln wegen ihrer Position, sondern ordnet sie in die neue Form ein. Was schon in einer gültigen Zelle liegt, bleibt dort. Der Rest wird der Reihe nach wieder einsortiert. Verloren gehen Kacheln nur, wenn das neue Raster **weniger Zellen hat, als du Kacheln hast**. Cora sagt dir dann, wie viele weggefallen sind. Wechselst du von 10×5 (50 Zellen) auf 3×3 (9), sind die meisten weg.
:::

## Hinzufügen und anordnen

Oben im Editor stehen die drei Gesten: **Tippe auf eine Kachel, um sie zu bearbeiten**, **drück lange, um sie zu verschieben**, und tippe auf **✕, um sie zu entfernen**. Eine Kachel kann eine oder zwei Zellen breit und eine oder zwei Zellen hoch sein.

Mit **Steckdosen & Füttern** fügst du alle schaltbaren Steckdosen und Fütterungszyklen auf einmal hinzu. **Alles löschen** leert das Raster, damit du neu anfangen kannst.

Die neun Kacheltypen (Wert, Anzeige, Diagramm, Status, Steckdose, ReefBeat, Apex-Modul, Jecod und Maxspect *(Beta)*) findest du in der **[Widget-Übersicht](/help/mobile-widgets)**.

## Für den Blick aus der Entfernung

Einen Wandbildschirm liest du aus größerer Entfernung als ein Handy, und meist nur im Vorbeigehen.

- **Gib deinen wichtigsten Wasserwerten zwei mal zwei Zellen.** Alkalinität, Temperatur, pH: alles, was du ablesen willst, ohne hinzugehen.
- **Leg die Steuerung an den Rand.** Nach Steckdosenkacheln greifst du am häufigsten, und an den Seiten triffst du sie leichter.
- **Sortiere nach Thema.** Alles zur Dosierung zusammen, alles zur Strömung zusammen. An der Wand suchst du nach Bereichen.
- **Lass die Spurenelemente klein.** Spurenelemente und andere Werte, die sich langsam ändern, schaust du nur gelegentlich nach. Dafür reicht eine Wert-Kachel mit einer Zelle.

## Layouts speichern

Was du im Editor änderst, wirkt erst, wenn du auf **Speichern** tippst. Verlässt du den Editor ohne zu speichern, sind die Änderungen weg.

In **Meine Dashboards** legst du Layouts ab, zu denen du zurückkehren willst. So wechselst du zwischen ihnen, ohne sie neu zu bauen. Ein dichtes Layout für den Alltag und eines mit großen Kacheln für die Arbeit am Becken passen zu verschiedenen Situationen, und der Wechsel kostet nur einen Tipp.

## Mehrere Becken

Jedes Becken hat sein eigenes Layout. Du bearbeitest sie nacheinander, jeweils in den Einstellungen des Beckens.

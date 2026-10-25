---
title: Das Cora Max-Dashboard bearbeiten
description: Kacheln auf dem Cora Max-Dashboard hinzufügen, verschieben und entfernen, ein Raster wählen, Vorlagen oder Mit KI gestalten nutzen und Layouts speichern.
section: Cora Max
reviewed: 2026-10-18
order: 4
group: Your dashboard
twin: mobile-dashboard-editing
---

Diese Seite zeigt, wie du die Kacheln auf einem Cora Max-Dashboard anordnest. Es nutzt ein **festes Raster**: Der Bildschirm scrollt nicht, also muss jede Kachel auf einen Bildschirm passen. Das ist der größte Unterschied zum Dashboard auf dem Handy.

Öffne den Editor über das **Beckenmenü**: Tippe in der oberen Leiste auf den Beckennamen und dann auf **Dashboard-Layout**. Du findest ihn auch unter **Einstellungen → [dein Becken] → Dashboard-Layout**.

![Der Dashboard-Editor auf Cora Max](img/max-dashboard-editor.webp "Oben die Rastergrößen, darunter die Kacheln. Das ist ein Layout-Bildschirm, deshalb zeigt jede Kachel ihren Typ und ihre Quelle statt eines Messwerts. Gespeichert wird erst, wenn du auf Speichern drückst.")

:::tip Du kannst es auch auf dem Handy bearbeiten
Öffne in Cora Mobile den Tab **Geräte**, tippe auf dein Cora Max und dann auf der Karte des Beckens auf **Dashboard-Layout**. Das geht schneller, als Kacheln an einem Wandbildschirm von Hand anzuordnen, und das Ergebnis erscheint auf Cora Max, sobald du speicherst.
:::

## Ein Raster wählen {#choosing-a-grid}

Wähl zuerst die Rastergröße. Änderst du sie später, verschieben sich alle Kacheln.

| Raster | Kacheln | So wirkt es |
|---|---|---|
| 2×2, 3×2, 3×3 | 4–9 | Groß. Quer durch den Raum gut lesbar. |
| 4×4, 5×3, 6×4 | 16–24 | Die übliche Wahl für ein komplettes System. |
| 6×5, 8×4, 8×5 | 30–40 | Dicht. Ein ganzer Riffraum auf einem Bildschirm. |
| 9×5, 10×5 | 45–50 | Sehr dicht. Am besten auf den größten Bildschirmen. |
| **Auto** | bis zu 32 | Cora wählt eine Form, die zur Zahl deiner Kacheln passt. |

Ein festes Raster fasst so viele Kacheln, wie es Zellen hat, bis zu 50 bei 10×5. **Auto** hat eine eigene Grenze von 32 Kacheln. Darüber wird die Schrift zu klein, um sie aus der Entfernung zu lesen.

:::note Unsicher? Fang mit Auto an
Füg die Kacheln hinzu, die du willst, und lass das Raster auf **Auto**. Cora wählt eine Form, die passt. Gefällt sie dir, kannst du danach auf diese feste Form wechseln.
:::

:::warning Beim Rasterwechsel fallen Kacheln nur weg, wenn sie nicht passen
Wenn du das Raster wechselst, wirft Cora keine Kacheln wegen ihrer Position weg. Kacheln, die noch eine gültige Zelle haben, bleiben, wo sie sind, und der Rest wird der Reihe nach wieder einsortiert. Kacheln verlierst du nur, wenn das neue Raster **weniger Zellen hat, als du Kacheln hast**, und Cora sagt dir, wie viele weggefallen sind. Von 10×5 (50 Zellen) auf 3×3 (9) verlierst du die meisten.
:::

## Kacheln hinzufügen und anordnen {#adding-and-arranging}

1. Tippe auf eine leere Zelle (sie zeigt ein **+**), um **Widget hinzufügen** zu öffnen.
2. Wähl unter **TYP** die Art der Kachel und dann, was sie zeigt (einen Messwert, eine Steckdose, ein Gerät oder eine Szene).
3. Wähl unter **GRÖSSE**, wie groß sie ist. Eine Kachel kann eine oder zwei Zellen breit und eine oder zwei Zellen hoch sein. Ein Diagramm hat außerdem einen **ZEITRAUM**. Eine Dosierpumpen-Kachel hat **Restmenge anzeigen als**, in **Tage** oder **Milliliter (mL)**.
4. Tippe auf **Hinzufügen**.

Die Gesten stehen oben im Editor: **Tippen zum Bearbeiten**, **Lange drücken zum Verschieben** und **✕ zum Entfernen**. **Alles löschen** leert das Raster, damit du neu anfangen kannst.

Die Kacheltypen sind Wert, Anzeige, Diagramm, Status, Steckdose, Szene, ReefBeat, Apex-Modul und Jecod. **Licht**, **Strömungspumpe** und **Pumpe** listen alle Leuchten, Strömungspumpen und Pumpen des Beckens auf, egal von welcher Marke, und jede erscheint nur, wenn das Becken so ein Gerät hat. Du findest die Kacheln in der [Widget-Referenz](/help/mobile-widgets). Die Kachel **Szene** gibt es nur auf Cora Max. Sie startet eine [Szene](/help/max-automation) mit einem Tippen.


## Steckdosen & Füttern {#outlets-feed}

**Steckdosen & Füttern** im Editor wählt, welche Steckdosen und Fütterungszyklen in **Steuerung** erscheinen, der Schublade, die du unten auf dem Dashboard nach oben wischst. Kacheln fügt es nicht hinzu. Wählst du keine aus, listet Steuerung alle auf. Um eine Steckdose auf das Raster selbst zu legen, füg eine Kachel **Steckdose** hinzu. Mehr dazu unter [Steckdosen und Steuerung](/help/max-controls).

Entfernst du ein Gerät aus einem Becken, verschwinden seine Kacheln von selbst vom Dashboard, auf deinem Handy und auf jedem Cora Max dieses Beckens. Eine Kachel, deren Gerät weg ist, sagt **Dieses Gerät ist nicht mehr in diesem Becken** und öffnet nichts.

## Vorlagen {#templates}

**Vorlagen** steht oben im Editor, neben **Meine Dashboards** und **Mit KI gestalten**. Es ist in jedem Abo offen und nutzt nie KI, funktioniert also auch ohne Teilen von Daten mit der KI.

Es öffnet **Dashboard-Vorlagen**, ein paar fertige Layouts, gebaut aus dem, was dieses Becken meldet und verknüpft hat:

- **Übersicht**: wenige große Kacheln, mit den wichtigsten Wasserwerten als Anzeigen und deinen Hauptgeräten
- **Ausrüstung**: zuerst eine Kachel pro Gerät, dann Steckdosen und die wichtigsten Wasserwerte
- **Wasserwerte**: Diagramme und Messwerte zuerst, Geräte und Steckdosen zuletzt

Jede zeigt eine Vorschau und wie viele Kacheln sie auf welchem Raster hat. Tippe auf **Verwenden**. Cora fragt zuerst **Dashboard ersetzen?** Tippe auf **Aktuelles zuerst sichern**, wenn du dein jetziges Layout behalten willst, oder auf **Ersetzen**. Gespeichert wird erst, wenn du auf **Speichern** drückst.

## Mit KI gestalten {#design-with-ai}

Der Editor hat eine Taste **Mit KI gestalten**. Sie funktioniert mit einem kostenpflichtigen Abo und während der Testphase. Cora schlägt ein ganzes Layout vor, ausgehend von dem, was dieses Becken meldet und verknüpft hat, und zeigt, wie viele Kacheln es hat und auf welchem Raster. Tippe auf **Verwenden**, um es in den Editor zu übernehmen, oder auf **Erneut versuchen** für einen anderen Vorschlag. Du kannst 5 Entwürfe pro Becken und Tag erstellen.

Ein KI-Entwurf ersetzt, was gerade auf diesem Dashboard ist. Gespeichert wird erst, wenn du auf **Speichern** drückst, und du kannst dein aktuelles Layout vorher behalten, indem du es unter **Meine Dashboards** speicherst. Im kostenlosen Abo führt **Mit KI gestalten** zu den Abos. Außerdem muss das Teilen von Daten mit der KI in Cora Mobile eingeschaltet sein. Mehr dazu unter [Cora fragen](/help/mobile-assistant).

## Für den Blick aus der Entfernung gestalten {#designing-for-distance}

Einen Wandbildschirm liest man aus größerer Entfernung als ein Handy, und meist nur mit einem kurzen Blick.

- Gib deinen wichtigsten Wasserwerten zwei mal zwei Zellen. Alkalinität, Temperatur und pH willst du ablesen, ohne hinzugehen.
- Leg Steuerungen an den Rand. Nach Steckdosen-Kacheln greifst du, und an den Seiten triffst du sie leichter.
- Gruppier Kacheln nach Thema. Halt alles zur Dosierung zusammen und alles zur Strömung zusammen, denn eine Wand überfliegst du nach Bereichen.
- Lass Spurenelemente klein. Sie und andere Werte, die sich langsam ändern, sind zum Nachschauen da, eine Wert-Kachel mit einer Zelle reicht also.

## Layouts speichern und wiederverwenden {#saving-layouts}

Was du im Editor tust, wirkt erst, wenn du auf **Speichern** drückst. Verlässt du ihn mit ungespeicherten Änderungen, fragt Cora zuerst **Änderungen verwerfen?**

**Meine Dashboards** bewahrt Designs auf, zu denen du zurückkehren willst. Sie sind in deinem Konto gespeichert, nicht auf diesem Bildschirm, deshalb kann jedes Cora Max in deinem Konto sie laden, für ein anderes Becken oder für einen Ersatzbildschirm.

- **Dieses Design speichern** speichert, was im Editor ist. Du kannst bis zu 30 behalten.
- **Laden** holt ein gespeichertes Design in den Editor. Designs, die auf dem Handy gespeichert wurden, sind mit **Telefon** markiert.
- Vor dem Laden sagt dir Cora, wie viele Kacheln mitkommen. Was nicht mitkommen kann, etwa ein Messwert, den dieses Becken nicht meldet, oder ein Gerät, das nicht zu diesem Becken gehört, steht unter **Zurückgelassen:** mit dem Grund.

Du könntest zum Beispiel ein dichtes Layout für den Alltag behalten und eins mit großen Kacheln für die Arbeit am Becken.

## Mehrere Becken {#multiple-tanks}

Jedes Becken hat sein eigenes Layout. Wechsle zu diesem Becken und öffne **Dashboard-Layout** über sein Beckenmenü, oder nutze **Einstellungen → [dieses Becken] → Dashboard-Layout**.

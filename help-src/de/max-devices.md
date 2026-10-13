---
title: Geräte und Gerätezustand
description: Die Ausrüstung sehen und umbenennen, die Cora Max abfragt, festlegen, welches Cora Max jedes Becken abfragt, ein Becken reparieren, dessen Messwerte stehen geblieben sind, und ein Cora Max vom Handy aus verwalten.
section: Cora Max
reviewed: 2026-10-13
order: 7
group: Equipment
twin: mobile-devices
---

**Einstellungen → Geräte** auf Cora Max listet die Ausrüstung auf, die es sehen kann, und wie es jedem Gerät geht. Das Gerätesymbol in der oberen Leiste öffnet dieselbe Liste, gefiltert auf das Becken auf dem Bildschirm.

## Die Geräteliste {#the-device-list}

![Die Geräteliste auf Cora Max, nach Becken gefiltert und nach Marke gruppiert](img/max-devices.webp "Nach Becken filtern, dann jedes Gerät nach Marke gruppiert, mit einer einzeiligen Zusammenfassung und seinem Becken.")

Cora Max sieht dieselbe Ausrüstung wie dein Handy, weil beide dasselbe Konto lesen.

Mit den Filter-Chips oben zeigst du **Alle Becken** oder nur eins. Die Geräte sind nach Marke gruppiert. Jeder Eintrag hat einen Statuspunkt (grau, wenn Cora es noch nicht weiß, grün, wenn es funktioniert, orange bei einer Warnung oder einem Fehler, rot, wenn es offline ist), eine einzeilige Zusammenfassung dessen, was das Gerät hat (*21 Steckdosen · 4 Fütterungen*, *19 Tests übrig*), das Becken, zu dem es gehört, und wann es **Zuletzt gesehen** wurde. Beta-Geräte tragen einen Chip **Beta**.

Tippe auf ein Gerät, um seine Seite zu öffnen. Jede Geräteseite beginnt mit einem Bereich **Status**. Was jede Seite kann, steht unter [Ausrüstung mit Cora Max steuern](/help/max-device-control).

Steht in der Liste **Einige Geräte werden noch geladen: Diese Liste ist möglicherweise unvollständig.**, gib ihr einen Moment.

:::note Beta
**Beta.** EcoTech-Leuchten, -Pumpen und -Dosierer, Inkbird-Raumluftmonitore und Kameras sind in der Beta und nur für Beta-Nutzer offen. Wenn du kein Beta-Nutzer bist, siehst du sie nicht unter **Gerät hinzufügen**. Für Beta-Zugang wende dich an den [Support](/support.html). Mehr dazu unter [Beta-Funktionen](/help/mobile-beta).
:::

### Ein Gerät umbenennen {#renaming-a-device}

Tippe auf den Stift in der Zeile eines Geräts oder auf seiner Seite und gib den neuen Namen ein. Lass den Namen leer, um zum eigenen Namen des Geräts zurückzukehren. Der Name wird mit deinem Handy geteilt und ändert sich dort also auch.

### Geräte hinzufügen und entfernen {#adding-and-removing-devices}

Geräte fügst du auf dem Handy hinzu, weist sie dort zu und entfernst sie dort. Cora Max zeigt und steuert sie. Gibt es noch keine Geräte, steht auf diesem Bildschirm **Füge Geräte in der Cora-App hinzu.** Mehr dazu unter [Geräte hinzufügen, bearbeiten und entfernen](/help/mobile-devices).

## Primäres Cora Max: welches Gerät mit deiner Ausrüstung spricht {#primary-cora-max}

Das **Primäre Cora Max** ist das Cora Max (oder ein anderes Cora-Gerät), das den Controller und die übrige Ausrüstung eines Beckens für das ganze Konto abfragt. Jedes Becken braucht dafür nur ein Gerät. Jeder andere Bildschirm zeigt, was es liest.

Um es zu sehen oder zu ändern, öffne **Einstellungen → [dein Becken] → Primäres Cora Max**. Du hast zwei Möglichkeiten.

- **Jedes aktive (automatisch)** heißt, dass sich alle Cora-Geräte, die online sind und die Ausrüstung dieses Beckens erreichen, die Arbeit teilen, und der neueste Schreibvorgang gewinnt. Nimm das, außer du hast einen Grund, ein Gerät festzulegen.
- Leg ein Gerät fest, damit nur dieses Gerät die Ausrüstung abfragt. Geht es offline, übernimmt kein anderes Cora Max. Dann liest nur noch Cora Mobile die Ausrüstung, wenn es im selben WLAN geöffnet ist, bis du ein anderes Gerät festlegst oder zurück auf **Jedes aktive (automatisch)** stellst.

Du legst das einmal für das Becken fest, und es gilt für jeden Cora-Bildschirm. Du kannst es an jedem Cora Max ändern, das das Becken zeigt, oder in Cora Mobile (**Als primäres Cora Max festlegen** auf der Seite des Cora Max). Mehr dazu unter [Mehr als ein Cora-Gerät](/help/mobile-multi-device).

:::note Primäres Cora Max und Antwortgerät sind zwei getrennte Einstellungen
Primäres Cora Max entscheidet, welches Gerät **deine Ausrüstung abfragt**. Das **Antwortgerät** in Cora Mobile entscheidet, welches **auf "Hey Cora" antwortet**. Hast du mehr als ein Cora Max, kannst du beides getrennt festlegen. Mehr dazu unter [Mit Cora sprechen](/help/max-voice).
:::

## Wenn die Messwerte eines Beckens stehen bleiben {#if-a-tanks-readings-stop}

Bleiben die Messwerte eines Beckens stehen, während ein anderes Becken auf demselben Bildschirm weiter aktualisiert wird, fang hier an.

1. Öffne **Einstellungen → [dieses Becken] → Primäres Cora Max**. Prüf, ob ein Gerät zugewiesen und online ist.
2. Zeigt ein anderes Cora Max für dieses Becken in seiner oberen Leiste **Haupt-Cora offline**, hat das primäre seine Verbindung verloren. Was die Statusanzeige bedeutet, steht unter [Der Cora Max-Startbildschirm](/help/max-tour#what-the-status-pill-means).
3. **Einstellungen → Cora Max-Einstellungen → Netzwerk & Updates → Geräteabfrage** zeigt, wie oft dieses Cora Max deine Geräte abfragt. Hier kannst du es nur ansehen. Eingestellt wird es in Cora Mobile.
4. Prüf den Bereich **Status** unter **Einstellungen → Cora Max-Einstellungen**. Er zeigt für jedes Becken den Abfragestatus, die letzte Abfrage und den letzten Schreibvorgang in die Cloud, ohne etwas zu ändern.

Hilft das nicht, schau in die [Problembehebung](/help/troubleshooting).

## Ein Cora Max vom Handy aus verwalten {#managing-a-cora-max-from-your-phone}

Öffne auf dem Handy den Tab **Geräte** und tippe auf das Cora Max. Die obere Karte zeigt seine Variante, seine Firmware und wann es zuletzt gesehen wurde. Dort kannst du es umbenennen, und wenn es eine neue Version gibt, tippst du auf **Auf v… aktualisieren**, um sie gleich zu installieren. Die Karte **Wiederherstellungs-PIN** sitzt direkt darunter.

![Die Seite eines Cora Max in Cora Mobile, mit Kindersicherung, Geräteabfrage, Zeitzone und Zugewiesene Becken](img/max-from-phone.webp "Die eigenen Einstellungen eines Cora Max auf deinem Handy: Kindersicherung, Geräteabfrage und Zeitzone, dann seine Becken.")

Diese Einstellungen gelten nur für **diesen einen Bildschirm**, genau als hättest du sie an der Wand geändert:

| Bereich | Einstellungen |
|---|---|
| **Anzeige** | **Helligkeit**, **Dimmen nach** |
| **Ton & Sprache** | **Warnton** schaltet den Warnton auf diesem Bildschirm ein oder aus, und **Warnlautstärke** legt fest, wie laut er ist. Warnungen erscheinen weiter auf dem Bildschirm, und Warnverlauf und Push-Benachrichtigungen ändern sich nicht |
| **Kindersicherung** | **Kindersicherung** sperrt den Touchscreen dieses Bildschirms und verhindert, dass er per Sprache Ausrüstung schaltet |
| **Netzwerk & Updates** | **Geräteabfrage** (wie oft er deine Ausrüstung abfragt) und **Zeitzone** (für die Nachtdimmung und das Update-Fenster) |

Unter **Becken** hat jedes Becken, das dieses Cora Max zeigt, eine Karte mit **Dashboard-Layout**, **Becken bearbeiten** und seinem abfragenden Gerät. **Becken hinzufügen** und das Symbol zum Entfernen ändern, welche Becken es zeigt, und diese Änderungen gelten für das ganze Konto. Du kannst sie nur auf dem Handy machen. Die Schritte stehen unter [Cora Max einrichten](/help/max-setup#changing-which-tanks-it-shows). Welches Gerät das Primäre Cora Max für ein Becken ist, kannst du auf dem Handy oder auf Cora Max ändern.

Unter **Zurücksetzen** schickt **Display zurücksetzen** den Bildschirm zurück zu seinem Kopplungsbildschirm. Er bleibt in deinem WLAN, du kannst ihn also wieder über Bluetooth koppeln, und deine Beckendaten bleiben erhalten. **Gerät entfernen** nimmt ihn aus deinem Konto. Deine Beckenmesswerte bleiben erhalten, und du kannst ihn später wieder koppeln.

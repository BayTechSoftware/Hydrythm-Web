---
title: Geräte hinzufügen, bearbeiten und entfernen
description: So fügst du Geräte zu Cora hinzu, ordnest sie einem Becken zu, benennst sie um und entfernst sie sauber.
section: Cora Mobile
reviewed: 2026-09-27
order: 9
group: Equipment
---

Im Tab **Geräte** steht alles, was du verbunden hast, nach Marke gruppiert. Jede Gruppe lässt sich zuklappen. So behältst du auch in einem Technikraum voller Geräte den Überblick.

![Der Tab Geräte](img/mobile-devices.webp "Ausrüstung ist nach Marke gruppiert. Jede Gruppe klappt sich zusammen.")

## Geräte hinzufügen

Unter der Liste stehen drei Schaltflächen für unterschiedliche Aufgaben:

| Schaltfläche | Fügt hinzu |
|---|---|
| **Gerät hinzufügen** | ein Cora Max. Findet Geräte, die schon in deinem WLAN sind, oder Geräte in der Nähe per Bluetooth. Findet die Suche nichts, gibt es auf diesem Bildschirm **IP-Adresse manuell eingeben**. |
| **Pumpe im Netzwerk suchen** | Jecod-Pumpen, die sich im lokalen Netzwerk selbst melden |
| **AquaWiz hinzufügen** | einen AquaWiz-Controller über dein AquaWiz-Konto |

![Ein Cora Max hinzufügen](img/mobile-add-device.webp "Gerät hinzufügen sucht in WLAN und Bluetooth nach einem Cora Max.")

Andere Geräte, also Neptune Apex und Red Sea ReefBeat, verbindest du über das Becken und nicht über diese Liste. Mehr dazu unter [Deine Ausrüstung verbinden](/help/mobile-connections).

Fügst du Ausrüstung wie einen Heizer, eine Pumpe oder einen Abschäumer hinzu, hilft dir eine **Autovervollständigung** bei Marke und Modell. Fang an zu tippen, und Cora macht Vorschläge aus einer großen, geprüften Liste von Herstellern. Steht deine Marke nicht drin, tipp sie trotzdem ein. Cora übernimmt, was du schreibst.

:::note Cora und dein Handy brauchen dasselbe Netzwerk
Geräte, die Cora lokal findet, müssen beim Hinzufügen im selben Netzwerk sein wie dein Handy. **Auch nach der Einrichtung erreichst du sie nur über dieses Netzwerk** (oder per Bluetooth, bei Geräten, die das nutzen). Die Ausnahme ist ein Cora-Gerät vor Ort, das sie für dich erreicht.

Ein Gerät, das zu Hause einwandfrei Werte liefert, kann unterwegs also ältere Werte zeigen, außer ein Cora Max vor Ort fragt es ab. Das liegt daran, von wo aus das Gerät erreichbar ist, und ist kein Fehler.
:::

## Ein Gerät einem Becken zuordnen

Die meisten Geräte gehören zu genau einem Becken. Erst dadurch erscheinen ihre Messwerte auf dem Dashboard dieses Beckens.

**Cora Max ist die Ausnahme.** Es kann bis zu vier Becken zugeordnet werden und wechselt auf dem Bildschirm zwischen ihnen. Mehr dazu unter [Mehr als ein Cora-Gerät](/help/mobile-multi-device).

Öffne das Gerät und wähl **Becken**. Hast du mehrere Systeme, ist das die wichtigste Einstellung. Ein Heizer, der dem falschen Becken zugeordnet ist, meldet seine Werte tadellos, nur eben an der falschen Stelle.

:::warning Erst das Becken zuordnen, dann den Messwerten trauen
Ein Gerät ohne Becken meldet trotzdem Werte, aber sie landen nirgends. Taucht ein gerade hinzugefügtes Gerät auf keinem Dashboard auf, prüf das zuerst.
:::

## Umbenennen

Öffne das Gerät und ändere seinen Namen. Nimm den Namen, den du im Alltag benutzt, etwa "Rückförderung", "Gyre links" oder "Heizer Technikbecken". Der Name steht auf Widgets, in Warnungen und in allem, was du Cora fragst. Ein Name, mit dem du etwas anfangen kannst, macht also alles Weitere klarer.

Der neue Name gilt nur in Cora. In der App des Herstellers bleibt der alte Name.

## Prüfen, ob ein Gerät in Ordnung ist

Jede Zeile zeigt den aktuellen Zustand des Geräts. Gut ist eine aktuelle Aktualisierungszeit ohne Warnung.

| Was du siehst | Was es bedeutet |
|---|---|
| eine aktuelle Aktualisierungszeit | alles normal |
| "Vor 3 Std. aktualisiert" bei einem Gerät, das nur alle paar Stunden meldet | in Ordnung |
| "Konnte nicht erreicht werden…" | ein Netzwerkproblem, oder das Gerät ist aus |
| "…hat die Anmeldung abgelehnt" | Das Herstellerkonto muss neu verbunden werden. Öffne das Gerät und melde dich erneut an |
| gar nichts | Das Gerät hat noch nie etwas gemeldet. Prüf die Zuordnung zum Becken und die Verbindung |

## Ein Gerät entfernen

Öffne das Gerät und wähl **Entfernen**. Cora fragt nach und sagt dir genau, was entfernt wird.

**Deine Messwerte bleiben erhalten.** Nach dem Entfernen sammelt Cora keine neuen Daten mehr von dem Gerät. Die bisherige Historie bleibt beim Becken, und jedes Widget, das auf das Gerät zeigt, behält seine alten Messwerte.

Du verlierst die Live-Verbindung. War das Gerät über ein Herstellerkonto verbunden, ist auch die gespeicherte Anmeldung weg. Fügst du es wieder hinzu, musst du dich neu anmelden.

:::tip Ein lautes Gerät beruhigen, ohne es zu entfernen
Funktioniert ein Gerät richtig, meldet sich aber zu oft, pass seine Schwellenwerte oder Benachrichtigungen an. Wie das geht, steht unter **[Warnungen und Schwellenwerte](/help/mobile-alerts)**. Verbindung und Daten bleiben, und trotzdem ist Ruhe.
:::

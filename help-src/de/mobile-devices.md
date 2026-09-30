---
title: Geräte hinzufügen, bearbeiten und entfernen
description: So fügst du Geräte zu Cora hinzu, ordnest sie einem Becken zu und entfernst sie sauber, alles an einer Stelle.
section: Cora Mobile
reviewed: 2026-09-30
order: 9
group: Equipment
---

Füg jedes Gerät im Tab **Geräte** hinzu, bearbeite, ordne und entferne es dort, nach Marke gruppiert. Jede Gruppe lässt sich zuklappen. So behältst du auch in einem Technikraum voller Geräte den Überblick.

![Der Tab Geräte](img/mobile-devices.webp "Ausrüstung ist nach Marke gruppiert. Jede Gruppe klappt sich zusammen.")

## Geräte hinzufügen

Tippe auf **Gerät hinzufügen** und wähl die Marke: **Cora**, **Neptune Apex**, **Red Sea**, **Jecod**, **Maxspect**, **GHL** *(Beta)*, **HYDROS** *(Beta)* oder **AquaWiz**. Jede öffnet genau das, was sie braucht, um deine Ausrüstung zu finden: einen Netzwerk-Scan, eine IP-Adresse, eine Anmeldung oder einen Geräteschlüssel. Was jede Marke dafür braucht, steht unter [Deine Ausrüstung verbinden](/help/mobile-connections).

**Cora** ist der Weg, ein neues Cora Max zu koppeln. Findet die Suche Geräte, die schon in deinem WLAN sind, erscheinen sie hier, ebenso Geräte in der Nähe per Bluetooth. Findet sie nichts, gibt es auf demselben Bildschirm **IP-Adresse manuell eingeben**.

Fügst du Ausrüstung wie einen Heizer, eine Pumpe oder einen Abschäumer hinzu, hilft dir eine Autovervollständigung bei Marke und Modell. Fang an zu tippen, und Cora macht Vorschläge aus einer großen, geprüften Liste von Herstellern. Steht deine Marke nicht drin, tipp sie trotzdem ein. Cora übernimmt, was du schreibst.

:::note Cora und dein Handy brauchen dasselbe Netzwerk
Geräte, die Cora lokal findet, müssen beim Hinzufügen im selben Netzwerk sein wie dein Handy. **Auch nach der Einrichtung erreichst du sie nur über dieses Netzwerk** (oder per Bluetooth, bei Geräten, die das nutzen), außer ein Cora-Gerät vor Ort erreicht sie für dich.

Ein Gerät, das zu Hause einwandfrei Werte liefert, kann unterwegs also ältere Werte zeigen, außer ein Cora Max vor Ort fragt es ab. Das liegt daran, von wo aus das Gerät erreichbar ist, und ist kein Fehler.
:::

## Die Seite eines Geräts

Öffne ein beliebiges Gerät aus der Liste. Zuerst kommen seine Steuerungen, danach drei Bereiche, die bei jeder Marke gleich funktionieren.

- **Becken** zeigt, welchem Becken (oder welchen Becken) es zugeordnet ist. Tippe auf **Ändern**, um es neu zuzuordnen.
- **Verbindung** ist die Stelle, an der du seine IP-Adresse, Anmeldung oder seinen Geräteschlüssel bearbeitest.
- **Gerät entfernen**, ganz unten.

Cora Max, Neptune Apex und GHL können mehr als ein Becken bedienen, deshalb ist ihre Beckenauswahl eine Checkliste. Cora Max lässt sich bis zu vier Becken zuordnen. Mehr dazu unter [Mehr als ein Cora-Gerät](/help/mobile-multi-device). Alles andere, auch HYDROS, bedient jeweils ein Becken: Wählst du ein anderes, wandert das Gerät dorthin und wird beim alten Becken entfernt.

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
| "Wartet auf Cora Max" | ein gerade hinzugefügter GHL-Controller: Er erscheint, sobald ein Cora Max in seinem Netzwerk ihn ausgelesen hat |
| gar nichts | Das Gerät hat noch nie etwas gemeldet. Prüf die Zuordnung zum Becken und die Verbindung |

## Ein Gerät entfernen

Öffne das Gerät und tippe auf **Gerät entfernen**. Cora fragt nach: *"{name} wird aus Cora entfernt. Das Gerät selbst wird dabei nicht zurückgesetzt oder verändert."*

**Deine Messwerte bleiben erhalten.** Nach dem Entfernen sammelt Cora keine neuen Daten mehr von dem Gerät. Die bisherige Historie bleibt beim Becken, und jedes Widget, das auf das Gerät zeigt, behält seine alten Messwerte.

Du verlierst die Live-Verbindung. War das Gerät über ein Herstellerkonto verbunden, ist auch die gespeicherte Anmeldung weg. Fügst du es wieder hinzu, musst du dich neu anmelden.

:::tip Ein lautes Gerät beruhigen, ohne es zu entfernen
Funktioniert ein Gerät richtig, meldet sich aber zu oft, pass seine Schwellenwerte oder Benachrichtigungen an. Wie das geht, steht unter **[Warnungen und Schwellenwerte](/help/mobile-alerts)**. Verbindung und Daten bleiben, und trotzdem ist Ruhe.
:::

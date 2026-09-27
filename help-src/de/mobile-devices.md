---
title: Geräte hinzufügen, bearbeiten und entfernen
description: So fügst du Ausrüstung zu Cora hinzu, weist sie einem Becken zu, benennst sie um und entfernst sie sauber.
section: Cora Mobile
reviewed: 2026-09-27
order: 9
group: Equipment
---

Der Tab **Geräte** ist alles, was du verbunden hast, nach Marke gruppiert. Jede Gruppe klappt sich zusammen, sodass ein Riffraum voller Ausrüstung übersichtlich bleibt.

![Der Tab Geräte](img/mobile-devices.webp "Ausrüstung ist nach Marke gruppiert. Jede Gruppe klappt sich zusammen.")

## Ausrüstung hinzufügen

Unter der Liste stehen drei Schaltflächen, und sie erledigen unterschiedliche Aufgaben:

| Schaltfläche | Fügt hinzu |
|---|---|
| **Gerät hinzufügen** | Ein Cora Max. Findet Geräte, die schon in deinem WLAN sind, oder nahe gelegene über Bluetooth. **IP-Adresse manuell eingeben** befindet sich innerhalb dieses Bildschirms, falls die Suche es nicht findet. |
| **Pumpe im Netzwerk suchen** | Jecod-Pumpen, die sich selbst im lokalen Netzwerk bekannt geben |
| **AquaWiz hinzufügen** | Einen AquaWiz-Controller, über dein AquaWiz-Konto |

![Ein Cora Max hinzufügen](img/mobile-add-device.webp "Gerät hinzufügen sucht in WLAN und Bluetooth nach einem Cora Max.")

Andere Ausrüstung (Neptune Apex und Red Sea ReefBeat) wird über das Becken verbunden, nicht über diese Liste. Siehe [Deine Ausrüstung verbinden](/help/mobile-connections).

Beim Hinzufügen von Ausrüstung wie einem Heizer, einer Pumpe oder einem Abschäumer wird eine **Autovervollständigung** für Marke und Modell angeboten: Fang an zu tippen, und Cora schlägt aus einer großen, quellengeprüften Liste von Ausrüstungsmarken vor. Wenn deine nicht aufgeführt ist, tippe sie trotzdem ein; Cora behält, was du eintippst.

:::note Cora und dein Handy brauchen dasselbe Netzwerk
Lokal gefundene Ausrüstung muss beim Hinzufügen im selben Netzwerk wie dein Handy sein. **Nach der Einrichtung ist sie weiterhin nur über dieses Netzwerk erreichbar** (oder über Bluetooth, für Geräte, die das nutzen), sofern nicht ein Cora-Gerät vor Ort sie für dich erreichen kann.

Ausrüstung, die zu Hause korrekt lesbar ist, kann daher ältere Werte zeigen, während du weg bist, sofern nicht ein Cora Max vor Ort sie abfragen kann. Das spiegelt wider, von wo aus die Ausrüstung erreichbar ist, und ist kein Fehler.
:::

## Ein Gerät einem Becken zuweisen

Die meiste Ausrüstung gehört zu genau einem Becken, und das ist es, was ihre Messwerte auf dem Dashboard dieses Beckens erscheinen lässt.

**Cora Max ist die Ausnahme**: Es kann bis zu vier Becken zugewiesen werden und wechselt auf dem Bildschirm zwischen ihnen. Siehe [Mehr als ein Cora-Gerät](/help/mobile-multi-device).

Öffne das Gerät und wähle **Becken**. Wenn du mehr als ein System betreibst, ist das die wichtigste Einstellung: Ein Heizer, der dem falschen Becken zugewiesen ist, meldet einwandfrei an den falschen Ort.

:::warning Weise das Becken zu, bevor du dich auf die Messwerte verlässt
Ein Gerät ohne Becken meldet trotzdem, aber seine Zahlen haben nirgendwo, wo sie landen. Wenn ein gerade hinzugefügtes Gerät nicht auf einem Dashboard erscheint, prüfe das zuerst.
:::

## Umbenennen

Öffne das Gerät und bearbeite seinen Namen. Nutze den Namen, den du im Alltag dafür verwendest: "Rückförderung", "Gyre links", "Technikbecken-Heizer". Der Name erscheint auf Widgets, in Warnungen und in allem, was du Cora fragst, daher macht ein Name, der für dich Bedeutung hat, alles Nachfolgende klarer.

Das Umbenennen ist lokal in Cora. Es ändert nicht den Namen in der eigenen App des Herstellers.

## Prüfen, ob ein Gerät gesund ist

Jede Zeile zeigt ihren aktuellen Zustand. Was du sehen willst, ist eine aktuelle Aktualisierungszeit und keine Warnung.

| Was du siehst | Was es bedeutet |
|---|---|
| Eine aktuelle Aktualisierungszeit | Funktioniert normal |
| "Vor 3 Std. aktualisiert" bei etwas, das stündlich meldet | In Ordnung |
| "Konnte nicht erreicht werden…" | Ein Netzwerkproblem, oder das Gerät ist aus |
| "…hat die Anmeldung abgelehnt" | Das Konto des Herstellers muss neu verbunden werden; öffne das Gerät und melde dich erneut an |
| Gar nichts | Es hat noch nie gemeldet; prüfe die Beckenzuweisung und die Verbindung |

## Ein Gerät entfernen

Öffne das Gerät und wähle **Entfernen**. Du wirst um Bestätigung gebeten und erfährst genau, was entfernt wird.

**Deine Messwerte bleiben erhalten.** Das Entfernen eines Geräts stoppt, dass Cora neue Daten davon sammelt; die bereits erfasste Historie bleibt beim Becken, und jedes Widget, das darauf verweist, behält seine bisherigen Messwerte.

Was du verlierst, ist die Live-Verbindung und, wo das Gerät über ein Herstellerkonto verbunden war, die gespeicherte Anmeldung. Es wieder hinzuzufügen bedeutet, sich erneut anzumelden.

:::tip Ein lautes Gerät beruhigen, ohne es zu entfernen
Wenn ein Gerät korrekt funktioniert, aber zu oft warnt, passe seine Schwellenwerte oder Benachrichtigungseinstellungen an; siehe **[Warnungen und Schwellenwerte](/help/mobile-alerts)**. Das behält die Verbindung und die Daten, während es den Lärm stoppt.
:::

---
title: Ausrüstung planen
description: Einen Zeitplan für eine Jecod-Pumpe im Editor bauen, von oder auf andere Pumpen kopieren, speichern, teilen und prüfen, ob die Pumpe ihn übernommen hat.
section: Cora Mobile
reviewed: 2026-11-03
order: 14
group: Equipment
---

Auf dieser Seite gibst du einer Jecod-Pumpe einen **Zeitplan**: eine Folge von Zeiträumen mit jeweils eigener Intensität, die sich jeden Tag wiederholt. Öffne ihn über **Geräte** → auf die Pumpe tippen.

Leuchten und Pumpen anderer Marken haben ihre Zeitpläne auf ihren eigenen Seiten: ReefDose von Red Sea unter [Deine Ausrüstung steuern](/help/mobile-device-control#red-sea).

![Eine Jecod-Pumpenseite in Cora Mobile mit gewähltem Zeitplan](img/mobile-schedules.webp "Oben Zeitplan gewählt, dann die Futterpause und der Tagesgraph.")

## Manuell oder Zeitplan {#same-all-day-or-schedule}

Eine Pumpe läuft in einem von zwei Modi. Wähl einen mit dem Schalter auf ihrer Seite. Der laufende ist mit *· läuft* markiert, und die Seite öffnet sich auf ihm.

- **Manuell** läuft die ganze Zeit mit einer Intensität.
- **Zeitplan** folgt einer Folge von Zeiträumen.

Cora schickt deine Wahl direkt an die Pumpe, wenn dein Handy in ihrem Netzwerk ist. Ist es das nicht, läuft sie über das Cora Max am Becken. Eine Bluetooth-Pumpe muss in Reichweite sein. Bis sie es ist, ändert deine Wahl nur, was du auf dem Bildschirm siehst.

Eine Futterpause nimmt die Pumpe eine Weile aus ihrem Zeitplan, und auf dem Handy kommt der Zeitplan nur zurück, solange die Seite der Pumpe offen bleibt. Siehe [Futterpause](/help/mobile-device-control#jecod-feeding).

## Der Zeitplan-Editor

Jeder Zeitplan-Bildschirm hat dieselben drei Teile.

Oben ist der Tagesgraph. Er zeigt den ganzen Tag von 0 bis 24 Uhr, und jeder Zeitraum ist ein Block, dessen Höhe seine Intensität ist. So prüfst du am schnellsten, ob ein Programm das tut, was du denkst.

Unter dem Graphen steht die Liste der Zeiträume. Jeder Zeitraum zeigt seine Uhrzeiten, seinen Modus und seine Intensität, zum Beispiel *Zufällig, 00:00–03:00, Freq 50 %, 40 %*. Hier fügst du Zeiträume hinzu, bearbeitest und entfernst sie.

Jede Änderung an einem Zeitplan läuft über den Editor. **Ändern** öffnet ihn mit dem Tag der Pumpe, und ebenso ein Tipp auf einen Zeitraum oder auf **Zum Zeitplan hinzufügen** auf der Seite der Pumpe: Der Editor öffnet sich mit diesem Zeitraum oder einem neuen, bereit zum Ändern. Im Editor änderst du einen Zeitraum und tippst auf **Speichern**, oder du entfernst ihn mit **Abschnitt löschen**. **Rückgängig** geht einen Schritt zurück. Das ⋮-Menü hat **Zeitplan speichern als…**, **Gespeicherte Zeitpläne…** und **Kopieren von…**.

Nichts wird an die Pumpe gesendet, bis du auf **Auf Pumpe speichern** tippst. Cora schreibt dann den ganzen Tag auf einmal. Klappt das nicht, sagt der Editor warum und behält deine Änderungen. Schließt du den Editor vor dem Speichern, fragt Cora zuerst *Diese Änderungen verwerfen?*


:::warning Auf Pumpe speichern schreibt den Zeitplan aufs Gerät
Wenn du auf **Auf Pumpe speichern** tippst, schickt Cora das Programm an die Ausrüstung, und die Ausrüstung führt es nach ihrer eigenen Uhr aus. Es läuft weiter, ob Cora sie erreichen kann oder nicht.
:::

## Ein Programm zwischen Pumpen kopieren {#copying-a-program-between-pumps}

Hast du mehrere Pumpen, die sich gleich verhalten sollen, bau ein Programm und kopier es. Du kannst in beide Richtungen kopieren, und nichts wird gesendet, bis du auf **Auf Pumpe speichern** tippst.

- **Kopieren von…** (im ⋮-Menü des Zeitplans und in dem des Editors) übernimmt den Zeitplan einer anderen Strömungspumpe an einem deiner Becken. Jeder Zeitraum bekommt den ähnlichsten Modus, den diese Pumpe hat, die Geschwindigkeiten bleiben in dem Bereich, den sie fahren kann, und **Was sich an dieser Pumpe ändert** listet jede Änderung auf. **In den Editor laden** legt die Kopie in den Editor dieser Pumpe, wo du sie anpassen und dann auf **Auf Pumpe speichern** tippen kannst. Eine Pumpe, deren Zeitplan Cora noch nicht gelesen hat, ist ausgegraut, und der Grund steht dabei.
- **Zeitplan kopieren nach…** gibt den Tag dieser Pumpe an andere Pumpen an jedem deiner Becken weiter, jede als *Becken · Pumpe* aufgeführt. Hake die Pumpen an und tippe auf **Prüfen**. Noch wird nichts gesendet. **Kopien prüfen** listet jede Pumpe mit ihrem Zustand, **Nicht gespeichert**, **Auf Pumpe gespeichert** oder **Fehlgeschlagen** mit dem Grund, und wie viele Änderungen sie bekommt. **Editor öffnen** öffnet den eigenen Editor dieser Pumpe mit dem kopierten Tag, mit einem eigenen **Auf Pumpe speichern**, das ihn nur an diese Pumpe sendet. Schlägt ein Speichern fehl, bleibt der Entwurf erhalten, damit du es noch einmal versuchen kannst. Verlässt du die Seite, solange einige Pumpen nicht gespeichert sind, fragt Cora zuerst *Nicht gespeicherte Kopien verwerfen?*

## Einen Zeitplan behalten und teilen

Hast du einen Zeitplan, der dir gefällt, musst du ihn nicht noch einmal bauen.

- **Zeitplan speichern als…** behält ihn unter einem Namen. **Gespeicherte Zeitpläne…** holt ihn später zurück: **In den Editor laden** öffnet ihn im Editor, und **Auf Pumpe speichern** sendet ihn.
- **Diesen Zeitplan teilen** macht daraus einen kurzen Code. **Zeitplan-Code einfügen…** lädt einen Code, den dir jemand geschickt hat, in den Editor, und nichts wird gesendet, bis du auf **Auf Pumpe speichern** tippst. Das ist eine Funktion von Cora Mobile. Der Code enthält nur den Zeitplan. Er gibt niemandem Zugang zu deinem Konto.

## Außerhalb des Netzwerks der Pumpe

Ist dein Handy nicht im Netzwerk der Pumpe, geht Cora Mobile über das Cora Max am Becken. Ein paar Dinge funktionieren dann anders.

- **Manuell** und **Zeitplan** schalten die Pumpe über dieses Cora Max um.
- Ein Zeitplan, den du auf die Pumpe speicherst, kommt nur durch, wenn dieses Cora Max die Pumpe in der letzten Stunde erreicht hat. Hat es das nicht, sagt dir der Zeitplan das, und du kannst ihn von dort, wo du bist, nicht ändern.
- **Zeitplan kopieren nach…**, **Zeitplan speichern als…**, **Gespeicherte Zeitpläne…**, **Diesen Zeitplan teilen** und **Zeitplan-Code einfügen…** brauchen dein Handy im Netzwerk der Pumpe. Bis dahin sind sie ausgegraut, und das Menü sagt dir, warum.

Ohne Cora Max am Becken kannst du eine Pumpe nur ändern, solange dein Handy in ihrem Netzwerk ist. Mehr dazu unter [Deine Ausrüstung verbinden](/help/mobile-connections#local-only).

Eine Bluetooth-Pumpe erreichst du nur von einem Handy in ihrer Nähe. Stell dich in Reichweite, um sie zu schalten, ihren Zeitplan zu ändern oder einen dieser Menüpunkte zu nutzen.

## Ein Programm anwenden

Du kannst einer Pumpe einen gespeicherten Zeitplan in einem Schritt geben, ohne die Zeiträume neu zu bauen. Öffne die Pumpe, tippe oben auf **Mehr** und wähl **Gespeicherte Zeitpläne…**. Die Liste enthält jeden Zeitplan, der an diesem Becken gespeichert ist, auch solche, die du an einer anderen Pumpe gebaut hast. Wähl einen und tippe auf **In den Editor laden**. Prüf ihn im Editor und tippe dann auf **Auf Pumpe speichern**. Er ersetzt den ganzen Tag der Pumpe.

## Prüfen, ob es angekommen ist

Nach dem Speichern zeigt die Geräteseite das Programm, das die Pumpe ausführt. Passt es nicht zu dem, was du gespeichert hast, ist die Änderung nicht durchgekommen. Prüf, ob das Gerät erreichbar ist, und versuch es noch einmal.

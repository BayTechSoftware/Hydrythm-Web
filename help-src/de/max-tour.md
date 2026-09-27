---
title: Der Cora Max-Startbildschirm
description: Was du auf dem Cora Max-Bildschirm siehst, von der oberen Leiste über das Dashboard-Raster bis zur Steckdosen-Schublade.
section: Cora Max
reviewed: 2026-09-27
order: 2
group: Getting started
---

Cora Max zeigt immer ein Becken auf einmal. Der ganze Bildschirm ist voller Live-Messwerte, die du quer durch den Raum lesen kannst.

![Der Cora Max-Startbildschirm](img/max-home.webp "Ein Becken auf dem ganzen Bildschirm.")

## Die obere Leiste

Von links nach rechts:

- **Das Raster-Symbol** öffnet den Riffraum mit allen Becken, die dieser Bildschirm zeigt.
- **Der Beckenname** mit einem kleinen Pfeil. Tippst du darauf, öffnet sich das **Beckenmenü** mit allen Bildschirmen für das angezeigte Becken, vom Eintragen eines Testergebnisses bis zum Anordnen des Dashboards. Die ganze Liste steht weiter unten.
- **Hinweis-Chips für Warnungen**: alles, was gerade außerhalb seines Bereichs liegt. Passen nicht alle hinein, siehst du zum Beispiel **+2**. Tippe darauf, um alle zu sehen.
- **Die Uhr**
- **Der Status-Chip** zeigt, was dieser Bildschirm gerade tut. Grün heißt alles gut, gelb braucht deine Aufmerksamkeit, rot ist ein Fehler. Alle möglichen Anzeigen stehen weiter unten.
- **Akku und WLAN**
- **Das Geräte-Symbol**: alles, was verbunden ist, und wie es ihm geht
- **Das Reef Buddy-Symbol** öffnet die heutige Zusammenfassung. Ein Punkt bedeutet, dass du sie noch nicht gelesen hast.
- **Das Cora Assistant-Symbol** startet ein Gespräch per Sprache.
- **Das Zahnrad**: die Einstellungen

### Was der Status-Chip bedeutet

| Anzeige | Bedeutung |
|---|---|
| **Online** | Dieser Bildschirm sammelt deine Messwerte, und sie sind aktuell |
| **Cloud** | Ein anderes Cora sammelt die Messwerte dieses Beckens, und dieser Bildschirm zeigt sie an. Die Werte sind genauso aktuell wie bei **Online**. Hast du mehrere Cora, zeigt der Bildschirm, der nicht selbst sammelt, diese Anzeige |
| **Apex-Abfrage**, **Sprache aktiv** | Cora Max ist gerade mit etwas beschäftigt |
| **Abfrage aus** | Das Sammeln ist für dieses Becken ausgeschaltet. In Cora Mobile kannst du es wieder einschalten |
| **Aktualisierung läuft** | Das Sammeln pausiert, während ein Update installiert wird |
| **Veraltet** | Es kommen keine neuen Messwerte mehr an. Der Bildschirm zeigt die letzten, die er bekommen hat |
| **Apex erneut in 12s** | Dein Apex hat nicht geantwortet. Cora Max versucht es noch einmal, wenn der Countdown abgelaufen ist |
| **Cloud-Abgleich fehlgeschlagen** | Dein Apex hat geantwortet, aber seine Messwerte ließen sich nicht in Cora Cloud speichern. Das Dashboard hinkt deshalb hinterher. Cora Max versucht es weiter |
| **Offline** | Keine Verbindung. Der Bildschirm zeigt die letzten Daten, die er bekommen hat |
| **Offline, erneuter Versuch in 45s** | Dein Netzwerk läuft, aber Cora Cloud ist seit mehr als 30 Sekunden nicht erreichbar. Cora Max verbindet sich von selbst neu. Der Countdown zeigt, wann der nächste Versuch kommt |
| **Haupt-Cora offline** | Dieser Bildschirm ist ein zweites Cora Max für dieses Becken, und das **Primäre Cora Max** (das Gerät, das die Ausrüstung dieses Beckens abfragen soll) ist offline. Dieser Bildschirm zeigt die letzten Daten, bis das primäre Gerät wieder da ist oder du ein anderes Primäres Cora Max wählst. Mehr dazu unter [Mehr als ein Cora-Gerät](/help/mobile-multi-device) |
| **Apex-Passwort** | Dein Apex hat das gespeicherte Passwort abgelehnt. Mehr dazu unter [Problembehebung](/help/troubleshooting) |

:::note So läuft der Countdown für neue Versuche
Cora Max versucht in festen Abständen, sich neu zu verbinden: etwa 15 Sekunden nach dem ersten Abbruch, dann nach weiteren 15 Sekunden, dann zweimal nach je 30 Sekunden und danach jede Minute, bis es klappt. Es versucht es also nicht ununterbrochen, gibt aber auch nicht auf. Zeigt der Bildschirm **Offline, erneuter Versuch in 45s**, ist alles in Ordnung.
:::

:::warning Cora Assistant hört sofort zu
Tippst du auf das Cora Assistant-Symbol, beginnt sofort ein Live-Gespräch per Sprache. Wolltest du eigentlich in die Einstellungen, nimm das Zahnrad ganz rechts.
:::

## Das Dashboard

Den Rest des Bildschirms füllt das Dashboard aus: ein festes Raster aus Widgets, die alle gleichzeitig zu sehen sind. Das Cora Max-Dashboard scrollt nicht.

Die Widgets funktionieren wie auf deinem Handy, sind aber so groß, dass du sie auch mit etwas Abstand liest. Was jedes Widget zeigt, steht in der **[Widget-Übersicht](/help/mobile-widgets)**. Wie du das Dashboard änderst, steht unter **[Das Cora Max-Dashboard bearbeiten](/help/max-dashboard-editing)**.

Jedes Widget mit einem gemessenen Wasserwert zeigt dessen **Alter** und **Quelle**, genau wie auf dem Handy. Steht `2d` neben einer Zahl, ist sie zwei Tage alt, und das siehst du auch. Geräte- und Steuerungskacheln zeigen dagegen ihren eigenen Zustand.

## Das Beckenmenü

![Das Beckenmenü](img/max-menu.webp "Alles für das aktuelle Becken, erreichbar über den Beckennamen in der oberen Leiste.")

Tippst du auf den Beckennamen, öffnet sich das Menü für das Becken, das gerade angezeigt wird:

| Eintrag | Was sich öffnet |
|---|---|
| **Werte erfassen** | Testergebnisse über die Bildschirmtastatur eintragen |
| **Tagebuch** | [Das Tagebuch](/help/mobile-journal) für dieses Becken |
| **Reef Buddy** | Die aktuelle [Zusammenfassung](/help/mobile-reef-buddy) |
| **Zustandsberichte** | Bewertungen zum Zustand deines Beckens |
| **Wartung** | Die [Aufgabenliste](/help/mobile-maintenance) |
| **ICP-Berichte** | Hochgeladene [Laborergebnisse](/help/mobile-icp-health) |
| **Warnungen** | Der gesunde Bereich für jeden Wasserwert dieses Beckens |
| **Besatz** | Der [Besatz](/help/mobile-livestock) dieses Beckens, hier nur zum Ansehen |
| **Aktivität** | [Alle Schaltvorgänge, Fütterungen und Dosierungen](/help/max-activity) und was daraus wurde |
| **Dashboard-Layout** | [Die Widgets auf diesem Bildschirm anordnen](/help/max-dashboard-editing) |
| **Beckeneinstellungen** | Alle Einstellungen für dieses Becken |

## Das Becken wechseln

Tippe auf das **Raster-Symbol** ganz links in der oberen Leiste, um in [den Riffraum](/help/max-reef-room) zu kommen, und öffne dort das Becken, das du sehen willst. Jedes Becken hat sein eigenes Dashboard-Layout. Wechselst du das Becken, sieht also der ganze Bildschirm anders aus.

## Die Schublade Steckdosen & Füttern

An der Lasche am unteren Bildschirmrand ziehst du eine Schublade hoch. Darin findest du alle Steckdosen deines Systems und die Fütterungssteuerung.

- **Steckdosen**: Jede lässt sich einzeln auf Auto, Aus oder Ein stellen.
- **Fütterung**: pausiert die passenden Geräte zum Füttern und schaltet danach alles wieder ein.

:::warning Diese Schublade steuert echte Geräte
Alles darin wirkt direkt auf deine Ausrüstung. Ein Befehl geht raus, sobald du tippst. Gesendet heißt aber noch nicht erledigt. Zurück kommt Bestätigt, Unbestätigt, Abgelehnt oder Keine Änderung, und unter [Aktivität](/help/max-activity) siehst du, was davon zutraf. Zum Füttern nimmst du am besten den Fütterungsmodus, denn er stellt alles von selbst wieder her. Schaltest du etwas von Hand auf Aus, bleibt es aus, bis du es selbst zurückstellst.
:::

## Wenn etwas nicht stimmt

Wirken die Messwerte veraltet oder ist der Status-Chip gelb oder rot, fang mit der **[Problembehebung](/help/troubleshooting)** an.

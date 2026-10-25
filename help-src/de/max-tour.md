---
title: Der Cora Max-Startbildschirm
description: Was die obere Leiste, die Statusanzeige, die Warnhinweise, das Beckenmenü und das Dashboard auf Cora Max bedeuten und wie du das Becken wechselst.
section: Cora Max
reviewed: 2026-10-13
order: 2
group: Getting started
twin: mobile-tour
---

Diese Seite erklärt, was du auf Cora Max siehst. Es zeigt ein Becken auf einmal, mit Live-Messwerten, die den ganzen Bildschirm füllen, damit du sie quer durch den Raum lesen kannst.

![Der Cora Max-Startbildschirm mit den Anzeigen, Werten, Diagrammen und Gerätekacheln eines Beckens unter der oberen Leiste](img/max-home.webp "Das Dashboard eines Beckens füllt den Bildschirm, darüber die obere Leiste.")

## Die obere Leiste {#the-top-bar}

![Die obere Leiste von Cora Max](img/max-topbar.webp "Die obere Leiste, von links nach rechts nummeriert wie in der Liste unten.")

Von links nach rechts:

1. **Das Raster-Symbol** öffnet [den Riffraum](/help/max-reef-room), die Übersicht über alle Becken, die dieser Bildschirm zeigt.
2. **Der Beckenname**, mit einem kleinen Pfeil. Tippe darauf, um das **Beckenmenü** zu öffnen, das jeden Bildschirm für das angezeigte Becken enthält. Die ganze Liste steht unten.
3. **Warnhinweise** zeigen, was gerade Aufmerksamkeit braucht: Messwerte außerhalb des Bereichs, Gerätefehler, verpasste Dosierungen oder knappe Vorräte. Tippe auf einen Hinweis, um diese Warnung wieder in die Mitte des Bildschirms zu holen. Passen nicht alle hinein, siehst du **+2** (oder wie viele es eben sind). Tippe darauf, um jeden aktiven Alarm zu sehen.
4. **Die Uhr**. Du kannst sie mit **Uhr anzeigen** unter **Einstellungen → Cora Max-Einstellungen** ausblenden.
5. **Die Statusanzeige** zeigt, was dieser Bildschirm gerade tut. Grün heißt alles gut, Blau heißt beschäftigt, Bernstein braucht einen Blick und Rot ist ein Fehler. Jeder Status steht unten.
6. **Akku und WLAN**.
7. **Das Gerätesymbol** öffnet **Geräte**, gefiltert auf dieses Becken. Ein Becken ohne Geräte zeigt es nicht.
8. **Das Reef Buddy-Symbol** öffnet das heutige Briefing. Ein Punkt heißt, dass du es noch nicht gelesen hast.
9. **Das Cora Assistant-Symbol** startet ein Gespräch per Sprache.
10. **Das Zahnrad** öffnet die Einstellungen.

:::warning Cora Assistant hört sofort zu
Ein Tippen auf das Cora Assistant-Symbol startet sofort ein Live-Gespräch per Sprache. Wolltest du in die Einstellungen, ist das das Zahnrad ganz rechts.
:::

### Was die Statusanzeige bedeutet {#what-the-status-pill-means}

| Anzeige | Bedeutung |
|---|---|
| **Online** | Dieser Bildschirm sammelt deine Messwerte, und sie sind aktuell |
| **Cloud** | Ein anderes Cora sammelt die Messwerte dieses Beckens, und dieser Bildschirm zeigt sie. Sie sind genauso aktuell wie bei **Online**. Hast du mehr als ein Cora, zeigt das, das nicht sammelt, diese Anzeige |
| **Apex-Abfrage**, **Sprache aktiv** | Gerade mit etwas beschäftigt (blau) |
| **Abfrage aus** | Das Sammeln ist für dieses Becken ausgeschaltet. Du kannst es in Cora Mobile wieder einschalten |
| **Aktualisierung läuft** | Das Sammeln pausiert, während ein Update installiert wird |
| **Veraltet** | Es kommen keine Messwerte mehr an. Der Bildschirm zeigt die letzten, die er bekommen hat |
| **Apex erneut in 12s** | Dein Apex hat nicht geantwortet. Cora Max versucht es noch einmal, wenn der Countdown abgelaufen ist |
| **Cloud-Abgleich fehlgeschlagen** | Dein Apex hat geantwortet, aber seine Messwerte ließen sich nicht in Cora Cloud speichern, deshalb hinkt das Dashboard hinterher. Cora Max versucht es weiter |
| **Cloud-Speichern abgelehnt** | Cora Cloud lehnt es ab, einen Teil der Daten dieses Bildschirms zu speichern. Mit deinem Becken und mit Cora Max ist alles in Ordnung, und auf diesem Bildschirm musst du nichts ändern. Die Lösung ist ein Update von Cora Cloud. Öffne **Einstellungen → Cora Max-Einstellungen** und scroll zum Bereich **Status**, wo die Zeile **Cloud-Speichern** sagt, welche Daten betroffen sind. Dann [wende dich an den Support](/support.html) |
| **Offline** | Keine Verbindung. Der Bildschirm zeigt die letzten Daten, die er bekommen hat |
| **Offline, erneuter Versuch in 45s** | Dein Netzwerk läuft, aber Cora Cloud ist seit mehr als 30 Sekunden nicht erreichbar. Cora Max verbindet sich von selbst neu, und der Countdown zeigt, wann es den nächsten Versuch macht |
| **Haupt-Cora offline** | Dieser Bildschirm ist ein zweites Cora Max für dieses Becken, und das **Primäre Cora Max** (das festgelegte Gerät, das die Ausrüstung dieses Beckens abfragt) ist offline gegangen. Dieser Bildschirm zeigt weiter die letzten Daten, die er hat, bis das primäre zurückkommt oder du ein anderes Primäres Cora Max wählst. Mehr dazu unter [Mehr als ein Cora-Gerät](/help/mobile-multi-device) |
| **Apex-Passwort** | Dein Apex hat das gespeicherte Passwort abgelehnt. Schau in die [Problembehebung](/help/troubleshooting) |

:::note So funktioniert der Countdown für neue Versuche
Cora Max versucht in gleichmäßigem Takt, sich neu zu verbinden. Es wartet etwa 15 Sekunden nach dem ersten Abbruch, dann wieder 15 Sekunden, dann zweimal 30 Sekunden und danach einmal pro Minute, bis es durchkommt. Es gibt nie auf. **Offline, erneuter Versuch in 45s** ist normal.
:::

## Das Dashboard {#the-dashboard}

Den Rest des Bildschirms füllt das Dashboard, ein festes Raster, das jedes Widget sichtbar hält. Es scrollt nicht.

Widgets funktionieren wie auf deinem Handy, sind aber groß genug, um sie ein paar Schritte entfernt zu lesen. Was jede Form zeigt, steht in der [Widget-Referenz](/help/mobile-widgets). Um zu ändern, was auf dem Dashboard ist, siehe [Das Cora Max-Dashboard bearbeiten](/help/max-dashboard-editing).

Jedes Widget mit einem gemessenen Wasserwert zeigt sein **Alter** und seine **Quelle**, genau wie auf dem Handy. Eine Zahl mit `2d` daneben ist zwei Tage alt. Geräte- und Steuerungskacheln zeigen stattdessen ihren eigenen Zustand.

### Wenn der Bildschirm gedimmt ist {#when-the-screen-is-dimmed}

Nach der Zeit unter **Dimmen nach** ohne Berührung dimmt sich der Bildschirm. Dein erstes Tippen weckt ihn nur, damit es nicht aus Versehen eine Steuerung drückt. Tippe noch einmal, um den Bildschirm zu nutzen.

## Das Beckenmenü {#the-tank-menu}

![Das Beckenmenü über dem Dashboard, mit Werte erfassen, Tagebuch, Reef Buddy und den anderen Bildschirmen für das Becken](img/max-menu.webp "Das Beckenmenü, geöffnet über den Beckennamen in der oberen Leiste.")

Tippe auf den Beckennamen, um das Menü für das angezeigte Becken zu öffnen.

| Eintrag | Öffnet |
|---|---|
| **Werte erfassen** | Testkit-Messwerte über die Bildschirmtastatur eintippen |
| **Tagebuch** | [Das Tagebuch](/help/max-records) für dieses Becken |
| **Reef Buddy** | Das neueste [Briefing](/help/max-intelligence) |
| **Gesundheitsberichte** | Gesundheitsbewertungen |
| **Wartung** | Die [Aufgabenliste](/help/max-records) |
| **ICP-Berichte** | Hochgeladene [Laborergebnisse](/help/max-intelligence) |
| **Parameterverlauf** | Einen beliebigen Wasserwert mit Daten wählen und sein [Diagramm](/help/max-intelligence) öffnen |
| **Warnschwellen** | Der [gesunde Bereich](/help/max-alerts) für jeden Wert dieses Beckens |
| **Besatz** | Der Bestand dieses Beckens, auf diesem Bildschirm nur zum Ansehen |
| **Aktivität** | [Jede Steckdose, Fütterung und Dosierung](/help/max-activity) und was passiert ist |
| **Dashboard-Layout** | [Die Widgets auf diesem Bildschirm anordnen](/help/max-dashboard-editing) |
| **Einheiten** | Die Anzeigeeinheiten für die Messwerte dieses Beckens |
| **Beckeneinstellungen** | Der vollständige Einstellungsbildschirm für dieses Becken |

## Das Becken wechseln {#switching-tanks}

Tippe auf das **Raster-Symbol** ganz links in der oberen Leiste, um zu [dem Riffraum](/help/max-reef-room) zu gehen, und öffne dann das Becken, das du willst. Du kannst auch auf dem Dashboard zur Seite wischen. Jedes Becken hat sein eigenes Dashboard-Layout, der ganze Bildschirm ändert sich also beim Wechseln.

## Die Schublade Steckdosen & Füttern {#the-outlets-feed-drawer}

Bei einem Becken mit Neptune Apex sitzt unten auf dem Dashboard eine kleine Beschriftung **Steckdosen & Füttern**. Tippe darauf oder wisch irgendwo auf dem Dashboard nach oben, um **Steuerung** zu öffnen.

- **FÜTTERN** startet einen deiner Apex-Fütterungszyklen mit **A**, **B**, **C** oder **D**. **Abbrechen** beendet ihn vorzeitig.
- **STECKDOSEN** lassen sich jeweils zwischen Auto, Aus und Ein schalten.

Sie listet die Steckdosen und Fütterungszyklen auf, die du für dieses Dashboard ausgewählt hast, oder alle, wenn du keine ausgewählt hast. Mehr dazu unter [Steckdosen und Steuerung](/help/max-controls).

:::warning Diese Schublade steuert echte Ausrüstung
Ein Befehl geht raus, sobald du tippst, aber gesendet heißt nicht erledigt. Er kommt mit Bestätigt, Unbestätigt, Abgelehnt oder Keine Änderung zurück, und unter [Aktivität](/help/max-activity) siehst du, was davon. Der Fütterungsmodus ist der sichere Weg, die Strömung zum Füttern zu pausieren, denn er stellt alles von selbst wieder her. Ein manuelles Aus bleibt aus, bis du es zurückstellst.
:::

## Wenn etwas nicht stimmt {#if-something-looks-out-of-place}

Wirken die Messwerte veraltet oder ist die Statusanzeige bernsteinfarben oder rot, fang mit der [Problembehebung](/help/troubleshooting) an.

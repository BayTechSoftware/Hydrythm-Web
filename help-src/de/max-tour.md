---
title: Der Cora Max Startbildschirm
description: Was alles auf dem Cora Max Display bedeutet: die obere Leiste, das Dashboard-Raster und die Steckdosen-Schublade.
section: Cora Max
reviewed: 2026-09-27
order: 2
group: Getting started
---

Cora Max zeigt jeweils ein Becken, füllt den Bildschirm mit Live-Messwerten, die du quer durch den Raum lesen kannst.

![Der Cora Max Startbildschirm](img/max-home.webp "Ein Becken, den ganzen Bildschirm ausfüllend.")

## Die obere Leiste

Von links nach rechts:

- **Das Raster-Symbol** öffnet den Riffraum, die Übersicht über alle Becken, die dieser Bildschirm zeigt
- **Der Beckenname**, mit einem Chevron. Tippen darauf öffnet das **Beckenmenü**: jeden Bildschirm für das angezeigte Becken, vom Protokollieren eines Testergebnisses bis zum Anordnen des Dashboards. Die vollständige Liste steht unten.
- **Warnungs-Pillen**: alles, was derzeit außerhalb des Bereichs liegt, mit einem **+n**, wenn mehr nicht hineinpassen. Tippen zeigt sie alle.
- **Die Uhr**
- **Die Status-Pille**: was dieser Bildschirm gerade tut. Grün ist gesund, gelb braucht Aufmerksamkeit, rot ist ein Fehler. Das vollständige Vokabular steht unten.
- **Akku und WLAN**
- **Das Geräte-Symbol**: alles Verbundene, und wie es ihm geht
- **Das Reef Buddy-Symbol**: öffnet die heutige Zusammenfassung. Ein Punkt bedeutet, dass die Zusammenfassung noch nicht gelesen wurde.
- **Das Cora Assistant-Symbol**: startet ein Sprachgespräch
- **Das Zahnrad**: Einstellungen

### Was die Status-Pille bedeutet

| Pille | Bedeutung |
|---|---|
| **Online** | Dieser Bildschirm sammelt deine Messwerte, und sie sind aktuell |
| **Cloud** | Ein anderes Cora sammelt die Messwerte dieses Beckens, und dieser Bildschirm zeigt sie an. Genauso aktuell wie **Online**; bei mehr als einem Cora zeigt der Bildschirm, der nicht sammelt, diese Pille |
| **Apex-Abfrage**, **Sprache aktiv** | Arbeitet in diesem Moment an etwas |
| **Abfrage aus** | Das Sammeln ist für dieses Becken ausgeschaltet. Du kannst es in Cora Mobile wieder einschalten |
| **Aktualisierung läuft** | Das Sammeln ist pausiert, während ein Update installiert wird |
| **Veraltet** | Es kommen keine Messwerte mehr an. Der Bildschirm zeigt den letzten, den er erhalten hat |
| **Apex erneut versuchen 12s** | Dein Apex hat nicht geantwortet. Cora Max versucht es erneut, wenn der Countdown endet |
| **Cloud-Abgleich fehlgeschlagen** | Dein Apex hat geantwortet, aber seine Messwerte konnten nicht in Cora Cloud gespeichert werden, sodass das Dashboard zurückbleibt. Cora Max versucht es weiterhin erneut |
| **Offline** | Keine Verbindung. Der Bildschirm zeigt die letzten Daten, die er erhalten hat |
| **Offline, erneuter Versuch in 45s** | Dein Netzwerk läuft, aber Cora Cloud war seit mehr als 30 Sekunden nicht erreichbar. Cora Max verbindet sich von selbst wieder; der Countdown ist die Zeit bis zum nächsten Versuch |
| **Haupt-Cora offline** | Dieser Bildschirm ist ein zweites Cora Max für dieses Becken, und das **primäre Cora Max** (das für die Abfrage der Ausrüstung dieses Beckens festgelegte) ist offline gegangen. Dieser Bildschirm zeigt weiterhin die letzten Daten, die er hat, bis das primäre wieder da ist, oder bis du ein anderes primäres Cora Max wählst. Siehe [Mehr als ein Cora-Gerät](/help/mobile-multi-device) |
| **Apex-Passwort** | Dein Apex hat das gespeicherte Passwort abgelehnt. Siehe [Problembehebung](/help/troubleshooting) |

:::note So funktioniert der Wiederholungs-Countdown
Cora Max versucht in einem festen Takt, sich wieder zu verbinden: etwa 15 Sekunden nach dem ersten Abbruch, 15 Sekunden danach, dann zweimal alle 30 Sekunden, dann jede Minute, bis es gelingt. Es versucht nicht sofort erneut und gibt nicht auf; ein Bildschirm, der **Offline, erneuter Versuch in 45s** zeigt, tut genau das, was er soll.
:::

:::warning Cora Assistant beginnt sofort zu hören
Tippen auf das Cora Assistant-Symbol startet eine Live-Sprachsitzung. Wenn du eigentlich die Einstellungen öffnen wolltest: Das ist das Zahnrad ganz rechts.
:::

## Das Dashboard

Der Rest des Bildschirms ist das Dashboard: ein festes Raster aus Widgets, alle gleichzeitig sichtbar. Das Cora Max Dashboard scrollt nicht.

Widgets funktionieren genauso wie auf deinem Handy, nur in einer Größe, die du auch aus der Entfernung lesen kannst. Siehe **[Widget-Referenz](/help/mobile-widgets)** für das, was jede Form zeigt, und **[Das Cora Max Dashboard bearbeiten](/help/max-dashboard-editing)**, um zu ändern, was darauf ist.

Jedes Widget, das einen gemessenen Wasserwert zeigt, trägt sein **Alter** und seine **Quelle**, genau wie auf dem Handy. Eine Zahl mit `2d` daneben ist zwei Tage alt und wird auch so angezeigt. Geräte- und Steuerungskacheln zeigen stattdessen ihren eigenen Zustand.

## Das Beckenmenü

![Das Beckenmenü](img/max-menu.webp "Alles für das aktuelle Becken, über den Beckennamen in der oberen Leiste.")

Tippen auf den Beckennamen öffnet das Menü für das gerade angezeigte Becken:

| Eintrag | Öffnet |
|---|---|
| **Wasserwerte protokollieren** | Testkit-Messwerte über die Bildschirmtastatur eingeben |
| **Tagebuch** | [Das Tagebuch](/help/mobile-journal) für dieses Becken |
| **Reef Buddy** | Die aktuelle [Zusammenfassung](/help/mobile-reef-buddy) |
| **Zustandsberichte** | Zustandsbewertungen |
| **Wartung** | Die [Aufgabenliste](/help/mobile-maintenance) |
| **ICP-Berichte** | Hochgeladene [Laborergebnisse](/help/mobile-icp-health) |
| **Warnungen** | Der gesunde Bereich für jeden Wasserwert dieses Beckens |
| **Besatz** | Das [Inventar](/help/mobile-livestock) dieses Beckens, auf diesem Bildschirm nur lesbar |
| **Aktivität** | [Jede Steckdose, Fütterung und Dosierung](/help/max-activity), und was daraus wurde |
| **Dashboard-Layout** | [Die Widgets auf diesem Bildschirm anordnen](/help/max-dashboard-editing) |
| **Beckeneinstellungen** | Der vollständige Einstellungsbildschirm für dieses Becken |

## Zwischen Becken wechseln

Nutze das **Raster-Symbol** ganz links in der oberen Leiste, um [den Riffraum](/help/max-reef-room) zu erreichen, und öffne dann das gewünschte Becken. Jedes Becken behält sein eigenes Dashboard-Layout, sodass sich der ganze Bildschirm ändert, wenn du zwischen ihnen wechselst.

## Die Steckdosen & Fütterung-Schublade

Der Tab am unteren Rand des Bildschirms zieht eine Schublade mit jeder Steckdose im System und den Fütterungssteuerungen hoch.

- **Steckdosen**: jede einzeln umschaltbar zwischen Auto, Aus und Ein
- **Fütterung**: pausiert die richtige Ausrüstung für eine Fütterung und stellt danach alles wieder her

:::warning Diese Schublade steuert echte Ausrüstung
Alles darin wirkt auf echte Ausrüstung. Ein Befehl wird in dem Moment gesendet, in dem du tippst, aber *gesendet* ist nicht *erledigt*; er kommt als Bestätigt, Unbestätigt, Abgelehnt oder Keine Änderung zurück, und [Aktivität](/help/max-activity) ist der Ort, an dem du siehst, welches davon zutrifft. Der Fütterungsmodus ist der sichere Weg, den Durchfluss für die Fütterung zu pausieren, weil er alles von selbst wiederherstellt; ein manuelles Aus bleibt aus, bis du es selbst wieder zurückstellst.
:::

## Wenn etwas nicht stimmt

Wenn Messwerte veraltet wirken, oder die Status-Pille gelb oder rot ist, beginne mit **[Problembehebung](/help/troubleshooting)**.

---
title: Deine Ausrüstung verbinden
description: So verbindest du Neptune Apex-, Red Sea ReefBeat-, Jecod- und AquaWiz-Ausrüstung mit Cora.
section: Cora Mobile
reviewed: 2026-09-17
order: 10
group: Equipment
---

Cora funktioniert mit Ausrüstung, die du schon besitzt. Diese Seite deckt ab, was unterstützt wird und was jede Verbindung braucht.

Jede Marke verbindet sich auf die Art, die zu ihr passt, daher starte am Einstiegspunkt für deine Ausrüstung:

| Marke | Starte bei |
|---|---|
| Neptune Apex | Dem Becken; sein Profil enthält die Apex-Verbindung |
| Red Sea ReefBeat | Dem Becken |
| Jecod / Jebao | **Geräte → Pumpe im Netzwerk suchen**, oder Bluetooth |
| AquaWiz | **Geräte → AquaWiz hinzufügen** |
| Maxspect *(Beta)* | **Geräte → Pumpe im Netzwerk suchen** |
| Cora Max | **Geräte → Gerät hinzufügen** |

## Neptune Apex

Cora liest deinen Apex über dein lokales Netzwerk: Sonden, Steckdosen und alle eingebauten Erweiterungsmodule.

**Du brauchst:** die Adresse deines Apex in deinem Netzwerk, und seine Anmeldedaten.

**Was du bekommst:** jede von deinem Apex gemeldete Sonde erscheint als Quelle, die du auf ein Dashboard setzen kannst. Steckdosen erscheinen als Steuerungen. Eingebaute Erweiterungsmodule bekommen eigene Gerätekacheln.

:::note Dein Apex behält seine eigene Programmierung
Cora liest deinen Apex, zeigt ihn zusammen mit allem anderen, und kann Steckdosen schalten, wenn du das verlangst. Deine eigene Programmierung läuft weiter genau so, wie du sie eingerichtet hast.
:::

## Red Sea ReefBeat

Cora spricht mit ReefBeat-Ausrüstung in deinem lokalen Netzwerk. Unterstützte Geräte sind **ReefDose**, **ReefATO+**, **ReefMat** und **ReefRun**.

**Du brauchst:** die Ausrüstung, bereits in ReefBeat eingerichtet und im selben Netzwerk wie dein Handy, wenn du sie hinzufügst.

**Was du bekommst:** eine Geräteseite pro Gerät, sowie die Messwerte jedes Geräts als Quellen. ReefDose meldet seine Köpfe und Behälter; ReefATO+ meldet sein Reservoir und Nachfüllungen; ReefMat meldet verbleibende Tage; ReefRun meldet den Pumpenzustand.

## Jecod / Jebao

Cora verbindet sich mit Jecod-Pumpen und kann sie lesen und steuern. Jecod-Geräte erreichen Cora auf einem von zwei Wegen, und welchen deins nutzt, entscheidet, was möglich ist.

![Eine Pumpe finden](img/mobile-connections.webp "Der Scan erklärt, was er braucht und warum eine Pumpe beim ersten Durchgang vielleicht nicht erscheint.")

**Über dein Netzwerk.** Nutze **Pumpe im Netzwerk suchen**; das findet Geräte, die sich selbst bekannt geben, daher muss keine Adresse eingegeben werden. Eine Netzwerkpumpe kann gelesen und gesteuert werden, wann immer sie eingeschaltet **und erreichbar** ist: Entweder ist dein Handy im selben Netzwerk, oder ein Cora Max in diesem Netzwerk leitet für dich weiter. Fern von zu Hause, ohne Cora Max vor Ort, ist eine reine Netzwerkpumpe sichtbar, aber nicht steuerbar.

:::note Eine Pumpe verpasst oft den ersten Durchgang
Pumpen antworten auf einen Scan und verpassen den nächsten. Wenn deine nicht aufgeführt ist, scanne erneut, statt anzunehmen, dass sie nicht erreichbar ist.
:::

Wenn eine Suche nichts findet, zeigt das Ergebnis die Adressen, die im WLAN überprüft wurden. Wenn deine Pumpe in der Jebao-App eine andere Adresse hat, ist dein Handy in einem anderen Netzwerk. Ein Gast- oder IoT-Netzwerk, oder ein reines 5-GHz-Band, sieht diese Pumpen nicht. Auf dem iPhone braucht Cora außerdem Zugriff auf das lokale Netzwerk, um Pumpen in deinem WLAN zu sehen. Ist das aus, bleibt die Liste leer und es erscheint kein Fehler, daher erklärt das Ergebnis das und bietet **Einstellungen öffnen** an, um es wieder einzuschalten. **Einstellungen → Gerätezugriff** öffnet jederzeit denselben Ort; siehe [Einstellungen](/help/mobile-settings).

**Über Bluetooth.** Manche Pumpen sind nur von einem Handy in ihrer Nähe erreichbar. Die Seite der Pumpe sagt das, und zeigt die letzten Einstellungen, die sie lesen konnte, zusammen mit deren Alter.

Cora braucht dafür die Bluetooth-Berechtigung. Erteile sie, bevor du eine Bluetooth-Pumpe hinzufügst: ohne Berechtigung kann die Pumpe überhaupt nicht entdeckt werden, statt nur länger zu brauchen, um zu erscheinen.

**Was du bekommst:** Live-Zustand, Modus und Intensität, Fütterungspause, und ein Tagesprogramm. Siehe [Ausrüstung planen](/help/mobile-schedules).

:::warning Eine Bluetooth-Pumpe ist nur erreichbar, wenn du in der Nähe bist
Ihre Seite zeigt die letzten von Cora gelesenen Einstellungen und wie lange das her ist. Um etwas zu ändern, einschließlich einer Fütterungspause zu starten, muss die Pumpe in Reichweite sein. Steh in ihrer Nähe und öffne die Seite erneut.
:::

## AquaWiz KH-Controller

Cora liest Alkalinität von einem AquaWiz KH-Controller über dein AquaWiz-Konto.

**Du brauchst:** deinen AquaWiz-Benutzernamen und dein Passwort. Cora meldet sich im Auftrag an und behält die Anmeldung, um weiter lesen zu können.

**Was du bekommst:** Alkalinität als Quelle, so oft aktualisiert, wie dein Controller titriert. pH ist als Option verfügbar, wenn dein Gerät ihn meldet.

:::warning Eine Anmeldung, geteilt
AquaWiz gibt eine einzige Anmeldung pro Konto aus, daher ist die, die Cora hält, dieselbe, die deren eigene App nutzt. Wenn du dein AquaWiz-Passwort änderst, trennt sich Cora; verbinde es danach wieder über die Gerätezeile. Um Coras Zugriff vollständig zu widerrufen, entferne das Gerät in Cora und ändere dein AquaWiz-Passwort.
:::

## Maxspect

:::note Die Maxspect-Unterstützung ist in der Beta
Die Unterstützung für Maxspect-Gyres wird noch getestet und weiterentwickelt, daher können manche Steuerungen eingeschränkt sein, und was du hier siehst, kann sich zwischen Updates ändern. Wenn etwas nicht wie beschrieben funktioniert, sag es uns über [Hilfe erhalten](/help/mobile-support).
:::

Cora verbindet sich mit Maxspect Gyre-Pumpen und kann sie lesen und steuern.

**Du brauchst:** wenn du sie hinzufügst, die Gyre und dein Handy im selben Netzwerk. Nutze **Geräte → Pumpe im Netzwerk suchen**.

**Was du bekommst:** Wellenmuster und Geschwindigkeit für **Gyre A** und **Gyre B**, den Zeitplan der Gyre zur Ansicht (lege ihn in der Maxspect-App fest), **Pumpenzustand**, und ob sie läuft, mit dem Zeitpunkt der letzten Messung. Siehe [Deine Ausrüstung steuern](/help/mobile-device-control).

:::note Wie Cora Mobile eine Gyre erreicht
Wenn ein Cora Max das Becken bedient, arbeitet Cora Mobile über dieses Cora Max, auch wenn du nicht zu Hause bist, und **Einstellungen ändern** startet von der letzten Messung dieses Cora Max. Andernfalls spricht dein Handy direkt mit der Gyre und muss im Netzwerk der Gyre sein. Die Seite der Gyre zu öffnen liest sie dann. Zeigt die Seite statt dessen eine ältere gespeicherte Messung, bleibt **Einstellungen ändern** verborgen, bis du auf Aktualisieren tippst.
:::

## Von Hand protokollieren

Manche Wasserwerte kommen von einem Testkit statt von Ausrüstung. Um ein Ergebnis einzutragen, scroll ans Ende des Dashboards und tippe auf **Wasserwerte protokollieren**.

Von Hand protokollierte Messwerte sind vollwertig: Sie erscheinen auf Widgets, tragen ihre eigene Quelle und ihr Alter, speisen Reef Buddy, und sind das, wogegen Cora deine Sonden vergleicht, wenn es dir sagt, dass zwei Quellen sich widersprechen.

## Wenn eine Verbindung nicht mehr funktioniert

Die Gerätezeile sagt dir, um welche Art von Problem es sich handelt. Siehe die Tabelle in **[Geräte hinzufügen, bearbeiten und entfernen](/help/mobile-devices)**, und **[Problembehebung](/help/troubleshooting)** für alles, was sie nicht abdeckt.

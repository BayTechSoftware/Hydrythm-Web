---
title: Deine Ausrüstung verbinden
description: So verbindest du Neptune Apex, Red Sea ReefBeat, Jecod, AquaWiz, GHL und HYDROS mit Cora.
section: Cora Mobile
reviewed: 2026-09-30
order: 10
group: Equipment
---

Cora arbeitet mit der Ausrüstung, die du schon hast. Hier erfährst du, was unterstützt wird und was du für die einzelnen Verbindungen brauchst.

Jede Marke wird auf ihre eigene Art verbunden. Such dir in der Tabelle den Startpunkt für deine Ausrüstung:

| Marke | Hier startest du |
|---|---|
| Neptune Apex | Beim Becken. Die Apex-Verbindung steckt in seinem Profil |
| Red Sea ReefBeat | Beim Becken |
| Jecod / Jebao | **Geräte → Pumpe im Netzwerk suchen** oder per Bluetooth |
| AquaWiz | **Geräte → AquaWiz hinzufügen** |
| Maxspect *(Beta)* | **Geräte → Pumpe im Netzwerk suchen** |
| GHL ProfiLux / Mitras *(Beta)* | Cora Max, in den Beckeneinstellungen |
| HYDROS *(Beta)* | **Geräte → HYDROS hinzufügen (Beta)** |
| Cora Max | **Geräte → Gerät hinzufügen** |

## Neptune Apex

Cora liest deinen Apex über dein lokales Netzwerk aus, also Sonden, Steckdosen und alle eingebauten Erweiterungsmodule.

Du brauchst dafür die Adresse deines Apex in deinem Netzwerk und seine Zugangsdaten.

Jede Sonde, die dein Apex meldet, steht dir danach als Quelle zur Verfügung, die du aufs Dashboard legen kannst. Steckdosen erscheinen als Schalter. Eingebaute Erweiterungsmodule bekommen eigene Gerätekacheln.

:::note Dein Apex behält seine eigene Programmierung
Cora liest deinen Apex aus, zeigt ihn neben allem anderen an und schaltet Steckdosen, wenn du das willst. Deine eigene Programmierung läuft genau so weiter, wie du sie eingerichtet hast.
:::

## Red Sea ReefBeat

Cora spricht mit ReefBeat-Geräten in deinem lokalen Netzwerk. Unterstützt werden **ReefDose**, **ReefATO+**, **ReefMat** und **ReefRun**.

Die Geräte müssen schon in ReefBeat eingerichtet sein. Beim Hinzufügen müssen sie im selben Netzwerk sein wie dein Handy.

Du bekommst für jedes Gerät eine eigene Geräteseite, und seine Messwerte stehen dir als Quellen zur Verfügung. ReefDose meldet seine Köpfe und Behälter. ReefATO+ meldet seinen Vorratsbehälter und die Nachfüllungen. ReefMat meldet die verbleibenden Tage, ReefRun den Zustand der Pumpe.

## Jecod / Jebao

Cora verbindet sich mit Jecod-Pumpen, liest sie aus und steuert sie. Jecod-Geräte erreichen Cora auf einem von zwei Wegen. Welchen Weg deine Pumpe nutzt, bestimmt, was möglich ist.

![Eine Pumpe finden](img/mobile-connections.webp "Der Scan erklärt, was er braucht und warum eine Pumpe beim ersten Durchgang vielleicht nicht erscheint.")

### Über dein Netzwerk

Tippe auf **Pumpe im Netzwerk suchen**. Die Suche findet Geräte, die sich im Netzwerk selbst melden. Eine Adresse musst du also nicht eingeben. Eine Netzwerkpumpe kannst du auslesen und steuern, solange sie eingeschaltet **und erreichbar** ist. Dafür ist entweder dein Handy im selben Netzwerk, oder ein Cora Max in diesem Netzwerk leitet für dich weiter. Bist du unterwegs und steht kein Cora Max vor Ort, siehst du eine reine Netzwerkpumpe zwar, kannst sie aber nicht steuern.

:::note Beim ersten Scan fehlt oft eine Pumpe
Pumpen antworten auf einen Scan und verpassen den nächsten. Fehlt deine in der Liste, scanne einfach noch einmal. Das heißt noch nicht, dass sie nicht erreichbar ist.
:::

Findet die Suche nichts, zeigt das Ergebnis die Adressen, die im WLAN geprüft wurden. Hat deine Pumpe in der Jebao-App eine andere Adresse, ist dein Handy in einem anderen Netzwerk. Aus einem Gast- oder IoT-Netzwerk oder einem reinen 5-GHz-Band heraus siehst du diese Pumpen nicht. Auf dem iPhone braucht Cora außerdem Zugriff auf das lokale Netzwerk, um Pumpen in deinem WLAN zu finden. Ist der Zugriff aus, bleibt die Liste leer, ohne Fehlermeldung. Deshalb erklärt das Ergebnis das und bietet dir **Einstellungen öffnen** an, damit du den Zugriff wieder einschalten kannst. Über **Einstellungen → Gerätezugriff** kommst du jederzeit an dieselbe Stelle. Mehr dazu unter [Einstellungen](/help/mobile-settings).

### Über Bluetooth

Manche Pumpen erreicht nur ein Handy, das direkt in der Nähe ist. Das steht dann auf der Seite der Pumpe. Dort siehst du auch die letzten Einstellungen, die Cora lesen konnte, und wie alt sie sind.

Cora braucht dafür die Bluetooth-Berechtigung. Erteil sie, bevor du eine Bluetooth-Pumpe hinzufügst. Ohne Berechtigung findet Cora die Pumpe überhaupt nicht, auch nicht nach längerem Warten.

Über beide Wege bekommst du den Live-Zustand, Modus und Intensität, die Fütterungspause und ein Tagesprogramm. Mehr dazu unter [Ausrüstung planen](/help/mobile-schedules).

:::warning Eine Bluetooth-Pumpe erreichst du nur aus der Nähe
Auf ihrer Seite siehst du die zuletzt gelesenen Einstellungen und wie lange das her ist. Willst du etwas ändern, auch eine Fütterungspause starten, muss die Pumpe in Reichweite sein. Stell dich in ihre Nähe und öffne die Seite noch einmal.
:::

## AquaWiz KH-Controller

Cora liest die Alkalinität eines AquaWiz KH-Controllers über dein AquaWiz-Konto aus.

Du brauchst dafür deinen AquaWiz-Benutzernamen und dein Passwort. Cora meldet sich in deinem Namen an und bleibt angemeldet, damit es weiter Werte lesen kann.

Die Alkalinität steht dir dann als Quelle zur Verfügung. Sie aktualisiert sich so oft, wie dein Controller titriert. Meldet dein Gerät auch den pH-Wert, kannst du ihn zusätzlich nutzen.

:::warning Eine Anmeldung für alle
AquaWiz vergibt nur eine Anmeldung pro Konto. Cora nutzt also dieselbe Anmeldung wie die AquaWiz-App. Änderst du dein AquaWiz-Passwort, verliert Cora die Verbindung. Verbinde es danach über die Gerätezeile neu. Willst du Cora den Zugriff ganz entziehen, entferne das Gerät in Cora und ändere dein AquaWiz-Passwort.
:::

## Maxspect

:::note Maxspect wird als Beta unterstützt
Die Unterstützung für Maxspect Gyre wird noch getestet und weiterentwickelt. Manche Steuerungen können deshalb eingeschränkt sein, und was du hier siehst, kann sich mit Updates ändern. Klappt etwas nicht wie beschrieben, sag uns über [Hilfe erhalten](/help/mobile-support) Bescheid.
:::

Cora verbindet sich mit Maxspect Gyre-Pumpen, liest sie aus und steuert sie.

Beim Hinzufügen müssen die Gyre und dein Handy im selben Netzwerk sein. Tippe auf **Geräte → Pumpe im Netzwerk suchen**.

Du bekommst Wellenmuster und Geschwindigkeit für **Gyre A** und **Gyre B** und kannst den Zeitplan der Gyre ansehen. Festlegen musst du ihn in der Maxspect-App. Dazu kommen der **Pumpenzustand** und die Info, ob sie läuft und wann sie zuletzt ausgelesen wurde. Mehr dazu unter [Deine Ausrüstung steuern](/help/mobile-device-control).

:::note Wie Cora Mobile eine Gyre erreicht
Betreut ein Cora Max das Becken, arbeitet Cora Mobile über dieses Cora Max, auch wenn du nicht zu Hause bist. **Einstellungen ändern** startet dann mit der letzten Messung dieses Cora Max. Ohne Cora Max spricht dein Handy direkt mit der Gyre und muss dafür in ihrem Netzwerk sein. Öffnest du dann die Seite der Gyre, liest Cora sie aus. Zeigt die Seite stattdessen eine ältere gespeicherte Messung, bleibt **Einstellungen ändern** ausgeblendet, bis du auf Aktualisieren tippst.
:::

## GHL ProfiLux und Mitras

:::note GHL wird als Beta unterstützt
Die Unterstützung für GHL wird noch getestet und weiterentwickelt. Manche Messwerte oder Steuerungen funktionieren vielleicht noch nicht, und was du hier siehst, kann sich mit Updates ändern. Klappt etwas nicht wie beschrieben, sag uns über [Hilfe erhalten](/help/mobile-support) Bescheid.
:::

Cora liest einen GHL ProfiLux- oder Mitras-Controller über dein lokales Netzwerk aus: Sonden, Steckdosen, Dosierer, Füllstandssensoren und, bei den Director-Modellen, KH- und Ionen-Testergebnisse.

Verbunden wird er über **Cora Max**, nicht über dein Handy: Öffne die Einstellungen des Beckens und trag dort seine IP-Adresse ein. Die Schritte dazu stehen unter [Ausrüstung mit Cora Max steuern](/help/max-device-control). Ist er einmal verbunden, erscheinen seine Messwerte und Steuerungen auch auf deinem Handy.

Damit Cora den Controller überhaupt erreicht, muss die GHL-API eingeschaltet sein. GHL schaltet sie nach jedem Firmware-Update wieder aus. Prüf das also zuerst, wenn nichts erscheint. Was du sonst tun kannst, steht unter [Problembehebung](/help/troubleshooting).

## HYDROS

:::note HYDROS wird als Beta unterstützt
Die Unterstützung für HYDROS wird noch getestet und weiterentwickelt. Manche Messwerte oder Steuerungen funktionieren vielleicht noch nicht, und was du hier siehst, kann sich mit Updates ändern. Klappt etwas nicht wie beschrieben, sag uns über [Hilfe erhalten](/help/mobile-support) Bescheid.
:::

HYDROS ist die einzige Anbindung, bei der Cora und dein Controller nicht im selben Netzwerk sein müssen. Cora erreicht ihn über die eigene Cloud von HYDROS, deshalb funktioniert es auch unterwegs und sogar bei geschlossener Cora-App.

Zum Verbinden öffne die HYDROS-App und leg dort einen **Geräteschlüssel** für den Anbieter **cora-iq** an. Wähl **Lesen**, wenn du nur die Messwerte willst, oder **Schreiben**, wenn du den Controller auch von Cora aus steuern willst. Geh dann zu **Geräte → HYDROS hinzufügen (Beta)** und füg den Schlüssel ein.

Sobald er verbunden ist, importiert Cora die letzten 33 Tage seiner Historie und liest danach fortlaufend weiter. Was du lesen und, mit einem Write-Code, steuern kannst, steht unter [Deine Ausrüstung steuern](/help/mobile-device-control).

## Von Hand eintragen

Manche Wasserwerte misst du mit einem Testkit und nicht mit einem Gerät. Um ein Ergebnis einzutragen, scroll im Dashboard ganz nach unten und tippe auf **Wasserwerte protokollieren**.

Von Hand eingetragene Messwerte sind vollwertig. Sie erscheinen auf Widgets, haben ihre eigene Quelle und ihr eigenes Alter und fließen in Reef Buddy ein. Mit ihnen vergleicht Cora auch deine Sonden, wenn zwei Quellen nicht zusammenpassen.

## Wenn eine Verbindung nicht mehr klappt

An der Gerätezeile siehst du, welche Art von Problem vorliegt. Die Tabelle dazu steht unter **[Geräte hinzufügen, bearbeiten und entfernen](/help/mobile-devices)**. Alles andere findest du in der **[Problembehebung](/help/troubleshooting)**.

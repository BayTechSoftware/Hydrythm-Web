---
title: Deine Ausrüstung verbinden
description: So verbindest du ein Neptune Apex-, Red Sea ReefBeat-, Jecod- oder AquaWiz-Gerät mit Cora.
section: Cora Mobile
reviewed: 2026-10-17
order: 12
group: Equipment
---

Diese Seite zeigt, wie du jede Marke mit Cora verbindest und was jede Verbindung braucht. Alle fangen gleich an: **Geräte → Gerät hinzufügen**, dann wählst du die Marke.

![Die Markenliste unter Gerät hinzufügen](img/mobile-add-device-brands.webp "Die Markenliste.")


| Marke | Öffnet | Ohne Cora Max |
|---|---|---|
| Cora | Einen Scan nach einem neuen Cora Max, über WLAN oder Bluetooth | |
| Neptune Apex | Einen Netzwerkscan oder seine IP-Adresse, dann die Becken, die er versorgt | Nur lokal |
| Red Sea | Einen Scan in deinem Netzwerk, dann das Becken, zu dem jedes Gerät gehört | Nur lokal |
| Jecod / Jebao | Einen Scan in deinem Netzwerk oder Bluetooth | Nur lokal |
| AquaWiz | Deine AquaWiz-Anmeldung | Funktioniert |

## Ohne Cora Max: nur lokal {#local-only}

Neptune Apex-, Red Sea- und Jecod-Ausrüstung ist in deinem Heimnetz (oder über Bluetooth erreichbar). Hast du kein Cora Max (oder keins an dem Becken, zu dem du hinzufügst), sagt der Bildschirm zum Hinzufügen bei diesen Marken *Diese Integration funktioniert ohne Cora Max nur lokal in der Mobile-App.* Das heißt:

- Dein Handy liest und steuert die Ausrüstung, solange Cora Mobile im selben Netzwerk geöffnet ist oder in Bluetooth-Reichweite.
- Unterwegs siehst du die letzten Messwerte, die dein Handy gespeichert hat, und kannst sie nicht steuern.

Ein Cora Max am Becken fragt diese Ausrüstung rund um die Uhr ab und leitet deine Befehle weiter, wenn du unterwegs bist. AquaWiz wird über den eigenen Dienst des Herstellers erreicht und funktioniert also überall ohne Cora Max. Mehr dazu unter [Mehr als ein Cora-Gerät](/help/mobile-multi-device).

## Neptune Apex {#neptune-apex}

Cora liest deinen Apex über dein lokales Netzwerk, mit Sonden, Steckdosen und allen Erweiterungsmodulen, die du eingebaut hast.

1. Geh zu **Geräte → Gerät hinzufügen → Neptune Apex**.
2. Tippe auf **Netzwerk nach APEX durchsuchen** und wähl deinen Apex, oder gib seine Adresse unter **Oder gib die IP manuell ein:** ein.
3. Füll **Apex-Anmeldung (nur wenn du eine am Apex eingerichtet hast):** aus. Lass das Passwort leer, wenn du keins festgelegt hast.
4. Tippe auf **Wasserwerte von APEX laden** und hak unter **Zu verfolgende Wasserwerte** die an, die du willst.
5. Stell die **Abfragehäufigkeit** ein. Lass sie nicht auf aus: Ohne Abfrage liest niemand den Apex, und seine Messwerte veralten.
6. Tippe auf **Weiter**, hak unter **Welche Becken versorgt dieser Apex?** jedes Becken an und tippe dann auf **Speichern**. Ein Apex kann mehr als ein Becken versorgen.

Findet der Scan nichts, prüf, ob dein Handy im selben WLAN ist wie der Apex, oder gib die IP-Adresse selbst ein.

Sobald er verbunden ist, wird jede Sonde, die dein Apex meldet, zu einer Quelle, die du auf ein Dashboard legen kannst. Steckdosen erscheinen als Steuerungen, und jedes eingebaute Erweiterungsmodul bekommt seine eigene Gerätekachel. Deine eigene Apex-Programmierung läuft genau so weiter, wie du sie eingerichtet hast. Was du steuern kannst, steht unter [Deine Ausrüstung steuern](/help/mobile-device-control#neptune-apex).

## Red Sea ReefBeat {#red-sea-reefbeat}

Cora spricht mit ReefBeat-Ausrüstung in deinem lokalen Netzwerk. Unterstützt werden **ReefDose**, **ReefATO+**, **ReefMat** und **ReefRun**.

1. Richte das Gerät zuerst in der ReefBeat-App von Red Sea ein und prüf, ob es im selben Netzwerk ist wie dein Handy.
2. Geh zu **Geräte → Gerät hinzufügen → Red Sea**. Cora durchsucht dein Netzwerk.
3. Wähl, zu welchem Becken jedes Gerät gehört.

Ein Red Sea-Gerät versorgt ein Becken. Wählst du ein anderes, wandert es dorthin.

Jedes Gerät bekommt seine eigene Geräteseite, und seine Messwerte werden zu Quellen. ReefDose meldet seine Köpfe und Behälter, ReefATO+ seinen Nachfüllbehälter und seine Befüllungen, ReefMat die Tage, die es noch hat, und ReefRun den Zustand seiner Pumpe. Was jede Seite dich tun lässt, steht unter [Deine Ausrüstung steuern](/help/mobile-device-control#red-sea).

## Jecod / Jebao {#jecod}

Cora verbindet sich mit Jecod-Pumpen und kann sie lesen und steuern. Füg eine über **Geräte → Gerät hinzufügen → Jecod** hinzu. Eine Jecod-Pumpe erreicht Cora auf einem von zwei Wegen, und das entscheidet, was du mit ihr tun kannst.

![Der Bildschirm zum Hinzufügen einer Pumpe in Cora Mobile, noch ohne gefundene Pumpen](img/mobile-connections.webp "Noch keine gesehen: Der Scan erklärt, was er braucht und warum eine Pumpe einen Durchgang verpassen kann.")

**Über dein Netzwerk.** Der Scan findet Pumpen, die sich selbst melden, du musst also keine Adresse eingeben. Eine Netzwerkpumpe kannst du lesen und steuern, solange sie Strom hat und erreichbar ist. Das heißt, dein Handy ist im selben Netzwerk, oder ein Cora Max in diesem Netzwerk leitet deine Befehle weiter. Bist du unterwegs und gibt es vor Ort kein Cora Max, kannst du eine Netzwerkpumpe sehen, aber nicht steuern.

:::note Eine Pumpe verpasst oft den ersten Scan
Pumpen antworten auf einen Scan und verpassen den nächsten. Steht deine nicht in der Liste, scanne noch einmal, bevor du entscheidest, dass sie nicht erreichbar ist.
:::

Findet eine Suche nichts, zeigt das Ergebnis die Adressen, die über WLAN geprüft wurden. Zeigt die Jebao-App eine andere Adresse für deine Pumpe, ist dein Handy in einem anderen Netzwerk. Ein Gast- oder IoT-Netzwerk oder ein reines 5-GHz-Band sieht diese Pumpen nicht. Auf dem iPhone braucht Cora außerdem Zugriff auf das lokale Netzwerk, um Pumpen in deinem WLAN zu sehen. Ohne ihn bleibt die Liste leer, ohne Fehlermeldung, deshalb erklärt das Ergebnis das und bietet **Einstellungen öffnen** an, um ihn wieder einzuschalten. Du kommst auch jederzeit über **Einstellungen → Gerätezugriff** dorthin, beschrieben unter [Cora Mobile-Einstellungen](/help/mobile-settings).

**Über Bluetooth.** Manche Pumpen lassen sich nur von einem Handy erreichen, das in ihrer Nähe steht. Die Seite der Pumpe sagt das und zeigt die letzten Einstellungen, die sie gelesen hat, und wie alt sie sind. Cora braucht dafür die Bluetooth-Berechtigung. Erteil sie, bevor du eine Bluetooth-Pumpe hinzufügst, sonst findet Cora die Pumpe gar nicht.

:::warning Du musst in der Nähe einer Bluetooth-Pumpe sein
Ihre Seite zeigt die letzten Einstellungen, die Cora gelesen hat, und wie lange das her ist. Etwas zu ändern, auch eine Futterpause zu starten, braucht die Pumpe in Reichweite. Stell dich in ihre Nähe und öffne die Seite noch einmal.
:::

Über beide Verbindungen bekommst du Live-Zustand, Modus und Intensität, eine Futterpause und ein Tagesprogramm. Eine Futterpause, die du auf dem Handy startest, braucht bei manchen Pumpen die geöffnete Seite der Pumpe. Die Details stehen unter [Deine Ausrüstung steuern](/help/mobile-device-control#jecod), und [Ausrüstung planen](/help/mobile-schedules) behandelt das Tagesprogramm.

## AquaWiz KH Controller {#aquawiz-kh-controller}

Cora liest die Alkalinität eines AquaWiz KH Controllers über dein AquaWiz-Konto, das funktioniert also auch unterwegs und braucht kein Cora Max.

1. Geh zu **Geräte → Gerät hinzufügen → AquaWiz**.
2. Gib deinen AquaWiz-Benutzernamen und dein Passwort ein und tippe auf **Verbinden**.
3. Wähl das Becken, prüf **Auch pH-Wert lesen** (es ist bei einem Gerät, das den pH-Wert meldet, zuerst eingeschaltet), und tippe auf **Mit Cora verknüpfen**.

Mit eingeschaltetem **Automatisch verbunden bleiben** behält Cora dein AquaWiz-Passwort und erneuert die Verbindung von selbst. Ist es aus, behält Cora nur ein Anmelde-Token, das AquaWiz etwa alle 30 Tage ablaufen lässt, und schickt dir eine Benachrichtigung, wenn du dich wieder anmelden musst.

Du bekommst die Alkalinität als Quelle, und auch den pH-Wert, wenn dein Gerät ihn meldet und **Auch pH-Wert lesen** an ist. Dein erster Messwert kommt, sobald du verknüpfst. Danach erlaubt AquaWiz Cora nur alle 12 Stunden, seine Cloud automatisch abzufragen. Ein Messwert von dort kann also bis zu etwa einen halben Tag alt sein. Ein Cora Max am Becken kann den Controller auch selbst jede Stunde auslesen, wenn er ihn erreicht. Öffne die Seite des Geräts, um zu sehen, wann jeder Messwert gemessen wurde und woher er kam, und tippe auf **Jetzt auslesen** für einen frischen (höchstens alle 15 Minuten). Was die AquaWiz-Karte zeigt und welche Warnungen es gibt, steht unter [Deine Ausrüstung steuern](/help/mobile-device-control#aquawiz).

:::warning Cora teilt deine AquaWiz-Anmeldung
AquaWiz vergibt pro Konto eine Anmeldung, deshalb nutzt Cora dieselbe wie die AquaWiz-App. Änderst du dein AquaWiz-Passwort, trennt sich Cora. Verbinde es danach über die Gerätezeile neu. Um Cora den Zugriff ganz zu entziehen, entferne das Gerät in Cora und ändere dein AquaWiz-Passwort.
:::


## Von Hand eintragen {#logging-by-hand}

Manche Wasserwerte kommen von einem Testkit, nicht von Ausrüstung. Um ein Ergebnis einzutragen, scroll ganz nach unten auf dem Dashboard und tippe auf **Wasserwerte protokollieren**.

Von Hand eingetragene Messwerte zählen genauso viel wie alle anderen. Sie erscheinen auf Widgets mit ihrer eigenen Quelle und ihrem eigenen Alter und fließen in Reef Buddy ein. Cora prüft auch deine Sonden gegen sie, wenn es dir sagt, dass sich zwei Quellen widersprechen.

## Wenn eine Verbindung nicht mehr funktioniert {#if-a-connection-stops-working}

Die Gerätezeile sagt dir, welche Art von Problem es ist. Schlag es in der Tabelle unter [Geräte hinzufügen, bearbeiten und entfernen](/help/mobile-devices#health) nach. Für alles, was dort nicht steht, siehe [Problembehebung](/help/troubleshooting).

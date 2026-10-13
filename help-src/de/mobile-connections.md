---
title: Deine Ausrüstung verbinden
description: So verbindest du ein Neptune Apex-, Red Sea ReefBeat-, Jecod- oder AquaWiz-Gerät und, in der Beta, Maxspect-, GHL-, HYDROS-, Focustronic- und Inkbird-Ausrüstung mit Cora.
section: Cora Mobile
reviewed: 2026-10-13
order: 12
group: Equipment
---

Diese Seite zeigt, wie du jede Marke mit Cora verbindest und was jede Verbindung braucht. Alle fangen gleich an: **Geräte → Gerät hinzufügen**, dann wählst du die Marke.

![Die Liste Gerät hinzufügen für einen Beta-Nutzer](img/mobile-add-device-beta.webp "Die Markenliste. Beta-Marken tragen einen Beta-Chip.")

Die mit *(Beta)* markierten Marken sind nur für Beta-Nutzer offen. Siehe [Beta-Funktionen](/help/mobile-beta).

| Marke | Öffnet | Ohne Cora Max |
|---|---|---|
| Cora | Einen Scan nach einem neuen Cora Max, über WLAN oder Bluetooth | |
| Neptune Apex | Einen Netzwerkscan oder seine IP-Adresse, dann die Becken, die er versorgt | Nur lokal |
| Red Sea | Einen Scan in deinem Netzwerk, dann das Becken, zu dem jedes Gerät gehört | Nur lokal |
| Jecod / Jebao | Einen Scan in deinem Netzwerk oder Bluetooth | Nur lokal |
| AquaWiz | Deine AquaWiz-Anmeldung | Funktioniert |
| Maxspect *(Beta)* | Denselben Scan wie Jecod | **Erfordert Cora Max** |
| GHL *(Beta)* | Seine Adresse, Schnittstelle und, bei einem mini, seine Anmeldung | **Erfordert Cora Max** |
| HYDROS *(Beta)* | Einen Geräteschlüssel aus der HYDROS-App | Funktioniert |
| Focustronic *(Beta)* | Deine Focustronic-Anmeldung, dann das Becken, zu dem jedes Gerät gehört | Funktioniert |
| EcoTech *(Beta)* | Einen Bluetooth-Scan nach Radion-Leuchten, VorTech-Pumpen und Versa-Dosierern. Siehe [EcoTech-Leuchten, -Pumpen und -Dosierer](/help/mobile-ecotech) | **Erfordert Cora Max** |
| Inkbird *(Beta)* | Einen Bluetooth-Scan nach deinem Raumluftmonitor | **Erfordert Cora Max** |
| Kamera *(Beta)* | Wyze, Tapo, Sonoff oder eine andere RTSP-Kamera. Siehe [Kameras und Skimmer-Wächter](/help/mobile-cameras) | **Erfordert Cora Max** |

## Ohne Cora Max: nur lokal {#local-only}

Neptune Apex-, Red Sea- und Jecod-Ausrüstung ist in deinem Heimnetz (oder über Bluetooth erreichbar). Hast du kein Cora Max (oder keins an dem Becken, zu dem du hinzufügst), sagt der Bildschirm zum Hinzufügen bei diesen Marken *Diese Integration funktioniert ohne Cora Max nur lokal in der Mobile-App.* Das heißt:

- Dein Handy liest und steuert die Ausrüstung, solange Cora Mobile im selben Netzwerk geöffnet ist oder in Bluetooth-Reichweite.
- Unterwegs siehst du die letzten Messwerte, die dein Handy gespeichert hat, und kannst sie nicht steuern.

Ein Cora Max am Becken fragt diese Ausrüstung rund um die Uhr ab und leitet deine Befehle weiter, wenn du unterwegs bist. AquaWiz, HYDROS und Focustronic werden über den eigenen Dienst des Herstellers erreicht, sie funktionieren also überall ohne Cora Max. Zeilen mit **Erfordert Cora Max** sind ausgegraut, bis das Becken eins hat. Mehr dazu unter [Mehr als ein Cora-Gerät](/help/mobile-multi-device).

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

Cora spricht mit ReefBeat-Ausrüstung in deinem lokalen Netzwerk. Unterstützt werden **ReefDose**, **ReefATO+**, **ReefMat** und **ReefRun**, dazu **ReefControl**, **ReefControl Power**, **ReefWave** und **ReefLED**, die *(Beta)* im Namen tragen, aber für alle offen sind.

1. Richte das Gerät zuerst in der ReefBeat-App von Red Sea ein und prüf, ob es im selben Netzwerk ist wie dein Handy.
2. Geh zu **Geräte → Gerät hinzufügen → Red Sea**. Cora durchsucht dein Netzwerk.
3. Wähl, zu welchem Becken jedes Gerät gehört.

Ein Red Sea-Gerät versorgt ein Becken. Wählst du ein anderes, wandert es dorthin.

Jedes Gerät bekommt seine eigene Geräteseite, und seine Messwerte werden zu Quellen. ReefDose meldet seine Köpfe und Behälter, ReefATO+ sein Reservoir und seine Befüllungen, ReefMat die Tage, die es noch hat, und ReefRun den Zustand seiner Pumpe. ReefControl meldet seine Sonden genauso. ReefWave und ReefLED zeigen vorerst nur ihren Modus. Was jede Seite dich tun lässt, steht unter [Deine Ausrüstung steuern](/help/mobile-device-control#red-sea).

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
Ihre Seite zeigt die letzten Einstellungen, die Cora gelesen hat, und wie lange das her ist. Etwas zu ändern, auch eine Fütterungspause zu starten, braucht die Pumpe in Reichweite. Stell dich in ihre Nähe und öffne die Seite noch einmal.
:::

Über beide Verbindungen bekommst du Live-Zustand, Modus und Intensität, eine Fütterungspause und ein Tagesprogramm. Eine Fütterungspause, die du auf dem Handy startest, braucht bei manchen Pumpen die geöffnete Seite der Pumpe. Die Details stehen unter [Deine Ausrüstung steuern](/help/mobile-device-control#jecod), und [Ausrüstung planen](/help/mobile-schedules) behandelt das Tagesprogramm.

## AquaWiz KH Controller {#aquawiz-kh-controller}

Cora liest die Alkalinität eines AquaWiz KH Controllers über dein AquaWiz-Konto, das funktioniert also auch unterwegs und braucht kein Cora Max.

1. Geh zu **Geräte → Gerät hinzufügen → AquaWiz**.
2. Gib deinen AquaWiz-Benutzernamen und dein Passwort ein und tippe auf **Verbinden**.
3. Wähl das Becken, schalte **Auch pH-Wert lesen** ein, wenn du willst, und tippe auf **Mit Cora verknüpfen**.

Mit eingeschaltetem **Automatisch verbunden bleiben** behält Cora dein AquaWiz-Passwort und erneuert die Verbindung von selbst. Ist es aus, behält Cora nur ein Anmelde-Token, das AquaWiz etwa alle 30 Tage ablaufen lässt, und schickt dir eine Benachrichtigung, wenn du dich wieder anmelden musst.

Du bekommst die Alkalinität als Quelle, so oft aktualisiert, wie dein Controller titriert, und auch den pH-Wert, wenn du ihn eingeschaltet hast und dein Gerät ihn meldet. Was die AquaWiz-Karte zeigt und ihre Warnung für den Zusatz stehen unter [Deine Ausrüstung steuern](/help/mobile-device-control#aquawiz).

:::warning Cora teilt deine AquaWiz-Anmeldung
AquaWiz vergibt pro Konto eine Anmeldung, deshalb nutzt Cora dieselbe wie die AquaWiz-App. Änderst du dein AquaWiz-Passwort, trennt sich Cora. Verbinde es danach über die Gerätezeile neu. Um Cora den Zugriff ganz zu entziehen, entferne das Gerät in Cora und ändere dein AquaWiz-Passwort.
:::

## Maxspect {#maxspect}

:::note Beta
**Beta.** Maxspect ist in der Beta und nur für Beta-Nutzer offen. Wenn du kein Beta-Nutzer bist, siehst du es nicht unter **Gerät hinzufügen**. Für Beta-Zugang wende dich an den [Support](/support.html). Manche Steuerungen können eingeschränkt sein, und was du hier siehst, kann sich mit Updates ändern. Funktioniert etwas nicht wie beschrieben, sag es uns über [Ein Problem melden](/help/mobile-support).
:::

Cora verbindet sich mit Maxspect Gyre-Pumpen und kann sie lesen und steuern. Füg eine über **Geräte → Gerät hinzufügen → Maxspect** hinzu, mit demselben Scan wie Jecod. Sie braucht ein Cora Max am Becken. Ohne eins zeigt die Zeile **Erfordert Cora Max**.

Beim Hinzufügen muss eine Gyre im selben Netzwerk sein wie dein Handy. Danach erreicht Cora Mobile sie über das Cora Max des Beckens, auch wenn du unterwegs bist. Wellenmuster, Geschwindigkeit, der Zeitplan und **Pumpenzustand** stehen unter [Deine Ausrüstung steuern](/help/mobile-device-control#maxspect).

## GHL ProfiLux und Mitras {#ghl-profilux-and-mitras}

:::note Beta
**Beta.** GHL ist in der Beta und nur für Beta-Nutzer offen. Wenn du kein Beta-Nutzer bist, siehst du es nicht unter **Gerät hinzufügen**. Für Beta-Zugang wende dich an den [Support](/support.html). Manche Messwerte oder Steuerungen funktionieren vielleicht noch nicht. Funktioniert etwas nicht wie beschrieben, sag es uns über [Ein Problem melden](/help/mobile-support).
:::

Cora liest einen GHL ProfiLux- oder Mitras-Controller: Sonden, Steckdosen, Dosierer, Füllstandssensoren und, bei den Director-Modellen, KH- und Ionen-Testergebnisse.

1. Geh zu **Geräte → Gerät hinzufügen → GHL**. Es braucht ein Cora Max am Becken und zeigt ohne eins **Erfordert Cora Max**.
2. Dein Handy kann nicht danach scannen, gib also seine Adresse ein und wähl die Schnittstelle selbst: **Offizielle API**, **HTTP** oder **ProfiLux mini** (der außerdem seine Anmeldung braucht).
3. Wähl, zu welchem Becken er gehört. Ein GHL-Controller kann mehr als ein Becken versorgen.

Ein GHL-Controller spricht nicht direkt mit deinem Handy. Er zeigt **Wartet auf Cora Max**, bis ein Cora Max in seinem Netzwerk ihn gelesen hat, dann erscheinen seine Messwerte und Steuerungen überall.

Die GHL-API muss eingeschaltet sein, damit Cora den Controller überhaupt erreicht. GHL schaltet sie nach jedem Firmware-Update aus, prüf das also zuerst, wenn nichts erscheint. Die [Problembehebung](/help/troubleshooting) sagt, was zu tun ist. Die Steuerung steht unter [Deine Ausrüstung steuern](/help/mobile-device-control#ghl).

## HYDROS {#hydros}

:::note Beta
**Beta.** HYDROS ist in der Beta und nur für Beta-Nutzer offen. Wenn du kein Beta-Nutzer bist, siehst du es nicht unter **Gerät hinzufügen**. Für Beta-Zugang wende dich an den [Support](/support.html). Manche Messwerte oder Steuerungen funktionieren vielleicht noch nicht. Funktioniert etwas nicht wie beschrieben, sag es uns über [Ein Problem melden](/help/mobile-support).
:::

Bei HYDROS müssen dein Handy und dein Controller nicht im selben Netzwerk sein, und du brauchst kein Cora Max. Cora erreicht ihn über die eigene Cloud von HYDROS, deshalb funktioniert er auch unterwegs und sogar bei geschlossenem Cora Mobile.

1. Leg in der HYDROS-App einen **Geräteschlüssel** für den Anbieter **cora-iq** an. Wähl **Lesen**, wenn du nur seine Messwerte willst, oder **Schreiben**, wenn du ihn auch von Cora aus steuern willst.
2. Geh in Cora Mobile zu **Geräte → Gerät hinzufügen → HYDROS**. Der Bildschirm heißt **HYDROS hinzufügen (Beta)**.
3. Füg den Schlüssel in **HYDROS-Geräteschlüssel** ein, tippe auf **Schlüssel prüfen**, wähl das Becken und tippe auf **Verknüpfen**.

Sobald er verknüpft ist, importiert Cora die letzten 33 Tage seines Verlaufs und liest von da an weiter. [Deine Ausrüstung steuern](/help/mobile-device-control#hydros) behandelt, was du lesen und, mit einem Schreibschlüssel, steuern kannst.

## Focustronic {#focustronic}

:::note Beta
**Beta.** Focustronic ist in der Beta und nur für Beta-Nutzer offen. Wenn du kein Beta-Nutzer bist, siehst du es nicht unter **Gerät hinzufügen**. Für Beta-Zugang wende dich an den [Support](/support.html).
:::

Cora liest Focustronic Alkatronic-, Dosetronic- und Mastertronic-Geräte über dein Focustronic-Konto, das funktioniert also auch unterwegs und braucht kein Cora Max.

1. Geh zu **Geräte → Gerät hinzufügen → Focustronic** und melde dich mit demselben Konto an, das du in der Focustronic-App nutzt.
2. Wähl, zu welchem Becken jedes Gerät gehört, und tippe dann auf **Mit Cora verknüpfen**.

**Angemeldet bleiben** lässt Cora dein Focustronic-Passwort verschlüsselt behalten und sich von selbst wieder anmelden. Schaltest du es aus, behält Cora nur eine vorübergehende Anmeldung und schickt dir eine Benachrichtigung, wenn du dich wieder anmelden musst. Lehnt Focustronic die Anmeldung ab, öffne **Focustronic hinzufügen** und melde dich erneut an.

Was jedes Gerät zeigt, und **Jetzt messen**, **Jetzt dosieren** und **Jetzt testen**, stehen unter [Deine Ausrüstung steuern](/help/mobile-device-control#focustronic).

## Inkbird-Raumluftmonitor {#inkbird-room-air-monitor}

:::note Beta
**Beta.** Inkbird ist in der Beta und nur für Beta-Nutzer offen. Wenn du kein Beta-Nutzer bist, siehst du es nicht unter **Gerät hinzufügen**. Für Beta-Zugang wende dich an den [Support](/support.html).
:::

Cora liest einen Inkbird-Raumluftmonitor IAM-T1 oder IAM-T2. Ein Cora Max am Becken liest ihn über Bluetooth, und Cora schreibt nie etwas auf den Monitor. Die Zeile zeigt **Erfordert Cora Max**, bis das Becken eins hat.

1. Geh zu **Geräte → Gerät hinzufügen → Inkbird**. Cora sucht nach Monitoren in der Nähe. Bluetooth muss eingeschaltet sein, mit Berechtigung für Cora.
2. Wähl deinen und tippe auf **Mit Becken verknüpfen**. Erscheint keiner, geh näher heran und tippe auf **Erneut suchen**.

Die Seite des Monitors zeigt seinen letzten Messwert. **Messintervall** legt fest, wie oft ein Cora Max ihn liest. Bis ein Cora Max ihn gelesen hat, steht auf der Seite **Warte auf Cora Max**. Wird er still, zeigt sie **Meldet nicht**, und Cora warnt dich. Raumwerte fließen auch in [Reef Buddy](/help/mobile-reef-buddy) ein. Um aufzuhören, tippe auf **Verknüpfung lösen**. Cora Max liest ihn dann nicht mehr, und der Verlauf bleibt.

## Von Hand eintragen {#logging-by-hand}

Manche Wasserwerte kommen von einem Testkit, nicht von Ausrüstung. Um ein Ergebnis einzutragen, scroll ganz nach unten auf dem Dashboard und tippe auf **Wasserwerte protokollieren**.

Von Hand eingetragene Messwerte zählen genauso viel wie alle anderen. Sie erscheinen auf Widgets mit ihrer eigenen Quelle und ihrem eigenen Alter und fließen in Reef Buddy ein. Cora prüft auch deine Sonden gegen sie, wenn es dir sagt, dass sich zwei Quellen widersprechen.

## Wenn eine Verbindung nicht mehr funktioniert {#if-a-connection-stops-working}

Die Gerätezeile sagt dir, welche Art von Problem es ist. Schlag es in der Tabelle unter [Geräte hinzufügen, bearbeiten und entfernen](/help/mobile-devices#health) nach. Für alles, was dort nicht steht, siehe [Problembehebung](/help/troubleshooting).

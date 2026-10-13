---
title: Deine Ausrüstung steuern
description: Die Seite eines Geräts öffnen, um seinen Live-Zustand zu sehen und Steckdosen, Pumpen, Dosierköpfe und Tester zu schalten, Marke für Marke.
section: Cora Mobile
reviewed: 2026-10-13
order: 13
group: Equipment
twin: max-device-control
---

Auf der eigenen Seite eines Geräts siehst du seinen Live-Zustand und änderst, was es tut. Öffne sie über **Geräte** → auf das Gerät tippen, oder tippe auf seine Kachel auf dem Dashboard.

![Eine ReefATO+-Seite in Cora Mobile](img/mobile-device-detail.webp "Status, die heutigen Messwerte und der Wasserstand, dann Leck, Befüllungen und Sondenkalibrierung.")

Jede Geräteseite ist gleich aufgebaut. Name und Details stehen oben, dann eine Reihe von Live-Messwerten, jeder Zustand, den das Gerät meldet, und seine Steuerungen. Die Glocke in der Titelleiste legt Warnschwellen für dieses Gerät fest, wie unter [Verbrauchsmaterial und Nachfüllwarnungen](/help/mobile-consumables) beschrieben. Wie du ein Gerät überhaupt hinzufügst, steht unter [Deine Ausrüstung verbinden](/help/mobile-connections).

Spring zu deiner Ausrüstung: [Neptune Apex](#neptune-apex) · [Trident](#trident) · [DŌS](#dos) · [Red Sea](#red-sea) · [ReefDose](#reefdose) · [ReefRun](#reefrun) · [ReefMat](#reefmat) · [ReefATO+](#reefato) · [Dosierer-Warnungen](#doser-alerts) · [Jecod](#jecod) · [AquaWiz](#aquawiz) · [Maxspect](#maxspect) · [GHL](#ghl) · [HYDROS](#hydros) · [Focustronic](#focustronic) · [EcoTech, Inkbird und Kameras](#ecotech-inkbird-cameras)

:::warning Diese Steuerung wirkt auf laufende Ausrüstung
Es gibt keine Vorschau und kein Rückgängig. Manche Steuerungen bitten dich vorher um Bestätigung.
:::

## Was passiert, wenn du einen Befehl schickst {#what-happens-when-you-send-a-command}

Ein Befehl kommt nicht immer durch. Cora sagt dir, welche von vier Möglichkeiten passiert ist:

| Ergebnis | Bedeutung |
|---|---|
| **Bestätigt** | Die Ausrüstung hat die Änderung angenommen und ihren neuen Zustand gemeldet |
| **Unbestätigt** | Der Befehl ging raus, aber es kam keine Rückmeldung. **Das heißt "wir wissen es nicht". Es heißt nicht, dass es geklappt hat.** Prüf den eigenen Zustand des Geräts |
| **Abgelehnt** | Etwas hat ihn abgelehnt (eine Sicherheitsregel, eine Sperre oder die Ausrüstung selbst), oder kein Cora-Gerät hat ihn rechtzeitig aufgenommen. Er wurde abgebrochen, und es wurde nichts ausgeführt |
| **Keine Änderung** | Die Ausrüstung war schon so eingestellt, wie du es wolltest |

Jedes Ergebnis wird unter [Aktivität](/help/mobile-activity) festgehalten, zusammen mit seinem Auslöser.

Ohne Cora Max am Becken funktioniert Neptune Apex-, Red Sea- und Jecod-Ausrüstung nur lokal: Dein Handy muss im selben Netzwerk sein (oder in Bluetooth-Reichweite), um einen Befehl zu schicken. Mit einem Cora Max am Becken schickt Cora Mobile ihn über dieses Cora Max, auch wenn du nicht zu Hause bist.

## Neptune Apex {#neptune-apex}

![Eine Apex-Seite in Cora Mobile, mit Status, Trident- und DŌS-Modulen, Parameterzuordnung und dem Becken, das er versorgt](img/mobile-apex.webp "Die Apex-Seite: Status, Module, Parameterzuordnung und Becken.")

Die Apex-Seite zeigt den Status des Controllers, dann **Module**, **Parameterzuordnung** und **Becken**.

- **Module** listet jeden eingebauten Trident und DŌS auf. Tippe auf einen, um seine eigene Seite zu öffnen.
- **Parameterzuordnung** ist, wo du wählst, was jede Sonde liefert. Sonden melden sich in Cora als Quellen, und du kannst sie auf ein Dashboard legen. Siehe [Parameterzuordnung und Sonden](/help/mobile-probes).
- **Becken** zeigt, welche Becken der Apex versorgt. Tippe auf **Ändern**, um sie zu bearbeiten.
- **Steckdosen** schaltest du über ein Widget **Steckdose** auf dem Dashboard zwischen **Auto**, **Aus** und **Ein**. Auto gibt die Steuerung an deine Apex-Programmierung zurück. Siehe [Widget-Referenz](/help/mobile-widgets#outlet).

Dein Apex führt weiter seine eigene Programmierung aus. Cora ändert eine Steckdose nur, wenn du darum bittest.

## Trident {#trident}

Die Trident-Seite zeigt den aktuellen Teststatus und den Stand von Reagenz und Abwasser. Du kannst hier einen Test starten.

Du kannst auch eine Warnung für die verbleibenden Tests und für die Abfallflasche festlegen, damit Cora dich warnt, bevor das Reagenz ausgeht oder die Flasche voll ist. Siehe [Verbrauchsmaterial und Nachfüllwarnungen](/help/mobile-consumables).

## DŌS {#dos}

![Eine DŌS-Seite, die meldet, dass der DŌS am AquaBus nicht antwortet, mit seiner letzten Reichweite, der heutigen Dosierung und dem Tagesplan, dann die Zeile Warnungen](img/mobile-dos.webp "Ein DŌS, der nicht am AquaBus ist: Die Seite zeigt seine letzten bekannten Zahlen, eine Karte Braucht Aufmerksamkeit und die Zeile Warnungen.")

Ein DŌS QD funktioniert genau wie ein DŌS, und alles hier gilt für beide. Wenn ein Cora Max deinen Apex abfragt, erscheinen Dosierköpfe auf der DŌS-Seite. In der Steckdosenliste erscheinen sie nie.

Jeder Dosierkopf zeigt, was er dosiert, seinen Zeitplan, was er heute dosiert hat und wie viel im Behälter übrig ist. Außerdem zeigt er die **Reichweite**, also wie viele Tage das bei der aktuellen Rate reicht.

Antwortet der DŌS nicht mehr am AquaBus, zeigt seine Seite **Nicht am Bus** und eine Karte **Braucht Aufmerksamkeit**. Die Zahlen auf der Seite sind dann die zuletzt gemeldeten, nicht das, was er gerade tut. Prüf das AquaBus-Kabel des Moduls und den Apex.

Für jeden Kopf kannst du:

- seinen Zeitplan **Pausieren** und **Fortsetzen**
- **Befüllen**, um Cora zu sagen, dass der Behälter wieder voll ist, oder einzustellen, wie viel drin ist (**Gesamtvolumen** ist die Größe des Behälters, **Verbleibendes Volumen** ist, was jetzt drin ist, und **Voll** setzt das eine auf das andere)
- **Jetzt dosieren**, für eine abgemessene Dosis von Hand

:::note Zeitpläne bearbeitest du in Apex Fusion
Cora zeigt den Zeitplan und verfolgt, was dosiert wurde, ändert den Zeitplan aber nicht. Zeitplan, Dosierrate und Zahl der Dosierungen bearbeitest du in der Apex Fusion-App. Pausieren, Befüllen und Dosieren von Hand funktionieren hier.
:::

:::note Miss einen Kopf, bevor du von Hand dosierst
Cora dosiert mit einem Kopf erst von Hand, wenn er gemessen wurde. **Zum Dosieren messen** und **Erneut messen** gibt es auf dem Cora Max, das für das Becken dosiert. Cora lässt den Kopf zwanzig Sekunden laufen, du misst, was herausgekommen ist, und Cora berechnet die echte Rate des Kopfes. Eine Messung gilt für jedes Cora Max und Cora Mobile. Miss jeden Kopf einmal, und noch einmal, nachdem du seinen Schlauch gewechselt hast.
:::

:::warning Ein DŌS dosiert weiter, wenn sein Behälter leer ist
Das Gerät hat keinen Füllstandssensor und hört nicht von selbst auf. Leg für jeden Kopf unter **Warnungen** auf der DŌS-Seite eine Nachfüllwarnung fest, damit Cora dich warnt, bevor der Behälter leer läuft. Siehe [Dosierer-Warnungen](#doser-alerts).
:::

### Wofür jeder Kopf verwendet wird {#dos-head-use}

Gib jedem Kopf einen **Verwendungstyp**, damit Cora weiß, was er tut, und richtig darüber spricht. Zur Wahl stehen **Supplement**, **Wasserwechsel: neues Salzwasser rein**, **Wasserwechsel: altes Wasser raus**, **Kalkwasser**, **Calciumreaktor**, **Futter**, **Nachfüllen** und **Andere**. Stell ihn unter **Verwendet für** in den Einstellungen des Kopfes ein.

Die beiden Wasserwechsel-Typen gehören in **Paare**. Stell bei einem Kopf **Gekoppelter Kopf** auf den Kopf, der Wasser in die andere Richtung bewegt, dann behandelt Cora die beiden als ein Wasserwechsel-Paar.

Ein Behälter kann bei jedem Verwendungstyp bis zu 1.000 l groß sein. Der Apex selbst zählt nur bis 150 l, darüber verfolgt Cora den Behälter also selbst anhand dessen, was der Kopf dosiert. Gib beim Einrichten das **Gesamtvolumen** ein. Cora setzt außerdem ab und zu den eigenen Zähler des Apex zurück, und die Aktivität zeigt das als *Den eigenen Zähler des Apex auf 150 L zurückgesetzt*.

Jeder Kopf hat außerdem eine Grenze **Größte manuelle Dosierung**, damit ein Tippfehler aus einer Handdosierung nicht etwas viel Größeres macht, als du wolltest. Große Handdosierungen werden erst verfügbar, nachdem die Rate des Kopfes am Becken mit einem echten Test gemessen wurde und du **Große Dosierungen (Beta)** in den Einstellungen des Kopfes eingeschaltet hast. Standardmäßig ist es aus. Schalte es erst ein, nachdem du die erste große Dosierung am Becken beobachtet hast.

## Red Sea ReefBeat {#red-sea}

Jedes Red Sea-Gerät hat eine Seite, die zu dem passt, was es tut:

| Gerät | Die Seite zeigt | Du kannst |
|---|---|---|
| [ReefDose](#reefdose) | Jeden Kopf, seinen Behälter und was er dosiert hat | Dosieren, die Tagesdosis ändern, den **Dosierplan (Beta)** bearbeiten |
| [ReefRun](#reefrun) | Geschwindigkeit und Zustand der Rückförder- und Abschäumerpumpe | Geschwindigkeit ändern, eine Pumpe schalten, den **Pumpenplan (Beta)** bearbeiten |
| [ReefMat](#reefmat) | Verbleibende Rolle, in Tagen und Metern | Die Matte vorschieben, **ReefMat-Einstellungen (Beta)** festlegen, eine neue Rolle eintragen |
| [ReefATO+](#reefato) | Füllstand des Reservoirs und Nachfüllaktivität | Eine Reservoir-Warnung festlegen |
| **ReefControl** *(Beta)* | Seine Sonden für Temperatur, pH, Salinität und ORP | Seine Messwerte ansehen |
| **ReefWave**, **ReefLED** *(Beta)* | Seinen aktuellen Modus | Vorerst nur ansehen |

ReefControl, ReefControl Power, ReefWave und ReefLED tragen *(Beta)* im Namen, sind aber für alle offen. Siehe [Beta-Funktionen](/help/mobile-beta).

Die Anschlüsse von **ReefControl Power** *(Beta)* erscheinen als Steckdosen und werden mit derselben Steckdosensteuerung geschaltet wie eine Apex-Steckdose, nur ein oder aus. Einen Automatikmodus gibt es für sie noch nicht.

Bist du nicht im Netzwerk des Geräts, schickt Cora Mobile Red Sea-Befehle über ein Cora Max am Becken. Kann das kein Cora Max, sagt die Seite das, und es wird nichts gesendet.

## ReefDose {#reefdose}

![Eine ReefDose 4-Seite in Cora Mobile](img/mobile-reefdose.webp "Status, Köpfe und heutige Gesamtmenge, Dosierer für Verbrauch nutzen, dann jeder Dosierkopf.")

Für jeden Kopf kannst du **Dosierung pro Tag** und **Rest in der Flasche** einstellen, **Jetzt dosieren** ausführen und **Zeitplan aktivieren**. Nachfüllwarnungen legst du pro Kopf mit der Glocke fest, wie unter [Dosierer-Warnungen](#doser-alerts) beschrieben.

Der Bereich **Dosierung** zeigt **Anstehende Dosierungen**, was jeder Kopf heute dosiert hat (**Heute bisher dosiert**) und **Dosiert pro Kopf** für die **Letzte 7 Tage** oder **Gesamt**. Cora liest das, solange ein Cora Max oder dein Handy in deinem Heimnetz ist.

### Einen Dosierplan bearbeiten *(Beta)* {#reefdose-plan}

Tippe auf einer ReefDose-Seite auf das Kalendersymbol, um den **Dosierplan (Beta)** zu öffnen.

Ein Plan ist eine Tagesmenge, aufgeteilt in bis zu vier Zeitfenster. Jedes Fenster hat eine Start- und Endzeit, wie viele Dosierungen es abgeben soll, und eine Geschwindigkeit: **Flüster**, **Normal** oder **Schnell**. Füg Fenster hinzu und entferne sie, dann speichere. Cora zeigt dir, was du gleich schickst, und bittet dich um Bestätigung, bevor es den ganzen Plan des Kopfes ersetzt.

Der Editor liest zuerst den Plan, der schon auf dem Gerät ist, du bearbeitest also den echten und kein leeres Formular.

## ReefRun {#reefrun}

ReefRun steuert Rückförder- und Abschäumerpumpen. Es ist keine Strömungspumpe. Du kannst die Geschwindigkeit einer Pumpe ändern, sie ein- oder ausschalten und Abschäumer-Einstellungen anpassen.

Tippe auf das Kalendersymbol, um den **Pumpenplan (Beta)** zu öffnen. Ein Programm hat bis zu sechs Abschnitte an einem Pumpenanschluss. Jeder Abschnitt hat eine Startzeit und eine Geschwindigkeit und kann einen kurzen Puls hinzufügen. Die Geschwindigkeit ist entweder 0 oder ab 5 %. Wie beim ReefDose-Plan liest er zuerst das Programm auf dem Gerät, und **Speichern** bittet um Bestätigung, bevor es das ganze Programm der Pumpe ersetzt.

## ReefMat {#reefmat}

Die ReefMat-Seite zeigt, wie viel Rolle übrig ist, in Tagen und Metern. Tippe auf **Jetzt vorschieben**, um die Matte von Hand weiterzuschieben. Cora fragt zuerst **Die Matte jetzt vorschieben?** Du kannst auch eine Nachfüllwarnung für die Rolle festlegen.

Tippe auf das Zahnrad für **ReefMat-Einstellungen (Beta)**:

- **Geplanter Vorschub** schaltet einen Vorschub zu festen Zeiten ein, getrennt vom Sensor für den automatischen Vorschub, der schon auf der Seite ist. Schalte ihn ein und leg fest, wie oft und wie weit jeder Vorschub die Matte bewegt.
- **ReefMat-Modell** und **Motorposition** (**Links** oder **Rechts**) sagen Cora, welches Gerät und welche Ausrichtung du hast.

Nachdem du eine neue Rolle eingelegt hast, sag es Cora mit **Neue Rolle (Beta)**: ihre Dicke und, wenn du ihn kennst, ihren Außendurchmesser. **Jetzt vorschieben** bewegt nur die Matte, die schon eingelegt ist.

## ReefATO+ {#reefato}

Die ReefATO+-Seite zeigt den Füllstand des Reservoirs und die letzten Nachfüllungen. Leg mit der Glocke eine Reservoir-Warnung fest. Cora schätzt aus dem jüngsten Nachfüllverbrauch, wie viele Tage das Reservoir noch reicht, und du kannst auch den Assistenten danach fragen.

## Wenn sich ein Red Sea-Gerät selbst stoppt {#red-sea-stops}

Ein Gerät kann sich selbst stoppen. Eine ReefRun-Pumpe tut das zum Beispiel, wenn der Abschäumerbecher voll ist. Passiert das, sagt die Seite, warum, und bietet die Lösung an:

| Gerät | Die Seite sagt | Tippe auf |
|---|---|---|
| ReefRun | Welche Pumpe gestoppt hat und warum, zum Beispiel, dass der Becher voll ist und du ihn leeren und dann fortsetzen sollst | **Fortsetzen** |
| ReefRun oder ReefMat | **Notstopp** | **Notstopp aufheben** |
| ReefMat | **Matte blockiert**, **Installationsfehler** oder **Einrichtungsfehler** | **Fortsetzen** |
| ReefMat | *Lege eine neue Rolle ein und bestätige es dann in der App von Red Sea.* | **Ich habe bereits eine neue Rolle eingelegt** |
| ReefMat | **Sensor muss gereinigt werden** | **Sensor gereinigt** |
| ReefDose | **Kopf-Fehlfunktion**, mit dem Namen des Kopfes | **Zurücksetzen** |
| ReefATO+ | **Fehler löschen** | **Fortsetzen** |

Manche davon bitten dich vorher um Bestätigung. Außerhalb des Netzwerks des Geräts laufen sie über ein Cora Max am Becken, wie unter [Red Sea ReefBeat](#red-sea) beschrieben.

## Dosierer-Warnungen {#doser-alerts}

Ein DŌS und ein ReefDose haben ihre Warnungen auf ihrer eigenen Seite. Der Tab **Regeln** der [Warnzentrale](/help/mobile-alerts) hat pro Dosierer eine Zeile, die sie öffnet, und die Taste **Dosierer öffnen** einer Dosierer-Warnung bringt dich ebenfalls hierher.

Tippe auf einer DŌS-Seite auf die Karte **Warnungen** (oder die Glocke in der Titelleiste). Das Fenster listet jeden Kopf auf, und für jeden kannst du festlegen:

- *[Kopf] · Tage übrig*, zum Beispiel *Jod · Tage übrig*: Du bekommst eine Warnung, wenn der Vorrat für weniger als so viele Tage reicht
- *[Kopf] · verbleibend*: Du bekommst eine Warnung, wenn weniger als so viel im Behälter ist
- **Verbleibender Platz im Abfallbehälter**, für einen Kopf, der altes Wasser abpumpt: Du bekommst eine Warnung, wenn der Abfallbehälter voll wird
- **Warnungen bei verpasster Dosierung**: ein Schalter, der dir meldet, wenn der Kopf eine geplante Dosierung verpasst

Jeder Schwellenwert hat seinen eigenen Schalter, du kannst also einen ausschalten und seinen Wert behalten. Tippe auf **Speichern**, wenn du fertig bist.

Tippe auf einer ReefDose-Seite auf die Glocke in der Titelleiste. Jeder Kopf hat seinen eigenen Schwellenwert für die verbleibenden Tage und seinen eigenen Schalter.

Standardwerte und anderes Verbrauchsmaterial stehen unter [Verbrauchsmaterial und Nachfüllwarnungen](/help/mobile-consumables).

## Jecod / Jebao-Pumpen {#jecod}

Die Pumpenseite zeigt das aktuelle Wellenmuster (Modus) und die Intensität, und du kannst beides ändern. Wähl oben **Den ganzen Tag gleich** oder **Zeitplan**. Wie du ein Tagesprogramm baust und es kopierst, speicherst oder teilst, steht unter [Ausrüstung planen](/help/mobile-schedules).

Gehört die Pumpe zu einer Gruppe, zeigt die Seite ihre Rolle, etwa **Führt die Gruppe an**, **Folgt: im Gleichschritt** oder **Folgt: wechselnd**.

### Fütterungspause {#jecod-feeding}

Starte eine Fütterungspause im Bereich **Fütterung** auf der Seite der Pumpe. Manche Pumpen beenden die Pause selbst, und die Seite sagt *Die Pumpe beendet das von selbst.*

:::warning Lass die Seite der Pumpe während einer Fütterungspause offen
Manche Pumpen beenden eine Fütterung nicht von selbst, und die Seite sagt das. Bei diesen, und bei jeder Pumpe mit Zeitplan, holt Cora Mobile das Wellenmuster und den Zeitplan nur zurück, solange die Seite der Pumpe offen bleibt. Verlässt du die Seite, bleibt die Pumpe im Fütterungsmodus gestoppt oder außerhalb ihres Zeitplans, bis du sie wieder änderst oder auf **Zeitplan** tippst.
:::

Eine Bluetooth-Pumpe muss in Reichweite deines Handys sein, um eine Fütterung zu starten, und eine Netzwerkpumpe muss in deinem Netzwerk sein.

### Fehlerprüfungen {#jecod-fault-checks}

**Fehlerprüfungen** legt fest, wie oft Cora die Pumpe erneut liest, damit es dich vor einem Fehler warnen kann, etwa einer blockierten oder trocken laufenden Pumpe. Stellst du es auf aus, hören diese Warnungen für diese Pumpe auf. Fehlerprüfungen brauchen ein Cora Max am Becken. Deine Wahl wird gespeichert, und die Prüfungen beginnen, sobald eins hinzugefügt wird. **Für jede Pumpe an diesem Becken verwenden** kopiert die Einstellung auf alle.

## AquaWiz {#aquawiz}

Die AquaWiz-Karte zeigt deine Alkalinitäts-Messwerte und den pH-Wert, wenn dein Gerät ihn meldet. Außerdem zeigt sie deinen KH-Zielwert, deine Dosierstärke und, bei einem Gerät mit eingerichteter Dosierung, seine maximale Dosis pro Stunde und wie viel Alkalinitäts-Zusatz noch im Behälter ist. Diese Werte kommen direkt aus deinen AquaWiz-Einstellungen, ändere sie also in der AquaWiz-App. Cora kann einen AquaWiz nicht steuern.

Erfasst dein Gerät seinen Behälter, warnt dich Cora, wenn der Zusatz zur Neige geht, standardmäßig bei 100 ml. Ändere das an seiner Regel in der [Warnzentrale](/help/mobile-alerts).

## Maxspect {#maxspect}

:::note Beta
**Beta.** Maxspect ist in der Beta und nur für Beta-Nutzer offen. Wenn du kein Beta-Nutzer bist, siehst du es nicht unter **Gerät hinzufügen**. Für Beta-Zugang [wende dich an den Support](/support.html). Manche Steuerungen können eingeschränkt sein, und was du hier siehst, kann sich mit Updates ändern. Funktioniert etwas nicht wie beschrieben, sag es uns über [Ein Problem melden](/help/mobile-support). Mehr dazu unter [Beta-Funktionen](/help/mobile-beta).
:::

Die Gyre-Seite zeigt, ob die Gyre läuft, Wellenmuster und Geschwindigkeit von **Gyre A** und **Gyre B** und wann sie zuletzt gelesen wurden. Von hier aus kannst du:

- Die Gyre mit dem Schalter neben ihrem Zustand ein- oder ausschalten. Cora bittet dich vorher um Bestätigung. Ausschalten stoppt beide Gyres und lässt den Zeitplan in Ruhe.
- Auf **Einstellungen ändern** tippen, um Wellenmuster und Pumpengeschwindigkeit jeder Gyre einzustellen, dazu die Dauer bei Mustern, die eine haben, und ob die beiden Gyres verbunden sind. Cora listet auf, was sich ändert, und bittet um Bestätigung. Wechselbetrieb stellst du in der Maxspect-App ein, und eine Gyre im Wechselbetrieb behält ihre Rampen und Haltezeiten.
- Auf **Programm festlegen** tippen, wenn das auf der Gyre gespeicherte Programm nicht gelesen werden kann. Es stellt beide Gyres so ein, dass die Gyre wieder starten kann.
- Das Tagesprogramm der Gyre auf der Karte **Zeitplan** sehen. Hier kannst du es nur ansehen. Den Zeitplan stellst du in der Maxspect-App ein.
- Den **Pumpenzustand** prüfen. Er zeigt, wann die Pumpe als Nächstes gereinigt werden muss (die Pumpe zählt das selbst herunter), den Strom an Kopf A, welche Köpfe verbaut sind und die Firmware. Tippe auf **Lesen**, um ihn abzurufen.

:::note Wie Cora Mobile eine Gyre erreicht
Versorgt ein Cora Max das Becken, geht Cora Mobile über dieses Cora Max, auch wenn du nicht zu Hause bist. **Einstellungen ändern** beginnt dann mit dem letzten Messwert dieses Cora Max. Andernfalls spricht dein Handy direkt mit der Gyre und muss in ihrem Netzwerk sein. Das Öffnen der Seite liest die Gyre. Zeigt die Seite einen älteren gespeicherten Messwert, bleibt **Einstellungen ändern** ausgeblendet, bis du auf Aktualisieren tippst.
:::

## GHL ProfiLux und Mitras {#ghl}

:::note Beta
**Beta.** GHL ist in der Beta und nur für Beta-Nutzer offen. Wenn du kein Beta-Nutzer bist, siehst du es nicht unter **Gerät hinzufügen**. Für Beta-Zugang [wende dich an den Support](/support.html). Manche Messwerte oder Steuerungen funktionieren vielleicht noch nicht, und was du hier siehst, kann sich mit Updates ändern. Funktioniert etwas nicht wie beschrieben, sag es uns über [Ein Problem melden](/help/mobile-support). Mehr dazu unter [Beta-Funktionen](/help/mobile-beta).
:::

Die Seite des Controllers zeigt seine Sonden, Steckdosen, Dosierer und Füllstandssensoren und, bei den Director-Modellen, seine KH- und Ionen-Testergebnisse.

Die Steuerung bleibt aus, bis du **Steuerung durch Cora zulassen (Beta)** auf der Seite des Geräts einschaltest. Standardmäßig ist es aus, und das Einschalten lässt Cora Befehle für Fütterungspause, Wartung, Wasserwechsel, Gewitter, Beleuchtung, Sollwerte und Steckdosen an diesen Controller schicken. Sobald du das Gerät hinzufügen kannst, braucht dieser Schalter keinen zusätzlichen Zugang.

Ist es eingeschaltet:

- Eine Steckdose kann auf **Immer ein**, **Immer aus** oder **Zurück zu automatisch** gestellt werden, um sie an die eigene Programmierung des Controllers zurückzugeben.
- Ein Sollwert, etwa Temperatur oder pH, zeigt seinen erlaubten Bereich und lehnt einen Wert außerhalb davon ab.

:::warning Eine Änderung an Steckdose oder Sollwert wird auf dem Controller selbst gespeichert
Sie wird nicht nur in Cora gespeichert. Stellst du eine Steckdose auf Immer ein oder Immer aus, übersteuert das die eigene Programmierung des Controllers dafür, bis du Zurück zu automatisch wählst.
:::

Sieht eine Steckdose oder ein Sollwert so aus, als gehöre er zu einem Heizer oder einer Rückförderpumpe, bittet Cora dich zweimal um Bestätigung, bevor es ihn schickt.

Geht der Behälter eines Dosierers zur Neige, warnt dich Cora genauso wie bei anderem Verbrauchsmaterial. Standard sind 20 % Füllstand, und du kannst das an der Regel des Dosierers in der [Warnzentrale](/help/mobile-alerts) ändern.

:::note ProfiLux mini
Ein mini kann nur seine Steckdosen schalten. Alles andere hier, etwa Sollwerte und Fütterungspause, braucht einen ProfiLux 3, 4 oder Mitras.
:::

Lehnt der Controller die Änderung ab, prüf, ob seine GHL-API mit vollem Zugriff eingeschaltet ist. GHL schaltet sie nach jedem Firmware-Update aus. Die [Problembehebung](/help/troubleshooting) hat die Schritte.

## HYDROS {#hydros}

:::note Beta
**Beta.** HYDROS ist in der Beta und nur für Beta-Nutzer offen. Wenn du kein Beta-Nutzer bist, siehst du es nicht unter **Gerät hinzufügen**. Für Beta-Zugang [wende dich an den Support](/support.html). Manche Messwerte oder Steuerungen funktionieren vielleicht noch nicht, und was du hier siehst, kann sich mit Updates ändern. Funktioniert etwas nicht wie beschrieben, sag es uns über [Ein Problem melden](/help/mobile-support). Mehr dazu unter [Beta-Funktionen](/help/mobile-beta).
:::

Was du hier siehst, hängt von dem Schlüssel ab, mit dem du verknüpft hast. Ein Schlüssel mit **Lesen** gibt dir nur seine Eingänge. Ein Schlüssel mit **Schreiben** fügt Ausgänge, Modi, Dosierung und Testerbefehle hinzu, dazu ein Banner auf der Seite, das dich daran erinnert, welche Art von Schlüssel du nutzt.

Mit einem Schreibschlüssel bleibt die Steuerung außerdem aus, bis du **Steuerung durch Cora zulassen (Beta)** auf der Seite des Geräts einschaltest. Standardmäßig ist es aus.

Ist es eingeschaltet, kann die Seite zeigen:

- **Ausgänge**, als Schalter für einen Ein/Aus-Ausgang, als Schieberegler für eine Stufe wie bei einer Pumpe oder einem Licht, oder als Taste für ein Flag. Ein übersteuerter Ausgang zeigt **Überschrieben** mit einer Taste **Zurück zum Zeitplan**, um ihn an sein eigenes Programm zurückzugeben.
- **Modi**, etwa Feed oder Water Change, als Reihe von Auswahlmöglichkeiten. Ein Tippen auf einen bittet um Bestätigung.
- **Dosierköpfe**, jeder mit einer Taste **Dosieren** und einem Eintrag **Kopfeinstellungen**, wo du seine eigenen Grenzen festlegst: eine größte Handdosis und eine Tagesobergrenze. Wer mehr als die Grenze eines Kopfes verlangt, oder mehr, als seine eigene Tagesobergrenze für den Tag noch übrig hat, wird abgelehnt, mit den Zahlen in der Meldung.
- **Testerbefehle**, für einen angeschlossenen iV oder Maven, über eine Taste ausgeführt und vorher bestätigt.

Hat sich der Controller eine Weile nicht gemeldet, sagt die Seite das, und Messwerte können veraltet sein. Ein Befehl, den du schickst, während er offline wirkt, wird gar nicht gesendet, und die Seite sagt dir auch das.

## Focustronic {#focustronic}

:::note Beta
**Beta.** Focustronic ist in der Beta und nur für Beta-Nutzer offen. Wenn du kein Beta-Nutzer bist, siehst du es nicht unter **Gerät hinzufügen**. Für Beta-Zugang [wende dich an den Support](/support.html). Mehr dazu unter [Beta-Funktionen](/help/mobile-beta).
:::

Jedes Gerät zeigt seinen Status, seine Firmware, den letzten Test und, bei einem Alkatronic, die gemessene Alkalinität und den pH-Wert. Außerdem siehst du die Pumpen mit ihrer jeweiligen Restmenge, Parameter, Fläschchen und alle Warnungen zu Reagenz oder Puffer. Cora fragt Focustronic alle 30 Minuten nach neuen Messwerten.

Unter **Steuerung** kannst du **Jetzt messen**, an einer Pumpe **Jetzt dosieren** (bis zu 500 ml auf einmal) und, bei einem Mastertronic, **Jetzt testen**. Jedes davon bittet dich vorher um Bestätigung. Cora wiederholt eine Dosierung nie. Sagt das Ergebnis, es sei unbekannt, prüf also das Gerät. Befehle laufen über die Server von Focustronic, auf die Cora keinen Einfluss hat, und sind nur verfügbar, solange das Gerät online ist.

## EcoTech, Inkbird und Kameras {#ecotech-inkbird-cameras}

:::note Beta
**Beta.** EcoTech, Inkbird und Kameras sind in der Beta und nur für Beta-Nutzer offen. Wenn du kein Beta-Nutzer bist, siehst du sie nicht unter **Gerät hinzufügen**. Für Beta-Zugang [wende dich an den Support](/support.html).
:::

Diese haben ihre eigenen Seiten:

- EcoTech Radion-Leuchten, VorTech-Pumpen und Versa-Dosierer: [EcoTech-Leuchten, -Pumpen und -Dosierer](/help/mobile-ecotech)
- Inkbird-Raumluftmonitore melden nur Messwerte, es gibt also nichts zu steuern: [Deine Ausrüstung verbinden](/help/mobile-connections#inkbird-room-air-monitor)
- Kameras und Skimmer-Wächter: [Kameras und Skimmer-Wächter](/help/mobile-cameras)

## Was passiert, nachdem du etwas geändert hast {#what-happens-after-you-change-something}

Jede Änderung wird unter [Aktivität](/help/mobile-activity) festgehalten, mit der Oberfläche, von der sie kam. Nimmt ein Gerät eine Änderung nicht an, wird auch das dort festgehalten.

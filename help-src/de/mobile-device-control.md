---
title: Deine Ausrüstung steuern
description: Die Seite eines Geräts öffnen, um seinen Live-Zustand zu sehen und Steckdosen, Pumpen, Dosierköpfe und Tester zu schalten, Marke für Marke.
section: Cora Mobile
reviewed: 2026-10-18
order: 13
group: Equipment
twin: max-device-control
---

Auf der eigenen Seite eines Geräts siehst du seinen Live-Zustand und änderst, was es tut. Öffne sie über **Geräte** → auf das Gerät tippen, oder tippe auf seine Kachel auf dem Dashboard.

![Eine ReefATO+-Seite in Cora Mobile](img/mobile-device-detail.webp "Status, die heutigen Messwerte und der Wasserstand, dann Leck, Befüllungen und Sondenkalibrierung.")

Jede Geräteseite ist gleich aufgebaut. Name und Details stehen oben, dann eine Reihe von Live-Messwerten, jeder Zustand, den das Gerät meldet, und seine Steuerungen. Die Glocke in der Titelleiste legt Warnschwellen für dieses Gerät fest, wie unter [Verbrauchsmaterial und Nachfüllwarnungen](/help/mobile-consumables) beschrieben. Wie du ein Gerät überhaupt hinzufügst, steht unter [Deine Ausrüstung verbinden](/help/mobile-connections).

Spring zu deiner Ausrüstung: [Neptune Apex](#neptune-apex) · [Trident](#trident) · [DŌS](#dos) · [Red Sea](#red-sea) · [ReefDose](#reefdose) · [ReefRun](#reefrun) · [ReefMat](#reefmat) · [ReefATO+](#reefato) · [Dosierpumpen-Warnungen](#doser-alerts) · [Jecod](#jecod) · [AquaWiz](#aquawiz)

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
Das Gerät hat keinen Füllstandssensor und hört nicht von selbst auf. Leg für jeden Kopf unter **Warnungen** auf der DŌS-Seite eine Nachfüllwarnung fest, damit Cora dich warnt, bevor der Behälter leer läuft. Siehe [Dosierpumpen-Warnungen](#doser-alerts).
:::

### Wofür jeder Kopf verwendet wird {#dos-head-use}

Gib jedem Kopf einen **Verwendungstyp**, damit Cora weiß, was er tut, und richtig darüber spricht. Zur Wahl stehen **Supplement**, **Wasserwechsel: neues Salzwasser rein**, **Wasserwechsel: altes Wasser raus**, **Kalkwasser**, **Calciumreaktor**, **Futter**, **Nachfüllen** und **Andere**. Stell ihn unter **Verwendet für** in den Einstellungen des Kopfes ein.

Die beiden Wasserwechsel-Typen gehören in **Paare**. Stell bei einem Kopf **Gekoppelter Kopf** auf den Kopf, der Wasser in die andere Richtung bewegt, dann behandelt Cora die beiden als ein Wasserwechsel-Paar.

Ein Behälter kann bei jedem Verwendungstyp bis zu 1.000 l groß sein. Der Apex selbst zählt nur bis 150 l, darüber verfolgt Cora den Behälter also selbst anhand dessen, was der Kopf dosiert. Gib beim Einrichten das **Gesamtvolumen** ein. Cora setzt außerdem ab und zu den eigenen Zähler des Apex zurück, und die Aktivität zeigt das als *Den eigenen Zähler des Apex auf 150 L zurückgesetzt*.

Jeder Kopf hat außerdem eine Grenze **Größte manuelle Dosierung**, damit ein Tippfehler aus einer Handdosierung nicht etwas viel Größeres macht, als du wolltest. Große Handdosierungen werden erst verfügbar, nachdem die Rate des Kopfes am Becken mit einem echten Test gemessen wurde und du **Große Dosierungen** in den Einstellungen des Kopfes eingeschaltet hast. Standardmäßig ist es aus. Schalte es erst ein, nachdem du die erste große Dosierung am Becken beobachtet hast.

## Red Sea ReefBeat {#red-sea}

Jedes Red Sea-Gerät hat eine Seite, die zu dem passt, was es tut:

| Gerät | Die Seite zeigt | Du kannst |
|---|---|---|
| [ReefDose](#reefdose) | Jeden Kopf, seinen Behälter und was er dosiert hat | Dosieren, die Tagesdosis ändern, den **Dosierplan** bearbeiten |
| [ReefRun](#reefrun) | Geschwindigkeit und Zustand der Rückförder- und Abschäumerpumpe | Geschwindigkeit ändern, eine Pumpe schalten |
| [ReefMat](#reefmat) | Verbleibende Rolle, in Tagen und Metern | Die Matte weiterspulen, **ReefMat-Einstellungen** festlegen, eine neue Rolle eintragen |
| [ReefATO+](#reefato) | Füllstand des Reservoirs und Nachfüllaktivität | Eine Nachfüllbehälter-Warnung festlegen |



Bist du nicht im Netzwerk des Geräts, schickt Cora Mobile Red Sea-Befehle über ein Cora Max am Becken. Kann das kein Cora Max, sagt die Seite das, und es wird nichts gesendet.

## ReefDose {#reefdose}

![Eine ReefDose 4-Seite in Cora Mobile](img/mobile-reefdose.webp "Status, Köpfe und heutige Gesamtmenge, Dosierpumpe für Verbrauch nutzen, dann jeder Dosierkopf.")

Für jeden Kopf kannst du **Dosierung pro Tag** und **Rest in der Flasche** einstellen, **Jetzt dosieren** ausführen und **Zeitplan aktivieren**. Nachfüllwarnungen legst du pro Kopf mit der Glocke fest, wie unter [Dosierpumpen-Warnungen](#doser-alerts) beschrieben.

Der Bereich **Dosierung** zeigt **Anstehende Dosierungen**, was jeder Kopf heute dosiert hat (**Heute bisher dosiert**) und **Dosiert pro Kopf** für die **Letzte 7 Tage** oder **Gesamt**. Cora liest das, solange ein Cora Max oder dein Handy in deinem Heimnetz ist.

### Einen Dosierplan bearbeiten {#reefdose-plan}

Tippe auf einer ReefDose-Seite auf das Kalendersymbol, um den **Dosierplan** zu öffnen.

Ein Plan ist eine Tagesmenge, aufgeteilt in bis zu vier Zeitfenster. Jedes Fenster hat eine Start- und Endzeit, wie viele Dosierungen es abgeben soll, und eine Geschwindigkeit: **Flüster**, **Normal** oder **Schnell**. Füg Fenster hinzu und entferne sie, dann speichere. Cora zeigt dir, was du gleich schickst, und bittet dich um Bestätigung, bevor es den ganzen Plan des Kopfes ersetzt.

Der Editor liest zuerst den Plan, der schon auf dem Gerät ist, du bearbeitest also den echten und kein leeres Formular.

## ReefRun {#reefrun}

ReefRun steuert Rückförder- und Abschäumerpumpen. Es ist keine Strömungspumpe. Du kannst die Geschwindigkeit einer Pumpe ändern, sie ein- oder ausschalten und Abschäumer-Einstellungen anpassen.


## ReefMat {#reefmat}

Die ReefMat-Seite zeigt, wie viel Rolle übrig ist, in Tagen und Metern. Tippe auf **Jetzt weiterspulen**, um die Matte von Hand weiterzuspulen. Cora fragt zuerst **Die Matte jetzt weiterspulen?** Du kannst auch eine Nachfüllwarnung für die Rolle festlegen.

Tippe auf das Zahnrad für **ReefMat-Einstellungen**:

- **Geplanter Vorschub** schaltet einen Vorschub zu festen Zeiten ein, getrennt vom Sensor für den automatischen Vorschub, der schon auf der Seite ist. Schalte ihn ein und leg fest, wie oft und wie weit jeder Vorschub die Matte bewegt.
- **ReefMat-Modell** und **Motorposition** (**Links** oder **Rechts**) sagen Cora, welches Gerät und welche Ausrichtung du hast.

Nachdem du eine neue Rolle eingelegt hast, sag es Cora mit **Neue Rolle**: ihre Dicke und, wenn du ihn kennst, ihren Außendurchmesser. **Jetzt weiterspulen** bewegt nur die Matte, die schon eingelegt ist.

## ReefATO+ {#reefato}

Die ReefATO+-Seite zeigt den Füllstand des Nachfüllbehälters und die letzten Nachfüllungen. Leg mit der Glocke eine Warnung für den Nachfüllbehälter fest. Cora schätzt aus dem jüngsten Nachfüllverbrauch, wie viele Tage der Nachfüllbehälter noch reicht, und du kannst auch den Assistenten danach fragen.

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

## Dosierpumpen-Warnungen {#doser-alerts}

Ein DŌS und ein ReefDose haben ihre Warnungen auf ihrer eigenen Seite. Der Tab **Regeln** der [Warnzentrale](/help/mobile-alerts) hat pro Dosierpumpe eine Zeile, die sie öffnet, und die Taste **Dosierpumpe öffnen** einer Dosierpumpen-Warnung bringt dich ebenfalls hierher.

Tippe auf einer DŌS-Seite auf die Karte **Warnungen** (oder die Glocke in der Titelleiste). Das Fenster listet jeden Kopf auf, und für jeden kannst du festlegen:

- *[Kopf] · Tage übrig*, zum Beispiel *Jod · Tage übrig*: Du bekommst eine Warnung, wenn der Vorrat für weniger als so viele Tage reicht
- *[Kopf] · verbleibend*: Du bekommst eine Warnung, wenn weniger als so viel im Behälter ist
- **Verbleibender Platz im Abfallbehälter**, für einen Kopf, der altes Wasser abpumpt: Du bekommst eine Warnung, wenn der Abfallbehälter voll wird
- **Warnungen bei verpasster Dosierung**: ein Schalter, der dir meldet, wenn der Kopf eine geplante Dosierung verpasst

Jeder Schwellenwert hat seinen eigenen Schalter, du kannst also einen ausschalten und seinen Wert behalten. Tippe auf **Speichern**, wenn du fertig bist.

Tippe auf einer ReefDose-Seite auf die Glocke in der Titelleiste. Jeder Kopf hat seinen eigenen Schwellenwert für die verbleibenden Tage und seinen eigenen Schalter.

Standardwerte und anderes Verbrauchsmaterial stehen unter [Verbrauchsmaterial und Nachfüllwarnungen](/help/mobile-consumables).

## Jecod / Jebao-Pumpen {#jecod}

Die Pumpenseite zeigt das aktuelle Wellenmuster (Modus) und die Intensität, und du kannst beides ändern. Ihr Status steht in der Titelzeile neben dem Namen der Pumpe. Ein Schalter mit **Den ganzen Tag gleich** und **Zeitplan** markiert den laufenden Modus mit *· läuft*, und die Seite öffnet sich auf ihm. Wie du ein Tagesprogramm baust und es kopierst, speicherst oder teilst, steht unter [Ausrüstung planen](/help/mobile-schedules).

Gehört die Pumpe zu einer Gruppe, zeigt die Seite ihre Rolle, etwa **Führt die Gruppe an**, **Folgt: im Gleichschritt** oder **Folgt: wechselnd**.

### Futterpause {#jecod-feeding}

Starte eine Futterpause unter **Füttern** auf der Seite der Pumpe: Tippe auf **5**, **10**, **15** oder **30** Min. Manche Pumpen beenden die Pause selbst, und die Seite sagt *Die Pumpe beendet das von selbst.*

:::warning Lass die Seite der Pumpe während einer Futterpause offen
Manche Pumpen beenden eine Fütterung nicht von selbst, und die Seite sagt das. Bei diesen, und bei jeder Pumpe mit Zeitplan, holt Cora Mobile das Wellenmuster und den Zeitplan nur zurück, solange die Seite der Pumpe offen bleibt. Verlässt du die Seite, bleibt die Pumpe im Fütterungsmodus gestoppt oder außerhalb ihres Zeitplans, bis du sie wieder änderst oder auf **Zeitplan** tippst.
:::

Hat dein Haushalt ein Cora Max, beendet es die Fütterung und setzt die Pumpe nach Ablauf der Zeit wieder auf ihr Programm, auch wenn Cora Mobile geschlossen ist. Die Warnung oben gilt dann nur, wenn es kein Cora Max gibt.

Eine Bluetooth-Pumpe muss in Reichweite deines Handys sein, um eine Fütterung zu starten, und eine Netzwerkpumpe muss in deinem Netzwerk sein.

### Fehlerprüfungen {#jecod-fault-checks}

**Fehlerprüfungen** legt fest, wie oft Cora die Pumpe erneut liest, damit es dich vor einem Fehler warnen kann, etwa einer blockierten oder trocken laufenden Pumpe. Stellst du es auf aus, hören diese Warnungen für diese Pumpe auf. Fehlerprüfungen brauchen ein Cora Max am Becken. Deine Wahl wird gespeichert, und die Prüfungen beginnen, sobald eins hinzugefügt wird. **Für jede Pumpe an diesem Becken verwenden** kopiert die Einstellung auf alle.

## AquaWiz {#aquawiz}

Die AquaWiz-Karte zeigt deine Alkalinitäts-Messwerte und den pH-Wert, wenn dein Gerät ihn meldet. Cora kann einen AquaWiz nicht steuern, ändere seine Einstellungen also in der AquaWiz-App.

Unter **Controller** auf der Geräteseite zeigt Cora, was der Controller meldet, jede Zeile nur, wenn er sie meldet:

- den KH-Zielwert;
- wie viel Alkalinitäts-Zusatz noch übrig ist, mit der Warnstufe, die du am Controller eingestellt hast (zum Beispiel *niedrig ab 100 mL*);
- wie viele mL für 1 dKH nötig sind (*mL pro 1 dKH*);
- die maximale Dosis pro Messung (*Bis zu 20 mL pro Messung*);
- die Firmware-Version.

Unter den Messwerten zeigt die Karte, wann der letzte gemessen wurde (zum Beispiel *Gemessen 14:00*) und woher er kam: **Stündlich von deinem Cora Max** oder **Aus der AquaWiz-Cloud, alle 12 Stunden**. Außerdem zeigt sie die **pH-Änderung**. Beim Öffnen der Seite fragt Cora einen frischen Messwert an, und **Jetzt auslesen** fragt noch einmal an, höchstens alle 15 Minuten. Ändert sich ein Messwert nicht, ist das normal: Das Gerät misst nur von Zeit zu Zeit.

Die Karte zeigt auch Pumpe und pH-Sonde, und Cora warnt dich, wenn die Pumpe einen Fehler meldet oder die pH-Sonde ausgefallen oder fast am Ende ihrer Lebensdauer ist. Das gilt für jeden AquaWiz, mit oder ohne Cora Max. Liest ein Cora Max das Gerät jede Stunde aus, zeigt die Karte auch den Wasserbox-Füllstand, und Cora warnt dich, wenn er länger als eine Stunde niedrig oder hoch bleibt.

Erfasst dein Gerät seinen Behälter, warnt dich Cora, wenn der Zusatz zur Neige geht, bei der Warnstufe, die du am Controller eingestellt hast. Du kannst sie weiterhin an ihrer Regel in der [Warnzentrale](/help/mobile-alerts) ändern, und deine Änderung bleibt erhalten.


## Was passiert, nachdem du etwas geändert hast {#what-happens-after-you-change-something}

Jede Änderung wird unter [Aktivität](/help/mobile-activity) festgehalten, mit der Oberfläche, von der sie kam. Nimmt ein Gerät eine Änderung nicht an, wird auch das dort festgehalten.

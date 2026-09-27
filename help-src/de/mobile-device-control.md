---
title: Deine Ausrüstung steuern
description: Öffne die eigene Seite eines Geräts, um seinen Live-Zustand zu sehen und es zu steuern: Steckdosen, Pumpen, Dosierköpfe und Testgeräte.
section: Cora Mobile
reviewed: 2026-09-27
order: 11
group: Equipment
---

Verbundene Ausrüstung hat ihre eigene Seite in Cora, die den Live-Zustand zeigt und die Steuerungen anbietet, die dieses Gerät unterstützt. Öffne eine aus dem Tab **Geräte**.

![Eine Geräteseite](img/mobile-device-detail.webp "Live-Messwerte oben, dann die Steuerungen, die dieses Gerät unterstützt.")

Jede Geräteseite folgt derselben Form: Identifikation oben, eine Reihe von Live-Messwerten, jeder vom Gerät gemeldete Zustand, dann seine Steuerungen. Die Glocke in der Titelleiste legt Warnschwellenwerte für dieses Gerät fest; siehe [Verbrauchsmaterial](/help/mobile-consumables).

:::warning Diese Steuerungen wirken auf echte Ausrüstung
Es gibt keine Vorschau und kein Rückgängig. Manche Steuerungen bitten außerdem zuerst um Bestätigung.
:::

## Was passiert, wenn du einen Befehl sendest

Ein Befehl gelingt nicht immer, und Cora sagt dir, welches von vier Dingen passiert ist, statt es anzunehmen:

| Ergebnis | Bedeutet |
|---|---|
| **Bestätigt** | Die Ausrüstung hat die Änderung bestätigt und ihren neuen Zustand gemeldet |
| **Unbestätigt** | Der Befehl wurde gesendet, aber nichts hat zurückgemeldet. **Das bedeutet "wir wissen es nicht", nicht "es hat funktioniert"**; prüfe den eigenen Zustand des Geräts |
| **Abgelehnt** | Etwas hat ihn abgelehnt (eine Sicherheitsregel, eine Sperre, oder die Ausrüstung selbst), oder kein Cora-Gerät hat ihn rechtzeitig aufgenommen, daher wurde er abgebrochen und nichts ist gelaufen |
| **Keine Änderung** | Die Ausrüstung war bereits in dem Zustand, den du verlangt hast |

Jedes Ergebnis wird in [Aktivität](/help/mobile-activity) zusammen mit seiner Ursache erfasst.

## Neptune Apex

Die Apex-Seite listet deine Sonden und Steckdosen auf.

- **Sonden** melden sich Cora als Quellen und können auf einem Dashboard platziert werden.
- **Steckdosen** schalten zwischen **Auto**, **Aus** und **Ein**. Auto gibt die Steuerung an deine Apex-Programmierung zurück.
- **Eingebaute Module** (Trident, DŌS und andere) haben jeweils ihre eigene Seite.

## Trident

Zeigt den aktuellen Teststatus, die verbleibenden Reagenz- und Abfallwasserstände, und lässt dich einen Test starten.

Du kannst von dieser Seite aus einen Warnschwellenwert für verbleibende Tests festlegen, sodass Cora dich warnt, bevor das Reagenz ausgeht. Siehe [Verbrauchsmaterial](/help/mobile-consumables).

## DŌS

Ein DŌS QD funktioniert genau wie ein DŌS, und alles hier gilt für beide. Wenn ein Cora Max deinen Apex liest, erscheinen Dosierköpfe auf der DŌS-Seite, nie in der Steckdosenliste.

Jeder Dosierkopf zeigt, was er dosiert, seinen Zeitplan, was er heute dosiert hat, wie viel im Behälter übrig ist, und seine **Reichweite**: wie viele Tage das beim aktuellen Verbrauch noch reicht.

Pro Kopf kannst du:

- Seinen Zeitplan **Pausieren** und **Fortsetzen**
- **Befüllen**: Cora sagen, dass der Behälter wieder voll ist, oder die darin enthaltene Menge festlegen
- **Jetzt dosieren**: eine bemessene manuelle Dosierung

:::note Zeitpläne werden in Apex Fusion bearbeitet, nicht hier
Cora zeigt den Zeitplan und verfolgt, was dosiert wurde, ändert ihn aber nicht. Den Zeitplan, die Dosierrate oder die Anzahl der Dosierungen zu bearbeiten geschieht in der Apex Fusion-App. Pausieren, Befüllen und manuelles Dosieren werden alle hier unterstützt.
:::

:::note Messe einen Kopf, bevor du ihn manuell dosierst
Cora dosiert einen Kopf nicht manuell, bis er gemessen wurde. **Zum Dosieren messen** und **Erneut messen** befinden sich auf dem Cora Max, das für das Becken dosiert: Cora lässt den Kopf zwanzig Sekunden laufen, du misst, was herauskam, und Cora ermittelt die tatsächliche Rate des Kopfes. Eine Messung dient jedem Cora Max und Cora Mobile, daher misst du jeden Kopf einmal, und erneut nach einem Wechsel seines Schlauchs.
:::

:::warning Ein DŌS dosiert weiter, wenn sein Behälter leer ist
Das Gerät hat keinen Füllstandssensor und stoppt nicht von selbst. Lege eine Nachfüllwarnung auf der Seite des Kopfes fest, damit Cora dich warnt, bevor der Behälter trockenläuft.
:::

### Wofür jeder Kopf verwendet wird

Jeder Kopf wird auf einen **Verwendungstyp** eingestellt, damit Cora weiß, was er tut, und korrekt darüber sprechen kann: **Supplement**, **Wasserwechsel: neues Salzwasser rein**, **Wasserwechsel: altes Wasser raus**, **Kalkwasser**, **Calciumreaktor**, **Futter**, **Nachfüllen**, oder **Andere**. Lege das unter **Verwendet für** in den Einstellungen des Kopfes fest.

Die beiden Wasserwechsel-Verwendungstypen sind dazu gedacht, **gekoppelt** zu werden: Setze den **Gekoppelten Kopf** des einen Kopfes auf den anderen, der Wasser in die entgegengesetzte Richtung bewegt, und Cora behandelt sie als ein Wasserwechsel-Paar statt als zwei unabhängige Köpfe.

Jeder Kopf hat außerdem eine Obergrenze **Größte manuelle Dosierung**, um zu verhindern, dass eine falsch eingegebene manuelle Dosierung weit größer ausfällt als beabsichtigt. Große manuelle Dosierungen werden erst verfügbar, sobald die Rate des Kopfes gegen einen echten Test am Becken gemessen wurde.

## Red Sea ReefBeat

Jedes Gerät hat eine Seite, die zu ihm passt:

| Gerät | Seite zeigt | Du kannst |
|---|---|---|
| **ReefDose** | Jeden Kopf, seinen Behälter und was er dosiert hat | Für jeden Kopf: **Dosierung pro Tag**, **Rest in der Flasche**, **Jetzt dosieren** und **Zeitplan aktivieren**. Nachfüllwarnungen pro Kopf festlegen |
| **ReefATO+** | Reservoirstand und Nachfüllaktivität | Eine Reservoirwarnung festlegen |
| **ReefMat** | Verbleibende Rolle, in Tagen und Metern | Die Rolle vorschieben, eine Nachfüllwarnung festlegen |
| **ReefRun** | Drehzahl und Zustand von Rückförder- und Abschäumerpumpe | Drehzahl ändern, eine Pumpe schalten, Abschäumereinstellungen anpassen |

**ReefRun ist ein Controller für Rückförder- und Abschäumerpumpe**, keine Strömungspumpe.

Ein Gerät kann sich selbst anhalten, zum Beispiel eine ReefRun-Pumpe, wenn sich der Abschäumerbecher füllt. Wenn das passiert, sagt seine Seite, warum, und bietet die Lösung an:

| Gerät | Die Seite sagt | Tippe auf |
|---|---|---|
| ReefRun | Welche Pumpe angehalten hat und warum, zum Beispiel *Becher voll. Leere ihn, und fahre dann fort.* | **Fortsetzen** |
| ReefRun oder ReefMat | **Notstopp** | **Notstopp aufheben** |
| ReefMat | **Matte blockiert**, **Installationsfehler** oder **Einrichtungsfehler** | **Fortsetzen** |
| ReefMat | *Lege eine neue Rolle ein, und bestätige das dann in Red Seas App.* | **Ich habe bereits eine neue Rolle eingelegt** |
| ReefMat | **Sensor muss gereinigt werden** | **Sensor gereinigt** |
| ReefDose | **Kopf-Fehlfunktion**, mit dem Namen des Kopfes | **Zurücksetzen** |
| ReefATO+ | **Fehler löschen** | **Fortsetzen** |

Manche davon bitten zuerst um Bestätigung. Fern vom Netzwerk des Geräts sendet Cora Mobile sie über ein Cora Max am Becken; wenn kein Cora Max das kann, sagt die Seite das, und nichts wird gesendet.

## Jecod-Pumpen

Die Pumpenseite zeigt ihren aktuellen Modus und ihre Intensität, und lässt dich beides ändern.

Du kannst außerdem:

- **Zeitplan kopieren nach…**: den Zeitplan dieser Pumpe auf eine andere übertragen
- **Zeitplan speichern als…** und **Gespeicherte Zeitpläne…**: einen Zeitplan behalten und später erneut anwenden
- **Diesen Zeitplan teilen** und **Zeitplan-Code einfügen…**: einen Zeitplan als kurzen Code zwischen Systemen bewegen

## Maxspect

:::note Die Maxspect-Unterstützung ist in der Beta
Die Unterstützung für Maxspect-Gyres wird noch getestet und weiterentwickelt, daher können manche Steuerungen eingeschränkt sein, und was du hier siehst, kann sich zwischen Updates ändern. Wenn etwas nicht wie beschrieben funktioniert, sag es uns über [Hilfe erhalten](/help/mobile-support).
:::

Die Gyre-Seite zeigt, ob die Gyre läuft, das Wellenmuster und die Geschwindigkeit von **Gyre A** und **Gyre B**, und wann das zuletzt gelesen wurde. Von dort aus kannst du:

- Die Gyre mit dem Schalter neben ihrem Zustand ein- oder ausschalten. Cora bittet zuerst um Bestätigung. Ausschalten stoppt beide Gyres und lässt den Zeitplan, wie er ist.
- Auf **Einstellungen ändern** tippen, um Wellenmuster und Pumpengeschwindigkeit jeder Gyre festzulegen (und die Dauer, für ein Muster, das eine hat), und ob die beiden Gyres verbunden sind. Cora listet auf, was sich ändern wird, und bittet um Bestätigung, bevor es angewendet wird. Abwechseln wird in der Maxspect-App festgelegt: Eine Gyre, die das ausführt, behält ihre Rampen und Haltezeiten.
- Statt dessen auf **Programm festlegen** tippen, wenn das auf der Gyre gespeicherte Programm nicht gelesen werden kann. Das stellt beide Gyres so ein, dass die Gyre wieder starten kann.
- Das Tagesprogramm der Gyre auf der Karte **Zeitplan** ansehen. Sie ist nur zur Ansicht: Lege den Zeitplan in der Maxspect-App fest.
- **Pumpenzustand** prüfen: wann die Pumpe als Nächstes gereinigt werden muss (die Pumpe zählt das selbst herunter), der von Kopf A aufgenommene Strom, welche Köpfe eingebaut sind, und die Firmware. Tippe auf **Lesen**, um sie abzurufen.

:::note Wie Cora Mobile eine Gyre erreicht
Wenn ein Cora Max das Becken bedient, arbeitet Cora Mobile über dieses Cora Max, auch wenn du nicht zu Hause bist, und **Einstellungen ändern** startet von der letzten Messung dieses Cora Max. Andernfalls spricht dein Handy direkt mit der Gyre und muss im Netzwerk der Gyre sein. Die Seite zu öffnen liest dann die Gyre; zeigt die Seite statt dessen eine ältere gespeicherte Messung, bleibt **Einstellungen ändern** verborgen, bis du auf Aktualisieren tippst.
:::

## Was passiert, nachdem du etwas geändert hast

Jede Änderung wird in [Aktivität](/help/mobile-activity) zusammen mit der Oberfläche erfasst, die sie angefordert hat. Wenn ein Gerät eine Änderung nicht annimmt, wird der Fehlschlag dort auch erfasst.

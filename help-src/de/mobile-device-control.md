---
title: Deine Ausrüstung steuern
description: Auf der Seite eines Geräts siehst du seinen Live-Zustand und steuerst es, ob Steckdose, Pumpe, Dosierkopf oder Testgerät.
section: Cora Mobile
reviewed: 2026-09-27
order: 11
group: Equipment
---

Jedes verbundene Gerät hat in Cora eine eigene Seite. Dort siehst du seinen Live-Zustand und findest alle Steuerungen, die das Gerät unterstützt. Du öffnest sie über den Tab **Geräte**.

![Eine Geräteseite](img/mobile-device-detail.webp "Live-Messwerte oben, dann die Steuerungen, die dieses Gerät unterstützt.")

Alle Geräteseiten sind gleich aufgebaut. Oben steht, um welches Gerät es geht. Darunter folgen eine Reihe Live-Messwerte, jeder Zustand, den das Gerät meldet, und zum Schluss die Steuerungen. Mit der Glocke in der Titelleiste legst du Warnschwellen für das Gerät fest. Mehr dazu unter [Verbrauchsmaterial](/help/mobile-consumables).

:::warning Diese Steuerungen schalten echte Geräte
Es gibt keine Vorschau und kein Rückgängig. Manche Steuerungen fragen vorher noch einmal nach.
:::

## Was nach einem Befehl passiert

Nicht jeder Befehl klappt. Cora nimmt deshalb nichts einfach an, sondern sagt dir, welcher von vier Fällen eingetreten ist:

| Ergebnis | Bedeutung |
|---|---|
| **Bestätigt** | Das Gerät hat die Änderung bestätigt und seinen neuen Zustand gemeldet |
| **Unbestätigt** | Der Befehl ging raus, aber es kam keine Rückmeldung. **Das heißt "wir wissen es nicht" und nicht "es hat geklappt".** Schau direkt am Gerät nach |
| **Abgelehnt** | Etwas hat den Befehl abgelehnt (eine Sicherheitsregel, eine Sperre oder das Gerät selbst), oder kein Cora-Gerät hat ihn rechtzeitig übernommen. Er wurde abgebrochen, und es ist nichts passiert |
| **Keine Änderung** | Das Gerät war schon im gewünschten Zustand |

Jedes Ergebnis landet mit seinem Auslöser in der [Aktivität](/help/mobile-activity).

## Neptune Apex

Die Apex-Seite listet deine Sonden und Steckdosen auf.

- **Sonden** liefern ihre Werte als Quellen an Cora. Du kannst sie aufs Dashboard legen.
- **Steckdosen** schaltest du zwischen **Auto**, **Aus** und **Ein**. Mit Auto übernimmt wieder deine Apex-Programmierung.
- **Eingebaute Module** wie Trident, DŌS und andere haben jeweils eine eigene Seite.

## Trident

Die Seite zeigt den aktuellen Teststatus und die Füllstände von Reagenz und Abwasser. Von hier aus startest du auch einen Test.

Du kannst hier eine Warnschwelle für die verbleibenden Tests festlegen. Dann warnt Cora dich, bevor das Reagenz ausgeht. Mehr dazu unter [Verbrauchsmaterial](/help/mobile-consumables).

## DŌS

Ein DŌS QD funktioniert genau wie ein DŌS. Alles in diesem Abschnitt gilt für beide. Liest ein Cora Max deinen Apex aus, erscheinen die Dosierköpfe auf der DŌS-Seite und nie in der Steckdosenliste.

Zu jedem Dosierkopf siehst du, was er dosiert, seinen Zeitplan, was er heute dosiert hat, wie viel noch im Behälter ist und seine **Reichweite**. Das ist die Zahl der Tage, die der Rest beim aktuellen Verbrauch noch reicht.

Für jeden Kopf kannst du:

- seinen Zeitplan **pausieren** und **fortsetzen**
- mit **Befüllen** Cora sagen, dass der Behälter wieder voll ist, oder die Füllmenge eintragen
- mit **Jetzt dosieren** eine abgemessene Dosis von Hand abgeben

:::note Zeitpläne bearbeitest du in Apex Fusion
Cora zeigt den Zeitplan und verfolgt, was dosiert wurde, ändert ihn aber nicht. Zeitplan, Dosierrate oder Zahl der Dosierungen bearbeitest du in der Apex Fusion-App. Pausieren, Befüllen und Dosieren von Hand gehen hier.
:::

:::note Miss einen Kopf aus, bevor du von Hand dosierst
Cora dosiert von Hand erst, wenn der Kopf ausgemessen ist. **Zum Dosieren messen** und **Erneut messen** findest du auf dem Cora Max, das für das Becken dosiert. Cora lässt den Kopf zwanzig Sekunden laufen, du misst die Menge, die herausgekommen ist, und Cora berechnet daraus die tatsächliche Rate des Kopfes. Eine Messung gilt für jedes Cora Max und für Cora Mobile. Du misst also jeden Kopf einmal aus und nach einem Schlauchwechsel noch einmal.
:::

:::warning Ein DŌS dosiert weiter, auch wenn der Behälter leer ist
Das Gerät hat keinen Füllstandssensor und hört nicht von selbst auf. Leg auf der Seite des Kopfes eine Nachfüllwarnung an. Dann warnt Cora dich, bevor der Behälter leerläuft.
:::

### Wofür ein Kopf verwendet wird

Jeder Kopf bekommt einen **Verwendungstyp**. So weiß Cora, was er tut, und kann richtig darüber sprechen. Zur Auswahl stehen **Supplement**, **Wasserwechsel: neues Salzwasser rein**, **Wasserwechsel: altes Wasser raus**, **Kalkwasser**, **Calciumreaktor**, **Futter**, **Nachfüllen** und **Andere**. Du stellst das in den Einstellungen des Kopfes unter **Verwendet für** ein.

Die beiden Wasserwechsel-Typen sind dafür gedacht, **gekoppelt** zu werden. Stell beim einen Kopf unter **Gekoppelter Kopf** den anderen ein, der das Wasser in die Gegenrichtung pumpt. Cora behandelt die beiden dann als ein Wasserwechsel-Paar und nicht als zwei getrennte Köpfe.

Jeder Kopf hat außerdem eine Obergrenze **Größte manuelle Dosierung**. Sie verhindert, dass eine vertippte Handdosierung viel größer ausfällt als gewollt. Große Handdosierungen sind erst möglich, wenn die Rate des Kopfes mit einem echten Test am Becken ausgemessen wurde.

## Red Sea ReefBeat

Jedes Gerät hat eine Seite, die zu ihm passt:

| Gerät | Die Seite zeigt | Du kannst |
|---|---|---|
| **ReefDose** | jeden Kopf, seinen Behälter und was er dosiert hat | für jeden Kopf **Dosierung pro Tag**, **Rest in der Flasche**, **Jetzt dosieren** und **Zeitplan aktivieren** nutzen und Nachfüllwarnungen pro Kopf anlegen |
| **ReefATO+** | Füllstand des Vorratsbehälters und Nachfüllvorgänge | eine Warnung für den Vorratsbehälter anlegen |
| **ReefMat** | verbleibende Rolle in Tagen und Metern | die Rolle weiterdrehen und eine Nachfüllwarnung anlegen |
| **ReefRun** | Drehzahl und Zustand von Rückförder- und Abschäumerpumpe | die Drehzahl ändern, eine Pumpe schalten und Abschäumer-Einstellungen anpassen |

**ReefRun steuert Rückförder- und Abschäumerpumpe.** Eine Strömungspumpe ist es nicht.

Ein Gerät kann sich auch selbst anhalten, zum Beispiel eine ReefRun-Pumpe, wenn der Abschäumerbecher voll ist. Die Seite sagt dir dann, warum, und bietet dir die passende Lösung an:

| Gerät | Die Seite sagt | Tippe auf |
|---|---|---|
| ReefRun | welche Pumpe angehalten hat und warum, zum Beispiel *Becher voll. Leere ihn und setze dann fort.* | **Fortsetzen** |
| ReefRun oder ReefMat | **Notstopp** | **Notstopp aufheben** |
| ReefMat | **Matte blockiert**, **Installationsfehler** oder **Einrichtungsfehler** | **Fortsetzen** |
| ReefMat | *Lege eine neue Rolle ein und bestätige es dann in der App von Red Sea.* | **Ich habe bereits eine neue Rolle eingelegt** |
| ReefMat | **Sensor muss gereinigt werden** | **Sensor gereinigt** |
| ReefDose | **Kopf-Fehlfunktion** mit dem Namen des Kopfes | **Zurücksetzen** |
| ReefATO+ | **Fehler löschen** | **Fortsetzen** |

Bei manchen davon fragt Cora vorher nach. Bist du nicht im Netzwerk des Geräts, schickt Cora Mobile den Befehl über ein Cora Max am Becken. Kann das kein Cora Max übernehmen, steht das auf der Seite, und es wird nichts gesendet.

## Jecod-Pumpen

Die Pumpenseite zeigt den aktuellen Modus und die Intensität. Beides kannst du dort ändern.

Außerdem kannst du:

- mit **Zeitplan kopieren nach…** den Zeitplan dieser Pumpe auf eine andere übertragen
- mit **Zeitplan speichern als…** und **Gespeicherte Zeitpläne…** einen Zeitplan aufheben und später wieder anwenden
- mit **Diesen Zeitplan teilen** und **Zeitplan-Code einfügen…** einen Zeitplan als kurzen Code auf ein anderes System bringen

## Maxspect

:::note Maxspect wird als Beta unterstützt
Die Unterstützung für Maxspect Gyre wird noch getestet und weiterentwickelt. Manche Steuerungen können deshalb eingeschränkt sein, und was du hier siehst, kann sich mit Updates ändern. Klappt etwas nicht wie beschrieben, sag uns über [Hilfe erhalten](/help/mobile-support) Bescheid.
:::

Die Seite der Gyre zeigt, ob sie läuft, Wellenmuster und Geschwindigkeit von **Gyre A** und **Gyre B** und wann das zuletzt ausgelesen wurde. Hier kannst du:

- die Gyre mit dem Schalter neben ihrem Zustand ein- oder ausschalten. Cora fragt vorher nach. Beim Ausschalten stoppen beide Gyres, und der Zeitplan bleibt, wie er ist.
- auf **Einstellungen ändern** tippen. Dort stellst du für jede Gyre Wellenmuster und Pumpengeschwindigkeit ein, bei Mustern mit Dauer auch die Dauer, und ob die beiden Gyres gekoppelt sind. Cora zeigt dir, was sich ändert, und fragt vor dem Übernehmen nach. Den Wechselbetrieb stellst du in der Maxspect-App ein. Eine Gyre im Wechselbetrieb behält ihre Rampen und Haltezeiten.
- auf **Programm festlegen** tippen, wenn sich das auf der Gyre gespeicherte Programm nicht lesen lässt. Damit stellt Cora beide Gyres so ein, dass die Gyre wieder anlaufen kann.
- das Tagesprogramm der Gyre auf der Karte **Zeitplan** ansehen. Ändern kannst du es dort nicht. Den Zeitplan legst du in der Maxspect-App fest.
- den **Pumpenzustand** prüfen. Du siehst, wann die Pumpe als Nächstes gereinigt werden muss (das zählt die Pumpe selbst herunter), wie viel Strom Kopf A zieht, welche Köpfe eingebaut sind und welche Firmware läuft. Tippe auf **Lesen**, um die Daten abzurufen.

:::note Wie Cora Mobile eine Gyre erreicht
Betreut ein Cora Max das Becken, arbeitet Cora Mobile über dieses Cora Max, auch wenn du nicht zu Hause bist. **Einstellungen ändern** startet dann mit der letzten Messung dieses Cora Max. Ohne Cora Max spricht dein Handy direkt mit der Gyre und muss dafür in ihrem Netzwerk sein. Öffnest du dann die Seite, liest Cora die Gyre aus. Zeigt die Seite stattdessen eine ältere gespeicherte Messung, bleibt **Einstellungen ändern** ausgeblendet, bis du auf Aktualisieren tippst.
:::

## Nachdem du etwas geändert hast

Jede Änderung landet in der [Aktivität](/help/mobile-activity), zusammen mit der Oberfläche, von der sie kam. Nimmt ein Gerät eine Änderung nicht an, steht auch das dort.

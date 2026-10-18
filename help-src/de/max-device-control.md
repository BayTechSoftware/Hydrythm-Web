---
title: Ausrüstung mit Cora Max steuern
description: Geräteseiten auf Cora Max für Neptune Apex, Trident und DŌS, Red Sea ReefBeat, Jecod und AquaWiz, nach Marke sortiert.
section: Cora Max
reviewed: 2026-10-18
order: 6
group: Equipment
twin: mobile-device-control
---

Auf dieser Seite geht es darum, was du auf der Seite jedes Geräts auf Cora Max sehen und tun kannst, Marke für Marke. Cora Max erreicht dieselbe Ausrüstung wie dein Handy. Öffne eine Geräteseite über das Gerätesymbol in der oberen Leiste, über **Einstellungen → Geräte** oder indem du auf dem Dashboard auf eine Gerätekachel tippst.

![Eine Apex-Seite auf Cora Max mit ihren Fütterungstasten und Steckdosen](img/max-device-control.webp "Feed A bis D und Abbrechen, dann die Steckdosen, für einen Wandbildschirm angeordnet.")

:::warning Diese Steuerung wirkt auf laufende Ausrüstung
Es gibt keine Vorschau und kein Rückgängig. Ein Befehl geht raus, sobald du tippst, aber gesendet heißt nicht erledigt. Er kommt mit **Bestätigt**, **Unbestätigt**, **Abgelehnt** oder **Keine Änderung** zurück, und unter [Aktivität](/help/max-activity) siehst du, was davon.
:::

Ausrüstung fügst du auf dem Handy hinzu, weist sie dort zu und entfernst sie dort. Cora Max zeigt sie, sobald dein Konto sie hat. Siehe [Deine Ausrüstung verbinden](/help/mobile-connections).

## Was eine Seite hat {#what-has-a-page}

| Gerät | Zeigt |
|---|---|
| **Neptune Apex** | Sonden und Steckdosen, und du kannst jede Steckdose schalten |
| **Trident** | Teststatus, Reagenz- und Abfallstand und eine Taste, um einen Test zu starten |
| **DŌS**, auch der DŌS QD | Für jeden Kopf Dosierung, Zeitplan, Reichweite und Behältervolumen (mit Pausieren, Befüllen, Jetzt dosieren und einer einmaligen Messung über zwanzig Sekunden) |
| **Red Sea ReefBeat** | Was das Gerät hat: Dosierköpfe, Nachfüllbehälter, Rollentage, Pumpenmodus, dazu ein vollständiger Editor für ReefDose-Plan und ReefMat-Einstellungen |
| **Jecod** | Pumpenmodus und Intensität und ihr Tagesprogramm |
| **AquaWiz** | Keine eigene Seite. Er steht unter **Geräte**, und seine Messwerte erscheinen auf dem Dashboard |

Die meisten Geräteseiten haben einen Stift, um das Gerät umzubenennen. Der neue Name erscheint auch auf deinem Handy. Mehr dazu unter [Geräte und Gerätezustand](/help/max-devices).

## Neptune Apex {#neptune-apex}

Die Apex-Seite listet deine Sonden und Steckdosen auf, mit deinen Fütterungszyklen oben. Jede Steckdose schaltet zwischen **Auto**, **Aus** und **Ein**, und Steckdosen mit Vorhängeschloss bitten um Bestätigung. Wie die drei Zustände und der Fütterungsmodus funktionieren, steht unter [Steckdosen und Steuerung](/help/max-controls).

Steckdosen erreichst du auch über die Schublade **Steckdosen & Füttern** unten auf dem Dashboard. Sie listet die Steckdosen auf, die für dieses Dashboard eingeschaltet sind (oder alle, wenn du keine ausgewählt hast).

Ein großer Apex mit mehreren Modulen zeigt alle seine Steckdosen und Sonden. DŌS-Köpfe erscheinen nie in der Steckdosenliste, du kannst dort also keinen einschalten und laufen lassen. Dosiere über die eigene Seite des Kopfes.

### Trident {#trident}

Die Trident-Seite zeigt den Teststatus und den Reagenz- und Abfallstand. Du kannst hier einen Test starten und mit **Warnungseinstellungen** eine Nachfüllwarnung festlegen.

## DŌS-Köpfe {#dos-heads}

Du musst einen DŌS-Kopf einmal messen, bevor Cora damit von Hand dosiert. **Zum Dosieren messen** lässt den Kopf zwanzig Sekunden lang in einen Messbecher laufen, und du gibst ein, wie viel herausgekommen ist. Cora behält eine Messung pro Kopf und nimmt die neueste, egal welches Cora Max sie gemacht hat. Die Seite des Kopfes zeigt, wo und wann er gemessen wurde.

Nach einer manuellen Dosierung bleibt ein Kopf, den du in Apex Fusion auf Aus gestellt hast, auf Aus. Jeder andere Kopf geht zurück auf Auto.

Ein DŌS hat keinen Füllstandssensor und dosiert auch aus einem leeren Behälter weiter. Leg mit **Warnungseinstellungen** auf der DŌS-Seite eine Nachfüllwarnung fest. Mehr dazu unter [Dosierer-Warnungen](/help/mobile-device-control#doser-alerts).

### Wofür ein Kopf verwendet wird {#what-a-head-is-used-for}

In den Einstellungen eines Kopfes kannst du seinen **Verwendungstyp** festlegen. Die Optionen sind **Supplement**, **Wasserwechsel: neues Salzwasser rein**, **Wasserwechsel: altes Wasser raus**, **Kalkwasser**, **Calciumreaktor**, **Futter** oder **Nachfüllen** und **Andere**. Der Verwendungstyp ändert zwei Dinge.

- Wie groß ein Behälter sein kann, den er verfolgt. Jeder Verwendungstyp kann einen Behälter mit bis zu 1.000 Litern verfolgen. Über dem eigenen 150-Liter-Zähler des Apex verfolgt Cora das Volumen selbst und setzt den Apex-Zähler alle 100 Liter zurück.
- Ob er von Hand eine große Dosierung bekommen kann. Supplement- und Futter-Köpfe behalten die bisherige kleine, vorsichtige Obergrenze. Jeder andere Verwendungstyp kann eine eigene Grenze **Größte manuelle Dosierung** haben, bis zu einer festen Obergrenze von 10 Litern, und ein eigenes **Tageslimit für Automationen und den Assistant**. Eine große Handdosierung braucht außerdem **Große Dosierungen**, eingeschaltet in den Einstellungen des Kopfes, standardmäßig aus. Schalte es erst ein, nachdem du die erste große Dosierung am Becken beobachtet hast.

Zwei Köpfe für den Wasserwechsel (neues Salzwasser rein, altes Wasser raus) kannst du als **Gekoppelter Kopf** verbinden und eine Menge für **Ausgleichswarnung ab** festlegen. Weichen die Tagessummen der beiden Köpfe um mehr als das voneinander ab, warnt Cora dich. Ein Paar außer Gleichgewicht heißt meist, dass eine Seite nicht pumpt, wie sie sollte.

### Wenn eine große Dosierung unterbrochen wird {#if-a-large-dose-is-interrupted}

Eine große Dosierung ändert eine Weile, was der Kopf am Apex tut, und stellt dann seinen normalen Zeitplan wieder her. Bricht die Verbindung mittendrin ab, zeigt Cora Max auf der Seite dieses Kopfes einen Hinweis: *"Eine große Dosierung an [Kopf] wurde nicht sauber abgeschlossen. Cora versucht weiterhin, sein Programm zurückzusetzen; prüfe es in Apex Fusion."*

Prüf den Kopf selbst in Apex Fusion und tippe dann auf **Ich habe den Kopf in Fusion geprüft**, um den Hinweis zu schließen. Tu das erst, wenn du bestätigt hast, dass der eigene Zeitplan des Kopfes läuft und nicht das Dosierprogramm von Cora.

Lässt sich der Hinweis nicht schließen oder kommt er immer wieder, schau in die [Problembehebung](/help/troubleshooting).

## Red Sea ReefBeat {#red-sea}

Jedes Red Sea-Gerät hat eine Seite, die zu dem passt, was es tut: ReefDose-Köpfe und Behälter, den Nachfüllbehälter des ReefATO+, die Rollentage des ReefMat und die Pumpengeschwindigkeiten des ReefRun. Vorratswarnungen für ReefDose-Köpfe, den ReefATO+-Nachfüllbehälter und die ReefMat-Rolle legst du mit **Warnungseinstellungen** auf der Seite des Geräts fest.

Stoppt sich ein Red Sea-Gerät selbst, sagt dir seine Seite, was los ist, und setzt die Lösung gleich daneben. Das ist **Fortsetzen**, **Notstopp aufheben**, **Sensor gereinigt**, **Ich habe bereits eine neue Rolle eingelegt** oder **Zurücksetzen** bei einem Dosierkopf.

Ein ReefDose-Plan und beim ReefMat der geplante Vorschub, das Modell, die Position und Neue Rolle funktionieren hier genauso wie auf dem Handy. [Deine Ausrüstung steuern](/help/mobile-device-control) hat die Details.


## Jecod {#jecod}

Die Jecod-Seite zeigt Modus und Intensität der Pumpe, und du kannst beides ändern. Ihr Status steht in der Titelzeile neben dem Namen der Pumpe. Die obere Leiste enthält den Ein/Aus-Schalter, das Muster, das gerade läuft, und **Füttern** mit vier Chips: **5**, **10**, **15** und **30** Min. Tippe auf einen Chip, um die Pumpe so lange zu pausieren. Darunter liegen zwei Karten:

- **Den ganzen Tag gleich**: tippe auf eine Einstellung, um sie den ganzen Tag laufen zu lassen.
- **Zeitplan**: die Tagesgrafik und die Liste der Pläne, mit **jetzt** beim aktuellen. **Ändern** öffnet den Editor, und das ⋮-Menü enthält **Zeitplan kopieren nach…**, **Zeitplan speichern als…** und **Gespeicherte Zeitpläne…**.

Die Karte, die läuft, hat einen Rahmen und einen Chip **Läuft**. Eine Jecod-Pumpe hat keine Schaltfläche **Fütterung beenden**. Jede Jecod-Pumpe, die für die Fütterung pausieren kann, zeigt die Chips **5**, **10**, **15** und **30** Min. Bei einer Jecod Pro tut die Kachel Füttern in den Wellenmustern dasselbe, für 10 Minuten. Über ein Cora Max, das nicht am Becken ist, füttert eine Jecod-Pumpe nur 10 Minuten lang. Kann eine Pumpe gerade nicht füttern, steht der Grund in einer kurzen Zeile unter den Chips, und ein langer Druck zeigt den ganzen Satz. Eine vom Telefon gestartete Fütterung beendet auch das Cora Max: Läuft die Zeit ab, kehrt die Pumpe zu ihrem Programm zurück.

Tagesprogramme für Jecod-Pumpen kannst du an der Wand genauso schreiben wie auf dem Handy. Der Editor ist derselbe, mit einer Tagesgrafik, einer Liste der Zeiträume und einer Reihe von Aktionen. Mehr dazu unter [Ausrüstung planen](/help/mobile-schedules).

## AquaWiz {#aquawiz}

Ein AquaWiz KH Controller hat auf Cora Max keine eigene Seite. Er steht unter **Geräte**, wo du ihn umbenennen kannst, und seine Messwerte erscheinen auf dem Dashboard wie jede andere Quelle. Richte ihn auf dem Handy ein und verwalte ihn dort, siehe [Deine Ausrüstung verbinden](/help/mobile-connections).

### Stündliches Auslesen durch Cora Max {#aquawiz-hourly}

Kommt mit dem nächsten Cora-Max-Update.

AquaWiz lässt Cora seine Cloud nur alle 12 Stunden auslesen. Damit die Alkalinität aktuell bleibt, liest das Haupt-Cora-Max des Beckens den Controller auch direkt aus, einmal pro Stunde, zehn Minuten vor der vollen Stunde:

- Es verbindet sich für ein paar Sekunden mit dem eigenen WLAN des Controllers, liest das letzte Ergebnis und wechselt sofort zurück in dein Heim-WLAN. Dabei ist das Cora Max etwa 4 Sekunden offline.
- Dein Heim-WLAN-Passwort wird dabei weder gespeichert noch irgendwohin gesendet.
- Nur das Haupt-Cora-Max des Beckens macht das. Ein zweites Cora Max am selben Becken nicht.
- Es wartet, solange das Cora Max mit dir spricht, aktualisiert, koppelt oder das WLAN wechselt, und versucht es in der nächsten Stunde wieder.
- Der Controller muss in WLAN-Reichweite des Cora Max sein, und seine Firmware muss lokalen Zugriff bieten. Schlagen zwei Messungen hintereinander fehl, versucht das Cora Max es für den Rest des Tages nicht mehr, und die 12-Stunden-Messung aus der Cloud läuft weiter.

Ein Messwert vom Cora Max zeigt auf der AquaWiz-Karte im Handy **Stündlich von deinem Cora Max**. Er bringt außerdem die Warnungen zu Pumpe, pH-Sonde und Wasserbehälter mit, die unter [Warnungen](/help/mobile-alerts#equipment-faults) beschrieben sind.


## Verbrauchsmaterial {#consumables}

Nachfüllschwellen (Reagenz, Behälter, Reservoirs) legst du hier auf der Seite des Geräts fest, genau wie auf dem Handy. Mehr dazu unter [Verbrauchsmaterial und Nachfüllwarnungen](/help/mobile-consumables).

## Am Becken eintragen und rechnen {#logging-and-calculating-at-the-tank}

Zwei Dinge gehen an der Wand oft leichter als auf dem Handy.

- **Werte erfassen** lässt dich Testergebnisse über die Bildschirmtastatur eintragen. Du findest es im Beckenmenü.
- **Dosierrechner** berechnet eine Korrektur aus dem Beckenvolumen und der Stärke deiner Produkte. Öffne ihn auf der Seite eines Wasserwerts. Er nutzt dasselbe Volumen und dieselben Produktstärken wie dein Handy, eine hier berechnete Dosis stimmt also mit einer dort berechneten überein. Mehr dazu unter [Dosierung](/help/mobile-dosing).

## Auf einem zweiten Cora Max {#on-a-second-cora-max}

Zeigt mehr als ein Cora Max ein Becken, fragt eins davon die Ausrüstung dieses Beckens ab. Die Geräteseiten nennen es das Cora Max am Becken. Die anderen können die Geräteseiten trotzdem öffnen, und eine Statusanzeige **Cloud** heißt, dass du auf einem von ihnen bist. Sie zeigen, was das Cora Max am Becken zuletzt gelesen hat und wie lange das her ist. Jeder Befehl geht über Cora Cloud an das Cora Max am Becken, das ihn ausführt.

Ein paar Dinge funktionieren nur am Cora Max am Becken.

- **Zum Dosieren messen** und **Erneut messen** erscheinen nur dort. Ist ein Kopf gemessen, funktioniert **Jetzt dosieren** auf jedem Cora Max.
- Einen Jecod-Zeitplan kannst du von einem anderen Cora Max nur ändern, wenn das Cora Max am Becken die Pumpe in der letzten Stunde gelesen hat, und nie bei einer Pumpe, die nur über Bluetooth spricht. Ein **Auf die Pumpe anwenden** von dort schickt höchstens 12 Änderungen, schick eine größere Änderung also in Teilen.

## Was geändert wurde, und wodurch {#what-was-changed-and-by-what}

Jede Aktion wird zusammen mit ihrem Auslöser protokolliert. Mehr dazu unter [Aktivität auf Cora Max](/help/max-activity).

---
title: Ausrüstung mit Cora Max steuern
description: Geräteseiten auf dem großen Bildschirm für Sonden, Steckdosen, Dosierköpfe, Testgeräte und Pumpen.
section: Cora Max
reviewed: 2026-09-30
order: 6
group: Equipment
---

Cora Max erreicht dieselbe Ausrüstung wie dein Handy, und jedes Gerät hat eine eigene Seite. Du öffnest sie über **Einstellungen → Geräte** oder indem du auf dem Dashboard auf eine Gerätekachel tippst.

![Eine Apex-Seite auf Cora Max](img/max-device-control.webp "Fütterungszyklen und alle Steckdosen, für einen Wandbildschirm angeordnet.")

:::warning Diese Steuerung wirkt auf echte Geräte
Es gibt keine Vorschau und kein Rückgängig. Ein Befehl geht raus, sobald du tippst. Gesendet heißt aber noch nicht erledigt. Zurück kommt **Bestätigt**, **Unbestätigt**, **Abgelehnt** oder **Keine Änderung**, und unter [Aktivität](/help/max-activity) siehst du, was davon zutraf.
:::

## Welche Geräte eine Seite haben

| Gerät | Was die Seite zeigt |
|---|---|
| **Neptune Apex** | Sonden und Steckdosen, jede Steckdose ist schaltbar |
| **Trident** | Teststatus, Reagenz- und Abfallstand, und du kannst einen Test starten |
| **DŌS**, auch DŌS QD | Für jeden Kopf Dosierung, Zeitplan, Reichweite und Behältervolumen (mit Pausieren, Befüllen, Jetzt dosieren und einer einmaligen Messung über zwanzig Sekunden) |
| **Red Sea ReefBeat** | Je nach Gerät Dosierköpfe, Reservoir, Rollentage oder Pumpenmodus |
| **Jecod** | Pumpenmodus, Intensität und das Tagesprogramm |
| **Maxspect** *(Beta)* | Modus und Geschwindigkeit für **Gyre A** und **Gyre B**, **Pumpenzustand** (Countdown bis zur Reinigung, Strom an Kopf A, verbaute Köpfe, Firmware) und der Zeitplan, nur zum Ansehen |
| **GHL ProfiLux / Mitras** *(Beta)* | Sonden, Steckdosen, Dosierer, Füllstandssensoren und, bei den Director-Modellen, KH- und Ionen-Testergebnisse |
| **HYDROS** *(Beta)* | Was sein Geräteschlüssel meldet: Eingänge, und mit einem Schreiben-Schlüssel auch Ausgänge, Modi, Dosierköpfe und Testbefehle |

Stoppt sich ein Red Sea-Gerät selbst, steht auf seiner Seite, was los ist, und die passende Lösung gleich daneben: **Fortsetzen**, **Notstopp aufheben**, **Sensor gereinigt**, **Ich habe bereits eine neue Rolle eingelegt** oder bei einem Dosierkopf **Zurücksetzen**.

## DŌS-Köpfe

Bevor Cora einen DŌS-Kopf von Hand dosiert, musst du ihn einmal messen. Mit **Zum Dosieren messen** läuft der Kopf zwanzig Sekunden lang in einen Messbecher, und du gibst ein, wie viel herausgekommen ist. Cora speichert pro Kopf eine Messung und nimmt immer die neueste, egal auf welchem Cora Max sie gemacht wurde. Auf der Seite des Kopfes siehst du, wo und wann er gemessen wurde.

Hast du einen Kopf in Apex Fusion auf Aus gestellt, bleibt er nach einer manuellen Dosierung aus. Alle anderen Köpfe gehen zurück auf Auto.

### Wofür ein Kopf verwendet wird

In den Einstellungen jedes Kopfes legst du einen **Verwendungstyp** fest: **Supplement**, **Wasserwechsel: neues Salzwasser rein**, **Wasserwechsel: altes Wasser raus**, **Kalkwasser**, **Calciumreaktor**, **Futter**, **Nachfüllen** oder **Andere**. Davon hängen zwei Dinge ab:

- **Wie groß der Behälter sein darf.** Ein Supplement-Kopf verfolgt bis zu 20 Liter. Alle anderen Verwendungstypen können einen viel größeren Behälter mit bis zu 500 Litern verfolgen. So wird ein Kopf für Wasserwechsel oder Calciumreaktor nicht wie eine kleine Dosierflasche behandelt.
- **Ob er große Mengen von Hand dosieren darf.** Supplement- und Futter-Köpfe behalten die bisherige kleine, vorsichtige Obergrenze. Für alle anderen Verwendungstypen kannst du eine eigene **Größte manuelle Dosierung** festlegen, höchstens 10 Liter, und ein eigenes **Tageslimit für Automationen und den Assistant**.

Zwei Köpfe für den Wasserwechsel (neues Salzwasser rein, altes Wasser raus) kannst du als **Gekoppelter Kopf** verbinden und einen Wert für **Ausgleichswarnung ab** eintragen. Weichen die Tagesmengen der beiden Köpfe um mehr als diesen Wert voneinander ab, warnt Cora dich. Meist pumpt dann eine Seite nicht so wie erwartet.

### Wenn eine große Dosierung abbricht

Für eine große Dosierung ändert Cora vorübergehend, was der Kopf am Apex tut, und stellt danach seinen normalen Zeitplan wieder her. Reißt die Verbindung mittendrin ab, zeigt Cora Max auf der Seite des Kopfes einen Hinweis: *„Eine große Dosierung an [Kopf] wurde nicht sauber abgeschlossen. Cora versucht weiterhin, sein Programm zurückzusetzen; prüfe es in Apex Fusion.“*

Prüf den Kopf dann selbst in Apex Fusion und tippe erst danach auf **Ich habe den Kopf in Fusion geprüft**, um den Hinweis zu schließen. Tu das nur, wenn du gesehen hast, dass wirklich der eigene Zeitplan des Kopfes läuft und nicht das Dosierprogramm von Cora.

Lässt sich der Hinweis nicht schließen oder taucht er immer wieder auf, hilft dir die [Problembehebung](/help/troubleshooting).

## GHL ProfiLux und Mitras

:::note GHL wird als Beta unterstützt
Die Unterstützung für GHL wird noch getestet und weiterentwickelt. Manche Messwerte oder Steuerungen funktionieren vielleicht noch nicht, und was du hier siehst, kann sich mit Updates ändern.
:::

Verbinde einen GHL-Controller unter **Einstellungen → [dein Becken] → GHL-Controller (Beta)**. Trag seine IP-Adresse in deinem Netzwerk ein und tippe auf **Erkennen**. Cora versucht zuerst die offizielle API des Controllers, dann seine anderen Schnittstellen, und sagt dir, welche davon geantwortet hat.

Antwortet nichts und ist der Controller ein ProfiLux mini, bietet Cora einen Ausweg an: Gib seine Zugangsdaten ein, und Cora liest ihn nur lesend aus. Sonst lässt sich an einem mini nichts steuern.

Steuerungen bleiben aus, bis du **Steuerung durch Cora zulassen (Beta)** auf der Seite des Geräts einschaltest. Das ist standardmäßig aus. Ist es eingeschaltet, kannst du eine Steckdose auf **Immer an**, **Immer aus** oder **Zurueck zu automatisch** stellen, und ein Sollwert wie Temperatur oder pH zeigt seinen erlaubten Bereich und weist einen Wert außerhalb davon zurück. Beide Arten von Änderung werden auf dem Controller selbst gespeichert und bleiben dort, auch wenn Cora später den Kontakt zu ihm verliert. Sieht eine Änderung nach Heizer oder Rückförderpumpe aus, fragt Cora dich zweimal.

Nimmt der Controller eine Änderung nicht an, ist seine GHL-API wahrscheinlich ausgeschaltet. GHL schaltet sie nach jedem Firmware-Update wieder aus. Schalte sie unter **System → GHL API** im GHL Control Center oder in GHL Connect wieder ein. Den Rest findest du unter [Problembehebung](/help/troubleshooting).

## HYDROS

:::note HYDROS wird als Beta unterstützt
Die Unterstützung für HYDROS wird noch getestet und weiterentwickelt. Manche Messwerte oder Steuerungen funktionieren vielleicht noch nicht, und was du hier siehst, kann sich mit Updates ändern.
:::

HYDROS ist die einzige Anbindung, die ihren Controller über die Cloud erreicht. Deshalb funktioniert sie auch, wenn Cora Max in einem anderen Netzwerk ist als der Controller. Verbinde ihn unter **Einstellungen → [dein Becken] → HYDROS (Beta)**.

Leg in der HYDROS-App einen Geräteschlüssel für den Anbieter **cora-iq** an, mit **Lesen** für nur Messwerte oder **Schreiben**, um ihn auch zu steuern. Füg den Schlüssel ein, tippe auf **Prüfen**, wähl das Becken und dann **Speichern**. Die letzten 33 Tage seiner Historie werden importiert, sobald er verbunden ist.

Lesen und Steuern funktioniert genauso wie auf deinem Handy; unter [Deine Ausrüstung steuern](/help/mobile-device-control) stehen Ausgänge, Modi, Dosierköpfe und Testbefehle sowie die Dosierungsgrenzen pro Kopf.

## Zeitpläne

Tagesprogramme für Jecod-Pumpen kannst du an der Wand genauso erstellen wie auf dem Handy. Der Editor ist derselbe, mit Tagesgrafik, Liste der Zeiträume und einer Zeile mit Aktionen. Mehr dazu unter [Ausrüstung planen](/help/mobile-schedules).

Den Zeitplan einer Maxspect-Gyre *(Beta)* kannst du hier ansehen, aber nicht speichern. Stell ihn in der Maxspect-App ein.

## Steckdosen

Steckdosen erreichst du auch über die Schublade **Steckdosen & Füttern** am unteren Rand des Dashboards. Dort stehen alle Steckdosen, die für dieses Dashboard freigegeben sind (oder alle, wenn du keine ausgewählt hast). Mehr dazu unter [Steckdosen und Steuerung](/help/max-controls).

DŌS-Köpfe erscheinen nie in der Steckdosenliste. So kann dort niemand einen Kopf einschalten und laufen lassen. Dosiere immer über die Seite des Kopfes. Ein großer Apex mit mehreren Modulen zeigt alle seine Steckdosen und Sonden.

## Verbrauchsmaterial

Die Schwellen fürs Nachfüllen (Reagenz, Behälter, Reservoirs) legst du hier auf der Seite des Geräts fest, genau wie auf dem Handy. Mehr dazu unter [Verbrauchsmaterial](/help/mobile-consumables).

## Am Becken eintragen und rechnen

Zwei Dinge gehen an der Wand oft bequemer als auf dem Handy:

- **Werte erfassen**: Trag Testergebnisse über die Bildschirmtastatur ein. Du findest das im Beckenmenü.
- **Dosierrechner**: Berechne eine Korrektur mit dem Beckenvolumen und der Stärke deiner Produkte. Du öffnest ihn auf der Seite eines Wasserwerts. Er nutzt dasselbe Volumen und dieselben Produktstärken wie das Handy, daher kommt hier dieselbe Dosis heraus wie dort. Mehr dazu unter [Dosierung](/help/mobile-dosing).

## Auf einem zweiten Cora Max

Zeigen mehrere Cora Max dasselbe Becken, liest nur eines davon die Ausrüstung dieses Beckens. Auf den Geräteseiten heißt es das Cora Max am Becken. Die anderen öffnen die Geräteseiten trotzdem. Steht im Status-Chip **Cloud**, ist dieser Bildschirm einer der anderen. Sie zeigen, was das Cora Max am Becken zuletzt gelesen hat und wie lange das her ist. Jeden Befehl schicken sie über Cora Cloud an dieses Cora Max, das ihn dann ausführt.

Ein paar Dinge gehen nur am Cora Max am Becken:

- **Zum Dosieren messen** und **Erneut messen** gibt es nur dort. Ist ein Kopf gemessen, funktioniert **Jetzt dosieren** auf jedem Cora Max.
- Einen Jecod-Zeitplan kannst du von einem anderen Cora Max nur ändern, wenn das Cora Max am Becken die Pumpe in der letzten Stunde gelesen hat. Bei einer Pumpe, die nur über Bluetooth spricht, geht das nie. Ein **Auf die Pumpe anwenden** von dort schickt höchstens 12 Änderungen. Größere Änderungen schickst du also in mehreren Teilen.

## Was geändert wurde, und von was

Jede Aktion wird mit ihrem Auslöser festgehalten. Mehr dazu unter [Aktivität und Zeitleiste](/help/mobile-activity).

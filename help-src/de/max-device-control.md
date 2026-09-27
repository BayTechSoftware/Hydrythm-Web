---
title: Ausrüstung von Cora Max aus steuern
description: Geräteseiten auf dem großen Bildschirm: Sonden, Steckdosen, Dosierköpfe, Testgeräte und Pumpen.
section: Cora Max
reviewed: 2026-09-27
order: 6
group: Equipment
---

Cora Max erreicht dieselbe Ausrüstung wie dein Handy, mit einer Seite für jedes Gerät. Öffne sie über **Einstellungen → Geräte**, oder durch Tippen auf eine Gerätekachel im Dashboard.

![Eine Apex-Seite auf Cora Max](img/max-device-control.webp "Fütterungszyklen und jede Steckdose, für einen Wandbildschirm angeordnet.")

:::warning Diese Steuerungen wirken auf echte Ausrüstung
Es gibt keine Vorschau und kein Rückgängig. Ein Befehl geht in dem Moment hinaus, in dem du tippst, aber *gesendet* ist nicht *erledigt*: Er kommt als **Bestätigt**, **Unbestätigt**, **Abgelehnt** oder **Keine Änderung** zurück, und [Aktivität](/help/max-activity) ist der Ort, an dem du siehst, welches davon zutraf.
:::

## Was eine Seite hat

| Gerät | Zeigt |
|---|---|
| **Neptune Apex** | Sonden und Steckdosen, jede Steckdose schaltbar |
| **Trident** | Teststatus, Reagenz- und Abfallstände, und die Möglichkeit, einen Test zu starten |
| **DŌS**, einschließlich DŌS QD | Die Dosierung, den Zeitplan, die Reichweite und das Behältervolumen jedes Kopfes (mit Pausieren, Befüllen, Jetzt dosieren und einer einmaligen zwanzigsekündigen Messung) |
| **Red Sea ReefBeat** | Was das Gerät auch ist: Dosierköpfe, Reservoir, Rollentage, Pumpenmodus |
| **Jecod** | Pumpenmodus und Intensität, und ihr Tagesprogramm |
| **Maxspect** *(Beta)* | Modus und Geschwindigkeit für **Gyre A** und **Gyre B**, **Pumpenzustand** (Reinigungs-Countdown, Strom von Kopf A, eingebaute Köpfe, Firmware), und ihr Zeitplan, nur zur Ansicht |

Wenn sich ein Red Sea-Gerät selbst anhält, sagt seine Seite, was nicht stimmt, und stellt die Lösung daneben: **Fortsetzen**, **Notstopp aufheben**, **Sensor gereinigt**, **Ich habe bereits eine neue Rolle eingelegt**, oder **Zurücksetzen** für einen Dosierkopf.

## DŌS-Köpfe

Ein DŌS-Kopf muss einmal gemessen werden, bevor Cora ihn manuell dosiert. **Zum Dosieren messen** lässt den Kopf zwanzig Sekunden in einen Messbehälter laufen, und du gibst ein, wie viel herauskam. Cora behält eine Messung pro Kopf und nutzt die neueste, egal welches Cora Max sie durchgeführt hat; die Seite des Kopfes zeigt, wo und wann er gemessen wurde.

Nach einer manuellen Dosierung bleibt ein Kopf, den du in Apex Fusion auf Aus gestellt hattest, aus. Jeder andere Kopf geht zurück auf Auto.

### Wofür ein Kopf verwendet wird

Jeder Kopf kann über sein Einstellungsblatt auf einen **Verwendungstyp** eingestellt werden: **Supplement**, **Wasserwechsel: neues Salzwasser rein**, **Wasserwechsel: altes Wasser raus**, **Kalkwasser**, **Calciumreaktor**, **Futter** oder **Nachfüllen**, oder **Andere**. Der Verwendungstyp ändert zwei Dinge:

- **Wie groß ein Behälter sein kann, den er verfolgt.** Ein Supplement-Kopf verfolgt bis zu 20 Liter; jeder andere Verwendungstyp kann einen deutlich größeren Behälter verfolgen, bis zu 500 Liter, sodass ein Kopf, der einen Wasserwechsel oder einen Calciumreaktor betreibt, nicht wie eine kleine Dosierflasche behandelt wird.
- **Ob er eine große manuelle Dosierung annehmen kann.** Supplement- und Futter-Köpfe behalten die heutige kleine, vorsichtige Obergrenze. Jeder andere Verwendungstyp kann sein eigenes Limit **Größte manuelle Dosierung** bekommen, bis zu einer festen Obergrenze von 10 Litern, und sein eigenes **Tageslimit für Automationen und den Assistenten**.

Ein Wasserwechsel-Paar (neues Salzwasser rein, altes Wasser raus) kann als **Gekoppelter Kopf** verbunden werden, mit einem Betrag **Ausgleichswarnung ab**: Wenn die Tagessummen der beiden Köpfe um mehr als diesen Betrag voneinander abweichen, warnt Cora, weil ein aus dem Gleichgewicht geratenes Paar meist bedeutet, dass eine Seite nicht wie erwartet pumpt.

### Wenn eine große Dosierung unterbrochen wird

Eine große Dosierung ändert vorübergehend, was der Kopf am Apex tut, und stellt danach seinen normalen Zeitplan wieder her. Bricht die Verbindung mitten in der Ausführung ab, zeigt Cora Max einen Banner auf der Seite dieses Kopfes: *"Eine große Dosierung an [Kopf] wurde nicht sauber abgeschlossen. Cora versucht weiterhin, sein Programm zurückzusetzen; prüfe es in Apex Fusion."*

Prüfe den Kopf selbst in Apex Fusion, und tippe dann auf **Ich habe den Kopf in Fusion geprüft**, um den Banner zu entfernen. Tu das erst, nachdem du bestätigt hast, dass der eigene Zeitplan des Kopfes läuft, nicht Coras Dosierprogramm.

**Wenn es nicht funktioniert:** Wenn der Banner sich nicht entfernen lässt, oder immer wieder zurückkommt, siehe [Problembehebung](/help/troubleshooting).

## Zeitpläne

Tagesprogramme für Jecod-Pumpen können auch an der Wand erstellt werden, genauso wie auf dem Handy. Der Editor ist derselbe: ein Tagesgraph, eine Zeitraumliste, und eine Aktionszeile. Siehe [Ausrüstung planen](/help/mobile-schedules).

Der Zeitplan einer Maxspect-Gyre *(Beta)* kann hier angesehen, aber nicht gespeichert werden. Lege ihn in der Maxspect-App fest.

## Steckdosen

Steckdosen sind auch über die Schublade **Steckdosen & Fütterung** am unteren Rand des Dashboards erreichbar, die die für dieses Dashboard freigegebenen Steckdosen an einem Ort listet (alle, wenn keine ausgewählt wurden). Siehe [Steckdosen und Steuerungen](/help/max-controls).

DŌS-Köpfe erscheinen nie in der Steckdosenliste, daher kann ein Kopf dort nicht eingeschaltet und laufen gelassen werden; dosiere von seiner eigenen Seite aus. Ein großer Apex mit mehreren Modulen zeigt alle seine Steckdosen und Sonden.

## Verbrauchsmaterial

Nachfüllschwellenwerte (Reagenz, Behälter, Reservoirs) werden hier von der eigenen Seite des Geräts festgelegt, genau wie auf dem Handy. Siehe [Verbrauchsmaterial](/help/mobile-consumables).

## Am Becken protokollieren und berechnen

Zwei Dinge sind an der Wand oft bequemer als auf einem Handy:

- **Wasserwerte protokollieren**: Testergebnisse über die Bildschirmtastatur eintragen, aus dem Beckenmenü
- **Dosierrechner**: eine Korrektur mit dem Volumen des Beckens und deinen Produktstärken berechnen, von der Seite eines Wasserwerts aus. Er nutzt dasselbe Volumen und dieselben Produktstärken wie das Handy, daher stimmt eine hier berechnete Dosierung mit einer dort berechneten überein. Siehe [Dosierung](/help/mobile-dosing).

## Auf einem zweiten Cora Max

Wenn mehr als ein Cora Max ein Becken zeigt, liest eines von ihnen die Ausrüstung dieses Beckens; die Geräteseiten nennen es das Cora Max am Becken. Die anderen öffnen die Geräteseiten trotzdem (eine Status-Pille, die **Cloud** liest, bedeutet, dass dieser Bildschirm einer von ihnen ist). Sie zeigen, was das Cora Max am Becken zuletzt gelesen hat, und wie lange das her ist, und leiten jeden Befehl über Cora Cloud an dieses Cora Max zur Ausführung weiter.

Ein paar Dinge bleiben beim Cora Max am Becken:

- **Zum Dosieren messen** und **Erneut messen** erscheinen nur dort. Sobald ein Kopf gemessen ist, funktioniert **Jetzt dosieren** von jedem Cora Max.
- Ein Jecod-Zeitplan kann von einem anderen Cora Max nur geändert werden, wenn das Cora Max am Becken die Pumpe in der letzten Stunde gelesen hat, und nie für eine Pumpe, die nur über Bluetooth spricht. Ein **Auf die Pumpe anwenden** von dort sendet höchstens 12 Änderungen, daher sende eine größere Bearbeitung in Teilen.

## Was geändert wurde, und von was

Jede Aktion wird mit ihrer Ursache erfasst. Siehe [Aktivität und Zeitleiste](/help/mobile-activity).

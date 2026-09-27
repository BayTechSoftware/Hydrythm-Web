---
title: Warnungen und Schwellenwerte
description: Lege den Bereich für jeden Wasserwert fest, wähle, worüber du informiert werden willst, und verstehe, warum eine Warnung ausgelöst wurde.
section: Cora Mobile
reviewed: 2026-09-27
order: 15
group: Alerts and automation
---

Eine Warnung wird ausgelöst, wenn ein Messwert den dafür festgelegten Bereich verlässt. Du legst die Bereiche fest, und du steuerst, welche Warnungen dein Handy erreichen.

Öffne die **Warnzentrale** aus der Verknüpfungsreihe am unteren Rand des Dashboards.

![Die Warnzentrale](img/mobile-alerts.webp "Aktive Warnungen, jede mit ihrem Schweregrad, was sie ausgelöst hat, und wann.")

## Die Warnzentrale

Zwei Tabs:

- **Aktiv**: derzeit ausgelöste Warnungen, mit einem Zähler-Abzeichen
- **Regeln**: die Schwellenwert- und Änderungsraten-Regeln, die sie erzeugen

Jede aktive Warnung zeigt den Wasserwert und das Becken, den Messwert, der sie ausgelöst hat, eine einfache Erklärung, ein Schweregrad-Chip, die Art der ausgelösten Regel (**Schwellenwert** oder **Änderungsrate**), und den Zeitpunkt, zu dem sie ausgelöst wurde.

Zwei Aktionen bei jeder:

- **Regel ansehen**: öffnet die Regel, die sie ausgelöst hat, damit du den Bereich anpassen kannst
- **Diese Warnung erklären**: bittet den Assistenten, sie im Licht der Historie deines Beckens zu interpretieren

## Einen Bereich festlegen

Wasserwerte, die Cora bewerten kann, haben einen Zielbereich, und die Standardwerte stammen von deinem Beckentyp und -alter, die du bei der Einrichtung angegeben hast, meist ein vernünftiger Ausgangspunkt. Ein Wasserwert ohne nutzbaren Bereich wird gar nicht bewertet: Er bleibt neutral grau, statt geraten zu werden.

Um einen zu ändern: **Halte das Widget lange gedrückt** auf dem Dashboard, was direkt die Schwellenwerte dieses Wasserwerts öffnet. Ein einfaches Tippen öffnet stattdessen die Wasserwert-Ansicht; die beiden Gesten führen an verschiedene Orte, und das lange Drücken ist die Verknüpfung, die sich zu merken lohnt.

Wenn der Wasserwert noch keine Regel hat, starten die Felder mit Coras Standardwert, und ein Hinweis darunter sagt das auch. Ändere einen beliebigen Wert, um deinen eigenen festzulegen.

Um sie alle zusammen zu sehen, nutze **Warnungen** in der Schaltflächenreihe unter dem Dashboard.

Du kannst festlegen:

- **Einen Bereich**: eine Unter- und eine Obergrenze, für Dinge wie Alkalinität oder Temperatur
- **Eine Obergrenze**: nur eine Obergrenze, für Dinge, bei denen niedrig in Ordnung ist, wie Nitrat oder Phosphat
- **Eine Untergrenze**: nur eine Untergrenze

:::tip Lege den Bereich fest, in dem dein Becken tatsächlich läuft
Die Standardwerte sind ein Ausgangspunkt, kein Urteil. Ein Becken, das nährstoffarm bei 6 dKH läuft, ist nicht "falsch", weil eine Tabelle 8–9 gesagt hat. Lege den Bereich fest, in dem du tatsächlich läufst, und Cora sagt es dir, wenn *du* davon abweichst.
:::

## Was eine Warnung auslöst

Eine Warnung wird ausgelöst, wenn ein Messwert einen Schwellenwert überschreitet. Cora prüft jeden Messwert, sobald er eintrifft, daher reicht ein einzelner Messwert außerhalb deines Bereichs aus, um eine auszulösen.

Sobald eine Warnung aktiv ist, benachrichtigt sie dich nicht ständig erneut über dieselbe Sache; es gibt eine Abklingzeit, bevor sie erneut ausgelöst werden kann. Und sie **löscht sich selbst** in dem Moment, in dem ein Messwert wieder in den Bereich zurückkehrt; es gibt nichts zu bestätigen.

Du kannst außerdem eine **Änderungsraten**-Regel festlegen, die beobachtet, wie schnell sich ein Wasserwert bewegt, statt wo er gerade steht. Das ist die richtige für Dinge, bei denen die Geschwindigkeit einer Veränderung wichtiger ist als die Zahl.

## Wo Warnungen erscheinen

- **Die Glocke**, oben rechts auf jedem Bildschirm, enthält deine Historie. Die Zahl zeigt, wie viele du noch nicht gelesen hast.
- **Push-Benachrichtigungen** erreichen dein Handy, wenn du sie erlaubst.
- **Das Widget** wird auf dem Dashboard gelb oder rot.
- **Cora Max** zeigt dieselben Warnungen auf dem großen Bildschirm.

## Wenn Ausrüstung Aufmerksamkeit braucht

Manche Warnungen betreffen Ausrüstung statt eines Messwerts. Wenn ein Gerät wie ein Trident oder eine Jecod-Pumpe einen Fehler meldet, sendet Cora eine Benachrichtigung, die das Becken und das Gerät benennt, zum Beispiel *"Display-Becken: Rückförderpumpe braucht Aufmerksamkeit"*, und sagt, was nicht stimmt, etwa ein blockierter Rotor. Wenn der Fehler behoben ist, folgt eine zweite: *"Display-Becken: Rückförderpumpe ist wieder in Ordnung"*. Beide fallen unter **Gerätefehler** in **Einstellungen → Benachrichtigungen**.

Eine Maxspect-Gyre (Beta) kann dieselbe Warnung auslösen, wenn ein Cora Max in ihrem Netzwerk feststellt, dass beide Köpfe auf 0 % stehen, oder zweimal in Folge keine Antwort von der Gyre bekommt. Behandle das als Warnung, nicht als Absicherung: Das Cora Max prüft von Zeit zu Zeit, nicht dauerhaft, und nur während es läuft und die Gyre erreichen kann.

## "Red Sea-Messwerte haben aufgehört, sich zu aktualisieren"

Auf der Wasserwert-Seite eines Beckens könntest du diesen Banner sehen:

> Red Sea-Messwerte haben aufgehört, sich zu aktualisieren. Kein Gerät liest derzeit die Red Sea-Geräte dieses Beckens: Prüfe Primäres Cora Max in den Einstellungen, oder öffne dieses Becken auf einem Gerät im selben WLAN.

Das bedeutet, dass gerade kein Handy oder Cora Max die ReefBeat-Ausrüstung dieses Beckens abfragt, daher sind die gezeigten Messwerte alt, nicht notwendigerweise falsch. Tippe auf den Banner, um **Primäres Cora Max** zu öffnen, und wähle entweder ein Gerät, das eingeschaltet ist, oder stelle es auf **Jedes aktive (automatisch)**. Siehe [Mehr als ein Cora-Gerät](/help/mobile-multi-device). Wenn es nicht verschwindet, siehe [Problembehebung](/help/troubleshooting).

## Wählen, was dich erreicht

**Einstellungen → Benachrichtigungen.** Du kannst steuern:

- Welche der Benachrichtigungskategorien senden dürfen

Reef Buddy hat keinen eigenen Schalter: Es sendet eine Zusammenfassung, wenn es etwas gibt, das eine Handlung wert ist, und bleibt still, wenn nicht.

:::note Cora ist darauf ausgelegt, still zu bleiben
Die tägliche Zusammenfassung ist ein Push pro Becken pro Tag, und an einem Tag, an dem nichts deine Aufmerksamkeit braucht, bleibt sie meist still, statt dir mitzuteilen, dass alles in Ordnung ist. Wenn Cora sendet, hat sich etwas geändert.
:::

## Abklingzeiten: wie oft dieselbe Warnung dich benachrichtigen darf

Jede Regel hat ihre eigene **Abklingzeit zwischen Warnungen**, festgelegt, wenn du die Regel hinzufügst oder bearbeitest (im Tab **Regeln** der Warnzentrale). Die Abklingzeit versteckt die Warnung selbst nicht: Sie begrenzt nur, wie oft Cora dir einen Push darüber sendet. Der Messwert bleibt die ganze Zeit bewertet, und die Warnung bleibt auf dem Widget und in der Glocke sichtbar.

Du kannst wählen zwischen: 15 Min., 30 Min., 1 Std., 2 Std., 4 Std., 8 Std., 1 Tag, 3 Tage, oder **1 Woche**.

Eine kurze Abklingzeit passt zu einem schnell wechselnden Messwert wie Temperatur. Eine lange, bis zu einer Woche, passt zu etwas, das tagelang falsch bleibt, während du auf ein Ersatzteil wartest, etwa ein Trident ohne Reagenz oder ein leerer Dosierbehälter: Ohne eine lange Abklingzeit würde Cora mehrmals am Tag über dasselbe bekannte Problem senden.

:::note Eine aktive Warnung schlummern legen läuft auf Cora Max
Cora Mobile hat auf einer aktiven Warnung keine eigene Schlummern-Schaltfläche; diese Steuerung befindet sich auf dem Cora Max-Bildschirm am Becken, und sie schaltet dieselbe Warnung für die hier gewählte Abklingzeit stumm. Vom Handy aus änderst du, wie oft du davon hörst, über diese Abklingzeit pro Regel, nicht über ein Schlummern pro Warnung.
:::

## Eine Warnung löschen

Eine Warnung wird gelöscht, wenn der Messwert wieder in den Bereich zurückkehrt. Es gibt nichts zu verwerfen; es ist eine Aussage über das Becken, keine Aufgabe.

:::note Vorübergehende Messwerte lösen Warnungen aus
Ein einzelner Messwert außerhalb des Bereichs reicht aus, um eine Warnung auszulösen, daher löst eine Sonde, die kurz ausschlägt, eine aus. Wenn eine Quelle unzuverlässig ist, kalibriere sie neu, oder richte das Widget auf eine andere Quelle, statt den Schwellenwert zu erweitern.
:::

Wenn ein Messwert falsch ist, statt dass das Becken falsch liegt (eine Sonde, die kalibriert werden muss, zum Beispiel), behebe die Quelle. Einen Schwellenwert zu erweitern, um eine schlechte Sonde zum Schweigen zu bringen, versteckt auch das nächste echte Problem.

## Warnungen für einen Wasserwert deaktivieren

Öffne die Regel im Tab **Regeln** der Warnzentrale, und schalte ihren **Aktivierungsschalter** aus. Die Regel und ihr Bereich bleiben erhalten, sodass du sie wieder einschalten kannst, ohne sie neu aufzubauen.

:::warning Einen Wasserwert stummschalten, ohne seinen Bereich zu löschen
Einen Schwellenwert zu entfernen, stoppt nicht notwendigerweise jede Bewertung dieses Messwerts; Standard-Referenzbänder färben den Wert weiterhin ein und können weiterhin in die Zusammenfassung einfließen. Nutze den Aktivierungsschalter der Regel.
:::

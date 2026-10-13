---
title: Szenen auf Cora Max
description: Szenen auf Cora Max anlegen, starten, bearbeiten und löschen, über Einstellungen → Automationen oder eine Szenen-Kachel auf dem Dashboard.
section: Cora Max
reviewed: 2026-10-13
order: 9
group: Alerts and automation
twin: mobile-automation
---

Eine **Szene** ist eine gespeicherte Gruppe von Aktionen für deine Ausrüstung, die zusammen ablaufen, entweder eine feste Zeit lang oder bis du sie stoppst. Du kannst Szenen auf Cora Max anlegen, starten und bearbeiten. Szenen, die du auf dem Handy und auf Cora Max anlegst, sind dieselben Szenen. Automationsregeln (die Art "wenn das passiert, tu das") richtest du auf dem Handy ein. Mehr dazu unter [Automationen und Szenen](/help/mobile-automation).

![Die Szenenliste auf Cora Max, mit einem Filter-Chip für jedes Becken und einer Taste Neue Szene](img/max-automation.webp "Die Szenenliste, nach Becken gefiltert. Gibt es noch keine Szenen, steht das dort, und Neue Szene wird angeboten.")

## Wo du Szenen findest

**Einstellungen → Automationen** öffnet **Szenen**, die Liste aller Szenen für alle deine Becken. Hast du mehr als ein Becken, gibt es für jedes einen Filter-Chip und dazu **Alle Becken**.

Tippe auf eine Szene, um sie zu bearbeiten, oder auf **Neue Szene**, um eine anzulegen. Hast du mehr als ein Becken und ist kein Filter gewählt, fragt Cora Max **Für welches Becken ist diese Szene?**

## Eine Szene anlegen

![Ein leeres Formular Neue Szene auf Cora Max](img/max-scene-builder.webp "Eine neue Szene: ein Name, Dauerhaft oder Zeitgesteuert, Vor der Ausführung fragen, dann Schritt hinzufügen.")

1. Gib einen **Szenenname** ein.
2. Tippe auf **Schritt hinzufügen** und wähl, was der Schritt tut. Du siehst nur die Arten von Ausrüstung, die dieses Becken hat:
   - **Apex-Steckdose**: eine Neptune Apex-Steckdose auf **EIN**, **AUS** oder **AUTO** schalten.
   - **Ein Red-Sea-Gerät steuern**: zum Beispiel **ReefDose: jetzt dosieren**, **ReefDose: Tagesdosis einstellen**, **ReefRun: Pumpengeschwindigkeit einstellen**, **ATO: manuelle Befüllung starten** oder **ReefMat: Rolle weiterdrehen**.
   - **Eine Strömungspumpe steuern**: Strömung oder Wellenmodus einer Jecod-Pumpe einstellen, sie ein- oder ausschalten oder **Für Fütterung pausieren**.
   - **Eine Gyre-Fütterung starten**: eine Maxspect-Gyre für die Fütterung pausieren. Sie startet danach von selbst wieder.
   - **GHL**: eine Fütterungspause, Wartung, Wasserwechsel, Lichtszene und andere Controller-Befehle.
   - **HYDROS**: ein Modus, eine Ausgangsstufe, eine Dosierung oder **HYDROS: zurück zum Zeitplan**.
3. Füg auf dieselbe Weise weitere Schritte hinzu. Du kannst sie umsortieren oder entfernen. Ein Schritt, den dieser Bildschirm nicht bearbeiten kann, zeigt **Hier nicht bearbeitbar**. Bearbeite ihn auf dem Handy.
4. Wähl, wie lange sie läuft. **Zeitgesteuert** läuft so viele Minuten, wie du unter **Laufzeit (Minuten)** festlegst. **Dauerhaft** läuft, bis du sie stoppst.
5. Lass **Vor der Ausführung fragen** eingeschaltet, außer du bist sicher, dass die Szene nie etwas berührt, das einen zweiten Blick braucht.
6. Tippe auf **Speichern**.

:::note Dosierungen in einer Szene
Ein Neptune DŌS-Kopf kann nie ein Szenenschritt sein. Ein Schritt **ReefDose: jetzt dosieren** schon, und er hat sein eigenes **Max. pro Dosis (ml)**. Lass es leer für 10 ml. Eine Dosierung über dieser Obergrenze wird abgelehnt, nie verkleinert. Lass **Vor der Ausführung fragen** bei jeder Szene eingeschaltet, die dosiert.
:::

:::note Beta
**Beta.** Maxspect, GHL und HYDROS sind in der Beta und nur für Beta-Nutzer offen. Wenn du kein Beta-Nutzer bist, siehst du sie nicht unter **Gerät hinzufügen**. Für Beta-Zugang wende dich an den [Support](/support.html).
:::

## Eine Szene starten

Szenen erscheinen als Kacheln auf dem Dashboard. Tippe auf **Start**, um eine zu starten.

Fragt die Szene vor der Ausführung, listet Cora Max zuerst auf, was gleich passiert, eine Zeile pro Schritt. Lies es und starte sie dann oder brich ab.

Während eine zeitgesteuerte Szene läuft, zählt ihre Kachel bis zum Ende herunter und zeigt **Stopp**, falls du sie früher beenden willst. Die Kachel einer dauerhaften Szene zeigt sie als laufend, bis du auf **Stopp** tippst. Wenn eine Szene endet oder du sie stoppst, zeigt die Kachel **Wiederherstellen…**, während Cora die Ausrüstung zurückstellt.

Das Starten oder Stoppen einer Szene läuft wie jeder andere Befehl über Cora Cloud. Das Ergebnis findest du unter [Aktivität](/help/max-activity).

Szenen lassen sich auf Cora Max nicht per Sprache starten. Nutze die Kachel, **Einstellungen → Automationen** oder dein Handy.

Lässt sich eine Szene nicht starten oder nicht stoppen, schau in die [Problembehebung](/help/troubleshooting).

:::note Die Kindersicherung gilt auch für Szenen
Solange die [Kindersicherung](/help/max-settings#child-lock) den Bildschirm gesperrt hat, kannst du dort keine Szene starten, stoppen oder bearbeiten, genau wie bei jeder anderen Steuerung.
:::

## Eine Szene bearbeiten oder löschen

Um eine Szene zu ändern, öffne sie über **Einstellungen → Automationen** oder drück lange auf ihre Kachel auf dem Dashboard. Ändere, was du brauchst, und tippe auf **Speichern**. Um sie zu entfernen, tippe auf **Szene löschen**. Das lässt sich nicht rückgängig machen.

:::note Ein älteres Cora Max kann eine Szene starten, aber nicht bearbeiten
Ältere Cora Max-Versionen zeigen und starten weiterhin jede Szene, können aber keine ändern. Aktualisiere Cora Max ([Updates und Wiederherstellung](/help/max-updates)) oder bearbeite die Szene auf dem Handy.
:::

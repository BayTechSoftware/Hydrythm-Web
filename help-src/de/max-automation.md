---
title: Szenen auf Cora Max
description: Szenen direkt auf dem Cora Max-Bildschirm erstellen, ausführen und bearbeiten.
section: Cora Max
reviewed: 2026-09-27
order: 15
group: Automation
---

Eine **Szene** ist eine gespeicherte Gruppe von Ausrüstungsaktionen, die gemeinsam läuft, entweder für eine feste Zeit oder bis du sie stoppst. Szenen funktionieren gleich, egal ob du sie auf deinem Handy oder auf Cora Max erstellst; diese Seite deckt ab, wie du das an der Wand tust.

## Wo du Szenen findest

**Einstellungen → Automationen** listet jede Szene über jedes deiner Becken, mit einem Filter-Chip für jedes Becken, wenn du mehr als eines hast. Sie öffnet dieselbe Liste, egal ob die Szene auf dem Handy oder auf Cora Max erstellt wurde.

Tippe auf eine Szene, um sie zu bearbeiten, oder auf **+**, um eine neue zu erstellen. Wenn du mehr als ein Becken hast und kein Filter gewählt ist, fragt Cora Max, zu welchem Becken die neue Szene gehört.

## Eine Szene erstellen

1. Gib der Szene einen **Namen**.
2. Füge **Schritte** hinzu. Von Cora Max aus kann ein Schritt eine Apex-Steckdose schalten (**Ein**, **Aus** oder **Auto**) oder eine Zigbee-Steckdose (**ein**, **aus** oder **umschalten**). Schritte, die auf dem Handy für andere Arten von Ausrüstung hinzugefügt wurden, erscheinen trotzdem hier, und können weiterhin neu geordnet oder entfernt werden, auch wenn dieser Bildschirm keinen weiteren dieser Art hinzufügen kann.
3. Wähle, wie lange sie läuft: eine feste Anzahl von Minuten, oder **dauerhaft** (sie läuft weiter, bis du sie stoppst).
4. Wähle, ob das Ausführen der Szene einen **Bestätigungsschritt** braucht. Lass das eingeschaltet, sofern du dir nicht sicher bist, dass die Szene nie etwas berührt, das unsicher zu ändern wäre, ohne noch einmal hinzusehen.
5. Speichern.

:::note DŌS-Dosierköpfe sind nie ein Szenenschritt
Eine Szene, ob auf Cora Max oder auf dem Handy erstellt, kann niemals einen Dosierkopf einschalten. Das ist Absicht: Eine Dosierung ist nicht die Art von Aktion, die eine Szene versehentlich auslösen sollte.
:::

## Eine Szene ausführen

Szenen erscheinen als Kacheln auf dem Dashboard. Tippe auf **Start**, um eine zu beginnen.

Wenn die Szene eine Bestätigung braucht, listet Cora Max genau auf, was sie gleich tun wird, eine Zeile pro Schritt, bevor irgendetwas passiert. Lies es, und entscheide dann, sie auszuführen oder abzubrechen.

Während eine zeitbegrenzte Szene läuft, zeigt ihre Kachel einen Countdown bis zu ihrem Ende, und eine **Stopp**-Schaltfläche, um sie vorzeitig zu beenden. Die Kachel einer dauerhaften Szene bleibt in ihrem laufenden Zustand, bis du sie stoppst.

Eine Szene auszuführen oder zu stoppen läuft immer über Cora Cloud, genauso wie jeder andere Befehl; siehe [Was geändert wurde, und von was](/help/max-activity) für den Ort, an dem das Ergebnis erfasst wird.

**Wenn es nicht funktioniert:** Wenn eine Szene sich nicht starten oder nicht stoppen lässt, siehe [Problembehebung](/help/troubleshooting).

:::note Die Kindersicherung deckt auch Szenen ab
Wenn die [Kindersicherung](/help/max-voice) eingeschaltet ist, ist das Ausführen oder Stoppen einer Szene von diesem Bildschirm aus zusammen mit jeder anderen Steuerung blockiert. Fragen zu einer Szene funktionieren per Sprache weiterhin; sie zu starten oder zu stoppen nicht.
:::

## Eine Szene bearbeiten oder löschen

Öffne die Szene über **Einstellungen → Automationen**, oder halte ihre Kachel auf dem Dashboard lange gedrückt, um ihren Namen, ihre Schritte, Dauer oder Bestätigungseinstellung zu ändern, oder um sie zu löschen.

:::note Ältere Cora Max-Bildschirme können eine Szene ausführen, aber nicht bearbeiten
Szenen an der Wand zu erstellen und zu bearbeiten ist eine neuere Cora Max-Fähigkeit. Ein älteres Cora Max im selben Konto kann trotzdem eine Szene zeigen und ausführen, die auf dem Handy oder auf einem neueren Cora Max erstellt wurde; es kann sie einfach nicht ändern. Aktualisiere Cora Max, oder bearbeite die Szene vom Handy oder von einem neueren Bildschirm aus, wenn das vorkommt.
:::

Siehe [Szenen und Automationen](/help/mobile-automation) für mehr Details dazu, was eine Szene tun kann, und wie sie auf dem Handy erstellt werden.

---
title: Aktivität und Zeitleiste
description: Jede Änderung sehen, die an deine Ausrüstung geschickt wurde, wer oder was sie ausgelöst hat und ob sie geklappt hat, und die Zeitleiste des Beckens rund um ein Datum lesen.
section: Cora Mobile
reviewed: 2026-10-18
order: 31
group: Records
twin: max-activity
---

Die Aktivität listet jeden Versuch auf, etwas an deiner Ausrüstung zu ändern: Steckdosen schalten, Fütterungszyklen, Dosierungen und alles, was eine Szene oder Automation getan hat. Jede Zeile zeigt, was es ausgelöst hat und was danach passiert ist, auch bei den Anfragen, die nicht geklappt haben.


Geh zu **Einstellungen → Aktivität**. Hast du mehr als ein Becken, wähl es mit den Becken-Chips oben.

![Die Aktivität in Cora Mobile](img/mobile-activity.webp "Oben die Legende der Ergebnisse, dann jede Aktion mit Ergebnis, Auslöser und Weg.")

## Was die Ergebnisse bedeuten {#outcomes}

Jede Zeile hat ein Ergebnis. Dieselbe Legende steht oben auf dem Bildschirm unter **WAS DIE ERGEBNISSE BEDEUTEN**.

| Ergebnis | Bedeutung |
|---|---|
| **Bestätigt** | Das Gerät hat gemeldet, dass es das getan hat |
| **Unbestätigt** | Es wurde gesendet, aber es kam keine Rückmeldung. Vielleicht hat es das Gerät erreicht, vielleicht nicht |
| **Abgelehnt** | Es wurde abgelehnt und nicht ausgeführt. Lies die Zeile, um zu sehen, warum |
| **Keine Änderung** | Die Ausrüstung war schon in diesem Zustand, deshalb wurde nichts gesendet |

Eine Ablehnung ist anders. *Kein Gerät hat rechtzeitig geantwortet* bedeutet, dass die Anfrage trotzdem ausgeführt worden sein kann. Prüf die Ausrüstung, bevor du es noch einmal versuchst.

Ein Befehl, der still nichts getan hat, ist genau das, was du hier finden willst. Deshalb bleiben fehlgeschlagene und wirkungslose Anfragen zusammen mit denen, die geklappt haben, im Protokoll.

## Was es ausgelöst hat {#causes}

Jede Zeile nennt ihren Auslöser:

| Auslöser | Bedeutung |
|---|---|
| **Diese App** | Du hast es in Cora Mobile angetippt |
| **Sprache in dieser App** | Du hast auf diesem Handy per Sprache gefragt |
| **Auf einem Cora getippt** | Jemand hat einen Cora Max-Bildschirm benutzt. Die Zeile sagt, welchen |
| **Sprache an einem Cora Max** | Jemand hat mit einem Cora Max gesprochen |
| **Cora Assistant** | Du hast Cora Assistant in einem Chat darum gebeten |
| **Automationsregel** | Eine [Automation oder Szene](/help/mobile-automation) hat es getan |
| **Von Cora Cloud gesendet** | Es kam von deinem Konto über Cora Cloud |
| **Unbekannte Quelle** | Aufgezeichnet, bevor Cora sagen konnte, woher es kam |

## Welchen Weg es genommen hat {#route}

Jede Zeile hat außerdem einen Chip für den Weg. Wenn etwas schiefgeht, erklärt oft der Weg, auf dem die Anfrage deine Ausrüstung erreicht hat, warum.

| Chip | Bedeutung |
|---|---|
| **LAN** | Über dein eigenes Netzwerk direkt an die Ausrüstung geschickt |
| **ÜBER CLOUD** | Über dein Konto geschickt, für Ausrüstung, die Cora nicht direkt erreicht |
| **ROUTE ?** | Aufgezeichnet, bevor Wege festgehalten wurden, deshalb ist der Weg unbekannt |

Hast du mehr als ein Cora Max, sagt die Zeile auch, welches die Anfrage ausgeführt hat.

## Die Zeitleiste des Beckens {#tank-timeline}

Bei der Aktivität geht es um Ausrüstung. Bei der Zeitleiste des Beckens, auf dem Bildschirm **Riffgeschichte** genannt, geht es um das Becken. Sie zeigt Tagebucheinträge, Wartung, Änderungen am Besatz, Wassertests und Warnungen in zeitlicher Reihenfolge, mit Meilensteinen unterwegs.

Um sie zu öffnen, geh zum [Tagebuch](/help/mobile-journal) und tippe oben auf das Symbol **Beckenzeitleiste**. Mit den Chips oben zeigst du nur **Tagebuch**, **Wartung**, **Besatz**, **Wassertests** oder **Warnungen**, oder **Alle**. **Ältere Geschichte laden** geht weiter zurück. Du kannst auch hier einen **Neuer Eintrag** anlegen oder einen diktieren.

Nimm die Aktivität, wenn du wissen willst *"Was hat etwas getan?"* Nimm die Zeitleiste, wenn du wissen willst *"Was war rund um dieses Datum los?"*

:::note Nutze die Zeitleiste zusammen mit dem Tagebuch
Die Zeitleiste sammelt, was Cora aufgezeichnet hat. Das Tagebuch enthält, was du getan hast und warum. Lies beide nebeneinander, um Ursache und Wirkung rund um ein Datum zu sehen.
:::

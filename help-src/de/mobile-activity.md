---
title: Aktivität und Zeitleiste
description: Alles, was mit deiner Ausrüstung passiert ist, und was es verursacht hat.
section: Cora Mobile
reviewed: 2026-09-09
order: 22
group: Records
---

Aktivität erfasst jede **Aktuierungsanfrage** (jeden Versuch, etwas zu ändern) zusammen mit dem, was danach gefragt hat, und dem, was daraus wurde.

Eine Anfrage ist nicht dasselbe wie eine Änderung. Abgelehnte Anfragen wurden nicht ausgeführt, mit einer Ausnahme: Ein Eintrag, der sagt *Kein Gerät hat rechtzeitig geantwortet*, könnte trotzdem gelaufen sein, daher prüfe die Ausrüstung, bevor du es wiederholst. Anfragen ohne Änderung fanden die Ausrüstung schon wie gewünscht vor, und eine unbestätigte hat das Gerät möglicherweise gar nicht erreicht. Alle davon werden erfasst.

**Einstellungen → Aktivität.**

![Das Aktivitätsprotokoll](img/mobile-activity.webp "Jede Aktion, mit der Oberfläche, die sie angefordert hat.")

## Was erfasst wird

Jede **Anfrage**, nicht nur die, die funktioniert haben: Steckdosenschaltungen, Fütterungszyklen, Dosierungen, Steckdosenänderungen, und alles, was eine Szene oder Automation getan hat.

Eine Anfrage, die **abgelehnt** wurde, die **keine Änderung** bewirkt hat, oder die hinausging und **unbestätigt** zurückkam, wird genauso erfasst wie eine ausgeführte. Das ist der Sinn: Ein Befehl, der still nichts bewirkt hat, ist genau das, was du hier finden möchtest.

## Was es verursacht hat

Jeder Eintrag benennt seine Ursache:

| Ursache | Bedeutet |
|---|---|
| **Diese App** | Du hast hier getippt |
| **Sprache in dieser App** | Du hast gefragt, auf diesem Handy |
| **Auf einem Cora getippt** | Jemand hat einen Cora-Bildschirm benutzt; die Zeile sagt, welchen |
| **Sprache an einem Cora Max** | Jemand hat mit einem Bildschirm gesprochen |
| **Cora Assistant** | Du hast Cora gebeten, es zu tun |
| **Automationsregel** | Eine Regel hat ausgelöst |
| **Smart-Taste** | Eine physische Taste wurde gedrückt |
| **Von Cora Cloud gesendet** | Von deinem Konto ausgegeben, statt von einem Gerät vor dir |
| **Unbekannte Quelle** | Erfasst, bevor die Quelle identifiziert werden konnte |

## Wie es gereist ist

Jede Zeile trägt auch einen Weg-Chip, weil *wie* eine Anfrage deine Ausrüstung erreicht hat viel darüber erklärt, was schiefging, wenn etwas schiefging:

| Chip | Bedeutet |
|---|---|
| **LAN** | Über dein eigenes Netzwerk gesendet, direkt an die Ausrüstung |
| **ÜBER CLOUD** | Über dein Konto gesendet, für Ausrüstung, die nicht direkt erreichbar ist |
| **WEG ?** | Erfasst, bevor Wege verfolgt wurden: wirklich unbekannt, nicht angenommen |

Auf einem System mit mehr als einem Cora benennt die Zeile außerdem, welches die Anfrage hinausgetragen hat.

## Die Becken-Zeitleiste

Getrennt von Ausrüstungsaktionen hat jedes Becken eine **Zeitleiste**: Messwerte, Warnungen, Tagebucheinträge, ICP-Ergebnisse und Besatzänderungen der Reihe nach angeordnet.

Nutze Aktivität, wenn du fragst *"was hat etwas getan?"*, und die Zeitleiste, wenn du fragst *"was ist rund um dieses Datum passiert?"*

:::note Die Zeitleiste und das Tagebuch ergänzen sich
Die Zeitleiste enthält, was Cora erfasst hat; das [Tagebuch](/help/mobile-journal) enthält, was du getan hast. Gemeinsam gelesen stellen sie Ursache und Wirkung rund um ein bestimmtes Datum her.
:::

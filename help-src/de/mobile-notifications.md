---
title: Benachrichtigungen
description: Wähle, was dein Handy erreicht, wann es ankommen darf, und wo du nachliest, was du verpasst hast.
section: Cora Mobile
reviewed: 2026-09-27
order: 16
group: Alerts and automation
---

**Einstellungen → Benachrichtigungen** steuert alles, was Cora dir senden darf.

![Benachrichtigungseinstellungen](img/mobile-notifications.webp "Jede Kategorie kann unabhängig senden.")

## Was senden darf

Jede Kategorie wird unabhängig geschaltet:

| Kategorie | Umfasst |
|---|---|
| **Wasserwert-Warnungen** | Wasserchemie außerhalb eines von dir festgelegten Bereichs |
| **Wartungserinnerungen** | Von dir geplante Aufgaben, wie Wasserwechsel |
| **Gerätefehler** | Ein Gerät meldet ein Problem: ein Trident, der aufgehört hat zu testen, zum Beispiel |
| **Vorräte werden knapp** | Reagenz, Nachfüllwasser, Dosierbehälter, und eine volle Abfallflasche |
| **ICP-Bericht bereit** | Deine ICP-Ergebnisse sind analysiert und bereit zum Lesen |

Eine Kategorie auszuschalten stoppt den Push. Das Ereignis wird trotzdem erfasst und erscheint weiterhin in der Glocke.

:::warning "Wasserwert-Warnungen" bedeutet Chemie, und nur Chemie
Es ist naheliegend, diesen Schalter so zu lesen, als würde er alles abdecken, was das Becken dir mitteilen könnte. Das tut er nicht. Ein Trident, der aufgehört hat zu testen, ist ein **Gerätefehler**, und ausgehendes Reagenz ist **Vorräte werden knapp**; jedes hat seinen eigenen Schalter. Wenn Wasserwert-Warnungen bei dir schon lange eingeschaltet ist und du angenommen hast, dass das den Rest abdeckt, prüf die anderen beiden.
:::

**Vorräte werden knapp umfasst auch die Abfallflasche**, die sich füllt statt leerläuft. Sie ist in dieser Kategorie, weil die nötige Handlung dieselbe ist: etwas leeren oder ersetzen, bevor es die Tests stoppt.

## Die Glocke

Oben rechts auf jedem Bildschirm. Sie enthält alles, was Cora ausgelöst hat, neueste zuerst, ob es gesendet wurde oder nicht. Die Zahl zeigt, was du noch nicht gelesen hast.

Das ist der richtige Ort, um nach einem Tag ohne Handy nachzusehen, oder nachdem eine ausgeschaltete Kategorie etwas ausgelöst hat.

## Wenn nichts ankommt

Geh diese Liste durch:

1. **Einstellungen → Benachrichtigungen**: Darf diese Kategorie senden?
2. Die eigenen Einstellungen deines Handys: Darf Cora überhaupt benachrichtigen? Eine bei der Installation verweigerte Berechtigung übersteuert alles hier.
3. Gibt es überhaupt etwas zu senden? Reef Buddy bleibt an Tagen still, an denen sich nichts geändert hat.

## Wenn zu viel ankommt

Überprüfe deine Schwellenwerte, bevor du Benachrichtigungen deaktivierst. Übermäßige Warnungen deuten meist auf einen Bereich hin, der enger eingestellt ist, als das Becken tatsächlich läuft, oder auf eine Quelle, die kalibriert werden muss. Siehe [Warnungen und Schwellenwerte](/help/mobile-alerts).

Eine Kategorie auszuschalten ist für diese Kategorie alles oder nichts. Wenn statt dessen eine bestimmte Warnung zu oft sendet, ändere ihre **Abklingzeit zwischen Warnungen** an der Regel selbst, von 15 Minuten bis zu 1 Woche, statt die ganze Kategorie auszuschalten. Siehe [Warnungen und Schwellenwerte](/help/mobile-alerts) für die Abklingzeit-Optionen und was "Schlummern" auf Cora Max bedeutet.

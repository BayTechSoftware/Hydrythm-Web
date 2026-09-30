---
title: Sonden
description: Sieh, welche Sonde jeden Messwert liefert, egal bei welchem Controller, und halte Kalibrierung und Reinigung fest.
section: Cora Mobile
reviewed: 2026-09-30
order: 13
group: Equipment
---

Hast du mehr als einen Controller, oder zwei Sonden, die dasselbe messen, muss Cora wissen, welchem Messwert es vertrauen soll. Genau dafür ist die Sondenzuordnung da, und dort legst du auch fest, wofür jede Sonde überhaupt steht.

Öffne dein **Beckenprofil** (der Stift oben auf dem Dashboard) und wähl **Sondenzuordnung**.

## Woher jeder Messwert kommt

![Woher jeder Messwert kommt](img/mobile-probes.webp "Jeder Wasserwert, welche Sonde ihn gerade liefert, und eine Schaltfläche zum Ändern.")

In diesem Abschnitt stehen alle Wasserwerte, die Cora für dieses Becken verfolgt, etwa pH oder Temperatur, und dazu, welche Sonde sie gerade liefert.

Tippe auf einen Wasserwert, um jede Sonde zu sehen, die ihn meldet, über alle verbundenen Controller hinweg. Zu jeder stehen ihre Marke, ihr eigener Name für die Sonde und ihr Live-Messwert. Wähl eine aus, um sie festzulegen, oder wähl **Automatisch**, damit Cora selbst entscheidet, welche Sonde gilt.

Ein Zusatz neben jedem Wasserwert zeigt, was gerade gilt: **Automatisch**, oder **Von dir gewählt**, sobald du eine Sonde festgelegt hast.

Meldet sich eine festgelegte Sonde nicht mehr, zeigt Cora, wann sie zuletzt gemeldet hat, und bietet **Zurück zu Automatisch** an. So kann eine tote Sonde einen Wasserwert nicht dauerhaft blockieren.

Tippe auf **Umbenennen**, um einem Wasserwert einen eigenen Anzeigenamen zu geben. Das ist unabhängig vom Namen, den du der Sonde selbst gibst. Dieser Name erscheint auf deinem Dashboard, in Warnungen und in Reef Buddy.

:::note Ein Lecksensor lässt sich hier nicht neu zuordnen
Der Alarm eines Lecksensors hängt an seinem eigenen Namen, deshalb taucht er in dieser Auswahl nicht auf. Er funktioniert weiterhin wie gewohnt.
:::

## Sonden: Cora sagen, was jede ist

Weiter unten stehen alle Sonden, die Cora kennt, gruppiert nach dem Gerät, das sie meldet, mit ihrem aktuellen Messwert. Die Standardnamen erkennt Cora selbst, und in der Zeile siehst du, welchem Wasserwert es die Sonde zugeordnet hat. Meist musst du also nur die Sonden korrigieren, die Cora nicht einordnen konnte, und nicht alle von Hand zuordnen.

In jeder Zeile hast du drei Möglichkeiten:

- **Einen Cora-Wasserwert**, also den Wert, den diese Sonde misst.
- **Eigen** für eine Sonde, für die Cora keinen Standard-Wasserwert kennt. Du gibst ihr ein kurzes Kürzel in Großbuchstaben, und Cora zeichnet sie unter diesem Namen auf.
- **Ignorieren** für Sonden, die Cora gar nicht aufzeichnen soll.

Eine ignorierte oder nicht zugeordnete Sonde erscheint auf keinem Dashboard und löst keine Warnungen aus.

Eine Zuordnung gilt ab dem nächsten Messwert. Korrigierst du hier etwas, bleibt die Historie also, wie sie ist. Nur was ab jetzt gespeichert wird, ändert sich. Tippe auf **Speichern**, um die Zuordnungen zu übernehmen.

:::warning Eine nicht zugeordnete Sonde sieht Cora nicht
Zeigt ein Wasserwert keine Messwerte, obwohl die Sonde funktioniert, prüf als Erstes ihre Zuordnung.
:::

## Mehrere Sonden für einen Wasserwert

Hast du zwei Temperatursonden, egal ob am selben Controller oder an zweien, ordne beide zu. Cora führt sie als getrennte Quellen, und oben unter **Woher jeder Messwert kommt** legst du fest, welche davon den Wasserwert liefert, oder lässt es auf Automatisch. In der [Wasserwert-Ansicht](/help/mobile-metric-detail) kannst du sie vergleichen.

## Sondenpflege festhalten

Sonden driften mit der Zeit. Cora kann festhalten, wann du jede zuletzt kalibriert oder gereinigt hast. So erkennst du, ob sich wirklich etwas im Becken ändert oder ob eine Sonde Pflege braucht.

Kalibrierung oder Reinigung trägst du beim Eintrag der Sonde ein. Das passt auch gut als wiederkehrende [Wartungsaufgabe](/help/mobile-maintenance).

:::note Die Kalibrierhistorie erklärt Abweichungen
Zeigen Sonde und Testkit unterschiedliche Werte, schau zuerst nach, wann du die Sonde zuletzt kalibriert hast.
:::

---
title: Wartung
description: Wiederkehrende Aufgaben wie Abschäumer reinigen oder Filtersocken wechseln hinzufügen, erinnert werden, wenn sie fällig sind, und sie als erledigt markieren oder verschieben.
section: Cora Mobile
reviewed: 2026-10-13
order: 28
group: Records
twin: max-records
---

Die Wartung hält die Aufgaben fest, die dein Becken regelmäßig braucht, mit einer Erinnerung für jede.

Tippe in der Reihe von Tasten unter dem Dashboard auf **Wartung**. Du findest sie auch unter Einstellungen → dein Becken → **Wartung**.

![Die Wartungsliste](img/mobile-maintenance.webp "Erfüllung, Zahl der überfälligen Aufgaben und jede Aufgabe mit ihrer letzten Erledigung und ihrem nächsten Fälligkeitsdatum.")

## Die Übersicht {#summary}

Oben siehst du **Wartungserfüllung**, den Anteil der Aufgaben, die gerade im Zeitplan sind, und wie viele Aufgaben überfällig sind.

Jede Aufgabe in der Liste ist farblich markiert: überfällig, bald fällig oder geplant. Sie zeigt auch, wann du sie zuletzt erledigt hast und wann sie wieder fällig ist.

## Eine Aufgabe hinzufügen {#adding-a-task}

Tippe auf **Aufgabe hinzufügen** und wähl dann:

- **Aus Vorlage** für eine gängige Aufgabe mit schon eingetragenem Intervall. Wähl sie, leg fest, wann sie das nächste Mal fällig ist und zu welcher Uhrzeit du erinnert werden willst, und tippe auf **Bestätigen**.
- **Eigene Aufgabe** für deine eigene. Gib ihr einen **Aufgabenname**, ein **Intervall (Tage)**, eine **Kategorie** und ein **Nächstes Fälligkeitsdatum**. Schalte **Erinnerung** ein und wähl **Erinnere mich um**, wenn du eine Benachrichtigung willst.

Einige der Vorlagen, mit dem Intervall, mit dem sie beginnen:

| Aufgabe | Intervall |
|---|---|
| Filtersocken wechseln | 3 Tage |
| Abschäumerbecher reinigen | 7 Tage |
| Wasserwechsel | 7 Tage |
| Wasserwerte testen | 7 Tage |
| Kohle wechseln | 30 Tage |
| pH-Sonde kalibrieren | 30 Tage |
| Strömungspumpen reinigen | 90 Tage |
| ICP-Ergebnisse hochladen | 90 Tage |

Das Intervall jeder Aufgabe kannst du später ändern.

### Aufgaben, die Cora für Red Sea-Ausrüstung hinzufügt {#red-sea-tasks}

Verbindest du ein Red Sea ReefDose, ReefATO+, ReefMat oder ReefRun, fügt Cora die Wartung hinzu, die dieses Gerät braucht, schon mit dem richtigen Intervall:

| Gerät | Aufgabe | Intervall |
|---|---|---|
| ReefATO+ | ReefATO+-EC-Sensor ersetzen | 42 Tage |
| ReefATO+ | ReefATO+-Rücklaufpumpe ersetzen | 135 Tage |
| ReefMat | ReefMat-Kohle ersetzen | 25 Tage |
| ReefRun | ReefRun-Abschäumer-Venturi prüfen | 35 Tage |
| ReefRun | ReefRun-Abschäumer-Rotor ersetzen | 135 Tage |
| ReefRun | ReefRun-Vollbecher-Sensor kalibrieren | 28 Tage |
| ReefRun | ReefRun-Überabschäum-Sensor kalibrieren | 28 Tage |
| ReefRun, pro Pumpe | Motor von ReefRun-Pumpe warten | 135 Tage |
| ReefRun, pro Pumpe | Sieb von ReefRun-Pumpe reinigen | 42 Tage |
| ReefDose, pro Kopf | ReefDose-Kopf kalibrieren | 90 Tage |
| ReefDose, pro Kopf | Schlauch von ReefDose-Kopf ersetzen | 450 Tage |

Sie funktionieren wie jede Aufgabe, die du selbst hinzufügst. Du kannst sie umbenennen, das Intervall ändern, sie verschieben oder löschen. Löschst du eine, fügt Cora sie für dieses Gerät nicht wieder hinzu.

### Wasser testen {#test-water}

Tippst du auf der Karte für den ersten Test auf **Erinnere mich jede Woche ans Testen**, fügt Cora eine wöchentliche Aufgabe namens **Wasser testen** hinzu, fällig an dem **Testtag**, den du wählst. Sie funktioniert wie jede andere Aufgabe. Siehe [Cora Mobile einrichten](/help/mobile-setup). Du kannst auch jederzeit eine Test-Erinnerung mit der Vorlage **Wasserwerte testen** hinzufügen.

### Aus einer Automation {#from-an-automation}

Eine [Automation](/help/mobile-automation) mit der Aktion **Wartungsaufgabe erstellen** kann eine Aufgabe auf diese Liste setzen, wenn ihre Regel auslöst, oder eine bestehende Aufgabe sofort fällig machen. Eine neue ist eine **Einmalige Aufgabe**, sofort fällig, und sie zeigt *Von einer Automation erstellt* mit dem Grund. Sie verschwindet aus der Liste, wenn du sie erledigst. Solange sie noch offen ist, fügt dieselbe Automation keine weitere hinzu. Du bekommst eine Benachrichtigung.

## Erinnerungen {#reminders}

Öffne eine Aufgabe, schalte **Erinnerung** ein und wähl dann **Erinnere mich um**. Du bekommst eine Benachrichtigung am Tag vor der Fälligkeit und eine am Tag selbst. Solange sie überfällig ist, bekommst du alle paar Tage eine Erinnerung. Werden mehrere Aufgaben eines Beckens gleichzeitig fällig, kommen sie als eine Benachrichtigung.

Erinnerungen fallen unter **Wartungserinnerungen** in [Einstellungen → Benachrichtigungen](/help/mobile-notifications). Willst du eine Aufgabe nur in der Liste sehen, schalte ihre **Erinnerung** aus.

## Eine Aufgabe als erledigt markieren {#marking-done}

Wisch die Aufgabe nach rechts oder öffne sie und tippe auf **Erledigt**. Hast du aus Versehen gewischt, tippe in der Meldung, die erscheint, auf **Rückgängig**.

Cora speichert die Zeit, zu der du fertig warst, und zählt die nächste Fälligkeit ab dann. Erledigst du eine Aufgabe drei Tage zu spät, rückt die nächste also auch um drei Tage nach hinten.

Das Fenster der Aufgabe zeigt ihren **Erledigungsverlauf**, auch wie spät jede war.

:::note Eine Aufgabe zu erledigen schreibt auch einen Tagebucheintrag
Cora fügt für dich einen kurzen Eintrag in dein [Tagebuch](/help/mobile-journal) ein und vermerkt, wenn sie zu spät war. Füg einen eigenen Eintrag hinzu, wenn es mehr zu sagen gibt, etwa wenn die Pumpe voller Sand war oder die Socken nach einem Tag schwarz waren.
:::

## Eine Aufgabe bearbeiten {#editing}

Tippe auf eine Aufgabe, um sie zu öffnen. Du kannst **Aufgabenname**, **Intervall (Tage)**, **Notizen (optional)**, **Nächstes Fälligkeitsdatum** und die Erinnerung ändern und dann auf **Speichern** tippen. **Löschen** entfernt sie.

## Verschieben {#snoozing}

Kommst du gerade nicht zu einer Aufgabe? Öffne sie, tippe auf **Verschieben** und wähl **1 Tag**, **3 Tage**, **1 Woche**, **2 Wochen** oder **1 Monat**. Sie bleibt als **Verschoben** mit ihrem neuen Datum in der Liste, und du wirst bis dahin nicht erinnert.

:::warning Markier eine Aufgabe nur als erledigt, wenn du sie erledigt hast
Die nächste Fälligkeit wird ab dem Tag gezählt, an dem du sie als erledigt markierst. Markierst du eine offene Aufgabe als erledigt, verschiebt sich jede spätere Fälligkeit. Verschieb sie stattdessen.
:::

Eine Aufgabe zu pausieren geht nicht. Für eine Aufgabe, die in dieser Saison nicht anfällt, verschieb sie um **1 Monat** oder lösche sie und füg sie später wieder hinzu.

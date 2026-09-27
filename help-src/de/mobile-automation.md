---
title: Automationen und Szenen
description: Erstelle Regeln, die von selbst laufen (Trigger, Bedingungen, Aktionen), und gruppiere sie zu Szenen.
section: Cora Mobile
reviewed: 2026-09-27
order: 17
group: Alerts and automation
---

Eine Automation ist eine Regel, die Cora für dich ausführt: *wenn das passiert, prüfe das, und tu dann dies.* Szenen gruppieren mehrere Aktionen zu einer Sache, die du ausführen oder planen kannst.

**Einstellungen → Automation.**

![Die Automations-Liste](img/mobile-automation.webp "Automationen und Szenen sind getrennte Tabs. Jede Regel hat einen Aktivierungsschalter.")

Der Bildschirm hat zwei Tabs (**Automationen** und **Szenen**) und eine Schaltfläche **Neue Automation**. Jede Regel zeigt eine einzeilige Zusammenfassung dessen, was sie tut, einen Aktivierungsschalter, und ein Menü zum Bearbeiten oder Löschen. Eine Regel, die noch nicht gelaufen ist, wird als solche gekennzeichnet.

:::warning Diese wirken auf echte Ausrüstung
Eine Regel, die eine Pumpe schaltet, schaltet sie, ob du zuschaust oder nicht. Erstelle eine nach der anderen, und prüfe bei jeder, dass sie das tut, was du erwartest, bevor du die nächste hinzufügst.
:::

## Der Aufbau einer Regel

Jede Regel besteht aus denselben drei Teilen:

**Auslöser**: was sie aufweckt
**Bedingungen**: was außerdem zutreffen muss
**Aktionen**: was sie dann tut, in der Reihenfolge

## Was eine Regel aufwecken kann

Vier Dinge:

| Trigger | Löst aus, wenn |
|---|---|
| **Wasserwert** | Ein Wasserwert einen von dir festgelegten Wert überschreitet, in einer von dir gewählten Richtung |
| **Warnung** | Eine Warnung ausgelöst, gelöscht, oder beides wird |
| **Zeitplan** | Eine Tageszeit, in deiner eigenen Zeitzone |
| **Gerätestatus** | Ein Gerät offline geht oder zurückkommt |

## Bedingungen

Bedingungen entscheiden, ob die Aktionen tatsächlich ausgeführt werden. Du hast die üblichen Vergleiche (gleich, ungleich, größer als, kleiner als, und so weiter) und kannst sie mit **und**, **oder** und **nicht** kombinieren.

Es gibt außerdem eine **Schritt**-Bedingung, die prüft, wie der *vorherige* Schritt ausgegangen ist. Das ist es, was dir erlaubt zu schreiben: "versuche das; wenn es nicht funktioniert hat, tu statt dessen jenes."

## Was eine Regel tun kann

Eine Aktion, die Ausrüstung braucht, wird nur auf einem Becken angeboten, das diese Ausrüstung hat:

| Aktion | Was sie tut |
|---|---|
| **Apex-Gerät steuern** | Eine Steckdose schalten |
| **Ein Red-Sea-Gerät steuern** | Ein ReefBeat-Gerät ansteuern |
| **Eine Strömungspumpe steuern** | Strömung, Wellenmodus oder Leistung einer Jecod-Pumpe festlegen, oder **Für Fütterung pausieren**: Das Cora Max am Becken stellt die Pumpe zurück, wenn die Fütterung endet |
| **Ein Cora-Gerät steuern** | Eine Smart-Steckdose schalten |
| **IR-Gerät steuern** | Einen Infrarot-Befehl senden |
| **Apex Fütterungszyklus starten** | Eine Fütterung starten |
| **Einen Trident Test durchführen** | Einen Test auslösen |
| **Mich benachrichtigen** | Dir selbst einen Push senden |
| **Vor dem nächsten Schritt warten** | Vor dem Fortfahren pausieren |
| **Eine Szene ausführen** | Eine andere Szene innerhalb dieser Regel ausführen |
| **Eine Automation verwalten** | Eine andere Regel ein- oder ausschalten |
| **Einen DŌS Kopf dosieren** | Eine bemessene Dosierung an einem DŌS-Kopf ausführen |

:::warning Dosieren aus einer Regel ist unumkehrbar und begrenzt
Eine Dosierung kann nicht aus dem Becken zurückgeholt werden. Der Kopf muss **kalibriert** sein, bevor eine Regel aus ihm dosieren darf, und unbeaufsichtigtes Dosieren ist auf **10 mL pro Kopf pro Tag** begrenzt; eine Regel kann das nicht überschreiten, egal wie sie geschrieben ist. Dosier-Aktionen erscheinen erst, sobald deine Köpfe als Dosierköpfe erkannt sind.
:::

:::note Nutze Warten, um Schritte innerhalb einer Regel zu ordnen
Eine Pause erlaubt einer einzelnen Regel, einen geordneten Ablauf durchzuführen (zum Beispiel eine Steckdose ausschalten, warten, und sie dann wieder einschalten), ohne eine zweite Regel und einen Zeitplan.
:::

## Szenen

Eine Szene ist eine benannte Gruppe von Aktionen, die du auf Verlangen, nach einem Zeitplan, oder innerhalb einer anderen Regel ausführen kannst: "Wasserwechsel", "Fotomodus", "Nacht".

Eine Szene kann eine andere Szene aufrufen. Cora verweigert die Ausführung einer Szene, die tiefer verschachtelt ist als das Tiefenlimit, und verweigert eine Szene, die sich selbst aufrufen würde, um eine Schleife zu verhindern, die unbegrenzt auf das Becken wirken würde.

Nachdem eine Szene gelaufen ist, wird dir Schritt für Schritt gesagt, was passiert ist, einschließlich allem, was fehlgeschlagen ist.

Eine Szene von Hand auszuführen fragt zuerst nach Bestätigung, da eine Szene mehrere Geräte auf einmal schalten kann.

## Auf Cora Max erstellte Szenen

Szenen können auch direkt auf einem Cora Max-Tablet erstellt und bearbeitet werden, nicht nur auf dem Handy: Es ist in beiden Fällen dieselbe Menge an Szenen, kontoübergreifend geteilt. Wenn ein Haushalt ein älteres Cora Max hat, kann es trotzdem eine auf dem Handy erstellte Szene ausführen; nur das Bearbeiten direkt auf dem Gerät ist eine neuere Funktion, daher zeigt ein älteres Tablet vielleicht eine Szene, ohne dir dort eine Änderung zu erlauben. Bearbeite sie statt dessen vom Handy aus.

## Eine Regel ausschalten

Jede Regel hat einen Aktivierungsschalter. Eine auszuschalten behält ihre Definition, nützlich, wenn du eine Regel zur nächsten Saison zurückwillst, statt sie neu aufzubauen.

## Sehen, was eine Regel getan hat

Jede Aktion, die eine Regel ausführt, wird mit der Regel als ihrer Ursache erfasst. Siehe **[Aktivität](/help/mobile-activity)**.

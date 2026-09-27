---
title: Automationen und Szenen
description: Leg Regeln an, die von selbst laufen (Auslöser, Bedingungen, Aktionen), und fasse Aktionen zu Szenen zusammen.
section: Cora Mobile
reviewed: 2026-09-27
order: 17
group: Alerts and automation
---

Eine Automation ist eine Regel, die Cora für dich ausführt: *Wenn das passiert, prüf jenes und tu dann dies.* In einer Szene fasst du mehrere Aktionen zusammen, die du dann auf einmal startest oder nach Zeitplan laufen lässt.

**Einstellungen → Automation.**

![Die Automations-Liste](img/mobile-automation.webp "Automationen und Szenen sind getrennte Tabs. Jede Regel hat einen Aktivierungsschalter.")

Der Bildschirm hat zwei Tabs, **Automationen** und **Szenen**, und die Schaltfläche **Neue Automation**. Zu jeder Regel siehst du in einer Zeile, was sie tut, dazu einen Aktivierungsschalter und ein Menü zum Bearbeiten oder Löschen. Ist eine Regel noch nie gelaufen, steht das dabei.

:::warning Regeln schalten echte Geräte
Eine Regel, die eine Pumpe schaltet, schaltet sie auch dann, wenn du nicht hinschaust. Leg eine Regel nach der anderen an. Prüf bei jeder, ob sie tut, was du erwartest, bevor du die nächste hinzufügst.
:::

## Wie eine Regel aufgebaut ist

Jede Regel hat dieselben drei Teile:

**Auslöser**: was sie startet
**Bedingungen**: was zusätzlich zutreffen muss
**Aktionen**: was sie dann der Reihe nach tut

## Was eine Regel startet

Es gibt vier Auslöser:

| Auslöser | Startet, wenn |
|---|---|
| **Wasserwert** | ein Wasserwert einen von dir gewählten Wert in der gewählten Richtung überschreitet |
| **Warnung** | eine Warnung kommt, verschwindet oder beides |
| **Zeitplan** | eine bestimmte Uhrzeit erreicht ist, in deiner eigenen Zeitzone |
| **Gerätestatus** | ein Gerät offline geht oder wieder erreichbar ist |

## Bedingungen

Mit Bedingungen entscheidest du, ob die Aktionen wirklich laufen. Du hast die üblichen Vergleiche (gleich, ungleich, größer als, kleiner als und so weiter) und kannst sie mit **und**, **oder** und **nicht** verknüpfen.

Dazu kommt eine **Schritt**-Bedingung. Sie prüft, wie der *vorige* Schritt ausgegangen ist. Damit kannst du Regeln schreiben wie: "Versuch das. Hat es nicht geklappt, mach stattdessen jenes."

## Was eine Regel tun kann

Aktionen für bestimmte Geräte bekommst du nur bei einem Becken angeboten, zu dem diese Geräte gehören:

| Aktion | Was sie tut |
|---|---|
| **Apex-Gerät steuern** | schaltet eine Steckdose |
| **Ein Red-Sea-Gerät steuern** | steuert ein ReefBeat-Gerät |
| **Eine Strömungspumpe steuern** | stellt bei einer Jecod-Pumpe Strömung, Wellenmodus oder Leistung ein. Oder du wählst **Für Fütterung pausieren**. Dann stellt das Cora Max am Becken die Pumpe nach der Fütterung zurück |
| **Ein Cora-Gerät steuern** | schaltet eine Smart-Steckdose |
| **IR-Gerät steuern** | sendet einen Infrarot-Befehl |
| **Apex Fütterungszyklus starten** | startet eine Fütterung |
| **Einen Trident Test durchführen** | startet einen Test |
| **Mich benachrichtigen** | schickt dir eine Push-Nachricht |
| **Vor dem nächsten Schritt warten** | legt eine Pause ein, bevor es weitergeht |
| **Eine Szene ausführen** | startet eine andere Szene aus dieser Regel heraus |
| **Eine Automation verwalten** | schaltet eine andere Regel ein oder aus |
| **Einen DŌS Kopf dosieren** | gibt an einem DŌS-Kopf eine abgemessene Dosis ab |

:::warning Dosieren per Regel lässt sich nicht rückgängig machen und ist begrenzt
Was einmal dosiert ist, bekommst du nicht mehr aus dem Becken. Ein Kopf muss **kalibriert** sein, bevor eine Regel damit dosieren darf. Unbeaufsichtigtes Dosieren ist auf **10 mL pro Kopf und Tag** begrenzt. Keine Regel kann das überschreiten, egal wie sie geschrieben ist. Dosier-Aktionen tauchen erst auf, wenn Cora deine Köpfe als Dosierköpfe erkannt hat.
:::

:::note Mit Warten Schritte in einer Regel ordnen
Mit einer Pause kann eine einzige Regel einen festen Ablauf abarbeiten. Sie schaltet zum Beispiel eine Steckdose aus, wartet und schaltet sie dann wieder ein. Eine zweite Regel mit Zeitplan brauchst du dafür nicht.
:::

## Szenen

Eine Szene ist eine Gruppe von Aktionen mit einem Namen, etwa "Wasserwechsel", "Fotomodus" oder "Nacht". Du startest sie von Hand, per Zeitplan oder aus einer anderen Regel heraus.

Eine Szene darf eine andere Szene aufrufen. Ist eine Szene tiefer verschachtelt als erlaubt, führt Cora sie nicht aus. Das gilt auch für eine Szene, die sich selbst aufrufen würde. So kann keine Endlosschleife entstehen, die immer weiter auf das Becken einwirkt.

Nach jedem Lauf zeigt dir Cora Schritt für Schritt, was passiert ist, auch was nicht geklappt hat.

Startest du eine Szene von Hand, fragt Cora vorher nach. Eine Szene kann ja mehrere Geräte auf einmal schalten.

## Szenen vom Cora Max

Du kannst Szenen auch direkt auf einem Cora Max anlegen und bearbeiten. Es sind dieselben Szenen wie auf dem Handy, sie gelten für das ganze Konto. Ein älteres Cora Max im Haushalt kann eine auf dem Handy erstellte Szene trotzdem ausführen. Nur das Bearbeiten direkt am Gerät ist neuer. Ein älteres Cora Max zeigt dir die Szene also vielleicht an, lässt dich dort aber nichts ändern. Bearbeite sie dann am Handy.

## Eine Regel ausschalten

Jede Regel hat einen Aktivierungsschalter. Schaltest du eine Regel aus, bleibt sie gespeichert. Das ist praktisch, wenn du sie nächste Saison wieder brauchst und nicht neu bauen willst.

## Nachsehen, was eine Regel getan hat

Jede Aktion einer Regel wird protokolliert, mit der Regel als Auslöser. Du findest sie unter **[Aktivität](/help/mobile-activity)**.

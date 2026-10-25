---
title: Automationen und Szenen
description: Cora von selbst handeln lassen, wenn ein Messwert, eine Warnung, eine Uhrzeit oder ein Gerät offline geht, und Aktionen zu Ein-Tipp-Szenen bündeln.
section: Cora Mobile
reviewed: 2026-10-24
order: 25
group: Alerts and automation
twin: max-automation
---

Eine Automation ist eine Regel, die Cora für dich ausführt: *Wenn das passiert, prüf jenes und tu dann dies.* Eine Szene fasst mehrere Aktionen zu einer Sache zusammen, die du startest, wann du willst.

Geh zu **Einstellungen → Automationen**.

![Der Automationsbildschirm in Cora Mobile, mit den Tabs Automationen und Szenen](img/mobile-automation.webp "Automationen und Szenen sind getrennte Tabs. Jede Regel hat ihren eigenen Schalter.")

Der Bildschirm hat zwei Tabs, **Automationen** und **Szenen**, mit einer Taste **Neue Automation** oder **Neue Szene**. Jede Regel zeigt eine einzeilige Zusammenfassung, einen Schalter zum Aktivieren und ein Menü zum **Bearbeiten** oder **Löschen**. Bei einer Regel, die noch nicht gelaufen ist, steht das dabei.

:::warning Regeln wirken auf echte Ausrüstung
Schaltet eine Regel eine Pumpe, schaltet die Pumpe auch dann, wenn du nicht hinschaust. Bau eine Regel nach der anderen und prüf, ob sie tut, was du erwartest, bevor du die nächste hinzufügst.
:::

## Wie eine Regel aufgebaut ist {#shape}

Jede Automation hat drei Teile.

- Der Auslöser weckt sie.
- Die Bedingungen müssen außerdem zutreffen.
- Die Aktionen sind das, was sie dann der Reihe nach tut.

![Ein leeres Formular Neue Automation in Cora Mobile](img/mobile-rule-builder.webp "Eine neue Automation: Auslöser, Wenn-Bedingungen, Dann-Aktionen, Sonst-wenn und Sonst, dann die Abklingzeit und das Zeitfenster.")

## Was eine Regel wecken kann {#triggers}

Füg unter **Wenn: ein beliebiger Auslöser** einen oder mehrere Auslöser hinzu. Jeder davon startet die Regel.

| Auslöser | Löst aus, wenn |
|---|---|
| **Wenn sich ein Wasserwert ändert** | Ein Wasserwert einen Wert überschreitet, den du festlegst. Wähl die **Richtung**: **Steigend**, **Fallend** oder **Jede Änderung** |
| **Wenn eine Warnung ausgelöst wird** | Eine Warnung **Ausgelöst** oder **Behoben** wird, oder beides. Du kannst es auf Warnungen vom Typ **Schwellenwert** oder **Änderungsrate** beschränken. |
| **Zu einer Tageszeit** | Eine Uhrzeit, in deiner eigenen Zeitzone |
| **Wenn ein Gerät offline geht** | Dein Cora Max **Offline** geht, wieder **Online** kommt, oder in beiden Fällen |

:::tip Erfahre es, wenn dein Cora Max wegfällt
Eine Regel mit **Wenn ein Gerät offline geht** und **Mich benachrichtigen** sagt dir, wenn das Cora Max, das deine Ausrüstung abfragt, Strom oder WLAN verliert.
:::

## Bedingungen {#conditions}

Bedingungen entscheiden, ob die Aktionen laufen. Tippe auf **Bedingung hinzufügen** und wähl:

- **Wasserwert vergleichen**, ein Messwert über, unter oder gleich einem Wert
- **Wasserwert innerhalb / außerhalb eines Bereichs**
- **Warnung aktiv**
- **Steckdose ist ein / aus**, für eine Apex-Steckdose
- **Tageszeit**, ein Zeitfenster wie 22:00 bis 06:00
- **Wie ein früherer Schritt verlaufen ist**, das prüft, ob ein früherer Schritt **OK** war oder **Übersprungen** wurde. Nutze es für "versuch das, und wenn es nicht geklappt hat, mach stattdessen jenes"

Bei mehreren Bedingungen stellst du **Übereinstimmung** auf **Alle (UND)** oder **Beliebig (ODER)**.

## Verzweigungen und Prüfungen pro Schritt {#branches}

Eine Automation kann in verschiedenen Fällen verschiedene Dinge tun. Ihr erster Block ist **Wenn**. Tippe auf **Sonst-wenn**, um einen weiteren Fall hinzuzufügen, oder füg einen Block **Sonst** für alles andere hinzu. Cora führt den ersten Block aus, dessen Bedingungen zutreffen.

Du kannst auch eine einzelne Aktion absichern. Tippe bei diesem Schritt auf **Nur wenn …** und gib ihm eine eigene Bedingung. Ohne Bedingung läuft der Schritt immer.

## Wann sie laufen darf {#when-it-may-run}

- **Abklingzeit zwischen Ausführungen** verhindert, dass eine Regel zu schnell wieder auslöst. Sie beginnt bei 10 Min.
- **Nur ausführen zwischen** beschränkt die Regel auf ein Zeitfenster, zum Beispiel nur tagsüber.
- **Mit aktuellen Werten testen** prüft die Regel gegen die aktuellen Messwerte deines Beckens, ohne etwas zu tun. Es sagt dir, was *laufen würde*, oder warum nichts laufen würde.

## Was eine Regel tun kann {#actions}

Eine Aktion, die Ausrüstung braucht, erscheint nur bei einem Becken, das diese Ausrüstung hat.

| Aktion | Was sie tut |
|---|---|
| **Apex-Gerät steuern** | Eine Steckdose schalten |
| **Apex Fütterungszyklus starten** | Eine Fütterung starten. Der Apex beendet sie mit seinem eigenen Timer |
| **Einen Trident Test durchführen** | Einen Test starten. Jeder Lauf verbraucht Reagenz |
| **Einen DŌS Kopf dosieren** | Eine abgemessene Dosis an einem DŌS-Kopf abgeben |
| **Ein Red-Sea-Gerät steuern** | Ein ReefBeat-Gerät steuern |
| **Eine Strömungspumpe steuern** | Strömung, Wellenmodus oder Leistung einer Jecod-Pumpe einstellen oder **Für Fütterung pausieren**. Das Cora Max am Becken stellt die Pumpe zurück, wenn die Fütterung endet |
| **Mich benachrichtigen** | Dir eine Push-Nachricht mit deinem eigenen **Titel** und deiner eigenen **Nachricht** schicken |
| **Vor dem nächsten Schritt warten** | Eine Pause einlegen, bevor es weitergeht |
| **Eine Szene ausführen** | Eine Szene aus dieser Regel heraus starten |
| **Eine Automation verwalten** | Eine andere Regel ein- oder ausschalten |
| **Wartungsaufgabe erstellen** | Eine Aufgabe auf die [Wartungsliste](/help/mobile-maintenance) des Beckens setzen, zum Beispiel das Material des CO2-Scrubbers wechseln, wenn der pH unter einen Wert fällt |


:::warning Eine Dosierung lässt sich nicht rückgängig machen, und sie ist begrenzt
Eine Dosierung bekommst du nicht mehr aus dem Becken heraus. Eine Regel kann nur aus einem Kopf dosieren, der auf einem Cora Max mit **Zum Dosieren messen** gemessen wurde. Die Dosierung läuft auf einem Cora Max am Becken. Dosieren per Regel ist auf **10 ml pro Kopf und Tag** begrenzt, egal wie die Regel geschrieben ist.
:::

:::note Was Wartungsaufgabe erstellen macht
Wähl das Becken, dann **Bestehende Aufgabe** (eine bestehende Aufgabe wird sofort fällig) oder **Neue Aufgabe** (gib ihr einen **Aufgabenname**). Eine neue Aufgabe ist einmalig und sofort fällig, und die Regel legt sie nicht noch einmal an, solange sie offen ist. Du bekommst eine Benachrichtigung, und die einmalige Aufgabe verschwindet aus der Liste, wenn du sie erledigst.
:::

:::note Warten ist kurz
**Vor dem nächsten Schritt warten** pausiert bis zu 60 Sekunden, und eine Verzweigung kann insgesamt 60 Sekunden warten. Nach der Pause sieht der nächste Schritt frische Messwerte. Für eine längere Pause, etwa eine Rückförderpumpe, die während eines Wasserwechsels 30 Minuten aus ist, nimm eine Szene mit **Ausführen für** (siehe unten).
:::

## Szenen {#scenes}

Eine Szene ist eine benannte Gruppe von Aktionen, etwa "Wasserwechsel", "Fotomodus" oder "Nacht". Tippe auf **Neue Automation** oder **Neue Szene** und wähl oben **Szene**. Eine Szene hat keinen Auslöser. Du startest sie mit **Jetzt ausführen** in der Liste, aus einer Regel heraus mit **Eine Szene ausführen** oder nach Zeitplan über eine Regel mit **Zu einer Tageszeit**.

**Ausführen für** legt fest, wie lange eine Szene dauert: eine Zahl von Minuten oder Stunden, oder **Bis ich es ändere**. Ist die Zeit um, schaltet Cora die Steckdosen der Szene zurück, wie sie waren. Andere Ausrüstung bleibt so, wie die Szene sie gelassen hat. Während eine zeitgesteuerte Szene läuft, zeigt die Liste einen Countdown und eine Taste **Stopp**, die sie vorzeitig beendet.

Schaltet eine Szene eine wichtige Steckdose, etwa einen Heizer, Kühler, eine Rückförderpumpe oder die Nachfüllanlage, fragt Cora vor dem Start nach und listet diese Schritte auf. Du kannst das mit **Vor der Ausführung fragen** an der Szene ausschalten.

Eine Szene kann eine andere Szene aufrufen, bis zu 3 Ebenen tief. Eine Szene, die sich selbst aufruft, führt Cora nicht aus, weil sie in einer Schleife immer weiter auf das Becken einwirken könnte.

Nachdem eine Szene gelaufen ist, siehst du Schritt für Schritt, was passiert ist, auch was fehlgeschlagen ist oder nicht gelaufen ist.

## Szenen, die auf Cora Max angelegt wurden {#scenes-on-cora-max}

Du kannst Szenen auch auf einem Cora Max anlegen und bearbeiten. Es sind dieselben Szenen, im ganzen Konto geteilt. Ein älteres Cora Max kann eine auf dem Handy angelegte Szene trotzdem starten. Das Bearbeiten am Gerät ist aber neuer, ein älteres Cora Max zeigt eine Szene also vielleicht, ohne dich etwas ändern zu lassen. Bearbeite sie dann auf dem Handy.

## Eine Regel ausschalten {#turning-a-rule-off}

Jede Regel hat einen Schalter zum Aktivieren. Schaltest du eine Regel aus, bleiben ihre Einstellungen erhalten. Das hilft, wenn du sie nächste Saison wieder willst.

## Sehen, was eine Regel getan hat {#seeing-what-a-rule-did}

Jede Aktion, die eine Regel ausführt, wird mit **Automationsregel** als Auslöser festgehalten. Du findest sie unter [Aktivität](/help/mobile-activity).

Ein Schritt, der fehlschlägt oder warten müsste, bleibt nicht offen. Er verfällt sofort, der Lauf wird als fehlgeschlagen festgehalten, und du bekommst eine Benachrichtigung, die die Automation, den Schritt und den Grund nennt. Ein Schritt scheitert zum Beispiel, wenn sein Gerät offline ist, kein Cora Max ihn ausführen kann, das Gerät ihn ablehnt oder nicht antwortet oder ein Heizer oder Kühler gerade erst geschaltet wurde. Für einen Schritt in einem entfernten Becken bekommst du keine Benachrichtigung.

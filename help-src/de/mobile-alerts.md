---
title: Warnungen und Schwellenwerte
description: Den gesunden Bereich für jeden Messwert festlegen, bestimmen, wie oft eine Warnung dich benachrichtigen darf, und herausfinden, warum ein Gerät "sich nicht mehr meldet".
section: Cora Mobile
reviewed: 2026-10-18
order: 22
group: Alerts and automation
twin: max-alerts
---

Du bekommst eine Warnung, wenn ein Messwert den Bereich verlässt, den du dafür festgelegt hast. Auf dieser Seite geht es darum, diese Bereiche festzulegen, was passiert, wenn eine Warnung ausgelöst wird, und wie lange Cora wartet, bevor es sagt, dass ein Gerät sich nicht mehr meldet.

Um die **Warnzentrale** zu öffnen, tippe in der Reihe von Tasten unter dem Dashboard auf **Warnungen**. Du findest sie auch unter Einstellungen → dein Becken → **Warnschwellen**.

![Der Tab Aktiv der Warnzentrale in Cora Mobile](img/mobile-alerts.webp "Aktive Warnungen, jede mit ihrem Schweregrad, was sie ausgelöst hat und wann, dazu Regel ansehen und Diese Warnung erklären.")

## Die Warnzentrale {#alert-center}

Sie hat zwei Tabs. **Aktiv** listet die Warnungen auf, die gerade bestehen, mit einer Zahl daneben. **Regeln** enthält die Regeln, die sie auslösen.

Jede aktive Warnung zeigt den Wasserwert und das Becken, den Messwert, der sie ausgelöst hat, eine kurze Erklärung, einen Chip für den Schweregrad, die Art der Regel, die ausgelöst hat (**Schwellenwert** oder **Änderungsrate**), und wann sie ausgelöst hat. Sie hat zwei Tasten:

- **Regel ansehen** öffnet die Regel dahinter, damit du den Bereich anpassen kannst. Bei einer Dosierpumpen-Warnung, etwa einem DŌS- oder ReefDose-Kopf, der zur Neige geht, oder einer verpassten Dosierung, heißt diese Taste stattdessen **Dosierpumpe öffnen**. Sie öffnet die Seite dieser Dosierpumpe mit ihren Warnungen.
- **Diese Warnung erklären** öffnet Cora Assistant mit einer fertigen Frage zur Warnung. Prüf sie, ändere sie, wenn du willst, und schick sie dann ab.

## Der Tab Regeln {#rules}

![Der Tab Regeln](img/mobile-alert-rules.webp "Regeln nach Wasserwert gruppiert, jede mit ihrem eigenen Schalter.")

Die Regeln sind nach Wasserwert gruppiert. Jede Regel hat in ihrer Zeile einen eigenen Schalter, du kannst sie also ausschalten, ohne sie zu öffnen. Eine Zeile zeigt außerdem **Löst gerade aus**, solange ihre Warnung besteht, oder wann sie zuletzt ausgelöst hat (oder **Nie ausgelöst**).

Die Regeln eines Dosierkopfs heißen nach dem Kopf und dem, was sie überwachen, zum Beispiel *Jod · Tage übrig* oder *Jod · verbleibend*. Eine verpasste Dosierung erscheint als *Jod · Dosierung verpasst*. Jeder DŌS und jeder ReefDose hat hier eine eigene Zeile, und die Warnungen seiner Köpfe werden nicht einzeln aufgelistet. Tippe auf die Zeile, um die Seite dieser Dosierpumpe zu öffnen. Siehe [Dosierpumpen-Warnungen](/help/mobile-device-control#doser-alerts).

Ganz unten:

- **Empfohlene Regeln hinzufügen** fügt die empfohlenen Regeln von Cora hinzu, die fehlen. Einen Wasserwert, der schon eine Regel hat, überspringt es. Bei einem Becken ganz ohne Regeln heißt diese Taste **Standardregeln hinzufügen**.
- **Eigene Regel hinzufügen** richtet eine eigene Regel ein. Wähl den Wasserwert und den **Regeltyp**, **Schwellenwert** oder **Änderungsrate**. Die Taste **Regel hinzufügen** unten rechts tut dasselbe.

### Eine Regel bearbeiten {#editing-a-rule}

Tippe auf die Zeile einer Regel, um sie zu öffnen. Du findest dort:

- **Warnuntergrenze** und **Warnobergrenze**, den Bereich selbst. Lass eins leer für eine Obergrenze oder eine Untergrenze.
- **Empfohlen**, das den von Cora vorgeschlagenen Bereich zurückholt.
- **Anzeigebereich (Cora-Anzeige)**, mit **Anzeige-Min.** und **Anzeige-Max.** Diese legen nur die Skala der Anzeige auf Cora Max fest. Sie lösen nie eine Warnung aus.
- **Abklingzeit zwischen Warnungen**, erklärt [weiter unten](#cooldowns).
- **Aktiviert** und eine Taste zum Löschen.

Eine Regel für einen Gerätefehler, etwa ein Trident ohne Reagenz, hat keinen Bereich. Du wählst nur ihre Abklingzeit.

## Einen Bereich festlegen {#setting-a-range}

Wasserwerte, die Cora bewerten kann, haben einen Zielbereich. Die Standardwerte kommen aus Beckentyp und Alter, die du beim Einrichten des Beckens angegeben hast, und sind ein sinnvoller Anfang. Hat ein Wasserwert keinen brauchbaren Bereich, bewertet Cora ihn nicht, und sein Widget bleibt neutral grau.

Am schnellsten änderst du einen Bereich, indem du auf dem Dashboard lange auf das Widget des Wasserwerts drückst. Das öffnet seine Schwellenwerte. Ein normales Tippen öffnet stattdessen die Ansicht des Wasserwerts.

![Das Fenster Schwellenwert bearbeiten für pH in Cora Mobile](img/mobile-threshold-sheet.webp "Warnuntergrenze und -obergrenze, der Anzeigebereich für Cora Max und die Abklingzeit zwischen Warnungen.")

Hat der Wasserwert noch keine Regel, starten die Felder mit dem Standard von Cora, und ein Hinweis darunter sagt das. Ändere einen beliebigen Wert, um deinen eigenen festzulegen.

Du kannst festlegen:

- einen Bereich, mit Unter- und Obergrenze, für Dinge wie Alkalinität oder Temperatur
- eine Obergrenze, nur mit einem Höchstwert, für Dinge, bei denen niedrig in Ordnung ist, wie Nitrat oder Phosphat
- eine Untergrenze, nur mit einem Mindestwert

:::tip Stell den Bereich ein, in dem dein Becken wirklich läuft
Die Standardwerte sind nur ein Ausgangspunkt. Ein nährstoffarmes Becken mit 6 dKH ist nicht "falsch", nur weil in einer Tabelle 8–9 steht. Stell den Bereich ein, in dem du fährst, und Cora sagt dir, wenn *du* abdriftest.
:::

## Was eine Warnung auslöst {#what-triggers-an-alert}

Eine Warnung löst aus, wenn ein Messwert einen Schwellenwert überschreitet. Cora prüft jeden Messwert, sobald er ankommt, ein einziger Messwert außerhalb deines Bereichs genügt also.

Eine Regel für die Änderungsrate achtet darauf, wie schnell sich ein Wasserwert bewegt, statt darauf, wo er steht. Nimm sie, wenn das Tempo einer Änderung wichtiger ist als die Zahl.

Ist eine Warnung aktiv, benachrichtigt sie dich nicht ständig wegen derselben Sache. Die [Abklingzeit](#cooldowns) der Regel entscheidet, wann sie dich wieder benachrichtigen darf.

## Wo Warnungen erscheinen

- Die Glocke oben rechts in den Haupt-Tabs bewahrt deinen Verlauf auf. Die Zahl zeigt, wie viele du noch nicht gelesen hast. Mehr dazu unter [Benachrichtigungen](/help/mobile-notifications).
- Eine Push-Benachrichtigung erreicht dein Handy, wenn diese Kategorie eingeschaltet ist.
- Das Widget auf dem Dashboard wird bernsteinfarben oder rot.
- Cora Max zeigt dieselben Warnungen auf seinem Bildschirm.

## Wenn Ausrüstung Aufmerksamkeit braucht {#equipment-faults}

Manche Warnungen betreffen Ausrüstung, keinen Messwert. Meldet ein Gerät wie ein Trident oder eine Jecod-Pumpe einen Fehler, schickt Cora eine Benachrichtigung mit dem Becken und dem Gerät, zum Beispiel *"Hauptbecken: Rückförderpumpe braucht Aufmerksamkeit"*. Sie sagt auch, was los ist, etwa ein blockierter Rotor. Ist der Fehler behoben, bekommst du eine zweite: *"Hauptbecken: Rückförderpumpe ist wieder in Ordnung"*. Beide fallen unter **Gerätefehler** in **Einstellungen → Benachrichtigungen**.

Ein AquaWiz KH Controller löst dieselbe Art Warnung aus, bei jedem AquaWiz und ohne Cora Max, wenn:

- seine Dosierpumpe einen Fehler meldet;
- seine pH-Sonde ausgefallen ist oder bald am Ende ihrer Lebensdauer ist.

Geht der Alkalinitäts-Zusatz zur Neige, nutzt die Warnung die Warnstufe, die du am Controller eingestellt hast. Du kannst sie weiterhin in der Warnzentrale ändern. Bleibt der Füllstand der Wasserbox länger als eine Stunde zu niedrig oder zu hoch, gibt es ebenfalls eine Warnung, dafür braucht es aber das stündliche Auslesen durch das Cora Max (siehe [Ausrüstung mit Cora Max steuern](/help/max-device-control#aquawiz-hourly)): Die 12-Stunden-Messung aus der AquaWiz-Cloud enthält ihn nicht.


## Ein Gerät meldet sich nicht mehr {#stopped-reporting}

Wird ein verbundenes Gerät still, schickt Cora *"[Gerät]: meldet sich nicht mehr"*. Das heißt nicht, dass das Gerät kaputt ist, nur, dass Cora eine Weile nichts von ihm gehört hat. Du bekommst eine zweite Benachrichtigung, *"[Gerät]: meldet sich wieder"*, wenn es zurückkommt.

Wie lange Cora wartet, hängt vom Gerät ab:

| Gerät | Cora wartet |
|---|---|
| Neptune Apex | Etwa 30 Minuten ohne Update |
| Red Sea ReefBeat | Etwa 30 Minuten |
| AquaWiz | Etwa 25 Stunden, weil AquaWiz Cora nur alle 12 Stunden die Cloud abfragen lässt |
| Jecod-Pumpen | Drei verpasste Messungen in Folge, im Messintervall der Pumpe (90 Minuten beim Standard von 30) |
| Zigbee-Steckdose | Meldet sich 30 Minuten nach einem Neustart des Gateways noch nicht zurück. Gib ihr mit **Umbenennen** einen Namen, damit die Meldung sie nennt |

Was du prüfst, hängt davon ab, wie Cora das Gerät liest.

- Apex, ReefBeat und Jecod werden von einem Cora Max über WLAN abgefragt. Prüf Strom und WLAN des Geräts und ob das Cora Max, das es abfragt, eingeschaltet und online ist.
- AquaWiz wird über dein Konto beim Hersteller abgefragt. Prüf die Kontoverbindung auf der Seite des Geräts in Cora Mobile.


Diese Benachrichtigungen fallen unter **Gerätefehler** in **Einstellungen → Benachrichtigungen**.


Ein Red Sea-Becken kann außerdem einen Banner zeigen, *"Die Red Sea-Messwerte werden nicht mehr aktualisiert"*, wenn kein Handy und kein Cora Max seine ReefBeat-Ausrüstung abfragt. Tippe darauf, um ein **Primäres Cora Max** zu wählen. Die vollständige Lösung steht in der [Problembehebung](/help/troubleshooting#red-sea-readings-have-stopped-updating).

## Wählen, was dich erreicht {#choosing-what-reaches-you}

Unter **Einstellungen → Benachrichtigungen** wählst du, welche Kategorien dir eine Push-Nachricht schicken dürfen. Siehe [Benachrichtigungen](/help/mobile-notifications), wo es auch darum geht, [die Nächte ruhig zu halten](/help/mobile-notifications#quiet-at-night).

Reef Buddy hat keinen eigenen Schalter. Seine Uhrzeit ist die Zeile **Briefing-Zeit**, direkt unter Benachrichtigungen in den Einstellungen. Im kostenlosen Abo gibt es keine Briefing-Benachrichtigung.

:::note Cora bleibt still, außer es hat sich etwas geändert
Das tägliche Briefing ist eine Push-Nachricht pro Becken und Tag. An einem Tag, an dem nichts dich braucht, bleibt es meist still, statt dir zu sagen, dass alles gut ist. Schickt Cora etwas, hat sich etwas geändert.
:::

## Abklingzeiten: wie oft dieselbe Warnung dich benachrichtigen darf {#cooldowns}

Jede Regel hat ihre eigene **Abklingzeit zwischen Warnungen**. Du stellst sie ein, wenn du die Regel hinzufügst oder bearbeitest. Eine Regel, die nie eine hatte, nutzt 1 Std.

Die Abklingzeit versteckt die Warnung nicht. Sie begrenzt nur, wie oft Cora dazu eine Push-Nachricht schickt. Der Messwert wird weiter bewertet, und die Warnung bleibt die ganze Zeit auf dem Widget und unter der Glocke.

Du kannst 15 Min., 30 Min., 1 Std., 2 Std., 4 Std., 8 Std., 1 Tag, 3 Tage oder 1 Woche wählen.

Eine kurze Abklingzeit passt zu einem schnell schwankenden Messwert wie der Temperatur. Eine lange, bis zu einer Woche, passt zu etwas, das tagelang falsch bleibt, während du auf ein Teil wartest, etwa ein Trident ohne Reagenz oder ein leerer Dosierbehälter.

:::note Verschieben gibt es auf Cora Max
Cora Mobile hat bei einer aktiven Warnung keine Taste zum Verschieben. Verschieben gibt es auf dem Cora Max-Bildschirm am Becken, und es macht die Warnung für die Abklingzeit still, die du hier gewählt hast. Auf dem Handy änderst du mit der Abklingzeit der Regel, wie oft du von etwas hörst.
:::

## Eine Warnung beenden {#clearing-an-alert}

Eine Warnung verschwindet von selbst, wenn der Messwert wieder in den Bereich kommt. Du musst nichts wegklicken. Du bekommst dann eine Benachrichtigung, zum Beispiel *"Hauptbecken: Alkalinität wieder normal"*. Kommt das Problem später zurück, bekommst du eine neue Warnung.

:::note Auch kurze Ausreißer lösen Warnungen aus
Ein einziger Messwert außerhalb des Bereichs reicht für eine Warnung, eine Sonde, die kurz ausschlägt, löst also eine aus. Ist eine Quelle unzuverlässig, kalibriere sie neu oder stell das Widget auf eine andere Quelle. Mach den Schwellenwert nicht weiter.
:::

Manchmal ist der Messwert falsch und das Becken in Ordnung, etwa wenn eine Sonde kalibriert werden muss. Kümmere dich in dem Fall um die Quelle. Machst du einen Schwellenwert weiter, um eine schlechte Sonde ruhigzustellen, verpasst du auch das nächste echte Problem.

## Eine Warnung ausschalten {#turning-an-alert-off}

Schalte den Schalter in der Zeile der Regel im Tab **Regeln** aus. Cora behält die Regel und ihren Bereich, du kannst sie also wieder einschalten, ohne sie neu einzurichten.

Solange eine Regel aus ist, bewertet Cora diesen Messwert nicht. Sein Widget bleibt neutral grau und löst nie eine Warnung aus.

:::warning Schalte einen Wasserwert aus, ohne seinen Bereich zu löschen
Eine Regel zu löschen, hält Cora nicht immer davon ab, diesen Messwert zu bewerten. Standard-Referenzbereiche färben den Wert weiter ein und können weiter ins Briefing einfließen. Nimm den Schalter der Regel.
:::

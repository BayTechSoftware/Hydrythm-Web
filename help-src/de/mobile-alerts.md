---
title: Warnungen und Schwellenwerte
description: Leg für jeden Wasserwert den Bereich fest, bestimme, worüber du Bescheid bekommst, und finde heraus, warum eine Warnung kam.
section: Cora Mobile
reviewed: 2026-09-30
order: 15
group: Alerts and automation
---

Verlässt ein Messwert den Bereich, den du festgelegt hast, meldet Cora eine Warnung. Die Bereiche legst du selbst fest, und du bestimmst auch, welche Warnungen auf deinem Handy ankommen.

Die **Warnzentrale** öffnest du über die Reihe mit Verknüpfungen am unteren Rand des Dashboards.

![Die Warnzentrale](img/mobile-alerts.webp "Aktive Warnungen, jede mit ihrem Schweregrad, was sie ausgelöst hat, und wann.")

## Die Warnzentrale

Die Warnzentrale hat zwei Tabs:

- **Aktiv** zeigt die gerade bestehenden Warnungen, mit einer Zahl daneben.
- **Regeln** zeigt die Schwellenwert- und Änderungsraten-Regeln, aus denen die Warnungen entstehen.

Zu jeder aktiven Warnung siehst du den Wasserwert und das Becken, den auslösenden Messwert und eine kurze Erklärung. Dazu kommen ein Chip für den Schweregrad, die Art der Regel (**Schwellenwert** oder **Änderungsrate**) und die Uhrzeit.

Bei jeder Warnung hast du zwei Möglichkeiten:

- **Regel ansehen** öffnet die zugehörige Regel. Dort kannst du den Bereich anpassen.
- **Diese Warnung erklären** lässt den Assistenten die Warnung vor dem Hintergrund der Geschichte deines Beckens einordnen.

## Einen Bereich festlegen

Wasserwerte, die Cora bewerten kann, haben einen Zielbereich. Die Standardwerte richten sich nach Beckentyp und Alter, die du bei der Einrichtung angegeben hast. Damit fährst du am Anfang meist gut. Hat ein Wasserwert keinen brauchbaren Bereich, bewertet Cora ihn gar nicht. Er bleibt neutral grau, und Cora rät nicht herum.

Zum Ändern **hältst du das Widget** auf dem Dashboard **lange gedrückt**. Dann gehen direkt die Schwellenwerte dieses Wasserwerts auf. Tippst du nur kurz, landest du in der Ansicht des Wasserwerts. Die beiden Gesten führen also an verschiedene Stellen. Das lange Drücken lohnt sich zu merken.

Gibt es für den Wasserwert noch keine Regel, stehen in den Feldern Coras Standardwerte. Ein Hinweis darunter sagt dir das. Ändere einfach einen Wert, dann gilt deiner.

Alle Bereiche auf einen Blick findest du unter **Warnungen** in der Reihe mit Schaltflächen unter dem Dashboard.

Du kannst Folgendes festlegen:

- **Einen Bereich** mit Unter- und Obergrenze, etwa für Alkalinität oder Temperatur
- **Eine Obergrenze** allein, für Werte, bei denen niedrig in Ordnung ist, etwa Nitrat oder Phosphat
- **Eine Untergrenze** allein

:::tip Stell den Bereich ein, in dem dein Becken wirklich läuft
Die Standardwerte sind ein Ausgangspunkt, kein Urteil. Ein nährstoffarmes Becken mit 6 dKH ist nicht "falsch", nur weil in einer Tabelle 8–9 steht. Stell den Bereich ein, in dem dein Becken läuft. Dann sagt Cora dir Bescheid, wenn *du* davon abweichst.
:::

## Wann eine Warnung kommt

Eine Warnung kommt, sobald ein Messwert einen Schwellenwert überschreitet. Cora prüft jeden Messwert beim Eintreffen. Ein einziger Messwert außerhalb deines Bereichs genügt also.

Ist eine Warnung aktiv, meldet sie sich nicht ständig neu wegen derselben Sache. Erst nach einer Abklingzeit kann sie wieder ausgelöst werden. Sobald ein Messwert wieder im Bereich liegt, **verschwindet sie von selbst**. Du musst nichts bestätigen.

Außerdem kannst du eine Regel für die **Änderungsrate** anlegen. Sie achtet darauf, wie schnell sich ein Wasserwert bewegt, und nicht darauf, wo er gerade steht. Nimm sie für Werte, bei denen das Tempo einer Veränderung wichtiger ist als die Zahl selbst.

## Wo Warnungen auftauchen

- **Die Glocke** oben rechts auf jedem Bildschirm enthält den Verlauf. Die Zahl zeigt, wie viele du noch nicht gelesen hast.
- **Push-Benachrichtigungen** kommen auf dein Handy, wenn du sie erlaubst.
- **Das Widget** auf dem Dashboard färbt sich gelb oder rot.
- **Cora Max** zeigt dieselben Warnungen auf dem großen Bildschirm.

## Wenn die Ausrüstung Hilfe braucht

Manche Warnungen betreffen die Ausrüstung und keinen Messwert. Meldet ein Gerät wie ein Trident oder eine Jecod-Pumpe einen Fehler, schickt Cora eine Benachrichtigung mit Becken und Gerät, zum Beispiel *"Display-Becken: Rückförderpumpe braucht Aufmerksamkeit"*. Darin steht auch, was los ist, etwa ein blockierter Rotor. Ist der Fehler behoben, kommt eine zweite Nachricht: *"Display-Becken: Rückförderpumpe ist wieder in Ordnung"*. Beide gehören zur Kategorie **Gerätefehler** unter **Einstellungen → Benachrichtigungen**.

Auch eine Maxspect Gyre (Beta) kann diese Warnung auslösen. Das passiert, wenn ein Cora Max im selben Netzwerk feststellt, dass beide Köpfe auf 0 % stehen, oder wenn die Gyre zweimal hintereinander nicht antwortet. Verlass dich darauf nur als Hinweis, nicht als Schutz. Das Cora Max schaut nur ab und zu nach und nur, solange es läuft und die Gyre erreicht.

## Ein Gerät meldet sich nicht mehr

Meldet sich ein Neptune Apex, ein Red Sea ReefBeat-Gerät, AquaWiz, eine Jecod-Pumpe oder eine Maxspect Gyre nicht mehr, sagt dir Cora Bescheid: *"[Gerät]: meldet sich nicht mehr."* Prüfe Stromversorgung und WLAN, und ob das Cora Max, das es ausliest, eingeschaltet ist. Die meisten Geräte lösen das nach etwa 30 Minuten ohne Update aus. AquaWiz prüft seltener, deshalb wartet es etwa 3 Stunden. Meldet sich das Gerät wieder, bekommst du eine zweite Benachrichtigung.

Das fällt wie die Fehlerwarnungen oben unter **Gerätefehler** in **Einstellungen → Benachrichtigungen**.

## "Die Red Sea-Messwerte werden nicht mehr aktualisiert"

Auf der Wasserwert-Seite eines Beckens kann dieser Banner erscheinen:

> Die Red Sea-Messwerte werden nicht mehr aktualisiert. Kein Gerät liest die Red Sea-Geräte dieses Beckens aus: Prüfe das primäre Cora Max in den Einstellungen oder öffne dieses Becken auf einem Gerät im selben Wi-Fi-Netzwerk.

Gerade fragt also weder ein Handy noch ein Cora Max die ReefBeat-Ausrüstung dieses Beckens ab. Die angezeigten Messwerte sind deshalb alt, aber nicht unbedingt falsch. Tippe auf den Banner, um **Primäres Cora Max** zu öffnen. Wähle dort ein Gerät, das eingeschaltet ist, oder stell **Jedes aktive (automatisch)** ein. Mehr dazu unter [Mehr als ein Cora-Gerät](/help/mobile-multi-device). Verschwindet der Banner nicht, hilft dir die [Problembehebung](/help/troubleshooting) weiter.

## Bestimmen, was bei dir ankommt

Unter **Einstellungen → Benachrichtigungen** legst du fest, welche Benachrichtigungskategorien dir Push-Nachrichten schicken dürfen.

Reef Buddy hat keinen eigenen Schalter. Es schickt dir eine Zusammenfassung, wenn es etwas zu tun gibt, und bleibt sonst still.

:::note Cora meldet sich nur, wenn es etwas zu sagen gibt
Die tägliche Zusammenfassung ist eine Push-Nachricht pro Becken und Tag. An Tagen, an denen nichts deine Aufmerksamkeit braucht, bleibt sie meist aus. Cora schreibt dir dann nicht extra, dass alles in Ordnung ist. Kommt eine Nachricht, hat sich etwas geändert.
:::

## Abklingzeit: wie oft dieselbe Warnung dich benachrichtigt

Jede Regel hat eine eigene **Abklingzeit zwischen Warnungen**. Du stellst sie ein, wenn du die Regel anlegst oder bearbeitest (im Tab **Regeln** der Warnzentrale). Die Warnung selbst bleibt dabei sichtbar. Die Abklingzeit begrenzt nur, wie oft Cora dir dazu eine Push-Nachricht schickt. Der Messwert wird die ganze Zeit weiter bewertet, und die Warnung bleibt auf dem Widget und in der Glocke stehen.

Zur Auswahl stehen 15 Min., 30 Min., 1 Std., 2 Std., 4 Std., 8 Std., 1 Tag, 3 Tage und **1 Woche**.

Eine kurze Abklingzeit passt zu schnell schwankenden Messwerten wie der Temperatur. Eine lange, bis zu einer Woche, passt zu Problemen, die tagelang bestehen, während du auf Ersatz wartest. Beispiele sind ein Trident ohne Reagenz oder ein leerer Dosierbehälter. Ohne lange Abklingzeit würde Cora dich mehrmals am Tag an dasselbe bekannte Problem erinnern.

:::note Schlummern geht nur am Cora Max
In Cora Mobile gibt es bei einer aktiven Warnung keine eigene Schlummern-Schaltfläche. Die findest du am Cora Max-Bildschirm am Becken. Sie schaltet die Warnung für die Abklingzeit stumm, die du hier gewählt hast. Am Handy steuerst du über die Abklingzeit der Regel, wie oft du von einer Sache hörst. Ein Schlummern für einzelne Warnungen gibt es hier nicht.
:::

## Eine Warnung beenden

Eine Warnung verschwindet, sobald der Messwert wieder im Bereich liegt. Wegklicken musst du nichts. Die Warnung beschreibt den Zustand des Beckens und ist keine Aufgabe.

:::note Auch kurze Ausreißer lösen Warnungen aus
Ein einziger Messwert außerhalb des Bereichs genügt für eine Warnung. Schlägt eine Sonde kurz aus, bekommst du also eine. Ist eine Quelle unzuverlässig, kalibriere sie neu oder stell das Widget auf eine andere Quelle um. Den Schwellenwert zu erweitern hilft hier nicht.
:::

Stimmt der Messwert nicht und das Becken ist in Ordnung (zum Beispiel, weil eine Sonde kalibriert werden muss), kümmere dich um die Quelle. Weitest du den Schwellenwert aus, um eine schlechte Sonde ruhigzustellen, überhörst du auch das nächste echte Problem.

## Warnungen für einen Wasserwert abschalten

Öffne die Regel im Tab **Regeln** der Warnzentrale und schalte ihren **Aktivierungsschalter** aus. Regel und Bereich bleiben gespeichert. Du kannst sie später wieder einschalten, ohne alles neu einzurichten.

:::warning Wasserwert stummschalten, ohne den Bereich zu löschen
Löschst du einen Schwellenwert, hört die Bewertung dieses Messwerts nicht unbedingt ganz auf. Standard-Referenzbereiche färben den Wert weiter ein und können weiter in die Zusammenfassung einfließen. Nimm deshalb den Aktivierungsschalter der Regel.
:::

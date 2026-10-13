---
title: Steckdosen und Steuerung
description: Apex-Steckdosen auf Cora Max schalten, den Fütterungsmodus starten oder abbrechen, die Schublade Steckdosen & Füttern nutzen und was Auto, Aus und Ein bedeuten.
section: Cora Max
reviewed: 2026-10-13
order: 5
group: Equipment
---

Auf dieser Seite geht es darum, auf Cora Max Steckdosen zu schalten und den Fütterungsmodus zu starten. Das geht über Steckdosen-Kacheln auf dem Dashboard, über die Schublade **Steckdosen & Füttern** oder per Sprache.

:::warning Diese Steuerung wirkt direkt auf dein Becken
Es gibt kein Rückgängig. Steckdosen mit Vorhängeschloss bitten dich vorher um Bestätigung. Alle anderen schalten, sobald du tippst. Ein Befehl kann mit **Bestätigt**, **Unbestätigt** (gesendet, aber keine Rückmeldung), **Abgelehnt** oder **Keine Änderung** zurückkommen. Mehr dazu unter [Deine Ausrüstung steuern](/help/mobile-device-control).
:::

## Die drei Zustände {#the-three-states}

Jede Steckdose ist in einem von drei Zuständen.

**Auto** gibt die Steckdose an ihre Apex-Programmierung zurück. Meistens sollte eine Steckdose dort stehen.

**Aus** und **Ein** sind manuelle Übersteuerungen. Sie wirken sofort und **bleiben, bis du sie zurückstellst**. Sie laufen nicht ab, und nichts stellt sie für dich zurück.

:::warning Eine manuelle Übersteuerung läuft nicht ab
Stell sie zurück auf **Auto**, wenn du fertig bist, denn sonst tut es niemand. Eine Übersteuerung ist aber keine Sperre. Du, deine Stimme oder eine Automation können sie später trotzdem ändern.
:::

## Auf dem Dashboard schalten {#switching-from-the-dashboard}

Steckdosen-Kacheln zeigen die drei Zustände und heben den aktuellen hervor. Tippe auf den, den du willst.

Manche Steckdosen haben ein **Vorhängeschloss**. Es bedeutet, dass die Steckdose dich vor einer Änderung um Bestätigung bittet, damit ein versehentliches Tippen nichts Wichtiges schaltet. Wenn du darauf tippst, zeigt ein Dialog die Steckdose, ihren aktuellen Zustand, die Übersteuerung, die du gleich setzt, und was das mit dem Becken machen kann. Es gibt keine Sperre, die du anderswo ausschalten müsstest.

Standardmäßig haben Heizer, Kühler, Rückförderpumpen, Nachfüllanlage (ATO), Futterautomaten und jede Steckdose, die Cora nicht einordnen kann, das Vorhängeschloss. Licht, Abschäumer, Strömungspumpen, Dosierpumpen, Reaktoren, UV und Lüfter schalten mit einem Tippen.

## Die Schublade Steckdosen & Füttern {#the-controls-drawer}

Du siehst sie nur bei einem Becken mit Neptune Apex. Tippe auf die kleine Beschriftung **Steckdosen & Füttern** unten auf dem Dashboard oder wisch irgendwo auf dem Dashboard nach oben. Das öffnet **Steuerung**, mit **FÜTTERN** oben und **STECKDOSEN** darunter.

![Die Schublade Steuerung](img/max-controls.webp "Oben die Fütterungszyklen, darunter die Steckdosen, die für dieses Dashboard ausgewählt sind.")

Sie zeigt die Steckdosen und Fütterungszyklen, die du im [Dashboard-Editor](/help/max-dashboard-editing#outlets-feed) unter **Steckdosen & Füttern** ausgewählt hast, oder alle, wenn du keine ausgewählt hast. Steckdosen mit Vorhängeschloss bitten auch hier um Bestätigung. Anschlüsse an anderen Controllern schaltest du auf ihren eigenen Geräteseiten, siehe [Ausrüstung mit Cora Max steuern](/help/max-device-control).

Kommt nach dem Tippen auf eine Steckdose *Der Apex hat nicht geantwortet: Es wurde möglicherweise übernommen* zurück, prüf die Steckdose, bevor du es noch einmal versuchst.

## Fütterungsmodus {#feed-mode}

Mit dem Fütterungsmodus pausierst du die Strömung sicher, während du fütterst. Dein Apex pausiert die Ausrüstung, die pausieren soll, lässt den Rest in Ruhe und **stellt alles von selbst wieder her**, wenn die Zeit um ist.

Nimm ihn, statt Pumpen von Hand auszuschalten. Er stellt das System auch dann wieder her, wenn du es vergisst.

Die Fütterungszyklen sind Feed A, Feed B, Feed C und Feed D und erscheinen unter **FÜTTERN** als **A**, **B**, **C** und **D**. Es sind die Zyklen, die auf deinem Apex programmiert sind, und jeder kann andere Ausrüstung pausieren. Wähl den, der zu dem passt, was du vorhast. **Abbrechen** beendet einen laufenden Zyklus vorzeitig und stellt alles sofort wieder her.

Starte einen in der Schublade oder sag *"Fütterungsmodus starten"*.

Sagt Cora Max, dass der Apex nicht geantwortet hat, läuft die Fütterung vielleicht schon. Prüf die Rückförderpumpe, bevor du sie noch einmal startest.

## Per Sprache {#by-voice}

Du kannst Steckdosen per Sprache schalten, zum Beispiel *"Schalte den Abschäumer aus"* oder *"Stell den Lüfter zurück auf Auto"*.

Bevor etwas deine Ausrüstung erreicht, **fragt Cora erst bei dir nach**. Cora sagt dir, was gleich passiert, und wartet auf dein OK. Ist Cora nicht sicher, was du meinst, passiert nichts.

Mehr dazu unter [Mit Cora sprechen](/help/max-voice).

## Nachsehen, was passiert ist {#seeing-what-happened}

Jede Anfrage wird protokolliert, mit dem, was sie ausgelöst hat, und wie sie ausgegangen ist, egal ob sie aus Cora Mobile, von einem Cora Max, per Sprache, vom Assistenten oder von einer Automation kam. Auf Cora Max tippst du in der oberen Leiste auf den Beckennamen und wählst **Aktivität**. Auf dem Handy findest du es unter **Einstellungen → Aktivität**. Mehr dazu unter [Aktivität auf Cora Max](/help/max-activity).

Hat sich etwas geändert und du weißt nicht, warum, schau zuerst dort nach.

---
title: Dosierprodukte und Dosierrechner
description: Die Stärke deiner Alkalinitäts-, Calcium- und Magnesiumprodukte prüfen, eigene hinzufügen und mit dem Dosierrechner ausrechnen, wie viel du zugeben musst.
section: Cora Mobile
reviewed: 2026-10-13
order: 28
group: Records
---

Cora kann nur dann Dosierungen berechnen, wenn es weiß, wie stark deine Produkte sind. Auf dieser Seite geht es um die Produktliste und den Dosierrechner, der sie nutzt.

Geh zu **Einstellungen → Dosierprodukte**.

![Dosierprodukte](img/mobile-dosing.webp "Produkte tragen die Stärke, die Cora für Dosier- und Verbrauchsberechnungen nutzt.")

## Die Produktbibliothek {#the-product-library}

Der Bildschirm **Dosierprodukte** listet schon gängige Produkte auf, gruppiert unter **Alkalinität (dKH)**, **Calcium (ppm)** und **Magnesium (ppm)**. Such deins und tippe darauf, um seine Stärke zu prüfen.

Jede Stärke gibt an, wie stark 1 ml (oder 1 g eines Trockenprodukts) den Wasserwert in einer festen Wassermenge anhebt. Mit dieser Zahl wird aus "5 ml" ein "+0,2 dKH in deinem Becken". Wechsle oben zwischen **pro 100 L** und **pro 100 gal**.

Ändere eine eingebaute Stärke nur, wenn auf deiner Flasche etwas anderes steht. Tippe auf das Produkt, um **Stärke anpassen** zu öffnen. **Auf Standard zurücksetzen** holt den Wert von Cora zurück.

## Eigene Produkte hinzufügen {#adding-your-own}

Steht dein Produkt nicht in der Liste, tippe auf **+** (**Eigenes Produkt hinzufügen**). Gib ihm einen **Produktname**, wähl **Flüssig (ml)** oder **Trocken (g)** und trag seine Stärke für Alkalinität, Calcium oder Magnesium ein. Lass ein Feld leer, wenn das Produkt diesen Wert nicht verändert. Ein Zwei-Komponenten-Produkt füllt je eins aus, ein Komplettprodukt mehrere.

Die Stärke steht fast immer auf dem Etikett, etwa "1 ml pro 100 Liter hebt die Alkalinität um 0,1 dKH".

:::warning Nimm die Stärke, die der Hersteller angibt
Stimmt die Stärke nicht, liegt jede Dosis, die Cora für dieses Produkt berechnet, im selben Verhältnis daneben. Findest du die Zahl nicht, lass das Produkt weg. Rate nicht.
:::

Nitrat- und Phosphatprodukte kommen im Rechner aus der eigenen Liste von Cora. Hier kannst du sie nicht hinzufügen.

Die **Salzmischung** deines Beckens ist kein Dosierprodukt. Du legst sie im Profil des Beckens fest, und Cora hat dafür einen Katalog gängiger Meersalze mit ihren veröffentlichten Werten und Quellen zur Auswahl. Siehe [Dein Beckenprofil](/help/mobile-tank-profile).

## Der Dosierrechner {#the-dose-calculator}

Der Rechner berechnet, wie viel Produkt nötig ist, um einen Wasserwert auf seinen Zielwert zu bringen. Es gibt ihn für Alkalinität, Calcium, Magnesium, Nitrat und Phosphat.

1. Tippe auf dem Dashboard auf das Widget des Wasserwerts, um ihn zu öffnen.
2. Tippe oben auf das Rechnersymbol. Ein Punkt daran heißt, dass der Messwert unter dem Ziel liegt.
3. Prüf die Zahlen, die Cora eingetragen hat:
   - Der aktuelle Wert ist dein neuester Messwert. Aktualisiere ihn, wenn du gerade getestet hast.
   - Das Ziel ist die Mitte deines Warnbereichs für diesen Wasserwert oder der übliche Riffbereich, wenn du keinen festgelegt hast.
   - **Nettowasservolumen (l)** sind 90 % deines Beckenvolumens, um Gestein und Sand zu berücksichtigen. Ändere es, wenn du die echte Zahl kennst.
4. Wähl das **Produkt**. Deine eigenen Produkte aus dem Beckenprofil kommen zuerst, dann Vorgaben der Marken. Du kannst auch eine **Eigene Stärke** eingeben.

Cora zeigt die Gesamtmenge, die nötig ist, um das Ziel zu erreichen.

:::warning Verteil eine große Korrektur
Der Rechner gibt die Gesamtmenge an, keine Tagesdosis. Ist die Gesamtmenge ein größerer Sprung, als an einem Tag sicher ist, sagt er das, und du teilst sie auf mehrere Tage auf. **Cora fragen** öffnet Cora Assistant mit deinen Zahlen, wenn du Hilfe beim Planen der Tagesmenge willst.
:::

Wenn du dosiert hast, tippe auf **Die verabreichte Dosis protokollieren**. Das fügt einen Eintrag zu deinem [Tagebuch](/help/mobile-journal) hinzu.

Liegst du schon auf oder über dem Ziel, sagt dir der Rechner, dass es nichts zuzugeben gibt. Einen Wasserwert kannst du nicht nach unten dosieren. Die Antwort ist ein Wasserwechsel, ein Wechsel des Filtermediums oder eine Änderung an dem, was du schon dosierst.

Das Volumen ist hier wichtig. Liegt es um 20 % daneben, liegen auch die Dosierungen um 20 % daneben.

## Verbrauch {#consumption}

Sobald Cora sowohl deine Dosierungen als auch deine Messwerte sieht, kann es ausrechnen, was dein Becken verbraucht, und dir sagen, wenn sich das ändert.

Ändert sich der Bedarf, schau genauer hin, bevor du Schlüsse ziehst. Steigender Alkalinitätsbedarf heißt oft Wachstum, aber eine plötzliche Änderung in die eine oder andere Richtung kann auch von einer verpassten Dosierung, einem Testfehler, einer Ausfällung, einem Wasserwechsel oder einer Änderung an der Technik kommen. Prüf, was sich um dieses Datum herum noch geändert hat.

## Dosiertechnik {#dosing-equipment}

Hast du eine verbundene Dosierpumpe, etwa einen Neptune DŌS oder einen Red Sea ReefDose, erscheinen ihre Köpfe mit eigenen Messwerten, auch was jeder Kopf noch übrig hat und was er dosiert hat. Wie du sie betreibst und nachfüllst, steht unter [Deine Ausrüstung steuern](/help/mobile-device-control), und ihre Warnungen für leere Behälter und verpasste Dosierungen stehen unter [Dosierpumpen-Warnungen](/help/mobile-device-control#doser-alerts).

Eine Automation kann auch aus einem DŌS-Kopf dosieren, begrenzt auf 10 ml pro Kopf und Tag. Siehe [Automationen und Szenen](/help/mobile-automation#actions).

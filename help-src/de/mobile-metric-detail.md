---
title: Einen Wasserwert genauer ansehen
description: Tippe auf ein Widget, um den ganzen Verlauf eines Wasserwerts zu sehen, Quellen und Wasserwerte zu vergleichen, einen falschen Messwert auszuschließen und Sondenpflege festzuhalten.
section: Cora Mobile
reviewed: 2026-10-13
order: 7
group: Your dashboard
---

Ein Widget zeigt dir eine Zahl. Tippe darauf, um die Geschichte hinter dieser Zahl zu sehen.

Es gibt zwei Wege hinein. Tippe auf ein Widget auf dem Dashboard, oder tippe in der Reihe von Tasten unter den Widgets auf **Werteverlauf** und wähl einen Wasserwert. **Werteverlauf** listet jeden Wasserwert mit Daten auf, auch einen ohne Widget auf dem Dashboard.

## Was du bekommst {#what-you-get}

![Einen Wasserwert genauer ansehen](img/mobile-metric-detail.webp "Oben die Dropdowns, dann das Diagramm mit deinem schattierten Warnband.")

- Ein Verlaufsdiagramm. Die Reihe darüber legt fest, was es zeigt. **Parameter** wechselt zu jedem anderen Wasserwert mit Daten und behält deinen Zeitraum. **Zeitraum** reicht von 1h über 6h, 12h, 24h, 3d, 7d, 15d, 30d, 90d, 180d und 360d bis Alle. **Quelle** beginnt bei **Alle Quellen** und listet die Quellen auf, die diesen Wasserwert an diesem Becken melden, etwa *Apex*, *Cora*, *Red Sea* oder *Manuell*. Wähl eine, um nur ihre Messwerte zu sehen.
- **Vergleichen**, am Ende derselben Reihe, zeichnet einen zweiten Wasserwert ins Diagramm, etwa Alkalinität mit Calcium oder pH mit Temperatur. Die Taste zeigt dann **vs** und den Namen des anderen Wasserwerts. Tippe noch einmal darauf, um die zweite Linie wegzunehmen.
- Eine Zeile mit **Neuester**, **Min**, **Durchschn.** und **Max** für den angezeigten Zeitraum.
- Symbole in der oberen Leiste: **Messwerte** öffnet die Liste der Rohmesswerte, und **Sondenpflege erfassen** hält eine Kalibrierung oder Reinigung fest. Bei Alkalinität, Calcium und Magnesium gibt es außerdem den Dosierrechner, der das Beckenvolumen aus deinem [Beckenprofil](/help/mobile-tank-profile) und die Stärken aus [Dosierung](/help/mobile-dosing) nutzt.

Der Bildschirm öffnet sich immer mit 24h und **Alle Quellen**. Er merkt sich nicht, was du beim letzten Mal gewählt hast.

## Das Diagramm lesen {#reading-the-chart}

- Das grüne Band ist dein Warnbereich, du siehst also jeden Messwert im Verhältnis dazu. Um den Bereich zu ändern, drück auf dem Dashboard lange auf das Widget. Mehr dazu unter [Warnungen und Schwellenwerte](/help/mobile-alerts).
- Eine gestrichelte Linie markiert eine eingetragene Dosierung, damit du eine Änderung mit dem abgleichen kannst, was du dosiert hast.
- **30 T. Hoch** und **30 T. Tief** sind gestrichelte Linien, die die Extreme der letzten 30 Tage zeigen.
- Ein hohler Punkt ist ein Messwert, den du ausgeschlossen hast.
- Mit eingeschaltetem **Vergleichen** nutzt der zweite Wasserwert die rechte Achse.

## Einen Zeitraum wählen {#choosing-a-range}

Wähl den Zeitraum, der dazu passt, wie sich der Wasserwert bewegt.

| Wasserwert | Sinnvoller Zeitraum |
|---|---|
| pH | 24 Stunden, weil er im Tagesrhythmus schwankt |
| Temperatur | 24 Stunden oder 7 Tage |
| Alkalinität | 7 oder 30 Tage |
| Spurenelemente | 30 Tage oder ein Jahr |

:::note Flache Linie? Prüf, wie alt der Messwert ist
Eine Linie, die sich nicht bewegt, kann heißen, dass der Wasserwert stabil ist. Sie kann auch heißen, dass die Quelle nichts mehr meldet. Das Alter neben dem Wert auf dem Widget sagt dir, was davon.
:::

## Quellen vergleichen {#comparing-sources}

Melden mehrere Quellen einen Wasserwert, hält Cora sie getrennt und mittelt sie nicht. Nutze das Dropdown **Quelle**, um dir jede anzusehen. So vergleichst du am schnellsten eine Sonde mit einem Testkit.

Auf dem Dashboard steht der neueste. Ein aktueller Wert wird nur durch einen Messwert mit späterem Messzeitpunkt ersetzt, aus welcher Quelle auch immer. Ein älterer Messwert geht in den Verlauf und überschreibt nicht, was auf dem Widget steht. Hast du unter **Parameterzuordnung** eine Quelle festgelegt, folgt Cora stattdessen dieser Quelle.

Liegen eine Sonde und deine von Hand eingetragenen Tests dauerhaft um denselben Betrag auseinander, muss meist die Sonde kalibriert werden.

Ein [ICP-Ergebnis](/help/mobile-icp-health) ist eine nützliche dritte Meinung, entscheidet die Frage aber nicht. Labore unterscheiden sich, und wie die Probe behandelt, gelagert und verschickt wurde, verändert das Ergebnis. Betrachte einen ICP als Hinweis. Zwei Tests, die übereinstimmen, sind viel mehr wert als einer.

## Festlegen, welcher Quelle ein Messwert folgt {#choosing-which-source-a-widget-trusts}

Die Quelle wird pro Becken und pro Wasserwert festgelegt, nicht pro Widget. Geh zu **Einstellungen**, tippe auf das Becken, dann auf **Parameterzuordnung** und dann auf den Tab **Quellen**. Wähl eine Sonde oder **Automatisch (neueste Messung gewinnt)**. Die Wahl gilt für diesen Wasserwert überall im Becken. Mehr dazu unter [Parameterzuordnung](/help/mobile-probes).

## Einen falschen Messwert ausschließen {#excluding-a-bad-reading}

Vielleicht hat eine Sonde ausgeschlagen, du hast einen Test falsch abgelesen, oder du hast die Probe mitten in einem Wasserwechsel genommen. Ein falscher Messwert verzerrt das Diagramm, die Durchschnitte und alles, was daraus berechnet wird.

![Die pH-Messwertliste in Cora Mobile](img/mobile-readings.webp "Jeder Messwert hinter der Linie, mit Zeit und Quelle. Tippe auf einen, um ihn auszuschließen.")

Tippe in der oberen Leiste auf **Messwerte** und dann auf einen Messwert. Cora fragt **Diesen Messwert ausschließen?** und erklärt, dass er in deinem Protokoll bleibt, aber nicht mehr für Durchschnitte, Trends, Erkenntnisse und den Assistenten zählt. Tippe auf **Ausschließen**. Es wird nichts gelöscht, und du kannst ihn auf demselben Weg zurückholen.

Messwerte, die älter als 90 Tage sind, lassen sich nicht ausschließen oder zurückholen.

:::warning Schließ falsche Messwerte aus, keine unwillkommenen
Schließ nur einen Messwert aus, von dem du weißt, dass er ungültig ist. Gefällt dir ein Messwert nur nicht, du findest aber keinen Fehler daran, sind es echte Daten. Ihn zu entfernen, macht jeden späteren Vergleich weniger ehrlich.
:::

## Sondenpflege erfassen {#recording-probe-care}

Tippe auf **Sondenpflege erfassen** (das Sensorsymbol in der oberen Leiste) und wähl, was du gemacht hast: kalibriert, gereinigt, ersetzt, umgesetzt oder verglichen. Cora versieht diese Quelle mit dem Datum, damit eine frische Kalibrierung nicht für Drift gehalten wird. Widerspricht die Sonde später etwas, siehst du, wann sie zuletzt gepflegt wurde. Mehr dazu unter [Parameterzuordnung und Sonden](/help/mobile-probes).

## Einen Messwert von Hand eintragen {#logging-a-reading-by-hand}

Messwerte trägst du auf dem Dashboard ein, nicht auf diesem Bildschirm. Tippe unter den Widgets auf **Wasserwerte protokollieren** und gib ein, was dein Testkit anzeigt. Die Liste ist gruppiert, und die Gruppe **Spurenelemente** umfasst Jod, Eisen und Kupfer in µg/L und Kalium in mg/L. Von Hand eingetragene Messwerte zählen genauso viel wie alle anderen. Sie bekommen ihre eigene Quelle und Zeit, erscheinen im Diagramm und fließen in Reef Buddy ein. Mit ihnen prüft Cora auch deine Ausrüstung.

:::note Cora prüft seltsam aussehende Eingaben nach
Liegt ein Wert weit weg von dem, wo das Becken bisher war, bittet Cora dich vor dem Speichern um Bestätigung. Das fängt ein Komma an der falschen Stelle ab oder einen Messwert, der beim falschen Wasserwert eingetragen wurde. Bestätigst du, wird der Messwert wie gewohnt gespeichert.
:::

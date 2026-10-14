---
title: Dein Dashboard lesen
description: So liest du das Dashboard von Cora, von Widgets, Alter der Messwerte und Quellen bis zu dem, was die Farben bedeuten, und den Karten, die kommen und gehen.
section: Cora Mobile
reviewed: 2026-10-13
order: 6
group: Your dashboard
---

Das Dashboard ist ein Raster aus **Widgets** für ein Becken. Jedes Widget zeigt eine Sache. Was darauf kommt, entscheidest du, wie unter [Dein Dashboard bearbeiten](/help/mobile-dashboard-editing) beschrieben.

![Ein Dashboard in Cora Mobile](img/mobile-dashboard.webp "Die Beckenkopfzeile und die Reef Buddy-Karte, dann Anzeigen, Werte, Diagramme und Gerätekacheln.")

## Die Beckenkopfzeile {#the-tank-header}

Jedes Dashboard beginnt mit:

- Dem Beckennamen, mit einem kleinen Zeichen daneben. Tippe auf den Namen, um das Becken umzubenennen. Mehr tut er nicht.
- **Füttern**, nur bei einem Becken mit Neptune Apex. Es öffnet **Fütterungsmodus** mit den Zyklen **Feed A** bis **Feed D** deines Apex. Dein Apex entscheidet, was pausiert und wann es zurückkommt, so wie du es dort eingerichtet hast. Während ein Zyklus läuft, zeigt die Taste, welcher es ist, zum Beispiel **Feed A**. Tippe darauf und wähl **Fütterung abbrechen**, um ihn vorzeitig zu beenden. Unterwegs schickt ein Cora Max am Becken den Befehl für dich.
- Dem Zeitungssymbol, das das neueste **Reef Buddy**-Briefing öffnet.
- Dem Teilen-Symbol, das einen Schnappschuss des Beckens macht. Siehe [Dein Becken teilen](/help/mobile-sharing).
- Dem Lineal, das **Einheiten** für dieses Becken öffnet. Siehe [Dein Beckenprofil](/help/mobile-tank-profile#units).
- Dem Stift rechts, der [das Beckenprofil](/help/mobile-tank-profile) öffnet.

:::note Drei Bedienelemente, die sich ähneln
Der Beckenname benennt das Becken um. Der Stift rechts öffnet das **Profil** des Beckens. Um das Dashboard selbst zu bearbeiten, tippe auf **Dashboard bearbeiten** direkt unter den Widgets.
:::

Hast du mehr als ein Becken, wisch zur Seite, um zwischen ihnen zu wechseln. Siehe [Deine Becken verwalten](/help/mobile-tanks).

## Die Reef Buddy-Karte {#the-reef-buddy-card}

Über den Widgets fasst eine Karte das neueste Briefing zusammen. Sie zeigt die Schlagzeile, eine Bewertung von 100, sobald Cora genug Daten hat, das Datum und wie viele Insights und abdriftende Messwerte es gibt. Tippe darauf, um das ganze Briefing zu öffnen, oder schließ sie mit **×**. Mit dem nächsten Briefing erscheint eine neue Karte. Mehr dazu unter [Reef Buddy](/help/mobile-reef-buddy).

## Ein Wasserwert-Widget lesen {#how-to-read-a-parameter-widget}

Ein Widget für einen **gemessenen Wasserwert** zeigt immer dieselben drei Dinge an denselben Stellen. Geräte- und Steuerungskacheln, etwa eine Steckdose, eine Dosiereinheit oder eine Pumpe, zeigen stattdessen ihren eigenen Zustand, weil hinter ihnen kein einzelner Messwert steht.

Der Wert ist der Messwert selbst, groß in der Mitte.

Das Alter steht darunter oder daneben, als `now`, `1h` oder `2d`. Es ist, wie lange es her ist, dass die Quelle diesen Wert zuletzt bestätigt hat, nicht wann der Bildschirm zuletzt aktualisiert hat. Bei einer Sonde ist das, wann ihr Gerät sich zuletzt gemeldet hat, ein gleichbleibender Messwert einer funktionierenden Sonde bleibt also frisch, auch wenn sich die Zahl nicht ändert. Bei einem Testkit- oder ICP-Ergebnis ist es, wann du den Test gemacht hast. Ein Alter, das bei einer Sonde immer weiter wächst, heißt, dass ihr Gerät sich nicht mehr meldet.

Das Quellenabzeichen ist die kleine Markierung neben dem Alter. Es zeigt, woher die Zahl kommt: von einer Sonde, einem Controller, einem Laborergebnis oder von dir mit einem Testkit. Tippe auf das Widget, um die Quelle ausgeschrieben zu sehen, mit ihrem jüngsten Verlauf.

:::note Warum das Alter wichtig ist
Ein perfekter Alkalinitäts-Messwert von vor vier Tagen ist nicht deine Alkalinität heute. Jeder Wert zeigt sein Alter, damit du den Unterschied schnell siehst.
:::

## Farben {#colours}

Cora nutzt wenig Farbe, und jede Farbe bedeutet immer dasselbe:

| Farbe | Bedeutung |
|---|---|
| Grün | Sicher innerhalb des Bereichs für diesen Wasserwert |
| Bernstein | Nah am Rand. **Meist noch innerhalb des Bereichs**, im letzten Zehntel davon |
| Rot | Über den Rand hinaus, und es lohnt sich zu handeln |
| Grau | Keine Bewertung. Es gibt keinen aktuellen Messwert oder keinen brauchbaren Bereich zum Bewerten |

:::note Bernstein heißt meist "für jetzt in Ordnung, aber mit Drift"
Bernstein ist ein Puffer. Ein Messwert innerhalb seines Bereichs, aber in dessen letzten 10 %, wird bernsteinfarben, damit du eine Drift siehst, solange noch Zeit zum Handeln ist.

Es gibt zwei Feinheiten.

**Ein Bereich, den du selbst festlegst, ist eine harte Grenze.** Überschreitest du ihn, wird das Widget sofort rot, ohne bernsteinfarbenen Puffer. Ein Bereich, den **Cora vorgibt**, ist weicher. Wird er überschritten, zeigt das Widget für die ersten 10 % jenseits des Rands Bernstein und danach Rot.

**Eine einseitige Grenze**, etwa eine Obergrenze für einen Schadstoff oder eine Untergrenze für einen Nährstoff, wird nur an ihrer oberen Kante bewertet. Kupfer bei null ist also grün und wird nicht bernsteinfarben, weil es am unteren Ende der Skala liegt.
:::

Ein Widget mit bernsteinfarbenem oder rotem Rahmen braucht Aufmerksamkeit. Das ganze Widget bekommt den Rahmen, damit du es beim Scrollen bemerkst.

Um einen Bereich zu ändern, drück lange auf das Widget. Mehr dazu unter [Warnungen und Schwellenwerte](/help/mobile-alerts).

## Karten, die kommen und gehen {#cards-that-come-and-go}

Manche Karten erscheinen nur, wenn es etwas zu sagen gibt. Die meisten sitzen zwischen der Kopfzeile und den Widgets.

| Karte | Wann sie erscheint | Worauf du tippst |
|---|---|---|
| **Startest du ein neues Becken?** | Bei einem Becken ganz ohne Messwerte. Hast du angefangen, wird daraus **Einfahren fortsetzen** | Die Karte, um das geführte Einfahren zu starten. Siehe [Geführte Journeys](/help/mobile-journeys) |
| **Beckenwerte** mit *Noch keine Messwerte* | Das Becken hat noch keine Messwerte | **Becken konfigurieren** |
| *Deine Messwerte waren nicht erreichbar: Zeigt zwischengespeicherte Daten.* | Cora kann die neuesten Messwerte nicht laden, oft ohne Verbindung | **Erneut versuchen** |
| **Laborergebnis von {lab} wartet auf dich.** | Ein Labor hat ein Ergebnis geschickt, und Cora muss wissen, für welches Becken es ist | **Becken wählen**. Siehe [ICP und Gesundheitsberichte](/help/mobile-icp-health) |
| Profilhinweis (**Schalte klügere Einblicke frei**) | Das Beckenprofil ist zu weniger als 80 % ausgefüllt | Die Karte, um mit dem Profil weiterzumachen |
| **Cora Pro Testphase: noch 9 Tage** | Die letzten Tage deiner Testphase | Die Karte oder **Pro behalten**. Siehe [Pläne und Abos](/help/mobile-plans) |
| **Reef Buddy** | Ein Briefing ist fertig | Die Karte |
| **Wie fütterst du normalerweise?** | Du hast keinen Fütterungsplan festgelegt | **Routine einrichten** |
| *Die Red Sea-Messwerte werden nicht mehr aktualisiert.* | Nichts fragt die Red Sea-Geräte dieses Beckens ab | Siehe [Warnungen und Schwellenwerte](/help/mobile-alerts) |
| **Trage deinen ersten Wassertest ein** | Keine Messwerte und keine verknüpfte Ausrüstung, unter den Widgets | Die Karte. Siehe [Cora Mobile einrichten](/help/mobile-setup#the-first-test-card) |

## Unter den Widgets {#below-the-widgets}

![Der untere Teil des Dashboards in Cora Mobile](img/mobile-dashboard-foot.webp "Dashboard bearbeiten, die Tasten Wasserwerte protokollieren, Werteverlauf und Fütterung und Verknüpfungen zu den vier Aufzeichnungsbereichen.")

Von oben nach unten findest du:

- Eine Zeile, die sagt, wann das Dashboard zuletzt aktualisiert wurde und welche Quellen es genutzt hat, mit **Dashboard bearbeiten** daneben. Das öffnet den [Dashboard-Editor](/help/mobile-dashboard-editing).
- Die Karte **Trage deinen ersten Wassertest ein**, bei einem Becken ohne Messwerte und ohne verknüpfte Ausrüstung.
- **Wasserwerte protokollieren**, um Testkit-Messwerte von Hand einzutragen.
- **Werteverlauf**, um den Verlauf jedes Wasserwerts mit Daten zu öffnen, auch eines ohne Widget. Siehe [Einen Wasserwert genauer ansehen](/help/mobile-metric-detail).
- **Fütterung**, um eine Fütterung einzutragen, die von deinem Plan abweicht. Siehe [Das Tagebuch](/help/mobile-journal).
- **Tagebuch · Warnungen · Wartung · Besatz**, Verknüpfungen zu diesen Bereichen für dieses Becken.

## Tippen und lange drücken {#tapping-through}

Tippe auf ein beliebiges Wasserwert-Widget, um seine Details zu öffnen. Du siehst den ganzen Verlauf als Diagramm, jede Quelle, die ihn gemeldet hat, und dein Warnband. Von dort kannst du Quellen vergleichen, einen falschen Messwert ausschließen oder Sondenpflege erfassen. Siehe [Einen Wasserwert genauer ansehen](/help/mobile-metric-detail).

**Drück lange** auf ein Wasserwert-Widget, um seinen Warnbereich direkt vom Dashboard aus festzulegen.

## Wenn ein Widget keinen Wert hat {#if-a-widget-has-no-value}

Ein Widget zeigt einen Wert, sobald es einen bekommt. Ist es leer, liegt es meist an einem davon:

- Das Gerät ist offline. Prüf den Tab **Geräte**.
- Der Wasserwert hat noch keine Quelle. Trag ihn von Hand ein oder verbinde Ausrüstung, die ihn meldet.
- Für den Wasserwert wurde noch nie etwas gemeldet oder eingetragen.

Ein alter Messwert verschwindet nicht, nur weil er älter ist als das Diagrammfenster. Er bleibt mit seinem Alter auf dem Widget, ein veralteter Wert sieht also veraltet aus und nicht fehlend.

Für alles andere siehe [Problembehebung](/help/troubleshooting#a-widget-shows-no-value).

---
title: Dein Dashboard lesen
description: So liest du Coras Dashboard, von den Widgets über Alter und Quellen bis zu den Farben.
section: Cora Mobile
reviewed: 2026-09-09
order: 5
group: Your dashboard
---

Das Dashboard ist ein Raster aus **Widgets**. Jedes zeigt eine Sache zu einem Becken. Was darauf steht, bestimmst du ganz allein. Wie das geht, steht unter **[Dein Dashboard bearbeiten](/help/mobile-dashboard-editing)**.

![Ein Cora Mobile Dashboard](img/mobile-dashboard.webp "Anzeigen, Zahlen, Trends und Steuerungen auf einem Bildschirm.")

## Die Kopfzeile des Beckens

Ganz oben auf jedem Dashboard findest du:

- **den Beckennamen** mit einem kleinen Symbol daneben. Damit benennst du das Becken **schnell um**, sonst nichts.
- **Füttern** pausiert Strömung und Abschäumer für die Fütterung und stellt danach alles wieder her.
- **Reef Buddy** öffnet die Zusammenfassung von heute Morgen.
- **Teilen** verschickt einen Schnappschuss des Dashboards.
- **den Stift rechts**. Er öffnet [das Beckenprofil](/help/mobile-tank-profile).

:::note Drei ähnliche Symbole, drei Ziele
Das Symbol neben dem Namen benennt das Becken um. Der Stift rechts öffnet das **Profil** des Beckens. Das Dashboard selbst bearbeitest du mit keinem von beiden, sondern über **Dashboard bearbeiten** ganz *unten* auf dem Dashboard, unter den Widgets.
:::

Hast du mehrere Becken, wischst du seitlich zwischen ihnen hin und her.

## Die Reef Buddy-Karte

Unter der Kopfzeile fasst eine Karte die neueste Zusammenfassung zusammen. Du siehst eine Schlagzeile, die Werte für **Stabilität** und **Daten** und die Zahl der Insights. Tippe darauf, um die ganze Zusammenfassung zu öffnen, oder blende die Karte mit **×** aus. Mit der nächsten Zusammenfassung kommt eine neue Karte.

## Ein Wasserwert-Widget lesen

Ein Widget für einen **gemessenen Wasserwert** zeigt immer dieselben drei Dinge an denselben Stellen. Kacheln für Geräte und Steuerungen, etwa eine Steckdose, eine Dosiereinheit oder eine Pumpe, zeigen ihren eigenen Zustand. Hinter ihnen steht kein einzelner Messwert.

Der **Wert** ist der Messwert selbst, groß in der Mitte.

Das **Alter** steht darunter oder daneben: `jetzt`, `1h`, `2d`. Es gibt an, wie lange die Messung her ist, und nicht, wann der Bildschirm zuletzt aktualisiert wurde. Hat sich eine Zahl seit zwei Tagen nicht bewegt, steht dort `2d`. Auch das sagt dir etwas.

Das **Quellen-Abzeichen** ist die kleine Markierung neben dem Alter. Es zeigt, woher die Zahl kommt: von einer Sonde, einem Controller, einem Laborergebnis oder von dir mit einem Testkit. Tippst du auf ein Widget, siehst du die Quelle ausgeschrieben und dazu die jüngste Historie.

:::note Warum das Alter so wichtig ist
Ein perfekter Alkalinitäts-Messwert von vor vier Tagen ist kein aktueller Alkalinitäts-Messwert. Deshalb steht das Alter neben jedem Wert, und du siehst den Unterschied sofort.
:::

## Farben

Cora setzt Farbe sparsam ein, und jede Farbe bedeutet immer dasselbe:

| Farbe | Bedeutung |
|---|---|
| Grün | sicher im Bereich für diesen Wasserwert |
| Gelb | nah am Rand. **Meist noch im Bereich**, aber im letzten Zehntel |
| Rot | über den Rand hinaus, du solltest etwas tun |
| Grau | keine Bewertung, weil es keinen aktuellen Messwert oder keinen brauchbaren Bereich zum Vergleich gibt |

:::note Gelb heißt meist "noch in Ordnung, aber mit Tendenz"
Gelb ist ein *Puffer*, noch kein Verstoß. Liegt ein Messwert im Bereich, aber in dessen letzten 10 %, färbt Cora ihn gelb. So siehst du, wohin sich ein Wert bewegt, solange du noch Zeit zum Handeln hast, und nicht erst, wenn es schon ein Problem ist.

Dazu gibt es zwei Feinheiten.

Einen Bereich, den du selbst festgelegt hast, behandelt Cora als feste Grenze. Überschreitet ein Wert sie, wird das Widget sofort rot, ohne gelben Puffer. Du hast diese Linie ja bewusst gezogen. Ein Bereich, den **Cora vorgibt**, ist eher ein Richtwert. Wird er überschritten, zeigt das Widget für die ersten 10 % jenseits des Rands Gelb und erst danach Rot.

Eine einseitige Grenze, also eine Obergrenze für einen Schadstoff oder eine Untergrenze für einen Nährstoff, bewertet Cora nur an ihrer oberen Kante. Kupfer bei null ist also grün und wird nicht gelb, nur weil es am unteren Ende der Skala liegt.
:::

Hat ein Widget einen gelben oder roten Rahmen, solltest du hinschauen. Der Rahmen liegt um das ganze Widget. So fällt er dir auch beim Scrollen auf.

## Unter den Widgets

![Der untere Rand des Dashboards](img/mobile-dashboard-foot.webp "Dashboard bearbeiten, Wasserwerte protokollieren, und Verknüpfungen zu den vier Aufzeichnungsbereichen.")

Ganz unten auf dem Dashboard findest du:

- **Dashboard bearbeiten** öffnet den [Dashboard-Editor](/help/mobile-dashboard-editing).
- Mit **Wasserwerte protokollieren** trägst du Testkit-Ergebnisse von Hand ein.
- **Tagebuch · Warnungen · Wartung · Besatz** führen direkt zu diesen Bereichen für dieses Becken.

Eine Zeile darüber zeigt, wann das Dashboard zuletzt aktualisiert wurde und aus welchen Quellen die Daten stammen.

## Weitertippen

Tippe auf ein Widget, um die Details zu öffnen. Dort siehst du die ganze Historie als Diagramm, jede Quelle, die den Wert gemeldet hat, und die aktuell geltenden Schwellenwerte. Von hier aus kannst du einen neuen Messwert von Hand eintragen, den Bereich ändern oder weiter zurückschauen.

## Wenn ein Widget keinen Wert zeigt

Ein Widget zeigt einen Wert, sobald es einen bekommt. Bleibt es leer, liegt es meist an einem dieser Gründe:

- Das Gerät ist offline. Schau im Tab **Geräte** nach.
- Der Wasserwert hat noch keine Quelle. Trag ihn von Hand ein oder verbinde ein Gerät, das ihn meldet.
- Der Wasserwert wurde noch nie gemeldet oder eingetragen. Es gibt dazu also noch keine Daten.

Ein alter Messwert verschwindet nicht, nur weil das Diagrammfenster kürzer ist als sein Alter. Er bleibt mit seinem Alter auf dem Widget stehen. Ein veralteter Wert sieht also veraltet aus und nicht so, als würde er fehlen.

Bei allem anderen hilft dir die **[Problembehebung](/help/troubleshooting)**.

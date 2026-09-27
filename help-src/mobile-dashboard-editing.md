---
title: Editing your dashboard
description: Set the column count, add and arrange widgets, resize tiles, and save layouts to reuse on other tanks.
section: Cora Mobile
reviewed: 2026-09-09
order: 6
group: Your dashboard
---

The dashboard editor sets which widgets appear on a tank's dashboard and how they're arranged.

## Opening the editor

Scroll to the bottom of the dashboard and tap **Edit dashboard**.

:::note The pencil next to the tank name opens something else
It opens **Edit tank**, the tank profile with volume, livestock, dosing and equipment. That's covered in [Your tank profile](/help/mobile-tank-profile).
:::

![The dashboard editor](img/mobile-edit.webp "Each tile shows its name and type. Tap a red cross to remove it.")

## Setting the column count

Pick **2**, **3** or **4** columns at the top of the editor. The grid grows downward as you add widgets, and the dashboard scrolls.

| Columns | Use when |
|---|---|
| 2 | You watch a few parameters and want big tiles |
| 3 | The default. Works for most tanks |
| 4 | You want a dense view, or you have a big phone |

## Adding a widget

1. Tap **+** in the editor.
2. Pick what the widget shows: a parameter, a device or an outlet.
3. Pick the widget type. The [Widget reference](/help/mobile-widgets) describes each one.

You only see sources the tank has. A parameter with no source shows up once you connect equipment that reports it, or log a reading by hand.

## Arranging widgets

- To move a widget, press and hold it, then drag. The others move around it.
- To remove a widget, tap the red cross in its corner.
- To change a widget's settings, tap it.

## Resizing

A widget takes up one or two columns and one or two rows. Set the size in the widget's settings.

A **trend** widget is always at least two columns wide.

## Widget settings

Depending on the widget type, you can set:

| Setting | Applies to |
|---|---|
| Label | All types |
| Source | Any parameter reported by more than one thing |
| Time window | Trend: 1 hour, 6 hours, 24 hours, 7 days, 30 days, 1 year |
| Range | Gauge. Taken from the tank's thresholds unless you change it here |
| Size | All types |

## Saving

Tap **Save** to keep the layout, or the close icon to throw away your changes.

## My dashboards

You can save a layout you like and use it again. Tap **My dashboards → Save this design** and give it a name. You can keep up to **30**.

You can load a saved design onto another tank or onto a Cora Max screen.

:::note You see which tiles won't fit before you load
Loading a design keeps only the tiles the target can fill. The rest are dropped and listed under **Left behind** before you confirm, each with its reason. The tank may never have reported that metric, there may be no outlet with that name, the ReefBeat device or Apex module may not be linked to this tank, or the grid may have run out of room.
:::

## Restoring a previous layout

A saved design is how you get back to a layout you liked. Save one while the dashboard looks the way you want, and you can apply it again later.

This restores a saved layout. It isn't an undo. You pick the design from the list and confirm, and it replaces the current layout, dropping any tile the tank can't fill. You get the layout you saved, not whatever was there before your last edit.

Readings, history and journal entries are stored apart from the layout, so editing a dashboard can never lose them.

## Editing the Cora Max dashboard

You edit the Cora Max dashboard separately, from **Devices → your Cora Max → Edit Dashboard**. It uses a fixed grid that doesn't scroll. See [Editing the Cora Max dashboard](/help/max-dashboard-editing).

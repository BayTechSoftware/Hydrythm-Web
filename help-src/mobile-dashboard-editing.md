---
title: Editing your dashboard
description: Set the column count, add and arrange widgets, resize tiles, and save layouts you can reuse across tanks.
section: Cora Mobile
order: 5
---

The dashboard editor controls which widgets appear on a tank's dashboard and how they are arranged.

## Opening the editor

Scroll to the bottom of the dashboard and tap **Edit dashboard**.

:::note The pencil beside the tank name is a different screen
That opens **Edit tank** — the tank profile, covering volume, livestock, dosing and equipment. See [Your tank profile](/help/mobile-tank-profile).
:::

![The dashboard editor](img/mobile-edit.webp "Each tile shows its name and type. Tap a red cross to remove it.")

## Setting the column count

Choose **2**, **3** or **4** columns at the top of the editor. The grid grows downward as you add widgets, and the dashboard scrolls.

| Columns | Use when |
|---|---|
| 2 | You watch a small number of parameters and want large tiles |
| 3 | Default. Suitable for most tanks |
| 4 | You want a dense view, or you use a large phone |

## Adding a widget

1. Tap **+** in the editor.
2. Choose what the widget shows — a parameter, a device, or an outlet.
3. Choose the widget type. See [Widget reference](/help/mobile-widgets).

Only sources that exist on the tank are offered. A parameter with no source appears once you connect equipment that reports it or log a reading by hand.

## Arranging widgets

- **To move a widget**, press and hold it, then drag. The remaining widgets reflow around it.
- **To remove a widget**, tap the red cross in its corner.
- **To change a widget's settings**, tap it.

## Resizing

A widget occupies one or two columns and one or two rows. Set the size in the widget's settings.

A **trend** widget is always at least two columns wide.

## Widget settings

Depending on the widget type, you can set:

| Setting | Applies to |
|---|---|
| Label | All types |
| Source | Any parameter reported by more than one thing |
| Time window | Trend — 1 hour, 6 hours, 24 hours, 7 days, 30 days, 1 year |
| Range | Gauge — inherited from the tank's thresholds unless overridden here |
| Size | All types |

## Saving

Tap **Save** to apply the layout, or the close icon to discard your changes.

## My dashboards

A layout you like can be saved and reused. **My dashboards → Save this design**, then name it. You can keep up to **30**.

A saved design can be loaded onto another tank, or onto a Cora Max screen.

:::note What a tank cannot fill is left behind, not left empty
Loading a design keeps only the tiles the target can actually populate. Anything else is dropped and listed for you under **Left behind** before you commit, each with its reason — the tank has never reported that metric, there is no outlet with that name, the ReefBeat device or Apex module is not linked to this tank, or the grid ran out of room.
:::

## Recovering a layout you did not mean to change

There is no reset-to-default for a dashboard. The way back is a saved design — which is the argument for saving one while the layout is how you want it, because that is what turns a bad edit into one tap to undo.

Readings, history and journal entries are stored separately from layout, so no edit to a dashboard can lose them.

## Editing the Cora Max dashboard

The Cora Max dashboard is edited separately: **Devices → your Cora Max → Edit Dashboard**. It uses a fixed grid rather than a scrolling one. See [Editing the Cora Max dashboard](/help/max-dashboard-editing).

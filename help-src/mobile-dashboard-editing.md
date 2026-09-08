---
title: Editing your dashboard
description: Choose a layout, add and arrange widgets, resize tiles, and save dashboards you can reuse across tanks.
section: Cora Mobile
order: 4
---

Your dashboard starts with a sensible default. It gets genuinely useful once you make it yours — the parameters you actually watch, in the order you actually think about them.

Open the editor with the **pencil** in the tank header.

![The dashboard editor](img/mobile-edit.webp "Edit mode: drag to move, tap to configure, and the widget catalog along the bottom.")

## The grid

The phone dashboard is **two to four columns wide** and scrolls downward for as long as you need. Set the column count at the top of the editor.

- **Two columns** — big, readable tiles. Good if you watch a handful of parameters.
- **Three columns** — the default, and the right answer for most tanks.
- **Four columns** — dense. Good on a large phone, or when you want everything on one screen.

Rows are not fixed. Add widgets and the grid grows; the dashboard simply scrolls.

## Adding a widget

Tap **+** where you want it, or pick from the catalog at the bottom of the editor. You are asked two things:

1. **What to show** — a parameter (alkalinity, temperature, nitrate…), a device, or an outlet.
2. **How to show it** — see the shapes below.

A widget only offers sources you actually have. If nothing in your system reports phosphate, phosphate is not in the list until you log it by hand or connect something that does.

## The widget shapes

| Shape | Best for | What it shows |
|---|---|---|
| **Value** | Anything you just want the number for | Current reading, unit, age and source |
| **Gauge** | Parameters with a target range | An arc with your range banded onto it, and a knob at the current value |
| **Trend** | Anything that drifts | A sparkline over a window you choose, with high and low marked |
| **Status** | Things that are a state, not a number | Current state as text — running, idle, closed |
| **Control** | Outlets you switch | A three-way control: Auto, Off, On |
| **Device** | Equipment with several readings | One tile for the whole unit, with its own summary |

Full detail on each: **[Widget reference](/help/mobile-widgets)**.

## Moving and resizing

**Press and hold** a widget, then drag it. Everything else reflows around it.

**Tap** a widget in edit mode to open its settings — including its size. A widget can be one or two cells wide and one or two cells tall; a **trend** is always at least two cells wide, because a sparkline in a single cell shows nothing useful. A gauge you care about at two-by-two reads across the room; a number you glance at can sit at one-by-one.

:::tip Put the drifty things at the top
You scroll past the bottom of a dashboard. Alkalinity, pH and temperature usually deserve the first row; the things that never move can live further down.
:::

## Configuring a widget

Tap any widget in edit mode. Depending on its shape you can set:

- **Time window** for trends — one hour, six hours, twenty-four hours, seven days, thirty days, or one year
- **Range** for gauges — inherited from your tank targets, or overridden just for this tile
- **Label** — rename it to whatever you call it
- **Source** — when more than one thing reports the same parameter, choose which one this tile trusts

## Saving a layout you like

Once a dashboard works, save it: **Presets**, then **Save current as preset**. Give it a name.

A saved preset can be applied to another tank, restored after you have experimented, or used as the starting point for a new tank. This is the fastest way to set up a second tank — build one good dashboard, save it, apply it.

:::note Presets carry shapes, not readings
Applying a preset to another tank gives you the same widgets in the same places, pointed at *that* tank's data. Widgets whose source does not exist on the new tank are left empty rather than dropped, so you can see what is missing.
:::

## Editing the Cora Max dashboard from your phone

Cora Max has its own dashboard, and you can build it here rather than typing on the wall. In **Devices**, open your Cora Max and choose **Edit dashboard**.

The big screen works differently from a phone: instead of scrolling, it uses a **fixed grid** you pick up front, from 2×2 up to 10×5. Everything has to fit on one screen, because nobody scrolls a wall display.

| Grid | Tiles | Feels like |
|---|---|---|
| 2×2, 3×2, 3×3 | 4–9 | Large, readable from across the room |
| 4×4, 5×3, 6×4 | 16–24 | The usual choice for a full system |
| 6×5, 8×4, 8×5 | 30–40 | Dense — a whole reef room at once |
| 9×5, 10×5 | 45–50 | Very dense; best on the largest screens |
| **Fill** | automatic | Cora picks a shape to fit however many widgets you added |

A Cora Max dashboard holds up to **32 widgets**. If you add more than the grid can show, the extras are kept but not painted — reduce the count or pick a denser grid.

:::warning Pick the grid before you build
Changing grid shape after you have arranged everything re-flows the whole layout. Choose roughly the density you want first, then fill it.
:::

## Starting over

**Presets → Reset to default** rebuilds the dashboard from your tank profile. Nothing is lost: readings, history and journal entries are separate from layout.

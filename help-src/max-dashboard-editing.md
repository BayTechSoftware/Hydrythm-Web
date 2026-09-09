---
title: Editing the Cora Max dashboard
description: Choose a grid, add widgets, and save layouts for the Cora Max display.
section: Cora Max
reviewed: 2026-09-09
order: 4
group: Your dashboard
---

The Cora Max dashboard uses a **fixed grid**. Every tile must fit on one screen; the display does not scroll. That is the main difference from the phone dashboard.

Open the editor from **Settings → Tank settings → [your tank] → Dashboard layout**.

![The dashboard editor on Cora Max](img/max-dashboard-editor.webp "Grid sizes across the top, then the tiles. Each shows its type and source, not a reading — this is a layout screen. Nothing is written until you press Save.")

:::tip You can also edit it from your phone
**Devices → your Cora Max → Edit Dashboard** builds the same layout from Cora Mobile. It is quicker than arranging tiles by hand on a wall, and the result appears on the screen straight away.
:::

## Choosing a grid

Pick the density first, because changing it re-flows everything.

| Grid | Tiles | Feels like |
|---|---|---|
| 2×2, 3×2, 3×3 | 4–9 | Large. Readable from right across the room. |
| 4×4, 5×3, 6×4 | 16–24 | The usual choice for a full system. |
| 6×5, 8×4, 8×5 | 30–40 | Dense — a whole reef room at once. |
| 9×5, 10×5 | 45–50 | Very dense. Best on the largest screens. |
| **Auto** | up to 32 | Cora picks a shape to fit however many tiles you added. |

A fixed grid holds as many tiles as it has cells — up to 50 on 10×5. **Auto** is the one option with its own ceiling: it stops at 32 tiles, because beyond that the text becomes too small to read at a distance.

:::note Start with Auto if you are unsure
Add the tiles you want and leave the grid on **Auto**; Cora chooses a shape that fits them. If you like the result, pin it to that fixed shape afterwards.
:::

:::warning Changing grid can drop tiles — but only when there is no room
Tiles are re-flowed into the new shape rather than discarded by position: anything already in a legal cell stays put, and the rest are packed back in, in order. Tiles are only lost when the new grid has **fewer cells than you have tiles**, and Cora tells you how many went. Moving from 10×5 (50 cells) to 3×3 (9) will lose most of them.
:::

## Adding and arranging

The editor tells you the three gestures along the top: **tap a tile to edit**, **long-press to move it**, and **✕ to remove it**. Tiles can be one or two cells wide and one or two cells tall.

**Outlets & Feed** adds your controllable outlets and feed cycles in one step, rather than one tile at a time. **Clear all** empties the grid so you can start again.

The nine tile types — Value, Gauge, Graph, Status, Outlet, ReefBeat, Apex module, Jecod and Maxspect *(coming soon)* — are described in the **[Widget reference](/help/mobile-widgets)**.

## Designing for distance

A wall display is read from further away than a phone, and usually at a glance rather than with attention.

- **Give your headline parameters two-by-two.** Alkalinity, temperature, pH — the things you want to read without walking over.
- **Put controls at the edges.** Outlet tiles are the ones you reach for; they are easier to hit at the sides.
- **Group by subject, not by type.** Everything about dosing together, everything about flow together. You scan a wall by area.
- **Leave the traces small.** Trace elements and other slow numbers are reference, not monitoring — a one-by-one value tile is plenty.

## Saving layouts

Nothing you do in the editor takes effect until you press **Save**. Leaving without saving discards the changes.

**My dashboards** keeps layouts you want to come back to, so you can switch between them instead of rebuilding. A dense everyday layout and a big-tile layout for when you are working in the tank suit different moments, and switching between them takes one tap.

## Multiple tanks

Each tank has its own layout. Edit them separately, one tank at a time, from that tank's own settings.

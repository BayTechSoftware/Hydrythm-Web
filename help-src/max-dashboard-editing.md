---
title: Editing the Cora Max dashboard
description: Choose a grid, add widgets and save layouts for the Cora Max display.
section: Cora Max
reviewed: 2026-09-30
order: 4
group: Your dashboard
---

The Cora Max dashboard uses a **fixed grid**. The display doesn't scroll, so every tile has to fit on one screen. That's the main difference from the phone dashboard.

Open the editor from the **tank menu** (tap the tank name in the top bar, then **Dashboard layout**). You'll also find it under **Settings → Tank settings → [your tank] → Dashboard layout**.

![The dashboard editor on Cora Max](img/max-dashboard-editor.webp "Grid sizes across the top, then the tiles. This is a layout screen, so each tile shows its type and source instead of a reading. Nothing is saved until you press Save.")

:::tip You can also edit it from your phone
In Cora Mobile, go to **Devices → your Cora Max → Edit Dashboard** to build the same layout. It's quicker than arranging tiles by hand on a wall screen, and the result shows up on Cora Max right away.
:::

## Choosing a grid

Pick the grid size first. Changing it later moves all the tiles around.

| Grid | Tiles | Feels like |
|---|---|---|
| 2×2, 3×2, 3×3 | 4–9 | Large. Easy to read from across the room. |
| 4×4, 5×3, 6×4 | 16–24 | The usual choice for a full system. |
| 6×5, 8×4, 8×5 | 30–40 | Dense. A whole reef room on one screen. |
| 9×5, 10×5 | 45–50 | Very dense. Best on the largest screens. |
| **Auto** | up to 32 | Cora picks a shape that fits however many tiles you've added. |

A fixed grid holds as many tiles as it has cells, up to 50 on 10×5. **Auto** has its own limit of 32 tiles. Past that, the text gets too small to read from a distance.

:::note Not sure? Start with Auto
Add the tiles you want and leave the grid on **Auto**. Cora picks a shape that fits them. If you like it, you can switch to that fixed shape afterwards.
:::

:::warning Changing the grid only drops tiles when they don't fit
When you change the grid, Cora doesn't throw tiles away by position. Tiles that still have a valid cell stay where they are, and the rest are packed back in, in order. You only lose tiles when the new grid has **fewer cells than you have tiles**, and Cora tells you how many went. Going from 10×5 (50 cells) to 3×3 (9) loses most of them.
:::

## Adding and arranging

The three gestures are listed along the top of the editor: **tap a tile to edit**, **long-press to move it**, and **✕ to remove it**. A tile can be one or two cells wide and one or two cells tall.

**Outlets & Feed** adds all your controllable outlets and feed cycles in one go. **Clear all** empties the grid so you can start over.

The eleven tile types are Value, Gauge, Graph, Status, Outlet, ReefBeat, Apex module, Jecod, Maxspect *(beta)*, GHL *(beta)* and HYDROS *(beta)*. You'll find them all in the [Widget reference](/help/mobile-widgets).

## Designing for distance

People read a wall display from further away than a phone, and usually with a quick glance.

- Make your key parameters two by two. Alkalinity, temperature and pH are things you'll want to read without walking over.
- Put controls at the edges. Outlet tiles are the ones you reach for, and they're easier to hit at the sides.
- Group tiles by subject. Keep everything about dosing together and everything about flow together, because you scan a wall by area.
- Keep trace elements small. They and other slow-moving numbers are for reference, so a one-by-one value tile is plenty.

## Saving layouts

Nothing you do in the editor takes effect until you press **Save**. If you leave without saving, your changes are lost.

**My dashboards** keeps layouts you want to come back to, so you can switch instead of rebuilding. For example, you might want a dense everyday layout and a big-tile one for when you're working in the tank. Switching takes one tap.

## Multiple tanks

Each tank has its own layout. Edit each one from that tank's own settings.

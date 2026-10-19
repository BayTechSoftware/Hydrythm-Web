---
title: Editing the Cora Max dashboard
description: Add, move and remove tiles on the Cora Max dashboard, pick a grid, use templates or Design with AI, and save layouts to reuse on any Cora Max.
section: Cora Max
reviewed: 2026-10-18
order: 4
group: Your dashboard
twin: mobile-dashboard-editing
---

This page shows how to arrange the tiles on a Cora Max dashboard. It uses a **fixed grid**: the display doesn't scroll, so every tile has to fit on one screen. That's the main difference from the phone dashboard.

Open the editor from the **tank menu**: tap the tank name in the top bar, then **Dashboard layout**. It's also under **Settings → [your tank] → Dashboard layout**.

![The dashboard editor on Cora Max](img/max-dashboard-editor.webp "Grid sizes across the top, then the tiles. This is a layout screen, so each tile shows its type and source instead of a reading. Nothing is saved until you press Save.")

:::tip You can also edit it from your phone
In Cora Mobile, open the **Devices** tab, tap your Cora Max, then tap **Dashboard layout** on the tank's card. It's quicker than arranging tiles by hand on a wall screen, and the result shows up on Cora Max as soon as you save.
:::

## Choosing a grid {#choosing-a-grid}

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

## Adding and arranging tiles {#adding-and-arranging}

1. Tap an empty cell (it shows a **+**) to open **Add widget**.
2. Under **TYPE**, pick the kind of tile, then what it shows (a reading, an outlet, a device or a scene).
3. Under **SIZE**, pick how big it is. A tile can be one or two cells wide and one or two cells tall. A Graph also has a **TIME RANGE**. A doser tile has **Show remaining as**, in **Days** or **Milliliters (mL)**.
4. Tap **Add**.

The gestures are listed along the top of the editor: **tap a tile to edit**, **long-press to move it**, and **✕ to remove it**. **Clear all** empties the grid so you can start over.

The tile types are Value, Gauge, Graph, Status, Outlet, Scene, ReefBeat, Apex module and Jecod. **Light**, **Wavemaker** and **Pump** list every light, wavemaker or pump on the tank, whatever the brand, and each appears only when the tank has one. You'll find the tiles in the [Widget reference](/help/mobile-widgets). The **Scene** tile only exists on Cora Max. It runs a [scene](/help/max-automation) with one tap.


## Outlets & Feed {#outlets-feed}

**Outlets & Feed** in the editor chooses which outlets and feed cycles appear in **Controls**, the drawer you swipe up from the bottom of the dashboard. It doesn't add tiles. If you pick none, Controls lists all of them. To put an outlet on the grid itself, add an **Outlet** tile. More in [Outlets and controls](/help/max-controls).

When you remove a device from a tank, its tiles leave the dashboard by themselves, on your phone and on every Cora Max of that tank. A tile whose device has gone says **This device is no longer on this tank** and opens nothing.

## Templates {#templates}

**Templates** sits at the top of the editor, beside **My dashboards** and **Design with AI**. It's open on every plan and never uses AI, so it also works without AI data sharing.

It opens **Dashboard templates**, a few ready-made layouts built from what this tank reports and has linked:

- **Overview**: few, large tiles, with the core parameters as gauges and your main devices
- **Equipment**: one tile per device first, then outlets and the core parameters
- **Parameters**: charts and readings first, with devices and outlets last

Each one shows a preview and how many tiles it has on which grid. Tap **Use this**. Cora asks **Replace your dashboard?** first. Tap **Save current as preset first** if you want to keep the layout you have, or **Replace**. Nothing is saved until you press **Save**.

## Design with AI {#design-with-ai}

The editor has a **Design with AI** button. It works on a paid plan and during the trial. Cora proposes a whole layout from what this tank reports and has linked, and shows how many tiles it has and on which grid. Tap **Use this** to put it in the editor, or **Try again** for another. You can make 5 designs per tank per day.

An AI design replaces what's on this dashboard now. Nothing is saved until you press **Save**, and you can keep your current layout first by saving it to **My dashboards**. On the free plan, **Design with AI** points you to the plans. It also needs AI data sharing turned on in Cora Mobile. More in [Asking Cora](/help/mobile-assistant).

## Designing for distance {#designing-for-distance}

People read a wall display from further away than a phone, and usually with a quick glance.

- Make your key parameters two by two. Alkalinity, temperature and pH are things you'll want to read without walking over.
- Put controls at the edges. Outlet tiles are the ones you reach for, and they're easier to hit at the sides.
- Group tiles by subject. Keep everything about dosing together and everything about flow together, because you scan a wall by area.
- Keep trace elements small. They and other slow-moving numbers are for reference, so a one-by-one value tile is plenty.

## Saving and reusing layouts {#saving-layouts}

Nothing you do in the editor takes effect until you press **Save**. If you leave with unsaved changes, Cora asks **Discard changes?** first.

**My dashboards** keeps designs you want to come back to. They're saved on your account, not on this screen, so any Cora Max on your account can load them, for another tank or for a replacement screen.

- **Save this design** stores what's in the editor. You can keep up to 30.
- **Load** puts a saved design in the editor. Designs saved from your phone are marked **Phone**.
- Before loading, Cora tells you how many tiles will come across. Anything that can't, such as a reading this tank doesn't report or a device that isn't on this tank, is listed under **Left behind:** with the reason.

For example, you might keep a dense everyday layout and a big-tile one for when you're working in the tank.

## Multiple tanks {#multiple-tanks}

Each tank has its own layout. Switch to that tank and open **Dashboard layout** from its tank menu, or use **Settings → [that tank] → Dashboard layout**.

---
title: Editing your dashboard
description: Add, move, resize and remove widgets on your phone dashboard, set the column count, and edit a Cora Max dashboard from your phone.
section: Cora Mobile
reviewed: 2026-10-13
order: 8
group: Your dashboard
twin: max-dashboard-editing
---

The dashboard editor sets which widgets appear on a tank's dashboard and how they're arranged. Each tank has its own layout, and it follows your account to any phone you sign in on.

## Opening the editor {#opening-the-editor}

Scroll down the dashboard and tap **Edit dashboard**, just under the widgets. The editor opens as **Edit Dashboard**, with the hint **Long-press a tile to move it. Tap to configure.**

:::note The pencil in the tank header opens something else
It opens **Edit tank**, the tank profile with volume, livestock, dosing, lighting and flow. That's covered in [Your tank profile](/help/mobile-tank-profile).
:::

![The Edit Dashboard screen in Cora Mobile](img/mobile-edit.webp "Columns at the top, then each tile with its name and type. Tap a red cross to remove it.")

## Setting the column count {#setting-the-column-count}

Pick **2**, **3** or **4** next to **COLUMNS** at the top of the editor. The grid grows downward as you add widgets, and the dashboard scrolls.

| Columns | Use when |
|---|---|
| 2 | You watch a few parameters and want big tiles |
| 3 | The default. Works for most tanks |
| 4 | You want a dense view, or you have a big phone |

## Adding a widget {#adding-a-widget}

1. Tap **Add tile** under the grid, or tap an empty cell.
2. In **Add a tile**, pick what kind it is. **Metric** covers a value, gauge, graph or status for a parameter. **Outlet** controls an Apex outlet. The other rows are for equipment, such as **ReefBeat**, **Trident**, **DŌS** or **Jecod**. Most of them only appear when the tank has that equipment.
3. Pick the parameter, outlet or device.
4. For a metric, pick the type. The [Widget reference](/help/mobile-widgets) describes each one.

You only see parameters the tank has. A parameter with no source shows up once you connect equipment that reports it, or log a reading by hand.

The grid holds up to 20 rows. When it's full, Cora says **Dashboard is full: remove a tile first.** A graph needs two free cells side by side.

## Arranging widgets {#arranging-widgets}

- To move a widget, press and hold it, then drag. The others move around it.
- To remove a widget, tap the red cross in its corner, or tap the widget and then **Remove**.
- To change a widget's settings, tap it.

## Widget settings {#widget-settings}

Tap a widget in the editor to open its settings. Depending on the widget, you can set:

| Setting | Applies to |
|---|---|
| **Type** | Metric widgets: Value, Gauge, Graph or Status |
| **Parameter** | Metric widgets: which parameter it shows |
| The outlet or device | Outlet and equipment tiles: which one it shows |
| **Show remaining as** | Doser tiles: **Days** or **Milliliters (mL)** |
| **Width** | Every widget: **1×** or **2×**. A graph is always at least 2 wide |
| **Height** | Every widget: **1×** or **2×** |
| **Time range** | Graph: 1h, 6h, 24h, 7d, 30d or 1y |

Tap **Done** to keep the settings, or **Remove** to take the widget off.

A widget has no label, source or range of its own. Its alert range comes from the tank's alert thresholds: long-press the widget on the dashboard, or see [Alerts and thresholds](/help/mobile-alerts). Which source a parameter follows is set per tank in [Parameter Mapping](/help/mobile-probes).

## Saving {#saving}

Tap **Save** to keep the layout. To throw your changes away, tap the close icon. If you changed anything, Cora asks **Discard changes?** Tap **Discard**, or **Keep editing** to go back.

The phone editor has no undo and no saved designs. Readings, history and journal entries are stored apart from the layout, so editing a dashboard can never lose them.

## Editing the Cora Max dashboard {#editing-the-cora-max-dashboard}

You edit the Cora Max dashboard separately, from **Devices →** your Cora Max **→ Dashboard layout**, on the tank's card. It uses a fixed grid that doesn't scroll, and nothing reaches Cora Max until you tap **Save & Publish**.

That editor has three extras the phone dashboard doesn't:

- **My dashboards** keeps up to 30 saved designs on your account. Any Cora Max on the account can load one. Tiles the target can't fill are listed under **Left behind:** before you load.
- **Templates** opens **Dashboard templates**: **Overview**, **Equipment** and **Parameters**. It's open on every plan and doesn't use AI.
- **Design with AI**, on a paid plan or during the trial, proposes a whole layout from what the tank reports and has linked. You can make 5 designs per tank per day.

How each one works is in [Editing the Cora Max dashboard](/help/max-dashboard-editing).

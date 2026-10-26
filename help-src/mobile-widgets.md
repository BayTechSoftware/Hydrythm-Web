---
title: Widget reference
description: Every widget type on the Cora Mobile dashboard, from value, gauge, graph, status and outlet to the device tiles, and when to use each one.
section: Cora Mobile
reviewed: 2026-10-18
order: 9
group: Your dashboard
---

A widget is one tile on your dashboard, and it shows one thing. This page goes through each type and what you can set on it.

You add and arrange widgets in [the dashboard editor](/help/mobile-dashboard-editing). Tap a widget there to open its settings: **Type** and **Parameter** for a metric, the outlet or device for the others, then **Width** and **Height**, and **Time range** for a graph.

![A widget's settings sheet in Cora Mobile](img/mobile-widget-config.webp "The lower half of a widget's settings: the parameter, width, height and time range, then Remove and Done.")

## The widget types {#the-widget-types}

| Type | Shows |
|---|---|
| **Value** | The current reading, its unit, age and source |
| **Gauge** | An arc with your range banded onto it and a knob at the value |
| **Graph** | A trend over a time range you choose |
| **Status** | The reading as plain text with a coloured dot |
| **Outlet** | A three-way control: Auto, Off, On |
| **ReefBeat** | One Red Sea unit, with its own summary |
| **Apex module** | One fitted Apex module, such as a Trident or DŌS |
| **Jecod** | One Jecod pump, with its mode and intensity |

Everything after Outlet is a **device** tile. Each one belongs to a piece of equipment instead of a parameter, and shows whatever that unit reports. Cora Max also has a **Scene** tile, which you add on Cora Max. See [Editing the Cora Max dashboard](/help/max-dashboard-editing).


## Sizing {#sizing}

**Width** and **Height** can each be **1×** or **2×**, so a widget is one or two cells wide and one or two cells tall. A graph is never one cell wide. On a three-column dashboard, a two-wide gauge takes up two thirds of the row. That's usually a good shape for your most important parameter.

## What a parameter widget shows {#what-a-parameter-widget-shows}

Value, Gauge, Graph and Status widgets all show a measured parameter, and they always show three things. Outlet and device tiles show their own state, since there's no single reading behind them.

- **The value**, in large type
- **The age** (`now`, `1h`, `2d`), which is how long ago the source last confirmed the value. For a probe, that's when its device last checked in, so a steady reading stays fresh. For a test-kit or ICP result, it's when you took the test. More in [Reading your dashboard](/help/mobile-dashboard#how-to-read-a-parameter-widget).
- **The source**, a small badge that says where the number came from

A parameter widget has no range or source setting of its own. The range comes from the tank's alert thresholds (long-press the widget on the dashboard), and the source from [Parameter Mapping](/help/mobile-probes). Tap the widget on the dashboard to see its full history, every source that reports it and your alert band.

## Value {#value}

This is the plain number. It shows the current reading, its unit, how old it is and where it came from.

Use it for parameters you check by the number more than by the trend, like calcium, magnesium or nitrate.

## Gauge {#gauge}

A gauge is an arc with your alert range marked on it, and a knob at the current value. The knob's colour tells you where you are: inside the range, drifting or out.

Use it for the parameters you actively manage, like alkalinity, pH, salinity or temperature.

:::note Make gauges at least two columns wide
At one column the arc is too small to read quickly. If you're short on space, use a **Value** widget.
:::

## Graph {#graph}

A graph is a sparkline over a time range you choose: 1h, 6h, 24h, 7d, 30d or 1y. It marks the high and low and labels the current value.

For a parameter you test (with a Trident or a test kit), the line joins up your real tests. If there's only one test in the window, the line comes in from the test before it, and there's no high or low. If there's no test in the window, or nothing earlier to join a single test to, the tile shows **Collecting…** in place of a line.

Use it for anything that moves, like pH through the day, temperature in a heatwave or alkalinity between doses.

A graph is always **at least two cells wide**. A sparkline squeezed into one cell tells you nothing, so the editor won't let you make one.

:::note Pick the range that fits the parameter
pH swings on a daily cycle, so 24 hours shows you the pattern. Alkalinity moves over days, so 7 or 30 days tells you much more.
:::

## Status {#status}

This shows the reading as plain text, with a coloured dot for in range, drifting or out. Use it for a parameter that has no useful gauge range.

## Outlet {#outlet}

This is a three-way switch for an Apex outlet: **Auto**, **Off** and **On**. You pick which outlet it controls.

- **Auto** gives the outlet back to whatever normally runs it. That might be a schedule, a rule or the controller it belongs to.
- **Off** and **On** are manual overrides. They stay until you change them back.

:::warning Manual overrides don't wear off
Off means off until you set it back to Auto. If you switch a return pump off to work in the tank, put it back to Auto when you're done. Cora won't do it for you.
:::

## ReefBeat {#reefbeat}

This is one tile for a whole piece of equipment. It shows the unit's own summary instead of a single parameter, for example an ATO's status and reservoir, a doser's heads or how many days a mat roller has left. You pick which device it shows.

Which devices can have a tile depends on what you've connected. See [Connecting your equipment](/help/mobile-connections).

## Doser tiles {#doser-tiles}

A tile for a doser (an Apex DŌS or a ReefDose) shows one row per head. A head name is never shrunk below a readable size. On a tall tile the row takes two lines, with the name on the first and what's left on the second, for example *40d* and *2.8 L*. On a short tile the detail line is dropped and the name stays readable.

Set what comes first with **Show remaining as**: **Days** or **Milliliters (mL)**. A ReefDose head with no name of its own is shown as the device name followed by "head" and its number. A Jecod doser tile is read only and shows the daily plan, because Jecod doesn't report how much is left in the bottle.

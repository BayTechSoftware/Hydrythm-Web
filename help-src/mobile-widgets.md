---
title: Widget reference
description: Every widget type in Cora, from value, gauge, graph, status and outlet to the device tiles, and when to use each one.
section: Cora Mobile
reviewed: 2026-09-17
order: 7
group: Your dashboard
---

A widget is one tile on your dashboard, and it shows one thing. This page goes through each type and what you can set on it.

You add and arrange widgets in [the dashboard editor](/help/mobile-dashboard-editing). Tap a widget there to open its settings.

![Configuring a widget](img/mobile-widget-config.webp "Type, parameter, then width and height.")

## The nine types

| Type | Shows |
|---|---|
| **Value** | The current reading, its unit, age and source |
| **Gauge** | An arc with your range banded onto it and a knob at the value |
| **Graph** | A trend over a window you choose |
| **Status** | A state as text: running, idle, closed |
| **Outlet** | A three-way control: Auto, Off, On |
| **ReefBeat** | One Red Sea unit, with its own summary |
| **Apex module** | One fitted Apex module, such as a Trident or DŌS |
| **Jecod** | One Jecod pump, with its mode and intensity |
| **Maxspect** *(beta)* | One gyre, with both motors |

The last four are **device** tiles. Each one belongs to a piece of equipment instead of a parameter, and shows whatever that unit reports.

## Sizing

**Width** and **Height** can each be **1×** or **2×**. A graph is never one cell wide.

## Value

This is the plain number. It shows the current reading, its unit, how old it is and where it came from.

Use it for parameters you check by the number more than by the trend, like calcium, magnesium or nitrate.

You can set its label, source and size.

## Gauge

A gauge is an arc with your target range marked on it, and a knob at the current value. The knob's colour tells you where you are: inside the range, drifting or out.

Use it for the parameters you actively manage, like alkalinity, pH, salinity or temperature.

You can set its label, source, range and size. The range comes from your tank targets unless you change it here.

:::note Make gauges at least two columns wide
At one column the arc is too small to read quickly. If you're short on space, use a **value** widget.
:::

## Graph

A graph is a sparkline over a time window you choose. It marks the high and low and labels the current value.

For a parameter you test (with a Trident or a test kit), the line joins up your real tests. If there's only one test in the window, the line comes in from the test before it, and there's no high or low. If there's no test in the window, or nothing earlier to join a single test to, the tile shows **Collecting…** in place of a line.

Use it for anything that moves, like pH through the day, temperature in a heatwave or alkalinity between doses.

You can set its label, source, **time window** (1 hour, 6 hours, 24 hours, 7 days, 30 days, 1 year) and size.

A trend is always **at least two cells wide**. A sparkline squeezed into one cell tells you nothing, so the editor won't let you make one.

:::note Pick the window that fits the parameter
pH swings on a daily cycle, so 24 hours shows you the pattern. Alkalinity moves over days, so 7 or 30 days tells you much more.
:::

## Status

This shows text in place of a number, for things that have a state. Running, idle, open, closed, feeding.

You can set its label, source and size.

## Outlet

This is a three-way switch for an outlet: **Auto**, **Off** and **On**.

- **Auto** gives the outlet back to whatever normally runs it. That might be a schedule, a rule or the controller it belongs to.
- **Off** and **On** are manual overrides. They stay until you change them back.

You can set its label, which outlet it controls, and its size.

:::warning Manual overrides don't wear off
Off means off until you set it back to Auto. If you switch a return pump off to work in the tank, put it back to Auto when you're done. Cora won't do it for you.
:::

## ReefBeat

This is one tile for a whole piece of equipment. It shows the unit's own summary instead of a single parameter, for example an ATO's status and reservoir, a doser's heads or how many days a mat roller has left.

Which devices can have a tile depends on what you've connected. See [Connecting your equipment](/help/mobile-connections).

You can set its label, which device it shows, and its size.

## What a parameter widget shows

Value, Gauge, Graph and Status widgets all show a measured parameter, and they always show three things. Outlet and device tiles show their own state, since there's no single reading behind them.

- **The value**, in large type
- **The age** (`now`, `1h`, `2d`), which is how old the reading is. It isn't how long ago the screen refreshed.
- **The source**, a small badge that says where the number came from

Tap any widget to see its full history, every source that reports it and the thresholds that apply.

## Sizes

Widgets are one or two cells wide and one or two cells tall. The exception is a **trend**, which is always at least two wide. On a three-column dashboard, a two-wide gauge takes up two thirds of the row. That's usually a good shape for your most important parameter.

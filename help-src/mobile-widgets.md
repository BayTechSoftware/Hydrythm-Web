---
title: Widget reference
description: Every widget type in Cora (value, gauge, graph, status, outlet and the device tiles) and when to use each.
section: Cora Mobile
reviewed: 2026-09-09
order: 7
group: Your dashboard
---

A widget is one tile on your dashboard showing one thing. This page covers each type and what you can configure.

Add and arrange them in **[the dashboard editor](/help/mobile-dashboard-editing)**; tap a widget there to open its settings.

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
| **Maxspect** *(coming soon)* | One gyre, with both motors |

The last four are **device** tiles: they are keyed to a piece of equipment rather than to a parameter, and each shows whatever that unit reports.

## Sizing

**Width** and **Height** are each **1×** or **2×**. A graph is never one cell wide.

## Value

The plain number. Current reading, its unit, how old it is and where it came from.

Use it for parameters you check numerically rather than by trend: calcium, magnesium, nitrate.

**Settings:** label, source, size.

## Gauge

An arc with your target range banded onto it and a knob at the current value. The knob's colour tells you where you stand: inside the band, drifting, or out.

Use it for the parameters you actively manage: alkalinity, pH, salinity, temperature.

**Settings:** label, source, range (inherited from your tank targets unless you override it here), size.

:::note Size gauges at two columns or more
At a single column the arc is too small to read at a glance; use a **value** widget instead if space is limited.
:::

## Graph

A sparkline over a window you choose, with the high and low marked and the current value called out.

Use it for anything that moves: pH through the day, temperature across a heatwave, alkalinity between doses.

**Settings:** label, source, **time window** (1 hour, 6 hours, 24 hours, 7 days, 30 days, 1 year), size.

A trend is always **at least two cells wide**; a sparkline squeezed into one cell tells you nothing, so the editor will not make one.

:::note Choose the window to match the rhythm
pH swings on a daily cycle, so 24 hours shows you the shape. Alkalinity moves over days, so 7 or 30 tells you more than 24 ever will.
:::

## Status

Text rather than a number, for things that are a state. Running, idle, open, closed, feeding.

**Settings:** label, source, size.

## Outlet

A three-way switch for an outlet: **Auto**, **Off**, **On**.

- **Auto** hands the outlet back to whatever normally runs it: a schedule, a rule, or the controller it belongs to.
- **Off** and **On** are manual overrides that stay until you change them back.

**Settings:** label, which outlet, size.

:::warning A manual override does not expire
Off means off until you set it back to Auto. If you switch a return pump off to work in the tank, put it back to Auto when you have finished; Cora will not do it for you.
:::

## ReefBeat

One tile for a whole piece of equipment, showing its own summary rather than a single parameter: an ATO's status and reservoir, a dosing unit's heads, a mat roller's remaining days.

Which devices offer a tile depends on what you have connected. See **[Connecting your equipment](/help/mobile-connections)**.

**Settings:** label, which device, size.

## What a parameter widget shows

On a widget backed by a measured parameter (Value, Gauge, Graph and Status), three things are always present. Outlet and device tiles show their own state instead, because no single reading sits behind them:

- **The value**, large
- **The age** (`now`, `1h`, `2d`): how old the reading is, not how recently the screen refreshed
- **The source**: a small badge saying where the number came from

Tap any widget to open its full history, every source that reports it, and the thresholds in force.

## Sizes

Widgets are one or two cells wide and one or two cells tall, except a **trend**, which is always at least two wide. On a three-column dashboard a two-wide gauge takes two thirds of the row, which is usually the right shape for your most important parameter.

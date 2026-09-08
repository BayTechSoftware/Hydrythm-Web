---
title: Widget reference
description: Every widget shape in Cora — value, gauge, trend, status, control and device tiles — and when to use each.
section: Cora Mobile
order: 6
---

A widget is one tile on your dashboard showing one thing. There are six shapes. This page covers what each is for and what you can configure.

Add and arrange them in **[the dashboard editor](/help/mobile-dashboard-editing)**.

## Value

The plain number. Current reading, its unit, how old it is and where it came from.

Use it for parameters you check numerically rather than by trend — calcium, magnesium, nitrate.

**Settings:** label, source, size.

## Gauge

An arc with your target range banded onto it and a knob at the current value. The knob's colour tells you where you stand: inside the band, drifting, or out.

Use it for the parameters you actively manage — alkalinity, pH, salinity, temperature.

**Settings:** label, source, range (inherited from your tank targets unless you override it here), size.

:::note Size gauges at two columns or more
At a single column the arc is too small to read at a glance; use a **value** widget instead if space is limited.
:::

## Trend

A sparkline over a window you choose, with the high and low marked and the current value called out.

Use it for anything that moves — pH through the day, temperature across a heatwave, alkalinity between doses.

**Settings:** label, source, **time window** (1 hour, 6 hours, 24 hours, 7 days, 30 days, 1 year), size.

A trend is always **at least two cells wide** — a sparkline squeezed into one cell tells you nothing, so the editor will not make one.

:::note Choose the window to match the rhythm
pH swings on a daily cycle, so 24 hours shows you the shape. Alkalinity moves over days, so 7 or 30 tells you more than 24 ever will.
:::

## Status

Text rather than a number — for things that are a state. Running, idle, open, closed, feeding.

**Settings:** label, source, size.

## Control

A three-way switch for an outlet: **Auto**, **Off**, **On**.

- **Auto** hands the outlet back to whatever normally runs it — a schedule, a rule, or the controller it belongs to.
- **Off** and **On** are manual overrides that stay until you change them back.

**Settings:** label, which outlet, size.

:::warning A manual override does not expire
Off means off until you set it back to Auto. If you switch a return pump off to work in the tank, put it back to Auto when you're done — Cora will not do it for you.
:::

## Device

One tile for a whole piece of equipment, showing its own summary rather than a single parameter — an ATO's status and reservoir, a dosing unit's heads, a mat roller's remaining days.

Which devices offer a tile depends on what you have connected. See **[Connecting your gear](/help/mobile-connections)**.

**Settings:** label, which device, size.

## What every widget shows

Whatever the shape, three things are always present:

- **The value**, large
- **The age** — `now`, `1h`, `2d` — how old the reading is, not how recently the screen refreshed
- **The source** — a small badge saying where the number came from

Tap any widget to open its full history, every source that reports it, and the thresholds in force.

## Sizes

Widgets are one or two cells wide and one or two cells tall — except a **trend**, which is always at least two wide. On a three-column dashboard a two-wide gauge takes two thirds of the row, which is usually the right shape for your most important parameter.

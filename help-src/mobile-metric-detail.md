---
title: Looking into a parameter
description: Tap a widget to see a parameter's full history, compare sources and parameters, exclude a bad reading and record probe care.
section: Cora Mobile
reviewed: 2026-10-13
order: 7
group: Your dashboard
---

A widget shows you a number. Tap it to see the story behind that number.

There are two ways in. Tap a widget on the dashboard, or tap **Parameter History** in the row of buttons under the widgets and choose a parameter. **Parameter History** lists every parameter that has data, even one with no widget on the dashboard.

## What you get {#what-you-get}

![Looking into a parameter](img/mobile-metric-detail.webp "The dropdowns along the top, then the chart with your alert band shaded.")

- A history chart. The row above it sets what it shows. **Parameter** switches to any other parameter that has data, and keeps your timeframe. **Timeframe** goes from 1h through 6h, 12h, 24h, 3d, 7d, 15d, 30d, 90d, 180d and 360d to All. **Source** starts on **All sources** and lists the sources that report this parameter on this tank, such as *Apex*, *Cora*, *Red Sea* or *Manual*. Pick one to see only its readings.
- **Compare**, at the end of the same row, draws a second parameter on the chart, like alkalinity with calcium or pH with temperature. The button then reads **vs** and the other parameter's name. Tap it again to take the second line off.
- A row with **Latest**, **Min**, **Avg** and **Max** for the time window on screen.
- Icons in the top bar: **Readings** opens the raw readings list, and **Record probe care** logs a calibration or cleaning. For alkalinity, calcium and magnesium there's also the dose calculator, which uses the tank volume from your [tank profile](/help/mobile-tank-profile) and the strengths from [Dosing](/help/mobile-dosing).

The screen always opens on 24h and **All sources**. It doesn't remember what you picked last time.

## Reading the chart {#reading-the-chart}

- The green band is your alert range, so you see each reading against it. To change the range, long-press the widget on the dashboard. More in [Alerts and thresholds](/help/mobile-alerts).
- A dashed line marks a logged dose, so you can line up a change with what you dosed.
- **30d high** and **30d low** are dashed lines showing the last 30 days' extremes.
- A hollow dot is a reading you excluded.
- With **Compare** on, the second parameter uses the right-hand axis.

## Choosing a timeframe {#choosing-a-range}

Pick the timeframe that fits how the parameter moves.

| Parameter | Useful window |
|---|---|
| pH | 24 hours, since it swings on a daily cycle |
| Temperature | 24 hours or 7 days |
| Alkalinity | 7 or 30 days |
| Trace elements | 30 days or a year |

:::note Flat line? Check how old the reading is
A line that hasn't moved can mean the parameter is stable. It can also mean the source stopped reporting. The age next to the value on the widget tells you which.
:::

## Comparing sources {#comparing-sources}

When more than one source reports a parameter, Cora keeps them separate and doesn't average them. Use the **Source** dropdown to look at each one. It's the quickest way to compare a probe with a test kit.

Which one shows on the dashboard is the newest. A live value is only replaced by a reading with a later measurement time, from any source. An older reading goes into history and doesn't overwrite what's on the widget. If you pinned a source in **Parameter Mapping**, Cora follows that source instead.

If a probe and your hand-logged tests stay apart by the same amount, the probe usually needs calibrating.

An [ICP result](/help/mobile-icp-health) is a useful third opinion, but it doesn't settle the question. Labs differ from each other, and how the sample was handled, stored and shipped all change the result. Treat one ICP as evidence. Two tests that agree are worth far more than one.

## Choosing which source a reading follows {#choosing-which-source-a-widget-trusts}

The source is set per tank and per parameter, not per widget. Go to **Settings**, tap the tank, tap **Parameter Mapping**, then the **Sources** tab. Pick a probe, or **Automatic (newest reading wins)**. The choice applies to that parameter everywhere for the tank. More in [Parameter Mapping](/help/mobile-probes).

## Excluding a bad reading {#excluding-a-bad-reading}

Maybe a probe spiked, you misread a test, or you took the sample in the middle of a water change. One wrong reading throws off the chart, the averages and anything worked out from them.

![The pH readings list in Cora Mobile](img/mobile-readings.webp "Every reading behind the line, with its time and source. Tap one to exclude it.")

Tap **Readings** in the top bar, then tap a reading. Cora asks **Exclude this reading?** and explains that it stays in your log but stops counting toward averages, trends, insights and the assistant. Tap **Exclude**. Nothing is deleted, and you can bring it back the same way.

Readings older than 90 days can't be excluded or brought back.

:::warning Exclude wrong readings, not unwelcome ones
Only exclude a reading you know is invalid. If you just don't like a reading but can't find anything wrong with it, it's real data. Removing it makes every later comparison less honest.
:::

## Recording probe care {#recording-probe-care}

Tap **Record probe care** (the sensor icon in the top bar) and pick what you did: calibrate, clean, replace, move or compare. Cora puts the date on that source, so a fresh calibration isn't mistaken for drift. Later, if the probe disagrees with something, you can see when it was last looked after. More in [Parameter Mapping](/help/mobile-probes).

## Logging a reading by hand {#logging-a-reading-by-hand}

You log readings from the dashboard, not from this screen. Tap **Log Parameters** under the widgets and enter what your test kit says. The list is grouped, and the **Trace** group covers iodine, iron and copper in µg/L, and potassium in mg/L. Hand-logged readings count as much as any other. They get their own source and time, show on the chart and feed Reef Buddy. They're also what Cora checks your equipment against.

:::note Cora double-checks odd-looking entries
If a value is far from where the tank has been, Cora asks you to confirm it before saving. This catches a decimal point in the wrong place, or a reading entered under the wrong parameter. Once you confirm, the reading is saved as usual.
:::

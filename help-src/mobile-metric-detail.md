---
title: Looking into a parameter
description: Tap any widget to see its full history, every source that reports it, and where to change its range.
section: Cora Mobile
reviewed: 2026-10-12
order: 8
group: Your dashboard
---

A widget shows you a number. Tap it to see the story behind that number.

There are two ways in. Tap a widget on the dashboard, or tap **Parameter History** in the row of buttons under the widgets and choose a parameter. **Parameter History** lists every parameter that has data, even one with no widget on the dashboard.

## What you get

![Looking into a parameter](img/mobile-metric-detail.webp "The dropdowns along the top, then the chart with your alert band shaded.")

- A history chart. Three dropdowns above it set what it shows. **Parameter** switches to any other parameter that has data, and keeps your timeframe. **Timeframe** goes from 1h through 6h, 12h, 24h, 3d, 7d, 15d, 30d, 90d, 180d and 360d to All. **Source** starts on **All sources** and lists the sources that report this parameter on this tank, such as *Apex*, *Cora*, *Red Sea* or *Manual*. Pick one to see only its readings. It's the quickest way to compare a probe with a test kit. Just switch between them on the same chart.
- The screen always opens on 24h and **All sources**. It doesn't remember what you picked last time.
- A row with **Latest**, **Min**, **Avg** and **Max** for the time window on screen.
- A link to the dose calculator, for parameters you dose. It uses the tank volume from your [tank profile](/help/mobile-tank-profile) and the strengths from [Dosing](/help/mobile-dosing).
- **Compare**, which draws a second parameter on the same chart, like alkalinity with calcium or pH with temperature. The list has every parameter the tank has. If you suspect two things move together, you can see it here. Tap the chip again to take the second line off.
- Dose markers on the chart, so you can line up a change with what you dosed.
- The raw readings list, with every reading behind the line and its source and time.
- Your alert band, shaded on the chart, so you see each reading against its range. To change the range, long-press the widget on the dashboard. More about that in [Alerts and thresholds](/help/mobile-alerts).
- A way to log a reading by hand.

## Choosing a range

Pick the range that fits how the parameter moves.

| Parameter | Useful window |
|---|---|
| pH | 24 hours, since it swings on a daily cycle |
| Temperature | 24 hours or 7 days |
| Alkalinity | 7 or 30 days |
| Trace elements | 30 days or a year |

:::note Flat line? Check how old the reading is
A line that hasn't moved can mean the parameter is stable. It can also mean the source stopped reporting. The age next to the value tells you which.
:::

## Comparing sources

When more than one source reports a parameter, Cora keeps them separate and doesn't average them. Use the **Source** dropdown to look at each one.

Which one shows on the dashboard is the newest. A live value is only replaced by a reading with a later measurement time, from any source. An older reading goes into history and doesn't overwrite what's on the widget. If you pinned a source for the widget, Cora follows that source instead.

If a probe and your hand-logged tests stay apart by the same amount, the probe usually needs calibrating.

An [ICP result](/help/mobile-icp-health) is a useful third opinion, but it doesn't settle the question. Labs differ from each other, and how the sample was handled, stored and shipped all change the result. Treat one ICP as evidence. Two tests that agree are worth far more than one.

## Choosing which source a widget trusts

If you want a widget to follow one source, set that in the widget's settings. You'll find how in [Editing your dashboard](/help/mobile-dashboard-editing).

## Excluding a bad reading

Maybe a probe spiked, you misread a test, or you took the sample in the middle of a water change. One wrong reading throws off the chart, the averages and anything worked out from them.

![The raw readings list](img/mobile-readings.webp "Every reading behind the line, with its source and time.")

Open the readings list from the icon in the top bar, then tap a reading to exclude it. The screen tells you what happens: *excluded from averages and insights, but it stays in your log.* Nothing is deleted, and you can bring it back.

:::warning Exclude wrong readings, not unwelcome ones
Only exclude a reading you know is invalid. If you just don't like a reading but can't find anything wrong with it, it's real data. Removing it makes every later comparison less honest.
:::

## Recording probe care

When you log a calibration or cleaning here, Cora puts the date on that source. Later, if the probe disagrees with something, you can see when it was last looked after. More in [Probes](/help/mobile-probes).

## Logging a reading by hand

Enter what your test kit says. The list is grouped, and the **Trace** group covers iodine, iron and copper in µg/L, and potassium in mg/L. Hand-logged readings count as much as any other. They get their own source and time, show on the chart and feed Reef Buddy. They're also what Cora checks your equipment against.

:::note Cora double-checks odd-looking entries
If a value is far from where the tank has been, Cora asks you to confirm it before saving. This catches a decimal point in the wrong place, or a reading entered under the wrong parameter. Once you confirm, the reading is saved as usual.
:::

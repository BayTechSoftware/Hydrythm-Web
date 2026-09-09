---
title: Looking into a parameter
description: Tap any widget for full history, every source reporting it, and where to change its range.
section: Cora Mobile
order: 8
---

A widget shows you a number. Tapping it shows you the story behind the number.

## What you get

![Looking into a parameter](img/mobile-metric-detail.webp "Ranges along the top, then the sources reporting this parameter, then the chart with your alert band shaded.")

**A history chart**, with its own range selector: **1h · 6h · 12h · 24h · 3d · 7d** and longer.

**A source filter.** Below the ranges is a row of chips — **All**, plus one per source reporting this parameter, such as *Apex*, *Cora*, *Red Sea* or *Manual*. Select one to see only its readings. This is how you compare a probe against a test kit directly: switch between them on the same chart.

**A dose calculator link**, for parameters you dose. It uses the tank volume from your [tank profile](/help/mobile-tank-profile) and the strengths from [Dosing](/help/mobile-dosing).

**A comparison overlay.** *Compare with* draws a second parameter on the same chart — alkalinity against calcium, pH against temperature — so a relationship you suspect becomes visible instead of remembered.

**Summary statistics** for the window on screen: **MIN**, **AVG** and **MAX**, shown as a row under the current value.

**Dose markers** on the chart, so a movement can be lined up against what you actually dosed.

**The raw readings list** — every individual reading behind the line, with its source and timestamp.

**Your alert band**, shaded on the chart, so a reading is read against its range rather than in isolation. To change the range itself, long-press the widget on the dashboard — see [Alerts and thresholds](/help/mobile-alerts).

**Log a reading** by hand.

## Choosing a range

The right range depends on the rhythm of the parameter:

| Parameter | Useful window |
|---|---|
| pH | 24 hours — it swings on a daily cycle |
| Temperature | 24 hours or 7 days |
| Alkalinity | 7 or 30 days |
| Trace elements | 30 days or a year |

:::note Check the reading age on a flat trend
A line that has not moved may indicate a stable parameter or a source that has stopped reporting. The age shown beside the value distinguishes the two.
:::

## Comparing sources

When more than one source reports a parameter, Cora keeps them separate rather than averaging them. Use the source chips to view each in turn.

A persistent offset between a probe and a hand-logged test usually indicates the probe needs calibrating.

An [ICP result](/help/mobile-icp-health) is a useful third opinion, but not an arbiter. Laboratories differ from one another, and the sample's handling, storage and transit all move the result. Treat a single ICP as evidence, not as the true value — two tests agreeing is worth far more than one.

## Choosing which source a widget trusts

If you want a widget to follow one particular source, set that in the widget's settings — see **[Editing your dashboard](/help/mobile-dashboard-editing)**.

## Excluding a bad reading

A probe that spiked, a test misread, a sample taken mid water-change — a single wrong reading distorts the chart, the averages and anything reasoning from them.

![The raw readings list](img/mobile-readings.webp "Every reading behind the line, with its source and time.")

Open the readings list from the icon in the top bar, then tap a reading to exclude it. The screen says it plainly: *excluded from averages and insights, but it stays in your log.* Nothing is deleted, and it can be restored.

:::warning Exclude a wrong reading, not an unwelcome one
Excluding is for readings you know to be invalid. A reading you dislike but cannot fault is data, and removing it makes every later comparison less honest.
:::

## Recording probe care

Logging a calibration or cleaning from here stamps the date against that source, so a later disagreement can be read against when the probe was last seen to. See [Probes](/help/mobile-probes).

## Logging a reading by hand

Enter what your test kit says. Hand-logged readings are first-class: they get their own source and timestamp, they appear on the chart, they feed Reef Buddy, and they are what Cora compares your equipment against.

:::note Cora checks entries that look implausible
If a value is far from what the tank has been running, you are asked to confirm it before it is saved. This catches a decimal point in the wrong place or a reading entered against the wrong parameter. Confirm it and the reading is stored normally.
:::

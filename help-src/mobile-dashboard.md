---
title: Reading your dashboard
description: How to read Cora's dashboard, from widgets and reading age to sources and what the colours mean.
section: Cora Mobile
reviewed: 2026-09-09
order: 5
group: Your dashboard
---

The dashboard is a grid of **widgets**. Each one shows one thing about one tank. You decide what goes on it, as described in [Editing your dashboard](/help/mobile-dashboard-editing).

![A Cora Mobile dashboard](img/mobile-dashboard.webp "Gauges, numbers, trends and controls on one screen.")

## The tank header

Every dashboard starts with:

- The tank name, with a small glyph next to it. Tap the glyph to rename the tank. That's all it does.
- **Feed** pauses flow and skimming for a feeding, then puts everything back.
- **Reef Buddy** opens this morning's briefing.
- **Share** sends a snapshot of the dashboard.
- The pencil on the right opens [the tank profile](/help/mobile-tank-profile).

:::note Three controls that look alike
The glyph next to the name renames the tank. The pencil on the right opens the tank **profile**. To edit the dashboard itself, tap **Edit dashboard** at the *bottom* of the dashboard, below the widgets.
:::

If you have more than one tank, swipe sideways to move between them.

## The Reef Buddy card

Under the header, a card sums up the latest briefing. It shows a headline, the **Stability** and **Data** scores, and how many insights there are. Tap it to open the full briefing, or close it with **×**. A new card appears with the next briefing.

## How to read a parameter widget

A widget for a **measured parameter** always shows the same three things in the same places. Device and control tiles, like an outlet, a dosing unit or a pump, show their own state instead, since there's no single reading behind them.

The value is the reading itself, large and in the middle.

The age sits below or next to it, as `now`, `1h` or `2d`. It's how long ago the reading was taken, not when the screen last refreshed. A number that hasn't changed in two days shows `2d`, and that tells you something.

The source badge is the small mark next to the age. It shows where the number came from: a probe, a controller, a lab result, or you with a test kit. Tap any widget to see the source written out, with its recent history.

:::note Why the age matters
A perfect alkalinity reading from four days ago isn't your alkalinity today. Every value shows its age so you can see the difference quickly.
:::

## Colours

Cora doesn't use much colour, and each colour always means the same thing:

| Colour | Meaning |
|---|---|
| Green | Comfortably inside the range for this parameter |
| Amber | Near an edge. **Usually still inside the range**, in the last tenth of it |
| Red | Past the edge, and worth acting on |
| Grey | No verdict. There's no recent reading, or no usable range to judge it by |

:::note Amber usually means "fine for now, but drifting"
Amber is a margin. A reading inside its range but in the last 10% of it turns amber, so you see drift while there's still time to act.

There are two refinements.

**A range you set yourself is a hard line.** Cross it and the widget goes straight to red, with no amber margin. A range **Cora supplied** is softer. Crossing it shows amber for the first 10% past the edge, then red beyond that.

**A one-sided limit**, such as a ceiling for a contaminant or a floor for a nutrient, is graded on its high edge only. So copper at zero shows green and doesn't turn amber for sitting near the bottom of the scale.
:::

A widget outlined in amber or red needs attention. The whole widget gets the outline, so you'll spot it while scrolling.

## Below the widgets

![The foot of the dashboard](img/mobile-dashboard-foot.webp "Edit dashboard, Log Parameters, and shortcuts to the four record areas.")

At the bottom of the dashboard you'll find:

- **Edit dashboard**, which opens the [dashboard editor](/help/mobile-dashboard-editing)
- **Log Parameters**, for entering test-kit readings by hand
- **Journal · Alerts · Maintenance · Livestock**, shortcuts to those areas for this tank

A line above them shows when the dashboard last updated and which sources it used.

## Tapping through

Tap any widget to open its detail. You'll see the full history as a chart, every source that has reported it and the thresholds in use. From there you can log a reading by hand, change the range or look further back.

## If a widget has no value

A widget shows a value once it gets one. If it's blank, it's usually one of these:

- The device is offline. Check the **Devices** tab.
- The parameter has no source yet. Log it by hand, or connect equipment that reports it.
- Nothing has ever been reported or logged for the parameter.

An old reading doesn't disappear just because it's older than the chart window. It stays on the widget with its age, so a stale value looks stale and doesn't look missing.

For anything else, see [Troubleshooting](/help/troubleshooting).

---
title: Reading your dashboard
description: How to read Cora's dashboard, from widgets, reading age and sources to what the colours mean and the cards that come and go.
section: Cora Mobile
reviewed: 2026-10-18
order: 6
group: Your dashboard
---

The dashboard is a grid of **widgets** for one tank. Each widget shows one thing. You decide what goes on it, as described in [Editing your dashboard](/help/mobile-dashboard-editing).

![A Cora Mobile dashboard](img/mobile-dashboard.webp "The tank header and the Reef Buddy card, then gauges, values, graphs and device tiles.")

## The tank header {#the-tank-header}

Every dashboard starts with:

- The tank name, with a small glyph next to it. Tap the name to rename the tank. That's all it does.
- **Feed**, only on a tank with a Neptune Apex. It opens **Feed mode** with your Apex's **Feed A** to **Feed D** cycles. Your Apex decides what pauses and when it comes back, as you set it up there. While a cycle runs, the button shows which one, for example **Feed A**. Tap it and choose **Cancel feed** to end it early. Away from home, a Cora Max on the tank sends the command for you.
- The newspaper icon, which opens the latest **Reef Buddy** briefing.
- The share icon, which makes a snapshot of the tank. See [Sharing your tank](/help/mobile-sharing).
- The ruler, which opens **Units** for this tank. See [Your tank profile](/help/mobile-tank-profile#units).
- The pencil on the right, which opens [the tank profile](/help/mobile-tank-profile).

:::note Three controls that look alike
The tank name renames the tank. The pencil on the right opens the tank **profile**. To edit the dashboard itself, tap **Edit dashboard** just under the widgets.
:::

If you have more than one tank, swipe sideways to move between them. See [Managing your tanks](/help/mobile-tanks).

## The Reef Buddy card {#the-reef-buddy-card}

Above the widgets, a card sums up the latest briefing. It shows the headline, a score out of 100 once Cora has enough data, the date it's from, and how many insights and drifting readings there are. Tap it to open the full briefing, or close it with **×**. A new card appears with the next briefing. More in [Reef Buddy](/help/mobile-reef-buddy).

## How to read a parameter widget {#how-to-read-a-parameter-widget}

A widget for a **measured parameter** always shows the same three things in the same places. Device and control tiles, like an outlet, a dosing unit or a pump, show their own state instead, since there's no single reading behind them.

The value is the reading itself, large and in the middle.

The age sits below or next to it, as `now`, `1h` or `2d`. It's how long ago the source last confirmed that value, not when the screen last refreshed. For a probe, that's when its device last checked in, so a steady reading from a working probe stays fresh even when the number doesn't change. For a test-kit or ICP result, it's when you took the test. An age that keeps growing on a probe means its device has stopped reporting.

The source badge is the small mark next to the age. It shows where the number came from: a probe, a controller, a lab result, or you with a test kit. Tap the widget to see the source written out, with its recent history.

:::note Why the age matters
A perfect alkalinity reading from four days ago isn't your alkalinity today. Every value shows its age so you can see the difference quickly.
:::

## Colours {#colours}

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

To change a range, long-press the widget. More in [Alerts and thresholds](/help/mobile-alerts).

## Cards that come and go {#cards-that-come-and-go}

Some cards only show when there's something to say. Most of them sit between the header and the widgets.

| Card | When it shows | What to tap |
|---|---|---|
| **Starting a new tank?** | On a tank with no readings at all. Once you've started, it becomes **Continue cycling** | The card, to start guided cycling. See [Guided journeys](/help/mobile-journeys) |
| **Tank parameters** with *No readings yet* | The tank has no readings yet | **Configure tank** |
| *Couldn't reach your readings: showing what's cached.* | Cora can't load the latest readings, often with no connection | **Retry** |
| **Lab result from {lab} is waiting.** | A lab sent a result and Cora needs to know which tank it's for | **Choose tank**. See [ICP and health reports](/help/mobile-icp-health) |
| Profile prompt (**Unlock smarter insights**) | The tank profile is under 80% complete | The card, to carry on with the profile |
| **Cora Advanced trial: 9 days left** | The last days of your trial | The card, or **Keep Advanced**. See [Plans and subscriptions](/help/mobile-plans) |
| **Reef Buddy** | A briefing is ready | The card |
| **How do you usually feed?** | You haven't set a feeding routine | **Set up routine** |
| *Red Sea readings have stopped updating.* | Nothing is reading this tank's Red Sea devices | See [Alerts and thresholds](/help/mobile-alerts) |
| **Log your first water test** | No readings and no linked equipment, under the widgets | The card. See [Setting up Cora Mobile](/help/mobile-setup#the-first-test-card) |

## Below the widgets {#below-the-widgets}

![The foot of the dashboard in Cora Mobile](img/mobile-dashboard-foot.webp "Edit dashboard, the Log Parameters, Parameter History and Feeding buttons, and shortcuts to the four record areas.")

From top to bottom you'll find:

- A line saying when the dashboard last updated and which sources it used, with **Edit dashboard** beside it. That opens the [dashboard editor](/help/mobile-dashboard-editing).
- The **Log your first water test** card, on a tank with no readings and no linked equipment.
- **Log Parameters**, for entering test-kit readings by hand.
- **Parameter History**, to open the history of any parameter that has data, even one with no widget. See [Looking into a parameter](/help/mobile-metric-detail).
- **Feeding**, to log a feeding that differs from your routine. See [The journal](/help/mobile-journal).
- **Journal · Alerts · Maintenance · Livestock**, shortcuts to those areas for this tank.

## Tapping and long-pressing {#tapping-through}

Tap any parameter widget to open its detail. You'll see the full history as a chart, every source that has reported it and your alert band. From there you can compare sources, exclude a bad reading or record probe care. See [Looking into a parameter](/help/mobile-metric-detail).

**Long-press** a parameter widget to set its alert range straight from the dashboard.

## If a widget has no value {#if-a-widget-has-no-value}

A widget shows a value once it gets one. If it's blank, it's usually one of these:

- The device is offline. Check the **Devices** tab.
- The parameter has no source yet. Log it by hand, or connect equipment that reports it.
- Nothing has ever been reported or logged for the parameter.

An old reading doesn't disappear just because it's older than the chart window. It stays on the widget with its age, so a stale value looks stale and doesn't look missing.

For anything else, see [Troubleshooting](/help/troubleshooting#a-widget-shows-no-value).

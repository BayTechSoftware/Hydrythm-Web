---
title: Reading your dashboard
description: How to read Cora's dashboard — widgets, freshness, sources, and what the colours mean.
section: Cora Mobile
order: 4
---

The dashboard is a grid of **widgets**, each showing one thing about one tank. What is on it is entirely up to you — see **[Editing your dashboard](/help/mobile-dashboard-editing)**.

![A Cora Mobile dashboard](img/mobile-dashboard.webp "Gauges, numbers, trends and controls on one screen.")

## The tank header

At the top of every dashboard:

- **The tank name**, with a pencil that opens [the tank profile](/help/mobile-tank-profile) — not dashboard editing
- **Feed** — pauses flow and skimming for a feeding, then puts everything back
- **Reef Buddy** — opens this morning's briefing
- **Share** — sends a snapshot of the dashboard
- **Edit** — the pencil that opens dashboard editing

With more than one tank, swipe sideways to move between them.

## The Reef Buddy card

Below the header, a card summarises the most recent briefing: a headline, its **Stability** and **Data** scores, and the number of insights. Tap it to open the full briefing, or dismiss it with **×**. A new card appears with the next briefing.

## How to read a widget

Every widget shows the same three things, in the same places.

**The value** is the reading itself, large and central.

**The age** sits below or beside it — `now`, `1h`, `2d`. This is how long ago the reading was taken, not how long ago the screen refreshed. A number that has not moved in two days says `2d`, and that is information.

**The source badge** is the small mark next to the age. It tells you where the number came from: a probe, a controller, a lab result, or you with a test kit. Tap any widget to see the source spelled out along with its recent history.

:::note Why age matters so much
A perfect alkalinity reading from four days ago is not a current alkalinity reading. Most systems hide this and show you the last number they have as though it were live. Cora puts the age next to every value so you always know what you are looking at.
:::

## Colours

Cora uses colour sparingly, and always to mean the same thing:

| Colour | Meaning |
|---|---|
| Green | Inside the range you set for this parameter |
| Amber | Drifting — outside your target but not dangerous |
| Red | Outside the range, and worth acting on |
| Grey | No recent reading, or no range set |

A widget outlined in amber or red is one Cora wants you to look at. The outline is on the widget, not just the number, so you can spot it while scrolling.

## Below the widgets

![The foot of the dashboard](img/mobile-dashboard-foot.webp "Edit dashboard, Log Parameters, and shortcuts to the four record areas.")

At the bottom of the dashboard:

- **Edit dashboard** — opens the [dashboard editor](/help/mobile-dashboard-editing)
- **Log Parameters** — enter test-kit readings by hand
- **Journal · Alerts · Maintenance · Livestock** — shortcuts to those areas for this tank

A line above them shows when the dashboard last updated and which sources it drew on.

## Tapping through

Tap any widget to open its detail: the full history as a chart, every source that has reported it, and the thresholds currently applied. From there you can log a new reading by hand, change the range, or look further back.

## When a number is missing

A widget with no value has not received one. That is usually one of:

- The device is offline — check the **Devices** tab
- The parameter has no source yet — log it by hand, or connect equipment that reports it
- The parameter has never been reported or logged — nothing has been recorded for it yet

An old reading does not vanish because the chart window is shorter than its age. It stays on the widget with its age shown, so a stale value reads as stale rather than as missing.

See **[Troubleshooting](/help/troubleshooting)** if none of those fit.

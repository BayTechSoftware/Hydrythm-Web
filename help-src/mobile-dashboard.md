---
title: Reading your dashboard
description: How to read Cora's dashboard — widgets, freshness, sources, and what the colours mean.
section: Cora Mobile
order: 3
---

The dashboard is a grid of **widgets**, each showing one thing about one tank. What is on it is entirely up to you — see **[Editing your dashboard](/help/mobile-dashboard-editing)**.

![A Cora Mobile dashboard](img/mobile-dashboard.webp "Gauges, numbers, trends and controls on one screen.")

## The tank header

At the top of every dashboard:

- **The tank name**, with a pencil to rename it
- **Feed** — pauses flow and skimming for a feeding, then puts everything back
- **Reef Buddy** — opens this morning's briefing
- **Share** — sends a snapshot of the dashboard
- **Edit** — the pencil that opens dashboard editing

With more than one tank, swipe sideways to move between them.

## The Reef Buddy card

Under the header you will usually find a card summarising this morning's briefing — a headline, a score out of 100, and how many insights are waiting. Tap it to read the whole thing, or dismiss it with the **×** and it comes back tomorrow.

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

## Tapping through

Tap any widget to open its detail: the full history as a chart, every source that has reported it, and the thresholds currently applied. From there you can log a new reading by hand, change the range, or look further back.

## When a number is missing

A widget with no value has not received one. That is usually one of:

- The device is offline — check the **Devices** tab
- The parameter has no source yet — log it by hand, or connect equipment that reports it
- The reading is older than the window the widget is showing — switch it to a longer window in dashboard editing

See **[Troubleshooting](/help/troubleshooting)** if none of those fit.

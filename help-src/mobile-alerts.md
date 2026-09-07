---
title: Alerts and thresholds
description: Set the range for each parameter, choose what you get told about, and understand why an alert fired.
section: Cora Mobile
order: 8
---

An alert is Cora telling you a reading left the range you set for it. You decide the ranges and you decide what reaches your phone.

## Setting a range

Every parameter has a target range. Defaults come from your tank type and age when you set the tank up, which is usually a reasonable place to start.

To change one: tap the widget, then **Thresholds**. Or set them all in one place under **Settings → Tanks → [your tank] → Thresholds**.

You can set:

- **A range** — a low and a high, for things like alkalinity or temperature
- **A ceiling** — a high only, for things where low is fine, like nitrate or phosphate
- **A floor** — a low only

:::tip Your range, not the internet's
The defaults are a starting point, not a verdict. A tank running low-nutrient at 6 dKH is not "wrong" because a chart said 8–9. Set the range you actually run, and Cora will tell you when *you* drift.
:::

## What triggers an alert

An alert fires when a reading crosses a threshold. Cora does not fire on a single stray reading — it wants to see the parameter genuinely outside the range, so a momentary probe glitch does not wake you up.

If a parameter has more than one source and they disagree, Cora says so rather than picking one.

## Where alerts appear

- **The bell**, top right of every screen, holds your history. The number is how many you have not read.
- **Push notifications** reach your phone when you allow them.
- **The widget** turns amber or red on the dashboard.
- **Cora Max** shows the same alerts on the big screen.

## Choosing what reaches you

**Settings → Notifications.** You can control:

- Which parameters can push, and at what severity
- Quiet hours
- Whether the daily Reef Buddy briefing pushes

:::note Cora tries hard not to be noisy
The daily briefing is one push per tank per day, and on a day when nothing needs your attention it usually stays silent rather than telling you everything is fine. If Cora is pushing, something changed.
:::

## Clearing an alert

An alert clears when the reading comes back into range. There is nothing to dismiss — it is a statement about the tank, not a task.

If a reading is wrong rather than the tank being wrong — a probe that needs calibrating, say — fix the source. Widening a threshold to silence a bad probe hides the next real problem too.

## Alerts you don't want at all

If a parameter genuinely doesn't matter for your system, remove its range. With no threshold set, Cora shows the value and stops judging it.

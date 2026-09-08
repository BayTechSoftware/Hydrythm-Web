---
title: Alerts and thresholds
description: Set the range for each parameter, choose what you get told about, and understand why an alert fired.
section: Cora Mobile
order: 10
---

An alert is raised when a reading leaves the range you set for it. You set the ranges, and you control which alerts reach your phone.

Open the **Alert Center** from the shortcut row at the bottom of the dashboard.

![The Alert Center](img/mobile-alerts.webp "Active alerts, each with its severity, what triggered it, and when.")

## The Alert Center

Two tabs:

- **Active** — alerts currently raised, with a count badge
- **Rules** — the thresholds and rate-of-change rules that produce them

Each active alert shows the parameter and tank, the reading that triggered it, a plain explanation, a severity chip, the kind of rule that fired (**Threshold** or **Rate of Change**), and the time it fired.

Two actions on each:

- **View rule** — opens the rule that raised it, so you can adjust the range
- **Explain this alert** — asks the Assistant to interpret it against your tank's history

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

An alert fires when a reading crosses a threshold. Cora checks each reading as it arrives, so a single reading outside your range is enough to raise one.

Once an alert is up it will not keep re-notifying you about the same thing — there is a cooldown before it can fire again. And it **clears itself** the moment a reading comes back inside the range; there is nothing to acknowledge.

You can also set a **rate-of-change** rule, which watches how fast a parameter moves rather than where it currently sits. That is the one to use for things where the speed of a change matters more than the number.

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

:::note Transient readings raise alerts
A single out-of-range reading is sufficient to raise an alert, so a probe that spikes will trigger one. If a source is unreliable, recalibrate it or point the widget at a different source rather than widening the threshold.
:::

If a reading is wrong rather than the tank being wrong — a probe that needs calibrating, say — fix the source. Widening a threshold to silence a bad probe hides the next real problem too.

## Disabling alerts for a parameter

If a parameter genuinely doesn't matter for your system, remove its range. With no threshold set, Cora shows the value and stops judging it.

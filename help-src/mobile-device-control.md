---
title: Controlling your equipment
description: Open a device's own page to see its live state and drive it: outlets, pumps, dosing heads and testers.
section: Cora Mobile
reviewed: 2026-09-09
order: 11
group: Equipment
---

Connected equipment has its own page in Cora, showing live state and offering whatever controls that device supports. Open one from the **Devices** tab.

![A device page](img/mobile-device-detail.webp "Live readings at the top, then the controls that device supports.")

Every device page follows the same shape: identification at the top, a row of live readings, any state the device reports, then its controls. The bell in the title bar sets alert thresholds for that device; see [Consumables](/help/mobile-consumables).

:::warning These controls act on live equipment
There is no preview and no undo. Some controls also ask you to confirm first.
:::

## What happens when you send a command

A command does not always succeed, and Cora tells you which of four things happened rather than assuming:

| Outcome | Means |
|---|---|
| **Confirmed** | The equipment acknowledged the change and reported its new state |
| **Unconfirmed** | The command was sent, but nothing reported back. **This means "we do not know", not "it worked"**; check the device's own state |
| **Refused** | Something declined it: a safety rule, a lock, or the equipment itself |
| **No change** | The equipment was already in the state you asked for |

Every outcome is recorded in [Activity](/help/mobile-activity) with what caused it.

## Neptune Apex

The Apex page lists your probes and outlets.

- **Probes** report into Cora as sources and can be placed on a dashboard.
- **Outlets** switch between **Auto**, **Off** and **On**. Auto returns control to your Apex programming.
- **Fitted modules** (Trident, DŌS and others) each have their own page.

## Trident

Shows the current test state, the remaining reagent and waste-water levels, and lets you start a test.

You can set an alert threshold for remaining tests from this page, so Cora warns you before reagent runs out. See [Consumables](/help/mobile-consumables).

## DŌS

Each dosing head shows what it is dosing, its schedule, what it has dosed today, how much is left in the container and its **runway**: how many days that will last at the current rate.

Per head you can:

- **Pause** and **Resume** its schedule
- **Fill**: tell Cora the container is full again, or set the volume in it
- **Dose now**: a measured manual dose

:::note Schedules are edited in Apex Fusion, not here
Cora shows the schedule and tracks what has been dosed, but does not change it. Editing the schedule, the dose rate or the number of doses is done in the Apex Fusion app. Pausing, filling and dosing by hand are all supported here.
:::

:::note Measure the head before dosing by hand
On Cora Max, **Measure to dose** runs a head for twenty seconds so you can weigh or measure what actually came out. Cora turns that into the head's real rate and uses it for every manual dose afterwards: worth doing once per head, and again after changing tubing.
:::

:::warning A DŌS keeps dosing when its container is empty
The unit has no level sensor and does not stop on its own. Set a refill alert from the head's page so Cora warns you before the container runs dry.
:::

## Red Sea ReefBeat

Each unit has a page appropriate to what it is:

| Unit | Page shows | You can |
|---|---|---|
| **ReefDose** | Each head, its container and what it has dosed | Set refill alerts per head |
| **ReefATO+** | Reservoir level and top-off activity | Set a reservoir alert |
| **ReefMat** | Remaining roll, in days and metres | Advance the roll, set a refill alert |
| **ReefRun** | Return and skimmer pump speed and state | Change speed, switch a pump, adjust skimmer settings |

**ReefRun is a return and skimmer pump controller**, not a wave pump; it stops itself when the skimmer cup fills, and the page tells you when it has.

## Jecod pumps

The pump page shows its current mode and intensity, and lets you change both.

You can also:

- **Copy schedule to…**: put this pump's schedule on another one
- **Save schedule as…** and **Saved schedules…**: keep a schedule and re-apply it later
- **Share this schedule** and **Paste a schedule code…**: move a schedule between systems as a short code

## Maxspect

:::note Maxspect support is coming soon
Maxspect gyres are not yet generally available in Cora. This page describes how they work so it is ready when they arrive; until then, the controls below may not appear for your unit.
:::

The gyre page shows the current mode and intensity for each head, and when the unit last reported.

:::note A gyre must be read before it can be changed
The page shows when it last reported. If the reading is stale, refresh it before changing settings so the change is applied to the unit's actual current state.
:::

## What happens after you change something

Every change is recorded in [Activity](/help/mobile-activity) with the surface that requested it. If a device does not accept a change, the failure is recorded there too.

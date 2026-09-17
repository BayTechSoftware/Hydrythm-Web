---
title: Controlling equipment from Cora Max
description: Device pages on the big screen: probes, outlets, dosing heads, testers and pumps.
section: Cora Max
reviewed: 2026-09-17
order: 6
group: Equipment
---

Cora Max reaches the same equipment as your phone, with a page for each device. Open them from **Settings → Devices**, or by tapping a device tile on the dashboard.

![An Apex page on Cora Max](img/max-device-control.webp "Feed cycles and every outlet, laid out for a wall screen.")

:::warning These controls act on live equipment
There is no preview and no undo. A command goes out the moment you tap, but *sent* is not *done*: it comes back **Confirmed**, **Unconfirmed**, **Refused** or **No change**, and [Activity](/help/max-activity) is where you see which it was.
:::

## What has a page

| Device | Shows |
|---|---|
| **Neptune Apex** | Probes and outlets, with each outlet switchable |
| **Trident** | Test state, reagent and waste levels, and the ability to start a test |
| **DŌS**, including the DŌS QD | Each head's dosing, schedule, runway and container volume (with pause, fill, dose now and a one-time twenty-second measure) |
| **Red Sea ReefBeat** | Whatever the unit is: dosing heads, reservoir, roller days, pump mode |
| **Jecod** | Pump mode and intensity, and its day program |
| **Maxspect** *(beta)* | Mode and speed for **Gyre A** and **Gyre B**, **Pump health** (cleaning countdown, head A current, fitted heads, firmware), and its schedule, view only |

If a Red Sea unit stops itself, its page says what is wrong and puts the fix beside it: **Resume**, **Clear emergency**, **Sensor cleaned**, **I already loaded a new roll**, or **Reset** for a dosing head.

## DŌS heads

A DŌS head has to be measured once before Cora will dose it by hand. **Measure to dose** runs the head for twenty seconds into a measuring container, and you enter how much came out. Cora keeps one measurement per head and uses the newest, whichever Cora Max took it; the head's page shows where and when it was measured.

After a manual dose, a head you had set to Off in Apex Fusion stays Off. Any other head goes back to Auto.

## Schedules

Jecod pump day programs can be authored at the wall as well as on the phone. The editor is the same: a day graph, a period list, and an action row. See [Scheduling equipment](/help/mobile-schedules).

A Maxspect gyre's schedule *(beta)* can be viewed here but not saved. Set it in the Maxspect app.

## Outlets

Outlets are also reachable from the **Outlets & Feed** drawer at the bottom of the dashboard, which lists the outlets enabled for this dashboard in one place (all of them, if none have been chosen). See [Outlets and controls](/help/max-controls).

DŌS heads never appear in the outlet list, so a head cannot be switched on there and left running; dose from its own page. A large Apex with several modules shows all of its outlets and probes.

## Consumables

Refill thresholds (reagent, containers, reservoirs) are set from the device's own page here, exactly as on the phone. See [Consumables](/help/mobile-consumables).

## Logging and calculating at the tank

Two things are often more convenient at the wall than on a phone:

- **Log parameters**: enter test results on the on-screen keyboard, from the tank menu
- **Dose calculator**: work out a correction using the tank's volume and your product strengths, from a parameter's page. It uses the same volume and product strengths as the phone, so a dose worked out here matches one worked out there. See [Dosing](/help/mobile-dosing).

## On a second Cora Max

When more than one Cora Max shows a tank, one of them reads that tank's equipment; the device pages call it the Cora Max at the tank. The others still open the device pages (a status pill reading **Cloud** means this screen is one of them). They show what the Cora Max at the tank last read, and how long ago, and pass each command through Cora Cloud to that Cora Max to carry out.

A few things stay with the Cora Max at the tank:

- **Measure to dose** and **Re-measure** appear only there. Once a head is measured, **Dose now** works from any Cora Max.
- A Jecod schedule can be changed from another Cora Max only if the Cora Max at the tank has read the pump in the last hour, and never for a pump that only talks over Bluetooth. One **Apply to the pump** from there sends at most 12 changes, so send a bigger edit in parts.

## What was changed, and by what

Every action is recorded with its cause. See [Activity and timeline](/help/mobile-activity).

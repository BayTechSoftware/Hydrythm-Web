---
title: Scheduling equipment
description: Build a day program for pumps and gyres, and copy it between units.
section: Cora Mobile
order: 11
---

Pumps and gyres can run a **day program** — a set of periods, each with its own intensity, that repeats daily. Cora can author these directly.

Open the device from the **Devices** tab and choose its schedule.

## The schedule editor

Every schedule screen has the same three parts:

**The day graph** — the whole day as a bar, showing where each period sits and how strong it is. This is the fastest way to see whether a program does what you think.

**The period list** — each period with its start time, end time and intensity. Add, edit and remove periods here.

**The action row** — save the program to the device, or discard your changes.

A gyre has two motors, so its graph has **two tracks** — one per motor.

:::warning A schedule is written to the device
Saving sends the program to the equipment, which then runs it on its own clock. It continues running whether or not Cora is reachable.
:::

## Copying a program between pumps

If you run several pumps that should behave alike, build one program and copy it.

Open the pump whose program you want, then **Copy schedule**, and choose the pump to copy it to.

## Grouping pumps

Pumps can be grouped so a change applies to all of them at once, rather than being set one at a time.

## Applying a program

A pump can also be given a prepared program in one step, rather than by building periods by hand.

## Checking it took

After saving, the device page shows the program the unit is actually running. If the two disagree, the write did not land — check the device is reachable and try again.

:::note Read the device before changing a gyre
A gyre's page shows when it last reported. If that reading is stale, refresh it before editing so the schedule is built on the unit's actual current state.
:::

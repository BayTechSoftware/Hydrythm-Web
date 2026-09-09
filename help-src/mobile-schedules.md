---
title: Scheduling equipment
description: Build a day program for pumps and gyres, and copy it between units.
section: Cora Mobile
reviewed: 2026-09-09
order: 12
group: Equipment
---

Pumps and gyres can run a **day program** — a set of periods, each with its own intensity, that repeats daily. Cora can author these directly.

Open the device from the **Devices** tab.

![A pump schedule](img/mobile-schedules.webp "The day graph across 0–24 hours, with each period listed below it.")

## Same all day, or Schedule

A pump runs in one of two modes, chosen at the top of its page:

- **Same all day** — one intensity, constantly
- **Schedule** — a day program with periods

Choosing between them here only changes what you are looking at until the pump is reachable; the change is written when Cora can reach it.

## The schedule editor

Every schedule screen has the same three parts:

**The day graph** — the whole day from 0 to 24 hours, with each period drawn as a block whose height is its intensity. This is the fastest way to see whether a program does what you think.

**The period list** — each period below the graph, with its hours, its mode and its intensity: *Random, 00:00–03:00, Freq 50%, 40%*. Add, edit and remove periods here.

**The action row** — save the program to the device, or discard your changes.

A gyre has two motors, so its graph has **two tracks** — one per motor. *(Maxspect gyre support is coming soon; Jecod pumps are available now.)*

:::warning A schedule is written to the device
Saving sends the program to the equipment, which then runs it on its own clock. It continues running whether or not Cora is reachable.
:::

## Copying a program between pumps

If you run several pumps that should behave alike, build one program and copy it.

Open the pump whose program you want, then **Copy schedule to…**, and choose the pump to copy it to.

## Keeping and sharing a schedule

A schedule you are happy with does not have to be rebuilt:

- **Save schedule as…** keeps it under a name, and **Saved schedules…** applies it again later.
- **Share this schedule** turns it into a short code, and **Paste a schedule code…** applies one someone sent you. This is a Cora Mobile feature — the code carries the schedule, not access to your account.

## Applying a program

A pump can also be given a prepared program in one step, rather than by building periods by hand.

## Checking it took

After saving, the device page shows the program the unit is actually running. If the two disagree, the write did not land — check the device is reachable and try again.

:::note Read the device before changing a gyre
A gyre's page shows when it last reported. If that reading is stale, refresh it before editing so the schedule is built on the unit's actual current state.
:::

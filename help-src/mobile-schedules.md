---
title: Scheduling equipment
description: Build a day program for a Jecod pump and copy it between pumps, and view a Maxspect gyre's schedule (beta).
section: Cora Mobile
reviewed: 2026-09-17
order: 12
group: Equipment
---

Pumps and gyres can run a **day program**: a set of periods, each with its own intensity, that repeats daily. Cora can author these directly for Jecod pumps. A Maxspect gyre's schedule *(beta)* can only be viewed here: set it in the Maxspect app.

Open the device from the **Devices** tab.

![A pump schedule](img/mobile-schedules.webp "The day graph across 0–24 hours, with each period listed below it.")

## Same all day, or Schedule

A pump runs in one of two modes, chosen at the top of its page:

- **Same all day**: one intensity, constantly
- **Schedule**: a day program with periods

Your choice is sent to the pump, through the Cora Max at the tank when your phone is not on the pump's network. A Bluetooth pump has to be in range: until it is, choosing here only changes what you are looking at.

## The schedule editor

Every schedule screen has the same three parts:

**The day graph**: the whole day from 0 to 24 hours, with each period drawn as a block whose height is its intensity. This is the fastest way to see whether a program does what you think.

**The period list**: each period below the graph, with its hours, its mode and its intensity: *Random, 00:00–03:00, Freq 50%, 40%*. Add, edit and remove periods here.

**Adding and changing periods**: **Add to schedule** adds a period. Open a period to change it and tap **Save**, or **Delete** it; you are asked to confirm before it goes.

A Maxspect gyre *(beta)* has two heads, shown as Gyre A and Gyre B, so its day graph has two tracks, one for each, and its plans are listed under **GYRE A** and **GYRE B**. A gyre's schedule is view only: its action row reads **View only**, and the schedule is set in the Maxspect app.

:::warning A schedule is written to the device
Saving sends the program to the equipment, which then runs it on its own clock. It continues running whether or not Cora is reachable.
:::

## Copying a program between pumps

If you run several pumps that should behave alike, build one program and copy it.

Open the pump whose program you want, then **Copy schedule to…**, and choose the pump to copy it to.

## Keeping and sharing a schedule

A schedule you are happy with does not have to be rebuilt:

- **Save schedule as…** keeps it under a name, and **Saved schedules…** applies it again later.
- **Share this schedule** turns it into a short code, and **Paste a schedule code…** applies one someone sent you. This is a Cora Mobile feature; the code carries the schedule, not access to your account.

## Away from the pump's network

When your phone is not on the pump's network, Cora Mobile works through the Cora Max at the tank, with limits:

- **Same all day** and **Schedule** switch the pump through that Cora Max.
- A period you add or change goes through it only if it has reached the pump in the last hour. If it has not, the schedule says so and cannot be changed from where you are.
- **Copy schedule to…**, **Save schedule as…**, **Saved schedules…**, **Share this schedule** and **Paste a schedule code…** need your phone on the pump's network. Until then they are greyed out, and the menu says why.

A Bluetooth pump can only be reached from a phone near it: stand in range to switch it, change its schedule or use any of those items.

## Applying a program

A pump can also be given a prepared program in one step, rather than by building periods by hand.

## Checking it took

After saving, the device page shows the program the unit is actually running. If the two disagree, the write did not land; check the device is reachable and try again.

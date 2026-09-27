---
title: Scheduling equipment
description: Build a day program for a Jecod pump and copy it between pumps, and view a Maxspect gyre's schedule (beta).
section: Cora Mobile
reviewed: 2026-09-17
order: 12
group: Equipment
---

Pumps and gyres can run a **day program**. It's a set of periods, each with its own intensity, that repeats every day. Cora can build these for Jecod pumps. You can view a Maxspect gyre's schedule *(beta)* here, but you set it in the Maxspect app.

Open the device from the **Devices** tab.

![A pump schedule](img/mobile-schedules.webp "The day graph across 0–24 hours, with each period listed below it.")

## Same all day, or Schedule

A pump runs in one of two modes. Pick one at the top of its page.

- **Same all day** runs at one intensity the whole time.
- **Schedule** follows a day program made of periods.

Cora sends your choice to the pump. If your phone isn't on the pump's network, it goes through the Cora Max at the tank. A Bluetooth pump has to be in range. Until it is, your choice only changes what you see on screen.

## The schedule editor

Every schedule screen has the same three parts.

At the top is the day graph. It shows the whole day from 0 to 24 hours, and each period is a block whose height is its intensity. It's the quickest way to check that a program does what you think.

Below the graph is the period list. Each period shows its hours, mode and intensity, for example *Random, 00:00–03:00, Freq 50%, 40%*. You add, edit and remove periods here.

Tap **Add to schedule** to add a period. To change one, open it and tap **Save**. To remove it, tap **Delete** and confirm.

A Maxspect gyre *(beta)* has two heads, shown as Gyre A and Gyre B. Its day graph has a track for each, and its plans are listed under **GYRE A** and **GYRE B**. You can only view a gyre's schedule here. Its action row says **View only**, and you set the schedule in the Maxspect app.

:::warning Saving writes the schedule to the device
When you save, Cora sends the program to the equipment, and the equipment runs it on its own clock. It keeps running whether Cora can reach it or not.
:::

## Copying a program between pumps

If you have several pumps that should behave the same way, build one program and copy it.

Open the pump that has the program you want, tap **Copy schedule to…** and choose the pump to copy it to.

## Keeping and sharing a schedule

Once you have a schedule you like, you don't have to build it again.

- **Save schedule as…** keeps it under a name. **Saved schedules…** applies it again later.
- **Share this schedule** turns it into a short code. **Paste a schedule code…** applies a code someone sent you. This is a Cora Mobile feature. The code only carries the schedule. It gives no one access to your account.

## Away from the pump's network

When your phone isn't on the pump's network, Cora Mobile goes through the Cora Max at the tank. A few things work differently.

- **Same all day** and **Schedule** switch the pump through that Cora Max.
- A period you add or change only goes through if that Cora Max has reached the pump in the last hour. If it hasn't, the schedule tells you, and you can't change it from where you are.
- **Copy schedule to…**, **Save schedule as…**, **Saved schedules…**, **Share this schedule** and **Paste a schedule code…** need your phone on the pump's network. Until it is, they're greyed out and the menu tells you why.

You can only reach a Bluetooth pump from a phone close to it. Stand in range to switch it, change its schedule or use any of those menu items.

## Applying a program

You can give a pump a saved schedule in one step, without building the periods again. Open the pump, tap **More** at the top and choose **Saved schedules…**. The list holds every schedule saved on this tank, including ones you built on another pump. Pick one and tap **Apply**. It replaces the pump's whole day.

## Checking it took

After you save, the device page shows the program the pump is running. If it doesn't match what you saved, the change didn't get through. Check that the device is reachable and try again.

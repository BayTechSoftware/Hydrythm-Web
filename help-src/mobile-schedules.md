---
title: Scheduling equipment
description: Build a daily schedule for a Jecod pump in the editor, copy a program from or to other pumps, save and share it, and check that the pump took it.
section: Cora Mobile
reviewed: 2026-11-03
order: 14
group: Equipment
---

Use this page to give a Jecod pump a **schedule**: a set of periods, each with its own intensity, that repeats every day. Open it from **Devices** → tap the pump.

Lights and pumps from other brands keep their schedules in their own pages: Red Sea's ReefDose in [Controlling your equipment](/help/mobile-device-control#red-sea).

![A Jecod pump page in Cora Mobile with Schedule picked](img/mobile-schedules.webp "Schedule picked at the top, the feeding pause, then the day graph.")

## Manual, or Schedule {#same-all-day-or-schedule}

A pump runs in one of two modes. Pick one with the switch on its page. The one that is running is marked *· running*, and the page opens on it.

- **Manual** runs at one intensity the whole time.
- **Schedule** follows a set of periods.

Cora sends your choice straight to the pump when your phone is on its network. If your phone isn't, it goes through the Cora Max at the tank. A Bluetooth pump has to be in range. Until it is, your choice only changes what you see on screen.

A feeding pause takes the pump off its schedule for a while, and on your phone the schedule comes back only while the pump's page stays open. See [Feeding pause](/help/mobile-device-control#jecod-feeding).

## The schedule editor

Every schedule screen has the same three parts.

At the top is the day graph. It shows the whole day from 0 to 24 hours, and each period is a block whose height is its intensity. It's the quickest way to check that a program does what you think.

Below the graph is the period list. Each period shows its hours, mode and intensity, for example *Random, 00:00–03:00, Freq 50%, 40%*. You add, edit and remove periods here.

Every change to a schedule goes through the editor. **Edit** opens it on the pump's day, and so does tapping a period or **Add to schedule** on the pump's page: the editor opens with that period, or a new one, ready to change. In the editor, change a period and tap **Save**, or remove it with **Delete plan**. **Undo** steps back. The ⋮ menu has **Save schedule as…**, **Saved schedules…** and **Copy from…**.

Nothing is sent to the pump until you tap **Save to pump**. Cora then writes the whole day in one go. If it can't, the editor says why and keeps your changes. If you close the editor before saving, Cora asks *Discard these changes?* first.


:::warning Save to pump writes the schedule to the device
When you tap **Save to pump**, Cora sends the program to the equipment, and the equipment runs it on its own clock. It keeps running whether Cora can reach it or not.
:::

## Copying a program between pumps {#copying-a-program-between-pumps}

If you have several pumps that should behave the same way, build one program and copy it. You can copy in either direction, and nothing is sent until you tap **Save to pump**.

- **Copy from…** (in the schedule's ⋮ menu and the editor's) takes the schedule of another wavemaker on any of your tanks. Each period gets the closest mode this pump has, speeds are kept to what it can run, and **What changes on this pump** lists every change. **Load in editor** puts the copy in this pump's editor, where you can adjust it and then tap **Save to pump**. A pump whose schedule Cora hasn't read yet is greyed out, with the reason.
- **Copy schedule to…** gives this pump's day to other pumps on any of your tanks, each listed as *Tank · Pump*. Tick the pumps and tap **Review**. Nothing is sent yet. **Review copies** lists each pump with its state, **Not saved**, **Saved to pump** or **Failed** with the reason, and how many changes it gets. **Open editor** opens that pump's own editor on the copied day, with its own **Save to pump**, which sends it to that pump only. If a save fails, the draft is kept so you can try again. If you leave while some pumps are not saved, Cora asks *Discard unsaved copies?* first.

## Keeping and sharing a schedule

Once you have a schedule you like, you don't have to build it again.

- **Save schedule as…** keeps it under a name. **Saved schedules…** brings it back later: **Load in editor** opens it in the editor, and **Save to pump** sends it.
- **Share this schedule** turns it into a short code. **Paste a schedule code…** loads a code someone sent you into the editor, and nothing is sent until you tap **Save to pump**. This is a Cora Mobile feature. The code only carries the schedule. It gives no one access to your account.

## Away from the pump's network

When your phone isn't on the pump's network, Cora Mobile goes through the Cora Max at the tank. A few things work differently.

- **Manual** and **Schedule** switch the pump through that Cora Max.
- A schedule you save to the pump only goes through if that Cora Max has reached the pump in the last hour. If it hasn't, the schedule tells you, and you can't change it from where you are.
- **Copy schedule to…**, **Save schedule as…**, **Saved schedules…**, **Share this schedule** and **Paste a schedule code…** need your phone on the pump's network. Until it is, they're greyed out and the menu tells you why.

Without a Cora Max at the tank, you can only change a pump while your phone is on its network. More in [Connecting your equipment](/help/mobile-connections#local-only).

You can only reach a Bluetooth pump from a phone close to it. Stand in range to switch it, change its schedule or use any of those menu items.

## Applying a program

You can give a pump a saved schedule in one step, without building the periods again. Open the pump, tap **More** at the top and choose **Saved schedules…**. The list holds every schedule saved on this tank, including ones you built on another pump. Pick one and tap **Load in editor**. Check it in the editor, then tap **Save to pump**. It replaces the pump's whole day.

## Checking it took

After you save, the device page shows the program the pump is running. If it doesn't match what you saved, the change didn't get through. Check that the device is reachable and try again.

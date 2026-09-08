---
title: Connecting your gear
description: How to connect Neptune Apex, Red Sea ReefBeat, Jecod and AquaWiz equipment to Cora.
section: Cora Mobile
order: 9
---

Cora works with equipment you already own. This page covers what is supported and what each connection needs.

Add any of these from **Devices → Add Device**.

## Neptune Apex

Cora reads your Apex over your local network — probes, outlets and any expansion modules you have fitted.

**You will need:** your Apex's address on your network, and its sign-in.

**What you get:** every probe your Apex reports appears as a source you can put on a dashboard. Outlets appear as controls. Fitted expansion modules get their own device tiles.

:::note Cora does not take your Apex over
Your Apex keeps running its own programming. Cora reads it, shows it alongside everything else, and can switch outlets when you ask — it does not replace what you have set up.
:::

## Red Sea ReefBeat

Cora talks to ReefBeat equipment on your local network — dosing units, ATO, mat rollers, wave pumps and lights, depending on what you own.

**You will need:** the equipment already set up in ReefBeat and on the same network as your phone when you add it.

**What you get:** a device tile per unit, plus each unit's readings as sources. A dosing unit reports its heads; an ATO reports its reservoir; a mat roller reports days remaining.

## Jecod / Jebao

Cora connects to Jecod pumps, and can read and control them. Jecod units reach Cora in one of two ways, and which one yours uses decides what is possible.

**Over your network.** Use **Find a pump on your network** — it finds units that advertise themselves, so no address needs entering. These can be read and driven whenever the pump is powered.

**Over Bluetooth.** Some pumps are reachable only from a phone standing near them. The pump's page says so, and shows the last settings it managed to read along with how old they are.

**What you get:** live state, mode and intensity, feeding pause, and a day program. See [Scheduling equipment](/help/mobile-schedules).

:::warning A Bluetooth pump is only reachable when you are near it
Its page shows the last settings Cora read and how long ago. Changing anything — including starting a feeding pause — needs the pump in range. Stand near it and reopen the page.
:::

## AquaWiz KH Controller

Cora reads alkalinity from an AquaWiz KH controller through your AquaWiz account.

**You will need:** your AquaWiz username and password. Cora signs in on your behalf and keeps the sign-in so it can keep reading.

**What you get:** alkalinity as a source, updated as often as your controller titrates. pH is available as an option if your unit reports it.

:::warning One sign-in, shared
AquaWiz issues a single sign-in per account, so the one Cora holds is the same one their own app uses. Changing your AquaWiz password will disconnect Cora — reconnect it from the device row afterwards. To revoke Cora's access entirely, remove the device in Cora and change your AquaWiz password.
:::

## Maxspect

If you have a Maxspect Gyre, add it the same way — **Devices → Add Device**, then
**Find a pump on your network**. It appears in its own group alongside your other brands.

## Logging by hand

Not every parameter has a device behind it. To enter a test-kit result, scroll to the bottom of the dashboard and tap **Log Parameters**.

Hand-logged readings are first-class: they appear on widgets, carry their own source and age, feed Reef Buddy, and are what Cora compares your probes against when it tells you two sources disagree.

## When a connection stops working

The device row tells you which kind of problem it is. See the table in **[Adding, editing and removing devices](/help/mobile-devices)**, and **[Troubleshooting](/help/troubleshooting)** if it isn't obvious.

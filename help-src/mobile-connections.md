---
title: Connecting your gear
description: How to connect Neptune Apex, Red Sea ReefBeat, Jecod and AquaWiz equipment to Cora.
section: Cora Mobile
order: 9
---

Cora works with equipment you already own. This page covers what is supported and what each connection needs.

⚠️ **There is no single "add anything" button.** Where you start depends on the brand:

| Brand | Start from |
|---|---|
| Neptune Apex | The tank — its profile holds the Apex connection |
| Red Sea ReefBeat | The tank |
| Jecod / Jebao | **Devices → Find a pump on your network**, or Bluetooth |
| AquaWiz | **Devices → Add AquaWiz** |
| Maxspect *(coming soon)* | **Devices → Find a pump on your network** |
| Cora Max | **Devices → Add Device** |

## Neptune Apex

Cora reads your Apex over your local network — probes, outlets and any expansion modules you have fitted.

**You will need:** your Apex's address on your network, and its sign-in.

**What you get:** every probe your Apex reports appears as a source you can put on a dashboard. Outlets appear as controls. Fitted expansion modules get their own device tiles.

:::note Cora does not take your Apex over
Your Apex keeps running its own programming. Cora reads it, shows it alongside everything else, and can switch outlets when you ask — it does not replace what you have set up.
:::

## Red Sea ReefBeat

Cora talks to ReefBeat equipment on your local network. Supported units are **ReefDose**, **ReefATO+**, **ReefMat** and **ReefRun**.

**You will need:** the equipment already set up in ReefBeat and on the same network as your phone when you add it.

**What you get:** a device page per unit, plus each unit's readings as sources. ReefDose reports its heads and containers; ReefATO+ reports its reservoir and fills; ReefMat reports remaining days; ReefRun reports pump state.

## Jecod / Jebao

Cora connects to Jecod pumps, and can read and control them. Jecod units reach Cora in one of two ways, and which one yours uses decides what is possible.

![Finding a pump](img/mobile-connections.webp "The scan explains what it needs and why a pump may not appear on the first sweep.")

**Over your network.** Use **Find a pump on your network** — it finds units that advertise themselves, so no address needs entering. A network pump can be read and driven whenever it is powered **and reachable**: either your phone is on the same network, or a Cora Max on that network relays for you. Away from home with no Cora Max on site, a network-only pump is visible but not controllable.

:::note A pump often misses the first sweep
Pumps answer one scan and miss the next. If yours is not listed, scan again rather than assuming it is unreachable.
:::

**Over Bluetooth.** Some pumps are reachable only from a phone standing near them. The pump's page says so, and shows the last settings it managed to read along with how old they are.

Cora needs Bluetooth permission for this. Without it, a Bluetooth-paired pump cannot be found at all — it will not simply be slower to appear.

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

:::note Maxspect support is coming soon
Maxspect gyres are not yet generally available in Cora. This page describes how they work so it is ready when they arrive; until then, the controls below may not appear for your unit.
:::

Cora connects to Maxspect Gyre pumps and can read and drive them.

**You will need:** the gyre on your network. Use **Devices → Find a pump on your network**.

**What you get:** mode and intensity **for each of its two motors**, the unit's schedule, and its current state with the time it was last read.

:::warning A gyre must be read before it is changed
The page shows when the unit last reported. If that is stale, refresh it before changing anything — otherwise a change is built on a state the pump may have moved away from. See [Scheduling equipment](/help/mobile-schedules).
:::

## Logging by hand

Not every parameter has a device behind it. To enter a test-kit result, scroll to the bottom of the dashboard and tap **Log Parameters**.

Hand-logged readings are first-class: they appear on widgets, carry their own source and age, feed Reef Buddy, and are what Cora compares your probes against when it tells you two sources disagree.

## When a connection stops working

The device row tells you which kind of problem it is. See the table in **[Adding, editing and removing devices](/help/mobile-devices)**, and **[Troubleshooting](/help/troubleshooting)** if it isn't obvious.

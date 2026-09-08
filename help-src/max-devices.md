---
title: Devices and device health
description: What Cora Max can see, how it is polling, and the diagnostics screen.
section: Cora Max
order: 7
---

**Settings → Devices** lists the equipment Cora Max can see and reports how it is doing.

## The device list

![The device list](img/max-devices.webp "Filter by tank, then each device with a one-line summary of what it holds.")

Cora Max sees the same equipment as your phone, because both read the same account.

Filter chips at the top narrow the list to **All tanks** or one tank. Each entry carries a status dot, a one-line summary of what the device holds — *21 outlets · 4 feeds*, *19 tests left* — and the tank it belongs to.

Adding and configuring equipment is easier on the phone — see [Adding, editing and removing devices](/help/mobile-devices).

## Managing a Cora Max from your phone

Open the unit from your phone's **Devices** tab to see its variant, firmware version and when it was last seen, and to change its settings without walking to it.

![Cora Max settings from the phone](img/max-from-phone.webp "Polling interval, brightness, volume, on-screen alerts and dim timer.")

| Setting | Does |
|---|---|
| **Apex Polling** | How often this unit reads the controller |
| **Brightness** | Screen brightness |
| **Volume** | Voice replies and the alert chime |
| **Alerts** | On-screen alert banners. Turning them off does not affect alert history or push notifications |
| **Dim after** | How long before the screen dims |

The tanks this unit shows are listed below those settings.

## Device health

**Settings → Devices → Device health** is the diagnostics screen for the Cora Max unit itself. It reports:

- **Software version and update state**
- **Wake state** — whether this unit is currently the household's voice responder
- **Polling** — for each tank, whether this unit is reading the controller, and whether it is the designated primary
- **Write state** — whether this unit is permitted to send commands to a controller

It also hosts a few controls, so common problems can be fixed at the wall rather than from a laptop:

- Claim or release the voice responder role
- Re-configure a tank's controller connection
- Open the outlets and feed controls

## Why polling state matters

When more than one Cora device could read the same controller, one is designated the primary and the others defer. If readings stop for one tank but continue for another, this screen shows whether this unit believes it should be polling at all.

The primary is chosen per tank from the phone — see [More than one Cora device](/help/mobile-multi-device).

:::note Device health is read-first
Most of the screen reports state rather than changing it. Use it to establish what is happening before altering anything.
:::

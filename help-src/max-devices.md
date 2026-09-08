---
title: Devices and device health
description: What Cora Max can see, how it is polling, and the diagnostics screen.
section: Cora Max
order: 6
---

**Settings → Devices** lists the equipment Cora Max can see and reports how it is doing.

## The device list

Cora Max sees the same equipment as your phone, because both read the same account. Each entry shows its current state and when it last reported.

Adding and configuring equipment is easier on the phone — see [Adding, editing and removing devices](/help/mobile-devices).

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

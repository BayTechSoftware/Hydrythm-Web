---
title: More than one Cora device
description: Choose which device answers voice and which one polls each tank.
section: Cora Mobile
order: 28
---

A household can have several Cora devices — more than one Cora Max, or a Cora Max alongside your phone. Two settings decide which device does what, so they do not duplicate each other's work.

## Voice responder

When several devices can hear you, only one should answer.

**Settings → Assistant & AI → Voice responder** chooses which device responds to the wake word across the whole household.

:::note One responder for the household, not per tank
This is a single choice covering every device on the account. Set it to whichever unit is nearest where you usually stand.
:::

## Primary poller

Equipment on your network is read by a Cora device. When more than one device could read the same controller, they would otherwise poll it in parallel.

The **primary poller** is a per-tank choice of which device reads that tank's controller.

| Setting | Behaviour |
|---|---|
| A named device | Only that device polls the controller. Others defer to it. |
| Any active (automatic) | Whichever device is active reads it. Suitable for a single-device household. |

If the chosen device goes offline or its data goes stale, another device takes over so readings do not stop.

:::note Set a primary when two devices watch one tank
Naming a primary reduces load on the controller and removes duplicate readings from the same source.
:::

## Where each device's state is shown

Cora Max reports its own polling and voice state under **Settings → Devices → Device health**. See [Devices and device health](/help/max-devices).

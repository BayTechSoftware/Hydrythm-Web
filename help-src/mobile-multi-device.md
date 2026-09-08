---
title: More than one Cora device
description: Choose which device answers voice and which one polls each tank.
section: Cora Mobile
order: 28
---

A household can have several Cora devices. Two settings decide which one does what, so they do not duplicate each other's work — and a third thing worth knowing is what is shared between them at all.

## What is shared, and what is not

| Shared across every device | Belongs to one screen |
|---|---|
| Tanks, readings and history | Its dashboard layout |
| Devices and their settings | Wi-Fi, brightness, audio |
| Journal, livestock, maintenance | Wake word and child lock |
| Alerts, thresholds, automations | Which tanks that screen shows |
| Plans and usage | |

Changing a threshold on one device changes it everywhere. Rearranging a dashboard does not — each screen keeps its own layout, and the phone and Cora Max never share one.

## Voice responder

**Settings → Assistant & AI → Voice responder** chooses which **Cora device** answers when you speak to the room. Only one answers, however many can hear you — set it to whichever unit is nearest where you usually stand.

![The voice responder picker](img/mobile-voice-responder.webp "Each device shows what it listens for, and whether it is online.")

Each device in the list shows the wake phrase it listens for, along with whether it is online. **These are not all the same.** A wake phrase is trained into the device itself, so different Cora models can listen for different ones. Read the phrase from the device's own row rather than assuming the household shares one.

:::note Your phone is not in this picker
The phone does not listen for a wake phrase. You start a conversation on it by tapping, which always works and is unaffected by this setting. The picker lists voice-capable Cora hardware only.
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

Cora Max reports its own polling and voice state under **Settings → Cora Max → Firmware → Device health & controls**. See [Devices and device health](/help/max-devices).

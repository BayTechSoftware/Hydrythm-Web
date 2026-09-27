---
title: More than one Cora device
description: Choose which device answers voice and which one polls each tank.
section: Cora Mobile
reviewed: 2026-09-27
order: 29
group: Account
---

A household can have more than one Cora Max. Two settings decide which one does what, so they do not duplicate each other's work, and a third thing worth knowing is what is shared between them at all.

## What is shared, and what is not

| Shared across every device | Belongs to one screen |
|---|---|
| Tanks, readings and history | Its dashboard layout |
| Devices and their settings | Wi-Fi, brightness, audio |
| Journal, livestock, maintenance | Wake word and child lock |
| Alerts, thresholds, automations | Which tanks that screen shows |
| Plans and usage | |

Changing a threshold on one device changes it everywhere. Rearranging a dashboard does not; each screen keeps its own layout, and the phone and Cora Max never share one.

## Cora Assistant: Answering device

**Settings → Cora Assistant → Answering device** chooses which **Cora device** answers when you speak to the room. Only one answers, however many can hear you; set it to whichever unit is nearest where you usually stand.

This is a different choice from Primary Cora Max below: Answering device decides which device answers your voice, and Primary Cora Max decides which device polls a tank's equipment. A household with two tablets may want each set differently.

![The voice responder picker](img/mobile-voice-responder.webp "Each device shows what it listens for, and whether it is online.")

Each device in the list shows the wake phrase it listens for, along with whether it is online. **These are not all the same.** A wake phrase is trained into the device itself, so different Cora models can listen for different ones. Read the phrase from the device's own row rather than assuming the household shares one.

:::note Your phone is not in this picker
The phone does not listen for a wake phrase. You start a conversation on it by tapping, which always works and is unaffected by this setting. The picker lists voice-capable Cora hardware only.
:::

## Primary Cora Max

Equipment on your network is read by a Cora Max. When more than one could read the same controller, they would otherwise poll it in parallel.

**Primary Cora Max** is a per-tank choice of which device reads that tank's controller. In Cora Mobile, open the tank and tap **Primary Cora Max**.

| Setting | Behaviour |
|---|---|
| A named device | It becomes the only Cora device that polls the controller, and it stays the primary even while it is offline: other Cora devices do not take over. Cora Mobile polls only while it is offline. |
| **Any active (automatic)** | The app and any online Cora device share the work (last write wins), so if one goes offline another carries on. Suitable for a single-device household, and the safer default when you are not sure which device should own it. |

While a device you named is offline, a command that has to go through it does not run: Cora tells you the tank is set to use that device, that it is offline, and that nothing ran, so you can try again once it is back. If it will be offline for a while, choose another device or **Any active (automatic)**.

:::note Set a primary when two devices watch one tank
Naming a primary reduces load on the controller and removes duplicate readings from the same source.
:::

:::note This is an account-wide, per-tank setting, not a per-device one
Primary Cora Max belongs to the tank, not to the phone or tablet you are looking at. Changing it from any device changes it for the whole household.
:::

## What works away from home

Your phone does not talk to your equipment directly when you are away from your tank's own Wi-Fi. Instead, a command travels to Cora Cloud, which passes it to a Cora Max sitting at the tank; that Cora Max is the one that actually reaches the equipment.

This means:

- **Readings and history** are always available, wherever you are, because they are already stored in Cora Cloud.
- **Controlling equipment** (switching an outlet, starting a feed, dosing a head, pausing a pump) works away from home too, as long as a Cora Max at the tank is online and can reach that equipment. If none is, the command cannot be delivered.
- **A device's own native settings** (as opposed to its readings) sometimes need a phone on the *same* network as the device itself, not just a Cora Max at the tank. Where that applies, the page says so.

Two messages tell you the command did not simply succeed:

- **"Nothing was sent"**: the command never left your phone, or no Cora Max at the tank could take it. Nothing ran. This is what you will see if the tank's Primary Cora Max is offline and no other device on that tank can step in.
- **"It may already have run"**: the command was sent, but no Cora Max answered in time to confirm it. Cora genuinely does not know whether it ran. Check the equipment's own state before trying again, so you do not send it twice.

If either message keeps appearing, check that a Cora Max at the tank is online, or set **Primary Cora Max** to **Any active (automatic)** so any online device can pick the command up. See [Controlling your equipment](/help/mobile-device-control) for the full outcomes a command can have.

## Where each device's state is shown

Cora Max reports its own polling and voice state under **Settings → Cora Max → Firmware → Device health & controls**. See [Devices and device health](/help/max-devices).

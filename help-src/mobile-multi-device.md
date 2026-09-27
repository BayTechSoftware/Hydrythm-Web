---
title: More than one Cora device
description: Choose which device answers your voice and which one polls each tank.
section: Cora Mobile
reviewed: 2026-09-27
order: 29
group: Account
---

A household can have more than one Cora Max. Two settings decide which one does what, so they don't do the same work twice. It also helps to know what they share.

## What is shared, and what is not

| Shared across every device | Belongs to one screen |
|---|---|
| Tanks, readings and history | Its dashboard layout |
| Devices and their settings | Wi-Fi, brightness, audio |
| Journal, livestock, maintenance | Wake word and child lock |
| Alerts, thresholds, automations | Which tanks that screen shows |
| Plans and usage | |

If you change a threshold on one device, it changes everywhere. Dashboard layouts are different. Each screen keeps its own, and the phone and Cora Max never share one.

## Cora Assistant: Answering device

**Settings → Cora Assistant → Answering device** picks the **Cora device** that answers when you talk to the room. However many devices hear you, only one answers. Set it to the one closest to where you usually stand.

This is separate from Primary Cora Max, further down. Answering device decides who answers your voice. Primary Cora Max decides who polls a tank's equipment. With two Cora Max devices at home, you might set them differently.

![The voice responder picker](img/mobile-voice-responder.webp "Each device shows what it listens for, and whether it is online.")

Each device in the list shows its wake phrase and whether it's online. **The wake phrases aren't always the same.** The phrase is trained into the device, so different Cora models can listen for different ones. Check each device's own row. Don't assume the whole household uses one phrase.

:::note Your phone isn't in this list
The phone doesn't listen for a wake phrase. You start a conversation on it by tapping, and that always works, whatever this setting says. The list only shows Cora hardware that has voice.
:::

## Primary Cora Max

A Cora Max reads the equipment on your network. If more than one can reach the same controller, they'd all poll it side by side.

**Primary Cora Max** lets you pick, for each tank, which device reads that tank's controller. In Cora Mobile, open the tank and tap **Primary Cora Max**.

| Setting | Behaviour |
|---|---|
| A named device | It's the only Cora device that polls the controller. It stays the primary even while it's offline, and other Cora devices don't take over. Cora Mobile only polls while it's offline. |
| **Any active (automatic)** | Cora Mobile and any online Cora device share the work (last write wins). If one goes offline, another carries on. Good for a household with one device, and the safer choice if you're not sure which device should own the tank. |

While the device you named is offline, a command that has to go through it won't run. Cora tells you the tank is set to use that device, that it's offline and that nothing ran. Try again once it's back. If it'll be offline for a while, pick another device or **Any active (automatic)**.

:::note Two devices watching one tank? Set a primary
Naming a primary takes load off the controller and gets rid of duplicate readings from the same source.
:::

:::note This setting belongs to the tank
Primary Cora Max is set per tank for the whole account. It doesn't belong to the phone or Cora Max you're holding. Change it from any device and it changes for the whole household.
:::

## What works away from home

When you're away from your tank's Wi-Fi, your phone doesn't talk to your equipment directly. A command goes to Cora Cloud, which hands it to a Cora Max at the tank. That Cora Max is what reaches the equipment.

Here's what that means for you.

- **Readings and history** are always there, wherever you are. They're already stored in Cora Cloud.
- **Controlling equipment** works away from home too, as long as a Cora Max at the tank is online and can reach that equipment. That covers things like switching an outlet, starting a feed, dosing a head or pausing a pump. If no Cora Max can reach it, the command can't get through.
- **A device's own settings** (its native settings, not its readings) sometimes need a phone on the *same* network as the device. A Cora Max at the tank isn't enough for those. The page for that device says when this applies.

Two messages tell you a command didn't go through cleanly.

- **"Nothing was sent"** means the command never left your phone, or no Cora Max at the tank could take it. Nothing ran. You'll see this if the tank's Primary Cora Max is offline and no other device on that tank can step in.
- **"It may already have run"** means the command went out, but no Cora Max confirmed it in time. Cora really doesn't know whether it ran. Check the equipment itself before you try again, so you don't send it twice.

If either message keeps coming up, check that a Cora Max at the tank is online. You can also set **Primary Cora Max** to **Any active (automatic)** so any online device can pick up the command. Every possible outcome of a command is listed in [Controlling your equipment](/help/mobile-device-control).

## Where each device's state is shown

Cora Max shows each tank's polling status under **Settings → Cora Max Settings → Status**. There's more in [Devices and device health](/help/max-devices).

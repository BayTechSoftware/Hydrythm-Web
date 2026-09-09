---
title: Updates and recovery
description: How Cora Max updates itself, and what happens if an update goes wrong.
section: Cora Max
order: 14
---

## Automatic updates

Cora Max keeps itself current. New versions download in the background and install themselves; you are told what changed.

Nothing is required from you to stay up to date.

## Checking the version

![Device settings](img/max-updates.webp "Firmware update and device health, at the top of device settings.")

**Settings → Cora Max → Firmware → Firmware Update** covers checking, installing, the update channel and its schedule. **Device health & controls** sits directly beside it in the same **Firmware** group, and is where the unit's own diagnostics live — polling primary, device links and voice responder included.

## When an update is available

A prompt appears describing what is new, with two choices:

- **Update now** — installs immediately and restarts
- **Snooze 3 hours** — asks again later

Left alone, an update installs itself overnight, between roughly 3 and 5 in the morning, so the screen is not restarting while you are looking at it.

:::note Readings are not lost during an update
Data lives in your account, not on the screen. A unit that restarts comes back with the same tanks, dashboards and history.
:::

## Recovery

Recovery is a maintenance mode for when a unit will not start normally, or when you need to repair its setup without a laptop.

**To enter it:** hold **five fingers** on the top-right of the screen for about **ten seconds**, then enter the unit's **Recovery PIN**.

That six-digit PIN was shown when the unit was paired, and it is also in that device's settings in Cora Mobile. It is not shown on the Cora Max itself — which is the point: recovery cannot be reached by a guest, or by a child leaning on the screen.

From recovery you can:

- Repair the **Wi-Fi** connection
- **Re-pair** the unit to your account
- Force a **firmware update**
- **Factory reset** the unit

A unit that fails to start several times in a row can also roll itself back to the previous version.

:::warning A screen in recovery is not controlling anything
Your controller keeps running its own programming. But an [automation](/help/mobile-automation) whose action has to be carried out **by this Cora Max** cannot run while it is in recovery — the rule fires and the step does not reach the hardware.
:::

## If a unit does not restart

Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)** with the version shown on screen and what it says. Do not re-pair the unit first — pairing state is often useful in working out what happened.

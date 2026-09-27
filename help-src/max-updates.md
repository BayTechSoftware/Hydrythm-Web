---
title: Updates and recovery
description: How Cora Max updates itself, and what happens if an update goes wrong.
section: Cora Max
reviewed: 2026-09-09
order: 14
group: Settings
---

## Automatic updates

Cora Max keeps itself up to date. New versions download in the background and install themselves, and Cora Max tells you what changed.

You don't need to do anything to stay current.

## Checking the version

![Device settings](img/max-updates.webp "Firmware Update, in the Network & Updates section of Cora Max Settings.")

Go to **Settings → Cora Max Settings → Firmware Update** (in the **Network & Updates** section) to check for and install updates, and to set the update channel and schedule. Further down the same screen, the **Status** section shows each tank's polling status, last poll and last cloud write.

## When an update is available

A prompt tells you what's new and gives you two choices.

- **Update now** installs right away and restarts.
- **Snooze 3 hours** asks you again later.

If you leave it, the update installs itself overnight, roughly between 3 and 5 in the morning, so the screen doesn't restart while you're looking at it.

:::note You don't lose readings during an update
Your data lives in your account. When Cora Max restarts, it comes back with the same tanks, dashboards and history.
:::

## Recovery

Recovery is a maintenance mode for when Cora Max won't start normally, or when you need to fix its setup without a laptop.

To get in, hold **five fingers** on the top-right of the screen for about **ten seconds**, then enter the **Recovery PIN**.

You saw that six-digit PIN when you paired Cora Max, and it's also in that device's settings in Cora Mobile. Cora Max itself never shows it, so a guest or a child leaning on the screen can't get into recovery.

From recovery you can:

- Fix the **Wi-Fi** connection
- **Re-pair** Cora Max to your account
- Force a **firmware update**
- **Factory reset** Cora Max

If Cora Max fails to start several times in a row, it can also roll itself back to the previous version.

:::warning A screen in recovery isn't controlling anything
Your controller keeps running its own programming. But an [automation](/help/mobile-automation) step that **this Cora Max** has to carry out can't run while it's in recovery. The rule fires, but the step never reaches the equipment.
:::

## If a unit does not restart

Email **[cora@coraiq.tech](mailto:cora@coraiq.tech)** with the version shown on screen and the message it shows. Don't re-pair it first. The pairing state often helps work out what happened.

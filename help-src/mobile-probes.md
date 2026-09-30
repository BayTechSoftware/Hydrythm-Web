---
title: Probes
description: See which probe drives each reading across every controller, and log calibration and cleaning.
section: Cora Mobile
reviewed: 2026-09-30
order: 13
group: Equipment
---

If you have more than one controller, or two probes that both measure the same thing, Cora needs to know which reading to trust. Probe mapping is where you sort that out, and where you tell Cora what each probe is in the first place.

Open your **tank profile** (the pencil at the top of the dashboard) and choose **Probe Mapping**.

## Where each reading comes from

![Where each reading comes from](img/mobile-probes.webp "Every metric, which probe is driving it, and a Choose button to change it.")

This section lists every metric Cora tracks for this tank, such as pH or temperature, and shows which probe is currently feeding it.

Tap a reading to see every probe that reports it, across every controller you've connected. Each one shows its brand, its own name for the probe, and its live value. Pick one to pin it, or choose **Automatic** to let Cora use whichever probe is reporting.

A tag next to each reading shows which is in effect: **Automatic**, or **Chosen by you** once you've pinned a probe.

If a pinned probe stops reporting, Cora shows when it was last heard from and offers **Back to Automatic**, so a dead probe can't leave a reading stuck.

Tap **Rename** to give a reading its own display name. This is separate from any name you give the probe itself. It's what shows up on your dashboard, in alerts and in Reef Buddy.

:::note A leak sensor can't be reassigned here
A leak sensor's alarm depends on its own name, so it's excluded from this picker. It works the same as always.
:::

## Probes: telling Cora what each one is

Further down, you'll see every probe Cora knows about, grouped by the device that reports it, with its current reading. Cora recognises standard probe names on its own, and each row shows what it matched. Usually you only need to fix the few it couldn't place.

Each row gives you three choices.

- **A Cora parameter** is the metric that probe measures.
- **Custom** is for a probe Cora has no standard parameter for. Give it a short upper-case name, and Cora tracks it under that name.
- **Ignore** is for probes you don't want recorded at all.

An ignored or unmapped probe won't show on a dashboard and won't trigger alerts.

A mapping starts working the next time readings come in. Fixing one here doesn't rewrite history. It only changes what gets saved from then on. Tap **Save** to apply your changes.

:::warning Cora can't see an unmapped probe
If a parameter shows no readings but the probe is working, check its mapping first.
:::

## Multiple probes for one parameter

If you have two temperature probes, whether on the same controller or on two different ones, map them both. Cora keeps them as separate sources, and **Where each reading comes from** above is where you pick which one drives the reading, or leave it Automatic. You can compare them in [the parameter view](/help/mobile-metric-detail).

## Recording probe care

Probes drift. Cora can keep track of when you last calibrated or cleaned each one. That helps you tell a real change from a probe that needs attention.

Log a calibration or cleaning from the probe's entry. It also works well as a recurring [maintenance task](/help/mobile-maintenance).

:::note Calibration dates explain disagreements
When a probe and a test kit disagree, check when you last calibrated the probe. That's usually the answer.
:::

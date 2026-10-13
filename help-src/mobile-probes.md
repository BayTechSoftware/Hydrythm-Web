---
title: Parameter Mapping and probes
description: Choose which probe drives each reading, tell Cora what each probe measures, and record probe calibration and cleaning.
section: Cora Mobile
reviewed: 2026-10-13
order: 15
group: Equipment
---

Use **Parameter Mapping** to tell Cora what each probe measures and, when two probes report the same thing, which one to trust. Go to **Settings**, open the tank, and tap **Parameter Mapping**.

It sits between **Edit tank** and **Alert thresholds**. The pencil at the top of the dashboard opens **Edit tank**, which doesn't have it. You can also reach it from the Neptune Apex and GHL (Beta) device pages. GHL is only open to Beta users. See [Beta features](/help/mobile-beta).

The screen has a search field (**Search parameters**) and two tabs, **Mapping** and **Sources**. Search looks at parameter names, probe names, devices and brands. The same search field is in every parameter picker.

## Probes: telling Cora what each one is {#mapping}

![The Mapping tab](img/mobile-probe-mapping.webp "Each probe, grouped by the device that reports it, with the parameter it's mapped to.")

The **Mapping** tab opens first. It lists every probe Cora knows about, grouped by the device that reports it, with its current reading. Cora recognises standard probe names on its own, and each row shows what it matched. Usually you only need to fix the few it couldn't place.

Each row gives you three choices.

- **A Cora parameter** is the metric that probe measures.
- **Custom…** is for a probe Cora has no standard parameter for. Type a short upper-case name in **Custom metric (UPPER token)**, and Cora tracks it under that name.
- **Ignore** is for probes you don't want recorded at all.

An ignored or unmapped probe won't show on a dashboard and won't trigger alerts.

A mapping starts working the next time readings come in. Fixing one here doesn't rewrite history. It only changes what gets saved from then on. Tap **Save** to apply your changes.

:::warning Cora can't see an unmapped probe
If a parameter shows no readings but the probe is working, check its mapping first.
:::

## Where each reading comes from {#sources}

![The Sources tab](img/mobile-probes.webp "Each reading, the probe feeding it, and whether it's Automatic or Chosen by you.")

The **Sources** tab lists every metric Cora tracks for this tank, such as pH or temperature, and shows which probe is feeding it now.

Tap a reading to see every probe that reports it, across every controller you've connected. Each one shows its brand, its own name for the probe, and its live value. Pick one to pin it, or choose **Automatic (newest reading wins)** to let Cora use whichever probe reported most recently. The others stay in history.

A tag next to each reading shows which is in effect: **Automatic**, or **Chosen by you** once you've pinned a probe. Your choice applies to that reading across the whole tank, not to one widget.

If a pinned probe stops reporting, Cora shows when it was last heard from and offers **Back to Automatic**, so a dead probe can't leave a reading stuck.

Tap **Rename** to give a reading its own display name. This is separate from any name you give the probe itself. It's what shows up on your dashboard, in alerts and in Reef Buddy.

The tank profile also has a **Parameter Sources** section (it's hidden while you create a new tank). It sets the same thing in a shorter form. Use Parameter Mapping when you want every probe on every controller in one place.

:::note A leak sensor can't be reassigned here
A leak sensor's alarm depends on its own name, so it's excluded from this picker. It works the same as always.
:::

## Multiple probes for one parameter {#multiple-probes}

If you have two temperature probes, whether on the same controller or on two different ones, map them both. Cora keeps them as separate sources, and the **Sources** tab is where you pick which one drives the reading, or leave it on Automatic. You can compare them in [the parameter view](/help/mobile-metric-detail).

When two sources report the same parameter, the newest measurement wins. A value on screen is only replaced by a reading with a later measurement time, whichever device it comes from. An older reading, or a device that re-sends an old one, goes to history and doesn't overwrite the current value. If you pinned a source in the **Sources** tab, Cora follows that source instead.

## Recording probe care {#recording-probe-care}

Probes drift. When you calibrate, clean or replace a probe, tell Cora, so it doesn't mistake the jump in the reading for a real change in the tank.

1. Tap the parameter's widget on the dashboard, for example pH, temperature, salinity or ORP.
2. Tap **Record probe care** (the sensor icon) in the top bar.
3. Pick what you did: **Calibrated**, **Cleaned**, **Replaced**, **Repositioned** or **Compared to reference**. You can add a **Reference reading** and a note.
4. Tap **Log probe care**.

The parameter view then shows how long ago that probe was calibrated. Probe care also works well as a recurring [maintenance task](/help/mobile-maintenance).

:::note Calibration dates explain disagreements
When a probe and a test kit disagree, check when you last calibrated the probe. That's usually the answer.
:::

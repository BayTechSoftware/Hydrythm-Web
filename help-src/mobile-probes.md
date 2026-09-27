---
title: Probes
description: Match your controller's probes to Cora parameters, and log calibration and cleaning.
section: Cora Mobile
reviewed: 2026-09-09
order: 13
group: Equipment
---

Your controller gives its probes its own names. Probe mapping tells Cora which one is your pH probe, which one is temperature, and so on.

## Mapping probes

Open your **tank profile** (the pencil at the top of the dashboard), expand your controller's section and choose **Probe Mapping**.

![Probe mapping](img/mobile-probes.webp "Each probe your controller reports, its live reading, and what Cora is doing with it.")

You'll see every probe your controller reports, with its current reading. Cora recognises the standard names on its own, and each row shows what it matched. Usually you only need to fix the few it couldn't place.

Each row gives you three choices.

- **A Cora parameter** is the metric that probe measures.
- **Custom** is for a probe Cora has no standard parameter for. Give it a short upper-case name, and Cora tracks it under that name.
- **Ignore** is for probes you don't want recorded at all.

An ignored or unmapped probe won't show on a dashboard and won't trigger alerts.

A mapping starts working the next time readings come in. Fixing one here doesn't rewrite history. It only changes what gets saved from then on. Tap **Save** to apply your changes.

:::warning Cora can't see an unmapped probe
If a parameter shows no readings but the probe is working, check the mapping first.
:::

## Multiple probes for one parameter

If you have two temperature probes, you can map both. Cora keeps them as separate sources. The widget's source setting decides which one a tile follows, and you can compare them in [the parameter view](/help/mobile-metric-detail).

## Recording probe care

Probes drift. Cora can keep track of when you last calibrated or cleaned each one. That helps you tell a real change from a probe that needs attention.

Log a calibration or cleaning from the probe's entry. It also works well as a recurring [maintenance task](/help/mobile-maintenance).

:::note Calibration dates explain disagreements
When a probe and a test kit disagree, check when you last calibrated the probe. That's usually the answer.
:::

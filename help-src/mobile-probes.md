---
title: Probes
description: Map your controller's probes to Cora parameters, and record calibration and cleaning.
section: Cora Mobile
order: 11
---

A controller reports probes by its own names. Probe mapping tells Cora which of those is your pH probe, which is temperature, and so on.

## Mapping probes

Open your controller from the **Devices** tab and choose **Probe mapping**.

Each probe your controller reports is listed. Assign each one to the parameter it measures. Anything left unmapped is ignored — it will not appear on a dashboard and will not feed alerts.

:::warning An unmapped probe is invisible to Cora
If a parameter shows no readings although the probe is working, check the mapping before anything else.
:::

## Multiple probes for one parameter

A system with two temperature probes can map both. Cora keeps them as separate sources; the widget's source setting decides which one a tile follows, and [the parameter view](/help/mobile-metric-detail) lets you compare them.

## Recording probe care

Probes drift. Cora can track when each was last calibrated or cleaned, so you can tell a real change from a probe that needs attention.

Record calibration or cleaning from the probe's entry. It also fits well as a recurring [maintenance task](/help/mobile-maintenance).

:::note Calibration history explains disagreements
When a probe and a test kit disagree, the date the probe was last calibrated is usually the first thing worth checking.
:::

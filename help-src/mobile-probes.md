---
title: Probes
description: Map your controller's probes to Cora parameters, and record calibration and cleaning.
section: Cora Mobile
order: 12
---

A controller reports probes by its own names. Probe mapping tells Cora which of those is your pH probe, which is temperature, and so on.

## Mapping probes

Open your **tank profile** — the pencil at the top of the dashboard — expand your controller's section, and choose **Probe Mapping**.

![Probe mapping](img/mobile-probes.webp "Each probe your controller reports, its live reading, and what Cora is doing with it.")

Every probe your controller reports is listed with its current reading. Cora auto-detects the standard names, and the row shows which one it matched, so the job here is usually to correct the ones it could not place rather than to map all of them by hand.

Each row offers three choices:

- **A Cora parameter** — the metric that probe measures.
- **Custom** — for a probe Cora has no standard parameter for. You give it a short upper-case token, and it is tracked under that name.
- **Ignore** — for probes you do not want recorded at all.

An ignored or unmapped probe will not appear on a dashboard and will not feed alerts.

Mappings take effect when readings are next recorded, so a correction here does not rewrite history — it changes what is stored from that point on. Press **Save** to apply them.

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

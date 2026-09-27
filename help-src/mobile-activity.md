---
title: Activity and timeline
description: Everything that's happened to your equipment, and what caused it.
section: Cora Mobile
reviewed: 2026-09-09
order: 22
group: Records
---

Activity records every **actuation request**, meaning every attempt to change something. Each entry shows what asked for it and what happened next.

Some requests don't change anything. A refused request didn't run, with one exception: *No device answered in time* means it may still have run. Check the equipment before you try again. A no-change request found the equipment already in the requested state. An unconfirmed request may or may not have reached the device. Cora records every outcome.

**Settings → Activity.**

![The activity log](img/mobile-activity.webp "Every action, with the surface that requested it.")

## What is recorded

Every **request** is recorded, including the ones that didn't work. That covers outlet switches, feed cycles, doses, plug changes, and anything a scene or automation did.

A request that was **refused**, made **no change** or came back **unconfirmed** is recorded the same way as one that ran. A command that quietly did nothing is exactly what you want to find here.

## What caused it

Each entry names its cause:

| Cause | Means |
|---|---|
| **This app** | You tapped it here |
| **Voice in this app** | You asked, on this phone |
| **Tapped on a Cora** | Someone used a Cora screen. The row says which one |
| **Voice on a Cora Max** | Someone spoke to a screen |
| **Cora Assistant** | You asked Cora to do it |
| **Automation rule** | A rule fired |
| **Smart button** | Someone pressed a physical button |
| **Sent from Cora Cloud** | It came from your account through Cora Cloud |
| **Unknown source** | Recorded before Cora could tell where it came from |

## How it travelled

Each row also has a route chip. When something goes wrong, how the request reached your equipment often explains why.

| Chip | Means |
|---|---|
| **LAN** | Sent over your own network, straight to the equipment |
| **VIA CLOUD** | Sent through your account, for equipment Cora can't reach directly |
| **ROUTE ?** | Recorded before routes were tracked, so the route really is unknown |

If you have more than one Cora, the row also says which one carried out the request.

## The tank timeline

Apart from equipment actions, each tank has a **timeline**. It lays out readings, alerts, journal entries, ICP results and livestock changes in order.

Use activity when you want to know *"what did something do?"* Use the timeline when you want to know *"what was happening around this date?"*

:::note Use the timeline with the journal
The timeline holds what Cora recorded. The [journal](/help/mobile-journal) holds what you did. Read them side by side to see cause and effect around a date.
:::

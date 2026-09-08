---
title: Activity and timeline
description: Everything that has happened to your equipment, and what caused it.
section: Cora Mobile
order: 21
---

Activity records every **actuation request** — every attempt to change something — together with what asked for it and what became of it.

A request is not the same as a change. Refused requests never ran, no-change requests found the equipment already as asked, and an unconfirmed one may or may not have reached the device at all. All of them are recorded, which is what makes the log worth reading.

**Settings → Activity.**

![The activity log](img/mobile-activity.webp "Every action, with the surface that requested it.")

## What is recorded

Every **request**, not only the ones that worked — outlet switches, feed cycles, doses, plug changes, and anything a scene or automation did.

A request that was **refused**, that made **no change**, or that went out and came back **unconfirmed** is recorded just as an executed one is. That is the point: a command that quietly did nothing is exactly what you want to find here.

## What caused it

This is the column that matters. Each entry names its cause:

| Cause | Means |
|---|---|
| **This app** | You tapped it here |
| **Voice in this app** | You asked, on this phone |
| **Tapped on a Cora** | Someone used a Cora screen — the row says which |
| **Voice on a Cora Max** | Someone spoke to a screen |
| **Cora Assistant** | You asked Cora to do it |
| **Automation rule** | A rule fired |
| **Smart button** | A physical button was pressed |
| **Sent from Cora Cloud** | Issued by your account rather than by a device in front of you |
| **Unknown source** | Recorded before the source could be identified |

## How it travelled

Each row also carries a route chip, because *how* a request reached your equipment explains a lot of what went wrong when something did:

| Chip | Means |
|---|---|
| **LAN** | Sent across your own network, directly to the equipment |
| **VIA CLOUD** | Sent through your account, for equipment not reachable directly |
| **ROUTE ?** | Recorded before routes were tracked — genuinely unknown, not assumed |

On a system with more than one Cora, the row also names which one carried the request out.

## The tank timeline

Separately from equipment actions, each tank has a **timeline** — readings, alerts, journal entries, ICP results and livestock changes laid out in order.

Use activity when you are asking *"what did something do?"* and the timeline when you are asking *"what was happening around this date?"*

:::note The timeline and the journal are complementary
The timeline holds what Cora recorded; the [journal](/help/mobile-journal) holds what you did. Read together they establish cause and effect around a given date.
:::

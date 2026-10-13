---
title: Activity and timeline
description: See every change sent to your equipment, who or what asked for it and whether it worked, and read the tank's timeline around a date.
section: Cora Mobile
reviewed: 2026-10-13
order: 28
group: Records
twin: max-activity
---

Activity lists every attempt to change something on your equipment: outlet switches, feed cycles, doses, and anything a scene or automation did. Each row shows what asked for it and what happened next, including the requests that didn't work.

Go to **Settings → Activity**. If you have more than one tank, pick it with the tank chips at the top.

![Activity in Cora Mobile](img/mobile-activity.webp "The outcome key at the top, then each action with its outcome, cause and route.")

## What the outcomes mean {#outcomes}

Each row carries an outcome. The same key is at the top of the screen under **WHAT THE OUTCOMES MEAN**.

| Outcome | Means |
|---|---|
| **Confirmed** | The device said it did it |
| **Unconfirmed** | It was sent, but nothing reported back. It may or may not have reached the device |
| **Refused** | It was turned down and didn't run. Read the row to see why |
| **No change** | The equipment was already in that state, so nothing was sent |

One refusal is different. *No device answered in time* means the request may still have run. Check the equipment before you try again.

A command that quietly did nothing is exactly what you want to find here, so failed and unchanged requests are kept along with the ones that worked.

## What caused it {#causes}

Each row names its cause:

| Cause | Means |
|---|---|
| **This app** | You tapped it in Cora Mobile |
| **Voice in this app** | You asked by voice, on this phone |
| **Tapped on a Cora** | Someone used a Cora Max screen. The row says which one |
| **Voice on a Cora Max** | Someone spoke to a Cora Max |
| **Cora Assistant** | You asked Cora Assistant to do it in a chat |
| **Automation rule** | An [automation or scene](/help/mobile-automation) did it |
| **Sent from Cora Cloud** | It came from your account through Cora Cloud |
| **Unknown source** | Recorded before Cora could tell where it came from |

## How it travelled {#route}

Each row also has a route chip. When something goes wrong, how the request reached your equipment often explains why.

| Chip | Means |
|---|---|
| **LAN** | Sent over your own network, straight to the equipment |
| **VIA CLOUD** | Sent through your account, for equipment Cora can't reach directly |
| **ROUTE ?** | Recorded before routes were tracked, so the route is unknown |

If you have more than one Cora Max, the row also says which one carried out the request.

## The tank timeline {#tank-timeline}

Activity is about equipment. The tank timeline, called **Tank Story** on screen, is about the tank. It lays out journal entries, maintenance, livestock changes, water tests and alerts in date order, with milestones along the way.

To open it, go to the [journal](/help/mobile-journal) and tap the **Tank timeline** icon at the top. Use the chips at the top to show only **Journal**, **Maintenance**, **Livestock**, **Water tests** or **Alerts**, or **All**. **Load older story** goes further back. You can add a **New Entry** or dictate one from here too.

Use Activity when you want to know *"what did something do?"* Use the timeline when you want to know *"what was happening around this date?"*

:::note Use the timeline with the journal
The timeline gathers what Cora recorded. The journal holds what you did and why. Read them side by side to see cause and effect around a date.
:::

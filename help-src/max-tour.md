---
title: The Cora Max home screen
description: What the top bar, status tag, alert tags, tank menu and dashboard on Cora Max mean, and how to switch tanks and open Outlets & Feed.
section: Cora Max
reviewed: 2026-10-13
order: 2
group: Getting started
twin: mobile-tour
---

This page explains what you see on Cora Max. It shows one tank at a time, with live readings filling the screen so you can read them from across the room.

![The Cora Max home screen with one tank's gauges, values, graphs and device tiles under the top bar](img/max-home.webp "One tank's dashboard fills the screen, with the top bar above it.")

## The top bar {#the-top-bar}

![The Cora Max top bar](img/max-topbar.webp "The top bar, numbered left to right to match the list below.")

From left to right:

1. **The grid icon** opens [the Reef Room](/help/max-reef-room), the overview of every tank this screen shows.
2. **The tank name**, with a small arrow. Tap it to open the **tank menu**, which has every screen for the tank you're looking at. The full list is below.
3. **Alert tags** show what needs attention right now: readings out of range, device faults, missed doses or low supplies. Tap a tag to bring that alert back to the middle of the screen. If there are more than fit, you'll see **+2** (or however many). Tap it to see every active alarm.
4. **The clock**. You can hide it with **Show clock** in **Settings → Cora Max Settings**.
5. **The status tag** shows what this screen is doing right now. Green means all is well, blue means busy, amber needs a look, and red is a fault. Every status is listed below.
6. **Battery and Wi-Fi**.
7. **The devices icon** opens **Devices**, filtered to this tank. A tank with no devices doesn't show it.
8. **The Reef Buddy icon** opens today's briefing. A dot means you haven't read it yet.
9. **The Cora Assistant icon** starts a voice conversation.
10. **The gear** opens settings.

:::warning Cora Assistant starts listening right away
Tapping the Cora Assistant icon starts a live voice session. If you wanted settings, that's the gear on the far right.
:::

### What the status tag means {#what-the-status-pill-means}

| Tag | Meaning |
|---|---|
| **Online** | This screen is collecting your readings, and they're up to date |
| **Cloud** | Another Cora is collecting this tank's readings and this screen is showing them. They're just as up to date as with **Online**. If you have more than one Cora, the one that isn't collecting shows this |
| **Polling Apex**, **Voice active** | Busy with something right now (blue) |
| **Polling off** | Collecting is turned off for this tank. You can turn it back on in Cora Mobile |
| **Updating** | Collecting is paused while an update installs |
| **Stale** | Readings have stopped coming in. The screen shows the last ones it got |
| **Apex retry 12s** | Your Apex didn't answer. Cora Max tries again when the countdown ends |
| **Cloud sync failed** | Your Apex answered, but its readings couldn't be saved to Cora Cloud, so the dashboard falls behind. Cora Max keeps trying |
| **Cloud save refused** | Cora Cloud is refusing to save some of this screen's data. Nothing is wrong with your tank or with Cora Max, and nothing needs changing on this screen. The fix is a Cora Cloud update. Open **Settings → Cora Max Settings** and scroll to the **Status** section, where the **Cloud save** line says which data is affected. Then [contact support](/support.html) |
| **Offline** | No connection. The screen shows the last data it got |
| **Offline, retrying in 30s** | Your network is up, but Cora Cloud has been out of reach for about 15 seconds. Cora Max reconnects by itself, and the countdown shows when it tries next |
| **Main Cora offline** | This screen is a second Cora Max for this tank, and the **Primary Cora Max** (the one pinned to read this tank's equipment) has gone offline. This screen keeps showing the last data it has until the primary comes back or you choose a different Primary Cora Max. More in [More than one Cora device](/help/mobile-multi-device) |
| **Apex password** | Your Apex turned down the saved password. Have a look at [Troubleshooting](/help/troubleshooting) |

:::note How the retry countdown works
Cora Max tries to reconnect at a steady pace. It waits about 15 seconds after the first drop, then 15 seconds again, then 30 seconds twice, then once a minute until it gets through. It never gives up. **Offline, retrying in 30s** is normal.
:::

## The dashboard {#the-dashboard}

The rest of the screen is the dashboard, a fixed grid that keeps every widget visible. It doesn't scroll.

Widgets work the same as on your phone, but big enough to read from a few steps back. What each shape shows is in the [Widget reference](/help/mobile-widgets). To change what's on the dashboard, see [Editing the Cora Max dashboard](/help/max-dashboard-editing).

Every widget with a measured parameter shows its **age** and **source**, just like on your phone. A number with `2d` next to it is two days old. Device and control tiles show their own state instead.

### When the screen is dimmed {#when-the-screen-is-dimmed}

After the **Dim after** time with no touch, the screen dims. Your first tap only wakes it, so it can't press a control by accident. Tap again to use the screen.

## The tank menu {#the-tank-menu}

![The tank menu open over the dashboard, listing Log parameters, Journal, Reef Buddy and the other screens for the tank](img/max-menu.webp "The tank menu, opened from the tank name in the top bar.")

Tap the tank name to open the menu for the tank on screen.

| Item | Opens |
|---|---|
| **Log parameters** | Type in test-kit readings on the on-screen keyboard |
| **Journal** | [The journal](/help/max-records) for this tank |
| **Reef Buddy** | The latest [briefing](/help/max-intelligence) |
| **Health Reports** | Health assessments |
| **Maintenance** | The [task list](/help/max-records) |
| **ICP Reports** | Uploaded [lab results](/help/max-intelligence) |
| **Parameter History** | Pick any parameter that has data and open its [chart](/help/max-intelligence) |
| **Alert thresholds** | The [healthy range](/help/max-alerts) for each metric on this tank |
| **Livestock** | This tank's inventory, view only on this screen |
| **Activity** | [Every outlet, feed and dose](/help/max-activity), and what happened |
| **Dashboard layout** | [Arrange the widgets on this screen](/help/max-dashboard-editing) |
| **Units** | The display units for this tank's readings |
| **Tank settings** | The full settings screen for this tank |

## Switching tanks {#switching-tanks}

Tap the **grid icon** at the far left of the top bar to go to [the Reef Room](/help/max-reef-room), then open the tank you want. You can also swipe sideways on the dashboard. Each tank has its own dashboard layout, so the whole screen changes as you switch.

## The Outlets & Feed drawer {#the-outlets-feed-drawer}

On a tank with a Neptune Apex, a small **Outlets & Feed** label sits at the bottom of the dashboard. Tap it, or swipe up anywhere on the dashboard, to open **Controls**.

- **FEED** starts one of your Apex feed cycles with **A**, **B**, **C** or **D**. **Cancel** ends it early.
- **Outlets** can each be switched between Auto, Off and On.

It lists the outlets and feed cycles you picked for this dashboard, or all of them if you haven't picked any. More in [Outlets and controls](/help/max-controls).

:::warning This drawer controls real equipment
A command goes out the moment you tap, but sending it doesn't mean it's done. It comes back Confirmed, Unconfirmed, Refused or No change, and you can see which in [Activity](/help/max-activity). Feed mode is the safe way to pause flow for feeding, because it puts everything back by itself. A manual Off stays off until you change it back.
:::

## If something looks out of place {#if-something-looks-out-of-place}

If readings look stale, or the status tag is amber or red, start with [Troubleshooting](/help/troubleshooting).

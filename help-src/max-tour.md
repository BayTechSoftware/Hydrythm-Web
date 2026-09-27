---
title: The Cora Max home screen
description: What everything on the Cora Max display means, from the top bar to the dashboard grid and the outlets drawer.
section: Cora Max
reviewed: 2026-09-27
order: 2
group: Getting started
---

Cora Max shows one tank at a time, with live readings filling the screen so you can read them from across the room.

![The Cora Max home screen](img/max-home.webp "One tank, filling the screen.")

## The top bar

From left to right:

- **The grid icon** opens the Reef Room, the overview of every tank this screen shows.
- **The tank name**, with a small arrow. Tap it to open the **tank menu**, which has every screen for the tank you're looking at, from logging a test result to arranging the dashboard. The full list is below.
- **Alert tags** show anything that's out of range right now. If there are more than fit, you'll see **+2** (or however many). Tap one to see them all.
- **The clock**.
- **The status tag** shows what this screen is doing right now. Green means all is well, amber needs a look, and red is a fault. Every status is listed below.
- **Battery and Wi-Fi**.
- **The devices icon** shows everything connected and how it's doing.
- **The Reef Buddy icon** opens today's briefing. A dot means you haven't read it yet.
- **The Cora Assistant icon** starts a voice conversation.
- **The gear** opens settings.

### What the status pill means

| Tag | Meaning |
|---|---|
| **Online** | This screen is collecting your readings, and they're up to date |
| **Cloud** | Another Cora is collecting this tank's readings and this screen is showing them. They're just as up to date as with **Online**. If you have more than one Cora, the one that isn't collecting shows this |
| **Polling Apex**, **Voice active** | Busy with something right now |
| **Polling off** | Collecting is turned off for this tank. You can turn it back on in Cora Mobile |
| **Updating** | Collecting is paused while an update installs |
| **Stale** | Readings have stopped coming in. The screen shows the last ones it got |
| **Apex retry 12s** | Your Apex didn't answer. Cora Max tries again when the countdown ends |
| **Cloud sync failed** | Your Apex answered, but its readings couldn't be saved to Cora Cloud, so the dashboard falls behind. Cora Max keeps trying |
| **Offline** | No connection. The screen shows the last data it got |
| **Offline, retrying in 45s** | Your network is up, but Cora Cloud has been out of reach for more than 30 seconds. Cora Max reconnects by itself, and the countdown shows when it tries next |
| **Main Cora offline** | This screen is a second Cora Max for this tank, and the **Primary Cora Max** (the one pinned to read this tank's equipment) has gone offline. This screen keeps showing the last data it has until the primary comes back or you choose a different Primary Cora Max. More in [More than one Cora device](/help/mobile-multi-device) |
| **Apex password** | Your Apex turned down the saved password. Have a look at [Troubleshooting](/help/troubleshooting) |

:::note How the retry countdown works
Cora Max tries to reconnect at a steady pace. It waits about 15 seconds after the first drop, then 15 seconds again, then 30 seconds twice, then once a minute until it gets through. It never gives up. **Offline, retrying in 45s** is normal.
:::

:::warning Cora Assistant starts listening right away
Tapping the Cora Assistant icon starts a live voice session. If you wanted settings, that's the gear on the far right.
:::

## The dashboard

The rest of the screen is the dashboard, a fixed grid of widgets you can see all at once. It doesn't scroll.

Widgets work the same as on your phone, but big enough to read from a few steps back. What each shape shows is in the [Widget reference](/help/mobile-widgets). To change what's on the dashboard, see [Editing the Cora Max dashboard](/help/max-dashboard-editing).

Every widget with a measured parameter shows its **age** and **source**, just like on your phone. A number with `2d` next to it is two days old. Device and control tiles show their own state instead.

## The tank menu

![The tank menu](img/max-menu.webp "Everything for the current tank, from the tank name in the top bar.")

Tap the tank name to open the menu for the tank on screen.

| Item | Opens |
|---|---|
| **Log parameters** | Type in test-kit readings on the on-screen keyboard |
| **Journal** | [The journal](/help/mobile-journal) for this tank |
| **Reef Buddy** | The latest [briefing](/help/mobile-reef-buddy) |
| **Health Reports** | Health assessments |
| **Maintenance** | The [task list](/help/mobile-maintenance) |
| **ICP Reports** | Uploaded [lab results](/help/mobile-icp-health) |
| **Alerts** | The healthy range for each metric on this tank |
| **Livestock** | This tank's [inventory](/help/mobile-livestock), view only on this screen |
| **Activity** | [Every outlet, feed and dose](/help/max-activity), and what happened |
| **Dashboard layout** | [Arrange the widgets on this screen](/help/max-dashboard-editing) |
| **Tank settings** | The full settings screen for this tank |

## Switching tanks

Tap the **grid icon** at the far left of the top bar to go to [the Reef Room](/help/max-reef-room), then open the tank you want. Each tank has its own dashboard layout, so the whole screen changes as you switch.

## The Outlets & Feed drawer

Pull up the tab at the bottom of the screen to open a drawer with every outlet on the system and the feed controls.

- **Outlets** can each be switched between Auto, Off and On.
- **Feed** pauses the right equipment while you feed and puts it all back afterwards.

:::warning This drawer controls real equipment
Everything here acts on your equipment. A command goes out the moment you tap, but sending it doesn't mean it's done. It comes back Confirmed, Unconfirmed, Refused or No change, and you can see which in [Activity](/help/max-activity). Feed mode is the safe way to pause flow for feeding, because it puts everything back by itself. A manual Off stays off until you change it back.
:::

## If something looks out of place

If readings look stale, or the status tag is amber or red, start with [Troubleshooting](/help/troubleshooting).

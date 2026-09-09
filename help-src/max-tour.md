---
title: The Cora Max home screen
description: What everything on the Cora Max display means — the top bar, the dashboard grid, and the outlets drawer.
section: Cora Max
reviewed: 2026-09-09
order: 2
group: Getting started
---

Cora Max shows one tank at a time, filling the screen with live readings you can read from across the room.

![The Cora Max home screen](img/max-home.webp "One tank, filling the screen.")

## The top bar

Left to right:

- **The grid icon** opens the Reef Room, the overview of every tank this screen shows
- **The tank name**, with a chevron. Tapping it opens the **tank menu** — every screen for the tank on display, from logging a test result to arranging the dashboard. The full list is below.
- **Alert pills** — anything currently out of range, with a **+n** when there are more than fit. Tap to see them all.
- **The clock**
- **The status pill** — what this screen is doing right now. Green is healthy, amber wants attention, red is a fault. The full vocabulary is below.
- **Battery and Wi-Fi**
- **The devices icon** — everything connected, and how it is doing
- **The Reef Buddy icon** — opens today's briefing. A dot means the briefing has not been read yet.
- **The Cora swoosh** — starts a voice conversation
- **The gear** — settings

### What the status pill means

| Pill | Meaning |
|---|---|
| **Online** | This screen is collecting your readings, and they are current |
| **Cloud** | Another Cora is collecting this tank's readings and this screen is showing them. Just as current as **Online** — with more than one Cora, the screen that is not doing the collecting shows this |
| **Polling Apex**, **Voice active** | Working on something at this moment |
| **Polling off** | Collection is switched off for this tank. You can turn it back on from Cora Mobile |
| **Updating** | Collection is paused while an update installs |
| **Stale** | Readings have stopped arriving. The screen shows the last it received |
| **Offline** | No connection. The screen shows the last data it received |
| **Apex password** | Your Apex rejected the stored password. See [Troubleshooting](/help/troubleshooting) |

:::warning The swoosh starts listening immediately
Tapping the Cora mark begins a live voice session. If you meant to open settings, that is the gear on the far right.
:::

## The dashboard

The remainder of the screen is the dashboard: a fixed grid of widgets, all visible at once. The Cora Max dashboard does not scroll.

Widgets work the same as on your phone, at a size you can read standing back. See **[Widget reference](/help/mobile-widgets)** for what each shape shows, and **[Editing the Cora Max dashboard](/help/max-dashboard-editing)** to change what is on it.

Every widget showing a measured parameter carries its **age** and its **source**, just like on the phone. A number with `2d` next to it is two days old, and is shown as such. Device and control tiles show their own state instead.

## The tank menu

![The tank menu](img/max-menu.webp "Everything for the current tank, from the tank name in the top bar.")

Tapping the tank name opens the menu for the tank currently on screen:

| Item | Opens |
|---|---|
| **Log parameters** | Enter test-kit readings on the on-screen keyboard |
| **Journal** | [The journal](/help/mobile-journal) for this tank |
| **Reef Buddy** | The current [briefing](/help/mobile-reef-buddy) |
| **Health Reports** | Health assessments |
| **Maintenance** | The [task list](/help/mobile-maintenance) |
| **ICP Reports** | Uploaded [lab results](/help/mobile-icp-health) |
| **Alerts** | The healthy band for each metric on this tank |
| **Livestock** | This tank's [inventory](/help/mobile-livestock), read-only on this screen |
| **Activity** | [Every outlet, feed and dose](/help/max-activity), and what came of it |
| **Dashboard layout** | [Arrange the widgets on this screen](/help/max-dashboard-editing) |
| **Tank settings** | The full settings screen for this tank |

## Switching tanks

Use the **grid icon** at the far left of the top bar to reach [the Reef Room](/help/max-reef-room), then open the tank you want. Each tank keeps its own dashboard layout, so the whole screen changes as you move between them.

## The Outlets & Feed drawer

The tab at the bottom of the screen pulls up a drawer with every outlet on the system and the feed controls.

- **Outlets** — each one switchable between Auto, Off and On
- **Feed** — pauses the right equipment for a feeding and puts it all back afterwards

:::warning This drawer controls real equipment
Everything in it acts on real equipment. A command is sent the moment you tap, but *sent* is not *done* — it comes back Confirmed, Unconfirmed, Refused or No change, and [Activity](/help/max-activity) is where you see which. Feed mode is the safe way to pause flow for feeding, because it restores everything by itself; a manual Off stays off until you change it back.
:::

## If something looks out of place

If readings look stale, or the status pill is amber or red, start with **[Troubleshooting](/help/troubleshooting)**.

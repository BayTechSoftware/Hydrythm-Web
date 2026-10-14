---
title: Cora Mobile settings
description: Where everything is in Cora Mobile's Settings tab, from your account and plan to tanks, Cora Assistant, language, dark mode, notifications and support.
section: Cora Mobile
reviewed: 2026-10-13
order: 35
group: Settings and account
twin: max-settings
---

This page walks through the **Settings** tab, in the order you'll find things.

![The Settings tab in Cora Mobile](img/mobile-settings.webp "Your account card at the top, a Vacation mode banner while it's on, then the Cora group.")

## Your account

The card at the top shows who you're signed in as and which plan you're on. Tap it to open **Account & Subscription**. It has these, from top to bottom.

- **Display name** is what Cora Mobile calls you.
- **Lab & ICP emails** lets you add up to 3 more email addresses that your lab can use to reach your account. See [ICP and health reports](/help/mobile-icp-health#which-email-a-lab-can-use).
- **Subscription** shows your plan and when it renews, with **See plans**, **Upgrade** or **Upgrade to Max**, then **Manage Subscription** and **Restore Purchases**. On Android there's also **Redeem code**. All of it is explained in [Plans and subscriptions](/help/mobile-plans).
- **Sign Out**
- **Export My Data** gives you your readings, journal entries and alerts as files, free on every plan. See [Exporting your data](/help/mobile-data-export).
- **Delete Account** is permanent. Read the two notes in [Your data and privacy](#your-data-and-privacy) before you use it.

## Cora

- **Automations** are rules and scenes that run on their own. There's more in [Automations and scenes](/help/mobile-automation).
- **Cora Assistant** holds the AI consent switches, AI memory, the Answering device, lab sharing and your usage. See [Cora Assistant](#cora-assistant) below.
- **Activity** is a log of every command sent to your equipment. More in [Activity and timeline](/help/mobile-activity).
- **Dosing Products** holds the strength of what you dose. More in [Dosing](/help/mobile-dosing).

:::warning Automations act on real equipment
A rule that switches a pump will switch it even when you're not watching. Build rules one at a time, and check each one does what you expect before you add the next.
:::

## Tanks

You'll see one row for each tank, then these.

- **Add tank** opens a new tank profile.
- **Reorder tanks** sets the order they come up when you swipe the dashboard. It also decides which tanks get Reef Buddy and AI monitoring when your plan covers fewer tanks than you have. See [Plans and subscriptions](/help/mobile-plans#paid-tiers).
- **Removed tanks** keeps tanks you've removed. Removing only hides a tank, and **Restore** brings it back with its readings, journal and devices.

Adding, removing and restoring tanks are covered step by step in [Managing your tanks](/help/mobile-tanks).

Open a tank and its settings page has three parts.

- **Settings** holds **Edit tank**, **Parameter Mapping**, **Alert thresholds**, **Units**, **Primary Cora Max** and **Vacation mode**.
- **Records & Reports** holds **Journal**, **Maintenance**, **Livestock**, **Reef Buddy**, **Health Reports**, **ICP Reports**, **Activity** and **Guided setup**.
- **Devices on this tank** is a read-only list.

**Parameter Mapping** is where you choose which device feeds each reading. See [Parameter Mapping](/help/mobile-probes). **Units** sets how this tank shows its readings, including litres or US or UK gallons for volume. See [Your tank profile](/help/mobile-tank-profile). **Primary Cora Max** is which device polls that tank's equipment, and is explained in [More than one Cora device](/help/mobile-multi-device#primary-cora-max). To add or remove a device, use the [Devices tab](/help/mobile-devices).

**Vacation mode** is a plan for whoever looks after the tank while you're away. You set the dates and make a checklist of jobs, with how often each one needs doing. Cora turns it into a simple read-only page you can share with your tank sitter. They don't need an account. More in [Going away](/help/mobile-vacation).

## App Settings

- **Notifications** decides what reaches your phone. More in [Notifications](/help/mobile-notifications).
- **Briefing time** is the hour your daily Reef Buddy briefing arrives, in your own time zone. It's one setting for the account, shared with Cora Max. More in [Reef Buddy](/help/mobile-reef-buddy#when-it-arrives).
- **Language** is the account's language. See below.
- **Appearance** has a **Dark Mode** switch. On, Cora Mobile uses the dark Deep Reef theme. Off, it uses the light Luminous Azure theme.
- **Device access** is explained below.
- **Help & Support** is where you contact support, report a bug and find the Cora website and FAQ. See below.
- **About** is explained below.

## Language

**There's one language for the whole account.** Devices don't each have their own. If you change it on your phone, it changes on every Cora Max in the household too, and the other way round. New reports, alerts and Reef Buddy briefings use the new language from then on. Older ones stay in the language they were written in. They aren't translated again.

If everything suddenly shows up in a language you didn't expect, someone changed it. They may have done it here, from another device on the account, or in the **Language** setting on a Cora Max. It's the same setting everywhere.

## Device access

**Device access** opens your phone's own settings for Cora. That's where you allow what Cora needs to find your equipment. The row doesn't show whether anything is turned off. It just takes you to the place where you can check.

- On iPhone, it's Local Network and Bluetooth. Without Local Network access, a search for equipment on your Wi-Fi finds nothing, and you won't see an error. iPhone only asks once, so this is how you turn it back on.
- On Android, it's Bluetooth and location.

## Cora Assistant

You open this from the **Cora Assistant** row under **Cora**, further up.

- **Allow Cora Assistant to use saved tank data** lets Cora Assistant use your tank history, metrics and devices. It has to be on for the Assistant (typed or spoken, on your phone and on Cora Max), ICP analysis, Health Reports and **Design with AI**. Reef Buddy still comes without it, with a plain summary. The full list is in [Asking Cora](/help/mobile-assistant#what-the-switch-covers).
- **Contribute anonymized tank data** keeps a de-identified copy of your parameter history for reef research. **It's on unless you turn it off.** That copy is made when you remove a tank, and it's the only thing kept after you delete your account. See [Contributing anonymised data](/help/mobile-data-export#contributing-anonymised-data).
- **AI memory** is what Cora remembers about your system from one conversation to the next. You can read it and reset it. It only shows while the consent switch above is on.
- **Answering device** picks which Cora device answers the wake phrase in your home. More in [More than one Cora device](/help/mobile-multi-device#cora-assistant-answering-device).
- **Share Cora's analysis with labs** decides whether a lab that sends you results can see Cora's scores and written analysis. It's off until you turn it on.
- **Trusted labs** lists the labs that can send results to your tanks without asking each time. It shows up once you've trusted one. More in [ICP and health reports](/help/mobile-icp-health#trusted-labs).
- **Usage & Limits** shows your monthly allowances and how much you've used.

## Your data and privacy

Three settings about your data live in different places, so they're easy to miss.

- **Export My Data** is in **Account & Subscription**, just above **Delete Account**. See [Exporting your data](/help/mobile-data-export).
- **Contribute anonymized tank data** is under **Cora Assistant**, above.
- **Send crash reports** is in **Help & Support**. It sends the technical details when Cora Mobile stops or a screen fails to load, without you having to write anything. No tank data, photos or account details are included.

:::warning Deleting your account does NOT cancel your subscription
An App Store or Google Play subscription belongs to the **store**, not to Cora. Deleting your account removes your record here, but **the billing doesn't stop**. You keep being charged until you cancel with Apple or Google yourself. Cancel the subscription first, then delete the account.
:::

:::note What deleting doesn't remove
If **Contribute anonymized tank data** is on (and it is, unless you turned it off), a de-identified copy of your tanks' profiles and parameter history is kept for research when you delete your account. It has no link back to you. If you want that gone too, turn the switch off *before* you delete.
:::

## Help & Support {#getting-help}

**Settings → Help & Support** has these.

- **Contact Support** opens an email to us. We usually reply within a day.
- **Report a Bug / Send Feedback** sends a report from inside Cora Mobile. See [Reporting a problem](/help/mobile-support).
- **Send crash reports**, described above.
- **Cora Website & FAQ** opens the Cora website.

## About

This shows the version you're running, and a few more rows.

- **Replay tips** plays the first-run dashboard tour again, the one described in [The first-run tour](/help/mobile-tour#the-first-run-tour). It's handy after an update, or when someone new starts using Cora Mobile.
- **Privacy Policy** and **Terms and Conditions** link to the legal pages.
- **Licenses** lists the open-source software Cora Mobile is built on.

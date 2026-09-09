---
title: Your data
description: Export your readings, journal and alerts as spreadsheets, and how to delete your account.
section: Cora Mobile
order: 30
---

Your tank records are yours, and you can take them out at any time.

![Account data controls](img/mobile-data.webp "Export and deletion sit together at the foot of Account & Subscription.")

## Exporting

**Settings → your account → Export My Data.**

Exporting is **free on every plan**, including the free one.

Cora exports as **CSV files** — spreadsheets that open in Excel, Numbers, Google Sheets, or anything that reads a table:

| File | Contains |
|---|---|
| `cora_parameters.csv` | Your readings, each with its source and timestamp |
| `cora_journal.csv` | Your journal entries |
| `cora_alerts.csv` | Alerts raised |
| `cora_export_summary.csv` | What this export covers, including anything that was truncated |

:::note What the export is, and what it is not
It covers **readings, journal entries and alerts** — the three records people ask for. It is not a copy of everything in your account: dashboards, livestock, maintenance, automations, reports and device settings are not included.

Each of the three is capped at **25,000 rows per tank**. A tank logging thirty metrics every five minutes writes more than that in three days, so a long-running tank will be cut off at the cap. The summary file states plainly when that has happened — check it rather than assuming the file is complete.
:::

The parameter export carries the **source** of each reading, not just the value — so a spreadsheet of your alkalinity keeps the distinction between what your probe said and what your test kit said.

:::note Export before major changes
Take an export before decommissioning a tank or making significant changes to your setup. The exported files are independent of the app and your account.
:::

## Signing out versus deleting

**Sign Out** disconnects this device from your account. Your data is untouched and signing back in restores everything.

**Delete account** is permanent.

## Deleting your account

**Settings → your account → Delete account.**

This is permanent. It removes your account, your tanks, your readings, your journal, your lab results and your device links. It cannot be undone and there is no grace period.

Export first if you want to keep anything.

:::warning It does not cancel your subscription
An App Store or Google Play subscription belongs to the **store**, not to Cora. Deleting your account removes your record here and **nothing stops the billing** — the charges continue until you cancel with Apple or Google yourself. Cancel there first, then delete.

## Contributing anonymised data

**Settings → Assistant & AI → Contribute anonymized tank data.**

While this is on, your tank's parameter history is retained for reef research **with no link to you** even if you later delete your account. Turn it off and that history is deleted along with everything else.

It is a separate decision from account deletion, and it is the only part of your data that outlives the account, so it is worth making deliberately. Note that it is **on by default** — a deletion made without visiting this switch leaves the de-identified copy behind.

## What Cora stores

The full detail is in the [privacy policy](/privacy-policy.html). In short: your tank data, your account, and the sign-ins for any equipment you connected through a manufacturer's account.

Removing a device forgets that sign-in. Deleting your account removes everything held against you — with the two exceptions above: the anonymised research copy, if you left that switch on, and your store subscription, which only the store can cancel.

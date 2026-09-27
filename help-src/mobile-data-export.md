---
title: Your data
description: Export your readings, journal and alerts as spreadsheets, and delete your account if you want to.
section: Cora Mobile
reviewed: 2026-09-27
order: 30
group: Account
---

Your tank records belong to you, and you can take them out whenever you like.

![Account data controls](img/mobile-data.webp "Export and deletion sit together at the foot of Account & Subscription.")

## Exporting

**Settings → your account → Export My Data.**

Exporting is **free on every plan**, including the free one.

Cora exports **CSV files**. They're spreadsheets that open in Excel, Numbers, Google Sheets or anything else that reads a table.

| File | Contains |
|---|---|
| `cora_parameters.csv` | Your readings, each with its source and timestamp |
| `cora_journal.csv` | Your journal entries |
| `cora_alerts.csv` | Alerts raised |
| `cora_export_summary.csv` | What this export covers, including anything that was cut short |

:::note What's in the export
It covers **readings, journal entries and alerts**, the three records people ask for. It isn't a copy of your whole account. Dashboards, livestock, maintenance, automations, reports and device settings aren't included.

Each of the three stops at **25,000 rows per tank**. A tank logging thirty metrics every five minutes writes more than that in three days, so a long-running tank will hit the cap. The summary file tells you when that's happened. Check it before you assume the export is complete.
:::

The parameter export includes the **source** of each reading. So in a spreadsheet of your alkalinity, you can still tell what your probe said from what your test kit said.

:::note Export before big changes
Take an export before you shut down a tank or make big changes to your setup. The files don't depend on Cora Mobile or your account.
:::

## Signing out versus deleting

**Sign Out** disconnects this device from your account. Your data isn't touched, and signing back in brings everything back.

**Delete account** is permanent.

## Deleting your account

**Settings → your account → Delete account.**

This is permanent. It removes your account, tanks, readings, journal, lab results and device links. You can't undo it, and there's no grace period.

If you want to keep anything, export it first.

:::warning Deleting doesn't cancel your subscription
An App Store or Google Play subscription belongs to the **store**. Deleting your account removes your record with Cora, but **the billing doesn't stop**. You'll keep being charged until you cancel with Apple or Google yourself. Cancel there first, then delete.
:::

## Contributing anonymised data

**Settings → Cora Assistant → Contribute anonymized tank data.**

While this is on, your tank's parameter history is kept for reef research **with no link to you**, even if you later delete your account. Turn it off and that history is deleted with everything else.

This is a separate choice from deleting your account. It's the only part of your data that outlives the account, so give it some thought. It's **on by default**. If you delete your account without checking this switch, the de-identified copy stays behind.

## What Cora stores

The [privacy policy](/privacy-policy.html) has the full detail. Briefly, Cora stores your tank data, your account, and the sign-ins for any equipment you connected through a manufacturer's account.

Removing a device forgets its sign-in. Deleting your account removes everything held under your name, with the two exceptions above. Those are the anonymised research copy, if you left that switch on, and your store subscription, which only the store can cancel.

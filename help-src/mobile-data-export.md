---
title: Exporting your data and deleting your account
description: Export your readings, journal and alerts as spreadsheet files, sign out, or delete your Cora account and what that removes.
section: Cora Mobile
reviewed: 2026-10-13
order: 39
group: Settings and account
---

Your tank records belong to you. This page shows how to export them, and how to delete your account if you want to.

![Export My Data and Delete Account in Cora Mobile](img/mobile-data.webp "Settings, then your account: Export My Data and Delete Account sit below Sign Out.")

## Exporting {#exporting}

1. Open **Settings** and tap the account card at the top. **Account & Subscription** opens.
2. Tap **Export My Data**.

Exporting is **free on every plan**, including the free one.

Cora exports **CSV files**. They're spreadsheets that open in Excel, Numbers, Google Sheets or anything else that reads a table.

| File | Contains |
|---|---|
| `cora_parameters.csv` | Your readings, each with its source and timestamp |
| `cora_journal.csv` | Your journal entries |
| `cora_alerts.csv` | Your notification history |
| `cora_export_summary.csv` | What this export covers, including anything that was cut short |

:::note What's in the export
It covers **readings, journal entries and alerts**, the three records people ask for. It isn't a copy of your whole account. Dashboards, livestock, maintenance, automations, reports and device settings aren't included.

Readings and journal entries stop at **25,000 records per tank**, and the alerts file stops at 25,000 for the whole account. A tank with years of history can reach the cap. The summary file tells you when that's happened. Check it before you assume the export is complete.
:::

The parameter export includes the **source** of each reading. So in a spreadsheet of your alkalinity, you can still tell what your probe said from what your test kit said.

:::note Export before big changes
Take an export before you shut down a tank or make big changes to your setup. The files don't depend on Cora Mobile or your account.
:::

## Signing out versus deleting

**Sign Out** disconnects this phone from your account. Your data isn't touched, and signing back in brings everything back.

**Delete Account** is permanent.

## Deleting your account {#deleting-your-account}

:::warning Deleting doesn't cancel your subscription
An App Store or Google Play subscription belongs to the **store**. Deleting your account removes your record with Cora, but **the billing doesn't stop**. You'll keep being charged until you cancel with Apple or Google yourself. Cancel there first, then delete. See [Cancelling](/help/mobile-plans#cancelling).
:::

1. If you want to keep anything, [export it](#exporting) first.
2. Open **Settings**, tap the account card, then **Delete Account**.
3. Read the confirmation. If you have a store subscription, it has a **Manage subscription** button so you can cancel first.
4. Tap **Delete**.

This removes your account, tanks, readings, journal, lab results and device links. You can't undo it, and there's no grace period.

If you signed in a while ago, Cora may ask you to prove it's you before it deletes anything. With an email and password, it asks you to **Confirm your password**. With Apple or Google, sign in with them again. Then try again. Until you do, nothing is deleted.

## Contributing anonymised data {#contributing-anonymised-data}

**Settings → Cora Assistant → Contribute anonymized tank data.**

While this is on, your tank's parameter history is kept for reef research **with no link to you**. That happens when you remove a tank, and when you delete your account. Turn it off and that history is deleted with everything else.

This is a separate choice from deleting your account. It's the only part of your data that outlives the account, so give it some thought. It's **on by default**. If you delete your account without checking this switch, the de-identified copy stays behind.

## What Cora stores

The [privacy policy](/privacy-policy.html) has the full detail. Briefly, Cora stores your tank data, your account, and the sign-ins for any equipment you connected through a manufacturer's account.

Removing a device forgets its sign-in. Deleting your account removes everything held under your name, with these exceptions:

- the anonymised research copy, if you left that switch on
- your store subscription, which only the store can cancel
- your customer record at our subscription management provider, which is deleted 120 days after your account is deleted so a store refund or payment dispute can still be handled

Signing in again on another phone, or changing your sign-in, is covered in [Signing in and account recovery](/help/mobile-account). Plans and billing are in [Plans and subscriptions](/help/mobile-plans).

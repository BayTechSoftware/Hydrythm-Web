---
title: Cameras and Skimmer Watch
description: Add a Wyze, Tapo, Sonoff or other RTSP camera to Cora, watch it on a tile or full screen, and let Skimmer Watch warn you before the skimmer cup overflows.
section: Cora Mobile
reviewed: 2026-10-12
order: 35
group: Equipment
---

:::note Beta
**Beta.** Cameras are in Beta and only open to Beta users. If you are not a Beta user you will not see them in **Add device**. To ask for Beta access, contact [support](/support.html).
:::

Add a camera to see your tank from Cora, on your phone and on Cora Max. A camera needs a Cora Max in the tank, so the **Camera** row shows **Requires Cora Max** until the tank has one.

## Adding a camera

1. Go to **Devices → Add Device → Camera**, then **Add a camera**.
2. Pick the type: Wyze, Tapo, Sonoff or **Other camera (RTSP)**.
3. Follow the steps Cora shows for that type. They tell you what to switch on in the camera's own app first.
4. Fill in the name, stream address, username, password and tank, then tap **Test connection**. When the camera answers, tap **Add camera**.

Your phone must be on the same Wi-Fi as the camera while you add it. The address has to be on your home network, and you enter the username and password in their own fields, not in the address.

Wyze, Tapo and Sonoff cameras have been tested (Wyze Cam v4, Tapo C120 and Sonoff Cam S3W). Other cameras that offer RTSP may work too.

| Camera | Turn this on first |
|---|---|
| Wyze | In the Wyze app, open the camera, then Settings, Advanced Settings, RTSP. Switch RTSP on, choose a username and password, then restart the camera. The camera needs firmware 4.52.17 or newer. |
| Tapo | In the Tapo app, open Settings, Advanced Settings, Camera Account and make a username and password. This isn't your TP-Link account. A Tapo camera can run only two of Tapo Care, SD card recording and streaming to other apps at once. |
| Sonoff | In eWeLink, turn on RTSP for the camera and set its account. Cora fills in a **Sonoff address** preset for you. |
| Other camera (RTSP) | Turn on RTSP or ONVIF in the camera's app, set a camera login, and enter the stream address from its manual. Leave the login empty if your camera has none. |

## Changing a camera

Open the camera and use its menu: **Rename**, **Edit addresses**, **Change password** or **Remove camera**. Removing it also deletes its saved password.

## Watching it

A camera can be a tile on your dashboard, up to 3×2 in size, and you can open it for **Full screen** and **Rotate**.

At home, with your phone on the camera's Wi-Fi, Cora plays **Live video** straight from the camera. Away from home, or when you choose **Snapshots**, your Cora Max takes still pictures from the camera and Cora shows them as near-live, updated every few seconds. If Cora Max isn't sending pictures, the tile says so.

## Skimmer Watch

:::note Beta
**Beta.** Skimmer Watch is in Beta and only open to Beta users. It also needs a paid plan: **Skimmer Watch is part of the paid plans.** To ask for Beta access, contact [support](/support.html).
:::

Skimmer Watch watches the skimmer collection cup through a camera and warns you before it overflows. It lives on the camera's page, in the **Skimmer Watch** card.

1. Point the camera at the cup and turn on **Watch the cup**.
2. Tap **Mark the cup**. Drag the box over the cup and pull the corners to fit it: the bottom edge on the bottom of the cup, the top edge just under the rim, where the cup is full.
3. Empty the cup and tap **Cup is empty now**. Cora takes a picture of the empty cup to compare against. It takes about 10 seconds. If you move the camera or the box, do this again.
4. Set **Alert at** to the fill level that should warn you. The card shows it as a percentage.

Cora Max checks the cup every few minutes. The card shows the last reading and how long ago it was. **Check now** asks for a check straight away, and it takes about 10 seconds. **Last 24 hours** shows how the cup filled over the day.

If the picture is hard to read, the card says so, for example **Light too bright behind the cup**.

### Camera tips

**Camera tips** on the card gives you the same advice as here.

- Set the camera's night vision to On (always infrared), not Auto, so every picture looks the same day and night.
- Set the camera's spotlight to Manual and leave it off. Bubbles and water in the sump count as motion and keep switching it on.
- Keep strong lights from shining straight at the camera from behind the cup.

## What happens to the pictures

At home, video plays straight from the camera and isn't recorded. Away from home, only one still picture per camera is kept, and each new one replaces the last. Skimmer Watch keeps the latest picture of the marked cup, the last 24 hours of fill readings (numbers only) and one small picture of the empty cup. They're deleted when you remove the camera, the tank or your account. The [privacy policy](/privacy-policy.html) has the full detail.

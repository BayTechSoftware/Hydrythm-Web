---
title: Cameras and Skimmer Watch
description: Add a Wyze, Tapo, Sonoff or other RTSP camera to Cora, watch your tank on a tile or full screen, and let Skimmer Watch warn you before the skimmer cup overflows.
section: Cora Mobile
reviewed: 2026-10-13
order: 17
group: Equipment
---

:::note Beta
**Beta.** Cameras are in Beta and only open to Beta users. If you are not a Beta user you will not see them in **Add device**. To ask for Beta access, contact [support](/support.html). More in [Beta features](/help/mobile-beta).
:::

Add a camera to see your tank from Cora, on your phone and on Cora Max, and to let Skimmer Watch keep an eye on the skimmer cup. Start from **Devices → Add Device → Camera**. A camera needs a Cora Max in the tank, so the **Camera** row shows **Requires Cora Max** until the tank has one.

## Adding a camera {#adding-a-camera}

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

## Changing a camera {#changing-a-camera}

Open the camera and use its menu: **Rename**, **Edit addresses**, **Change password** or **Remove camera**. Removing it also deletes its saved password.

## Watching it {#watching-it}

![A camera page](img/mobile-camera.webp "The camera page, with the picture at the top and the Skimmer Watch card below.")

A camera can be a tile on your dashboard, up to 3×2 in size. See [Editing your dashboard](/help/mobile-dashboard-editing). Open it for **Full screen** and **Rotate**.

At home, with your phone on the camera's Wi-Fi, Cora plays **Live video** straight from the camera. Away from home, or when you choose **Snapshots**, your Cora Max takes still pictures from the camera and Cora shows them as near-live, updated every few seconds. If Cora Max isn't sending pictures, the tile says so.

## Skimmer Watch {#skimmer-watch}

:::note Beta
**Beta.** Skimmer Watch is in Beta and only open to Beta users. It also needs a paid plan. Without one, the card says **Skimmer Watch is part of the paid plans.** and offers **See plans**. To ask for Beta access, contact [support](/support.html).
:::

Skimmer Watch watches the skimmer collection cup through a camera and warns you before it overflows. It lives on the camera's page, in the **Skimmer Watch** card.

![Marking the cup](img/mobile-camera-mark-cup.webp "Drag the box over the cup: bottom edge on the bottom of the cup, top edge just under the rim.")

1. Point the camera at the cup and turn on **Watch the cup**.
2. Tap **Mark the cup**. Drag the box over the cup and pull the corners to fit it: the bottom edge on the bottom of the cup, the top edge just under the rim, where the cup is full. Later the button reads **Move the cup box**.
3. Empty the cup and tap **Cup is empty now**. Cora takes a picture of the empty cup to compare against. It takes about 10 seconds. If you move the camera or the box, do this again.
4. Drag the **Alert at** slider to the fill level that should warn you. Leave some margin, because Cora checks every 15 minutes.

![The Skimmer Watch card on a camera page](img/mobile-skimmer-watch.webp "Cup is empty now, the last reading, the last 24 hours, Check now and the camera tips.")

Cora Max checks the cup every 15 minutes. The card shows the last reading and how long ago it was, and the camera tile on your dashboard shows the cup level too. **Check now** checks the cup now, which takes about 10 seconds. **Last 24 hours** shows how the cup filled over the day.

When the cup reaches your **Alert at** level, you get one notification. It's sent under **Equipment Faults**, so keep that category on in [Notifications](/help/mobile-notifications). Once you've emptied the cup, the alert is ready to fire again.

### If the reading looks wrong {#skimmer-watch-problems}

| The card says | What to do |
|---|---|
| **Light too bright behind the cup** | Turn off or move the light behind the cup. See the camera tips below |
| **Not sure (low confidence)** | The picture was hard to read. Check the camera tips, then tap **Check now** |
| **Mark the cup first** | Tap **Mark the cup** and draw the box |
| **Not calibrated: empty the cup and tap Cup is empty now** | Empty the cup, then tap **Cup is empty now** |
| **Box moved: calibrate again** | You moved the box. Empty the cup and tap **Cup is empty now** again |
| **Cora Max could not get a picture of the camera.** | Check that the camera is on and that the tank's Cora Max is online |
| **The last check failed.** | Tap **Check now**. If it keeps failing, see [Troubleshooting](/help/troubleshooting) |
| **No reading yet. Cora Max checks every 15 minutes.** | Wait for the first check, or tap **Check now** |

### Camera tips {#camera-tips}

**Camera tips** on the card gives you the same advice as here.

- Set the camera's night vision to On (always infrared), not Auto, so every picture looks the same day and night.
- Set the camera's spotlight to Manual and leave it off. Bubbles and water in the sump count as motion and keep switching it on.
- Keep strong lights from shining straight at the camera from behind the cup.

### On Cora Max {#skimmer-watch-on-cora-max}

![Camera tiles on Cora Max, one showing the skimmer cup level](img/max-skimmer-watch.webp "On Cora Max, the camera tile shows the cup level and how old it is.")

On Cora Max, the camera tile and the full-screen camera show **Cup** with the fill level and how old the reading is. The chip turns amber when the cup is within 10 points of your alert level and red when it reaches it. On the full-screen camera, the **Alert at** button opens **Skimmer cup alert**, where you can change the level too. While a check runs, the live picture may pause for a few seconds. More in [Controlling equipment from Cora Max](/help/max-device-control).

## What happens to the pictures {#pictures}

At home, video plays straight from the camera and isn't recorded. Away from home, only one still picture per camera is kept, and each new one replaces the last. Skimmer Watch keeps the latest picture of the marked cup, the last 24 hours of fill readings (numbers only) and one small picture of the empty cup. They're deleted when you remove the camera or delete your account. The [privacy policy](/privacy-policy.html) has the full detail.

---
title: WLED-Setup
aliases: [M-1 setup, M-1 wifi setup, WLED setup, connect M-1 to wifi, Apollo M-1 hotspot, add M-1 to Home Assistant, update M-1 WLED, upgrade WLED-MM to WLED]
type: guide
audience: customer
applies_to: ["[[M-1]]"]
sources:
  - https://wiki.apolloautomation.com/products/m1/setup/getting-started-m1/
  - https://wiki.apolloautomation.com/products/m1/faq/
  - https://wiki.apolloautomation.com/products/m1/choose-your-firmware/
  - https://wiki.apolloautomation.com/products/m1/setup/m1-matrix-settings/
  - https://wiki.apolloautomation.com/products/m1/setup/use-without-wifi/
  - https://wiki.apolloautomation.com/products/m1/setup/upgrade-to-wled/
  - https://wiki.apolloautomation.com/products/m1/troubleshooting/m1-find-ip-address-and-hostname/
  - https://wiki.apolloautomation.com/products/m1/troubleshooting/m1-boot-mode/
  - https://wiki.apolloautomation.com/products/m1/troubleshooting/m1-reflash/
  - https://wiki.apolloautomation.com/products/led1/introduction/
  - https://www.home-assistant.io/integrations/wled/
  - https://github.com/ApolloAutomation/WLED-M1/releases
review_status: draft
last_verified: 2026-11-17
---
# WLED-Setup

## Summary

How to set up an M-1 LED Matrix running WLED: attach the controller, join the "Apollo M-1" hotspot, put the M-1 on your home Wi-Fi, add it to Home Assistant, and update older WLED-MM units to WLED.

## Applies to

- [[M-1]] running WLED (16.0.1 or newer, ships on new units) or WLED-MM (14.5.1, units shipped earlier).
- If your M-1 runs ESPHome or Game Day Scoreboard firmware instead, see https://wiki.apolloautomation.com/products/m1/choose-your-firmware/
- [[LED-1]]: the LED-1 also runs WLED and joins Home Assistant through the WLED integration, but we don't have published setup or update steps for it yet. Contact support for LED-1 setup help.

## Before you start

- **Power:** 5V 3A over USB-C with the stock power supply covers one 64x64 panel. Each extra panel needs its own power module.
- **Check which firmware you have:** open the M-1 in a browser and tap **Info**. The version is at the top:
  - **16.0.1 or newer:** WLED.
  - **14.5.1:** WLED-MM.
- **Check your controller revision** if you plan to update: it is printed on the back of the controller board (Rev4 or Rev6). WLED 16.0.1 needs a Rev6 controller.

## Steps

### 1. Attach the controller

1. The controller and the LED Matrix ship separately. Line up the controller's power and data headers with the back of the LED Matrix panel and press it on gently.

### 2. Connect to the M-1 hotspot

1. Plug in USB-C power. The M-1 shows a picture of Apollo, our mascot, then a setup card on the panel.
2. On your phone or computer, join the Wi-Fi network **Apollo M-1**. It is an open network with no password.
   - On builds older than 16.0.1, the network name has a serial number added to the end.
3. If your phone asks about Wi-Fi connection options or warns there is no internet, choose **Always Connect** (or stay connected).
4. Scan the QR code on the panel, or open `4.3.2.1` in a browser such as Firefox, Chrome or Safari.
5. You should see the **Welcome to WLED** page.
   - A small WLED window may open by itself. That is the captive portal. If a control is missing or does nothing in it, open `4.3.2.1` in a full browser instead.

To use the M-1 without a home network, select **TO THE CONTROLS** and control it over its own hotspot. Details, including how to set a hotspot password: https://wiki.apolloautomation.com/products/m1/setup/use-without-wifi/

### 3. Put the M-1 on your home Wi-Fi

1. On the Welcome page, select **WIFI SETTINGS**.
2. Enter your network and password. Passwords are case sensitive.
   - **WLED:** select **Scan**, then select your network and enter your password.
   - **WLED-MM:** type your network name where it shows `Your_Network`, and your password directly below it.
3. Set the **mDNS address** (hostname), for example `apollo-led-matrix`. Use only lowercase letters, numbers and dashes. Don't skip this step; it saves you from having to find the IP address later. If you have several M-1s, give each one a different name.
4. Select **Save & Connect**.
   - **WLED:** wait a few seconds, then unplug the M-1 and plug it back in.
5. From any device on your network, open `apollo-led-matrix.local` (or the name you chose).
   - `4.3.2.1` stops working once the M-1 is on your Wi-Fi. That address only works while you are connected to the M-1's own hotspot.
   - If the M-1 can't join your network, it goes back to broadcasting the Apollo M-1 hotspot. Check the network name and password and repeat these steps.

### 4. Check the matrix settings (WLED-MM only)

Units shipped on WLED arrive already set up for one 64x64 panel, so skip this on WLED. On WLED-MM (14.5.1), these settings are required or the panel won't display correctly:

1. Click **Config**, then **LED Preferences**. Select **Hub75Matrix 64x64**, set **Chain Length** to `1`, uncheck **enable automatic brightness limiter**, and click **Save**.
2. Click **Config**, then **2D Configuration**. Select **2D Matrix**, click the circle next to **Basic**, set **Panel dimensions (WxH)** to `64 x 64`, and click **Save**.

If you reflashed or wiped a WLED unit, the WLED settings are listed at https://wiki.apolloautomation.com/products/m1/setup/m1-matrix-settings/

### 5. Add the M-1 to Home Assistant

1. Open your integrations page in Home Assistant. The WLED integration discovers the M-1 automatically.
2. Click **Add**, then **Submit**.
3. Give it a name and an area, then click **Finish** (on WLED-MM, click **Skip and Finish**).
4. Open the WLED integration page and select your M-1 to change colors, pick effects and run presets.

If the M-1 is not discovered, add it by hand: go to **Settings > Devices & services**, select **Add Integration**, choose **WLED**, and enter the M-1's hostname (e.g. `apollo-led-matrix.local`) or IP address in the **Host** field.

### 6. Update a WLED-MM 14.5.1 unit to WLED (Rev6 only)

Rev6 controllers on WLED-MM 14.5.1 should update to WLED. The update is over the air and keeps your Wi-Fi settings, presets and uploaded files. **Rev4 controllers must stay on WLED-MM 14.5.1.**

1. **Back up first.** Open your M-1 in a browser, click **Config**, then **Security & Updates**. Under **Backup & Restore**, download both the **presets** and the **configuration** files and keep them somewhere safe.
2. Download **M-1_ota.bin** from the latest release at https://github.com/ApolloAutomation/WLED-M1/releases. Use this file, not the full install image.
3. On the **Security & Updates** page, find **Manual OTA Update**, click **Browse**, select `M-1_ota.bin`, and click **Update!**
4. Let the M-1 finish and reboot on its own. Don't unplug it during the update.
5. Tap **Info** and check the version reads 16.0.1.
6. Go to **Config**, then **LED Preferences**, and check the panel settings. WLED describes HUB75 panels as a grid instead of a chain length; for a single panel see https://wiki.apolloautomation.com/products/m1/setup/m1-matrix-settings/
7. The display stays black after any HUB75 change until you reboot. To reboot, tap **Info**, scroll down, select **Reboot WLED**, and tap again to confirm.
8. Your presets are kept, but any that used WLED-MM-only effects will switch to a different effect.

Already on WLED 16.0.1? To install a newer Apollo build, use the same **Manual OTA Update** steps with `M-1_ota.bin` from the latest release.

**Don't use the update prompt in the WLED phone app.** Installing the update behind the red badge in the app will break your M-1's configuration. Only update with Apollo's files from the steps above or the Apollo installer.

## If it doesn't work

- **Half the screen shows color, or Scrolling Text is missing:** the matrix settings need to be set. This is not a fault. Follow https://wiki.apolloautomation.com/products/m1/setup/m1-matrix-settings/ and pick your firmware tab (on WLED-MM, this is the same as step 4).
- **Vertical lines across the panel:** reseat the controller on the back of the matrix.
- **Can't find the M-1 on your network:** use the WLED Native app (iOS or Android) on the same Wi-Fi as the M-1. Select the M-1, tap **Config**, then **WiFi Setup**; the hostname (ending in `.local`) and the IP address are shown at the bottom. Full steps: https://wiki.apolloautomation.com/products/m1/troubleshooting/m1-find-ip-address-and-hostname/
- **Factory reset:**
  - On WLED: hold the button for ten seconds. This restores every factory setting, including the display size. Then reconnect it to Wi-Fi.
  - On WLED-MM: a reset does not restore the display settings, so use a factory re-flash instead.
- **M-1 unresponsive (including after the WLED update):** do a factory re-flash over USB. This wipes the device, so back up first if you can. See also [[Boot-Mode]] and [[Factory-Reflash]].
  1. Use Chrome, Edge or another Chromium browser (recent Firefox also works) and a USB cable that carries power and data.
  2. Plug the cable into your computer. Press and hold the boot button (the **left** button on the M-1 controller), plug the USB-C cable into the M-1, then release the button.
  3. Open https://install.apolloautomation.com/#/m-1 and choose your firmware:
     - **WLED 16.0.1** (default, needs a Rev6 controller).
     - **WLED-MM 14.5.1 (Rev6)** or **WLED-MM 14.5.1 (Rev4)**, matching the revision printed on the back of your controller.
  4. Click **Connect**, then **Install**. Allow serial port access when the browser asks and select your M-1.
  5. Tick **Erase device**, click **Next**, then **Install**. Don't unplug during the install.
  6. When you see "Installation complete!", click **Next** and close the browser window.
  7. Fully unplug the M-1 and plug it back in. It stays in boot mode until you do.
  8. Set the M-1 up again from step 2. If you made a backup, restore only the **presets** file under **Config > Security & Updates > Backup & Restore**. Don't restore the old configuration file after moving from WLED-MM to WLED; it can leave panel settings that don't match.
- **When to contact support:** the M-1 still doesn't respond after a factory re-flash, the computer never sees it in boot mode, the hardware looks damaged, you need LED-1 setup help, or you have a warranty or return question.

## Customer phrasings

- "I can't find the Apollo M-1 Wi-Fi network / how do I connect my matrix?"
- "My M-1 only lights up half the screen after setup."
- "4.3.2.1 doesn't load anymore after I put it on my Wi-Fi."
- "Home Assistant didn't find my LED matrix."
- "How do I update my M-1 from WLED-MM to the new WLED?"
- "The WLED app says there's an update, should I install it?"

---
title: Firmware-Updates
aliases: [update firmware, OTA update, firmware update, beta firmware, firmware channel, update not showing, how do I update my sensor]
type: guide
audience: customer
applies_to: ["[[AIR-1]]", "[[BTN-1]]", "[[CAST-1]]", "[[CAST-PRO-1]]", "[[MSR-2]]", "[[MTR-1]]", "[[PLT-1]]", "[[PUMP-1]]", "[[R-PRO-1]]", "[[TEMP-1]]"]
sources:
  - https://wiki.apolloautomation.com/products/general/calibrating-and-updating/updating-firmware/
  - https://wiki.apolloautomation.com/products/general/setup/switch-to-beta-branch/
  - https://wiki.apolloautomation.com/products/general/troubleshooting/firmware-updates-not-appearing/
  - https://wiki.apolloautomation.com/products/general/battery-sensors/prevent-sleep/
  - https://wiki.apolloautomation.com/products/general/setup/getting-started/
  - https://wiki.apolloautomation.com/products/castpro1/faq/
review_status: draft
last_verified: 2026-11-17
---
# Firmware-Updates

## Summary

Most Apollo devices update themselves over the air from Home Assistant, with no computer or cable needed. The **Firmware Update** entity shows when a new version is available and installs it wirelessly. The **Firmware Channel** setting picks between Stable (the default) and Beta firmware. If you have taken control of your device in ESPHome Device Builder, you update it from Device Builder instead.

## Applies to

- [[AIR-1]], [[BTN-1]], [[CAST-1]], [[CAST-PRO-1]], [[MSR-2]], [[MTR-1]], [[PLT-1]] (including PLT-1B), [[PUMP-1]], [[R-PRO-1]], [[TEMP-1]] (including TEMP-1B)
- Devices that sleep install updates only while they are awake. All battery-powered devices sleep (BTN-1 battery version, PLT-1B, TEMP-1B), and the AIR-1, PLT-1 and TEMP-1 can be set to sleep too. See "Battery and sleeping devices" below.

## Before you start

- The device must be added to Home Assistant through the ESPHome integration.
- The device needs outbound internet access over HTTPS (port 443) to `apolloautomation.github.io`. This is where it checks for new firmware.
- If you plan to use ESPHome Device Builder, update ESPHome Device Builder first.

## Steps

### Update from Home Assistant (most devices)

1. In Home Assistant, go to **Settings > Devices & services > ESPHome** and open your device.
2. Find the **Firmware Update** entity. It shows when a new version is available.
3. Install the update:
   - If there is a **Press** button next to **Firmware Update**, select it.
   - If there is only a **Firmware Update** entity, select it and choose **Install** once the new version appears.
4. Wait about a minute while the device installs the update and restarts. It is finished when **Firmware Update** shows **Up-to-date**.

### Battery and sleeping devices

1. Start the update the same way as above. The device installs it the next time it wakes.
2. If no update appears, keep the device awake: on the device page in Home Assistant, scroll down to **Prevent Sleep** and turn it on. See [[Battery-and-Sleep]] for how to wake a sleeping device.
3. Reboot the device once, then check **Firmware Update** again.
4. When you are done, turn **Prevent Sleep** off. The device starts sleeping right away.

### Switch between Stable and Beta firmware

Stable is the tested release and the default. Beta gets new features and fixes sooner, with more risk of rough edges. You can switch at any time.

1. Go to **Settings > Devices & services > ESPHome** and open your device.
2. Under **Configuration**, set **Firmware Channel** to **Beta**.
3. Select **Press** next to **Firmware Update**. If there is no **Press** button, select **Firmware Update** and choose **Install** once the beta version appears.
4. Wait about a minute. It is finished when **Firmware Update** shows **Up-to-date**.

To go back to Stable, set **Firmware Channel** to **Stable** and select **Press** next to **Firmware Update** again. The device installs the current stable release, even if it is older than the beta you were on.

If your device has no **Firmware Channel** setting, see the full Beta guide, which covers switching with ESPHome Device Builder: https://wiki.apolloautomation.com/products/general/setup/switch-to-beta-branch/

### Update with ESPHome Device Builder

Use this if you have taken control of the device in ESPHome Device Builder (see [[Add-to-Home-Assistant]]), if you build the firmware yourself, or if your device has no **Firmware Update** entity.

1. In Home Assistant, open **ESPHome Device Builder**. Make sure ESPHome is up to date first.
2. Find your device and click the three dots on the far right of its card.
3. Select **Validate**.
4. When validation finishes, click **Install** in the bottom right.
5. Click **Wirelessly**.
6. Wait for the log to show `INFO OTA successful`, then click **STOP**.

### What changes after you take control

Once you have taken control of a device in ESPHome Device Builder, Home Assistant handles its updates through Device Builder, not through the Apollo **Firmware Update** entity. This is expected. Build and install updates from Device Builder using the steps above.

## If it doesn't work

- **Firmware Update says up to date, but a newer release exists:** the device may not be able to reach `apolloautomation.github.io`. This is common on an isolated IoT VLAN that blocks outbound traffic. Check the device logs (Logs in ESPHome Device Builder, or the device's web page). A blocked check logs `Failed to fetch manifest` with `ESP_ERR_HTTP_CONNECT`. Allow outbound HTTPS on port 443 to `apolloautomation.github.io` in your firewall, then reboot the device.
- **Still stale after a reboot:** older firmware can skip its first check if Wi-Fi wasn't connected yet at boot, and then waits about 6 hours for the next one. Wait, reboot once more while the network is up, or update to the latest release.
- **Battery or sleeping device shows no update:** turn on **Prevent Sleep** and reboot it once (see "Battery and sleeping devices" above).
- **Device Builder build fails with a `min_version` error:** update ESPHome Device Builder. Each Apollo release requires a minimum ESPHome version.
- Full troubleshooting guide: https://wiki.apolloautomation.com/products/general/troubleshooting/firmware-updates-not-appearing/
- If the device stops working after an update, a factory reflash can restore it (see [[Factory-Reflash]]). If none of this helps, contact Apollo support at support@apolloautomation.com with your device model and what the device log shows.

## Customer phrasings

- "How do I update the firmware on my sensor?"
- "Home Assistant says my device is up to date but there's a newer version."
- "How do I get the beta firmware, and how do I go back to stable?"
- "I took control in ESPHome and now the update button is gone."
- "My battery sensor never installs the update."
- "ESPHome says min_version when I try to install."

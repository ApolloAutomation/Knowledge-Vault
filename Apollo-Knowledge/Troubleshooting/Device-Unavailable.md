---
title: Device-Unavailable
aliases: [device unavailable, sensor offline, keeps disconnecting, keeps going unavailable, device keeps restarting, entities unavailable, lost connection to home assistant]
type: troubleshooting
audience: customer
applies_to: ["[[AIR-1]]", "[[BTN-1]]", "[[CAST-1]]", "[[CAST-PRO-1]]", "[[ESK-1]]", "[[MSR-2]]", "[[MTR-1]]", "[[PLT-1]]", "[[PUMP-1]]", "[[R-PRO-1]]", "[[TEMP-1]]"]
sources:
  - https://wiki.apolloautomation.com/products/general/troubleshooting/connection-issues/
  - https://wiki.apolloautomation.com/products/general/setup/getting-started/
  - https://wiki.apolloautomation.com/products/general/setup/getting-started-msr2/
  - https://wiki.apolloautomation.com/products/general/faq/
  - https://wiki.apolloautomation.com/products/general/battery-sensors/prevent-sleep/
  - https://wiki.apolloautomation.com/products/general/battery-sensors/wake-up-battery-sensor/
  - https://wiki.apolloautomation.com/products/general/battery-sensors/awake-ha-helper/
  - https://wiki.apolloautomation.com/products/ESPHome-Starter-Kit/modules/battery/
  - https://wiki.apolloautomation.com/products/general/troubleshooting/removing-device-from-home-assistant/
  - https://wiki.apolloautomation.com/products/general/troubleshooting/ubiquiti-unifi-mdns-auto-discover-issue/
  - https://wiki.apolloautomation.com/products/air1/faq/
  - https://www.home-assistant.io/integrations/esphome/
review_status: draft
last_verified: 2026-11-17
---
# Device-Unavailable

## Summary

When Home Assistant shows an Apollo device as **Unavailable**, it has lost its connection to the device. Common causes are a low-quality power supply, a weak Wi-Fi connection, the device having lost its Wi-Fi settings, or the device's IP address changing. Battery and sleep-enabled devices also drop off Wi-Fi while they sleep, which is normal. Work through the quick checks first, then the fix that matches what you see.

## Applies to

- [[AIR-1]], [[BTN-1]], [[CAST-1]], [[CAST-PRO-1]], [[ESK-1]], [[MSR-2]], [[MTR-1]], [[PLT-1]] (including PLT-1B), [[PUMP-1]], [[R-PRO-1]], [[TEMP-1]] (including TEMP-1B)
- Sleep mode applies to AIR-1, BTN-1, PLT-1, PLT-1B, TEMP-1, TEMP-1B and an ESK-1 set up with a battery and deep sleep.

## Symptoms

- The device and all its entities show **Unavailable** in Home Assistant.
- The device goes unavailable and comes back on its own, over and over.
- The device keeps restarting.
- A battery device is only available for short periods, then goes unavailable again.

## Quick checks

1. **Power supply.** Apollo sensors need 5V and draw 1A or less (some 350-500 mA), so most phone chargers work. Very cheap power bricks can make a device restart or go unavailable. Try a different power brick and a different USB-C cable.
   - [[MTR-1]] with the back USB-C wall-plug adapter: some wall plugs and outlets with smart charging don't work with it. Use a basic wall plug without smart charging.
   - [[R-PRO-1]] can also run on PoE (802.3af). If it is on PoE, try USB-C power to rule out the PoE port.
2. **Is the device's hotspot showing?** Look at the Wi-Fi list on your phone or computer. If you see the device's hotspot (named like "Apollo MSR2 Hotspot"), the device is not connected to your Wi-Fi. Go to "Reconnect the device to Wi-Fi" below.
   - Not every device uses a hotspot. [[ESK-1]] is set up in ESPHome Device Builder, and a [[CAST-1]] or [[CAST-PRO-1]] never shows its hotspot while an Ethernet cable is plugged in.
3. **Is it on your network?** Check your router's list of connected devices. Apollo devices show up with their Apollo name followed by the last 6 characters of their MAC address.
4. **Is it a device that sleeps?** See "Battery devices and sleep" below.

## Fix

### Power problems

1. Plug the device into a different, good-quality 5V power brick.
2. Use a different USB-C cable.
3. Watch the device in Home Assistant. If it no longer restarts or drops off, the old power supply was the cause.

### Reconnect the device to Wi-Fi

Use this if the device's hotspot is showing.

1. Connect your phone or computer to the device's hotspot. It can take a minute to appear.
2. The setup page should open on its own. If it doesn't, open a browser and go to `192.168.4.1` (on the CAST-1 and CAST PRO-1, `192.168.4.1/setup`).
3. Select your Wi-Fi network or type its name in, enter the password, and click **Save**. If you have a mesh system or several access points, type your network name in by hand so the device joins the strongest signal.
4. Full walkthrough: https://wiki.apolloautomation.com/products/general/setup/getting-started/ . See also [[Wi-Fi-Setup]] and [[Wont-Connect-to-Wi-Fi]].

If the device is on the wrong network or you changed your Wi-Fi password, reset its Wi-Fi settings first: with the device plugged in, hold the **BOOT** button for 10 seconds. It clears its Wi-Fi settings and the hotspot comes back.

### Weak Wi-Fi or frequent disconnects

The device's Wi-Fi uses a power-saving mode by default, and power saving can cause disconnects from the router. Turning it off gives the most reliable connection. This requires editing the device in ESPHome Device Builder.

1. In Home Assistant, open the ESPHome Device Builder app from the sidebar.
2. Click **Edit** on your device.
3. Under the `wifi:` section, add this line, indented to match the other lines in that section (add a `wifi:` line if there isn't one):

   ```yaml
   wifi:
     power_save_mode: none
   ```

4. Click **Save**, then **Install**.

Note: with power saving off, the device runs warmer inside, which can raise its temperature reading.

### The device's IP address changed

If the device's IP address changed and Home Assistant can't reach it, point Home Assistant at the new address.

1. Find the device's current IP address in your router's list of connected devices (Apollo name plus the last 6 characters of its MAC address).
2. In Home Assistant, go to **Settings > Devices & services > ESPHome**.
3. Use the **Reconfigure** option for the device and enter the new IP address.

If you use UniFi, check that **Multicast DNS** is turned on for your network so Home Assistant can find devices automatically: https://wiki.apolloautomation.com/products/general/troubleshooting/ubiquiti-unifi-mdns-auto-discover-issue/ . If Home Assistant and your devices are on different networks, mDNS must work across both networks and your firewall must allow traffic between them.

### Encryption (AIR-1)

AIR-1 firmware 26.7.23.1 and later encrypts the connection to Home Assistant automatically. You don't need to set anything up or change anything. If Home Assistant asks for an encryption key or shows an authentication error, contact Apollo support.

### Remove and re-add the device

1. If you took control of the device in ESPHome Device Builder: open ESPHome Device Builder, open the three-dot menu on the device, select **Delete**, then confirm with **Delete**. Skip this step if you never used ESPHome Device Builder.
2. Go to **Settings > Devices & services > ESPHome**, open the three-dot menu next to the device, and select **Delete**.
3. Add the device again: click the **Notifications** bell in the Home Assistant sidebar, click **Check it out**, click **Add** on the discovered device, then **Submit**. See [[Add-to-Home-Assistant]]. Full steps: https://wiki.apolloautomation.com/products/general/setup/getting-started/#connecting-to-home-assistant-via-esphome-integration

### Battery devices and sleep

A sleeping device turns off its Wi-Fi between wake-ups, so Home Assistant can show it as unavailable until it next wakes. This is normal and saves battery. See [[Battery-and-Sleep]].

Default sleep times:
- AIR-1: 5 minutes
- PLT-1: 5 minutes
- TEMP-1: 8 minutes
- BTN-1: 24 hours
- PLT-1B: 12 hours
- TEMP-1B: 12 hours

To wake the device:
- **TEMP-1B and PLT-1B:** press the **RESET** button. The BOOT button can't wake it.
- **BTN-1:** press **RESET** (left) or any of buttons 1 to 4. The BOOT (right) button can't wake it. A press on buttons 1 to 4 is sent to Home Assistant as a click once the BTN-1 reconnects, so any automation tied to that button will run. Use **RESET** if you only want to wake it.
- **AIR-1, PLT-1 and TEMP-1 on USB power:** unplug the device and plug it back in.

To keep it awake (for example, while updating or setting it up):
1. In Home Assistant, go to **Settings > Devices & services > ESPHome** and click the device's name.
2. Turn on **Prevent Sleep** on the **Configuration** card.
3. Or, once the device is awake, hold **BOOT** for 4-5 seconds, then release. Do not hold it for 10 seconds or more, which factory-resets the device and erases its Wi-Fi settings. Do not hold BOOT while pressing RESET, which puts the device into flashing mode ([[Boot-Mode]]).

When you're done, turn **Prevent Sleep** off. The device goes to sleep right away. To keep battery devices awake for updates without doing this by hand, see https://wiki.apolloautomation.com/products/general/battery-sensors/awake-ha-helper/

**ESK-1 with a battery:** an ESK-1 using deep sleep also shows unavailable between wake-ups. If you added the **Prevent Sleep** switch from the battery guide, turn it on while the device is awake to keep it awake for updates. You can also plug in the USB-C cable and flash over the wire.

## When to escalate

Hand the ticket to a person if:
- The device stays unavailable with a known-good power supply, its hotspot never appears, and it does not show in the router's device list.
- The device keeps restarting even on a different power supply and cable.
- A battery device never wakes after pressing RESET with a fresh, correctly inserted battery.
- The device has physical damage, gets hot, smells burnt, or got wet.
- The device is still unavailable after a factory reflash ([[Factory-Reflash]]).
- The customer asks about a warranty claim, return or replacement.
- Home Assistant asks for an encryption key or reports an authentication error.

## Customer phrasings

- "My sensor shows unavailable in Home Assistant."
- "My device keeps going offline and coming back."
- "It keeps disconnecting from Wi-Fi."
- "My battery sensor is unavailable most of the time."
- "The sensor keeps restarting."
- "I changed my router and now the device is offline."

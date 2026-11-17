---
title: Wont-Connect-to-Wi-Fi
aliases: [won't connect to Wi-Fi, can't connect to wifi, hotspot not showing, no hotspot, Wi-Fi keeps dropping, reset Wi-Fi, mesh network, hidden network, wifi not working]
type: troubleshooting
audience: customer
applies_to: ["[[MSR-2]]", "[[MTR-1]]", "[[R-PRO-1]]", "[[AIR-1]]", "[[TEMP-1]]", "[[PLT-1]]", "[[PUMP-1]]", "[[BTN-1]]", "[[CAST-1]]", "[[CAST-PRO-1]]", "[[M-1]]"]
sources:
  - https://wiki.apolloautomation.com/products/general/troubleshooting/connection-issues/
  - https://wiki.apolloautomation.com/products/general/setup/getting-started/
  - https://wiki.apolloautomation.com/products/general/setup/getting-started-rpro1/
  - https://wiki.apolloautomation.com/products/general/setup/adding-apollo-devices-to-hidden-networks/
  - https://wiki.apolloautomation.com/products/general/setup/adjusting-wifi-power/
  - https://wiki.apolloautomation.com/products/general/faq/
  - https://wiki.apolloautomation.com/products/msr2/troubleshooting/msr2-reset-wi-fi-credentials/
  - https://wiki.apolloautomation.com/products/mtr1/troubleshooting/mtr1-reset-wi-fi-credentials/
  - https://wiki.apolloautomation.com/products/rpro1/troubleshooting/rpro1-reset-wi-fi-credentials/
  - https://wiki.apolloautomation.com/products/rpro1/faq/
  - https://wiki.apolloautomation.com/products/air1/troubleshooting/air1-reset-wi-fi-credentials/
  - https://wiki.apolloautomation.com/products/temp1/troubleshooting/temp1-reset-wi-fi-credentials/
  - https://wiki.apolloautomation.com/products/temp1b/troubleshooting/temp1b-reset-wi-fi-credentials/
  - https://wiki.apolloautomation.com/products/plt1/troubleshooting/plt1-reset-wi-fi-credentials/
  - https://wiki.apolloautomation.com/products/plt1b/troubleshooting/plt1b-reset-wi-fi-credentials/
  - https://wiki.apolloautomation.com/products/pump1/troubleshooting/pump1-reset-wi-fi-credentials/
  - https://wiki.apolloautomation.com/products/btn1/troubleshooting/btn1-reset-wi-fi-credentials/
  - https://wiki.apolloautomation.com/products/cast1/troubleshooting/cast1-reset-wi-fi-credentials/
  - https://wiki.apolloautomation.com/products/msr2/troubleshooting/msr2-boot-mode/
  - https://wiki.apolloautomation.com/products/mtr1/troubleshooting/mtr1-boot-mode/
  - https://wiki.apolloautomation.com/products/rpro1/troubleshooting/rpro1-boot-mode/
  - https://wiki.apolloautomation.com/products/air1/troubleshooting/air1-boot-mode/
  - https://wiki.apolloautomation.com/products/temp1/troubleshooting/temp1-boot-mode/
  - https://wiki.apolloautomation.com/products/temp1b/troubleshooting/temp1b-boot-mode/
  - https://wiki.apolloautomation.com/products/plt1/troubleshooting/plt1-boot-mode/
  - https://wiki.apolloautomation.com/products/plt1b/troubleshooting/plt1b-boot-mode/
  - https://wiki.apolloautomation.com/products/pump1/troubleshooting/pump1-boot-mode/
  - https://wiki.apolloautomation.com/products/btn1/troubleshooting/btn1-boot-mode/
  - https://wiki.apolloautomation.com/products/castpro1/faq/
  - https://wiki.apolloautomation.com/products/castpro1/setup/getting-started/
  - https://wiki.apolloautomation.com/products/castpro1/troubleshooting/castpro1-boot-button/
  - https://wiki.apolloautomation.com/products/m1/setup/getting-started-m1/
  - https://wiki.apolloautomation.com/products/m1/faq/
  - https://wiki.apolloautomation.com/products/general/contact-us/contact-us-support/
  - https://esphome.io/components/wifi/
review_status: draft
last_verified: 2026-11-17
---
# Wont-Connect-to-Wi-Fi

## Summary

When an Apollo device can't reach your Wi-Fi, it broadcasts its own setup hotspot so you can enter your network details again. Most connection problems come down to the power supply, the network name being picked from a list on a mesh or multi-access-point system, a hidden network, or old Wi-Fi details saved on the device. This note covers the quick checks, how to bring the hotspot back by resetting the saved Wi-Fi details, and the settings that help a device stay connected.

## Applies to

- [[MSR-2]], [[MTR-1]], [[R-PRO-1]], [[AIR-1]], [[TEMP-1]] (including TEMP-1B), [[PLT-1]] (including PLT-1B), [[PUMP-1]], [[BTN-1]]: ESPHome firmware with an "Apollo ... Hotspot" setup network.
- [[CAST-1]], [[CAST-PRO-1]]: same idea, but the hotspot stays off while an Ethernet cable is plugged in. Both use 2.4 GHz Wi-Fi.
- [[M-1]]: runs WLED, so its hotspot and setup page are different (see the M-1 steps under Fix).

## Symptoms

- The device never shows up on your network or in Home Assistant after setup.
- You entered your Wi-Fi details, but the device's hotspot comes back.
- The device's setup hotspot doesn't appear in your phone or computer's Wi-Fi list.
- The device keeps dropping off Wi-Fi, restarting, or going unavailable.
- Your network is hidden, or you have a mesh system or several access points.

## Quick checks

1. **Try a different power brick and cable.** Apollo devices are sensitive to power quality, and cheap power bricks can cause restarts and dropped connections. Most devices need 5V and under 1A, so most phone chargers work. Device exceptions:
   - [[R-PRO-1]]: an 802.3af PoE port, or a USB-C supply of 5V 2A or more.
   - [[CAST-PRO-1]]: constant 5V over USB-C. 5V 1A is plenty, or 5V 3A if you run an LED strip from the screw terminals. The Ethernet port does not supply power.
   - [[M-1]]: use the USB-C cable and stock power supply, which provide 3A at 5V for one panel.
2. **Look for the device's hotspot.** Open the Wi-Fi list on your phone or computer. If the device's hotspot is showing, the device is not connected to your network. Join the hotspot and enter your Wi-Fi details again (see Fix, step 1). It can take about a minute for the hotspot to appear.
3. **Check your router's list of connected devices.** An Apollo device shows up with its Apollo name followed by the last 6 characters of its MAC address. If it's listed, the device is on your Wi-Fi and the problem is elsewhere.
4. **CAST-1 and CAST PRO-1: unplug the Ethernet cable.** Neither device broadcasts its setup hotspot while an Ethernet cable is connected.
5. **CAST PRO-1: run the status check.** With the device plugged in, hold the boot button (the second recessed button from the left, next to reset; use a pin) for about 3 seconds, then let go. The LEDs flash one color:
   - Yellow: not on your network. Check your Wi-Fi details or the Ethernet cable.
   - Green: on your network, but not connected to Home Assistant.
   - Blue: connected to Home Assistant.

## Fix

### 1. Enter your Wi-Fi details through the hotspot

1. On your phone or computer, join the device's hotspot. The names are:
   - [[MSR-2]]: "Apollo MSR2 Hotspot"
   - [[MTR-1]]: "Apollo MTR-1 Hotspot"
   - [[R-PRO-1]]: "Apollo R PRO 1 Hotspot"
   - [[AIR-1]]: "Apollo AIR-1 Hotspot"
   - [[TEMP-1]]: "Apollo TEMP1 Hotspot"; TEMP-1B: "Apollo TEMP1B Hotspot"
   - [[PLT-1]]: "Apollo PLT1 Hotspot"; PLT-1B: "Apollo PLT1B Hotspot"
   - [[PUMP-1]]: "Apollo PUMP-1 Hotspot"
   - [[BTN-1]]: "Apollo BTN1 Hotspot"
   - [[CAST-1]]: "Apollo CAST 1 Hotspot"
   - [[CAST-PRO-1]]: "Apollo CAST_PRO-1 Hotspot"
2. A setup page should open on its own. If it doesn't, type `192.168.4.1` into your browser's address bar. On the CAST-1 and CAST PRO-1, use `192.168.4.1/setup`
3. Choose your network or type its name, enter your Wi-Fi password, and save.
4. **If you have a mesh system or more than one access point, type your network name in by hand** instead of picking it from the list. That way the device joins the strongest signal.
5. The setup page closes once the device joins your Wi-Fi. On the CAST PRO-1, if it stays open and shows "Saved. Connecting...", setup is done and you can close it.

You can also set up Wi-Fi from Home Assistant over Bluetooth with Improv instead of the hotspot. That needs Bluetooth on your Home Assistant host (for example a Raspberry Pi's built-in Bluetooth) or an ESP32 Bluetooth proxy. Full guide: https://wiki.apolloautomation.com/products/general/setup/getting-started/ . See also [[Wi-Fi-Setup]].

### 2. Reset the saved Wi-Fi details to bring the hotspot back

If the device is holding old or wrong Wi-Fi details and the hotspot won't come back, clear them. Plug the device into power, then hold the BOOT button for 10 seconds. The device clears its Wi-Fi details and broadcasts its hotspot again, then follow step 1. Where to find BOOT:

- [[MSR-2]]: behind the right-hand of the two small slots in the case. The left slot is reset.
- [[MTR-1]]: behind the right-hand of the two small slots in the case. The left slot is reset.
- [[R-PRO-1]]: SW6, on the circuit board inside the case. With the back removed and the board flipped over, it is at the bottom right. RST1 at the bottom left is reset.
- [[AIR-1]]: with the USB-C port facing you, the right-hand of the two buttons beside the port. The left one is reset.
- [[TEMP-1]] and TEMP-1B: with the USB-C port facing you, press it with a paperclip through the small opening on the right side. With the lid off, it is labeled BOOT (on the TEMP-1 it sits next to the buzzer).
- [[PLT-1]]: through the small opening in the side of the case. The button near the USB-C port is reset. PLT-1B: SW1, next to the USB-C port, pressed with a pin through the small opening in the side.
- [[PUMP-1]]: with the device facing you, the button on the right. The left one is reset.
- [[BTN-1]]: on the back, with the device facing you, the button on the right. The left one is reset, so don't use it.
- [[CAST-1]]: unplug any Ethernet cable first. BOOT is on the left side of the case; the button on the right is reset.
- [[CAST-PRO-1]]: unplug any Ethernet cable first. Holding boot for 10 seconds is a full factory reset: it erases Wi-Fi details and settings, and the device restarts and broadcasts its hotspot. Then delete the old device in Home Assistant (open its page in the ESPHome integration, three-dot menu, Delete) and set it up again.

Per-device guides, for example: https://wiki.apolloautomation.com/products/msr2/troubleshooting/msr2-reset-wi-fi-credentials/

### 3. Hidden networks

If your network doesn't broadcast its name, the device needs `fast_connect` turned on:

1. Open ESPHome Device Builder in Home Assistant (install it first if needed).
2. Click **Edit** on your Apollo device.
3. Add `fast_connect: True` on a new line at the end of the `wifi:` section, indented two spaces like the lines above it.
4. Click **Save**, then **Install**, and choose **Wirelessly**.
5. When the log shows OTA successful, click **Close**.

With `fast_connect` on, the device skips the full Wi-Fi scan and joins the first matching network it sees, even if a closer access point is available. Full guide: https://wiki.apolloautomation.com/products/general/setup/adding-apollo-devices-to-hidden-networks/

### 4. Device keeps dropping off Wi-Fi: turn off power save

ESP32 devices use Wi-Fi power save mode `LIGHT` by default. Power saving generally makes the Wi-Fi connection less reliable. Setting it to `none` gives the most reliable connection, but the device's internal temperature goes up.

1. In Home Assistant, open ESPHome Device Builder and click **Edit** on your device.
2. Under the `wifi:` section, add `power_save_mode: none`, lined up with the other lines in that section. If there's no `wifi:` section, add one:

```yaml
wifi:
  power_save_mode: none
```

3. Click **Save**, then **Install**.

Don't set `power_save_mode: HIGH` to fix dropouts. It is the most power-saving mode and causes frequent disconnections from the router; Apollo only suggests it to reduce heat. Full guide: https://wiki.apolloautomation.com/products/general/troubleshooting/connection-issues/

### 5. M-1 (WLED)

1. Join the M-1's open hotspot, named "Apollo M-1" (no password). On builds older than 16.0.1, the name has a serial number at the end.
2. Type `4.3.2.1` into a browser's address bar.
3. Select **WIFI SETTINGS** and enter your network and password. Passwords are case sensitive. On WLED (16.0.1 or newer), select **Scan** and choose your network. On WLED-MM (14.5.1), type your network name where it shows `Your_Network`.
4. Set the mDNS address (for example `apollo-led-matrix`), then tap **Save & Connect**.
5. On WLED, wait a few seconds, then unplug the M-1 and plug it back in.
6. If it can't connect, the M-1 goes back to broadcasting the Apollo M-1 hotspot. Repeat the steps and double-check the network name and password.

Full guide: https://wiki.apolloautomation.com/products/m1/setup/getting-started-m1/ . See also [[WLED-Setup]].

## When to escalate

Hand the conversation to a person at support@apolloautomation.com when:

- The hotspot still doesn't appear after the 10-second BOOT reset with a known-good power supply. The next step is a factory reflash ([[Factory-Reflash]]). The customer can follow that guide, or a person can walk them through it.
- The device still won't connect after a factory reflash.
- The device shows no signs of power, or has physical damage.
- The customer asks about a warranty claim, return, or replacement.
- The customer's question about Wi-Fi bands goes beyond the 2.4 GHz guidance in [[Wi-Fi-Setup]], or is about special characters in the network name or password, or Wi-Fi range. These aren't documented yet.

## Customer phrasings

- "My sensor won't connect to my Wi-Fi."
- "I can't find the Apollo hotspot in my Wi-Fi list."
- "I typed my Wi-Fi password but the hotspot keeps coming back."
- "I have a mesh network and my device won't join."
- "My device keeps dropping offline in Home Assistant."
- "How do I reset the Wi-Fi on my Apollo device?"

---
title: Wi-Fi-Setup
aliases: [wifi setup, connect to wifi, Wi-Fi setup, hotspot setup, Improv setup, Improv via BLE, captive portal, reset Wi-Fi]
type: guide
audience: customer
applies_to: ["[[AIR-1]]", "[[BTN-1]]", "[[CAST-1]]", "[[CAST-PRO-1]]", "[[MSR-2]]", "[[MTR-1]]", "[[PLT-1]]", "[[PUMP-1]]", "[[R-PRO-1]]", "[[TEMP-1]]"]
sources:
  - https://wiki.apolloautomation.com/products/general/setup/getting-started/
  - https://wiki.apolloautomation.com/products/general/setup/getting-started-msr2/
  - https://wiki.apolloautomation.com/products/general/setup/getting-started-mtr1/
  - https://wiki.apolloautomation.com/products/general/setup/getting-started-rpro1/
  - https://wiki.apolloautomation.com/products/general/setup/getting-started-air1/
  - https://wiki.apolloautomation.com/products/general/setup/getting-started-temp1/
  - https://wiki.apolloautomation.com/products/general/setup/getting-started-plt1/
  - https://wiki.apolloautomation.com/products/general/setup/getting-started-pump1/
  - https://wiki.apolloautomation.com/products/temp1b/setup/getting-started-temp1/
  - https://wiki.apolloautomation.com/products/plt1b/setup/getting-started-plt1/
  - https://wiki.apolloautomation.com/products/btn1/setup/getting-started/
  - https://wiki.apolloautomation.com/products/cast1/setup/getting-started/
  - https://wiki.apolloautomation.com/products/castpro1/setup/getting-started/
  - https://wiki.apolloautomation.com/products/castpro1/faq/
  - https://wiki.apolloautomation.com/products/castpro1/troubleshooting/castpro1-boot-button/
  - https://wiki.apolloautomation.com/products/msr2/troubleshooting/msr2-reset-wi-fi-credentials/
  - https://wiki.apolloautomation.com/products/mtr1/troubleshooting/mtr1-reset-wi-fi-credentials/
  - https://wiki.apolloautomation.com/products/rpro1/troubleshooting/rpro1-reset-wi-fi-credentials/
  - https://wiki.apolloautomation.com/products/air1/troubleshooting/air1-reset-wi-fi-credentials/
  - https://wiki.apolloautomation.com/products/temp1/troubleshooting/temp1-reset-wi-fi-credentials/
  - https://wiki.apolloautomation.com/products/temp1b/troubleshooting/temp1b-reset-wi-fi-credentials/
  - https://wiki.apolloautomation.com/products/plt1/troubleshooting/plt1-reset-wi-fi-credentials/
  - https://wiki.apolloautomation.com/products/plt1b/troubleshooting/plt1b-reset-wi-fi-credentials/
  - https://wiki.apolloautomation.com/products/pump1/troubleshooting/pump1-reset-wi-fi-credentials/
  - https://wiki.apolloautomation.com/products/btn1/troubleshooting/btn1-reset-wi-fi-credentials/
  - https://wiki.apolloautomation.com/products/cast1/troubleshooting/cast1-reset-wi-fi-credentials/
  - https://wiki.apolloautomation.com/products/general/faq/
  - https://wiki.apolloautomation.com/products/general/setup/adding-apollo-devices-to-hidden-networks/
  - https://wiki.apolloautomation.com/products/general/troubleshooting/connection-issues/
  - https://www.home-assistant.io/integrations/improv_ble/
  - https://esphome.io/components/wifi/
review_status: draft
last_verified: 2026-11-17
---
# Wi-Fi-Setup

## Summary

A new Apollo device joins your Wi-Fi in one of two ways:

- **Hotspot (any phone or computer):** the device broadcasts its own Wi-Fi network. You join it, pick your home network, and enter your password.
- **Improv via BLE (Home Assistant):** Home Assistant sends your Wi-Fi details to the device over Bluetooth.

The CAST-1 (with its Ethernet module) and the CAST PRO-1 can also connect with an Ethernet cable instead.

Use one method, not both. Once the device is on your Wi-Fi, add it to Home Assistant through the ESPHome integration.

## Applies to

- [[AIR-1]], [[MSR-2]], [[MTR-1]], [[PUMP-1]], [[R-PRO-1]]
- [[TEMP-1]] and TEMP-1B, [[PLT-1]] and PLT-1B
- [[BTN-1]]
- [[CAST-1]] and [[CAST-PRO-1]], which also support Ethernet

Not covered here:

- The M-1 runs WLED and has its own setup. See [[WLED-Setup]].
- The ESK-1 is set up in ESPHome Device Builder.

## Before you start

1. **Use good power.** Apollo sensors need 5V and draw under 1A, so most phone chargers work. A cheap power brick or cable can cause restarts, a missing hotspot or an "unavailable" device. If that happens, try a different brick and cable.
   - BTN-1: use a 5V 1A USB-C supply. If you have the battery version, make sure its power switch is on. With the device on its side, slide the switch away from you.
   - CAST PRO-1: use 5V 1A, or 5V 3A if it drives an LED strip from the screw terminals.
2. **Use a 2.4 GHz network.** Most ESP32 devices only support 2.4 GHz Wi-Fi, so make sure your router offers a 2.4 GHz network. Most routers provide one by default, often with the same name as the 5 GHz network. The CAST-1 and CAST PRO-1 use 2.4 GHz Wi-Fi.
3. **Have your Wi-Fi name and password ready.**
4. **For Improv via BLE only:** your Home Assistant host needs Bluetooth (for example a Raspberry Pi's built-in Bluetooth) or at least one ESP32 Bluetooth proxy within range of the device.

## Steps

### Option A: Connect through the device's hotspot

1. Power on the device.
   - CAST-1 with the Ethernet module, or CAST PRO-1: unplug the Ethernet cable first. The hotspot never broadcasts while an Ethernet cable is connected.
2. On your phone or computer, open Wi-Fi settings and join the device's hotspot. It can take about a minute to appear. The hotspot names are:
   - AIR-1: "Apollo AIR-1 Hotspot"
   - BTN-1: "Apollo BTN1 Hotspot"
   - CAST-1: "Apollo CAST 1 Hotspot"
   - CAST PRO-1: "Apollo CAST_PRO-1 Hotspot"
   - MSR-2: "Apollo MSR2 Hotspot"
   - MTR-1: "Apollo MTR-1 Hotspot"
   - PLT-1: "Apollo PLT1 Hotspot"
   - PLT-1B: "Apollo PLT1B Hotspot"
   - PUMP-1: "Apollo PUMP-1 Hotspot"
   - R PRO-1: "Apollo R PRO 1 Hotspot"
   - TEMP-1: "Apollo TEMP1 Hotspot"
   - TEMP-1B: "Apollo TEMP1B Hotspot"
3. A setup page should open on its own. If it doesn't, open a browser and go to the setup address:
   - Most devices: **192.168.4.1**
   - CAST-1 and CAST PRO-1: **192.168.4.1/setup**
4. Pick your Wi-Fi network from the list, or scroll to the bottom and type the network name. Enter your password and click **Save**.
   - **Mesh Wi-Fi or several access points:** type the network name instead of picking it from the list. This helps the device join the access point with the strongest signal.
5. The setup page closes once the device joins your Wi-Fi. On the CAST PRO-1, if the page shows "Saved. Connecting..." and your phone switches back to your own Wi-Fi, setup is complete.
6. Add the device to Home Assistant ([[Add-to-Home-Assistant]]): click the **Notifications** bell, click **Check it out**, click **ADD** on the discovered device, click **Submit**, choose an **Area** and click **Finish**. You'll find it later under **Settings → Devices & services → ESPHome**.

### Option B: Connect with Improv via BLE (Home Assistant)

1. Power on the device near your Home Assistant host or a Bluetooth proxy.
2. In Home Assistant, go to **Settings → Devices & services** and click **ADD** on the discovered Apollo device card (Improv via BLE).
3. Enter your Wi-Fi details and finish setup. The clicks differ by device:
   - Most devices: click **Submit** when asked to set up the device. Enter your Wi-Fi name and password, then wait while the dialog shows the device connecting. When the success message appears, click the link in the dialog. Don't click **Close**. Choose an **Area** and finish. If the dialog already closed, add the device from the ESPHome discovery card as in Option A, step 6.
   - BTN-1: click **Submit**, enter your Wi-Fi name and password, click **Submit**, then click **Close** once it finishes. Then click **Add** on the discovered BTN-1, click **Submit**, choose an **Area** and click **Finish**.
   - CAST-1 and CAST PRO-1: enter your Wi-Fi name and password and click **Submit**. Click **Submit** again, choose an **Area** and click **Finish**. This also adds the device to Home Assistant.

### Option C: Ethernet (CAST-1 with Ethernet module, CAST PRO-1)

1. Plug an Ethernet cable from your router or switch into the device.
   - CAST-1: fit the Ethernet module first, with the CAST-1 unplugged. Line it up with the two rows of header pins on top of the case and press it straight down until it sits flat. Plug the cable into the module.
2. Power the device over USB-C. Ethernet carries data only and does not power the device.
3. The router gives the device an address automatically, so there is nothing to enter.
4. In Home Assistant, check that the **Network Connection** sensor on the device page shows Ethernet.
5. If you unplug the cable and Wi-Fi details are saved, the device falls back to Wi-Fi.

## If it doesn't work

1. **Swap the power brick and cable.** Power quality affects Wi-Fi. Try a few combinations.
2. **Check whether the hotspot is showing.** If you can see the device's hotspot, it is not on your Wi-Fi yet. Join the hotspot and enter your Wi-Fi details again.
3. **Look for the device on your router.** It shows in the router's client list as "Apollo" followed by six characters from the end of its MAC address.
4. **Reset the saved Wi-Fi details.** With the device powered, press and hold the **Boot** button for 10 seconds. It clears its Wi-Fi details and broadcasts its hotspot again. Then repeat Option A.
   - MSR-2, MTR-1: Boot is the button on the right. Press it with a small tool through the opening in the side of the case.
   - R PRO-1: Boot is SW6, on the circuit board inside the case. With the back removed and the board flipped over, it is at the bottom right. See [[Boot-Mode]].
   - PUMP-1: Boot is the button on the right.
   - BTN-1: Boot is the right-hand button on the back.
   - AIR-1: Boot is the right of the two buttons beside the USB-C port.
   - CAST-1: Boot is on the left. Unplug any Ethernet cable first.
   - CAST PRO-1: Boot is the second recessed button from the left, next to Reset. Use a pin. Unplug any Ethernet cable first. Holding 10 seconds also erases its settings, so delete the old CAST PRO-1 from the ESPHome integration before setting it up again.
   - TEMP-1, TEMP-1B, PLT-1, PLT-1B: press Boot with a small tool through the opening in the side of the case.
5. **CAST PRO-1 status check.** With it plugged in, hold Boot for about 3 seconds and release. The LEDs flash:
   - Yellow: no network connection. Check your Wi-Fi details or Ethernet cable.
   - Green: on your network but not connected to Home Assistant.
   - Blue: connected to Home Assistant.

   The LEDs then flash green once more. That is a component check passing, not a connection status.
6. **Hidden network.** If your Wi-Fi name is hidden, the device needs `fast_connect: True` added under `wifi:` in its YAML. Open ESPHome Device Builder, click **Edit** on the device, add the line, then **Save**, **Install** and **Wirelessly**. With this on, the device joins the first matching network it finds rather than scanning for the strongest one.
7. **Device keeps dropping off Wi-Fi.** Add `power_save_mode: none` under `wifi:` in the device's YAML, then **Save** and **Install**. The device's internal temperature rises with this setting.
8. **Improv via BLE fails.** Move the device closer to the Bluetooth adapter or proxy. Shelly and SMLIGHT proxies only listen, so they can't be used for Improv.
9. **Hotspot still missing after a reset on a CAST-1 or CAST PRO-1.** The next step is a factory reflash to restore its factory firmware (see [[Factory-Reflash]]). Contact Apollo support if you'd like a person to walk you through it.

If none of this works, see [[Wont-Connect-to-Wi-Fi]], then contact Apollo support at support@apolloautomation.com with your device model and what you've tried.

## Customer phrasings

- "I can't find the Apollo hotspot on my phone."
- "My sensor won't connect to my Wi-Fi."
- "The setup page at 192.168.4.1 won't load."
- "How do I change the Wi-Fi network on my Apollo device?"
- "Home Assistant doesn't see my new sensor."
- "Does it work with 5 GHz Wi-Fi?"

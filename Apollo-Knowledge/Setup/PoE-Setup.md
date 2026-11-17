---
title: PoE-Setup
aliases: [PoE setup, Ethernet setup, switch to Ethernet, switch to PoE, wired connection, Ethernet firmware, R PRO-1 PoE]
type: guide
audience: customer
applies_to: ["[[R-PRO-1]]", "[[CAST-PRO-1]]", "[[CAST-1]]"]
sources:
  - https://wiki.apolloautomation.com/products/rpro1/setup/rpro1-switch-firmware/
  - https://wiki.apolloautomation.com/products/rpro1/faq/
  - https://wiki.apolloautomation.com/products/rpro1/troubleshooting/rpro1-code/
  - https://wiki.apolloautomation.com/products/general/setup/getting-started-rpro1/
  - https://wiki.apolloautomation.com/products/castpro1/faq/
  - https://wiki.apolloautomation.com/products/castpro1/setup/getting-started/
  - https://wiki.apolloautomation.com/products/cast1/addons/ethernet-module/
  - https://wiki.apolloautomation.com/products/general/contact-us/contact-us-support/
review_status: draft
last_verified: 2026-11-17
---
# PoE-Setup

## Summary

The R PRO-1 is the only one of these devices that runs on PoE. It ships with Wi-Fi firmware, and you switch it to Ethernet firmware from Home Assistant, or by reflashing over USB. The CAST PRO-1 has built-in Ethernet, and the CAST-1 gets Ethernet from an add-on module. Both CAST models need no firmware change, but their Ethernet is data only with no PoE, so they still need USB-C power.

## Applies to

- [[R-PRO-1]]: PoE (802.3af) or USB-C power. Needs the Ethernet firmware to use the wired connection.
- [[CAST-PRO-1]]: built-in Ethernet, data only, no PoE. Powered over USB-C.
- [[CAST-1]]: Ethernet through the optional Ethernet add-on module, data only, no PoE. Powered over USB-C.

## Before you start

- **R PRO-1 power:** use a PoE port or injector that is 802.3af compliant, or a USB-C supply of 5V 2A or more.
- **R PRO-1 firmware:** it ships with Wi-Fi firmware, because not everyone has Ethernet or PoE. To switch from Home Assistant (step 1), set it up on Wi-Fi and add it to Home Assistant first (see [[Wi-Fi-Setup]] and [[Add-to-Home-Assistant]]).
- **R PRO-1 internet access:** to switch firmware from Home Assistant, the device must reach the internet, because it downloads the firmware from Apollo's GitHub. This won't work on an IoT network or VLAN that can't reach GitHub. In that case, use the USB reflash in step 2 below.
- **CAST PRO-1 power:** a 5V USB-C supply. 5V 1A is plenty, or use 5V 3A if you run an LED strip from the screw terminals. The Ethernet port does not take power.

## Steps

### 1. Switch the R PRO-1 to Ethernet firmware from Home Assistant

1. In Home Assistant, go to Settings, open the ESPHome integration, and click "1 device" under your Apollo R PRO-1.
2. Scroll down to the "Firmware Type" dropdown and select "Ethernet".
3. Find the Firmware Update entity and click "PRESS".
4. Wait a few minutes. The device downloads the firmware from the Apollo GitHub repo and installs it.
5. Your R PRO-1 is now on the Ethernet firmware and is ready to configure.

Full guide: https://wiki.apolloautomation.com/products/rpro1/setup/rpro1-switch-firmware/

### 2. Or reflash the R PRO-1 with Ethernet firmware over USB

Use this if the device can't reach GitHub, or isn't in Home Assistant yet. Boot mode details are in [[Boot-Mode]], and the general reflash steps in [[Factory-Reflash]].

1. Use Chrome, Edge, another Chromium-based browser, or a recent version of Firefox.
2. If the R PRO-1 was ever connected to Home Assistant, remove it from the ESPHome integration and from ESPHome Device Builder first.
3. Unplug the R PRO-1, remove the back, and take the board out of the case.
4. Hold the boot button (SW6, bottom right of the board), plug in a USB-C cable, then release the button.
5. Open https://install.apolloautomation.com/#/r-pro-1
6. Under "Choose your firmware", select **Ethernet**, then click **Connect & Install**.
7. In the browser pop-up, choose the R PRO-1's serial port and click **Connect**.
8. Click **Install ApolloAutomation.R-PRO-1-ETH**, then click **INSTALL**.
9. When the installer shows "Installation complete!", click **Next** and close the browser window.
10. The R PRO-1 is still in boot mode. Unplug it, then plug it back in so it starts in normal mode.
11. Set it up as a new device using the R PRO-1 getting started guide: https://wiki.apolloautomation.com/products/general/setup/getting-started-rpro1/

Full guide: https://wiki.apolloautomation.com/products/rpro1/troubleshooting/rpro1-code/

### 3. Switch the R PRO-1 back to Wi-Fi

1. In Home Assistant, go to Settings, open the ESPHome integration, and click "1 device" under your Apollo R PRO-1.
2. Scroll down to "Firmware Type" and select "WiFi".
3. Find the Firmware Update entity and click "PRESS".
4. Wait a few minutes for the download and install to finish.
5. Connect the R PRO-1 to your Wi-Fi through its hotspot, as in the R PRO-1 getting started guide: https://wiki.apolloautomation.com/products/general/setup/getting-started-rpro1/#connecting-through-hotspot

You can also reflash over USB as in step 2. Choose **WiFi** under "Choose your firmware", then click **Install ApolloAutomation.R-PRO-1-W**.

### 4. Connect a CAST PRO-1 over Ethernet

1. Plug the CAST PRO-1 into a 5V USB-C power supply.
2. Plug an Ethernet cable from your router or switch into the CAST PRO-1.
3. It picks up an address from your router on its own, so there's nothing to enter.
4. Home Assistant discovers it automatically. Open the ESPHome integration, click Add and Submit, edit the name, choose an Area, and click Finish.
5. On the device page, check that the Network Connection sensor reads Ethernet.

If you also set up Wi-Fi, the CAST PRO-1 keeps both connections up at once, so Home Assistant doesn't lose it when you plug or unplug the cable. Take the cable out and it goes back to Wi-Fi on its own, as long as it has Wi-Fi details saved. The Network Connection sensor reads Ethernet, WiFi, Ethernet + WiFi, or Hotspot.

Full guide: https://wiki.apolloautomation.com/products/castpro1/setup/getting-started/

### 5. Add Ethernet to a CAST-1

1. Unplug the CAST-1 from power.
2. Find the two rows of female header pins on the top of the case.
3. Line up the Ethernet module's pins with them, pin side down, and press straight down evenly on both ends until it sits flat. If it won't sit flat, lift it off and realign it. Don't force it.
4. Plug an Ethernet cable into the module, then plug the CAST-1 back into power.
5. On the device page, check that the Network Connection sensor reads Ethernet, or Ethernet + WiFi when both are connected.

Full guide: https://wiki.apolloautomation.com/products/cast1/addons/ethernet-module/

## If it doesn't work

- **R PRO-1 firmware switch doesn't work:** the switch needs internet access to github.com, so it won't work on an IoT network or VLAN that can't reach GitHub. Reflash over USB with the Ethernet firmware (step 2).
- **R PRO-1 has no power on PoE:** make sure your switch port or injector is 802.3af compliant, or power it over USB-C with a 5V 2A or bigger supply.
- **R PRO-1 not seen by your computer when reflashing:** make sure you held SW6 while plugging in the USB-C cable, and that you chose the right serial port.
- **CAST PRO-1 or CAST-1 is off with only an Ethernet cable plugged in:** their Ethernet is data only. They always need USB-C power.
- **CAST PRO-1 setup hotspot is missing:** the hotspot never broadcasts while an Ethernet cable is connected. Unplug the cable to set up Wi-Fi through the hotspot, or use Improv over Bluetooth.
- **Still stuck, or the device doesn't work after a reflash:** contact Apollo support at support@apolloautomation.com.

## Customer phrasings

- "How do I switch my R PRO-1 to PoE?"
- "I plugged my R PRO-1 into PoE but it doesn't show up in Home Assistant."
- "What PoE switch do I need for the R PRO-1?"
- "Can I power the CAST PRO-1 over Ethernet?"
- "My CAST PRO-1 hotspot isn't showing up."
- "How do I go back to Wi-Fi on my R PRO-1?"

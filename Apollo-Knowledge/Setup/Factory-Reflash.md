---
title: Factory-Reflash
aliases: [factory reflash, re-flash, reflash firmware, factory firmware, web installer, Apollo installer, reinstall firmware, flash over USB]
type: guide
audience: customer
applies_to: ["[[MSR-2]]", "[[MTR-1]]", "[[R-PRO-1]]", "[[AIR-1]]", "[[TEMP-1]]", "[[PLT-1]]", "[[PUMP-1]]", "[[BTN-1]]", "[[CAST-1]]", "[[CAST-PRO-1]]", "[[M-1]]"]
sources:
  - https://wiki.apolloautomation.com/products/msr2/troubleshooting/msr2-code/
  - https://wiki.apolloautomation.com/products/mtr1/troubleshooting/mtr1-code/
  - https://wiki.apolloautomation.com/products/rpro1/troubleshooting/rpro1-code/
  - https://wiki.apolloautomation.com/products/air1/troubleshooting/air1-code/
  - https://wiki.apolloautomation.com/products/temp1/troubleshooting/temp1-code/
  - https://wiki.apolloautomation.com/products/temp1b/troubleshooting/temp1b-code/
  - https://wiki.apolloautomation.com/products/plt1/troubleshooting/plt1-code/
  - https://wiki.apolloautomation.com/products/plt1b/troubleshooting/plt1b-code/
  - https://wiki.apolloautomation.com/products/pump1/troubleshooting/pump1-reflash/
  - https://wiki.apolloautomation.com/products/btn1/troubleshooting/btn1-reflash/
  - https://wiki.apolloautomation.com/products/cast1/troubleshooting/cast1-reflash/
  - https://wiki.apolloautomation.com/products/castpro1/troubleshooting/castpro1-reflash/
  - https://wiki.apolloautomation.com/products/msr1/troubleshooting/msr1-code/
  - https://wiki.apolloautomation.com/products/h1/reflash/
  - https://wiki.apolloautomation.com/products/h2/troubleshooting/reflash/
  - https://wiki.apolloautomation.com/products/h3/troubleshooting/reflash/
  - https://wiki.apolloautomation.com/products/m1/troubleshooting/m1-reflash/
  - https://wiki.apolloautomation.com/products/m1/troubleshooting/m1-reflash-esphome/
  - https://wiki.apolloautomation.com/products/temp1/troubleshooting/temp1-boot-mode/
  - https://wiki.apolloautomation.com/products/temp1b/troubleshooting/temp1b-boot-mode/
  - https://wiki.apolloautomation.com/products/plt1/troubleshooting/plt1-boot-mode/
  - https://wiki.apolloautomation.com/products/plt1b/troubleshooting/plt1b-boot-mode/
  - https://wiki.apolloautomation.com/products/h1/boot-mode/
  - https://wiki.apolloautomation.com/products/h3/troubleshooting/boot-mode/
  - https://wiki.apolloautomation.com/products/m1/choose-your-firmware/
  - https://wiki.apolloautomation.com/products/general/troubleshooting/removing-device-from-home-assistant/
  - https://wiki.apolloautomation.com/products/general/contact-us/contact-us-support/
review_status: draft
last_verified: 2026-11-17
---
# Factory-Reflash

## Summary

If your Apollo device has stopped responding and the other troubleshooting steps haven't helped, you can put the factory firmware back on it over USB with the Apollo web installer (https://install.apolloautomation.com). You put the device in boot mode, plug it into your computer, pick the firmware for your device in the installer and click Install. After the flash, you power-cycle the device and set it up again as a new device.

## Applies to

- [[MSR-2]], [[MTR-1]], [[R-PRO-1]], [[AIR-1]], [[PUMP-1]], [[BTN-1]], [[CAST-1]], [[CAST-PRO-1]]
- [[TEMP-1]] (USB-powered TEMP-1 and battery TEMP-1B)
- [[PLT-1]] (USB-powered PLT-1 and battery PLT-1B)
- [[M-1]] (WLED firmware)
- Also documented: MSR-1 and the H-1, H-2 and H-3 ornaments

The DEV-1, DEV-2, LED-1, NFC-1 and ESPHome Starter Kit boards are not covered by this guide.

## Before you start

1. Use Chrome, Edge or another Chromium-based browser on a computer. A recent version of Firefox also works.
2. Use a USB-C cable that carries both power and data. A charge-only cable won't show up in the installer.
3. If the device was ever added to Home Assistant, remove it first:
   - Only if you took control of it in the ESPHome Device Builder app: open ESPHome Device Builder, click the three dots on the device, choose Delete and confirm.
   - In Home Assistant, go to Settings → Devices & services → ESPHome. Click the three dots next to the device, choose Delete and confirm.
   - Full steps: https://wiki.apolloautomation.com/products/general/troubleshooting/removing-device-from-home-assistant/
4. Device-specific preparation:
   - PUMP-1: empty the water reservoir and make sure there is no water in the tubes, as a precaution.
   - TEMP-1B and PLT-1B: remove the battery. The reflash won't work properly while the battery is powering the device.
   - H-3: take the batteries out. With batteries in, the ornament stays powered and can't enter boot mode.
   - R PRO-1: unplug it, remove the back cover and take the board out of the case. The boot button is on the board.

## Steps

1. **Put the device in boot mode.** For most devices, hold the boot button, plug the USB-C cable into the device (the other end goes into your computer), then let go of the button. Pressing reset on its own only restarts the device. Button locations and the second boot method are in [[Boot-Mode]].
   - MSR-2: hold the boot button, through the right of the two small openings, while you plug in the cable.
   - MTR-1: hold the right of the two small openings (the boot button) while you plug in the cable.
   - AIR-1: hold the right of the two buttons beside the USB-C port while you plug in the cable.
   - R PRO-1: with the board out of the case, hold the boot button (SW6, bottom right of the board) while you plug in the cable.
   - TEMP-1 and TEMP-1B: with the USB-C port facing you, the boot button is behind a small opening on the right side. Press it with a paperclip while you plug in the cable.
   - PLT-1 and PLT-1B: the boot button is behind a small opening on the side of the case. Press it through the opening while you plug in the cable. (PLT-1B: a pin works.)
   - PUMP-1: unplug it first. Facing the device, hold the right button (boot) while you plug in the cable.
   - BTN-1: plug in the cable first. Facing the device, reset is on the left and boot is on the right. Hold boot, press and release reset, then let go of boot.
   - CAST-1: plug in the cable first. Boot is on the left and reset is on the right. Hold boot, press and release reset, then let go of boot.
   - CAST PRO-1: plug in the cable first. The buttons on the front are recessed, so use a pin. Hold boot (right), press and release reset (left), then let go of boot.
   - M-1: hold the left button on the controller (boot) while you plug in the cable.
   - MSR-1: hold the boot button (the left button, through the small opening in the top vents) while you plug in the cable.
   - H-2: unplug it first. Facing the ornament, hold the small black button on the right (boot) while you plug in the cable.
   - H-1: unplug it first. Hold the boot button while you plug in the cable. The boot mode page has a photo of where the button is: https://wiki.apolloautomation.com/products/h1/boot-mode/
   - H-3: with the batteries out, the back facing you and the hat at the top, the boot button is the small button to the left of the USB-C port, labeled BOOT. Hold it while you plug in the cable. Full steps: https://wiki.apolloautomation.com/products/h3/troubleshooting/boot-mode/
2. **Open the installer page for your device**, and pick a firmware option if the page asks:
   - MSR-2: https://install.apolloautomation.com/#/msr-2
   - MTR-1: https://install.apolloautomation.com/#/mtr-1
   - R PRO-1: https://install.apolloautomation.com/#/r-pro-1 — under Choose your firmware, pick WiFi if it connects over Wi-Fi, or Ethernet if it connects over PoE or Ethernet.
   - AIR-1: https://install.apolloautomation.com/#/air-1
   - TEMP-1: https://install.apolloautomation.com/#/temp-1 — choose USB Power.
   - TEMP-1B: https://install.apolloautomation.com/#/temp-1 (same page as TEMP-1) — choose Battery Power.
   - PLT-1: https://install.apolloautomation.com/#/plt-1 — choose USB Power.
   - PLT-1B: https://install.apolloautomation.com/#/plt-1 (same page as PLT-1) — choose Battery Power.
   - PUMP-1: https://install.apolloautomation.com/#/pump-1
   - BTN-1: https://install.apolloautomation.com/#/btn-1
   - CAST-1: https://install.apolloautomation.com/#/cast-1
   - CAST PRO-1: https://install.apolloautomation.com/#/cast-pro-1
   - M-1: https://install.apolloautomation.com/#/m-1 — new units ship with WLED 16.0.1, which is the default. WLED needs a Rev6 controller; the revision is printed on the back of the board. WLED-MM 14.5.1 (Rev6) and WLED-MM 14.5.1 (Rev4) are the older builds; if you use one, match the revision printed on the back of your controller. A Rev4 controller uses WLED-MM 14.5.1 (Rev4).
   - MSR-1: https://install.apolloautomation.com/#/msr-1
   - H-1: https://install.apolloautomation.com/#/h-1 (one firmware, the smart Wi-Fi firmware)
   - H-2: https://install.apolloautomation.com/#/h-2 and H-3: https://install.apolloautomation.com/#/h-3 — choose Smart (Wi-Fi) to join your Wi-Fi and Home Assistant, or Basic (No Wi-Fi) for the firmware the ornament ships with.
3. **Click Connect & Install.** In the browser pop-up, select your device's serial (COM) port, often shown as "USB JTAG/serial debug unit", then click Connect (or Allow).
4. **Click the Install option for your device's firmware**, then click INSTALL again to confirm. The option names are:
   - MSR-2: ApolloAutomation.MSR-2_Factory
   - MTR-1: ApolloAutomation.MTR-1
   - R PRO-1: ApolloAutomation.R-PRO-1-W (WiFi) or ApolloAutomation.R-PRO-1-ETH (Ethernet)
   - AIR-1: ApolloAutomation.AIR-1
   - TEMP-1: Apollo.TEMP-1_R2
   - TEMP-1B: Apollo.TEMP-1B_R2
   - PLT-1: ApolloAutomation.PLT-1
   - PLT-1B: ApolloAutomation.PLT-1B
   - PUMP-1: ApolloAutomation.PUMP-1
   - BTN-1: ApolloAutomation.BTN-1
   - MSR-1: ApolloAutomation.MSR-1_Factory
   - H-2: ApolloAutomation.H-2 (Smart) or ApolloAutomation.H-2D (Basic)
   - M-1: after you pick your M-1 from the list, tick **Erase device**, click Next, then click Install. The erase is what brings the M-1 back to its factory display settings.
5. **Wait for "Installation complete!"**, then click Next and close the browser window.
6. **Power-cycle the device.** It is still in boot mode after the flash. Unplug it, then plug it back in (put the battery back in for battery devices) so it starts normally. Don't skip this step.
7. **Set the device up as a new device** using its getting-started guide on the Apollo wiki (https://wiki.apolloautomation.com). See [[Wi-Fi-Setup]] and [[Add-to-Home-Assistant]].
   - M-1: go to Choose Your Firmware: https://wiki.apolloautomation.com/products/m1/choose-your-firmware/ (WLED setup: [[WLED-Setup]])
   - H-1: look for the Apollo hotspot and connect to it (it might not show if the H-1 was on your Wi-Fi before). Then open the ESPHome app in Home Assistant and check whether you can adopt the device.

## If it doesn't work

1. **No serial port shows in the pop-up:** the device is probably not in boot mode, or the cable is charge-only. See [[USB-Not-Detected]]. Try a different USB-C cable that supports data, then enter boot mode again. On the TEMP-1, TEMP-1B, PLT-1, PLT-1B and H-1 you can also try the other boot method from the boot mode page: with the cable plugged in, hold boot, press and release reset, then let go of boot. On the TEMP-1 and TEMP-1B this needs the lid off.
2. **Not sure which port is your device:** unplug it and see which port disappears from the list.
3. **"Failed to initialize, try holding the BOOT button while clicking Install":** the device isn't in boot mode. Put it in boot mode again and retry from step 3.
4. **"ERROR Logger is not configured!" during an H-1 install:** this is expected and you can ignore it.
5. **TEMP-1B or PLT-1B won't flash:** make sure the battery is removed.
6. **The device doesn't come back after the flash:** make sure you power-cycled it. Until you unplug and replug it, it stays in boot mode.
7. **M-1 running ESPHome firmware:** that firmware is flashed from a different installer. Follow https://wiki.apolloautomation.com/products/m1/troubleshooting/m1-reflash-esphome/

**When to escalate to a person**

- The device still doesn't work after a successful reflash and power-cycle.
- The device never appears in the serial port list after trying a second data-capable cable and every boot method on its boot mode page.
- The device shows physical damage.
- The customer asks about a warranty claim, return or replacement.
- A TEMP-1 or TEMP-1B may need the older Revision 1 (R1) firmware. Only support decides this.

Contact support at support@apolloautomation.com.

## Customer phrasings

- "My sensor is bricked, how do I put the original firmware back on?"
- "How do I reflash my MSR-2 to factory?"
- "The web installer doesn't see my device / no COM port shows up."
- "Where's the installer link for my TEMP-1B?"
- "I messed up my YAML in ESPHome and now it won't boot."
- "Which firmware do I pick for my R PRO-1, WiFi or Ethernet?"

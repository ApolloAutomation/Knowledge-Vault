---
title: USB-Not-Detected
aliases: [usb not detected, computer doesn't see device, no com port, no serial port, installer can't find device, web serial not working, device keeps connecting and disconnecting, usb keeps disconnecting]
type: troubleshooting
audience: customer
applies_to: ["[[MSR-2]]", "[[MTR-1]]", "[[AIR-1]]", "[[R-PRO-1]]", "[[BTN-1]]", "[[TEMP-1]]", "[[PLT-1]]", "[[PUMP-1]]", "[[M-1]]", "[[CAST-1]]", "[[CAST-PRO-1]]", "[[ESK-1]]", "[[ESPHome-C6-Board]]"]
sources:
  - https://wiki.apolloautomation.com/products/ESPHome-Starter-Kit/setup/first-steps/
  - https://wiki.apolloautomation.com/products/msr2/troubleshooting/msr2-code/
  - https://wiki.apolloautomation.com/products/btn1/troubleshooting/btn1-boot-mode/
  - https://wiki.apolloautomation.com/products/m1/troubleshooting/m1-boot-mode/
  - https://wiki.apolloautomation.com/products/cast1/troubleshooting/cast1-boot-mode/
  - https://wiki.apolloautomation.com/products/general/troubleshooting/connection-issues/
  - https://wiki.apolloautomation.com/products/general/contact-us/contact-us-support/
  - https://esphome.io/guides/physical_device_connection/
review_status: draft
last_verified: 2026-11-17
---
# USB-Not-Detected

## Summary

When you reflash an Apollo device, your computer has to see it over USB-C. If the Apollo web installer (or ESPHome Device Builder) shows no port to pick, or the device keeps connecting and disconnecting, the cause is almost always the cable, the USB port, the browser, or the device not being in boot mode. Work through the checks below in order.

## Applies to

[[MSR-2]], [[MTR-1]], [[AIR-1]], [[R-PRO-1]], [[BTN-1]], [[TEMP-1]] (including TEMP-1B), [[PLT-1]] (including PLT-1B), [[PUMP-1]], [[M-1]], [[CAST-1]], [[CAST-PRO-1]], and the ESP32-C6 board in the [[ESK-1]], also sold on its own as the [[ESPHome-C6-Board]].

## Symptoms

- The Apollo web installer opens, but no port shows up when you click Connect & Install.
- Your computer doesn't react at all when you plug the device in.
- The device keeps restarting, or connects and disconnects over and over.
- On Linux, the device doesn't appear as a serial port when you try to flash it.

## Quick checks

1. **Use a data cable.** The USB-C cable must carry both power and data. Charge-only cables, like the ones that often come with power banks, power the device but your computer can't see it.
2. **Try another cable and another USB port.** If the device keeps restarting or isn't detected, swap to a different USB-C cable and a different USB port on your computer.
3. **Seat the cable firmly.** On the ESK-1 / ESPHome C6 Board, hold the sides of the board and gently push the USB-C cable firmly into the port, avoiding the ribbon connectors on the sides.
4. **Use a supported browser.** The factory reflash needs Chrome, Edge, another Chromium-based browser, or a recent version of Firefox.

## Fix

1. **Unplug the device and start from a clean state.** Remove power completely, then plug the USB-C cable into your computer first.
2. **Put the device in boot mode.** Hold BOOT while you plug the cable into the device, then release it (Method 1). If that doesn't work, keep the cable plugged in, hold BOOT, press and release RESET, then release BOOT (Method 2). Pressing RESET on its own only restarts the device. Button locations for each device are in [[Boot-Mode]].
   - **BTN-1:** if a charged battery is installed, Method 1 won't work. Use Method 2.
   - **M-1:** hold the left button on the controller while plugging in. The M-1 uses Method 1 only.
   - **CAST-1:** BOOT is on the left and RESET is on the right, the reverse of most Apollo devices.
   - **ESK-1 / ESPHome C6 Board:** use Method 2. The board stays in boot mode until you flash it.
3. **Pick the port.** Open your device's page in the Apollo web installer (https://install.apolloautomation.com) and click Connect & Install. Select the open COM port, then click Connect. The installer page for each device is listed in [[Factory-Reflash]].
   - **ESK-1 / ESPHome C6 Board:** flash from ESPHome Device Builder instead. Click Install, then Plug into this computer. Select the COM port, then click Connect.
4. **Linux only:** if the device still doesn't appear as a serial port, add your user to the dialout group, then log out and back in:

   ```
   sudo usermod -a -G dialout $USER
   ```

5. **If it keeps restarting or dropping offline during normal use** (not while flashing), check the power. Power quality matters more than you'd think. Try a few different combinations of power cord and power brick.
   - **ESK-1 / ESPHome C6 Board:** ESP32 boards are sensitive to power. Use a quality USB-C cable and power source, or try a different USB port. A 5V 1A supply is plenty.
6. **After flashing, power-cycle the device.** It stays in boot mode until you unplug it completely and plug it back in. The full reflash steps are in [[Factory-Reflash]].
   - **ESK-1 / ESPHome C6 Board:** when the install completes, click Stop, then press RESET on the board.

## When to escalate

Hand the conversation to Apollo support (a person, not the AI) at https://wiki.apolloautomation.com/products/general/contact-us/contact-us-support/ if:

- The computer still doesn't detect the device after trying both boot mode methods, at least two known data cables, two USB ports and a supported browser.
- The USB-C port is loose or damaged, a button doesn't click or is stuck, or the case or board is damaged.
- The device is detected but still doesn't work after a successful reflash and power cycle.
- The customer has a DEV-1, DEV-2, LED-1 or NFC-1. We don't have documented USB or boot mode steps for these yet.
- The customer asks about USB drivers. We don't have Apollo-specific driver guidance.
- The customer asks about warranty, returns or a replacement.

## Customer phrasings

- The web installer says no device found / no port shows up.
- My computer doesn't see my MSR-2 when I plug it in.
- There's no COM port when I try to flash my sensor.
- My device keeps connecting and disconnecting from my PC.
- Do I need a driver to flash my Apollo device?
- My ESPHome kit doesn't show up as a serial port on Linux.

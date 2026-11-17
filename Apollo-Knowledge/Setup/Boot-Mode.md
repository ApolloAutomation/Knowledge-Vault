---
title: Boot-Mode
aliases: [boot mode, download mode, flash mode, bootloader mode, boot button, put device in boot mode, enter boot mode]
type: guide
audience: customer
applies_to: ["[[MSR-2]]", "[[MTR-1]]", "[[AIR-1]]", "[[R-PRO-1]]", "[[BTN-1]]", "[[TEMP-1]]", "[[PLT-1]]", "[[PUMP-1]]", "[[M-1]]", "[[CAST-1]]", "[[CAST-PRO-1]]", "[[ESK-1]]", "[[ESPHome-C6-Board]]"]
sources:
  - https://wiki.apolloautomation.com/products/msr2/troubleshooting/msr2-boot-mode/
  - https://wiki.apolloautomation.com/products/mtr1/troubleshooting/mtr1-boot-mode/
  - https://wiki.apolloautomation.com/products/air1/troubleshooting/air1-boot-mode/
  - https://wiki.apolloautomation.com/products/rpro1/troubleshooting/rpro1-boot-mode/
  - https://wiki.apolloautomation.com/products/btn1/troubleshooting/btn1-boot-mode/
  - https://wiki.apolloautomation.com/products/temp1/troubleshooting/temp1-boot-mode/
  - https://wiki.apolloautomation.com/products/temp1b/troubleshooting/temp1b-boot-mode/
  - https://wiki.apolloautomation.com/products/plt1/troubleshooting/plt1-boot-mode/
  - https://wiki.apolloautomation.com/products/plt1b/troubleshooting/plt1b-boot-mode/
  - https://wiki.apolloautomation.com/products/pump1/troubleshooting/pump1-boot-mode/
  - https://wiki.apolloautomation.com/products/m1/troubleshooting/m1-boot-mode/
  - https://wiki.apolloautomation.com/products/cast1/troubleshooting/cast1-boot-mode/
  - https://wiki.apolloautomation.com/products/castpro1/troubleshooting/castpro1-boot-mode/
  - https://wiki.apolloautomation.com/products/ESPHome-Starter-Kit/setup/first-steps/
  - https://wiki.apolloautomation.com/products/msr2/troubleshooting/msr2-code/
  - https://wiki.apolloautomation.com/products/btn1/troubleshooting/btn1-reflash/
  - https://wiki.apolloautomation.com/products/m1/troubleshooting/m1-reflash/
  - https://wiki.apolloautomation.com/products/cast1/troubleshooting/cast1-reflash/
  - https://wiki.apolloautomation.com/products/general/battery-sensors/wake-up-battery-sensor/
  - https://wiki.apolloautomation.com/products/mtr1/troubleshooting/mtr1-code/
  - https://wiki.apolloautomation.com/products/rpro1/troubleshooting/rpro1-code/
  - https://wiki.apolloautomation.com/products/air1/troubleshooting/air1-code/
  - https://wiki.apolloautomation.com/products/temp1/troubleshooting/temp1-code/
  - https://wiki.apolloautomation.com/products/temp1b/troubleshooting/temp1b-code/
  - https://wiki.apolloautomation.com/products/plt1/troubleshooting/plt1-code/
  - https://wiki.apolloautomation.com/products/plt1b/troubleshooting/plt1b-code/
  - https://wiki.apolloautomation.com/products/pump1/troubleshooting/pump1-reflash/
  - https://wiki.apolloautomation.com/products/castpro1/troubleshooting/castpro1-reflash/
review_status: draft
last_verified: 2026-11-17
---
# Boot-Mode

## Summary

Boot mode (also called download or flash mode) lets your computer write new firmware to an Apollo device over USB-C. You need it when you reflash a device from the Apollo web installer. You enter it with the device's BOOT button, either on its own while plugging in, or together with the RESET button. The device stays in boot mode until you remove power and plug it back in.

## Applies to

[[MSR-2]], [[MTR-1]], [[AIR-1]], [[R-PRO-1]], [[BTN-1]], [[TEMP-1]] (including the battery version, TEMP-1B), [[PLT-1]] (including PLT-1B), [[PUMP-1]], [[M-1]], [[CAST-1]], [[CAST-PRO-1]], and the ESP32-C6 board in the [[ESK-1]], also sold on its own as the [[ESPHome-C6-Board]].

## Before you start

1. Have a USB-C cable that carries both power and data, plus a computer to flash from. Charge-only cables will not work.
2. Have a paperclip, pin or small screwdriver ready. On most devices the buttons sit behind small openings in the case.
3. PUMP-1 only: empty the water reservoir and make sure no water is left in the tubes before you start.
4. TEMP-1B and PLT-1B only: remove the battery. Flashing won't work properly while the battery is still powering the device.
5. Know the two buttons:
   - **BOOT** puts the device into boot mode, but only when it is held while the device powers up or restarts.
   - **RESET** restarts the device. Pressing RESET on its own only restarts it; it does not enter boot mode.
   - On the battery models (BTN-1, TEMP-1B, PLT-1B), holding BOOT for 10 seconds or more on a running device resets it to factory settings and erases its Wi-Fi. Only hold BOOT as described in the steps below.

## Steps

### 1. Find the BOOT and RESET buttons on your device

- **MSR-2:** two small slots on the case. RESET is behind the left slot, BOOT is behind the right slot.
- **MTR-1:** two small slots on the case. RESET is behind the left slot, BOOT is behind the right slot.
- **AIR-1:** with the USB-C port facing you, the two buttons are beside the port. RESET is the left button and BOOT is the right button, pressed through a small opening.
- **R-PRO-1:** the buttons are on the circuit board inside. Unplug the R PRO-1, pry the back off at the seam below the USB-C port, then gently lift the board out of the case and flip it over. BOOT (marked SW6) is at the bottom right and RESET (marked RST1) is at the bottom left.
- **BTN-1:** with the BTN-1 facing you, RESET is on the left and BOOT is on the right.
- **TEMP-1 and TEMP-1B:** with the USB-C port facing you, BOOT is reached with a paperclip through the small opening on the right side. On the TEMP-1 it sits inside next to the buzzer. RESET (marked RST) is reached with the lid removed; gently pry the lid up at the small slit near the top of the case.
- **PLT-1:** BOOT is behind a small opening on the side of the case. RESET is near the USB-C port, below it.
- **PLT-1B:** BOOT (marked SW1) sits next to the USB-C port and is reached with a pin or tweezers through a small opening in the side of the case. RESET (marked RST, also SW2) has its own small opening in the side of the case.
- **PUMP-1:** with the PUMP-1 facing you, RESET is on the left and BOOT is on the right.
- **M-1:** BOOT is the left button on the M-1 controller. The M-1 uses Method 1 only.
- **CAST-1:** BOOT is on the left and RESET is on the right. This is the reverse of most Apollo devices.
- **CAST PRO-1:** looking at the front panel, RESET is on the left and BOOT is on the right. Both are recessed, so press them with a pin or small screwdriver. These are swapped compared to the CAST-1.
- **ESK-1 / ESPHome C6 Board:** with the USB-C cable pointing toward you, BOOT is to the left of the USB-C port and RESET is to the right. When plugging in, push gently and avoid the ribbon (FPC) connectors on the sides. The board uses Method 2.

### 2. Enter boot mode with Method 1 (BOOT button only)

Use this method on the MSR-2, MTR-1, AIR-1, R-PRO-1, TEMP-1, TEMP-1B, PLT-1, PLT-1B, PUMP-1, M-1, CAST-1, CAST PRO-1, and a BTN-1 without a battery.

1. Unplug the device from power.
2. Plug the USB-C cable into your computer.
3. Press and hold the BOOT button.
4. While still holding BOOT, plug the USB-C cable into the device's USB-C port.
5. Release BOOT. The device is now in boot mode.

BTN-1: if your BTN-1 has a battery installed and charged, Method 1 will not work. Use Method 2.

### 3. Or enter boot mode with Method 2 (BOOT and RESET)

Use this method if Method 1 doesn't work, on a BTN-1 with a battery, and on the ESK-1 / ESPHome C6 Board. On the TEMP-1 and TEMP-1B, remove the lid first so you can reach RESET.

1. Connect the device to your computer with the USB-C cable.
2. Press and hold the BOOT button. Keep holding it the whole time.
3. While still holding BOOT, press and release the RESET button.
4. Release BOOT. The device is now in boot mode.

### 4. Flash the firmware

Continue with the factory reflash steps for your device. The Apollo web installer is at https://install.apolloautomation.com and each device's reflash guide is on the Apollo wiki at https://wiki.apolloautomation.com (search for "re-flash" and your device name). See also [[Factory-Reflash]]. ESK-1 and ESPHome C6 Board owners flash from ESPHome Device Builder instead; the board stays in boot mode until you flash it.

### 5. Leave boot mode

1. When flashing is finished, power cycle the device before doing anything else: unplug it to remove power, then plug it back in. The device stays in boot mode until you do this.
2. ESK-1 / ESPHome C6 Board: after flashing from Device Builder, press RESET to restart the board.

## If it doesn't work

1. Try the other method. If Method 1 didn't work, use Method 2, and the other way round. The M-1 only has Method 1, and the ESK-1 / ESPHome C6 Board only has Method 2.
2. Make sure you are holding BOOT, not RESET. On the CAST-1 the buttons are swapped compared to the CAST PRO-1 and most other devices.
3. Try a different USB-C cable and a different USB port on your computer. The cable must carry data, not just power. See [[USB-Not-Detected]].
4. TEMP-1B and PLT-1B: make sure the battery is removed.
5. On Linux, if the device doesn't show up as a serial port, add your user to the dialout group with `sudo usermod -a -G dialout $USER`, then log out and back in.

### When to contact support

Contact Apollo support (a person, not the AI) if:

- The device still isn't detected by your computer after trying both methods, another data cable and another USB port.
- A button doesn't click, is stuck, or the case or board is damaged.
- The device still doesn't work after a successful reflash and power cycle.
- You have a question about warranty, returns or replacements.
- You own a device not listed here (for example DEV-1, DEV-2, LED-1 or NFC-1). We don't have documented boot mode steps for those yet.

## Customer phrasings

- How do I put my MSR-2 into boot mode?
- Where is the boot button on my device?
- The web installer can't find my device to flash it.
- How do I put my BTN-1 into flash mode?
- Which button is boot and which is reset on the CAST-1?
- I want to reflash my sensor back to factory firmware.

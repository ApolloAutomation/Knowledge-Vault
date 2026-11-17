---
title: Battery-and-Sleep
aliases: [battery life, sleep mode, prevent sleep, keep awake, wake up sensor, deep sleep, battery charging, update battery device]
type: guide
audience: customer
applies_to: ["[[BTN-1]]", "[[PLT-1]]", "[[TEMP-1]]", "[[AIR-1]]", "[[ESPHome-C6-Board]]", "[[ESK-1]]"]
sources:
  - https://wiki.apolloautomation.com/products/general/battery-sensors/prevent-sleep/
  - https://wiki.apolloautomation.com/products/general/battery-sensors/wake-up-battery-sensor/
  - https://wiki.apolloautomation.com/products/general/battery-sensors/awake-ha-helper/
  - https://wiki.apolloautomation.com/products/general/calibrating-and-updating/updating-firmware/
  - https://wiki.apolloautomation.com/products/general/troubleshooting/firmware-updates-not-appearing/
  - https://wiki.apolloautomation.com/products/btn1/faq/
  - https://wiki.apolloautomation.com/products/temp1b/faq/
  - https://wiki.apolloautomation.com/products/temp1b/setup/insert-battery/
  - https://wiki.apolloautomation.com/products/plt1b/faq/
  - https://wiki.apolloautomation.com/products/plt1b/additional-info/insert-battery/
  - https://wiki.apolloautomation.com/products/ESPHome-Starter-Kit/modules/battery/
  - https://apolloautomation.com/products/btn-1-macro-deck
review_status: draft
last_verified: 2026-11-17
---
# Battery-and-Sleep

## Summary

Apollo's battery sensors (BTN-1, TEMP-1B and PLT-1B) sleep to save battery. The ESPHome C6 Board and ESK-1 sleep only if you add sleep to your own configuration. While a device is asleep it drops off Wi-Fi and shows as unavailable in Home Assistant. This is expected. It wakes on its Sleep Duration timer, sends its readings, then sleeps again. This guide covers how to change the sleep time, wake a device, keep it awake for a firmware update, which battery to use and how to charge it, and how long the battery lasts.

## Applies to

- [[BTN-1]] (battery versions)
- [[TEMP-1]] battery version (TEMP-1B)
- [[PLT-1]] battery version (PLT-1B)
- [[AIR-1]] (no battery, but it has a Sleep Duration setting, and sleeping lowers the temperature offset it needs)
- [[ESPHome-C6-Board]] and [[ESK-1]] with an optional LiPo battery

## Before you start

- Your device should already be added to Home Assistant through the ESPHome integration.
- Sleeping devices can't receive commands. Change settings only while the device is awake, or wake it first (see step 2).
- The battery is not included with the TEMP-1B, PLT-1B, the International battery BTN-1, or the ESPHome C6 Board. The USA battery BTN-1 includes one.

## Steps

### 1. Change how long the device sleeps (Apollo devices)

1. In Home Assistant, go to **Settings > Devices & services > ESPHome** and click your Apollo device's name.
2. Scroll down to the **Prevent Sleep** toggle and the **Sleep Duration** box.
3. Enter the sleep time in **Sleep Duration**. Check the unit next to the box. Defaults:
   - AIR-1: 5 minutes
   - PLT-1: 5 minutes
   - TEMP-1: 8 minutes
   - BTN-1: 24 hours
   - PLT-1B: 12 hours
   - TEMP-1B: 12 hours
4. We recommend keeping the default values. Longer sleep gives longer battery life; shorter sleep gives fresher readings.

Turning **Prevent Sleep** off makes the device go to sleep straight away, so finish any changes first.

### 2. Wake a sleeping device

Press and release the **RESET** button. The BOOT button does not wake a sleeping device. You can also power-cycle the device, or remove and reinsert the battery.

- **TEMP-1B:** press and release the reset button (RST).
- **PLT-1B:** press and release the reset button.
- **BTN-1:** press and release the reset button (left side), or press any of the four main buttons. A main-button press is sent to Home Assistant as a click once the BTN-1 reconnects, so any automation on that click will run. Use reset if you only want to wake it.

The device goes back to sleep on its own after waking unless you keep it awake (step 3).

### 3. Keep a device awake (for updates or setup)

Choose one:

1. **Prevent Sleep toggle:** wake the device, then turn on **Prevent Sleep** on the device page in Home Assistant, or on the device's own web page (for example plt-1.local or its IP address).
2. **BOOT button:** after the device has woken up and restarted, press and hold BOOT for 4-5 seconds, then release. The BOOT button is on the right on the BTN-1.
   - Do not hold BOOT while pressing RESET. That puts the device into boot mode for flashing (see [[Boot-Mode]]).
   - Do not hold BOOT for 10 seconds or more. That factory-resets the device and erases its Wi-Fi settings.
3. **Home Assistant helper (for longer periods):**
   1. Go to **Settings > Devices & services > Helpers** and click **Create helper**.
   2. Scroll to the bottom, choose **Toggle**, name it `apollo_ota_mode` (an icon such as `mdi:sleep-off` is optional), and click **Create**.
   3. Search for `apollo_ota_mode` in the helpers list, open it and switch it **On**.
   4. While the toggle is on, your Apollo devices stay awake instead of going back to sleep the next time they wake on their timer or reboot.
   5. To avoid leaving devices awake by accident, add an automation: **Settings > Automations & scenes > Create automation**. Click **Add trigger**, choose **Entity**, then **State**. Set Entity to `apollo_ota_mode`, To **On**, and For **1 hour**. Under **Then do**, click **Add action**, choose **Input boolean: Turn off**, and select `apollo_ota_mode`.

When you are done, turn Prevent Sleep (or the helper) off so the device goes back to saving battery.

### 4. Update firmware on a battery device

1. Go to **Settings > Devices & services > ESPHome**, select the device and open its **Firmware Update** entity.
2. Start the update. On a battery device it installs the next time the device wakes.
3. Battery devices only check for updates while they are awake and connected. If no update appears, keep the device awake (step 3) and reboot it once. See also [[Firmware-Updates]].

### 5. Battery type and charging

- **BTN-1:** a 3.7V 2800 mAh battery with a PH 2.0 connector, no larger than 80mm x 30mm x 8mm. It charges through the BTN-1's USB-C port. Power the BTN-1 from a 5V 1A or larger USB-C supply.
- **TEMP-1B:** a rechargeable 16340 (RC-CR123A) flat-top battery, not included. USB-C does **not** charge it; use a separate 16340 charger. USB-C (5V, 1A or less) can power the device, and the battery then acts as backup if power is lost. To insert it:
  1. Carefully pry the case lid open with a flat metal tool.
  2. Lift the board out, or turn the case upside down so it drops out gently.
  3. Seat the battery with its positive end at the **+** mark on the holder.
  4. Put the board back battery-side down, with the RGB LED in the top-right corner. Rest one edge on the case ledge, then lower the other side so it lies flat.
  5. Line the RGB LED up with the small hole in the lid and press the lid down firmly until it snaps into place.
- **PLT-1B:** a flat-top, **unprotected** 18650 Li-ion cell, 3.6V or 3.7V nominal, about 2,500-3,500 mAh, not included. Protected cells are too long for the compartment. We recommend the Samsung 30Q 3000mAh. Cells advertised above 5,000 mAh are almost always counterfeit. USB does **not** charge the cell; use a separate 18650 charger. To insert it:
  1. Press your thumb on the case above the stake until the lid pops off.
  2. Push the stake down slightly, then lift it out of the bottom case.
  3. Flip the board over and find the markings: **+** on the left, **-** on the right. Double-check before going further.
  4. Place the battery's positive end on the left, matching the board's **+**. Press the **-** end in first, then the **+** end. It takes a bit of force.
  5. Flip the board back, lay it flat in the case, line up the notch in the top-left of the lid and press down until it snaps into place.
- **ESPHome C6 Board / ESK-1:** a rechargeable 3.7V LiPo with a 2-pin JST-PH 2.0 connector (the 3.7V 2800 mAh LiPo in our guide is one example that works).
  1. Check the wires first: black (ground) goes on the side nearest the ESP32-C6 chip, red on the side nearest the USB-C port. If they are reversed, stop and do not force it.
  2. Push the connector in until it seats fully.
  3. Plug in USB-C. The battery charges while the board keeps running. No separate charger or configuration is needed.
  4. To remove it, pull straight out by the connector body, not the wires.

### 6. Expected battery life

- **BTN-1:** up to a year with about 4 presses a day in deep sleep.
- **TEMP-1B:** about 6 months or more when waking every 12 hours.
- **PLT-1B:** about 6 months when waking every 8 hours, and about a year when waking every 12 hours or more.
- **ESPHome C6 Board / ESK-1:** depends on your own configuration; we don't publish a figure.

Battery life always depends on how often the device wakes. Keeping a device awake uses the battery much faster.

### 7. Sleep on the ESPHome C6 Board / ESK-1 (your own configuration)

The kit board only sleeps if you add sleep to its ESPHome configuration. Our battery guide shows an example that wakes every 10 minutes and stays awake for 30 seconds:

```yaml
deep_sleep:
  id: deep_sleep_1
  run_duration: 30s
  sleep_duration: 10min
```

1. Add a **Prevent Sleep** template switch as shown in the battery guide: https://wiki.apolloautomation.com/products/ESPHome-Starter-Kit/modules/battery/ . It is on by default, so finish setup and updates first, then turn it off to start sleeping.
2. Toggle it only while the board is awake. A sleeping board picks up the change at its next wake.
3. If you add the battery fuel gauge, keep its `update_interval` shorter than `run_duration`, or the Battery Voltage and Battery Level entities stay empty.
4. If an over-the-air update fails because the board keeps sleeping, turn on Prevent Sleep, or connect USB-C and flash over the cable.

## If it doesn't work

- **Device shows unavailable:** on a battery device this is normal while it sleeps. Wake it with RESET (step 2) and it reconnects.
- **BTN-1 is slow or multi-clicks don't work:** on battery, a sleeping BTN-1 takes around 10 seconds to wake and registers only a single press. Multi-clicks are not supported while it sleeps. Buzzer and LED commands also only work while it is awake.
- **Update never installs:** keep the device awake (step 3), reboot it once, then start the update.
- **TEMP-1B or PLT-1B won't power on from the battery:** charge the cell in a separate charger, since USB does not charge it, and check it is seated with **+** at the board's **+** mark.
- **PLT-1B battery doesn't fit:** use a flat-top, unprotected 18650. Protected cells are too long.
- If none of this helps, or the battery, holder or connector looks damaged, swollen or hot, stop using the battery and contact Apollo support.

## Customer phrasings

- "My sensor keeps going unavailable in Home Assistant."
- "How do I stop my TEMP-1 from sleeping so I can update it?"
- "My BTN-1 takes a while to respond and double-click doesn't work."
- "Does the PLT-1 charge its battery over USB?"
- "What battery should I buy for the plant sensor?"
- "How long will the battery last?"

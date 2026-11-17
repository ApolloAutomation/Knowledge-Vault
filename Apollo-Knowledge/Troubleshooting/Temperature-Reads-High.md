---
title: Temperature-Reads-High
aliases: [temperature reads high, temperature offset, humidity reads low, humidity wrong, temperature wrong, sensor runs hot, calibrate temperature, predicted room temperature, temperature probe not working]
type: troubleshooting
audience: customer
applies_to: ["[[AIR-1]]", "[[MSR-2]]", "[[MTR-1]]", "[[R-PRO-1]]", "[[TEMP-1]]", "[[PLT-1]]"]
sources:
  - https://wiki.apolloautomation.com/products/general/temp-hum-calibration/
  - https://wiki.apolloautomation.com/products/general/setup/how-to-add-temp-and-humidity-from-scd40/
  - https://wiki.apolloautomation.com/products/air1/additional-info/predicted-room-temp-humidity/
  - https://wiki.apolloautomation.com/products/air1/faq/
  - https://wiki.apolloautomation.com/products/msr2/faq/
  - https://wiki.apolloautomation.com/products/general/battery-sensors/prevent-sleep/
  - https://wiki.apolloautomation.com/products/general/troubleshooting/connection-issues/
  - https://wiki.apolloautomation.com/products/general/setup/adjusting-wifi-power/
  - https://wiki.apolloautomation.com/products/temp1/addons/temp-probe/
  - https://wiki.apolloautomation.com/products/temp1/addons/food-probe/
  - https://wiki.apolloautomation.com/products/temp1/addons/multiple-probes/
  - https://wiki.apolloautomation.com/products/temp1/setup/temp1-change-temp-probe-update-interval/
  - https://wiki.apolloautomation.com/products/temp1/faq/
  - https://wiki.apolloautomation.com/products/temp1b/faq/
  - https://apolloautomation.com/products/air-1
  - https://apolloautomation.com/products/temp-1
  - https://apolloautomation.com/products/r-pro-1
review_status: draft
last_verified: 2026-11-17
---
# Temperature-Reads-High

## Summary

The ESP32 chip inside Apollo sensors gives off heat while it runs and uses Wi-Fi. That heat warms the air inside the case, so the onboard sensors read warmer than the room. Because warmer air holds more moisture, the same heat also makes relative humidity read lower than it really is. This is expected, and you can correct it with an offset, with sleep, or (on the TEMP-1) with a probe that sits away from the device.

## Applies to

- [[AIR-1]] (SEN55, and the SCD40 if you have the CO2 add-on)
- [[MSR-2]] (DPS310 temperature, and the SCD40 if you have the CO2 add-on)
- [[MTR-1]] (SCD40 with the CO2 add-on)
- [[R-PRO-1]] (optional temperature and humidity readings)
- [[TEMP-1]] (onboard AHT20-F and the optional probes), including the battery version (TEMP-1B)
- [[PLT-1]] (onboard air temperature and humidity)

## Symptoms

- Temperature reads a few degrees higher than a thermostat or another thermometer in the same room.
- Humidity reads lower than another hygrometer in the same room.
- The MSR-2 or AIR-1 shows "unknown" for DPS310 Temperature.
- A TEMP-1 probe shows as failed or doesn't report.

## Quick checks

1. **Compare against a trusted reference.** Put a thermometer and hygrometer you trust right next to the Apollo device and let both settle for 15 to 20 minutes before comparing.
2. **Know what's normal.** On the AIR-1, heat from the ESP32-C3 means an offset of about 2 to 6 °C is needed. It is much lower when the AIR-1 uses its Sleep function. On the R PRO-1, heat can affect the optional temperature and humidity readings, so significant offsets are needed.
3. **Check Wi-Fi power saving.** If you set `power_save_mode: none` under `wifi:` (sometimes suggested for connection problems, see [[Wont-Connect-to-Wi-Fi]]), the device runs warmer inside and temperature reads higher. Only change this if you need it for a stable connection. Going the other way, setting `power_save_mode: HIGH` cuts the heat but makes the Wi-Fi connection less reliable, with frequent disconnections.
4. **Keep the TEMP-1 itself somewhere cool.** The probes are built for fridges, freezers, grills and water, but the TEMP-1 body must stay in a cool, dry place. With the food probe, set the TEMP-1 on the grill's side shelf, not on the hot lid.
5. **DPS310 Temperature shows "unknown" (MSR-2 or AIR-1).** A small number of units shipped without the DPS310 because the part was discontinued. The rest of the device works normally.

## Fix

### 1. AIR-1: use Predicted Room Temperature and Humidity

These sensors blend the SEN55, DPS310 and SCD40 readings with a model that corrects for heat inside the case. They come with recent AIR-1 firmware. If you don't see them, update the firmware first (see [[Firmware-Updates]]).

1. In Home Assistant, go to **Settings > Devices & services > ESPHome** and select your AIR-1.
2. Scroll down and select **entities not shown**.
3. Select **Predicted Room Temperature**, click the gear icon and choose **Enable**. Repeat for **Predicted Room Humidity**.
4. Wait a few minutes. These sensors wait 3 minutes after boot before reporting, so early readings don't skew them.
5. Place a trusted thermometer next to the AIR-1 and let everything settle for 15 to 20 minutes.
6. If **Predicted Room Temperature** is off by the same amount every time, change **Baseline Offset** (default 0) by that difference. For example, if it reads 0.4 °C high, set Baseline Offset to -0.4. Enable Baseline Offset the same way as in step 3 if you don't see it.
7. Leave **Physics Multiplier P** at its default of 0.5357. It is still being refined.

The original **SEN55 Temperature** and **SEN55 Humidity** sensors keep working, so you can pick whichever you prefer for dashboards and automations.

Guide: https://wiki.apolloautomation.com/products/air1/additional-info/predicted-room-temp-humidity/

### 2. Add offsets to the SCD40 (CO2 add-on)

- **AIR-1 and MSR-2:** add offset boxes with a short piece of YAML.
  - **AIR-1 with recent firmware:** first check **entities not shown** on the device page. If **SCD40 Temperature Offset** and **SCD40 Humidity Offset** are already listed there, they belong to the Predicted Room sensors. Don't add the YAML; use Fix 1 instead.
  1. In Home Assistant, open **ESPHome Device Builder** from the sidebar and click **EDIT** on your device.
  2. Paste the YAML from our guide at the bottom of the file, on a new line with no spaces before it: https://wiki.apolloautomation.com/products/general/setup/how-to-add-temp-and-humidity-from-scd40/
  3. Click **SAVE**, then **INSTALL**. When the log shows "INFO OTA successful", click **STOP**.
  4. Go to **Settings > Devices & services > ESPHome**, open your device and enter your values in **SCD40 Temperature Offset** and **SCD40 Humidity Offset**. They start at 14.54 °C and -18.86 %, and accept -70 to 70 in steps of 0.1.
  5. The offset is subtracted from the raw reading. Compare with your reference thermometer and adjust the offset by the difference. Allow up to 1 minute for a change to take effect.
- **MTR-1:** the firmware already includes **SCD40 Temperature** and **SCD40 Humidity** entities with their offsets, disabled by default. With the CO2 add-on fitted, enable them on the device page instead of adding YAML, then set the offsets the same way as step 4 above.

The starting values were measured against our own NIST-certified thermometer in our environment, so they may not match your home. Always fine-tune against your own reference.

### 3. Let the device sleep (AIR-1, PLT-1, TEMP-1)

The chip makes much less heat while asleep, so a sleeping sensor needs a much smaller offset.

1. In Home Assistant, go to **Settings > Devices & services > ESPHome** and click your device's name.
2. Scroll down to **Sleep Duration** and **Prevent Sleep**.
3. Set **Sleep Duration**, checking the unit next to the box. We recommend the defaults: AIR-1 5 minutes, PLT-1 5 minutes, TEMP-1 8 minutes.
4. Turn **Prevent Sleep** off. The device goes to sleep straight away, so finish any other changes first.

While asleep, the device only reports when it wakes, so Home Assistant can show it as unavailable in between. This is normal. See [[Battery-and-Sleep]].

### 4. MSR-2: correct the DPS310 temperature

Heat from the ESP32 can affect the DPS310 temperature reading. Adjust the temperature offset in the device's configuration, using the difference from a trusted reference thermometer as described in our calibration guide: https://wiki.apolloautomation.com/products/general/temp-hum-calibration/

### 5. TEMP-1: use a probe for the most accurate reading

The onboard AHT20-F can be warmed by the ESP32. For the most accurate temperature, use one of the optional probes, which sit away from the device. The DS18B20 flat-cable probes (1.5 m and 20 cm) are rated ±0.5 °C.

1. Plug the probe fully into the TEMP-1's 3.5mm port.
2. Press the reset button or power-cycle the TEMP-1. Probes are only detected at boot, and a probe plugged in later is marked as failed.
3. Go to **Settings > Devices & services > ESPHome**, open the TEMP-1 and set **Select Probe** to **Temperature** (DS18B20 probes) or **Food** (food probe).
4. **Using the multi-probe splitter:** connect all probes before powering on, keep **Select Probe** on **Temperature**, and enable the disabled 3rd and 4th temperature probe entities if you use more than two probes. The splitter needs firmware 25.11.20.1 or newer. The food probe doesn't work with the splitter.
5. **Keep the probe cable to 1.5 m or less.** Extension cables can cause voltage drop and bad readings.
6. The probe reports every 60 seconds by default. To change this, see https://wiki.apolloautomation.com/products/temp1/setup/temp1-change-temp-probe-update-interval/

## When to escalate

Hand the conversation to a person on the Apollo support team if:

- The reading is still far off after an offset, sleep or the AIR-1 predicted sensors, and the device sits next to a trusted reference.
- The reading jumps around wildly, or a sensor entity stays unavailable or "unknown" (other than DPS310, see Quick checks).
- A TEMP-1 probe still shows as failed after a power-cycle with the probe already plugged in, or the probe, cable or plug looks damaged.
- The device feels very hot to the touch, smells burnt or shows any physical damage.
- The customer asks about a warranty claim, replacement or return.

## Customer phrasings

- "My AIR-1 says it's 26 degrees but my thermostat says 22."
- "Why is the humidity on my sensor so much lower than my hygrometer?"
- "My MSR-2 temperature is always a few degrees too high."
- "How do I calibrate the temperature on my Apollo sensor?"
- "My TEMP-1 probe isn't showing up in Home Assistant."
- "Is it normal for the sensor to read high?"

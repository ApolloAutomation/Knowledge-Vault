---
title: CO2-Readings
aliases: [CO2 wrong, CO2 too low, CO2 too high, CO2 calibration, calibrate SCD40, CO2 Auto Calibration, ASC, forced recalibration, CO2 jumping, CO2 sawtooth]
type: troubleshooting
audience: customer
applies_to: ["[[AIR-1]]", "[[MSR-2]]", "[[MTR-1]]", "[[R-PRO-1]]"]
sources:
  - https://wiki.apolloautomation.com/products/general/calibrating-and-updating/co2-calibration/
  - https://wiki.apolloautomation.com/products/general/calibrating-and-updating/co2-calibration-quick/
  - https://wiki.apolloautomation.com/products/air1/faq/
  - https://wiki.apolloautomation.com/products/general/faq/
  - https://wiki.apolloautomation.com/products/general/tutorials/change-co2-update-interval/
  - https://wiki.apolloautomation.com/products/rpro1/faq/
  - https://wiki.apolloautomation.com/products/msr2/faq/
  - https://wiki.apolloautomation.com/products/mtr1/faq/
  - https://apolloautomation.com/products/air-1
  - https://apolloautomation.com/products/mtr-1
  - https://apolloautomation.com/products/r-pro-1
review_status: draft
last_verified: 2026-11-17
---
# CO2-Readings

## Summary

The optional CO2 sensor in Apollo devices is the Sensirion [[SCD40]]. The latest Apollo firmware turns on its automatic self-calibration (ASC) by default. ASC keeps readings accurate as long as the sensor sees fresh air (about 420 ppm) at least once a week. Common causes of "wrong" readings are a room that never gets fresh air, from vibration or strong airflow, and where the device is placed. You can also calibrate the sensor yourself outdoors in a few minutes.

The CO2 sensor is for air quality monitoring. It is not a safety alarm. See "Is it a safety device?" below.

## Applies to

- [[AIR-1]], [[MSR-2]], [[MTR-1]] and [[R-PRO-1]], when fitted with the optional SCD40 CO2 sensor.

## Symptoms

- CO2 reads lower than expected, or slowly drifts lower over weeks.
- CO2 reads very differently from another Apollo device in the same home.
- CO2 jumps up and down in a sawtooth pattern much more than expected (AIR-1).
- CO2 is slow to react when people enter a room.
- CO2 reads oddly on a device mounted in a wall or ceiling (R PRO-1).

## Quick checks

1. **Does the room get fresh air at least once a week?** Automatic self-calibration assumes the sensor sees fresh air (about 420 ppm) at least once a week. Airing out the room weekly is enough. In a room that rarely gets fresh air (a sealed office, basement or grow room), ASC slowly pulls readings down. See Fix 2.
2. **Is the device exposed to vibration or strong airflow?** If the sensor sees a lot of vibration or too much airflow, the SCD40 will have trouble working. Move it away from fans, vents and anything that vibrates.
3. **AIR-1 only: which side is facing up?** Some AIR-1 units give erratic CO2 readings when the "Apollo" side faces up. Turn the AIR-1 over onto its other side.
4. **R PRO-1 only: is it recessed?** CO2 readings may be skewed when the R PRO-1 is recessed in a wall or ceiling.
5. **Is the reading just slow?** CO2 updates every 60 seconds by default. Even at the fastest setting, the SCD40 takes about 90 seconds to fully show a real change in CO2, so a spike (for example, someone entering a room) ramps in over a couple of minutes. This is normal.

## Fix

### Fix 1: Calibrate the sensor outdoors

This sets the sensor's baseline to outdoor air, about 420 ppm.

1. Take the device outside and plug it in. If you can't get power outdoors (for example, in an apartment), use a USB battery bank.
2. Leave it outdoors for at least 5 minutes so the readings settle.
3. In Home Assistant, go to **Settings > Devices & services > ESPHome** and click your device.
4. Find **Calibrate SCD40 to 420 ppm** and press **Press** next to it.
   - Shortcut (computer only, not on a phone): on a Home Assistant dashboard, press the **e** key, type "Calibrate CO2", select your device, and click **PRESS**. If the search box doesn't appear, click on the dashboard first, then press **e**.
5. Check the CO2 reading. It should be at or near 420 ppm. If it isn't roughly 400–500 ppm, press **Calibrate SCD40 to 420 ppm** again. It can take several presses.

### Fix 2: Turn off auto calibration in rooms without fresh air

If the room rarely gets fresh air, automatic self-calibration will slowly pull readings too low.

1. In Home Assistant, go to **Settings > Devices & services > ESPHome** and open your device.
2. Turn off the **CO2 Auto Calibration** switch.
3. Calibrate the sensor outdoors using Fix 1.
4. With auto calibration off, repeat Fix 1 every 1 to 2 years to bring the baseline back to 420 ppm.

### Fix 3: Make CO2 update faster (optional)

If you want CO2 to update more often than every 60 seconds, follow [Changing your sensor's CO2 update interval](https://wiki.apolloautomation.com/products/general/tutorials/change-co2-update-interval/). The fastest setting is 5 seconds. This uses more Wi-Fi airtime and writes more to the Home Assistant database. It does not change the roughly 90-second time the sensor needs to fully react to a change.

### Is it a safety device?

No. The optional CO2 sensor on the AIR-1 and MTR-1 does not meet CO2 safety monitoring requirements as defined by the NBIC, NFPA or IFC. On the AIR-1, the CO2 and gas sensors are for air quality monitoring only. If you need CO2 or gas safety detection, use a dedicated CO2 or gas monitor.

As a general guide, Apollo suggests increasing air exchange to get CO2 below 1000 ppm for a safer environment.

## When to escalate

Hand the conversation to a person when:

- The device shows no CO2 reading at all, or the CO2 entity is missing or unavailable, on a unit that has the CO2 sensor.
- Readings still aren't roughly 400–500 ppm outdoors after several presses of **Calibrate SCD40 to 420 ppm**.
- Readings stay clearly wrong after the quick checks and an outdoor calibration.
- The device or sensor looks physically damaged.
- The customer asks about a warranty claim, replacement or return.
- The customer needs CO2 for safety or regulatory compliance.

## Customer phrasings

- "My CO2 is reading way too low, like 380 indoors."
- "My two Apollo sensors show completely different CO2 levels."
- "The CO2 graph on my AIR-1 is jumping up and down like a saw."
- "How do I calibrate the CO2 sensor?"
- "Can I use this as a CO2 alarm?"
- "CO2 takes forever to go up when people come in the room."

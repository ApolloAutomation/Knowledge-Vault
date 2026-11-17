---
title: R-PRO-1
aliases: ["R PRO-1", "R PRO 1", "RPRO1", "Apollo R PRO-1"]
type: product
audience: customer
source: https://apolloautomation.com/products/r-pro-1
status: available
status_checked: 2026-11-15
power_source: [poe, usb-c]
last_verified: 2026-11-16
---
# R-PRO-1

## Description

The R PRO-1 is Apollo's most advanced presence sensor: a compact PoE dual mmWave multisensor for smart homes and commercial buildings. It supports true PoE (802.3af compliant) and USB-C power, with built-in Wi-Fi and Bluetooth. It carries the Made for ESPHome badge, ships with Wi-Fi firmware that can be switched to PoE in the device dashboard, and is fully local, open source and cloud-free. The LD2450 is in the base unit; the LD2412 and SCD40 are optional.

## Features

- LD2450 base radar: multi-zone motion tracking with defined zones in its field of view
- Optional LD2412 radar working alongside the LD2450: excels at still presence (seated or resting people); together they give hybrid presence data
- PoE (802.3af) or USB-C power
- Built-in Wi-Fi and Bluetooth (Bluetooth tracking and Improv Wi-Fi provisioning)
- LTR390 for ambient lux and UV
- Two addressable RGB LEDs and a piezo buzzer
- Optional SCD40 NDIR CO2 on a mezzanine expansion board; rear mezzanine port for modular add-ons
- Flat-surface, single gang box or ceiling mounting
- Heat can affect the optional temperature/humidity readings (significant offsets needed), and CO2 may be skewed when the sensor is recessed in walls or ceilings
- Open source code and 3D files

## Specs

- Power input: PoE (802.3af) or USB-C
- Battery life: N/A — PoE or USB-C powered, no battery
- Operating temperature: -40 to 65 °C (rating of the ESP32-S3 module, most conservative ESP32-S3 range)
- Waterproof: No — the R PRO-1 is not waterproof
- Power consumption awake: Normal for a basic 802.3af PoE device; it does not need a high-power PoE port
- Power consumption sleeping: Unknown — escalate to support
- What battery works with it: N/A — PoE or USB-C powered, no battery

## Components

- [[LD2450]] - base mmWave radar, multi-zone motion tracking
- [[LD2412]] - optional mmWave radar for still presence detection
- [[LTR390]] - ambient lux and UV sensor
- [[SCD40]] - optional NDIR CO2 sensor on the mezzanine expansion board
- [[ESP32-S3]] - microcontroller; built-in Wi-Fi and Bluetooth

## Options and add-ons

- Add-ons: USB-C cable; front-facing USB-C wall charger (USA); 3D printed gang box mount; gang box kit; ceiling mount kit; [[LD2412]] mmWave sensor; [[SCD40]] CO2 sensor

## What's in the box

- Assembled sensor with case

## Common questions and answers

### How do I switch my R PRO-1 from Wi-Fi to PoE (Ethernet)?

The R PRO-1 ships with Wi-Fi firmware. To switch to the Ethernet (PoE) firmware:

1. In Home Assistant, go to Settings, open the ESPHome integration, and click the "1 device" link under your Apollo R PRO-1.
2. In the "Firmware Type" dropdown, select "Ethernet".
3. Find the Firmware Update entity and press its "PRESS" button.
4. Wait a few minutes while the device downloads and installs the new firmware.

The device must be able to reach github.com, because the firmware is downloaded from there. Full steps: https://wiki.apolloautomation.com/products/rpro1/setup/rpro1-switch-firmware/

### What kind of PoE does the R PRO-1 need?

The R PRO-1 supports true PoE (802.3af compliant). Its power draw is normal for a basic 802.3af PoE device, so it does not need a high-power PoE port. It can also be powered over USB-C instead.

### Will the R PRO-1 detect someone sitting still or resting?

The base LD2450 radar does multi-zone motion tracking. For still presence, such as seated or resting people, add the optional LD2412 radar. It works alongside the LD2450 and the two together give hybrid presence data.

### Why are the temperature, humidity or CO2 readings on my R PRO-1 off?

Heat can affect the optional temperature and humidity readings, so significant offsets are needed. CO2 readings may be skewed when the sensor is recessed in a wall or ceiling.

### How can I mount the R PRO-1?

It can be mounted on a flat surface, in a single gang box, or on the ceiling. Add-ons include a 3D printed gang box mount, a gang box kit and a ceiling mount kit.

### Can I get the R PRO-1 with CO2 or the LD2412 radar?

The LD2412 mmWave sensor and the SCD40 CO2 sensor are offered as add-ons. The SCD40 goes on a mezzanine expansion board, and the rear mezzanine port takes modular add-ons.

### How do I set up Wi-Fi on the R PRO-1?

The R PRO-1 supports Improv Wi-Fi provisioning, and it has built-in Wi-Fi and Bluetooth.

### Does the R PRO-1 need the cloud?

No. It is fully local, open source and cloud-free, and carries the Made for ESPHome badge.

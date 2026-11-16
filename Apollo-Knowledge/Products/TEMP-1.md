---
title: TEMP-1
aliases: ["TEMP 1", "TEMP-1 Battery"]
type: product
audience: customer
source: https://apolloautomation.com/products/temp-1
status: available
status_checked: 2026-11-15
power_source: [usb-c, battery]
last_verified: 2026-11-15
---
# TEMP-1

## Description

The TEMP-1 is a temperature sensor for ESPHome and Home Assistant over Wi-Fi, with Bluetooth too. It comes as a USB-C powered model or a battery model (rechargeable battery not included). For the most accurate readings it is designed to be used with optional probes through a 3.5mm jack. An onboard AHT20-F measures ambient temperature and humidity and can be affected by heat from the ESP32; sleep settings help. An RGB LED and buzzer give alerts.

## Features

- ESP32-based platform; local, private, open source
- Onboard AHT20-F temperature and humidity sensor
- 3.5mm jack for optional probes:
  - 1.5 m flat waterproof DS18B20 probe ([[Long-Temperature-Probe]])
  - 20 cm flat waterproof DS18B20 probe ([[Short-Temperature-Probe]])
  - 1 m stainless steel food-safe NTC probe, not dishwasher safe ([[TEMP-1-Food-Probe]])
- Multi-probe splitter (3.5mm 4-way) available (TEMP-1-Multi-Probe-Splitter)
- RGB LED and buzzer
- Wi-Fi and Bluetooth
- Use cases: fridge/freezer, cooking, fish tank, pool/hot tub, attic fan, HVAC, greenhouse, remote monitoring, overheat alerts
- Optional magnet mount

## Specs

- Battery life: Up to 6 months with optimized sleep settings (battery version)
- Operating temperature: Unknown — escalate to support
- Waterproof: The device itself: Unknown — escalate to support. The flat-cable DS18B20 probes are waterproof (submersible)
- Power consumption awake: Unknown — escalate to support
- Power consumption sleeping: Unknown — escalate to support
- What battery works with it: Rechargeable RC-CR123A (CR123A) or 16340 (not included; a 16340 battery is sold as an add-on)

## Components

- [[AHT20]] - onboard air temperature and humidity (AHT20-F variant)
- [[DS18B20]] - optional waterproof flat-cable temperature probes ([[Long-Temperature-Probe]], [[Short-Temperature-Probe]])
- NTC probe - optional stainless steel food-safe probe ([[TEMP-1-Food-Probe]])
- Microcontroller: ESP32-based; exact chip Unknown — escalate to support

## Options and add-ons

- Versions: Non-Battery, Battery (battery not included)
- Add-ons: USB-C cable; USB-C plug (USA style); 16340 battery; magnet mount; short probe ([[Short-Temperature-Probe]]); long probe ([[Long-Temperature-Probe]]); food probe ([[TEMP-1-Food-Probe]]); multi-probe splitter (TEMP-1-Multi-Probe-Splitter)

## What's in the box

Assembled sensor with case; Apollo sticker.

## Common questions and answers

### Does the TEMP-1 battery version come with a battery?

No. The rechargeable battery is not included. A 16340 battery is available as an add-on.

### What battery does the TEMP-1 use?

A rechargeable RC-CR123A (CR123A) or 16340 battery, in the battery version only.

### How long does the TEMP-1 battery last?

Up to 6 months with optimized sleep settings.

### Why does the TEMP-1 onboard temperature read high?

The onboard AHT20-F ambient sensor can be affected by heat from the ESP32. Sleep settings help. For the most accurate readings, the TEMP-1 is designed to be used with one of the optional probes through the 3.5mm jack.

### Which probes work with the TEMP-1?

The 1.5 m [[Long-Temperature-Probe]] and 20 cm [[Short-Temperature-Probe]] (both waterproof DS18B20 flat-cable probes), and the 1 m stainless steel [[TEMP-1-Food-Probe]] (NTC).

### Can I connect more than one probe to the TEMP-1?

Yes, with the 3.5mm 4-way multi-probe splitter. The long and short DS18B20 probes work with the splitter. The [[TEMP-1-Food-Probe]] is not compatible with the splitter.

### Can I put the TEMP-1 probe in water?

The flat-cable DS18B20 probes ([[Long-Temperature-Probe]] and [[Short-Temperature-Probe]]) are waterproof and submersible, which suits uses like a fish tank or pool/hot tub. Water resistance of the [[TEMP-1-Food-Probe]] is not listed, so please contact support before submerging it.

### Is the food probe dishwasher safe?

No. The [[TEMP-1-Food-Probe]] is food-safe stainless steel but is not dishwasher safe.

### Does the TEMP-1 have Bluetooth?

Yes. The TEMP-1 connects over Wi-Fi and also has Bluetooth.

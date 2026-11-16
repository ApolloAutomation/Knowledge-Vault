---
title: MTR-1
aliases: ["MTR 1", "Apollo MTR-1", "MTR1"]
type: product
audience: customer
source: https://apolloautomation.com/products/mtr-1
status: available
status_checked: 2026-11-15
power_source: [usb-c]
last_verified: 2026-11-15
---
# MTR-1

## Description

The MTR-1 is a multi-target radar multisensor for ESPHome that packs a diverse array of sensors into an affordable, compact package. It can measure multiple targets, zones, target coordinates, RGB, buzzer, LUX/UV and optional CO2. It is powered via USB-C and a standard wall plug, and uses Wi-Fi to connect to ESPHome on a Home Assistant install. Apollo offers the software and CAD drawings to the community.

## Features

- Multi-target, multi-zone mmWave radar (HLK-LD2450) that reports where people are, not just that someone is present (e.g. at the stove, sink, couch or bed)
- LUX and UV sensing (LTR-390UV)
- Optional CO2 sensor (SCD-40): pre-calibrated and ready to use; does not meet CO2 safety monitoring requirements per NBIC, NFPA or IFC
- Bluetooth tracker via the ESP32-C3-Mini (YAML config required)
- RGB pixel (RGB neopixel)
- Piezo buzzer with different beep patterns for different alerts
- Compact size, USB-C powered, Wi-Fi to ESPHome
- Back male USB-C adapter; some wall plugs and receptacles with smart charging do not work with it
- Open software and CAD files; Discord community

## Specs

- Battery life: N/A — USB-C powered, no battery
- Operating temperature: Unknown — escalate to support
- Waterproof: Unknown — escalate to support
- Power consumption awake: Unknown — escalate to support
- Power consumption sleeping: Unknown — escalate to support
- What battery works with it: N/A — USB-C powered, no battery

## Components

- [[LD2450]] - multi-target, multi-zone mmWave radar
- [[LTR390]] - LUX and UV light sensor
- [[ESP32-C3]] - microcontroller (ESP32-C3-Mini); Wi-Fi and Bluetooth tracking
- [[SCD40]] - optional CO2 sensor (With CO2 variant)

## Options and add-ons

- Variants: Base, With CO2
- Add-ons: articulating stand; mount (90-degree mount only, or 90-degree mount with US plug); USB-C charger (USA plug) and cable; back USB-C port; GPIO header

## What's in the box

- Assembled sensor with case
- Apollo sticker

## Common questions and answers

### My MTR-1 is not working when plugged into my wall plug with the back USB-C adapter. Why?

Some wall plugs and receptacles with smart charging do not work with the MTR-1's back male USB-C adapter. If yours is one of them, contact Apollo support for help choosing another way to power it.

### Can the MTR-1 tell where people are in a room?

Yes. Its multi-target, multi-zone LD2450 mmWave radar reports where people are, not just that someone is present, for example at the stove, sink, couch or bed. It can measure multiple targets, zones and target coordinates.

### Can I use the MTR-1 CO2 sensor as a safety alarm?

No. The optional SCD-40 CO2 sensor is pre-calibrated and ready to use, but it does not meet CO2 safety monitoring requirements per NBIC, NFPA or IFC.

### How do I track Bluetooth devices with the MTR-1?

The MTR-1 can act as a Bluetooth tracker through its ESP32-C3-Mini, but this requires YAML configuration in ESPHome.

### Which MTR-1 variants are there?

There are two: Base and With CO2.

### How does the MTR-1 connect to Home Assistant?

It uses Wi-Fi to connect to ESPHome on your Home Assistant install.

### Where can I get help or the source files for the MTR-1?

The software and CAD files are open, and community support is available on Discord.

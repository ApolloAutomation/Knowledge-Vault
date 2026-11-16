---
title: AIR-1
aliases: ["AIR 1", "Apollo AIR-1", "AIR1"]
type: product
audience: customer
source: https://apolloautomation.com/products/air-1
status: available
status_checked: 2026-11-15
power_source: [usb-c]
last_verified: 2026-11-16
---
# AIR-1

## Description

The AIR-1 is a compact, feature-rich, affordable and expandable air sensor for Home Assistant. It uses Wi-Fi and ESPHome, is controlled locally with no subscription or cloud, and is powered via USB-C and a wall adapter. It also integrates with platforms like Homey, Hubitat and HomeSeer. Apollo offers the software and CAD drawings to the community.

## Features

- SEN55 particulate sensor: PM1, PM2.5, PM4, PM10, VOC, NOx, temperature, humidity
- Optional CO2 sensor (SCD40), pre-calibrated. It does not meet CO2 safety monitoring requirements per NBIC, NFPA or IFC.
- Optional gas sensor (MiCS-4514 from DFRobot): CO, ethanol, H2, NO2, ammonia, methane. It behaves more as an exists/doesn't-exist indicator than an exact ppm readout. It does not meet gas safety monitoring requirements per NBIC, NFPA or IFC.
- Bluetooth tracker via the ESP32-C3-Mini (YAML config required)
- RGB pixels for color-coded alerts
- Power and sensor expansion connector for future sensors and power methods
- A temperature offset is needed because of heat from the ESP32-C3; the offset is user adjustable, and using the sleep function lowers the needed offset
- Open software and CAD files

## Specs

- Temperature offset: Needed due to heat buildup from the ESP32-C3; between 2 and 6 °C, user adjustable; much lower when using the Sleep function
- Battery life: N/A — USB-C powered, no battery
- Operating temperature: -40 to 85 °C (rating of the ESP32-C3-MINI-1 module)
- Waterproof: No — the AIR-1 is not waterproof
- Power consumption awake: Unknown — escalate to support
- Power consumption sleeping: Unknown — escalate to support
- What battery works with it: N/A — USB-C powered, no battery

## Components

- [[SEN55]] - particulate, VOC, NOx, temperature and humidity sensor
- [[SCD40]] - optional CO2 sensor
- [[MiCS-4514]] - optional multi-gas sensor
- [[ESP32-C3]] - microcontroller (ESP32-C3-Mini); Wi-Fi and Bluetooth tracking

## Options and add-ons

- Variants: no CO2 / no gas; with CO2 / no gas; with CO2 / with gas
- Add-ons: GPIO header; USB-C charger (USA plug) and/or cable

## What's in the box

- Assembled sensor with case
- Apollo sticker

## Common questions and answers

### Why does my AIR-1 read a higher temperature than my other thermometers?

Heat from the ESP32-C3 microcontroller builds up inside the AIR-1, so a temperature offset is needed. The offset is between 2 and 6 °C, and you can adjust it yourself. Using the Sleep function makes the needed offset much lower.

### Why do the gas readings (methane, CO, etc.) jump around or not match exact ppm values?

The optional MiCS-4514 gas sensor behaves more as an exists/doesn't-exist indicator than an exact ppm readout. Beta testers saw the methane reading spike when the sensor was exposed to high amounts of other gases. Use it to tell whether a gas is present rather than to read an exact concentration.

### Can I use the AIR-1 as a CO2 or gas safety alarm?

No. The optional CO2 sensor (SCD40) and the optional gas sensor (MiCS-4514) do not meet CO2 or gas safety monitoring requirements per NBIC, NFPA or IFC.

### Do I need to calibrate the CO2 sensor?

The optional SCD40 CO2 sensor comes pre-calibrated.

### How do I track Bluetooth devices with the AIR-1?

The AIR-1 can act as a Bluetooth tracker through its ESP32-C3-Mini, but this requires YAML configuration in ESPHome.

### Which variants of the AIR-1 are there?

There are three: no CO2 / no gas; with CO2 / no gas; and with CO2 / with gas. A GPIO header and a USB-C charger (USA plug) and/or cable are available as add-ons.

### Does the AIR-1 need the cloud or a subscription?

No. The AIR-1 is controlled locally over Wi-Fi with ESPHome, with no subscription or cloud. It works with Home Assistant and also integrates with Homey, Hubitat and HomeSeer.

### Does the AIR-1 run on batteries?

No. It is powered via USB-C and a wall adapter.

### Is the AIR-1 waterproof?

No. The AIR-1 is not waterproof.

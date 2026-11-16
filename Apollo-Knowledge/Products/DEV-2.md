---
title: DEV-2
aliases: ["Apollo DEV-2", "DEV2"]
type: product
audience: customer
source: https://apolloautomation.com/products/apollo-dev-2
status: available
status_checked: 2026-11-15
power_source: [usb-c]
last_verified: 2026-11-15
---
# DEV-2

## Description

The Apollo DEV-2 is a development board for prototyping and custom projects. It uses an ESP32-C6-MINI-1 chip with USB-C for power and data, GPIO, I2C and an RGB LED. Compared with the [[DEV-1]] it also supports Thread and Zigbee. It ships with pre-soldered headers. The DEV-2 does not come pre-flashed with ESPHome or WLED, so you flash it yourself.

## Features

- ESP32-C6-MINI-1 chip: WiFi, Thread, Zigbee and Bluetooth enabled
- USB-C for power and data
- GPIO and I2C interfaces for easy sensor integration
- Built-in RGB LED indicator on GPIO 3
- Pre-soldered headers
- Use cases: Home Assistant, IoT, automation solutions, prototyping and custom projects

## Specs

- Power input: USB-C, or back-fed through the 5V and G pins (use only one power source at a time)
- 3.3V pin output: up to 600 mA, of which the microcontroller itself uses 100-200 mA
- I2C pins: SDA on GPIO1, SCL on GPIO0
- UART pins: TX on GPIO16, RX on GPIO17
- ADC pins: GPIO0, GPIO1, GPIO2, GPIO4, GPIO5, GPIO6
- Onboard RGB LED: GPIO3
- Firmware: Not pre-flashed; you flash ESPHome or WLED yourself
- Battery life: N/A — USB-C powered, no battery
- Operating temperature: Unknown — escalate to support
- Waterproof: Unknown — escalate to support
- Power consumption awake: About 100-200 mA drawn by the microcontroller from the 3.3V rail; total board draw Unknown — escalate to support
- Power consumption sleeping: Unknown — escalate to support
- What battery works with it: N/A — USB-C powered, no battery

## Components

- [[ESP32-C6]] - the microcontroller (sold as the ESP32-C6-MINI-1 module); provides WiFi, Bluetooth, Thread and Zigbee

## Options and add-ons

Optional extras sold with the board:

- Breadboard and Dupont cables (breadboard only, Dupont cables only, or both)
- USB-C charger and cable (USA plug; charger only, cable only, or both)
- Breakout boards: SCD40 ([[SCD40]]), SEN55 ([[SEN55]]), or SEN55 and SCD40 together

Related board: [[DEV-1]] (ESP32-C3 version).

## What's in the box

- Apollo DEV-2 board
- Apollo sticker

## Common questions and answers

### Does the DEV-2 come with ESPHome already installed?

No. The DEV-2 does not come pre-flashed with ESPHome or WLED, so you flash it yourself. The getting-started video on the Apollo wiki was made for the DEV-1, but the steps are the same; use the DEV-2 YAML from https://wiki.apolloautomation.com/products/dev2/introduction/

### What is the difference between the DEV-1 and the DEV-2?

The DEV-2 uses an ESP32-C6-MINI-1 and supports WiFi, Bluetooth, Thread and Zigbee. The [[DEV-1]] uses an ESP32-C3-MINI-1 and supports WiFi and Bluetooth only. Their UART and ADC pins also differ (see Specs).

### Can I power the DEV-2 from USB-C and the 5V pin at the same time?

No. Use one power source at a time: either USB-C, or back-feed power through the 5V and G pins, but not both.

### How much current can I draw from the 3.3V pin?

The 3.3V pin supplies up to 600 mA, but the microcontroller itself uses 100-200 mA of that, so plan your sensors around the remainder.

### Which pins are I2C, UART and the RGB LED on the DEV-2?

I2C uses SDA on GPIO1 and SCL on GPIO0. UART uses TX on GPIO16 and RX on GPIO17. The onboard RGB LED is on GPIO3. ADC-capable pins are GPIO0, GPIO1, GPIO2, GPIO4, GPIO5 and GPIO6.

### Does the DEV-2 run on a battery?

No. The DEV-2 is powered over USB-C (or through its 5V and G pins) and has no battery.

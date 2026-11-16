---
title: DEV-1
aliases: ["Apollo DEV-1", "DEV1"]
type: product
audience: customer
source: https://apolloautomation.com/products/apollo-dev-1
status: available
status_checked: 2026-11-15
power_source: [usb-c]
last_verified: 2026-11-15
---
# DEV-1

## Description

The Apollo DEV-1 is a development board for prototyping and custom projects. It uses an ESP32-C3-MINI-1 chip with USB-C for power and data, GPIO, I2C and an RGB LED. It is aimed at Home Assistant, IoT and automation projects, and ships with pre-soldered headers. The DEV-1 does not come pre-flashed with ESPHome or WLED, so you flash it yourself. For a version with Thread and Zigbee support, see [[DEV-2]].

## Features

- ESP32-C3-MINI-1 chip (WiFi and Bluetooth enabled)
- USB-C for power and data
- GPIO and I2C interfaces for easy sensor integration
- Built-in RGB LED indicator on GPIO 3
- Pre-soldered headers
- Use cases: Home Assistant, IoT, automation solutions, prototyping and custom projects

## Specs

- Power input: USB-C, or back-fed through the 5V and G pins (use only one power source at a time)
- 3.3V pin output: up to 600 mA, of which the microcontroller itself uses 100-200 mA
- I2C pins: SDA on GPIO1, SCL on GPIO0
- UART pins: TX on GPIO21, RX on GPIO20 (115200 baud in the example; match it to the connected device)
- ADC pins: GPIO0, GPIO1, GPIO2, GPIO4
- Onboard RGB LED: GPIO3
- Firmware: Not pre-flashed; you flash ESPHome or WLED yourself
- Battery life: N/A — USB-C powered, no battery
- Operating temperature: Unknown — escalate to support
- Waterproof: Unknown — escalate to support
- Power consumption awake: About 100-200 mA drawn by the microcontroller from the 3.3V rail; total board draw Unknown — escalate to support
- Power consumption sleeping: Unknown — escalate to support
- What battery works with it: N/A — USB-C powered, no battery

## Components

- [[ESP32-C3]] - the microcontroller (sold as the ESP32-C3-MINI-1 module); provides WiFi and Bluetooth

## Options and add-ons

Optional extras sold with the board:

- Breadboard and Dupont cables (breadboard only, Dupont cables only, or both)
- USB-C charger (USA plug) and cable (charger only, cable only, or both)
- Breakout boards: SCD40 ([[SCD40]]), SEN55 ([[SEN55]]), or SEN55 and SCD40 together

Related board: [[DEV-2]] (ESP32-C6 version with Thread and Zigbee).

## What's in the box

- Apollo DEV-1 board
- Apollo sticker

## Common questions and answers

### Does the DEV-1 come with ESPHome already installed?

No. The DEV-1 does not come pre-flashed with ESPHome or WLED, so you flash it yourself. The Apollo wiki has a getting-started guide and example YAML: https://wiki.apolloautomation.com/products/dev1/introduction/

### Can I power the DEV-1 from USB-C and the 5V pin at the same time?

No. Use one power source at a time: either USB-C, or back-feed power through the 5V and G pins, but not both.

### How much current can I draw from the 3.3V pin?

The 3.3V pin supplies up to 600 mA, but the microcontroller itself uses 100-200 mA of that, so plan your sensors around the remainder.

### Which pins are I2C, UART and the RGB LED on the DEV-1?

I2C uses SDA on GPIO1 and SCL on GPIO0. UART uses TX on GPIO21 and RX on GPIO20. The onboard RGB LED is on GPIO3. ADC-capable pins are GPIO0, GPIO1, GPIO2 and GPIO4.

### Does the DEV-1 support Thread or Zigbee?

No. The DEV-1's ESP32-C3 provides WiFi and Bluetooth. If you need Thread or Zigbee, the [[DEV-2]] uses an ESP32-C6 that supports WiFi, Bluetooth, Thread and Zigbee.

### Does the DEV-1 run on a battery?

No. The DEV-1 is powered over USB-C (or through its 5V and G pins) and has no battery.

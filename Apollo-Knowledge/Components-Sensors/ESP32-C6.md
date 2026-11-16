---
title: ESP32-C6
aliases: ["ESP32-C6-MINI", "ESP32-C6-MINI-1"]
type: component
audience: customer
used_in: ["[[DEV-2]]", "[[ESPHome-C6-Board]]", "[[ESK-1]]", "[[NFC-1]]", "[[BTN-1]]", "[[Apollo-Breakout-Module]]", "[[PUMP-1]]"]
last_verified: 2026-11-15
---
# ESP32-C6

## Description

The Espressif ESP32-C6 is the microcontroller on several Apollo boards, where it is fitted as the ESP32-C6-MINI-1 module. It provides Wi-Fi, Bluetooth LE and Thread. Zigbee is enabled on the [[DEV-2]].

On the [[Apollo-Breakout-Module]], the C6 drives a shared I2C bus on GPIO0 (SCL) and GPIO1 (SDA) and 1-Wire on GPIO6. It powers the connectors from its controlled rail, which is off during sleep.

The [[NFC-1]] uses it with 8MB flash and a built-in Bluetooth proxy that can be switched on or off.

## Used in

- [[DEV-2]]
- [[ESPHome-C6-Board]]
- [[ESK-1]]
- [[NFC-1]]
- [[BTN-1]]
- [[Apollo-Breakout-Module]]
- [[PUMP-1]]

## Specs

- Operating range: -40 °C to +85 °C on the ESPHome-C6-Board. Other products: Unknown — escalate to support
- Wifi capability: Wi-Fi, plus Bluetooth LE and Thread; Zigbee enabled on the DEV-2
- Can be bluetooth proxy: Yes on the NFC-1 (built-in Bluetooth proxy that can be switched on or off)

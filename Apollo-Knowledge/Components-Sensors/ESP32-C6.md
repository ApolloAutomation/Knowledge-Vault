---
title: ESP32-C6
aliases: ["ESP32-C6-MINI", "ESP32-C6-MINI-1"]
type: component
audience: customer
used_in: ["[[DEV-2]]", "[[ESPHome-C6-Board]]", "[[ESK-1]]", "[[NFC-1]]", "[[BTN-1]]", "[[Apollo-Breakout-Module]]", "[[PUMP-1]]"]
last_verified: 2026-11-16
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

- Operating range: -40 to 85 °C (rating of the ESP32-C6-MINI-1 module; see Datasheet figures)
- Wifi capability: Wi-Fi, plus Bluetooth LE and Thread; Zigbee enabled on the DEV-2
- Can be bluetooth proxy: Yes on the NFC-1 (built-in Bluetooth proxy that can be switched on or off)

## Datasheet figures (chip manufacturer, not an Apollo rating)

Source: Espressif ESP32-C6-MINI-1 & MINI-1U Datasheet v1.5, Tables 1-1/1-2 and Recommended Operating Conditions (https://www.espressif.com/sites/default/files/documentation/esp32-c6-mini-1_mini-1u_datasheet_en.pdf)

- ESP32-C6-MINI-1 / MINI-1U, N4 variant (85 °C version): -40 to 85 °C ambient. This is the -40 to +85 °C range listed for the [[ESPHome-C6-Board]].
- ESP32-C6-MINI-1 / MINI-1U, H4 and H8 variants (105 °C version): -40 to 105 °C ambient

Source: Espressif ESP32-C6 Series Datasheet v1.6, Table 1-1 (https://www.espressif.com/sites/default/files/documentation/esp32-c6_datasheet_en.pdf)

- Bare chip, for reference: ESP32-C6, C6FH4 and C6FH8 are rated -40 to 105 °C. For a finished product, the module rating applies.

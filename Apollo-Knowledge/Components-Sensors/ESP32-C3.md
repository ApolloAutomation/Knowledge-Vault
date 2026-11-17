---
title: ESP32-C3
aliases: ["ESP32-C3-Mini", "ESP32-C3-MINI-1"]
type: component
audience: customer
used_in: ["[[MSR-2]]", "[[MTR-1]]", "[[AIR-1]]", "[[DEV-1]]", "[[PLT-1]]", "[[TEMP-1]]"]
last_verified: 2026-11-16
---
# ESP32-C3

## Description

The ESP32-C3 (also called the ESP32-C3-Mini) is the main microcontroller in several Apollo devices. The [[DEV-1]] uses the ESP32-C3-MINI-1 module, a Wi-Fi and Bluetooth-enabled chip.

On the [[MSR-2]], [[MTR-1]] and [[AIR-1]] it also provides Bluetooth tracking, which requires YAML configuration.

It is also the microcontroller in the [[PLT-1]] and [[TEMP-1]].

Heat from the ESP32-C3 causes a temperature offset on the AIR-1.

## Used in

- [[MSR-2]]
- [[MTR-1]]
- [[AIR-1]]
- [[DEV-1]]
- [[PLT-1]]
- [[TEMP-1]]

## Specs

- Operating range: -40 to 85 °C (rating of the ESP32-C3-MINI-1 module; see Datasheet figures)
- Wifi capability: Yes, Wi-Fi and Bluetooth (ESP32-C3-MINI-1 on the DEV-1)
- Can be bluetooth proxy: Unknown — escalate to support

## Datasheet figures (chip manufacturer, not an Apollo rating)

Source: Espressif ESP32-C3-MINI-1 & MINI-1U Datasheet v2.2, Tables 1-1/1-2 and Recommended Operating Conditions (https://www.espressif.com/sites/default/files/documentation/esp32-c3-mini-1_datasheet_en.pdf)

- ESP32-C3-MINI-1 / MINI-1U, N4 and N4X variants (85 °C version): -40 to 85 °C ambient
- ESP32-C3-MINI-1 / MINI-1U, H4, H4X, H8X and H4-AZ variants (105 °C version): -40 to 105 °C ambient
- The part-number suffix on the module marking sets the range. Ambient temperature is the environment immediately outside the module.

Source: Espressif ESP32-C3 Series Datasheet v2.5, Table 1-1 ESP32-C3 Series Comparison (https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf)

- Bare chip, for reference: ESP32-C3, C3FH4, C3FH4AZ, C3FH4X and C3FH8X are rated -40 to 105 °C; ESP32-C3FN4 (EOL) is rated -40 to 85 °C. For a finished product, the module rating applies.

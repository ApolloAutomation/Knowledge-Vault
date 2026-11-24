---
title: ESP32-S3
aliases: []
type: component
audience: customer
used_in: ["[[CAST-1]]", "[[CAST-PRO-1]]", "[[M-1]]", "[[R-PRO-1]]"]
last_verified: 2026-11-16
---
# ESP32-S3

## Description

The Espressif ESP32-S3 is the microcontroller on the [[CAST-1]] and [[CAST-PRO-1]] (CAST PRO-1) audio casting devices, and it is listed in the [[M-1]] LED matrix product details. The CAST-1 version has 16 MB flash and 8 MB PSRAM. The M-1 controller ships pre-flashed with WLED. It is also the microcontroller in the [[R-PRO-1]] (R PRO-1).

## Used in

- [[CAST-1]]
- [[CAST-PRO-1]]
- [[M-1]]
- M-1-Controller (the M-1's controller board)
- [[R-PRO-1]]

## Specs

- Operating range: -40 to 65 °C (most conservative ESP32-S3 module rating; other variants are rated to 85 °C or 105 °C, see Datasheet figures)
- Wifi capability: 2.4 GHz Wi-Fi (CAST-1 and CAST PRO-1)
- Can be bluetooth proxy: Yes. The CAST-1 is Home Assistant Bluetooth Proxy capable; the CAST PRO-1 uses Bluetooth LE for Bluetooth proxy and Improv Wi-Fi setup

## Datasheet figures (chip manufacturer, not an Apollo rating)

Source: Espressif ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8, Section 1.2, Tables 1-1/1-2 and Recommended Operating Conditions (https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf)

- ESP32-S3-WROOM-1 / WROOM-1U, N4, N8, N16, N4R2, N8R2 and N16R2 (no PSRAM or Quad-SPI PSRAM, 85 °C version): -40 to 85 °C ambient
- ESP32-S3-WROOM-1 / WROOM-1U, H4 (105 °C version, custom order only): -40 to 105 °C ambient
- ESP32-S3-WROOM-1 / WROOM-1U, N4R8, N8R8, N16R8 and N16R16VA (Octal PSRAM, 65 °C version): -40 to 65 °C ambient. With PSRAM ECC enabled, the maximum rises to 85 °C, but usable PSRAM shrinks by 1/16.

Source: Espressif ESP32-S3 Series Datasheet v2.2, Table 1-1 ESP32-S3 Series Comparison (https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf)

- Bare chip, for reference: ESP32-S3 (no in-package memory) and S3RH2 are rated -40 to 105 °C; S3FN8, S3FH4R2 and S3R2 (EOL) are rated -40 to 85 °C; S3R8, S3R16V and S3R8V (EOL) are rated -40 to 65 °C. For a finished product, the module rating applies.

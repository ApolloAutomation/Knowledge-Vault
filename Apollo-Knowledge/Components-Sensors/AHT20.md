---
title: AHT20
aliases: [AHT20-F, AHT20F]
type: component
audience: customer
used_in: ["[[PLT-1]]", "[[TEMP-1]]", "[[ESK-1]]"]
last_verified: 2026-11-16
---
# AHT20

## Description

The AHT20 is the onboard air temperature and humidity sensor. Apollo uses the AHT20-F variant (also written AHT20F), which is dust-protected. Heat from the ESP chip can affect its readings; the device sleep settings help keep readings accurate.

## Used in

- [[PLT-1]] - air temperature and humidity (AHT20-F)
- [[TEMP-1]] - onboard air temperature and humidity (AHT20-F)
- [[ESK-1]] - temperature and humidity sensor module (AHT20F)

## Specs

- Max/min temp reading: Unknown — escalate to support
- Max/min humidity reading: Unknown — escalate to support
- Accuracy (AHT20-F in ESK-1, PLT-1 and TEMP-1): ±0.3 °C, ±2% RH

## Datasheet figures (chip manufacturer, not an Apollo rating)

Source: Aosong Data Sheet AHT20 Humidity and Temperature Sensor, Version V1.0, May 2021 (https://www.aosong.com/userfiles/files/media/Data%20Sheet%20AHT20.pdf)

- Temperature accuracy: typ ±0.3 °C
- Humidity accuracy: typ ±2 %RH
- Temperature range: -40 to 85 °C
- Humidity range: 0–100 %RH (normal operating range 0–80 %RH)
- Supply voltage: 2.2–5.5 V
- Interface: I²C

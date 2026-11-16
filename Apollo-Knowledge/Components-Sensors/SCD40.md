---
title: SCD40
aliases: [SCD-40, Sensirion SCD40]
type: component
audience: customer
used_in: ["[[MSR-2]]", "[[MTR-1]]", "[[R-PRO-1]]", "[[AIR-1]]", "[[DEV-1]]", "[[DEV-2]]"]
last_verified: 2026-11-16
---
# SCD40

## Description

The SCD40 (SCD-40) is a true NDIR (non-dispersive infrared) CO2 sensor for indoor air quality monitoring. It is pre-calibrated and ready to use, has low power consumption, and gives real-time CO2 measurements. It connects over I2C. Apollo sells it as an add-on and on breakout boards, which give CO2 readings with integrated temperature and humidity compensation. It is optional on several Apollo products, for example on the optional mezzanine expansion board on the R PRO-1.

The SCD40 is not for CO2 safety monitoring and does not meet NBIC, NFPA or IFC CO2 safety monitoring requirements.

## Used in

- [[MSR-2]] - optional CO2 sensor (With CO2 variant)
- [[MTR-1]] - optional CO2 sensor (With CO2 variant)
- [[R-PRO-1]] - optional NDIR CO2 sensor on the mezzanine expansion board
- [[AIR-1]] - optional CO2 sensor
- [[DEV-1]] - optional breakout board
- [[DEV-2]] - optional breakout board
- SCD40-Breakout-Board
- SEN55-SCD40-Breakout-Board

## Specs

- Sensor type: True NDIR CO2
- Calibration: Pre-calibrated, ready to use
- Interface: I2C
- Breakout boards: CO2 readings with integrated temperature and humidity compensation
- Safety rating: Not for CO2 safety monitoring (does not meet NBIC, NFPA or IFC requirements)

## Datasheet figures (chip manufacturer, not an Apollo rating)

Source: Sensirion SCD4x Datasheet, Version 1.7, April 2025 (https://sensirion.com/media/documents/48C4B7FB/67FE0194/CD_DS_SCD4x_Datasheet_D1.pdf)

- CO2 accuracy (SCD40): ±(50 ppm + 5 % of reading) over 400–2000 ppm
- CO2 output range: 0–40,000 ppm
- Humidity accuracy: typ ±6 %RH (15–35 °C, 20–65 %RH); typ ±9 %RH over -10 to 60 °C
- Temperature accuracy: typ ±0.8 °C (15–35 °C); typ ±1.5 °C over -10 to 60 °C
- Supply voltage: 2.4–5.5 V
- Interface: I²C
- Average current: typ 15 mA at 3.3 V (periodic measurement every 5 s)
- Operating range: -10 to 60 °C, 0–95 %RH non-condensing
- Lifetime: more than 10 years

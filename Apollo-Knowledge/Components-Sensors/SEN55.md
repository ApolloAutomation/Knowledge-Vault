---
title: SEN55
aliases: [Sensirion SEN55]
type: component
audience: customer
used_in: ["[[AIR-1]]", "[[DEV-1]]", "[[DEV-2]]"]
last_verified: 2026-11-16
---
# SEN55

## Description

The SEN55 is the air quality sensor on the [[AIR-1]]. It is a high-precision environmental sensor that reports PM1, PM2.5, PM4, PM10, VOC, NOx, temperature and humidity. It is also offered on breakout boards for the [[DEV-1]] and [[DEV-2]]: the SEN55 Breakout Board, and the SEN55 plus SCD40 Breakout Board.

## Used in

- [[AIR-1]] - particulate, VOC, NOx, temperature and humidity sensor
- [[DEV-1]] - optional SEN55 Breakout Board or SEN55 plus SCD40 Breakout Board
- [[DEV-2]] - optional SEN55 Breakout Board or SEN55 plus SCD40 Breakout Board
- SEN55-SCD40-Breakout-Board

## Specs

- Measurements: PM1, PM2.5, PM4, PM10, VOC, NOx, temperature, humidity
- Breakout boards: SEN55 Breakout Board; SEN55 plus SCD40 Breakout Board (for DEV-1 and DEV-2)

## Datasheet figures (chip manufacturer, not an Apollo rating)

Source: Sensirion Datasheet SEN5x, Version 2 – D1, March 2022 (https://sensirion.com/media/documents/6791EFA0/62A1F68F/Sensirion_Datasheet_Environmental_Node_SEN5x.pdf). Sensirion lists the SEN55 as not recommended for new designs, with the [[SEN65]] as its successor.

- Temperature accuracy: typ ±0.45 °C, max ±0.7 °C (15–30 °C, 50 %RH)
- Humidity accuracy: typ ±4.5 %RH, max ±6 %RH (25 °C, 30–70 %RH)
- PM specified range: 0–1000 µg/m³ for PM1, PM2.5, PM4 and PM10
- PM precision (PM1, PM2.5): ±(5 µg/m³ + 5 % of reading) from 0–100 µg/m³, ±10 % of reading from 100–1000 µg/m³
- PM precision (PM4, PM10): ±25 µg/m³ from 0–100 µg/m³, ±25 % of reading from 100–1000 µg/m³
- VOC and NOx index range: 1–500
- Operating range: recommended 10–40 °C; absolute limits -10 to 50 °C
- Supply voltage: 4.5–5.5 V (typ 5.0 V)
- Lifetime: more than 10 years (24 h/day operation)

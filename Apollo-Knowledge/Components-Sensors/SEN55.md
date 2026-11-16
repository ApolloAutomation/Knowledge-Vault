---
title: SEN55
aliases: [Sensirion SEN55]
type: component
audience: customer
used_in: ["[[AIR-1]]", "[[DEV-1]]", "[[DEV-2]]"]
last_verified: 2026-11-15
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

Source: Sensirion SEN5x datasheet (Version 2, March 2022; SparkFun-hosted copy). Sensirion lists the SEN55 as not recommended for new designs, with the [[SEN65]] as its successor.

- Temperature accuracy: typ ±0.45 °C, max ±0.7 °C
- Humidity accuracy: typ ±4.5 %RH
- PM range: 0–1000 µg/m³ for PM1, PM2.5, PM4 and PM10 (same as the SEN65 datasheet)
- PM precision (PM1, PM2.5): ±(5 µg/m³ + 5 % of reading) up to 100 µg/m³, then ±10 %
- VOC and NOx index range: 1–500
- Operating range: -10 to 50 °C absolute (recommended 10–40 °C)
- Lifetime: >10 years

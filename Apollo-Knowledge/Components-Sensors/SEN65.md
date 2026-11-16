---
title: SEN65
aliases: [Sensirion SEN65, SEN65 air quality module]
type: component
audience: customer
used_in: ["[[ESK-1]]", "[[Apollo-Breakout-Module]]"]
last_verified: 2026-11-15
---
# SEN65

## Description

The SEN65 is an air quality sensing module sold as an optional add-on to the [[ESK-1]] Starter Kit. It requires the [[Apollo-Breakout-Module]], where it plugs into the dedicated SEN6x port. It is a sensing platform for particulate matter, relative humidity and temperature, VOC and NOx, and reports up to eight parameters: PM1, PM2.5, PM4, PM10, temperature, relative humidity, VOC Index and NOx Index. Its core is a miniaturized MEMS-based particulate matter sensing component, the SPS6x. It suits IAQ-standard applications such as RESET and the WELL Building Standard.

## Used in

- [[ESK-1]] - optional air quality module add-on (requires the Breakout Module)
- [[Apollo-Breakout-Module]] - plugs into the dedicated SEN6x port

## Specs

- Measurements: PM1, PM2.5, PM4, PM10, temperature, relative humidity, VOC Index, NOx Index (up to eight parameters)
- Particulate sensing core: SPS6x, MEMS-based
- Requires: [[Apollo-Breakout-Module]]
- Suitable standards: IAQ-standard applications such as RESET and WELL Building Standard
- What's in the box: SEN65 module and SEN65 cable

## Datasheet figures (chip manufacturer, not an Apollo rating)

Source: Sensirion SEN6x datasheet (D1 Version 1.0, Oct 2026)

- Temperature accuracy: typ ±0.45 °C, max ±0.7 °C (15–30 °C, 50 %RH)
- Humidity accuracy: typ ±4.5 %RH (range 0–100 %RH)
- PM range: 0–1000 µg/m³ for PM1, PM2.5, PM4 and PM10
- PM precision (PM1, PM2.5): ±(5 µg/m³ + 5 % of reading) up to 100 µg/m³, then ±10 %
- VOC and NOx index range: 1–500
- Operating range: recommended 10–40 °C; absolute short-term max/min -10 to 50 °C
- Lifetime: >10 years

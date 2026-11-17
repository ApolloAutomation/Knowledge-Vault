---
title: SEN65
aliases: [Sensirion SEN65, SEN65 air quality module]
type: component
audience: customer
used_in: ["[[ESK-1]]", "[[Apollo-Breakout-Module]]"]
last_verified: 2026-11-16
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

Source: Sensirion SEN6x Datasheet, D1 Version 1.0, October 2026 (https://sensirion.com/media/documents/FAFC548D/6AC50BC5/PS_DS_SEN6x.pdf)

- Temperature accuracy: typ ±0.45 °C, max ±0.7 °C (15–30 °C, 50 %RH)
- Humidity accuracy: typ ±4.5 %RH, max ±6 %RH (25 °C, 30–70 %RH)
- PM specified range: 0–1000 µg/m³ for PM1, PM2.5, PM4 and PM10 (output range 0–6000 µg/m³)
- PM precision (PM1, PM2.5): ±(5 µg/m³ + 5 % of reading) from 0–100 µg/m³, ±10 % of reading from 100–1000 µg/m³
- PM precision (PM4, PM10): ±25 µg/m³ from 0–100 µg/m³, ±25 % of reading from 100–1000 µg/m³
- VOC and NOx index range: 1–500
- Operating range: recommended 10–40 °C, 20–80 %RH; short-term limits -10 to 50 °C, 0–90 %RH non-condensing
- Supply voltage: 3.15–3.6 V (typ 3.3 V)
- Lifetime: at least 10 years (24 h/day indoor operation)
